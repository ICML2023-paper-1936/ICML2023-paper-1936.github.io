# 刘泽阳的个人学术主页

以简洁的学术主页为设计方向：白底、蓝色链接、左侧导航、衬线字体和按年份整理的论文。

## 页面

- `index.html`：英文主页（默认）
- `zh.html`：中文主页
- `publications.html`：英文论文页
- `publications-zh.html`：中文论文页
- `assets/style.css`：样式与移动端布局
- `assets/portrait.jpg`：学校团队主页公开照片
- `data/publications.json`：15 篇已核对的论文数据
- `tools/build.py`：通过 Python 标准库生成全部页面

这是可直接发布到 GitHub Pages 的静态网站，无需安装主题或前端依赖。

## GitHub Pages 发布

1. 登录您希望用于主页的 GitHub 账号，确认用户名。
2. 新建公开仓库，仓库名称必须是 `用户名.github.io`，例如用户名为 `example` 时，仓库名为 `example.github.io`。
3. 将本目录中的文件和目录上传到仓库根目录。不要把外层 `homepage` 文件夹一起作为根目录上传。
4. 仓库 `Settings → Pages → Build and deployment` 中，选择 `Deploy from a branch`，然后选择 `main` 分支和 `/(root)`，点击 `Save`。
5. 等待 Pages 部署完成，在该设置页确认网站地址，再打开检查。

若账号已经存在同名主页仓库，请先检查现有内容，再将本网站合并进去，避免覆盖原有主页。

## 日常维护

修改 `data/publications.json` 可添加或更正论文。`selected: true` 的论文会出现在主页，其余论文仍显示在论文页。保留正式发表标题与作者顺序；不应将预印本擅自标记为会议或期刊录用。

个人简介、研究方向和项目类别的文字位于 `tools/build.py`。编辑后运行：

```bash
python3 tools/build.py
```

将生成的 HTML 文件与修改过的数据文件一并提交，GitHub Pages 将自动更新。也可以直接编辑 HTML，但再次运行生成脚本会覆盖直接编辑的内容。

本地预览可直接双击 `index.html`；或有 Node.js 时运行 `npm run dev`，在浏览器访问 `http://localhost:4173`。

## 信息来源

核对日期：2026-09-29。已核对个人姓名、助理教授职务、学校邮箱、公开照片和论文信息。

- 个人简介：https://iair.xjtu.edu.cn/info/1046/3904.htm
- 团队成员及照片：https://gr.xjtu.edu.cn/zeuslan/zh_CN/zdylm/1067873/list/index.htm
- 团队论文列表：https://gr.xjtu.edu.cn/zeuslan/zh_CN/zdylm/1068030/list/index.htm
- Scholar：https://scholar.google.com/citations?user=YOOlkJoAAAAJ&hl=en
- 论文的正式出版链接位于 `data/publications.json`。

没有加入未经确认的教育经历、个人办公室、学生名额、奖励或未发表成果。主页仓库：https://github.com/ICML2023-paper-1936/ICML2023-paper-1936.github.io 。公开网页只使用学校公开邮箱，不包含账号登录信息。

设计参照 https://chengzu-li.github.io/ 的学术排版，页面代码独立编写。
