# Seam Melt

Sections that dissolve into each other instead of meeting at a hard edge. Each section is pulled up over the one before it, and its top edge is masked through a soft eased fade (10rem on desktop). An aurora "seam light", a blurred multi-hue ellipse, glows on every boundary, and one shared film-grain layer (SVG `feTurbulence`) runs over everything, so night, brand blue-teal and light read as one continuous surface. As a seam crosses the middle of the viewport, its light swells and shifts hue; on phones the overlap and glow scale down and the copy stacks. Depends on `tokens/variables.css`.

**Motion:** seam glow intensity, size and hue crossfade, scroll-linked (CSS `view()` timeline where supported, otherwise a rAF-throttled scroll listener; linear scrub, peaked keyframes) · scroll hint nudge (3 runs).

## HTML

```html
<div class="seam-melt" data-seam-melt>
  <section class="seam-melt__section seam-melt__section--night" aria-labelledby="seam-melt-title-1">
    <div class="seam-melt__inner">
      <header class="seam-melt__head">
        <p class="seam-melt__eyebrow">After hours</p>
        <h2 id="seam-melt-title-1" class="seam-melt__title">Midnight leak? We pick up.</h2>
      </header>
      <div class="seam-melt__body">
        <p class="seam-melt__copy">A real dispatcher answers in under a minute, day or night, and a licensed tech is on the way before you've found the stopcock.</p>
        <dl class="seam-melt__stats">
          <div><dt>Answer time</dt><dd>&lt; 1 min</dd></div>
          <div><dt>Average arrival</dt><dd>38 min</dd></div>
          <div><dt>Coverage</dt><dd>24/7</dd></div>
        </dl>
        <span class="seam-melt__hint" aria-hidden="true">Scroll
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
        </span>
      </div>
    </div>
  </section>

  <div class="seam-melt__seam seam-melt__seam--dusk" aria-hidden="true"></div>

  <section class="seam-melt__section seam-melt__section--brand" aria-labelledby="seam-melt-title-2">
    <div class="seam-melt__inner">
      <header class="seam-melt__head">
        <p class="seam-melt__eyebrow">On the job</p>
        <h2 id="seam-melt-title-2" class="seam-melt__title">One crew from first call to final check</h2>
      </header>
      <div class="seam-melt__body">
        <p class="seam-melt__copy">The tech who diagnoses it fixes it. No hand-offs, no second visit to quote, no surprise subcontractors.</p>
        <dl class="seam-melt__stats">
          <div><dt>Most jobs</dt><dd>1 visit</dd></div>
          <div><dt>Fixed same day</dt><dd>92%</dd></div>
          <div><dt>Workmanship warranty</dt><dd>2 yr</dd></div>
        </dl>
      </div>
    </div>
  </section>

  <div class="seam-melt__seam seam-melt__seam--dawn" aria-hidden="true"></div>

  <section class="seam-melt__section seam-melt__section--light" aria-labelledby="seam-melt-title-3">
    <div class="seam-melt__inner">
      <header class="seam-melt__head">
        <p class="seam-melt__eyebrow">After the visit</p>
        <h2 id="seam-melt-title-3" class="seam-melt__title">Clear prices, written down</h2>
      </header>
      <div class="seam-melt__body">
        <p class="seam-melt__copy">You approve a flat price before any work starts, and that's the number on the invoice. No call-out fee in Westlake, Northside or Riverside.</p>
        <dl class="seam-melt__stats">
          <div><dt>Call-out fee</dt><dd>$0</dd></div>
          <div><dt>Pricing</dt><dd>Flat</dd></div>
          <div><dt>1,200+ reviews</dt><dd>4.9</dd></div>
        </dl>
      </div>
    </div>
  </section>

  <div class="seam-melt__grain" aria-hidden="true"></div>
</div>
```

## CSS

```css
@property --seam-melt-i { syntax: "<number>"; inherits: true; initial-value: 0.6; }
@property --seam-melt-h { syntax: "<number>"; inherits: true; initial-value: 0.5; }

/* One surface: sections in a flex column (so negative margins never collapse), seams and grain above them */
.seam-melt {
  --seam-melt-overlap: clamp(6rem, 4rem + 8vw, 10rem);
  --seam-melt-fade: linear-gradient(to bottom, transparent,
    color-mix(in srgb, black 14%, transparent) calc(var(--seam-melt-overlap) * 0.25),
    color-mix(in srgb, black 50%, transparent) calc(var(--seam-melt-overlap) * 0.5),
    color-mix(in srgb, black 86%, transparent) calc(var(--seam-melt-overlap) * 0.75),
    black var(--seam-melt-overlap));
  position: relative; isolation: isolate; display: flex; flex-direction: column;
  overflow: hidden; overflow: clip; font-family: var(--font-sans);
}

/* Sections: padding keeps content clear of the overlap zones */
.seam-melt__section { position: relative; z-index: 0; padding-block: calc(var(--seam-melt-overlap) + clamp(2.5rem, 6vw, 5rem)); }
.seam-melt__section:first-child { padding-top: clamp(4rem, 10vw, 7rem); }
.seam-melt__seam + .seam-melt__section {
  margin-top: calc(var(--seam-melt-overlap) * -1);
  -webkit-mask-image: var(--seam-melt-fade); mask-image: var(--seam-melt-fade);
}
.seam-melt__section--night {
  --seam-melt-line: var(--border-inverse);
  --seam-melt-soft: var(--text-inverse-muted);
  --seam-melt-kicker: var(--text-inverse-muted);
  background: radial-gradient(70% 55% at 15% 10%, color-mix(in srgb, var(--primary) 22%, transparent), transparent 70%), var(--surface-deep);
  color: var(--text-inverse);
}
.seam-melt__section--brand {
  --seam-melt-line: color-mix(in srgb, var(--text-inverse) 24%, transparent);
  --seam-melt-soft: var(--text-inverse);
  --seam-melt-kicker: var(--text-inverse);
  background: linear-gradient(170deg, color-mix(in srgb, var(--primary) 80%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  color: var(--text-inverse);
}
.seam-melt__section--light {
  --seam-melt-line: var(--border-subtle);
  --seam-melt-soft: var(--text-muted);
  --seam-melt-kicker: var(--primary);
  background: radial-gradient(60% 50% at 85% 20%, color-mix(in srgb, var(--accent) 10%, transparent), transparent 70%), var(--surface-light);
  color: var(--text-main);
}

/* Content */
.seam-melt__inner { display: grid; gap: 1.5rem; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.seam-melt__eyebrow { margin: 0; color: var(--seam-melt-kicker); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.seam-melt__title {
  max-width: 16ch; margin: 0.75rem 0 0; font: 600 clamp(2.125rem, 1.4rem + 3.2vw, 4rem)/1.02 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.seam-melt__copy { max-width: 34rem; margin: 0; color: var(--seam-melt-soft); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.1875rem); line-height: 1.6; }
.seam-melt__stats {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(7rem, 1fr)); gap: 1.25rem;
  margin: 2rem 0 0; padding-top: 1.5rem; border-top: 1px solid var(--seam-melt-line);
}
.seam-melt__stats div { display: grid; align-content: start; gap: 0.375rem; }
.seam-melt__stats dt { color: var(--seam-melt-soft); font: 500 0.75rem/1.3 var(--font-mono); letter-spacing: 0.06em; }
.seam-melt__stats dd { margin: 0; font: 600 clamp(1.5rem, 1.2rem + 1.2vw, 2.25rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.seam-melt__hint {
  display: inline-flex; align-items: center; gap: 0.375rem; margin-top: 2rem;
  color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.seam-melt__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: seam-melt-nudge 1.6s var(--ease-in-out) 3; }

/* Seam light: two pre-blurred aurora ellipses on the boundary. Intensity scales and fades them; hue crossfades A → B */
.seam-melt__seam {
  position: relative; z-index: 2; flex: none; height: 0; pointer-events: none;
  transform-origin: 50% calc(var(--seam-melt-overlap) / -2);
  scale: calc(0.8 + 0.3 * var(--seam-melt-i)) calc(0.65 + 0.5 * var(--seam-melt-i));
}
.seam-melt__seam::before, .seam-melt__seam::after {
  content: ""; position: absolute; left: 50%; top: calc(var(--seam-melt-overlap) / -2);
  width: min(130vw, 96rem); height: clamp(4.5rem, 3rem + 5vw, 8rem); translate: -50% -50%;
  border-radius: 50%; filter: blur(var(--blur-lg));
}
.seam-melt__seam::before {
  background: linear-gradient(90deg, transparent 6%, color-mix(in srgb, var(--seam-melt-a1) 85%, transparent) 30%, color-mix(in srgb, var(--seam-melt-a2) 85%, transparent) 70%, transparent 94%);
  opacity: calc(var(--seam-melt-i) * (1 - var(--seam-melt-h)));
}
.seam-melt__seam::after {
  background: linear-gradient(90deg, transparent 6%, color-mix(in srgb, var(--seam-melt-b1) 85%, transparent) 34%, color-mix(in srgb, var(--seam-melt-b2) 85%, transparent) 66%, transparent 94%);
  opacity: calc(var(--seam-melt-i) * var(--seam-melt-h));
}
.seam-melt__seam--dusk {
  --seam-melt-a1: var(--primary-2); --seam-melt-a2: var(--primary);
  --seam-melt-b1: color-mix(in srgb, var(--primary) 60%, var(--danger)); --seam-melt-b2: color-mix(in srgb, var(--primary-2) 70%, var(--surface-light));
}
.seam-melt__seam--dawn {
  --seam-melt-a1: color-mix(in srgb, var(--primary-2) 70%, var(--surface-light)); --seam-melt-a2: color-mix(in srgb, var(--primary) 45%, var(--surface-light));
  --seam-melt-b1: color-mix(in srgb, var(--accent) 75%, var(--surface-light)); --seam-melt-b2: color-mix(in srgb, var(--primary-2) 55%, var(--surface-light));
}

/* Film grain shared by every section: one static tile of desaturated SVG turbulence */
.seam-melt__grain {
  position: absolute; inset: 0; z-index: 3; pointer-events: none; opacity: 0.12;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='200' height='200' filter='url(%23g)'/%3E%3C/svg%3E");
  background-size: 200px 200px;
}

@media (min-width: 768px) {
  .seam-melt__inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); align-items: end; gap: 3rem; }
}

/* Signature: each seam peaks and shifts hue as it crosses the middle of the viewport */
@media (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .seam-melt__seam { animation: seam-melt-pass auto linear both; animation-timeline: view(); }
  }
}
@keyframes seam-melt-pass {
  0% { --seam-melt-i: 0.2; --seam-melt-h: 0; }
  32% { --seam-melt-i: 0.42; }
  50% { --seam-melt-i: 1; }
  68% { --seam-melt-i: 0.42; }
  100% { --seam-melt-i: 0.2; --seam-melt-h: 1; }
}
@keyframes seam-melt-nudge { 50% { translate: 0 4px; } }
@media (prefers-reduced-motion: reduce) {
  .seam-melt *, .seam-melt *::before, .seam-melt *::after { animation: none !important; }
}
```

## JS

```js
// Fallback for engines without scroll-driven animations (e.g. Firefox): same curve, written per frame
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const native = CSS.supports('animation-timeline: view()');

document.querySelectorAll('[data-seam-melt]').forEach((root) => {
  if (native) return;
  const seams = [...root.querySelectorAll('.seam-melt__seam')];
  let near = false;
  let frame = 0;

  const render = () => {
    frame = 0;
    const mid = innerHeight / 2;
    seams.forEach((seam) => {
      if (reduce.matches) {
        seam.style.removeProperty('--seam-melt-i');
        seam.style.removeProperty('--seam-melt-h');
        return;
      }
      // d: 1 as the seam enters at the bottom, 0 at the centre, -1 as it leaves at the top
      const d = Math.max(-1, Math.min(1, (seam.getBoundingClientRect().top - mid) / mid));
      seam.style.setProperty('--seam-melt-i', (0.2 + 0.8 * (1 - Math.abs(d)) ** 2).toFixed(3));
      seam.style.setProperty('--seam-melt-h', ((1 - d) / 2).toFixed(3));
    });
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(render); };

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; queue(); }).observe(root);
  addEventListener('scroll', queue, { passive: true });
  addEventListener('resize', queue, { passive: true });
  reduce.addEventListener('change', render);
  render();
});
```

## Notes

- The sections stay plain, semantic `<section>`s with real headings, copy and `<dl>` stats. Seams and grain are `aria-hidden` with `pointer-events: none`, and the padding (`--seam-melt-overlap` plus breathing room) keeps all text out of the masked, overlapping zones.
- Mechanics: any section that follows a `.seam-melt__seam` is pulled up by `--seam-melt-overlap` and masked with an eased fade, so the section underneath shows through. The wrapper is a flex column, so the negative margin never collapses. Seams (z 2) and grain (z 3) sit above the sections.
- The signature uses a CSS `view()` timeline to animate the registered `--seam-melt-i`/`--seam-melt-h` (Chromium, Safari 26+). Other engines get the same curve from a rAF-throttled passive scroll listener. With reduced motion, or without JS in those engines, the seams hold a static glow (intensity 0.6, half-mixed hue).
- Contrast: the brand gradient mixes `--primary`/`--primary-2` with 20%/30% `--surface-deep`, so `--text-inverse` is 6.1–6.7:1. Night copy uses `--text-inverse-muted` (7:1). Light copy uses `--text-muted`, 4.6:1 on the faint amber tint. The grain adds at most about 6% grey noise and doesn't push any pair below its threshold.
- Retheme each seam with `--seam-melt-a1/-a2` (hue before the centre) and `--seam-melt-b1/-b2` (after), and the overlap depth with `--seam-melt-overlap`. The glows are pre-blurred, and only their opacity and scale change, so scrolling stays on the compositor.
