'use strict';

const content = window.EVORL_CONTENT || {};
const safeUrl = (value) => {
  if (typeof value !== 'string' || !value.trim()) return null;
  try {
    const url = new URL(value, window.location.href);
    return ['https:', 'http:', 'file:'].includes(url.protocol) ? url.href : null;
  } catch { return null; }
};

document.querySelectorAll('[data-resource]').forEach((placeholder) => {
  const url = safeUrl(content.resources?.[placeholder.dataset.resource]);
  if (!url) return;
  const link = document.createElement('a');
  link.className = placeholder.className;
  link.textContent = placeholder.firstChild.textContent.trim();
  link.href = url;
  link.target = '_blank';
  link.rel = 'noopener';
  placeholder.replaceWith(link);
});

document.querySelectorAll('[data-video]').forEach((placeholder) => {
  const url = safeUrl(content.videos?.[placeholder.dataset.video]);
  if (!url) return;
  const video = document.createElement('video');
  video.src = url;
  video.controls = true;
  video.playsInline = true;
  video.preload = 'metadata';
  video.className = 'demo-video' + (placeholder.classList.contains('overview-video') ? ' overview-video' : '');
  video.setAttribute('aria-label', placeholder.querySelector('strong').textContent);
  const fallback = document.createElement('a');
  fallback.href = url;
  fallback.textContent = 'Download video';
  video.append(fallback);
  video.addEventListener('error', () => {
    const note = document.createElement('p');
    note.className = 'fill-note';
    note.textContent = 'Video could not be loaded. Please check the media file or URL.';
    video.after(note);
  }, { once: true });
  placeholder.replaceWith(video);
});

const copyButton = document.querySelector('#copy-citation');
if (typeof content.bibtex === 'string' && content.bibtex.trim()) {
  const pre = document.createElement('pre');
  const code = document.createElement('code');
  code.textContent = content.bibtex.trim();
  pre.append(code);
  document.querySelector('#citation-content').replaceChildren(pre);
  copyButton.disabled = false;
  copyButton.textContent = 'Copy BibTeX';
  copyButton.addEventListener('click', async () => {
    const status = document.querySelector('#copy-status');
    try {
      await navigator.clipboard.writeText(content.bibtex.trim());
      status.textContent = 'BibTeX copied.';
      copyButton.textContent = 'Copied';
    } catch {
      const selection = window.getSelection();
      const range = document.createRange();
      range.selectNodeContents(code);
      selection.removeAllRanges();
      selection.addRange(range);
      status.textContent = 'Copy is unavailable here. Citation selected; press Ctrl+C or Command+C.';
    }
  });
}
