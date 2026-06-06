# InnerAtlas Interaction Templates

Use these templates to keep complete mode stable. Ask one primary question per turn unless the user asks for batch mode.

## Mode Choice

```text
你想用哪种模式？

A. 快速模式
我基于你已经给的全部原始输入直接推理并生成 WENXIN_REPORT.xml。所有猜测都会写明猜测依据。doctor 不到 100% 时，我只补问缺失项。

B. 完整模式
我先基于输入尽量推理所有方面，然后围绕矛盾点、异常点、重点产出点和确认点继续交互。只有 doctor 到 100% 才算完成。
```

## State Update

```text
当前状态：{workflow_state}
当前 completion：{completion_percent}%
已完成：{done}
还缺：{missing}
下一步只处理：{next_focus}
```

## Contradiction

```text
我看到一个矛盾点：
- A 信号：{signal_a}
- B 信号：{signal_b}
- 影响字段：{target_field}

我的当前假设是：{hypothesis}
这个假设如果错了，会影响 {impact}。

哪一种更接近真实情况？
```

## Anomaly

```text
这里有一个异常点：
- 异常信号：{signal}
- 为什么异常：{why_unusual}
- 我的解释假设：{hypothesis}

这是偶然事件、长期模式，还是我误读了？
```

## Key Output Confirmation

```text
我要确认一个重点产出字段：{target_field}

当前写法：{current_value}
依据：{evidence}
风险：{risk_if_wrong}

你会保留、下调、改写，还是标成证据不足？
```

## Simulated Scenario

```text
我想用一个类似场景确认判断：

假设 {scenario}
你第一反应会怎么判断？
你会先看什么信息？
你会怎么行动？

这个回答会用于确认：{target_field}
```

## Doctor Follow-up

```text
doctor 还没到 100%，现在缺的是：{missing_field}
为什么需要：{why_needed}

我只问一个问题：
{next_question}
```
