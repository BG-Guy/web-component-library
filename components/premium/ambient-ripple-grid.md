# Ripple Dot Grid

A deep ambient layer: a quiet dot matrix behind the page that turns into a pond when you scroll. Each scroll burst sends a ring across the grid from alternating edges at the middle of the screen, as strong as the flick that made it; dots lift and brighten as the wave passes, and the mouse leaves a soft wake of lit dots. Waves fade, the loop stops, and the grid is still again. On phones and touch screens the grid is coarser and the canvas resolution lower. Depends on `tokens/variables.css`.

**Motion:** canvas ripple rings (radius grows ~0.75px/ms, strength decays over ~1.1s) · dot lift in radius, alpha and colour · pointer wake fading over ~0.6s · loop runs only while a wave or wake is alive.

## HTML

```html
<div class="amb-ripple-demo">
  <div class="amb-ripple" aria-hidden="true">
    <div class="amb-ripple__stage"><canvas class="amb-ripple__canvas"></canvas></div>
  </div>

  <section class="amb-ripple-demo__section amb-ripple-demo__section--hero" aria-labelledby="amb-ripple-hero-title">
    <div class="amb-ripple-demo__inner">
      <p class="amb-ripple-demo__eyebrow"><span class="amb-ripple-demo__ping"></span>Brand Leak Detection · Springfield</p>
      <h2 id="amb-ripple-hero-title" class="amb-ripple-demo__title">We hear the drip <em>before you see it.</em></h2>
      <p class="amb-ripple-demo__lead">Acoustic and thermal leak detection that finds hidden water without tearing up your floors. Most leaks are pinpointed in under an hour.</p>
      <div class="amb-ripple-demo__actions">
        <a class="amb-ripple-demo__btn amb-ripple-demo__btn--primary" href="#amb-ripple-book">
          Book a leak check
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-ripple-demo__btn" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          24/7: (555) 555-0123
        </a>
      </div>
      <p class="amb-ripple-demo__hint">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
        Scroll
      </p>
    </div>
  </section>

  <section class="amb-ripple-demo__section" aria-labelledby="amb-ripple-services-title">
    <div class="amb-ripple-demo__inner">
      <header class="amb-ripple-demo__head">
        <p class="amb-ripple-demo__eyebrow">Services</p>
        <h2 id="amb-ripple-services-title" class="amb-ripple-demo__h2">Find it, fix it, dry it out.</h2>
        <p class="amb-ripple-demo__intro">One crew from the first reading to the last patch, with photos of everything we find.</p>
      </header>
      <ul class="amb-ripple-demo__grid" role="list">
        <li class="amb-ripple-demo__card">
          <span class="amb-ripple-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M2 12h3l2-6 4 12 3-9 2 3h6" /></svg></span>
          <h3><a class="amb-ripple-demo__link" href="#amb-ripple-book">Leak detection</a></h3>
          <p>Acoustic and thermal scans through walls and slabs.</p>
          <p class="amb-ripple-demo__price"><span>from</span> $149</p>
        </li>
        <li class="amb-ripple-demo__card">
          <span class="amb-ripple-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M4 14h4v6H4zM8 17h5a3 3 0 0 0 3-3V8M13 4h6M16 4v4" /></svg></span>
          <h3><a class="amb-ripple-demo__link" href="#amb-ripple-book">Pipe repair</a></h3>
          <p>Pinhole leaks and burst lines, patched or replaced.</p>
          <p class="amb-ripple-demo__price"><span>from</span> $189</p>
        </li>
        <li class="amb-ripple-demo__card">
          <span class="amb-ripple-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 3s6 6.4 6 10.5a6 6 0 0 1-12 0C6 9.4 12 3 12 3zM8 21h8" /></svg></span>
          <h3><a class="amb-ripple-demo__link" href="#amb-ripple-book">Water damage</a></h3>
          <p>Moisture mapping, drying and insurance photos.</p>
          <p class="amb-ripple-demo__price"><span>from</span> $249</p>
        </li>
        <li class="amb-ripple-demo__card">
          <span class="amb-ripple-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 3a9 9 0 1 0 9 9M12 7a5 5 0 1 0 5 5M12 11a1 1 0 1 0 1 1M21 3l-9 9" /></svg></span>
          <h3><a class="amb-ripple-demo__link" href="#amb-ripple-book">Smart shut-off</a></h3>
          <p>Sensors that close the main the moment water appears.</p>
          <p class="amb-ripple-demo__price"><span>from</span> $399</p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-ripple-demo__section" aria-labelledby="amb-ripple-proof-title">
    <div class="amb-ripple-demo__inner amb-ripple-demo__inner--split">
      <header class="amb-ripple-demo__head amb-ripple-demo__head--start">
        <p class="amb-ripple-demo__eyebrow">Results</p>
        <h2 id="amb-ripple-proof-title" class="amb-ripple-demo__h2">Less digging, smaller bills.</h2>
        <p class="amb-ripple-demo__intro">Pinpointing a leak first means we open one tile, not the whole floor.</p>
      </header>
      <dl class="amb-ripple-demo__stats">
        <div><dt>Leaks found on the first visit</dt><dd>96%</dd></div>
        <div><dt>Average time to pinpoint</dt><dd>48<small>min</small></dd></div>
        <div><dt>Saved per job vs. exploratory digging</dt><dd>$1.2k</dd></div>
        <div><dt>Reviews from Springfield homes</dt><dd>4.9<small>/5</small></dd></div>
      </dl>
    </div>
  </section>

  <section class="amb-ripple-demo__section amb-ripple-demo__section--cta" id="amb-ripple-book" aria-labelledby="amb-ripple-cta-title">
    <div class="amb-ripple-demo__inner">
      <div class="amb-ripple-demo__panel">
        <h2 id="amb-ripple-cta-title" class="amb-ripple-demo__h2">Water bill creeping up?</h2>
        <p class="amb-ripple-demo__intro">That's often the first sign. Book a check today and we'll call ahead with a two-hour arrival window.</p>
        <div class="amb-ripple-demo__actions">
          <a class="amb-ripple-demo__btn amb-ripple-demo__btn--primary" href="#amb-ripple-book">
            Book a leak check
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
          <a class="amb-ripple-demo__btn" href="mailto:hello@example.com">hello@example.com</a>
        </div>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Layer: decorative, first child of a relative + isolated host; the sticky stage is one viewport tall,
   so the canvas never grows with the page. The CSS grid and glow are the still frame (no JS, reduced motion). */
.amb-ripple {
  --amb-ripple-gap: 22px; /* dot spacing; JS widens it on touch, small screens and very large viewports */
  --amb-ripple-wave: var(--primary-2);   /* ring colour (canvas reads these three) */
  --amb-ripple-wake: var(--primary);     /* pointer wake */
  --amb-ripple-crest: var(--text-inverse); /* what a lifted dot brightens toward */
  --amb-ripple-dot: color-mix(in srgb, var(--amb-ripple-crest) 16%, transparent);
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-ripple--page { position: fixed; }
.amb-ripple__stage {
  position: sticky; top: 0; height: 100vh; height: 100svh; overflow: clip;
  background:
    radial-gradient(circle at center, var(--amb-ripple-dot) 1.1px, transparent 1.7px) 0 0 / var(--amb-ripple-gap) var(--amb-ripple-gap),
    radial-gradient(70% 55% at 50% 45%, color-mix(in srgb, var(--amb-ripple-wake) 16%, transparent), transparent 75%),
    radial-gradient(45% 40% at 88% 92%, color-mix(in srgb, var(--amb-ripple-wave) 12%, transparent), transparent 75%);
}
.amb-ripple--page .amb-ripple__stage { position: relative; height: 100%; }
.amb-ripple__canvas { display: block; width: 100%; height: 100%; }
/* Contrast guard: --amb-ripple-scrim (0–1) fades a deep veil over grid and waves */
.amb-ripple__stage::after { content: ""; position: absolute; inset: 0; background: color-mix(in srgb, var(--surface-deep) calc(var(--amb-ripple-scrim, 0) * 100%), transparent); }

/* ---- Demo page (deep) ---- */
.amb-ripple-demo {
  position: relative; isolation: isolate; overflow-x: clip;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.amb-ripple-demo__section { padding-block: clamp(5rem, 11vw, 8rem); }
.amb-ripple-demo__section--hero { display: grid; align-items: center; min-height: 92vh; min-height: 92svh; text-align: center; }
.amb-ripple-demo__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); box-sizing: border-box; }

.amb-ripple-demo__eyebrow {
  display: inline-flex; align-items: center; gap: 0.625rem; margin: 0; color: var(--text-inverse);
  font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase;
}
.amb-ripple-demo__ping {
  width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--primary-2);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--primary-2) 25%, transparent), 0 0 0 9px color-mix(in srgb, var(--primary-2) 10%, transparent);
}
.amb-ripple-demo__title {
  max-width: 14ch; margin: 1.5rem auto 0; font: 600 clamp(2.5rem, 1.2rem + 5.6vw, 5.5rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-ripple-demo__title em {
  font-style: normal; padding-bottom: 0.06em;
  background: linear-gradient(100deg, color-mix(in srgb, var(--primary-2) 25%, var(--text-inverse)), var(--text-inverse) 70%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.amb-ripple-demo__lead { max-width: 36rem; margin: 1.25rem auto 0; font-size: clamp(1.0625rem, 1rem + 0.4vw, 1.25rem); line-height: 1.6; }
.amb-ripple-demo__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2.25rem; }
.amb-ripple-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 70%, transparent); color: var(--text-inverse); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-ripple-demo__btn:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 60%, transparent), var(--highlight-inverse); }
.amb-ripple-demo__btn:active { transform: scale(0.97); }
.amb-ripple-demo__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: 0 12px 40px -12px color-mix(in srgb, var(--primary-2) 80%, transparent); }
.amb-ripple-demo__btn--primary:hover { box-shadow: 0 16px 48px -10px color-mix(in srgb, var(--primary-2) 95%, transparent); }
.amb-ripple-demo svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-ripple-demo :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.amb-ripple-demo__hint {
  display: flex; flex-direction: column; align-items: center; gap: 0.375rem; margin: 3.5rem 0 0;
  font: 500 0.6875rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.amb-ripple-demo__hint svg { animation: amb-ripple-nudge 1.4s var(--ease-in-out) 3; } /* three nudges, then still */

/* Section heads */
.amb-ripple-demo__head { max-width: 38rem; margin: 0 auto 3rem; text-align: center; }
.amb-ripple-demo__head--start { margin: 0; text-align: left; }
.amb-ripple-demo__h2 { margin: 1rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.8vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.amb-ripple-demo__intro { max-width: 32rem; margin: 1rem auto 0; font-size: 1.0625rem; line-height: 1.6; }
.amb-ripple-demo__head--start .amb-ripple-demo__intro { margin-inline: 0; }

/* Service cards: deep panels with a teal hairline on hover */
.amb-ripple-demo__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.amb-ripple-demo__card {
  position: relative; display: flex; flex-direction: column; gap: 0.5rem; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-deep) 82%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-ripple-demo__card:hover { transform: translateY(-4px); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 60%, transparent), var(--highlight-inverse), 0 24px 48px -24px color-mix(in srgb, var(--primary-2) 50%, transparent); }
.amb-ripple-demo__icon {
  display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 0.875rem; color: color-mix(in srgb, var(--primary-2) 45%, var(--text-inverse));
  background: color-mix(in srgb, var(--primary-2) 14%, transparent); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 40%, transparent);
}
.amb-ripple-demo__card h3 { margin: 0.75rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-ripple-demo__card p { margin: 0; color: var(--text-inverse-muted); line-height: 1.55; }
.amb-ripple-demo__link { color: inherit; text-decoration: none; }
.amb-ripple-demo__link::after { content: ""; position: absolute; inset: 0; border-radius: inherit; }
.amb-ripple-demo .amb-ripple-demo__link:focus-visible { outline: none; }
.amb-ripple-demo__link:focus-visible::after { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.amb-ripple-demo__card .amb-ripple-demo__price {
  display: flex; align-items: baseline; gap: 0.375rem; margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--border-inverse);
  color: var(--text-inverse); font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight);
}
.amb-ripple-demo__price span { color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.04em; }

/* Results: a 2 x 2 readout */
.amb-ripple-demo__inner--split { display: grid; gap: 2.5rem; align-items: center; }
.amb-ripple-demo__stats {
  display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1px; margin: 0; overflow: hidden; border-radius: var(--radius-2xl);
  background: var(--border-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse);
}
.amb-ripple-demo__stats div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.5rem; padding: 1.25rem; background: color-mix(in srgb, var(--surface-deep) 90%, transparent); }
.amb-ripple-demo__stats dt { color: var(--text-inverse-muted); font: 500 0.75rem/1.4 var(--font-mono); }
.amb-ripple-demo__stats dd { margin: 0; font: 600 clamp(1.875rem, 1.4rem + 2vw, 3rem)/1 var(--font-display); letter-spacing: var(--tracking-display); }
.amb-ripple-demo__stats small { margin-left: 0.125rem; color: color-mix(in srgb, var(--primary-2) 45%, var(--text-inverse)); font-size: 0.45em; letter-spacing: 0; }

/* CTA panel */
.amb-ripple-demo__panel {
  max-width: 44rem; margin-inline: auto; padding: clamp(2rem, 6vw, 3.5rem) clamp(1.25rem, 5vw, 3rem); border-radius: var(--radius-2xl); text-align: center;
  background: radial-gradient(80% 70% at 50% 0%, color-mix(in srgb, var(--primary-2) 16%, transparent), transparent 70%), color-mix(in srgb, var(--surface-deep) 85%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 40px 80px -40px var(--surface-deep);
}
.amb-ripple-demo__panel .amb-ripple-demo__h2 { margin-top: 0; }

@media (min-width: 600px) { .amb-ripple-demo__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1024px) {
  .amb-ripple-demo__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .amb-ripple-demo__inner--split { grid-template-columns: 0.9fr 1.1fr; gap: 4rem; }
}

@media (prefers-reduced-motion: reduce) {
  .amb-ripple-demo__hint svg { animation: none; }
}
@keyframes amb-ripple-nudge { 50% { transform: translateY(5px); } }
```

## JS

```js
// Ripple Dot Grid: scroll bursts send rings across a canvas dot matrix and the mouse leaves a wake.
// The CSS grid is the still frame; the canvas only draws the dots a wave or the wake has lifted.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const coarse = matchMedia('(pointer: coarse)');
const LEVELS = 6;

document.querySelectorAll('.amb-ripple').forEach((layer) => {
  if (reduce.matches) return; // the CSS grid and glow are the reduced-motion still
  const page = layer.classList.contains('amb-ripple--page');
  const host = layer.parentElement;
  const stage = layer.querySelector('.amb-ripple__stage');
  const canvas = layer.querySelector('.amb-ripple__canvas');
  const ctx = canvas.getContext('2d');
  let w = 0, h = 0, gap = 22, cols = 0, rows = 0, heat = new Float32Array(0), hot = 0, box = null;
  let rings = [], raf = 0, on = false, last = 0, lastY = scrollY, burstAt = -1e4, side = 0;
  let left = 0, hostTop = 0, hostH = 0, vh = innerHeight, stageTop = 0, ptr = null, prev = null;

  // Colour buckets from the layer's tokens: each level lifts toward the crest colour, alpha capped at 0.55
  const css = getComputedStyle(layer);
  const rgb = (name) => {
    ctx.fillStyle = css.getPropertyValue(name).trim(); // the canvas normalises any CSS colour to hex or rgba()
    const s = ctx.fillStyle;
    return s[0] === '#' ? [1, 3, 5].map((i) => parseInt(s.slice(i, i + 2), 16)) : s.match(/[\d.]+/g).slice(0, 3).map(Number);
  };
  const crest = rgb('--amb-ripple-crest');
  const tint = (base, lift) => Array.from({ length: LEVELS }, (_, k) => {
    const a = (k + 1) / LEVELS;
    const c = base.map((v, i) => Math.round(v + (crest[i] - v) * a * lift));
    return { fill: `rgb(${c.join(' ')})`, alpha: 0.2 + 0.35 * a, r: 1.2 + 2.2 * a, pts: [] };
  });
  const buckets = [...tint(rgb('--amb-ripple-wave'), 0.4), ...tint(rgb('--amb-ripple-wake'), 0.5)];

  const measure = () => {
    const r = host.getBoundingClientRect();
    [vh, hostTop, hostH] = [innerHeight, r.top + scrollY, r.height];
  };
  // Canvas = one viewport. DPR capped; dot count scales with area and drops on touch and small screens.
  const resize = () => {
    const r = stage.getBoundingClientRect();
    const small = coarse.matches || r.width < 768;
    const dpr = Math.min(devicePixelRatio || 1, coarse.matches ? 1.5 : 2);
    [w, h, left] = [r.width, r.height, r.left];
    gap = Math.round(Math.max(small ? 26 : 22, Math.sqrt((w * h) / (small ? 1400 : 3200))));
    [cols, rows] = [Math.ceil(w / gap), Math.ceil(h / gap)];
    heat = new Float32Array(cols * rows);
    [canvas.width, canvas.height] = [Math.round(w * dpr), Math.round(h * dpr)];
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    layer.style.setProperty('--amb-ripple-gap', `${gap}px`);
    box = null;
    measure();
  };

  // Pointer wake: light the dots around a point (kept at the brighter of old and new heat)
  const stamp = (x, y) => {
    const c0 = Math.max(0, Math.floor((x - 64) / gap)), c1 = Math.min(cols - 1, Math.floor((x + 64) / gap));
    const r0 = Math.max(0, Math.floor((y - 64) / gap)), r1 = Math.min(rows - 1, Math.floor((y + 64) / gap));
    for (let r = r0; r <= r1; r++) for (let c = c0; c <= c1; c++) {
      const d = Math.hypot(gap * (c + 0.5) - x, gap * (r + 0.5) - y);
      if (d < 64) heat[r * cols + c] = Math.max(heat[r * cols + c], 0.85 * (1 - d / 64));
    }
  };

  // Draw only lifted dots, one path per colour bucket; clear only last frame's dirty box
  const draw = () => {
    if (box) ctx.clearRect(box[0], box[1], box[2] - box[0], box[3] - box[1]);
    let x0 = w, y0 = h, x1 = -1, y1 = -1;
    for (const b of buckets) {
      if (!b.pts.length) continue;
      ctx.globalAlpha = b.alpha;
      ctx.fillStyle = b.fill;
      ctx.beginPath();
      for (let j = 0; j < b.pts.length; j += 2) {
        const x = b.pts[j], y = b.pts[j + 1];
        ctx.moveTo(x + b.r, y);
        ctx.arc(x, y, b.r, 0, Math.PI * 2);
        x0 = Math.min(x0, x); x1 = Math.max(x1, x); y0 = Math.min(y0, y); y1 = Math.max(y1, y);
      }
      ctx.fill();
    }
    box = x1 < 0 ? null : [x0 - 5, y0 - 5, x1 + 5, y1 + 5];
  };

  const tick = (t) => {
    const dt = last ? Math.min(64, t - last) : 16.7;
    const y = scrollY;
    const v = Math.abs(y - lastY) / dt; // px per ms
    [last, lastY] = [t, y];
    stageTop = page ? 0 : Math.max(Math.min(0, hostTop + hostH - h - y), hostTop - y); // where the sticky stage sits
    // A scroll burst spawns a ring at the viewport middle, from alternating edges, as strong as the flick
    if (v > 0.05 && t - burstAt > 340) {
      [burstAt, side] = [t, 1 - side];
      rings.push({ x: side * w, y: Math.min(h, Math.max(0, vh / 2 - stageTop)), t0: t, s: Math.min(1, 0.25 + v / 3) });
      if (rings.length > 6) rings.shift();
    }
    if (ptr) { // stamp along the path since the last move, so fast strokes leave an unbroken wake
      const x = ptr.x, py = ptr.y - stageTop, from = prev || { x, y: py };
      const steps = Math.max(1, Math.ceil(Math.hypot(x - from.x, py - from.y) / (gap / 2)));
      for (let k = 1; k <= steps; k++) stamp(from.x + ((x - from.x) * k) / steps, from.y + ((py - from.y) * k) / steps);
      [prev, ptr] = [{ x, y: py }, null];
    }
    const diag = Math.hypot(w, h), fade = 0.9 ** (dt / 16.7);
    rings = rings.filter((g) => {
      g.R = (t - g.t0) * 0.75;
      g.a = g.s * Math.exp(-(t - g.t0) / 1100);
      return g.a > 0.03 && g.R < diag + 120;
    });
    for (const b of buckets) b.pts.length = 0;
    hot = 0;
    for (let i = 0; i < cols * rows; i++) {
      const x = gap * ((i % cols) + 0.5), yy = gap * (Math.floor(i / cols) + 0.5);
      let wave = 0;
      for (const g of rings) {
        const d = Math.hypot(x - g.x, yy - g.y) - g.R;
        if (d > -90 && d < 90) wave = Math.max(wave, g.a * Math.exp(-(d * d) / 1800));
      }
      const wk = heat[i] > 0.02 ? (heat[i] *= fade) : (heat[i] = 0);
      if (wk) hot++;
      const amp = Math.max(wave, wk);
      if (amp >= 0.06) buckets[(wk > wave ? LEVELS : 0) + Math.min(LEVELS - 1, Math.floor(amp * LEVELS))].pts.push(x, yy);
    }
    draw();
    if (!hot) prev = null;
    raf = rings.length || hot ? requestAnimationFrame(tick) : 0;
    if (!raf) last = 0;
  };

  // Run only while the layer is on screen, the tab is visible and a wave or wake is alive
  const wake = () => {
    if (raf || !on || reduce.matches || document.visibilityState === 'hidden') return;
    raf = requestAnimationFrame(tick);
  };
  const sleep = () => { cancelAnimationFrame(raf); raf = 0; last = 0; };

  resize();
  new ResizeObserver(resize).observe(stage);
  new IntersectionObserver(([e]) => { on = e.isIntersecting; lastY = scrollY; if (on) wake(); else sleep(); }).observe(layer);
  addEventListener('resize', measure, { passive: true });
  addEventListener('scroll', wake, { passive: true });
  addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'touch') { ptr = { x: e.clientX - left, y: e.clientY }; wake(); }
  }, { passive: true });
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') sleep(); else { lastY = scrollY; wake(); }
  });
});
```

## Notes

- **Layer contract:** `.amb-ripple` is decorative (`aria-hidden="true"`, `pointer-events: none`). Make it the first child of a `position: relative; isolation: isolate` host, at `z-index: -1`; the host can be one long section or, as in the demo, a wrapper around several. A sticky, viewport-tall stage holds the canvas, so the canvas is always one screen in size, never the height of the page. The wake comes from a passive `pointermove` listener on `window` (mouse and pen only), so the layer never takes clicks. `.amb-ripple--page` fixes the layer behind the whole page (sections need transparent backgrounds). Use one ambient background per page.
- **Performance:** device pixel ratio is capped at 2 (1.5 on coarse pointers), and the canvas resizes through a `ResizeObserver`. Dots sit 22px apart (26px on touch or under 768px), and spacing widens on big screens so the grid stays at about **3,200 dots at most (1,400 on touch and small screens)**. The static grid is a CSS background, so the canvas only draws lifted dots: twelve batched paths per frame, clearing only last frame's dirty box. The loop runs only while a ring or wake is alive, the layer is on screen and the tab is visible; rings fade out within about 2s. No layout reads per frame (host and stage geometry are cached on resize).
- **Contrast:** lifted dots brighten toward `--amb-ripple-crest` but are capped at 55% alpha. Worst case under the demo's `--text-inverse` body copy is a fully lifted dot on the glow: 5.0:1. Muted text only sits on the 82–90% deep panels (6.5:1 or better), and the headline gradient stays at 3.8:1 or better (large text). `--amb-ripple-scrim` (0–1) fades a deep veil over the grid and its waves.
- **No JS and reduced motion:** the stage's CSS background is a complete still: a quiet dot grid with a soft radial glow. Under reduced motion the canvas is never set up; the scroll hint also skips its three nudges.
- **Adapting:** retheme with `--amb-ripple-wave`, `--amb-ripple-wake` and `--amb-ripple-crest` (any colour tokens; the canvas reads them once at start-up) and `--amb-ripple-dot` for the resting grid. Ring speed (0.75px/ms), decay (1.1s) and wake radius (64px) are plain numbers in the JS. The loop listens to window scroll.
