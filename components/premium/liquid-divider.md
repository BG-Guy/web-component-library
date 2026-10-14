# Liquid Divider

An organic wave seam between two sections, built from three stacked SVG wave tiles: a translucent brand tint at the back, a translucent wash of the next section's colour, and a solid front wave in that colour. As the seam scrolls past, each layer slides at its own speed and direction, and scroll speed makes the waves swell. When you stop, they settle on damped springs, so the seam ripples with your scroll and never moves on its own. It has placement modifiers (`--bottom`, `--top` flips it) and a `--calm` variant; on phones each wave period stays at least 56rem wide, so the swell stays long and gentle. Depends on `tokens/variables.css`.

**Motion:** per-layer phase slide (scroll scrub, `translate` of a seamless 2× tile) · amplitude swell from scroll speed with per-layer damped springs (`scale`, rAF only while settling) · card hover lift (`--dur-3` `--ease-spring`).

## HTML

```html
<div class="liquid-divider-demo">
  <section class="liquid-divider-demo__section liquid-divider-demo__section--deep" aria-labelledby="liquid-divider-demo-title-1">
    <div class="liquid-divider-demo__inner">
      <p class="liquid-divider-demo__eyebrow">Brand Plumbing · Springfield</p>
      <h2 id="liquid-divider-demo-title-1" class="liquid-divider-demo__title">Leaks don't wait. Neither do we.</h2>
      <p class="liquid-divider-demo__lead">Burst pipe at 2 a.m.? A licensed plumber is on the way within the hour, with the parts already on the van.</p>
      <dl class="liquid-divider-demo__stats">
        <div><dt>Average arrival</dt><dd>38 min</dd></div>
        <div><dt>Emergency line</dt><dd>24/7</dd></div>
        <div><dt>1,200+ reviews</dt><dd>4.9</dd></div>
      </dl>
      <span class="liquid-divider-demo__hint" aria-hidden="true">Scroll
        <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
      </span>
    </div>

    <!-- Seam on the bottom edge: rises into this section in the colour of the next one -->
    <div class="liquid-divider liquid-divider--bottom" aria-hidden="true" data-liquid-divider>
      <svg class="liquid-divider__wave liquid-divider__wave--far" viewBox="0 0 2880 160" preserveAspectRatio="none" focusable="false">
        <path d="M0 24C207 24 253 80 460 80C658 80 702 18 900 18C1026 18 1054 62 1180 62C1297 62 1323 24 1440 24C1647 24 1693 80 1900 80C2098 80 2142 18 2340 18C2466 18 2494 62 2620 62C2737 62 2763 24 2880 24V161H0Z" />
      </svg>
      <svg class="liquid-divider__wave liquid-divider__wave--mid" viewBox="0 0 2880 160" preserveAspectRatio="none" focusable="false">
        <path d="M0 42C135 42 165 94 300 94C480 94 520 34 700 34C853 34 887 88 1040 88C1220 88 1260 42 1440 42C1575 42 1605 94 1740 94C1920 94 1960 34 2140 34C2293 34 2327 88 2480 88C2660 88 2700 42 2880 42V161H0Z" />
      </svg>
      <svg class="liquid-divider__wave liquid-divider__wave--front" viewBox="0 0 2880 160" preserveAspectRatio="none" focusable="false">
        <path d="M0 66C162 66 198 110 360 110C540 110 580 56 760 56C913 56 947 112 1100 112C1253 112 1287 66 1440 66C1602 66 1638 110 1800 110C1980 110 2020 56 2200 56C2353 56 2387 112 2540 112C2693 112 2727 66 2880 66V161H0Z" />
      </svg>
    </div>
  </section>

  <section class="liquid-divider-demo__section liquid-divider-demo__section--light" aria-labelledby="liquid-divider-demo-title-2">
    <div class="liquid-divider-demo__inner">
      <p class="liquid-divider-demo__eyebrow">What we fix</p>
      <h2 id="liquid-divider-demo-title-2" class="liquid-divider-demo__title">Fixed right the first time</h2>
      <ul class="liquid-divider-demo__cards" role="list">
        <li class="liquid-divider-demo__card">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z" /><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5" /></svg>
          <h3>Leak detection</h3>
          <p>Acoustic and thermal tracing finds hidden leaks without tearing out walls.</p>
        </li>
        <li class="liquid-divider-demo__card">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z" /></svg>
          <h3>Pipe repair</h3>
          <p>Copper, PEX and cast iron repaired or replaced, with a two-year workmanship warranty.</p>
        </li>
        <li class="liquid-divider-demo__card">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3c1 3 4 4.5 4 8.5a4 4 0 0 1-8 0c0-1.6.8-2.8 1.8-3.7.2 1.5 1 2.2 2 2.2 0-2.5-.6-4.6.2-7z" /></svg>
          <h3>Water heaters</h3>
          <p>Tank and tankless installs, same day in Westlake, Northside and Riverside.</p>
        </li>
      </ul>
    </div>
  </section>

  <section class="liquid-divider-demo__section liquid-divider-demo__section--brand" aria-labelledby="liquid-divider-demo-title-3">
    <!-- Flipped, calmer seam on the top edge: hangs down in the colour of the section above -->
    <div class="liquid-divider liquid-divider--top liquid-divider--calm" style="--liquid-divider-tint: var(--surface-light)" aria-hidden="true" data-liquid-divider>
      <svg class="liquid-divider__wave liquid-divider__wave--far" viewBox="0 0 2880 160" preserveAspectRatio="none" focusable="false">
        <path d="M0 24C207 24 253 80 460 80C658 80 702 18 900 18C1026 18 1054 62 1180 62C1297 62 1323 24 1440 24C1647 24 1693 80 1900 80C2098 80 2142 18 2340 18C2466 18 2494 62 2620 62C2737 62 2763 24 2880 24V161H0Z" />
      </svg>
      <svg class="liquid-divider__wave liquid-divider__wave--mid" viewBox="0 0 2880 160" preserveAspectRatio="none" focusable="false">
        <path d="M0 42C135 42 165 94 300 94C480 94 520 34 700 34C853 34 887 88 1040 88C1220 88 1260 42 1440 42C1575 42 1605 94 1740 94C1920 94 1960 34 2140 34C2293 34 2327 88 2480 88C2660 88 2700 42 2880 42V161H0Z" />
      </svg>
      <svg class="liquid-divider__wave liquid-divider__wave--front" viewBox="0 0 2880 160" preserveAspectRatio="none" focusable="false">
        <path d="M0 66C162 66 198 110 360 110C540 110 580 56 760 56C913 56 947 112 1100 112C1253 112 1287 66 1440 66C1602 66 1638 110 1800 110C1980 110 2020 56 2200 56C2353 56 2387 112 2540 112C2693 112 2727 66 2880 66V161H0Z" />
      </svg>
    </div>
    <div class="liquid-divider-demo__inner">
      <h2 id="liquid-divider-demo-title-3" class="liquid-divider-demo__title">Book a plumber in two minutes</h2>
      <p class="liquid-divider-demo__lead">Upfront pricing, a two-hour arrival window and a text when we're five minutes out.</p>
      <div class="liquid-divider-demo__actions">
        <a class="liquid-divider-demo__btn" href="#book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="liquid-divider-demo__tel" href="tel:+15555550123">(555) 555-0123</a>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* The seam: a transparent box on a section edge, tall enough (1.8×) to hold the swell without clipping */
.liquid-divider {
  --liquid-divider-h: clamp(4rem, 3rem + 6vw, 9rem);
  --liquid-divider-fill: var(--surface-light);
  --liquid-divider-tint: var(--primary-2);
  --liquid-divider-pace: 1;
  --liquid-divider-amp: 1;
  position: absolute; left: 0; right: 0; bottom: -1px; height: calc(var(--liquid-divider-h) * 1.8);
  overflow: hidden; pointer-events: none;
}
.liquid-divider--bottom { top: auto; bottom: -1px; scale: none; }
.liquid-divider--top { top: -1px; bottom: auto; scale: 1 -1; }
.liquid-divider--calm { --liquid-divider-h: clamp(3rem, 2.5rem + 3vw, 5.5rem); --liquid-divider-pace: 0.45; --liquid-divider-amp: 0.4; }

/* Soft light rising off the seam */
.liquid-divider::before {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(to top, color-mix(in srgb, var(--liquid-divider-tint) 24%, transparent) 20%, transparent 70%);
}

/* Wave tiles: two periods wide, slid by phase (0–1 = one period, set by JS, static offset without it) and stretched upward by the swell */
.liquid-divider__wave {
  position: absolute; left: 0; bottom: 0; display: block;
  width: calc(2 * max(100%, 56rem)); height: calc(100% / 1.8);
  transform-origin: 0 100%; will-change: translate, scale;
  translate: calc(var(--liquid-divider-x, var(--liquid-divider-o)) * -50%) 0;
  scale: 1 calc(1 + var(--liquid-divider-s, 0) * var(--liquid-divider-lift) * var(--liquid-divider-amp));
}
.liquid-divider__wave--far { --liquid-divider-o: 0.4; --liquid-divider-v: 0.35; --liquid-divider-lift: 0.55; fill: color-mix(in srgb, var(--liquid-divider-tint) 42%, transparent); }
.liquid-divider__wave--mid { --liquid-divider-o: 0.8; --liquid-divider-v: -0.55; --liquid-divider-lift: 0.45; fill: color-mix(in srgb, var(--liquid-divider-fill) 38%, transparent); }
.liquid-divider__wave--front { --liquid-divider-o: 0; --liquid-divider-v: 0.9; --liquid-divider-lift: 0.32; fill: var(--liquid-divider-fill); }

/* Demo: deep → light → brand gradient, each with real content above the seam */
.liquid-divider-demo { font-family: var(--font-sans); }
.liquid-divider-demo__section { position: relative; }
.liquid-divider-demo__inner {
  position: relative; z-index: 1; max-width: var(--container-max); margin-inline: auto;
  padding: calc(clamp(3.5rem, 8vw, 6rem) + var(--liquid-divider-demo-top, 0rem)) var(--gutter) calc(clamp(3.5rem, 8vw, 6rem) + var(--liquid-divider-demo-bottom, 0rem));
}
.liquid-divider-demo__section--deep {
  --liquid-divider-demo-bottom: clamp(4rem, 3rem + 6vw, 9rem);
  display: grid; align-content: center; min-height: 75vh;
  background: radial-gradient(60% 70% at 85% 0%, color-mix(in srgb, var(--primary) 28%, transparent), transparent 70%), var(--surface-deep);
  color: var(--text-inverse);
}
.liquid-divider-demo__section--light { background: var(--surface-light); color: var(--text-main); }
.liquid-divider-demo__section--brand {
  --liquid-divider-demo-top: clamp(3rem, 2.5rem + 3vw, 5.5rem);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 85%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 72%, var(--surface-deep)));
  color: var(--text-inverse);
}
.liquid-divider-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.liquid-divider-demo__section--deep .liquid-divider-demo__eyebrow { color: var(--text-inverse-muted); }
.liquid-divider-demo__title {
  max-width: 18ch; margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.3rem + 3vw, 3.5rem)/1.04 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.liquid-divider-demo__lead { max-width: 34rem; margin: 1rem 0 0; font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
.liquid-divider-demo__section--deep .liquid-divider-demo__lead { color: var(--text-inverse-muted); }
.liquid-divider-demo__stats { display: flex; flex-wrap: wrap; gap: 1.25rem 2.5rem; margin: 2rem 0 0; }
.liquid-divider-demo__stats div { display: grid; gap: 0.375rem; padding-left: 1rem; border-left: 1px solid var(--border-inverse); }
.liquid-divider-demo__stats dt { color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.06em; }
.liquid-divider-demo__stats dd { margin: 0; font: 600 1.75rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.liquid-divider-demo__hint {
  display: inline-flex; align-items: center; gap: 0.375rem; margin-top: 2.5rem;
  color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.liquid-divider-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: liquid-divider-nudge 1.6s var(--ease-in-out) 3; }
.liquid-divider-demo__cards { display: grid; gap: 1rem; margin: 2.5rem 0 0; padding: 0; list-style: none; }
.liquid-divider-demo__card {
  padding: 1.5rem; border-radius: var(--radius-xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-md);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.liquid-divider-demo__card:hover { transform: translateY(-3px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-lg); }
.liquid-divider-demo__card svg {
  box-sizing: border-box; display: block; width: 2.75rem; height: 2.75rem; padding: 0.625rem; border-radius: var(--radius-lg);
  background: color-mix(in srgb, var(--primary) 10%, var(--surface-light));
  fill: none; stroke: var(--primary); stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round;
}
.liquid-divider-demo__card h3 { margin: 1rem 0 0; font: 600 1.125rem/1.3 var(--font-display); letter-spacing: var(--tracking-tight); }
.liquid-divider-demo__card p { margin: 0.5rem 0 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.55; }
.liquid-divider-demo__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 1.5rem; margin-top: 2rem; }
.liquid-divider-demo__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1.25rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem var(--font-sans); text-decoration: none;
  box-shadow: var(--highlight), 0 14px 32px -14px color-mix(in srgb, var(--surface-deep) 80%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.liquid-divider-demo__btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.liquid-divider-demo__btn:hover { transform: translateY(-2px); }
.liquid-divider-demo__btn:hover svg { translate: 3px 0; }
.liquid-divider-demo__btn:active { transform: scale(0.97); }
.liquid-divider-demo__tel {
  display: inline-flex; align-items: center; min-height: 2.75rem; color: var(--text-inverse);
  font: 500 0.9375rem var(--font-mono); text-decoration: underline; text-underline-offset: 0.3em;
}
.liquid-divider-demo__section--brand a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

@media (min-width: 768px) {
  .liquid-divider-demo__cards { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.25rem; }
}
@keyframes liquid-divider-nudge { 50% { translate: 0 4px; } }
@media (prefers-reduced-motion: reduce) {
  .liquid-divider-demo *, .liquid-divider-demo *::before, .liquid-divider-demo *::after { animation: none !important; }
}
```

## JS

```js
const clamp01 = (n) => Math.min(1, Math.max(0, n));
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
// 0 as the seam enters at the bottom of the viewport, 1 as it leaves at the top
const passage = (el) => { const r = el.getBoundingClientRect(); return clamp01((innerHeight - r.top) / (innerHeight + r.height)); };
const num = (css, name, fallback) => parseFloat(css.getPropertyValue(name)) || fallback;

document.querySelectorAll('[data-liquid-divider]').forEach((root) => {
  // Per layer: phase offset and speed from CSS, plus a damped spring for the swell (back layers softer, so it ripples)
  const layers = [...root.querySelectorAll('.liquid-divider__wave')].map((el, i) => {
    const css = getComputedStyle(el);
    return { el, o: num(css, '--liquid-divider-o', 0), v: num(css, '--liquid-divider-v', 0) * num(css, '--liquid-divider-pace', 1), x: 0, vel: 0, k: 60 + i * 35, c: 8 + i * 3 };
  });
  const start = passage(root); // phase is measured from here, so a seam in view at load never jumps
  let near = false;
  let frame = 0;
  let lastY = scrollY;
  let lastT = 0;
  let speed = 0;

  const step = (now) => {
    frame = 0;
    const dt = Math.min(0.05, Math.max(1 / 240, (now - lastT) / 1000));
    speed = Math.max(speed * 0.86, Math.abs(scrollY - lastY) / dt); // px/s, eases off between scroll events
    lastY = scrollY;
    lastT = now;
    const target = Math.min(1, speed / 2400);
    const shift = passage(root) - start;
    let busy = target > 0.002;
    layers.forEach((l) => {
      l.vel += (l.k * (target - l.x) - l.c * l.vel) * dt;
      l.x += l.vel * dt;
      if (Math.abs(l.vel) > 0.003 || Math.abs(l.x) > 0.003) busy = true;
      // The tile repeats every half of its width, so the phase can wrap without a seam
      l.el.style.setProperty('--liquid-divider-x', ((((l.o + shift * l.v) % 1) + 1) % 1).toFixed(4));
      l.el.style.setProperty('--liquid-divider-s', l.x.toFixed(4));
    });
    if (busy && near) frame = requestAnimationFrame(step); // stops once the seam has settled: no idle loop
  };
  const wake = () => {
    if (!near || frame || reduce.matches) return;
    lastY = scrollY;
    lastT = performance.now();
    frame = requestAnimationFrame(step);
  };
  const reset = () => layers.forEach((l) => {
    l.x = 0;
    l.vel = 0;
    l.el.style.removeProperty('--liquid-divider-x');
    l.el.style.removeProperty('--liquid-divider-s');
  });

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; }, { rootMargin: '10% 0px' }).observe(root);
  addEventListener('scroll', wake, { passive: true });
  addEventListener('resize', wake, { passive: true });
  reduce.addEventListener('change', () => (reduce.matches ? reset() : wake()));
});
```

## Notes

- Decorative only: the seam is `aria-hidden`, has `pointer-events: none` and sits under the section content (`z-index: 1` on the content). Its box is transparent, so it works over gradients and photos.
- To place it, put the divider inside a `position: relative` section. The default/`--bottom` modifier sits on the section's bottom edge and rises in `--liquid-divider-fill`, the next section's colour. `--top` sits on the top edge of the section below and hangs down in the colour above. Give the host section padding equal to `--liquid-divider-h` on that edge. `--liquid-divider-tint` colours the back wave and glow; `--calm` lowers the height, pace and swell.
- Without JS, and under reduced motion, the three waves render static at their offset phases. Nothing moves on its own: the rAF loop runs only while you scroll near the seam and while the springs settle (under a second), then stops.
- Contrast: the brand section mixes `--primary`/`--primary-2` with 15%/28% `--surface-deep`, so `--text-inverse` stays at 5.9:1 or more across the gradient. The light section uses `--text-main` (14.6:1) and `--text-muted` (4.8:1); the deep section uses `--text-inverse-muted` (7:1).
- Each wave path is a seamless two-period tile, and its period is never narrower than 56rem, so phones see long, gentle swells instead of a compressed zigzag. Swap the three paths for your own two-period shapes (keep the end height equal to the start height).
