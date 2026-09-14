# Evo-RL 项目网站

根据 `../Evo_RL/main.tex` 当前草稿搭建的英文项目页，参考 GazeVLA 的学术项目页信息结构，采用白底、深青色标题和分区长页布局。科研图片来自当前论文及用户补充的 PiperX 实验结果图，未复制参考站的图片、视频、文字或代码。最近同步日期：2026-09-14。

## 本地查看

可以直接用浏览器打开 `dist/index.html`，或者在本目录启动：

```bash
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

访问 `http://127.0.0.1:4173/`。没有依赖安装或构建步骤；页面文字和表格不依赖 JavaScript，图片、样式和脚本都在本地。修改后刷新浏览器。

## 文件与修改入口

| 文件 | 用途 |
| --- | --- |
| `dist/index.html` | 标题、作者、摘要、章节、实验表格、占位说明 |
| `dist/styles.css` | 页面主题、排版、手机适配 |
| `dist/content.js` | 论文、代码、数据集、模型链接；4 个视频地址；BibTeX |
| `dist/site.js` | 正式资源替换、视频加载、引用复制、导航高亮 |
| `dist/assets/` | 论文 PDF 导出的图片、原始结果图及后续补充的视频 |
| `CONTENT_TODO.md` | 逐项补充清单及论文口径问题 |
| `.github/workflows/pages.yml` | 推送 `main` 后自动发布 `dist/` 到 GitHub Pages |
| `.openai/hosting.json` | 此前 Sites 预览的历史配置，GitHub Pages 不使用 |

只需把 `content.js` 中相应的 `null` 替换为正式值，资源按钮、视频播放器和 BibTeX 复制功能就会启用。不要把 Token、密码或私有下载凭据写进前端代码。

```js
// 视频可填相对路径，例如：
videos: {
  overview: 'assets/overview.mp4',
  insertion: 'assets/insertion.mp4',
  folding: null,
  packing: null
}
```

视频请使用直接可播放的 MP4 / WebM 文件；不要把 YouTube 等播放页 URL 当作视频文件。正文中对应的待补充说明需在内容确认后同步移除。

## 内容来源与取舍

- 标题、作者占位、摘要改写：`main.tex` 标题、Abstract、Introduction。首屏概述、研究动机与两项贡献重点对齐摘要和引言；两项研究分别链接到人类数据效率与完整学习循环的结果。
- RW-RL 的 1,000+ 小时、4 种本体、9 类场景、30+ 任务模板：RW-RL Dataset 章节。
- 三阶段方法：新版 Abstract、Algorithm 1、Method 及实验中的 Value Learning and Advantage-Guided Sampling。
- 总览图沿用 `figures/rwrl_overview.png`；方法图、统计图、任务序列图依据正文实际引用的 PDF 重新导出；新增价值 / 优势片段选择图。不要直接复制目录中未同步更新的同名旧 PNG。详见下方图片来源表。
- 主结果表保留 `tab:scale_intervention`（Table I）与 `tab:complete_loop`（Table II）的数值及缺项。新版 `tab:packing_intervention` 已注释，网页移除旧数据；收纳仍保留为数据集演示及视频占位。
- SR 按成功 attempts / 总 attempts 定义，TP 为成功 units / 机器人执行小时；折叠任务中的 unit 是阶段，插入任务中的 unit 是 screw–sleeve pair。
- 论文的发布状态表述不一致，页面统一保留资源待发布状态，直到提供正式链接。
- 补充的 PiperX 结果图以原文件保留，六项指标另有可展开的文字表：图表数值沿用图中精度，论文表沿用两位小数。整任务成功率与 attempt success 分开说明；完成时间只统计成功试次，缺项和无成功试次均不写成零。
- 论文中仍待确认的采样比例、训练混合方式和表格引用见 `CONTENT_TODO.md`；本次没有修改论文。

## 图片来源

| 网页文件（`dist/assets/`） | 来源 | 处理 |
| --- | --- | --- |
| `rwrl_overview.png` | `../Evo_RL/figures/rwrl_overview.png` | 原样复制 |
| `evo_rl_method.png` | `../Evo_RL/figures/evo_rl_method.pdf` | PDF 单页导出，宽 2400 px |
| `data_characterization.png` | `../Evo_RL/figures/data_characterization.pdf` | PDF 单页导出，宽 2400 px |
| `task_progression.png` | `../Evo_RL/figures/task_progression.pdf` | PDF 单页导出，宽 2400 px |
| `value_advantage_500x200.png` | `../Evo_RL/figures/value_advantage_500x200.pdf` | PDF 单页导出，宽 2400 px |
| `piperx_experimental_results.png` | 用户于 2026-09-14 提供的两组 PiperX 实验图 | 原样保存 998 × 1004 px，保留误差线 |

所有图都可点击查看完整分辨率。结果图下方的折叠表提供可选取的六项指标数据；未根据图片估算置信区间端点或重建原始试次数据。

## 发布与后续维护

当前目标仓库为 `QLL-ABAB/evo-rl`，GitHub Pages 默认地址为 `https://qll-abab.github.io/evo-rl/`。是否已发布以仓库 Actions 的成功部署记录和实际访问结果为准。

`dist/` 是完整静态站点，发布工作流只上传这个目录，不把维护文档和历史 Sites 配置作为网页内容发布。网站与 Overleaf 论文目录相互独立，不需要把网站代码推送到 Overleaf。

首次在 GitHub 仓库的 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。之后每次推送 `main`，工作流会自动发布；也可以在 **Actions → Deploy Evo-RL to GitHub Pages → Run workflow** 手动重跑。无需配置个人 Token 为仓库 Secret，工作流使用 GitHub 提供的短期 `GITHUB_TOKEN`。

本地修改、检查后提交并推送：

```bash
git add dist .github README.md CONTENT_TODO.md
git commit -m "Update Evo-RL project website"
git push origin main
```

## 后续交接给一作

可以将 `evo-rl` 仓库整体转移给一作的 GitHub 账号或团队组织，网站源码和发布工作流随仓库转移。当前页面使用相对资源路径，未写死 `QLL-ABAB` 或仓库名称，因此网页资源无需因为更换所有者而修改。

转移后核对以下事项：

1. 在接收方仓库中检查 Actions 是否启用，以及 Settings → Pages 是否仍选择 GitHub Actions。
2. 确认 `github-pages` 环境允许 `main` 部署，并重新运行发布工作流。
3. 从部署结果获取新网站地址，通常为 `https://新账号.github.io/evo-rl/`。GitHub 仓库地址的重定向不意味着旧 Pages 网站会自动重定向。
4. 把本地 Git 的 `origin` 改成新仓库地址，并更新论文、README 和其他对外链接。

如果之后使用专门的项目组织和与组织名匹配的 `组织名.github.io` 仓库，可以改为不带 `/evo-rl/` 路径的项目独立首页。

## 草稿状态

初版使用 `noindex, nofollow`，防止未完成内容被主动索引。正式公开前核对清单，并移除 `dist/index.html` 中该 robots meta 标签。该标签并不提供访问控制；访问权限由托管服务控制。

网站没有表单、追踪脚本、外部字体、CDN 依赖或自动播放视频。
