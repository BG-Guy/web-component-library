# Scroll-Scrubbed Before/After

A pinned before/after of a kitchen remodel, framed in a rounded, device-like bezel with a soft layered shadow on a light surface. The signature: scrolling sweeps the divider from right to left to uncover the "after", the Before and After labels fade as it crosses them, and a "Finished in 9 days" chip springs in near the end. The glass handle is directly operable (drag anywhere on the photo, or tab to the native range and use the arrow keys), and manual control holds until you scroll again, when the divider glides back to your scroll position. On phones the frame turns square; with reduced motion it isn't pinned and opens at 50%. Depends on `tokens/variables.css`.

**Motion:** divider, clip and label fades scrub with scroll (linear, rAF) · glide back to the scroll position after a manual drag (`--dur-4`, `--ease-out`, via `@property`) · chip pop (`--dur-4`, `--ease-spring`) · handle hover/press (`--ease-spring`) · intro hint bobs three times.

## HTML

```html
<div class="scroll-compare-demo">
  <p class="scroll-compare-demo__copy">One Westlake kitchen, start to finish.</p>
  <p class="scroll-compare-demo__hint">Scroll to reveal
    <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
  </p>
</div>

<section class="scroll-compare" aria-labelledby="scroll-compare-title" data-scroll-compare>
  <div class="scroll-compare__stage">
    <div class="scroll-compare__inner">
      <header class="scroll-compare__head">
        <p class="scroll-compare__eyebrow">Kitchen remodel · Westlake</p>
        <h2 id="scroll-compare-title" class="scroll-compare__title">Same kitchen. Nine days later.</h2>
        <p class="scroll-compare__lead">New cabinets, quartz worktops and lighting, finished in nine working days.</p>
      </header>

      <div class="scroll-compare__device">
        <div class="scroll-compare__view">
          <figure class="scroll-compare__figure scroll-compare__figure--before">
            <img src="kitchen-before.jpg" width="1600" height="1000" alt="Before: dated oak cabinets, laminate worktops and a fluorescent ceiling panel" loading="lazy" decoding="async" draggable="false">
            <figcaption class="scroll-compare__label">Before</figcaption>
          </figure>
          <figure class="scroll-compare__figure scroll-compare__figure--after">
            <img src="kitchen-after.jpg" width="1600" height="1000" alt="After: white oak cabinets, quartz worktops and an island under brass pendants" loading="lazy" decoding="async" draggable="false">
            <figcaption class="scroll-compare__label">After</figcaption>
          </figure>
          <input class="scroll-compare__range" type="range" min="0" max="100" step="1" value="0" aria-label="Reveal after photo" hidden>
          <span class="scroll-compare__divider" aria-hidden="true"></span>
          <span class="scroll-compare__handle" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="m9 7-5 5 5 5M15 7l5 5-5 5" /></svg>
          </span>
          <p class="scroll-compare__chip" aria-hidden="true">
            <span class="scroll-compare__chip-icon"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM9 15l2 2 4-4" /></svg></span>
            <span><strong>Finished in 9 days</strong><small>Mar 4 → Mar 13</small></span>
          </p>
        </div>
      </div>

      <p class="scroll-compare__hint" aria-hidden="true"><span class="scroll-compare__hint-scroll">Scroll to reveal · </span>Drag the photo or use the arrow keys</p>
    </div>
  </div>
</section>

<div class="scroll-compare-demo">
  <p class="scroll-compare-demo__copy">Planning your own? Quotes are free.</p>
  <p class="scroll-compare-demo__hint">Scroll back up to rewind</p>
</div>
```

## CSS

```css
/* Registered so the glide back to the scroll position can transition */
@property --scroll-compare-v { syntax: "<number>"; inherits: true; initial-value: 0; }

/* Demo scroll room above and below */
.scroll-compare-demo {
  display: grid; place-content: center; justify-items: center; gap: 0.875rem; min-height: 70vh; padding: 3rem var(--gutter);
  background: var(--surface-light); color: var(--text-muted); font-family: var(--font-sans); text-align: center;
}
.scroll-compare-demo__copy { margin: 0; color: var(--text-main); font: 600 clamp(1.5rem, 1.1rem + 1.6vw, 2.25rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.scroll-compare-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.scroll-compare-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: scroll-compare-bob 1.4s var(--ease-in-out) 600ms 3; }

/* Section. --scroll-compare-lb/-la: where each label's inner edge sits, in % of the photo width */
.scroll-compare {
  --scroll-compare-lb: 34; --scroll-compare-la: 70;
  position: relative; background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
}
.scroll-compare__stage { position: relative; isolation: isolate; }
.scroll-compare__stage::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background:
    radial-gradient(50% 45% at 50% 60%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%),
    radial-gradient(circle, color-mix(in srgb, var(--text-main) 10%, transparent) 1px, transparent 1.5px) 0 0 / 22px 22px;
  -webkit-mask-image: radial-gradient(ellipse 65% 60% at 50% 55%, black 30%, transparent 80%);
  mask-image: radial-gradient(ellipse 65% 60% at 50% 55%, black 30%, transparent 80%);
}
.scroll-compare__inner { display: grid; gap: clamp(1.25rem, 3vw, 2rem); width: 100%; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.scroll-compare__head { max-width: 40rem; margin-inline: auto; text-align: center; }
.scroll-compare__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.scroll-compare__title { margin: 0.75rem 0 0; font: 600 clamp(1.75rem, 1.2rem + 2.2vw, 2.75rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.scroll-compare__lead { max-width: 34rem; margin: 0.75rem auto 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.55; text-wrap: balance; }

/* Device: aluminium-light bezel, camera dot, layered shadow with a hint of brand light */
.scroll-compare__device {
  position: relative; width: 100%; max-width: 64rem; margin-inline: auto; padding: 0.625rem; border-radius: var(--radius-2xl);
  background: linear-gradient(180deg, var(--surface-light), color-mix(in srgb, var(--border-subtle) 75%, var(--surface-light)));
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl), 0 48px 96px -40px color-mix(in srgb, var(--primary) 32%, transparent);
}
.scroll-compare__device::before { content: ""; position: absolute; top: 0.1875rem; left: 50%; width: 0.25rem; height: 0.25rem; translate: -50% 0; border-radius: var(--radius-full); background: color-mix(in srgb, var(--text-main) 28%, var(--surface-light)); }

/* Default (no JS): two captioned figures, stacked on phones, side by side from 768px */
.scroll-compare__view { position: relative; display: grid; gap: 0.625rem; }
.scroll-compare__figure {
  position: relative; margin: 0; overflow: hidden; border-radius: calc(var(--radius-2xl) - 0.625rem);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 22%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 26%, var(--surface-light)));
}
.scroll-compare__figure--after { background: linear-gradient(135deg, color-mix(in srgb, var(--accent) 24%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 22%, var(--surface-light))); }
.scroll-compare__figure img { display: block; width: 100%; height: auto; aspect-ratio: 16 / 10; object-fit: cover; -webkit-user-select: none; user-select: none; }
.scroll-compare__label {
  position: absolute; left: 0.75rem; bottom: 0.75rem; padding: 0.375rem 0.75rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-light) 86%, transparent); color: var(--text-main); box-shadow: var(--highlight), var(--shadow-md);
  font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase;
}

/* Comparison (JS): photos share one cell; "after" is clipped to the right of the divider */
.scroll-compare--js .scroll-compare__view {
  gap: 0; aspect-ratio: 1; overflow: hidden; border-radius: calc(var(--radius-2xl) - 0.625rem);
  cursor: ew-resize; touch-action: pan-y; -webkit-user-select: none; user-select: none;
}
.scroll-compare--js .scroll-compare__view::after { content: ""; position: absolute; inset: 0; z-index: 1; pointer-events: none; background: linear-gradient(115deg, color-mix(in srgb, var(--surface-light) 16%, transparent), transparent 38%); }
.scroll-compare--js .scroll-compare__figure { grid-area: 1 / 1; border-radius: 0; }
.scroll-compare--js .scroll-compare__figure img { height: 100%; aspect-ratio: auto; }
.scroll-compare--js .scroll-compare__figure--after { clip-path: inset(0 0 0 calc((100 - var(--scroll-compare-v)) * 1%)); }
.scroll-compare--js .scroll-compare__figure--before .scroll-compare__label { opacity: clamp(0, calc((100 - var(--scroll-compare-v) - var(--scroll-compare-lb)) / 6), 1); }
.scroll-compare--js .scroll-compare__figure--after .scroll-compare__label { left: auto; right: 0.75rem; opacity: clamp(0, calc((var(--scroll-compare-la) - 100 + var(--scroll-compare-v)) / 6), 1); }
.scroll-compare.is-resync { transition: --scroll-compare-v var(--dur-4) var(--ease-out); }

/* Divider: a vertical brand-gradient line; the glass handle rides it but never leaves the frame */
.scroll-compare__divider, .scroll-compare__handle { display: none; }
.scroll-compare--js .scroll-compare__view { container-type: inline-size; }
.scroll-compare--js .scroll-compare__divider { display: block; position: absolute; inset: 0; z-index: 2; pointer-events: none; transform: translateX(calc((100 - var(--scroll-compare-v)) * 1%)); }
.scroll-compare__divider::before {
  content: ""; position: absolute; inset-block: 0; left: -1px; width: 2px;
  background: linear-gradient(to bottom, transparent, var(--primary) 18%, var(--primary-2) 82%, transparent);
  box-shadow: 0 0 0 1px color-mix(in srgb, var(--surface-light) 45%, transparent), 0 0 18px color-mix(in srgb, var(--primary) 55%, transparent);
}
.scroll-compare--js .scroll-compare__handle {
  position: absolute; z-index: 2; top: 50%; left: calc((100 - var(--scroll-compare-v)) * 1%); display: grid; place-items: center; width: 3.25rem; height: 3.25rem;
  translate: -50% -50%; border-radius: var(--radius-full); pointer-events: none;
  background: color-mix(in srgb, var(--surface-light) 72%, transparent); color: var(--text-main);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 85%, transparent), var(--highlight), var(--shadow-lg);
  transition: scale var(--dur-3) var(--ease-spring);
}
/* With container units: transform-only, clamped so the circle stays whole at either end of the sweep */
@supports (width: 1cqw) {
  .scroll-compare--js .scroll-compare__handle { left: 0; translate: calc(clamp(2rem, (100 - var(--scroll-compare-v)) * 1cqw, 100cqw - 2rem) - 50%) -50%; }
}
.scroll-compare__handle svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.scroll-compare--js .scroll-compare__view:hover .scroll-compare__handle { scale: 1.06; }
.scroll-compare--js .scroll-compare__view.is-dragging .scroll-compare__handle { scale: 0.94; }

/* The native range: invisible, keyboard- and AT-operable; pointer drags are handled on the photo */
.scroll-compare__range { position: absolute; inset: 0; z-index: 3; width: 100%; height: 100%; margin: 0; opacity: 0; pointer-events: none; direction: rtl; }
.scroll-compare__range[hidden] { display: none; }
.scroll-compare__range:focus-visible ~ .scroll-compare__handle { outline: 2px solid var(--primary); outline-offset: 3px; }

/* "Finished in 9 days": static without JS, springs in near the end with JS */
.scroll-compare__chip {
  position: absolute; z-index: 2; right: 0.75rem; bottom: 0.75rem; display: flex; align-items: center; gap: 0.625rem; margin: 0; padding: 0.4375rem 0.875rem 0.4375rem 0.4375rem;
  border-radius: var(--radius-full); background: color-mix(in srgb, var(--surface-light) 88%, transparent); color: var(--text-main); box-shadow: var(--highlight), var(--shadow-lg); pointer-events: none;
}
.scroll-compare__chip-icon { display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: var(--radius-full); background: var(--success); color: var(--surface-light); }
.scroll-compare__chip-icon svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.scroll-compare__chip strong { display: block; font: 600 0.875rem/1.2 var(--font-display); letter-spacing: -0.01em; }
.scroll-compare__chip small { color: color-mix(in srgb, var(--text-main) 75%, var(--surface-light)); font: 500 0.6875rem/1.4 var(--font-mono); }
.scroll-compare--js .scroll-compare__chip {
  top: 0.75rem; bottom: auto; opacity: 0; scale: 0.6; translate: 0 0.5rem; transform-origin: 100% 0;
  transition: opacity var(--dur-3) var(--ease-out), scale var(--dur-4) var(--ease-spring), translate var(--dur-4) var(--ease-spring);
}
.scroll-compare--js .scroll-compare__chip.is-shown { opacity: 1; scale: 1; translate: 0 0; }
@supports (backdrop-filter: blur(1px)) {
  .scroll-compare__label, .scroll-compare__chip, .scroll-compare__handle { backdrop-filter: blur(var(--blur-md)) saturate(1.6); }
}

/* Hint under the frame (JS only); the scroll half only while pinned */
.scroll-compare__hint { display: none; margin: 0; color: var(--text-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.04em; text-align: center; }
.scroll-compare--js .scroll-compare__hint { display: block; }
.scroll-compare__hint-scroll { display: none; }
.scroll-compare--pinned .scroll-compare__hint-scroll { display: inline; }

/* Pinned: a tall track and a sticky stage; the frame shrinks to fit short viewports */
.scroll-compare--pinned { height: 300vh; height: 300svh; }
.scroll-compare--pinned .scroll-compare__stage { position: sticky; top: 0; display: grid; align-items: center; height: 100vh; height: 100svh; overflow: hidden; }
.scroll-compare--pinned .scroll-compare__inner { padding-block: clamp(1.25rem, 4vh, 3rem); }
.scroll-compare--pinned .scroll-compare__device { width: min(100%, calc(100vh - 18rem)); width: min(100%, calc(100svh - 18rem)); }

@media (min-width: 768px) {
  .scroll-compare { --scroll-compare-lb: 16; --scroll-compare-la: 85; }
  .scroll-compare:not(.scroll-compare--js) .scroll-compare__view { grid-template-columns: 1fr 1fr; }
  .scroll-compare--js .scroll-compare__view { aspect-ratio: 16 / 10; }
  .scroll-compare__label { left: 0.875rem; bottom: 0.875rem; }
  .scroll-compare--js .scroll-compare__figure--after .scroll-compare__label { right: 0.875rem; }
  .scroll-compare--pinned .scroll-compare__device { width: min(100%, calc((100vh - 16rem) * 1.6)); width: min(100%, calc((100svh - 16rem) * 1.6)); }
}
@media (prefers-reduced-motion: reduce) {
  .scroll-compare-demo *, .scroll-compare-demo *::before, .scroll-compare-demo *::after { animation: none !important; }
}
@keyframes scroll-compare-bob { 50% { transform: translateY(4px); } }
```

## JS

```js
// Shared recipe: 0 when the track's top reaches the viewport top, 1 when its bottom reaches the viewport bottom
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? Math.min(1, Math.max(0, -r.top / range)) : 0; };

document.querySelectorAll('[data-scroll-compare]').forEach((root) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const view = root.querySelector('.scroll-compare__view');
  const range = root.querySelector('.scroll-compare__range');
  const chip = root.querySelector('.scroll-compare__chip');
  let near = false, frame = 0, user = false, drag = false, timer = 0, shown = -1;
  root.classList.add('scroll-compare--js');
  range.hidden = false;

  // Draw a reveal amount (0–100% of the after photo): divider, clip, labels and chip all follow --scroll-compare-v
  const show = (v) => {
    root.style.setProperty('--scroll-compare-v', v.toFixed(2));
    chip.classList.toggle('is-shown', v >= 88);
    const rounded = Math.round(v);
    if (rounded === shown) return;
    shown = rounded;
    range.value = String(rounded);
    range.setAttribute('aria-valuetext', `${rounded}% of the after photo shown`);
  };

  // Pinned: scroll sweeps the divider between 12% and 84% of the track, unless the user has taken over
  const update = () => {
    frame = 0;
    if (!reduce.matches && !user) show(Math.min(1, Math.max(0, (progress(root) - 0.12) / 0.72)) * 100);
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(update); };
  const take = (v) => { user = true; show(v); };
  const mode = () => {
    root.classList.toggle('scroll-compare--pinned', !reduce.matches);
    user = false;
    if (reduce.matches) show(50);
    else update();
  };

  // Direct manipulation: a mouse press jumps and drags; touch drags horizontally (vertical swipes still scroll)
  const fromPointer = (e) => {
    const r = view.getBoundingClientRect();
    return Math.min(100, Math.max(0, ((r.right - e.clientX) / r.width) * 100));
  };
  view.addEventListener('pointerdown', (e) => {
    if (e.button !== 0) return;
    e.preventDefault();
    drag = true;
    view.setPointerCapture(e.pointerId);
    if (e.pointerType === 'mouse') take(fromPointer(e));
  });
  view.addEventListener('pointermove', (e) => {
    if (!drag) return;
    view.classList.add('is-dragging');
    take(fromPointer(e));
  });
  const drop = () => { drag = false; view.classList.remove('is-dragging'); };
  view.addEventListener('pointerup', drop);
  view.addEventListener('pointercancel', drop);
  range.addEventListener('input', () => take(Number(range.value)));

  // Scrolling again hands control back to scroll; the divider glides to the scroll position
  addEventListener('scroll', () => {
    if (user && !drag && !reduce.matches) {
      user = false;
      root.classList.add('is-resync');
      clearTimeout(timer);
      timer = setTimeout(() => root.classList.remove('is-resync'), 600);
    }
    queue();
  }, { passive: true });

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; queue(); }).observe(root);
  addEventListener('resize', queue);
  reduce.addEventListener('change', mode);
  mode();
});
```

## Notes

- The control is a real `<input type="range">` named "Reveal after photo", so the APG slider semantics come for free. Its value is the share of the after photo shown, with a matching `aria-valuetext`. It's invisible and ignores the pointer, and the glass handle shows its focus ring. `direction: rtl` puts 0% on the right, so ← and ↑ reveal more and the handle moves the way the key points; Page Up/Down step 10%, Home/End jump to the ends. Both photos stay `<figure>`s with real `alt` text and captions. The chip and hint are decorative; the nine-day fact is also in the lead.
- Pointer drags are handled on the photo, so the whole frame is the hit area. Mouse presses jump and drag. Touch follows horizontal drags while vertical swipes keep scrolling the page (`touch-action: pan-y`). Dragging or the keys take over until the next scroll; then the divider glides back to the scroll position through the registered `--scroll-compare-v`, or snaps in browsers without `@property`.
- With `prefers-reduced-motion` (switched live) nothing is pinned and nothing moves on scroll: the comparison opens at 50% and is purely manual. Without JS the two photos sit side by side (stacked on phones) as captioned figures, with the chip shown statically.
- Contrast: labels, chip and handle sit on ≥ 86% white glass, so `--text-main` stays ≥ 10:1 over any photo and the chip's mono dates (75% mix) ≥ 4.9:1. On white, the eyebrow (`--primary`) is 5.2:1 and the lead (`--text-muted`) 4.8:1.
- Tuning: the track is 300vh with the sweep between 12% and 84% of it (in `update`), and the chip appears at 88% revealed. `--scroll-compare-lb`/`-la` mark where each label meets the divider (set per breakpoint). The frame is square on phones and 16:10 from 768px, and while pinned it shrinks to fit short viewports.
- Support: `clip-path: inset()`, the standalone `scale`/`translate` properties and `svh` (with a `vh` fallback) cover current engines; the glass falls back to near-opaque white without `backdrop-filter`.
