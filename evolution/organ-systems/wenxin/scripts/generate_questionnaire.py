#!/usr/bin/env python3
"""
问心 · 动态问卷生成器
====================

用于「路径 B」（用户无素材）入口。根据用户已经回答的内容，动态生成下一组问题。

设计理念：
- 不一次性给所有问题（会让用户疲惫）
- 根据初步回答的"信号特征"决定下一轮问什么
- 4 轮以内必须收集到足够锚点 + 信号，否则结束问卷

用法：
    python generate_questionnaire.py --round 1
    python generate_questionnaire.py --round 2 --previous-answers answers.json
    python generate_questionnaire.py --round 3 --previous-answers answers.json
    python generate_questionnaire.py --round 4 --previous-answers answers.json

输出：JSON 格式的下一组问题。

Note: 这个脚本是辅助工具。Claude 读取 references/questionnaire_bank.md 后
也可以**手动**实现同样的逻辑——脚本只是把这个逻辑代码化、可复用。
"""

import json
import argparse
import sys
from pathlib import Path


# ============== 题库 ==============

ROUND_1_OPENERS = {
    "time_allocation": [
        "你最近一次熬夜是为了什么？（不限定工作 / 兴趣 / 个人）",
        "周末通常你怎么过？哪种活动你做的时候完全感觉不到时间？",
        "通勤路上你看什么？（公众号 / 视频 / 播客 / 书 / 发呆）",
    ],
    "help_flow": [
        "你的朋友 / 同事来找你帮忙时，最常求你帮的是哪一类事？",
        "你最近被求助的一次是什么？",
    ],
    "looking_back": [
        "过去 5 年里，哪一段你回头看会**眼睛发光**？",
        "哪一段你**不太愿意提起**？（不答也是信息）",
    ],
    "trigger": [
        "你最近一次在工作里**特别有成就感**是什么时候？发生了什么？",
        "你最近一次在工作里**特别想离职**是什么时候？",
    ],
}


ROUND_2_BRANCHES = {
    # 用户已经在做某件具体的事 → 项目深化
    "project_deepening": [
        "你刚才说的 [具体事件]，能展开讲讲吗？",
        "那件事里你具体做了什么？（不是 title，是动作）",
        "那件事最后结果怎样？",
        "那件事换一个人来做，能做出来吗？",
    ],
    # 用户答得空洞模糊 → 换框架
    "reframe": [
        "不说工作。**业余时间**你最投入的事情是什么？",
        "你父母 / 朋友会怎么向**别人**介绍你？",
        "你做过最不像 [用户自己贴的标签] 的一件事是什么？",
        "如果让你**不挣钱**做一件事一年，你会做什么？",
    ],
    # 用户精神状态压力大 → 减压
    "destress": [
        "不用着急。我们慢慢来——你不需要现在就证明任何事。",
        "我换个问法：**最近一次你帮别人解决了一个问题、对方很感谢你**——是什么事？",
        "**你哪种事做得比身边人都轻松**？（不一定是大事，可能是\"会修电脑\"、\"会查机票\"、\"会写邮件\"）",
    ],
}


ROUND_3_TEXTURE = {
    # CCI 改编题（5 选 2-3）
    "cci": [
        "童年时期你最崇拜的 3 个人是谁？为什么崇拜 ta 们？",
        "你最喜欢看的杂志/电视/网站/账号是什么？",
        "你最喜欢的故事/电影/书是什么？讲一下情节。",
        "你最喜欢的座右铭/格言是什么？",
        "你最早的 3 个童年记忆是什么？",
    ],
    # 价值观触发题
    "values": [
        "你拒绝过哪些\"看起来好的机会\"？为什么？",
        "你最嫉妒哪一类人？为什么？",
        "你最讨厌哪种工作方式 / 同事 / 任务？",
    ],
}


# ============== 信号检测 ==============

def detect_signals(previous_answers: dict) -> dict:
    """
    分析用户已经回答的内容，提取信号特征。

    返回：
        {
            "concrete_events": int,    # 提到的具体事件数
            "behavior_signals": int,    # 给出的行为信号数
            "stress_indicators": bool, # 是否表现出心理压力
            "vague_answers": bool,     # 是否答得空洞
            "self_labels": list,       # 用户给自己贴的标签（用于 unique outcomes）
        }

    Note: 这个函数是简化版——真正的实现需要 LLM 来判断。
    Claude 调用此脚本时应根据上下文手动判断这些信号。
    """
    text = " ".join(str(v) for v in previous_answers.values())
    text_lower = text.lower()

    signals = {
        "concrete_events": 0,
        "behavior_signals": 0,
        "stress_indicators": False,
        "vague_answers": False,
        "self_labels": [],
    }

    # 简化的检测逻辑（真实实现应由 LLM 判断）
    stress_keywords = ["迷茫", "焦虑", "什么都不会", "不知道自己", "没什么", "普通", "平庸"]
    if any(k in text for k in stress_keywords):
        signals["stress_indicators"] = True

    vague_keywords = ["还行", "就那样", "正常吧", "一般", "没什么特别"]
    if any(k in text for k in vague_keywords) and len(text) < 200:
        signals["vague_answers"] = True

    label_patterns = ["普通打工人", "普通人", "小镇做题家", "学渣", "废物", "没用的人"]
    for pattern in label_patterns:
        if pattern in text:
            signals["self_labels"].append(pattern)

    # 这些计数需要更智能的判断，简化版只是占位
    if len(text) > 300:
        signals["behavior_signals"] = 3  # 占位

    return signals


# ============== 路由逻辑 ==============

def select_questions(round_num: int, previous_answers: dict = None) -> dict:
    """
    根据轮次和之前的回答，选择下一组问题。

    返回：
        {
            "round": int,
            "questions": list[str],
            "guidance": str,        # 给 Claude 的指引
            "should_terminate": bool,  # 是否该结束问卷
        }
    """
    if round_num == 1:
        # Round 1: 必问开场
        questions = (
            ROUND_1_OPENERS["time_allocation"][:1]
            + ROUND_1_OPENERS["help_flow"][:1]
            + ROUND_1_OPENERS["looking_back"][:1]
        )
        return {
            "round": 1,
            "questions": questions,
            "guidance": "开场题。挑 3 个用户最容易回答的问题。注意观察用户回答的'温度'——是激动地展开还是简短地回避。",
            "should_terminate": False,
        }

    if round_num >= 2 and previous_answers is None:
        return {
            "round": round_num,
            "questions": [],
            "guidance": "Round 2+ 需要 previous_answers 才能动态选题。",
            "should_terminate": True,
        }

    signals = detect_signals(previous_answers)

    if round_num == 2:
        if signals["stress_indicators"]:
            questions = ROUND_2_BRANCHES["destress"]
            branch = "destress"
        elif signals["vague_answers"]:
            questions = ROUND_2_BRANCHES["reframe"]
            branch = "reframe"
        else:
            questions = ROUND_2_BRANCHES["project_deepening"]
            branch = "project_deepening"

        return {
            "round": 2,
            "questions": questions[:3],  # 只取前 3 个，不要一次性全问
            "guidance": f"Round 2 走的是 '{branch}' 分支。如果用户给了具体事件，主动接住继续追问。",
            "should_terminate": False,
        }

    if round_num == 3:
        # 是否已经收集够了？
        if signals["concrete_events"] >= 2 and signals["behavior_signals"] >= 3:
            return {
                "round": 3,
                "questions": [],
                "guidance": "已经收集到足够锚点和信号。**直接转入阶段 1**——不需要再问了。",
                "should_terminate": True,
            }

        # 还没够，加质地题
        questions = ROUND_3_TEXTURE["cci"][:2] + ROUND_3_TEXTURE["values"][:1]
        return {
            "round": 3,
            "questions": questions,
            "guidance": "Round 3 加质地题。这一轮的目标是从'做了什么'转向'是怎样的人'。",
            "should_terminate": False,
        }

    if round_num >= 4:
        # 第 4 轮还没够，要诚实告诉用户
        return {
            "round": 4,
            "questions": [],
            "guidance": (
                "4 轮后仍未收集到足够锚点。**直接告诉用户**：\n\n"
                "「我感觉我们现在的信息还不够构建一个有质感的画像。"
                "这不是你的问题——可能是我问的方式没打到你的点。"
                "要不你试试这样：找一个你信任的人，让 ta 用 5 分钟告诉你 ta 觉得你是怎样的人。"
                "然后把 ta 的描述告诉我。**外部视角往往能照出我们自己看不见的东西**。」"
            ),
            "should_terminate": True,
        }


# ============== 主入口 ==============

def main():
    parser = argparse.ArgumentParser(description="问心 · 动态问卷生成器")
    parser.add_argument("--round", type=int, required=True, help="当前轮次（1-4）")
    parser.add_argument(
        "--previous-answers",
        type=str,
        help="JSON 文件路径，包含之前轮次的回答",
    )
    args = parser.parse_args()

    previous_answers = None
    if args.previous_answers:
        path = Path(args.previous_answers)
        if path.exists():
            previous_answers = json.loads(path.read_text(encoding="utf-8"))
        else:
            print(f"Warning: {path} not found", file=sys.stderr)

    result = select_questions(args.round, previous_answers)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
