# Evo-RL 项目网站

根据 `../Evo_RL/main.tex` 当前草稿搭建的英文项目页，参考 GazeVLA 的学术项目页信息结构，采用白底、深青色标题和分区长页布局。科研图片来自当前论文及用户补充的 PiperX 实验结果图，未复制参考站的图片、视频、文字或代码。最近同步日期：2026-09-15。页面按方法概览、摘要与动机、学习循环、完整实验、演示视频、RW-RL 补充内容排列。

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
| `dist/assets/` | 论文 PDF 导出的图片、最新对比图、原始结果图及后续补充的视频 |
| `data/results.json` | 最新论文两张主表的数值、逐单元计数及来源哈希 |
| `scripts/render_policy_results.py` | 用上述数据生成静态结果图（制图需 matplotlib） |
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

## 内容来源与页面重点

- 摘要和动机重点对齐最新 Abstract / Introduction：困难状态的针对性纠错，以及不断增长经验中的选择性复用。首屏展示方法图、两项首轮提升与第二轮结果。
- 方法按 Algorithm 1：初始化一次，后续交替两类更新。优势采样说明采用实验中的 50-action / top 10% / 20-action 设置，删除已过时的 top 30% 待办。
- `tab:complete_loop`（Table II）和 `tab:scale_intervention`（Table I）均已补齐最新数值，结果区前置。新增值包括论文标红的修订内容，仍保留草稿状态。
- SR 是成功 attempts / 全部 attempts。网页 TP 使用插入 units/h 和叠衣 stages/h，与数据效率分析和论文审计脚本一致；待统一的正文措辞见 `CONTENT_TODO.md`。
- 用户 9 月 14 日提供的 PiperX 六项指标图不改动，放在补充实验中；原图不含最新所有条件，不用它替代主表。完成时间仅统计成功试次。
- RW-RL 压缩到页面末尾；总览、标注图、任务序列、收纳视频在默认关闭的原生 details 内。两项评估任务的视频和项目总览保留在主页面。
- 资源链接、四个视频、作者和 BibTeX 未提供时继续占位。论文源码未修改。

## 图片来源与复现

正文引用的 PDF 为图片更新依据；目录里的同名 PNG 可能未同步。

| 网页文件（`dist/assets/`） | 来源 |
| --- | --- |
| `evo_rl_method.png` | `../Evo_RL/figures/evo_rl_method.pdf` |
| `rwrl_overview.png` | `../Evo_RL/figures/rwrl_overview.pdf` |
| `data_characterization.png` | `../Evo_RL/figures/data_characterization.pdf` |
| `task_progression.png` | `../Evo_RL/figures/task_progression.pdf` |
| `value_advantage_500x200.png` | `../Evo_RL/figures/value_advantage_500x200.pdf` |
| `policy_results.svg` / `.png` | 最新稿 Table II，快照保存在 `data/results.json` |
| `piperx_experimental_results.png` | 用户于 2026-09-14 提供的实验图，原样保存 998 × 1004 px |

论文 PDF 使用 `pdftoppm -singlefile -png -scale-to 2400` 导出。最新比较图使用 matplotlib：

```bash
python3 scripts/render_policy_results.py
```

网站运行本身不需要 Python 或 matplotlib；生成的静态图片已随仓库提交。之后更新论文数值时，应同步 JSON、网页主表与逐单元表，并重新生成比较图。新图只展示已报告点估计，未从旧误差条推算新条件的置信区间。

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
