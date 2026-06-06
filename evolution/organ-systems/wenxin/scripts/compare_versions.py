#!/usr/bin/env python3
"""
compare_versions.py · 对比两份 WENXIN_REPORT.md 生成 compare.html

用法：
    python compare_versions.py archive/2026-05-03.md WENXIN_REPORT.md public/compare.html

读两份报告，diff 各段，生成视觉化对比页。
"""

import sys
import re
import os
from pathlib import Path
from datetime import datetime


def parse_frontmatter(content):
    """提取 frontmatter"""
    if not content.startswith('---'):
        return {}, content
    end = content.find('---', 3)
    if end == -1:
        return {}, content
    fm_text = content[3:end].strip()
    body = content[end+3:].lstrip('\n')
    fm = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return fm, body


def parse_sections(body):
    """按 ## 段落标题切分"""
    sections = {}
    current = None
    buf = []
    for line in body.split('\n'):
        if line.startswith('## ') and not line.startswith('### '):
            if current:
                sections[current] = '\n'.join(buf).strip()
            current = line[3:].strip()
            buf = []
        else:
            buf.append(line)
    if current:
        sections[current] = '\n'.join(buf).strip()
    return sections


def parse_radar_table(radar_text):
    """从雷达图段落提取 {维度: 水位%}"""
    radar = {}
    for line in radar_text.split('\n'):
        if line.startswith('|') and '%' in line:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if len(cells) >= 3:
                dim = cells[0]
                pct_match = re.search(r'(\d+)%', cells[2])
                if pct_match and dim != '维度':
                    radar[dim] = int(pct_match.group(1))
    return radar


def parse_nickname(identity_text):
    """从身份层段落提取外号"""
    for line in identity_text.split('\n'):
        m = re.match(r'-\s*外号-接地气版[:：]\s*(.+)', line)
        if m:
            return m.group(1).strip()
    return None


def parse_milestones(milestones_text):
    """提取里程碑列表"""
    items = []
    for line in milestones_text.split('\n'):
        line = line.strip()
        if line.startswith('- '):
            items.append(line[2:].strip())
    return items


def diff_radar(old, new):
    """对比雷达图"""
    diffs = []
    all_dims = set(old.keys()) | set(new.keys())
    for dim in all_dims:
        old_val = old.get(dim)
        new_val = new.get(dim)
        if old_val is None:
            diffs.append((dim, None, new_val, 'added'))
        elif new_val is None:
            diffs.append((dim, old_val, None, 'removed'))
        elif old_val != new_val:
            change = new_val - old_val
            direction = 'up' if change > 0 else 'down'
            diffs.append((dim, old_val, new_val, direction, change))
        else:
            diffs.append((dim, old_val, new_val, 'same'))
    # 排序：变化大的在前
    diffs.sort(key=lambda d: abs(d[4]) if len(d) > 4 else 0, reverse=True)
    return diffs


def render_html(old_fm, new_fm, old_sections, new_sections, output_path):
    """渲染对比 HTML"""
    old_radar = parse_radar_table(old_sections.get('雷达图', ''))
    new_radar = parse_radar_table(new_sections.get('雷达图', ''))
    old_nick = parse_nickname(old_sections.get('身份层', '')) or old_fm.get('nickname', '?')
    new_nick = parse_nickname(new_sections.get('身份层', '')) or new_fm.get('nickname', '?')
    old_milestones = parse_milestones(old_sections.get('里程碑', ''))
    new_milestones = parse_milestones(new_sections.get('里程碑', ''))
    new_only_milestones = [m for m in new_milestones if m not in old_milestones]

    radar_diffs = diff_radar(old_radar, new_radar)

    old_date = old_fm.get('last_updated', old_fm.get('generated_at', '?'))
    new_date = new_fm.get('last_updated', new_fm.get('generated_at', '?'))

    # 生成雷达图 diff 行
    diff_rows_html = []
    for d in radar_diffs:
        if d[3] == 'same':
            diff_rows_html.append(f'<tr class="same"><td>↔️</td><td>{d[0]}</td><td>{d[1]}%</td><td>{d[2]}%</td><td>持平</td></tr>')
        elif d[3] == 'up':
            diff_rows_html.append(f'<tr class="up"><td>⬆️</td><td>{d[0]}</td><td>{d[1]}%</td><td>{d[2]}%</td><td>+{d[4]}%</td></tr>')
        elif d[3] == 'down':
            diff_rows_html.append(f'<tr class="down"><td>⬇️</td><td>{d[0]}</td><td>{d[1]}%</td><td>{d[2]}%</td><td>{d[4]}%</td></tr>')
        elif d[3] == 'added':
            diff_rows_html.append(f'<tr class="added"><td>🆕</td><td>{d[0]}</td><td>—</td><td>{d[2]}%</td><td>新增维度</td></tr>')
        elif d[3] == 'removed':
            diff_rows_html.append(f'<tr class="removed"><td>❌</td><td>{d[0]}</td><td>{d[1]}%</td><td>—</td><td>移除维度</td></tr>')

    new_milestones_html = '\n'.join(f'<li>{m}</li>' for m in new_only_milestones) if new_only_milestones else '<li class="empty">（无新增）</li>'

    nickname_change_html = f'<div class="nickname-change"><span class="old-nick">{old_nick}</span> <span class="arrow">→</span> <span class="new-nick">{new_nick}</span></div>' if old_nick != new_nick else f'<div class="nickname-same">外号保持: <strong>{new_nick}</strong></div>'

    html = f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>InnerAtlas（问心）· 进展对比 {old_date} → {new_date}</title>
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Microsoft YaHei", sans-serif;
    color: #1a1a1a;
    background: #fafafa;
    line-height: 1.7;
  }}
  .container {{ max-width: 820px; margin: 0 auto; padding: 60px 32px 80px; }}

  .header {{
    text-align: center;
    padding: 40px 0;
    border-bottom: 1px solid #e8e8e8;
    margin-bottom: 50px;
  }}
  .header .label {{
    display: inline-block;
    font-size: 12px;
    color: #999;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    margin-bottom: 16px;
    padding: 6px 14px;
    border: 1px solid #ddd;
    border-radius: 20px;
  }}
  .header h1 {{
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 12px;
  }}
  .header .dates {{
    color: #888;
    font-size: 16px;
  }}
  .header .dates .arrow {{ margin: 0 12px; color: #4a90e2; font-weight: 700; }}

  h2 {{
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #999;
    margin: 50px 0 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid #eee;
  }}

  .nickname-change, .nickname-same {{
    background: white;
    padding: 24px 28px;
    border-radius: 12px;
    text-align: center;
    margin: 24px 0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    font-size: 22px;
  }}
  .nickname-change .old-nick {{
    color: #888;
    text-decoration: line-through;
  }}
  .nickname-change .arrow {{
    margin: 0 16px;
    color: #4a90e2;
    font-weight: 700;
  }}
  .nickname-change .new-nick {{
    color: #1a1a1a;
    font-weight: 800;
  }}

  .radar-diff {{
    background: white;
    border-radius: 12px;
    padding: 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    margin: 24px 0;
  }}
  table {{
    width: 100%;
    border-collapse: collapse;
  }}
  th {{
    background: #f5f5f7;
    padding: 12px 14px;
    text-align: left;
    font-weight: 600;
    color: #666;
    font-size: 12px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
  }}
  td {{
    padding: 12px 14px;
    border-bottom: 1px solid #f0f0f0;
  }}
  td:first-child {{ width: 60px; text-align: center; font-size: 18px; }}
  tr.up td:nth-child(2), tr.up td:nth-child(5) {{ color: #52c41a; font-weight: 600; }}
  tr.down td:nth-child(2), tr.down td:nth-child(5) {{ color: #f5222d; font-weight: 600; }}
  tr.added td:nth-child(2) {{ color: #4a90e2; font-weight: 600; }}
  tr.removed td:nth-child(2) {{ color: #888; font-weight: 600; }}
  tr.same {{ color: #888; }}

  .milestones {{
    background: white;
    border-radius: 12px;
    padding: 24px 28px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    margin: 24px 0;
  }}
  .milestones ul {{
    list-style: none;
    padding-left: 0;
  }}
  .milestones li {{
    padding: 10px 0;
    border-bottom: 1px solid #f5f5f7;
    color: #333;
  }}
  .milestones li:last-child {{ border-bottom: none; }}
  .milestones li.empty {{ color: #aaa; font-style: italic; }}
  .milestones li::before {{ content: "🆕 "; }}
  .milestones li.empty::before {{ content: ""; }}

  footer {{
    margin-top: 60px;
    padding: 32px 0;
    border-top: 1px solid #e8e8e8;
    text-align: center;
    color: #888;
    font-size: 14px;
  }}
  footer .links {{
    margin-top: 16px;
  }}
  footer a {{
    color: #4a90e2;
    text-decoration: none;
    margin: 0 12px;
  }}
  footer a:hover {{ text-decoration: underline; }}

  @media (max-width: 600px) {{
    .container {{ padding: 40px 20px 60px; }}
    .header h1 {{ font-size: 28px; }}
    .nickname-change, .nickname-same {{ font-size: 18px; }}
  }}
</style>
</head>
<body>
<div class="container">

<div class="header">
  <div class="label">InnerAtlas（问心）· 进展对比</div>
  <h1>你的成长记录</h1>
  <div class="dates">
    <span>{old_date}</span>
    <span class="arrow">→</span>
    <span>{new_date}</span>
  </div>
</div>

<h2>外号变化</h2>
{nickname_change_html}

<h2>雷达图维度变化</h2>
<div class="radar-diff">
  <table>
    <thead>
      <tr><th></th><th>维度</th><th>之前</th><th>现在</th><th>变化</th></tr>
    </thead>
    <tbody>
      {''.join(diff_rows_html)}
    </tbody>
  </table>
</div>

<h2>新增里程碑</h2>
<div class="milestones">
  <ul>
    {new_milestones_html}
  </ul>
</div>

<footer>
  <p>由 InnerAtlas（问心）生成 · {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
  <div class="links">
    <a href="/">← 个人网站首页</a>
    <a href="/report.html">完整问心报告 →</a>
  </div>
</footer>

</div>
</body>
</html>
"""

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ 对比页生成: {output_path}")


def main():
    if len(sys.argv) < 4:
        print("用法: python compare_versions.py <旧版> <新版> <输出 HTML>")
        print("例: python compare_versions.py archive/2026-05.md WENXIN_REPORT.md public/compare.html")
        sys.exit(1)

    old_path, new_path, output_path = sys.argv[1], sys.argv[2], sys.argv[3]

    if not os.path.exists(old_path):
        print(f"❌ 找不到旧版: {old_path}")
        sys.exit(1)
    if not os.path.exists(new_path):
        print(f"❌ 找不到新版: {new_path}")
        sys.exit(1)

    with open(old_path, 'r', encoding='utf-8') as f:
        old_content = f.read()
    with open(new_path, 'r', encoding='utf-8') as f:
        new_content = f.read()

    old_fm, old_body = parse_frontmatter(old_content)
    new_fm, new_body = parse_frontmatter(new_content)
    old_sections = parse_sections(old_body)
    new_sections = parse_sections(new_body)

    render_html(old_fm, new_fm, old_sections, new_sections, output_path)


if __name__ == '__main__':
    main()
