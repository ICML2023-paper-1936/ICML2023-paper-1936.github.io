#!/usr/bin/env python3
"""Rebuild this static academic homepage. Python standard library only."""
import json, html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PAPERS=json.loads((ROOT/'data/publications.json').read_text())
esc=html.escape
SCHOLAR='https://scholar.google.com/citations?user=YOOlkJoAAAAJ&hl=en'
OFFICIAL='https://iair.xjtu.edu.cn/info/1046/3904.htm'
TEAM='https://gr.xjtu.edu.cn/zeuslan/zh_CN/zdylm/1067873/list/index.htm'
FAVICON='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 64 64%22%3E%3Crect width=%2264%22 height=%2264%22 rx=%226%22 fill=%22%2328568d%22/%3E%3Ctext x=%2232%22 y=%2245%22 text-anchor=%22middle%22 font-family=%22Georgia,serif%22 font-size=%2236%22 fill=%22white%22%3EZL%3C/text%3E%3C/svg%3E'
def paper(p):
 authors=esc(p['authors']).replace('Zeyang Liu','<strong>Zeyang Liu</strong>').replace('刘泽阳','<strong>刘泽阳</strong>')
 links=''.join(f'<a href="{esc(url,quote=True)}">[{esc(label)}]</a>' for label,url in p.get('links',{}).items())
 return f'''<li><a class="paper-title" href="{esc(p['url'],quote=True)}">{esc(p['title'])}</a><p class="authors">{authors}</p><p class="venue"><strong>{esc(p['short_venue'])}</strong> · {p['year']}<span> — {esc(p['venue'])}</span></p><div class="paper-links">{links}</div></li>'''
def layout(body,zh=False,pub=False):
 home='zh.html' if zh else 'index.html'; pubs='publications-zh.html' if zh else 'publications.html'
 other=('publications.html' if zh else 'publications-zh.html') if pub else ('index.html' if zh else 'zh.html')
 labels=['首页','研究方向','论文发表','科研项目','联系方式'] if zh else ['Home','Research','Publications','Research Support','Contact']
 paths=[home,home+'#research',pubs,home+'#support',home+'#contact']
 nav=''.join(f'<a href="{u}"'+(' aria-current="page"' if i==(2 if pub else 0) else '')+f'>{l}</a>' for i,(u,l) in enumerate(zip(paths,labels)))
 title=('论文发表 | ' if zh else 'Publications | ') if pub else ''
 description='刘泽阳，西安交通大学人工智能学院助理教授。研究方向包括多智能体强化学习、具身智能与机器人自主决策。' if zh else 'Zeyang Liu is an Assistant Professor at the School of Artificial Intelligence, Xi’an Jiaotong University, working on multi-agent reinforcement learning, embodied AI, and autonomous robot decision-making.'
 return f'''<!doctype html>
<html lang="{'zh-CN' if zh else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}Zeyang Liu · 刘泽阳 | Xi’an Jiaotong University</title><meta name="description" content="{description}"><meta name="color-scheme" content="light"><meta property="og:type" content="website"><meta property="og:title" content="Zeyang Liu · 刘泽阳 | Xi’an Jiaotong University"><meta property="og:description" content="{description}"><link rel="icon" type="image/svg+xml" href="{FAVICON}"><link rel="stylesheet" href="assets/style.css"><link rel="alternate" hreflang="{'en' if zh else 'zh-CN'}" href="{other}"></head>
<body><a class="skip" href="#main">{'跳至正文' if zh else 'Skip to content'}</a><div class="shell"><aside class="sidebar"><div class="side-inner"><a class="brand" href="{home}">Zeyang Liu</a><p class="side-affiliation">XJTU · ARTIFICIAL INTELLIGENCE</p><div class="menu-label">{'导航' if zh else 'Menu'}</div><nav class="nav" aria-label="{'主导航' if zh else 'Main navigation'}">{nav}</nav><div class="sidebar-bottom"><a href="{SCHOLAR}">Google Scholar</a><a href="{OFFICIAL}">{'学院主页' if zh else 'Faculty Profile'}</a><a href="{TEAM}">{'研究团队' if zh else 'Research Group'}</a></div></div></aside>
<main id="main"><header class="titlebar"><h1>{('论文发表' if zh else 'Publications') if pub else 'Zeyang Liu <span class="cn" lang="zh-CN">刘泽阳</span>'}</h1><a class="lang" href="{other}" lang="{'en' if zh else 'zh-CN'}">{'English' if zh else '中文'}</a></header>{body}<footer><span>© 2026 Zeyang Liu · {'西安交通大学' if zh else 'Xi’an Jiaotong University'}</span><span>{'更新于 2026年9月' if zh else 'Updated September 2026'}</span><a class="back-top" href="#main">{'返回顶部' if zh else 'Back to top'}</a></footer></main></div></body></html>'''
def homepage(zh=False):
 pubs='publications-zh.html' if zh else 'publications.html'
 portrait='<img class="portrait" src="assets/portrait.jpg" alt="刘泽阳 / Zeyang Liu" width="174" height="218">'
 profile=f'''<section class="profile" aria-label="{'个人信息' if zh else 'Profile'}">{portrait}<div class="profile-copy"><p class="position">{'助理教授' if zh else 'Assistant Professor'}</p><p class="affiliation"><a href="https://iair.xjtu.edu.cn/">{'人工智能学院' if zh else 'School of Artificial Intelligence'}</a><br><a href="https://www.xjtu.edu.cn/">{'西安交通大学' if zh else 'Xi’an Jiaotong University'}</a></p><p class="contactline"><a href="mailto:zeyang.liu@xjtu.edu.cn">zeyang.liu@xjtu.edu.cn</a></p><div class="profile-links"><a href="https://github.com/ICML2023-paper-1936">[GitHub]</a><a href="{SCHOLAR}">[Google Scholar]</a><a href="{OFFICIAL}">[{'学院主页' if zh else 'Faculty Profile'}]</a><a href="{TEAM}">[{'研究团队' if zh else 'Research Group'}]</a></div></div></section>'''
 if zh:
  about='''<section id="about"><h2>个人简介</h2><p>我是西安交通大学人工智能学院助理教授、博士，入选西安交通大学青年优秀人才计划。研究方向包括多智能体系统、强化学习、具身智能与机器人自主决策。</p><p>我的研究围绕智能体如何学习协同、利用模型进行推理，以及在复杂环境中自主决策展开，关注从多智能体强化学习的方法研究到具身智能与机器人任务的应用。</p></section>'''
  research='''<section id="research"><h2>研究方向</h2><ul class="research-list"><li><strong>多智能体强化学习</strong>：协作决策、价值分解、动态协作图与高效探索。</li><li><strong>世界模型与具身智能</strong>：基于模型的推理、环境交互与机器人任务规划。</li><li><strong>机器人自主决策</strong>：离线强化学习、长时任务规划与策略泛化。</li></ul></section>'''
  support='''<section id="support"><h2>科研项目</h2><p>主持或负责以下类别的研究项目：</p><ul class="funding"><li>国家自然科学基金青年项目</li><li>国家重点研发计划子课题</li><li>国家地方共建人形机器人创新中心开放基金</li></ul></section>'''
  contact='''<section id="contact"><h2>联系方式</h2><p class="contact-block"><a href="mailto:zeyang.liu@xjtu.edu.cn">zeyang.liu@xjtu.edu.cn</a><br>西安交通大学人工智能学院<br>中国 · 陕西 · 西安</p></section>'''
 else:
  about='''<section id="about"><h2>About me</h2><p>I am an Assistant Professor at the <a href="https://iair.xjtu.edu.cn/">School of Artificial Intelligence</a>, <a href="https://www.xjtu.edu.cn/">Xi’an Jiaotong University</a>, where I was selected for the university’s Young Talent Program.</p><p>My research focuses on <strong>multi-agent reinforcement learning, embodied intelligence, and autonomous robot decision-making</strong>. I study how agents learn to cooperate, reason with models, and make decisions in complex environments, connecting learning algorithms with embodied tasks.</p></section>'''
  research='''<section id="research"><h2>Research</h2><ul class="research-list"><li><strong>Multi-agent reinforcement learning:</strong> cooperative decision-making, value decomposition, dynamic coordination graphs, and efficient exploration.</li><li><strong>World models and embodied intelligence:</strong> model-based reasoning, environment interaction, and robot task planning.</li><li><strong>Autonomous robot decision-making:</strong> offline reinforcement learning, long-horizon planning, and policy generalization.</li></ul></section>'''
  support='''<section id="support"><h2>Research Support</h2><p>My research has been supported through projects I lead, including:</p><ul class="funding"><li>Young Scientists Fund, National Natural Science Foundation of China</li><li>A subproject of the National Key R&amp;D Program of China</li><li>Open Research Fund of the National and Local Co-built Humanoid Robotics Innovation Center</li></ul></section>'''
  contact='''<section id="contact"><h2>Contact</h2><p class="contact-block"><a href="mailto:zeyang.liu@xjtu.edu.cn">zeyang.liu@xjtu.edu.cn</a><br>School of Artificial Intelligence<br>Xi’an Jiaotong University<br>Xi’an, Shaanxi, China</p></section>'''
 selected=[p for p in PAPERS if p.get('selected')]
 papers=f'''<section id="publications"><div class="section-head"><h2>{'代表性论文' if zh else 'Selected Publications'}</h2><a href="{pubs}">{'更多论文' if zh else 'More publications'}</a></div><ol class="papers">{''.join(paper(p) for p in selected)}</ol></section>'''
 return layout(profile+about+research+papers+support+contact,zh)
def publications(zh=False):
 years=sorted({p['year'] for p in PAPERS},reverse=True)
 intro=f'<p class="pub-intro">'+('以下列出部分研究论文。完整论文记录请参见 ' if zh else 'A selection of my research papers is listed below. For the full publication record, see ')+f'<a href="{SCHOLAR}">Google Scholar</a>.</p>'
 nav='<nav class="year-nav" aria-label="Publication years">'+''.join(f'<a href="#y{y}">{y}</a>' for y in years)+'</nav>'
 entries=''.join(f'<section id="y{y}"><h2>{y}</h2><ol class="papers">'+''.join(paper(p) for p in PAPERS if p['year']==y)+'</ol></section>' for y in years)
 return layout(intro+nav+entries,zh,True)
for name,content in [('index.html',homepage()),('zh.html',homepage(True)),('publications.html',publications()),('publications-zh.html',publications(True))]:
 (ROOT/name).write_text(content,encoding='utf-8')
(ROOT/'.nojekyll').touch()
print(f'Built 4 pages with {len(PAPERS)} verified publication entries.')
