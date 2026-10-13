# Toast Stack

Notification toasts with depth. New toasts slide up from the bottom and older ones tuck behind them, scaled back so their edges peek out. Hover or focus the stack and it fans out into a full list, pausing every timer; leave and it folds back. Swipe a toast sideways to throw it away. `toast.promise()` shows a spinner that morphs into success or error in place. Depends on `tokens/variables.css`.

**Motion:** slide-up entry · collapsed stack with scale + peek · fan-out on hover/focus (heights and offsets animate) · swipe with drag-follow and fling · in-place type morph (spinner → check).

## HTML

```html
<!-- Demo triggers -->
<div class="toast-stack-demo">
  <button class="toast-stack-demo__btn" type="button" data-toast-demo="success">Booking confirmed</button>
  <button class="toast-stack-demo__btn" type="button" data-toast-demo="error">Payment failed</button>
  <button class="toast-stack-demo__btn" type="button" data-toast-demo="info">Technician on the way</button>
  <button class="toast-stack-demo__btn" type="button" data-toast-demo="promise">Save changes</button>
</div>

<!-- Region: one per page, near the end of <body> -->
<section class="toast-stack" aria-label="Notifications" data-toast-stack>
  <ol class="toast-stack__list" aria-live="polite"></ol>
</section>

<template id="toast-stack-template">
  <li class="toast-stack__toast">
    <span class="toast-stack__icon" aria-hidden="true"></span>
    <div class="toast-stack__text"><p class="toast-stack__title"></p><p class="toast-stack__desc"></p></div>
    <button class="toast-stack__action" type="button" hidden></button>
    <button class="toast-stack__close" type="button" aria-label="Dismiss notification">
      <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
    </button>
  </li>
</template>
```

## CSS

```css
/* Region: bottom-centre on phones, bottom-right from 768px */
.toast-stack {
  position: fixed; z-index: var(--z-toast); left: 0; right: 0; bottom: 0; display: flex; justify-content: center;
  padding: 0 var(--gutter) calc(1rem + env(safe-area-inset-bottom, 0px)); pointer-events: none; font-family: var(--font-sans);
}
@media (min-width: 768px) { .toast-stack { left: auto; padding-right: 1.5rem; padding-bottom: 1.5rem; } }
.toast-stack__list {
  position: relative; width: min(100vw - 2 * var(--gutter), 22.5rem); height: var(--toast-stack-collapsed, 0px);
  margin: 0; padding: 0; list-style: none; pointer-events: auto; transition: height var(--dur-4) var(--ease-out);
}
.toast-stack__list:is(:hover, :focus-within) { height: var(--toast-stack-total, 0px); }

/* Toast: collapsed position is a peek behind the newest one */
.toast-stack__toast {
  position: absolute; left: 0; right: 0; bottom: 0; z-index: calc(50 - var(--i, 0));
  display: grid; grid-template-columns: auto minmax(0, 1fr) auto auto; align-items: center; gap: 0.75rem;
  height: var(--toast-stack-front, auto); padding: 0.875rem 0.75rem 0.875rem 1rem; overflow: hidden; border-radius: 1rem;
  background: var(--surface-light); color: var(--text-main);
  box-shadow: inset 0 0 0 1px var(--border-subtle), 0 14px 36px -14px color-mix(in srgb, var(--surface-deep) 40%, transparent);
  opacity: var(--o, 1); transform-origin: 50% 0;
  transform: translateY(calc(var(--i, 0) * -12px)) scale(calc(1 - var(--i, 0) * 0.05));
  touch-action: pan-y; user-select: none;
  transition: transform var(--dur-4) var(--ease-out), opacity var(--dur-4) var(--ease-out), height var(--dur-4) var(--ease-out), translate var(--dur-4) var(--ease-out);
}
.toast-stack__toast:first-child { height: var(--h, auto); }
.toast-stack__toast > * { transition: opacity var(--dur-3); }
.toast-stack__list:not(:hover, :focus-within) .toast-stack__toast:not(:first-child) > * { opacity: 0; }

/* Expanded: every toast at its own height and offset */
.toast-stack__list:is(:hover, :focus-within) .toast-stack__toast { height: var(--h, auto); transform: translateY(calc(var(--offset, 0px) * -1)); }

/* Enter, leave, swipe */
.toast-stack__list .toast-stack__toast[data-state="entering"] { opacity: 0; transform: translateY(110%) scale(0.98); }
.toast-stack__list .toast-stack__toast[data-state="leaving"] { opacity: 0; transform: translateY(calc(var(--i, 0) * -12px)) scale(0.88); }
.toast-stack__list .toast-stack__toast[data-state="swiped"] { opacity: 0; translate: var(--swipe, 120%) 0; }

/* Type icons */
.toast-stack__icon { position: relative; display: grid; place-items: center; width: 1.5rem; height: 1.5rem; border-radius: 50%; color: var(--surface-light); font: 800 0.8125rem/1 var(--font-sans); transition: background-color var(--dur-3); }
.toast-stack__toast--success .toast-stack__icon { background: var(--success); }
.toast-stack__toast--success .toast-stack__icon::after { content: ""; width: 0.3125rem; height: 0.5625rem; margin-top: -0.125rem; border: solid currentColor; border-width: 0 2px 2px 0; transform: rotate(45deg); animation: toast-stack-pop var(--dur-4) var(--ease-spring); }
.toast-stack__toast--error .toast-stack__icon { background: var(--danger); }
.toast-stack__toast--error .toast-stack__icon::after { content: "!"; }
.toast-stack__toast--info .toast-stack__icon { background: var(--primary); }
.toast-stack__toast--info .toast-stack__icon::after { content: "i"; font-family: Georgia, serif; font-style: italic; }
.toast-stack__toast--loading .toast-stack__icon { border: 2px solid var(--border-subtle); border-top-color: var(--primary); animation: toast-stack-spin 0.8s linear infinite; }

/* Text and buttons */
.toast-stack__title { margin: 0; font-size: 0.9375rem; font-weight: 600; line-height: 1.35; }
.toast-stack__desc { margin: 0.125rem 0 0; color: var(--text-muted); font-size: 0.8125rem; line-height: 1.4; }
.toast-stack__desc[hidden], .toast-stack__action[hidden] { display: none; }
.toast-stack__action {
  height: 2rem; padding: 0 0.75rem; border: 0; border-radius: 999px; cursor: pointer;
  background: var(--text-main); color: var(--surface-light); font: 600 0.8125rem var(--font-sans);
  transition: transform var(--dur-3) var(--ease-spring);
}
.toast-stack__action:active { transform: scale(0.95); }
.toast-stack__close {
  display: grid; place-items: center; width: 1.75rem; height: 1.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: transparent; color: var(--text-muted); transition: background-color var(--dur-2), color var(--dur-2);
}
.toast-stack__close:hover { background: var(--surface-muted); color: var(--text-main); }
.toast-stack__close svg { fill: none; stroke: currentColor; stroke-width: 2.5; stroke-linecap: round; }
.toast-stack :is(button):focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

/* Demo triggers */
.toast-stack-demo { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; padding: 3rem var(--gutter); font-family: var(--font-sans); }
.toast-stack-demo__btn {
  height: 2.75rem; padding: 0 1.125rem; border: 0; border-radius: 999px; cursor: pointer;
  background: var(--surface-light); color: var(--text-main); font: 600 0.875rem var(--font-sans);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm); transition: transform var(--dur-3) var(--ease-spring);
}
.toast-stack-demo__btn:active { transform: scale(0.96); }
.toast-stack-demo__btn:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

@media (prefers-reduced-motion: reduce) { .toast-stack__icon, .toast-stack__icon::after { animation: none !important; } }
@keyframes toast-stack-spin { to { rotate: 360deg; } }
@keyframes toast-stack-pop { from { transform: rotate(45deg) scale(0); } }
```

## JS

```js
const toastList = document.querySelector('[data-toast-stack] .toast-stack__list');
const toastTemplate = document.getElementById('toast-stack-template');
const TOAST_GAP = 10;
const TOAST_PEEK = 12;
const TOAST_VISIBLE = 3;
const toasts = []; // newest first: { id, el, h, remaining, started, timer }
let toastSeq = 0;
let toastHover = false;

// Write stacking variables: index, expanded offset, and the list's collapsed/expanded heights
const layoutToasts = () => {
  let offset = 0;
  toasts.forEach((t, i) => {
    t.el.style.setProperty('--i', i);
    t.el.style.setProperty('--offset', `${offset}px`);
    t.el.style.setProperty('--o', i < TOAST_VISIBLE ? 1 : 0);
    offset += t.h + TOAST_GAP;
  });
  const front = toasts[0]?.h || 0;
  toastList.style.setProperty('--toast-stack-front', `${front}px`);
  toastList.style.setProperty('--toast-stack-collapsed', `${front ? front + Math.min(toasts.length - 1, TOAST_VISIBLE - 1) * TOAST_PEEK : 0}px`);
  toastList.style.setProperty('--toast-stack-total', `${Math.max(offset - TOAST_GAP, 0)}px`);
};
const measureToast = (t) => {
  t.el.style.height = 'auto';
  t.h = t.el.offsetHeight;
  t.el.style.height = '';
  t.el.style.setProperty('--h', `${t.h}px`);
};

// Timers pause while the stack is hovered or focused
const startToastTimer = (t) => {
  clearTimeout(t.timer);
  if (toastHover || !Number.isFinite(t.remaining)) return;
  t.started = Date.now();
  t.timer = setTimeout(() => toast.dismiss(t.id), t.remaining);
};
const pauseToastTimer = (t) => {
  if (!t.started) return;
  clearTimeout(t.timer);
  t.remaining -= Date.now() - t.started;
  t.started = 0;
};

const fillToast = (t, { title, description = '', type = 'info', action }) => {
  t.el.className = `toast-stack__toast toast-stack__toast--${type}`;
  t.el.querySelector('.toast-stack__title').textContent = title;
  const desc = t.el.querySelector('.toast-stack__desc');
  desc.textContent = description;
  desc.hidden = !description;
  const btn = t.el.querySelector('.toast-stack__action');
  btn.hidden = !action;
  if (action) {
    btn.textContent = action.label;
    btn.onclick = () => { action.onClick?.(); toast.dismiss(t.id); };
  }
};

// Public API: toast(title, { type, description, action, duration }) → id
function toast(title, opts = {}) {
  const el = toastTemplate.content.firstElementChild.cloneNode(true);
  const t = { id: ++toastSeq, el, h: 0, remaining: opts.type === 'loading' ? Infinity : opts.duration ?? 4500, started: 0, timer: 0 };
  fillToast(t, { title, ...opts });
  el.dataset.state = 'entering';
  toastList.prepend(el);
  measureToast(t);
  toasts.unshift(t);
  layoutToasts();
  requestAnimationFrame(() => requestAnimationFrame(() => { delete el.dataset.state; }));
  startToastTimer(t);
  return t.id;
}
toast.update = (id, opts) => {
  const t = toasts.find((x) => x.id === id);
  if (!t) return;
  fillToast(t, opts);
  measureToast(t);
  layoutToasts();
  t.remaining = opts.duration ?? 4500;
  startToastTimer(t);
};
toast.dismiss = (id, swiped) => {
  const index = toasts.findIndex((x) => x.id === id);
  if (index < 0) return;
  const [t] = toasts.splice(index, 1);
  clearTimeout(t.timer);
  t.el.dataset.state = swiped ? 'swiped' : 'leaving';
  setTimeout(() => t.el.remove(), 600);
  layoutToasts();
};
toast.promise = (promise, { loading, success, error }) => {
  const id = toast(loading, { type: 'loading' });
  promise.then(() => toast.update(id, { title: success, type: 'success' }), () => toast.update(id, { title: error, type: 'error' }));
  return promise;
};
window.toast = toast;

// Hover/focus: expand and pause; close buttons; swipe to dismiss
const setToastHover = (on) => { toastHover = on; toasts.forEach((t) => (on ? pauseToastTimer(t) : startToastTimer(t))); };
toastList.addEventListener('pointerenter', () => setToastHover(true));
toastList.addEventListener('pointerleave', () => setToastHover(false));
toastList.addEventListener('focusin', () => setToastHover(true));
toastList.addEventListener('focusout', (e) => { if (!toastList.contains(e.relatedTarget)) setToastHover(false); });
toastList.addEventListener('click', (e) => {
  const li = e.target.closest('.toast-stack__close')?.closest('li');
  const t = li && toasts.find((x) => x.el === li);
  if (t) toast.dismiss(t.id);
});
let toastSwipe = null;
toastList.addEventListener('pointerdown', (e) => {
  const el = e.target.closest('.toast-stack__toast');
  if (!el || e.target.closest('button')) return;
  toastSwipe = { el, x: e.clientX, t: performance.now() };
  el.setPointerCapture(e.pointerId);
  el.style.transition = 'none';
});
toastList.addEventListener('pointermove', (e) => {
  if (!toastSwipe) return;
  const dx = e.clientX - toastSwipe.x;
  toastSwipe.el.style.translate = `${dx}px 0`;
  toastSwipe.el.style.opacity = String(1 - Math.min(Math.abs(dx) / 260, 0.8));
});
const endToastSwipe = (e) => {
  if (!toastSwipe) return;
  const { el, x, t: t0 } = toastSwipe;
  const dx = e.clientX - x;
  toastSwipe = null;
  el.style.transition = '';
  el.style.translate = '';
  el.style.opacity = '';
  const item = toasts.find((x2) => x2.el === el);
  if (item && (Math.abs(dx) > 90 || Math.abs(dx) / Math.max(performance.now() - t0, 1) > 0.5)) {
    el.style.setProperty('--swipe', dx > 0 ? '120%' : '-120%');
    toast.dismiss(item.id, true);
  }
};
toastList.addEventListener('pointerup', endToastSwipe);
toastList.addEventListener('pointercancel', endToastSwipe);

// Demo wiring
document.querySelectorAll('[data-toast-demo]').forEach((btn) => btn.addEventListener('click', () => {
  const kind = btn.dataset.toastDemo;
  if (kind === 'success') toast('Booking confirmed', { type: 'success', description: 'Mon 13 Oct, 10–12. We’ll text when Sam is on the way.', action: { label: 'Undo' } });
  if (kind === 'error') toast('Payment failed', { type: 'error', description: 'Your card was declined. Try another card.' });
  if (kind === 'info') toast('Sam is on the way', { type: 'info', description: 'Arriving in about 12 minutes.' });
  if (kind === 'promise') toast.promise(new Promise((resolve) => setTimeout(resolve, 1800)), { loading: 'Saving changes…', success: 'Changes saved', error: 'Couldn’t save' });
}));
```

## Notes

- The list is a polite live region, so every new toast and every in-place update (loading → success) is announced. For errors that need immediate attention, also move focus or use an inline alert. Don't rely on a toast alone.
- Timers pause while the stack is hovered or holds keyboard focus (WCAG 2.2.1), and each toast has a close button. Swiping is an extra, not the only way to dismiss.
- Keep toasts short: a title, an optional one-line description, at most one action. Anything longer belongs on the page.
- One region per page. Call `toast()` from anywhere once this script has loaded (it's also on `window.toast`).
- Under reduced motion every move is instant and the spinner holds still. States still change.
