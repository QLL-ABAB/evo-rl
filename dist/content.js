/* 将 null 替换为正式 URL。保留 null 时，页面显示明确占位，不会生成假链接。
 * 视频使用本地相对路径（如 assets/insertion.mp4）或直接 MP4/WebM URL。
 * 外部资源链接使用 HTTPS。不要在这里写任何 token、密码或私有下载凭据。
 */
window.EVORL_CONTENT = {
  resources: { paper: null, code: null, dataset: null, models: null },
  videos: { overview: null, insertion: null, folding: null, packing: null },
  bibtex: null
};
