# Evo-RL 网站待补充清单

以下所有空项均保留为空，不代表 0、不代表实验失败，也不代表资源已经发布。

## 首屏与资源

- [ ] 作者姓名、最终顺序、单位编号、个人主页；当前保留论文的 Anonymous Authors。
- [ ] 论文公开 PDF 或 arXiv 链接：`dist/content.js` → `resources.paper`。
- [ ] 正式 GitHub 代码仓库：`resources.code`。
- [ ] RW-RL 数据集下载或托管地址：`resources.dataset`。
- [ ] 模型 checkpoint 地址：`resources.models`。
- [ ] 如已确定，再添加会议 / 期刊 / 年份；不得自行推定接收状态。

## 4 个视频位置

| 配置项 | 待提供素材 | 应有标注 |
| --- | --- | --- |
| `videos.overview` | 项目总览，串联三阶段学习循环与实验对比 | 任务名称、策略版本、对比条件 |
| `videos.insertion` | PiperX 螺栓 / 套筒抓取、对齐与插入全过程 | 播放倍速、策略版本、失败或干预情况 |
| `videos.folding` | SO-101 取衣、铺展、对折、折袖、折下摆 | 五个评估阶段、人工复位是否出现 |
| `videos.packing` | SO-101 文具收纳全过程 | 自动控制、人工接管、控制权交还区间 |

当前提供的是论文中的静态任务序列图；未用它冒充视频或实验录像。

## 实验缺项

全部需补充 U₁–U₅ 的成功数 / 计划数（attempts），以及 SR 与 TP：

- [ ] 数据效率表：4 h 的 SFT + Int.。
- [ ] 数据效率表：8 h 的 SFT + Int.。
- [ ] 消融表：PiperX SFT + RL。
- [ ] 迭代表：PiperX Evo-RL R2。
- [ ] 任务表：SO-101 folding 的 Evo-RL。

更新 `dist/index.html` 时，同时修改摘要表和折叠的逐单元明细表，再移除对应 Pending 标记。不要把 SR 写成整任务完成率。已有 SO-101 packing 两行干预次数与时长数据已填入。

## 数据集与引用

- [ ] 数据卡：各平台规模、任务覆盖、文件组织、训练 / 测试划分、下载与使用说明。
- [ ] 数据集、代码和模型各自的许可协议。
- [ ] 正式 BibTeX：`dist/content.js` → `bibtex`。当前没有虚构作者、年份、arXiv 号或发表信息。
- [ ] 经确认的致谢及资助信息。

## 需要先统一的论文内容

1. **优势采样比例。** Method 中按 demonstration / autonomous 两类各取 top 30%；实验中写 50-action advantage、正优势且全局 top 10%、保留 20-action chunk。需要明确哪项是最终方法，是否属于不同实验设置。网页保留文字提示，不擅自采用任一比例。
2. **Critic 的描述与图示。** Abstract 提到 stage-aware critic、质量及阶段监督；Method 给出 vision-only、时间与接管惩罚的分类价值模型，方法图仍有 observation + language / advantage-conditioned 等标识。需要统一真实输入、训练数据范围、监督和采样流程，再更新方法图。网页主体仅写 value-guided refinement。
3. **资源发布状态。** Abstract 为未来发布，Introduction / Conclusion 有已经公开的表述，目录中未提供可验证的正式链接。网页统一显示 Coming soon。
4. **数据集总览图中的模态。** 原图包含标为 schematic 的 depth 展示，而正文对 PiperX / SO-101 主要明确 RGB 和 state / action。发布数据卡时需区分真实记录字段与示意图字段；网页未额外承诺深度数据覆盖。

## 已做的初版检查

- 使用论文原图，网页无伪造图像、视频或实验数字。
- 待发布资源按钮禁用；视频位置跳转到明确的占位区。
- 静态页面可离线打开，图像使用本地相对路径。
- 正文桌面 / 手机布局；大表格可在自身容器内横向滚动。
- 图片可点击查看原始分辨率，逐单元实验计数可展开查看。
- Git / 托管配置仅作用于独立网站目录，未修改论文源文件。
