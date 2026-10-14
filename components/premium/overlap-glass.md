# Overlapping Glass Panels

Three glass panels straddle the seam between a vivid brand-gradient section and the light section below it, so they literally blend the two containers. Each one blurs and saturates whatever is beneath it: its top half glows with the gradient and a pool of amber, teal or violet light, while its bottom half reads light. On scroll the panels drift at slightly different speeds, and under a mouse they tilt with a specular highlight that follows the cursor. On phones the first two sit side by side across the seam and the third becomes a full-width card below. Depends on `tokens/variables.css`.

**Motion:** scroll parallax at three speeds (one rAF scroll listener writing `--overlap-glass-p`; follows the scroll directly, no easing) · pointer tilt (`--dur-3`, `--ease-out`) · specular highlight fade (`--dur-3`) · button lift and press (`--dur-2`, `--ease-spring`).

## HTML

```html
<div class="overlap-glass" data-overlap-glass>
  <section class="overlap-glass__top" aria-labelledby="overlap-glass-title">
    <div class="overlap-glass__glow" aria-hidden="true">
      <span class="overlap-glass__pool overlap-glass__pool--amber"></span>
      <span class="overlap-glass__pool overlap-glass__pool--teal"></span>
      <span class="overlap-glass__pool overlap-glass__pool--violet"></span>
    </div>
    <div class="overlap-glass__inner">
      <p class="overlap-glass__eyebrow">Brand · Springfield</p>
      <h2 id="overlap-glass-title" class="overlap-glass__title">Home repairs, without the runaround.</h2>
      <p class="overlap-glass__lead">One call books a licensed pro, a fixed price and a two-hour arrival window. Most jobs are finished the same day.</p>
      <div class="overlap-glass__actions">
        <a class="overlap-glass__btn" href="#book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="overlap-glass__btn overlap-glass__btn--ghost" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
    </div>
  </section>

  <ul class="overlap-glass__panels" role="list">
    <li class="overlap-glass__panel">
      <div class="overlap-glass__head">
        <span class="overlap-glass__icon overlap-glass__icon--star" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg></span>
        <p class="overlap-glass__figure">4.9<span class="overlap-glass__sr"> out of 5</span></p>
      </div>
      <div class="overlap-glass__foot">
        <p class="overlap-glass__label">from 2,300 reviews</p>
        <p class="overlap-glass__note">Google · Yelp · Nextdoor</p>
      </div>
    </li>
    <li class="overlap-glass__panel">
      <div class="overlap-glass__head">
        <span class="overlap-glass__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M12 7v5l3 2M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z" /></svg></span>
        <p class="overlap-glass__figure">Same-day</p>
      </div>
      <div class="overlap-glass__foot">
        <p class="overlap-glass__label">in 92% of Springfield</p>
        <p class="overlap-glass__note">Westlake · Northside · Riverside</p>
      </div>
    </li>
    <li class="overlap-glass__panel">
      <div class="overlap-glass__head">
        <span class="overlap-glass__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M12 3l7 3v5c0 4.5-3 8.3-7 10-4-1.7-7-5.5-7-10V6zM9 12l2 2 4-4" /></svg></span>
        <p class="overlap-glass__figure overlap-glass__figure--words">Licensed · Bonded · Insured</p>
      </div>
      <div class="overlap-glass__foot">
        <p class="overlap-glass__label">State licence PL-55012</p>
        <p class="overlap-glass__note">$2M liability cover on every job</p>
      </div>
    </li>
  </ul>

  <section class="overlap-glass__bottom" aria-labelledby="overlap-glass-promise">
    <div class="overlap-glass__inner">
      <p class="overlap-glass__kicker">After you call</p>
      <h2 id="overlap-glass-promise" class="overlap-glass__subtitle">A fixed price before we start. A two-year guarantee after.</h2>
      <ul class="overlap-glass__points" role="list">
        <li class="overlap-glass__point">
          <span class="overlap-glass__point-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8zM14 3v5h5M9 13h6M9 17h4" /></svg></span>
          <h3>Upfront quote</h3>
          <p>Itemised and fixed before a tool comes out of the van.</p>
        </li>
        <li class="overlap-glass__point">
          <span class="overlap-glass__point-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z" /></svg></span>
          <h3>Tidy crews</h3>
          <p>Shoe covers, dust sheets and a proper clean-up before we leave.</p>
        </li>
        <li class="overlap-glass__point">
          <span class="overlap-glass__point-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M3 12a9 9 0 1 0 3-6.7L3 8M3 3v5h5" /></svg></span>
          <h3>Two-year guarantee</h3>
          <p>If our fix fails, we come back and put it right for free.</p>
        </li>
      </ul>
      <a class="overlap-glass__more" href="#guarantee">
        Read the guarantee
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
      </a>
    </div>
  </section>
</div>
```

## CSS

```css
/* Root: the light surface the panels' lower halves sit on */
.overlap-glass {
  --overlap-glass-lift: 5.5rem;
  position: relative; overflow: clip; background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
}
.overlap-glass__inner { position: relative; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }

/* Top: vivid gradient with three pools of light centred on the seam (they stop short of the copy) */
.overlap-glass__top {
  position: relative; overflow: clip; color: var(--text-inverse);
  background:
    radial-gradient(80% 60% at 50% 0%, color-mix(in srgb, var(--surface-deep) 35%, transparent), transparent 70%),
    linear-gradient(160deg, color-mix(in srgb, var(--primary) 88%, var(--surface-deep)) 10%, color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
}
.overlap-glass__top::after { content: ""; position: absolute; inset: auto 0 0; height: 1px; background: color-mix(in srgb, var(--surface-light) 40%, transparent); }
.overlap-glass__glow { position: absolute; inset: 0; pointer-events: none; }
.overlap-glass__pool { position: absolute; bottom: 0; width: min(18rem, 62vw); aspect-ratio: 1; border-radius: 50%; translate: -50% 50%; }
.overlap-glass__pool--amber { left: 18%; background: radial-gradient(closest-side, color-mix(in srgb, var(--accent) 75%, transparent), transparent); }
.overlap-glass__pool--teal { left: 50%; background: radial-gradient(closest-side, color-mix(in srgb, color-mix(in srgb, var(--primary-2) 50%, var(--surface-light)) 70%, transparent), transparent); }
.overlap-glass__pool--violet { left: 82%; background: radial-gradient(closest-side, color-mix(in srgb, color-mix(in srgb, var(--primary) 70%, var(--danger)) 75%, transparent), transparent); }
.overlap-glass__top .overlap-glass__inner {
  display: grid; justify-items: center; text-align: center;
  padding-top: clamp(4.5rem, 10vw, 7.5rem); padding-bottom: calc(var(--overlap-glass-lift) + 4.5rem);
}
.overlap-glass__eyebrow {
  margin: 0; padding: 0.4375rem 0.875rem; border-radius: var(--radius-full); background: var(--glass-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.overlap-glass__title { max-width: 18ch; margin: 1.25rem 0 0; font: 600 clamp(2.25rem, 1.2rem + 4vw, 4.5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.overlap-glass__lead { max-width: 36rem; margin: 1.25rem 0 0; color: color-mix(in srgb, var(--text-inverse) 90%, transparent); font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.overlap-glass__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.overlap-glass__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem/1.2 var(--font-sans); text-decoration: none;
  box-shadow: var(--highlight), 0 14px 36px -14px color-mix(in srgb, var(--surface-deep) 60%, transparent);
  transition: transform var(--dur-2) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.overlap-glass__btn:hover { transform: translateY(-2px); }
.overlap-glass__btn:active { transform: scale(0.97); }
.overlap-glass__btn--ghost { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.overlap-glass :is(.overlap-glass__btn, .overlap-glass__more, .overlap-glass__icon, .overlap-glass__point-icon) svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.overlap-glass__btn svg, .overlap-glass__more svg { transition: transform var(--dur-3) var(--ease-spring); }
.overlap-glass :is(.overlap-glass__btn:not(.overlap-glass__btn--ghost), .overlap-glass__more):hover svg { transform: translateX(3px); }
.overlap-glass__btn:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Panels: pulled up across the seam. No z-index or effects on this list: it must not become a backdrop root */
.overlap-glass__panels {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.75rem;
  max-width: var(--container-max); margin: calc(var(--overlap-glass-lift) * -1) auto 0; padding: 0 var(--gutter); list-style: none;
}
.overlap-glass__panel {
  --overlap-glass-speed: 2rem;
  position: relative; isolation: isolate; display: flex; flex-direction: column; justify-content: space-between; gap: 1rem;
  min-height: calc(var(--overlap-glass-lift) * 2); padding: 1rem; border-radius: var(--radius-2xl);
  background: var(--glass); color: var(--text-main);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 60%, transparent), var(--highlight), var(--shadow-xl);
  translate: 0 calc((0.5 - var(--overlap-glass-p, 0.5)) * var(--overlap-glass-speed));
  transform: perspective(60rem) rotateX(var(--overlap-glass-rx, 0deg)) rotateY(var(--overlap-glass-ry, 0deg));
  transition: transform var(--dur-3) var(--ease-out);
}
.overlap-glass__panel:nth-child(2) { --overlap-glass-speed: 3.5rem; }
.overlap-glass__panel:nth-child(3) { --overlap-glass-speed: 2.5rem; grid-column: 1 / -1; min-height: 0; }
/* Real glass where supported: a thin fill, blur and saturation, then an inner tint so dark text holds 4.5:1 over both halves */
@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .overlap-glass__panel {
    background: color-mix(in srgb, var(--surface-light) 14%, transparent);
    -webkit-backdrop-filter: blur(var(--blur-lg)) saturate(1.4);
    backdrop-filter: blur(var(--blur-lg)) saturate(1.4);
  }
  .overlap-glass__panel::before {
    content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit;
    background: linear-gradient(180deg, color-mix(in srgb, var(--surface-light) 52%, transparent), color-mix(in srgb, var(--surface-light) 34%, transparent));
  }
}
/* Specular highlight under the text, following the cursor */
.overlap-glass__panel::after {
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none; opacity: 0;
  background: radial-gradient(16rem circle at var(--overlap-glass-mx, 50%) var(--overlap-glass-my, 0%), color-mix(in srgb, var(--surface-light) 60%, transparent), transparent 60%);
  transition: opacity var(--dur-3) var(--ease-out);
}
.overlap-glass__panel.is-lit::after { opacity: 1; }

/* Panel content: the figure rides the coloured half, the label the light half */
.overlap-glass__head { display: grid; justify-items: start; gap: 0.75rem; }
.overlap-glass__icon {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: var(--radius-lg);
  background: color-mix(in srgb, var(--surface-light) 75%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 90%, transparent), var(--shadow-sm);
}
.overlap-glass .overlap-glass__icon--star svg { color: var(--accent); fill: currentColor; stroke-width: 1.5; }
.overlap-glass__figure { margin: 0; font: 600 clamp(1.5rem, 1rem + 2.5vw, 3rem)/1 var(--font-display); letter-spacing: var(--tracking-display); }
.overlap-glass__figure--words { font-size: clamp(1.125rem, 0.9rem + 1vw, 1.5rem); line-height: 1.2; letter-spacing: var(--tracking-tight); text-wrap: balance; }
.overlap-glass__foot { padding-top: 0.75rem; border-top: 1px solid color-mix(in srgb, var(--text-main) 12%, transparent); }
.overlap-glass__label { margin: 0; font-size: 0.9375rem; font-weight: 600; line-height: 1.35; }
.overlap-glass__note { margin: 0.375rem 0 0; font: 500 0.6875rem/1.45 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.overlap-glass__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Bottom: the light section */
.overlap-glass__bottom .overlap-glass__inner { padding-top: clamp(3.5rem, 7vw, 5rem); padding-bottom: clamp(4rem, 9vw, 6.5rem); }
.overlap-glass__kicker { margin: 0; color: var(--primary); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.overlap-glass__subtitle { max-width: 34rem; margin: 0.75rem 0 0; font: 600 clamp(1.75rem, 1.2rem + 2vw, 2.5rem)/1.1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.overlap-glass__points { display: grid; gap: 1.5rem; margin: 2.5rem 0 0; padding: 0; list-style: none; }
.overlap-glass__point { display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 0.25rem 1rem; }
.overlap-glass__point-icon {
  grid-row: span 2; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-lg);
  background: color-mix(in srgb, var(--primary) 8%, var(--surface-light)); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 18%, transparent); color: var(--primary);
}
.overlap-glass__point h3 { margin: 0; font: 600 1.0625rem/1.3 var(--font-display); letter-spacing: -0.01em; }
.overlap-glass__point p { margin: 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.55; }
.overlap-glass__more {
  display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; margin-top: 2rem; color: var(--primary); font-weight: 600;
  text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 0.3em;
}
.overlap-glass__more:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

@media (min-width: 768px) {
  .overlap-glass { --overlap-glass-lift: 7rem; }
  .overlap-glass__panels { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.5rem; }
  .overlap-glass__panel { padding: 1.5rem; }
  .overlap-glass__panel:nth-child(3) { grid-column: auto; min-height: calc(var(--overlap-glass-lift) * 2); }
  .overlap-glass__points { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 2rem; }
}
@media (prefers-reduced-motion: reduce) {
  .overlap-glass__panel { translate: none; transform: none; }
}
```

## JS

```js
document.querySelectorAll('[data-overlap-glass]').forEach((root) => {
  const panels = [...root.querySelectorAll('.overlap-glass__panel')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let frame = 0;

  // Parallax: one progress value (0–1) while the component crosses the viewport; each panel scales it by its own speed in CSS
  const update = () => {
    frame = 0;
    if (reduce.matches) return root.style.removeProperty('--overlap-glass-p');
    const r = root.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, (innerHeight - r.top) / (innerHeight + r.height)));
    root.style.setProperty('--overlap-glass-p', p.toFixed(4));
  };
  const onScroll = () => { if (!frame) frame = requestAnimationFrame(update); };
  new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) { addEventListener('scroll', onScroll, { passive: true }); onScroll(); }
    else removeEventListener('scroll', onScroll);
  }, { rootMargin: '120px 0px' }).observe(root);
  addEventListener('resize', onScroll, { passive: true });

  // Tilt towards the cursor with a specular highlight that follows it (mouse only)
  panels.forEach((panel) => {
    let raf = 0;
    const reset = () => {
      cancelAnimationFrame(raf);
      raf = 0;
      panel.classList.remove('is-lit');
      panel.style.setProperty('--overlap-glass-rx', '0deg');
      panel.style.setProperty('--overlap-glass-ry', '0deg');
    };
    panel.addEventListener('pointermove', (e) => {
      if (e.pointerType !== 'mouse' || reduce.matches || raf) return;
      raf = requestAnimationFrame(() => {
        raf = 0;
        const r = panel.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width;
        const y = (e.clientY - r.top) / r.height;
        panel.style.setProperty('--overlap-glass-mx', `${(x * 100).toFixed(1)}%`);
        panel.style.setProperty('--overlap-glass-my', `${(y * 100).toFixed(1)}%`);
        panel.style.setProperty('--overlap-glass-ry', `${((x - 0.5) * 12).toFixed(2)}deg`);
        panel.style.setProperty('--overlap-glass-rx', `${((0.5 - y) * 10).toFixed(2)}deg`);
        panel.classList.add('is-lit');
      });
    });
    panel.addEventListener('pointerleave', reset);
  });
});
```

## Notes

- **Glass:** each panel runs `backdrop-filter: blur(var(--blur-lg)) saturate(1.4)` over whatever is beneath it. Its top half picks up the gradient plus the amber, teal or violet pool centred on the seam, so each card tints differently, while its bottom half sits over the light section and reads white. The panels straddle the seam through a negative top margin equal to `--overlap-glass-lift`.
- **Inner tint for contrast:** a `::before` layer adds 52% white at the top, fading to 34% at the bottom. With the panel's own 14% fill, that's 59% white over the vivid half and 43% over the light half. All panel text is `--text-main`: at least 7.6:1 over the deepest saturated blue, at least 5.8:1 even if parallax lifts a label above the seam, and 14.6:1 over the light half. Without `backdrop-filter`, panels fall back to solid `--glass` (at least 9.5:1).
- **Backdrop-root gotcha:** nothing between a panel and the sections may use `filter`, `opacity` below 1, `mask`, `clip-path`, `mix-blend-mode`, `backdrop-filter` or `will-change` on those properties. Any of them would make the blur sample an empty layer. That's why the panel list has no `z-index` (the panels paint above the top section by DOM order) and the panels never fade in with `opacity`.
- **Motion:** one rAF-throttled, passive scroll listener, gated by IntersectionObserver, writes `--overlap-glass-p`, and each panel drifts by its own `--overlap-glass-speed` (2, 3.5 and 2.5rem). Tilt and the specular highlight are mouse-only. Under reduced motion, parallax and tilt are off and the panels sit flat; without JS the layout is identical, only still.
- **Top section:** white text measures 5.9–6.1:1 and the 90%-white lead at least 5.1:1 on the gradient. The pools stop short of the copy; moved up into it, they would drop the lead to 4.4:1. The bottom section measures 14.6 (text), 4.8 (muted) and 5.2 (link).
- On phones the first two panels share a row across the seam and the third becomes a full-width card on the light section. To retheme, recolour the three pools: they decide each panel's tint.
