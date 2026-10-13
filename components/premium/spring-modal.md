# Spring Modal

A booking dialog that springs out of the button that opened it. On desktop it scales up from the trigger's position with a real spring curve over a blurred backdrop. On phones it becomes a bottom sheet that slides up and can be dragged down to dismiss. Choosing a day and a slot gives springy chip feedback; confirming morphs the panel's height into a success view with a drawn check. Depends on `tokens/variables.css`.

**Motion:** zoom-from-trigger with spring (`--ease-spring`) · backdrop blur fade · bottom sheet slide with drag-to-dismiss · chip press pop · height morph between views · check ring and tick draw.

## HTML

```html
<div class="spring-dialog-demo">
  <button class="spring-dialog__trigger" type="button" data-spring-dialog-open="spring-dialog-book" aria-haspopup="dialog">
    <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /></svg>
    Book a visit
  </button>
</div>

<dialog class="spring-dialog" id="spring-dialog-book" aria-labelledby="spring-dialog-title">
  <div class="spring-dialog__panel">
    <span class="spring-dialog__handle" aria-hidden="true"></span>

    <div class="spring-dialog__view spring-dialog__view--form">
      <header class="spring-dialog__head">
        <div>
          <p class="spring-dialog__eyebrow">Leak repair · from $149</p>
          <h2 id="spring-dialog-title" class="spring-dialog__title">Pick a time</h2>
        </div>
        <button class="spring-dialog__close" type="button" aria-label="Close">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
        </button>
      </header>

      <fieldset class="spring-dialog__group">
        <legend>Day</legend>
        <div class="spring-dialog__days">
          <label class="spring-dialog__chip"><input type="radio" name="spring-dialog-day" value="Mon 13 Oct" checked><span>Mon</span><strong>13</strong></label>
          <label class="spring-dialog__chip"><input type="radio" name="spring-dialog-day" value="Tue 14 Oct"><span>Tue</span><strong>14</strong></label>
          <label class="spring-dialog__chip"><input type="radio" name="spring-dialog-day" value="Wed 15 Oct"><span>Wed</span><strong>15</strong></label>
          <label class="spring-dialog__chip"><input type="radio" name="spring-dialog-day" value="Thu 16 Oct"><span>Thu</span><strong>16</strong></label>
          <label class="spring-dialog__chip"><input type="radio" name="spring-dialog-day" value="Fri 17 Oct"><span>Fri</span><strong>17</strong></label>
        </div>
      </fieldset>

      <fieldset class="spring-dialog__group">
        <legend>Arrival window</legend>
        <div class="spring-dialog__slots">
          <label class="spring-dialog__slot"><input type="radio" name="spring-dialog-slot" value="8–10 am" disabled><span>8–10 am</span><small>Full</small></label>
          <label class="spring-dialog__slot"><input type="radio" name="spring-dialog-slot" value="10 am–12 pm" checked><span>10–12</span><small>2 left</small></label>
          <label class="spring-dialog__slot"><input type="radio" name="spring-dialog-slot" value="12–2 pm"><span>12–2 pm</span><small>Open</small></label>
          <label class="spring-dialog__slot"><input type="radio" name="spring-dialog-slot" value="2–4 pm"><span>2–4 pm</span><small>Open</small></label>
        </div>
      </fieldset>

      <footer class="spring-dialog__foot">
        <p>Free estimate on arrival. Change or cancel any time.</p>
        <button class="spring-dialog__confirm" type="button">Confirm booking</button>
      </footer>
    </div>

    <div class="spring-dialog__view spring-dialog__view--done" hidden>
      <svg class="spring-dialog__tick" viewBox="0 0 64 64" width="72" height="72" aria-hidden="true" focusable="false">
        <circle cx="32" cy="32" r="28" pathLength="1" /><path d="m21 33 8 8 15-17" pathLength="1" />
      </svg>
      <h3 class="spring-dialog__title">You're booked</h3>
      <p class="spring-dialog__summary">We'll text you when your technician is on the way.</p>
      <button class="spring-dialog__confirm" type="button" data-spring-dialog-close>Done</button>
    </div>
  </div>
</dialog>
```

## CSS

```css
/* Trigger (demo) */
.spring-dialog-demo { display: grid; place-items: center; min-height: 16rem; padding: 3rem var(--gutter); font-family: var(--font-sans); }
.spring-dialog__trigger {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; border: 0; border-radius: 999px; cursor: pointer;
  background: var(--text-main); color: var(--surface-light); font: 600 0.9375rem var(--font-sans);
  box-shadow: var(--highlight-inverse), 0 12px 28px -12px color-mix(in srgb, var(--text-main) 70%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.spring-dialog__trigger svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.spring-dialog__trigger:active { transform: scale(0.96); }
.spring-dialog__trigger:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Dialog: zooms from the trigger (origin set by JS) with a spring */
.spring-dialog {
  width: min(30rem, calc(100% - 2rem)); max-height: min(90dvh, 44rem); padding: 0; border: 0; border-radius: var(--radius-2xl);
  background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); overflow: hidden;
  box-shadow: 0 40px 100px -24px color-mix(in srgb, var(--surface-deep) 55%, transparent), inset 0 0 0 1px var(--border-subtle);
  opacity: 0; transform: scale(0.6); transform-origin: var(--spring-dialog-ox, 50%) var(--spring-dialog-oy, 50%);
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring);
}
.spring-dialog[data-state="open"] { opacity: 1; transform: none; }
.spring-dialog::backdrop { background: color-mix(in srgb, var(--surface-deep) 50%, transparent); backdrop-filter: blur(6px); opacity: 0; transition: opacity var(--dur-3) var(--ease-out); }
.spring-dialog[data-state="open"]::backdrop { opacity: 1; }
html:has(.spring-dialog[open]) { overflow: hidden; }

.spring-dialog__panel { display: flex; flex-direction: column; max-height: inherit; }
.spring-dialog__handle { display: none; }
.spring-dialog__view { display: grid; gap: 1.5rem; padding: 1.5rem; overflow-y: auto; }
.spring-dialog__view[hidden] { display: none; }
.spring-dialog__head { display: flex; align-items: flex-start; justify-content: space-between; gap: 1rem; }
.spring-dialog__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; }
.spring-dialog__title { margin: 0.375rem 0 0; font: 600 1.5rem/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.spring-dialog__close {
  flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-muted); color: var(--text-muted); transition: background-color var(--dur-2), color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.spring-dialog__close svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }
.spring-dialog__close:hover { background: var(--border-subtle); color: var(--text-main); transform: rotate(90deg); }
.spring-dialog :is(button, label):focus-visible, .spring-dialog label:has(:focus-visible) { outline: 2px solid var(--primary); outline-offset: 2px; }

/* Choice groups: radio inputs styled as chips that pop when chosen */
.spring-dialog__group { min-width: 0; margin: 0; padding: 0; border: 0; }
.spring-dialog__group legend { margin-bottom: 0.75rem; padding: 0; font-size: 0.875rem; font-weight: 600; }
.spring-dialog__days { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 0.5rem; }
.spring-dialog__slots { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.5rem; }
.spring-dialog__chip, .spring-dialog__slot {
  position: relative; display: grid; justify-items: center; gap: 0.125rem; padding: 0.75rem 0.25rem; border-radius: 1rem; cursor: pointer;
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px transparent;
  transition: background-color var(--dur-3), color var(--dur-3), box-shadow var(--dur-3), transform var(--dur-4) var(--ease-spring);
}
.spring-dialog__chip input, .spring-dialog__slot input { position: absolute; opacity: 0; pointer-events: none; }
.spring-dialog__chip span, .spring-dialog__slot small { color: var(--text-muted); font-size: 0.75rem; transition: color var(--dur-3); }
.spring-dialog__chip strong { font: 600 1.25rem/1 var(--font-display); }
.spring-dialog__slot span { font-weight: 600; font-size: 0.9375rem; }
.spring-dialog__chip:hover, .spring-dialog__slot:hover { box-shadow: inset 0 0 0 1px var(--border-subtle); }
.spring-dialog__chip:active, .spring-dialog__slot:active { transform: scale(0.94); }
.spring-dialog__chip:has(:checked), .spring-dialog__slot:has(:checked) {
  background: var(--text-main); color: var(--surface-light);
  box-shadow: 0 10px 22px -12px color-mix(in srgb, var(--text-main) 80%, transparent);
  animation: spring-dialog-pop var(--dur-4) var(--ease-spring);
}
.spring-dialog__chip:has(:checked) span, .spring-dialog__slot:has(:checked) small { color: color-mix(in srgb, var(--surface-light) 75%, transparent); }
.spring-dialog__slot:has(:disabled) { cursor: not-allowed; opacity: 0.55; }
.spring-dialog__slot:has(:disabled) span { text-decoration: line-through; }

/* Footer and confirm */
.spring-dialog__foot { display: grid; gap: 0.75rem; padding-top: 1.25rem; border-top: 1px solid var(--border-subtle); }
.spring-dialog__foot p { margin: 0; color: var(--text-muted); font-size: 0.8125rem; }
.spring-dialog__confirm {
  height: 3rem; border: 0; border-radius: 999px; cursor: pointer;
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font: 600 0.9375rem var(--font-sans);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 10px 24px -10px var(--primary);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3);
}
.spring-dialog__confirm:active { transform: scale(0.97); }

/* Success view: ring and tick draw in */
.spring-dialog__view--done { justify-items: center; padding-block: 2.5rem 1.5rem; text-align: center; }
.spring-dialog__view--done .spring-dialog__confirm { justify-self: stretch; }
.spring-dialog__summary { margin: -0.75rem 0 0; color: var(--text-muted); line-height: 1.55; }
.spring-dialog__tick circle, .spring-dialog__tick path { fill: none; stroke-linecap: round; stroke-linejoin: round; stroke-dasharray: 1; }
.spring-dialog__tick circle { stroke: color-mix(in srgb, var(--success) 25%, transparent); stroke-width: 4; }
.spring-dialog__tick path { stroke: var(--success); stroke-width: 5; }
.spring-dialog__view--done:not([hidden]) .spring-dialog__tick circle { animation: spring-dialog-draw var(--dur-5) var(--ease-out) both; }
.spring-dialog__view--done:not([hidden]) .spring-dialog__tick path { animation: spring-dialog-draw var(--dur-4) var(--ease-out) 350ms both; }
.spring-dialog__view--done:not([hidden]) .spring-dialog__tick { animation: spring-dialog-pop var(--dur-5) var(--ease-spring) 250ms both; }

/* Phones: a bottom sheet that slides up and can be dragged down */
@media (max-width: 639.98px) {
  .spring-dialog { width: 100%; max-width: 100%; margin: auto 0 0; border-radius: var(--radius-2xl) var(--radius-2xl) 0 0; opacity: 1; transform: translateY(100%); }
  .spring-dialog__handle { display: block; width: 2.5rem; height: 0.3125rem; margin: 0.625rem auto -0.5rem; border-radius: 999px; background: var(--border-subtle); }
  .spring-dialog__handle, .spring-dialog__head { touch-action: none; }
  .spring-dialog__view { padding-bottom: calc(1.5rem + env(safe-area-inset-bottom, 0px)); }
}

@media (prefers-reduced-motion: reduce) {
  .spring-dialog *, .spring-dialog *::before, .spring-dialog *::after { animation: none !important; }
}
@keyframes spring-dialog-pop { 0% { transform: scale(0.9); } 100% { transform: scale(1); } }
@keyframes spring-dialog-draw { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
```

## JS

```js
document.querySelectorAll('.spring-dialog').forEach((dialog) => {
  const panel = dialog.querySelector('.spring-dialog__panel');
  const form = dialog.querySelector('.spring-dialog__view--form');
  const done = dialog.querySelector('.spring-dialog__view--done');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const sheet = matchMedia('(max-width: 639.98px)');
  let opener = null;

  // Open: zoom out of the trigger (desktop) or slide up (sheet)
  const open = (trigger) => {
    opener = trigger;
    form.hidden = false;
    done.hidden = true;
    dialog.showModal();
    const r = trigger.getBoundingClientRect();
    dialog.style.setProperty('--spring-dialog-ox', `${r.left + r.width / 2 - dialog.offsetLeft}px`);
    dialog.style.setProperty('--spring-dialog-oy', `${r.top + r.height / 2 - dialog.offsetTop}px`);
    requestAnimationFrame(() => requestAnimationFrame(() => { dialog.dataset.state = 'open'; }));
  };

  // Close: play the exit, then really close and return focus
  const close = () => {
    if (dialog.dataset.state !== 'open') return;
    delete dialog.dataset.state;
    const finish = () => {
      clearTimeout(timer);
      dialog.removeEventListener('transitionend', onEnd);
      if (dialog.open) dialog.close();
      opener?.focus();
    };
    const onEnd = (e) => { if (e.target === dialog && e.propertyName === 'transform') finish(); };
    const timer = setTimeout(finish, 700);
    dialog.addEventListener('transitionend', onEnd);
  };

  document.querySelectorAll(`[data-spring-dialog-open="${dialog.id}"]`).forEach((t) => t.addEventListener('click', () => open(t)));
  dialog.addEventListener('cancel', (e) => { e.preventDefault(); close(); });
  dialog.addEventListener('click', (e) => {
    if (e.target === dialog || e.target.closest('.spring-dialog__close, [data-spring-dialog-close]')) close();
  });

  // Confirm: swap to the success view, morphing the panel height
  form.querySelector('.spring-dialog__confirm').addEventListener('click', () => {
    const day = form.querySelector('[name="spring-dialog-day"]:checked')?.value;
    const slot = form.querySelector('[name="spring-dialog-slot"]:checked')?.value;
    done.querySelector('.spring-dialog__summary').textContent = `${day}, ${slot}. We'll text you when your technician is on the way.`;
    const from = panel.offsetHeight;
    form.hidden = true;
    done.hidden = false;
    if (!reduce.matches) panel.animate({ height: [`${from}px`, `${panel.offsetHeight}px`] }, { duration: 460, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' });
    done.querySelector('button').focus();
  });

  // Sheet: drag the handle or header down to dismiss (distance or flick)
  let drag = null;
  panel.addEventListener('pointerdown', (e) => {
    if (!sheet.matches || e.target.closest('button') || !e.target.closest('.spring-dialog__handle, .spring-dialog__head')) return;
    drag = { y: e.clientY, t: performance.now() };
    panel.setPointerCapture(e.pointerId);
    dialog.style.transition = 'none';
  });
  panel.addEventListener('pointermove', (e) => {
    if (drag) dialog.style.transform = `translateY(${Math.max(0, e.clientY - drag.y)}px)`;
  });
  const drop = (e) => {
    if (!drag) return;
    const dy = e.clientY - drag.y;
    const velocity = dy / Math.max(performance.now() - drag.t, 1);
    drag = null;
    dialog.style.transition = '';
    dialog.style.transform = '';
    if (dy > 120 || velocity > 0.6) close();
  };
  panel.addEventListener('pointerup', drop);
  panel.addEventListener('pointercancel', drop);
});
```

## Notes

- A real modal `<dialog>`: focus is trapped, the page is inert, Escape and backdrop clicks close it with the exit animation, and focus returns to the trigger.
- Choices are native radio groups in `fieldset`/`legend`, so arrow keys work, and full slots are `disabled` (struck through, not just greyed).
- On phones the sheet also closes with a downward flick. The handle is decorative; the close button remains for keyboard and screen-reader users.
- Under reduced motion the spring, sheet slide and draws become instant; the height morph is skipped.
- Swap the form for any content. Keep `.spring-dialog__panel` and one or more `.spring-dialog__view`s.
