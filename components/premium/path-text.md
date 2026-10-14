# Text on a Path

A light services section crossed by two banners of text on sweeping SVG curves. A thick brand-gradient ribbon carries the five trades from bottom left to top right, and a slim deep tape of promises crosses it the other way. As the band scrolls into view the ribbons unroll along dashed guide lines, and every scroll slides the trades forward along their curve (`startOffset` bound to scroll progress) while the tape runs backwards. On phones the same scene is sliced to a taller viewBox crop, so the curves cross steeper and the type stays large. Depends on `tokens/variables.css`.

**Motion:** ribbon unfurl (mask stroke-dashoffset, scroll-scrubbed) · text travel along both paths in opposite directions (`startOffset`, scroll-scrubbed with a short exponential settle) · button arrow and press (`--dur-3`, `--ease-spring`). No autonomous loops.

## HTML

```html
<div class="path-text-demo">
  <div class="path-text-demo__intro">
    <p>A banner that unrolls as you scroll.</p>
    <span class="path-text-demo__hint">Scroll</span>
  </div>

  <section class="path-text" aria-labelledby="path-text-title" data-path-text>
    <div class="path-text__inner">
      <div class="path-text__head">
        <div>
          <p class="path-text__eyebrow">Five trades, one team</p>
          <h2 id="path-text-title" class="path-text__title">One call. <span class="path-text__accent">Every trade.</span></h2>
        </div>
        <div>
          <p class="path-text__lead">Licensed and insured, with same-day slots, upfront pricing and a 2-year guarantee on every job across Springfield.</p>
          <div class="path-text__actions">
            <a class="path-text__btn" href="#services">
              See all services
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <a class="path-text__phone" href="tel:+15555550123">
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
              (555) 555-0123
            </a>
          </div>
        </div>
      </div>
      <ul class="path-text__sr" aria-label="Trades we cover">
        <li>Plumbing</li><li>Electrical</li><li>HVAC</li><li>Roofing</li><li>Solar</li>
      </ul>
    </div>

    <div class="path-text__band">
      <svg class="path-text__svg" viewBox="0 0 1600 640" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
        <defs>
          <path id="path-text-curve-a" d="M-700 560C-250 600 250 600 640 440C1030 280 1150 110 1600 100C2050 90 2200 70 2400 60" />
          <path id="path-text-curve-b" d="M-700 110C-250 70 250 90 700 280C1150 470 1300 560 1600 560C1900 560 2150 560 2400 580" />
          <linearGradient id="path-text-grad" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="1600" y2="0">
            <stop offset="0" class="path-text__stop-a" />
            <stop offset="1" class="path-text__stop-b" />
          </linearGradient>
          <mask id="path-text-mask-b" maskUnits="userSpaceOnUse" x="-800" y="-100" width="3400" height="840">
            <use class="path-text__reveal" href="#path-text-curve-b" fill="none" stroke="white" stroke-width="50" stroke-linecap="round" />
          </mask>
          <mask id="path-text-mask-a" maskUnits="userSpaceOnUse" x="-800" y="-100" width="3400" height="840">
            <use class="path-text__reveal" href="#path-text-curve-a" fill="none" stroke="white" stroke-width="84" stroke-linecap="round" />
          </mask>
        </defs>

        <use class="path-text__guide" href="#path-text-curve-b" />
        <use class="path-text__guide" href="#path-text-curve-a" />

        <g class="path-text__track" mask="url(#path-text-mask-b)" data-path-text-track="660 100 0.08">
          <use class="path-text__edge" href="#path-text-curve-b" />
          <use class="path-text__tape" href="#path-text-curve-b" />
          <text class="path-text__ticker"><textPath href="#path-text-curve-b" startOffset="380">LICENSED &amp; INSURED • SAME-DAY SLOTS • UPFRONT PRICING • 2-YEAR GUARANTEE • LICENSED &amp; INSURED • SAME-DAY SLOTS • UPFRONT PRICING • 2-YEAR GUARANTEE • LICENSED &amp; INSURED • SAME-DAY SLOTS • UPFRONT PRICING • 2-YEAR GUARANTEE •</textPath></text>
        </g>

        <g class="path-text__track" mask="url(#path-text-mask-a)" data-path-text-track="100 660 0">
          <use class="path-text__ribbon" href="#path-text-curve-a" stroke="url(#path-text-grad)" />
          <text class="path-text__words"><textPath href="#path-text-curve-a" startOffset="380">Plumbing — Electrical — HVAC — Roofing — Solar — Plumbing — Electrical — HVAC — Roofing — Solar — Plumbing — Electrical — HVAC — Roofing — Solar — Plumbing — Electrical — HVAC — Roofing — Solar —</textPath></text>
        </g>
      </svg>
    </div>
  </section>

  <div class="path-text-demo__outro">
    <p>Scroll back up and the ribbon rewinds.</p>
    <span class="path-text-demo__hint">End of demo</span>
  </div>
</div>
```

## CSS

```css
/* Section: light, lit softly from two corners */
.path-text {
  --path-text-ribbon-from: var(--primary);
  --path-text-ribbon-to: color-mix(in srgb, var(--primary-2) 80%, var(--surface-deep)); /* keeps white text at 5:1 */
  position: relative; overflow: clip;
  padding-bottom: clamp(1.5rem, 4vw, 3rem);
  background:
    radial-gradient(55% 45% at 100% 0%, color-mix(in srgb, var(--primary-2) 9%, transparent), transparent 70%),
    radial-gradient(50% 50% at 0% 100%, color-mix(in srgb, var(--primary) 8%, transparent), transparent 70%),
    var(--surface-light);
  color: var(--text-main); font-family: var(--font-sans);
}
.path-text__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter) 0; }
.path-text a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.path-text__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Heading row */
.path-text__head { display: grid; gap: 1.5rem; }
.path-text__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; color: var(--primary); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.path-text__eyebrow::before { content: ""; width: 1.5rem; height: 2px; border-radius: 999px; background: var(--gradient-brand); }
.path-text__title { margin: 0.875rem 0 0; font: 600 clamp(2.25rem, 1.3rem + 3.8vw, 4.5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.path-text__accent { padding-bottom: 0.06em; background: var(--gradient-brand); -webkit-background-clip: text; background-clip: text; color: transparent; }
.path-text__lead { max-width: 30rem; margin: 0; color: var(--text-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
.path-text__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.5rem; margin-top: 1.5rem; }
.path-text__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; border-radius: 999px;
  background: var(--text-main); color: var(--surface-light); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight-inverse), 0 12px 28px -12px color-mix(in srgb, var(--text-main) 70%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.path-text__btn:active { transform: scale(0.97); }
.path-text__phone { display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; color: var(--text-main); font-weight: 600; text-decoration: none; }
.path-text__phone:hover { color: var(--primary); }
.path-text__btn svg, .path-text__phone svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.path-text__btn:hover svg { translate: 3px 0; }

/* The band: one scene, sliced to a taller crop on smaller screens */
.path-text__band { margin-top: clamp(1.5rem, 4vw, 2.5rem); }
.path-text__svg {
  display: block; width: 100%; height: auto; aspect-ratio: 4 / 5;
  filter: drop-shadow(0 18px 20px color-mix(in srgb, var(--primary) 20%, transparent));
}
.path-text__stop-a { stop-color: var(--path-text-ribbon-from); }
.path-text__stop-b { stop-color: var(--path-text-ribbon-to); }
.path-text__guide { fill: none; stroke: color-mix(in srgb, var(--primary) 40%, transparent); stroke-width: 1.5; stroke-dasharray: 3 9; }
.path-text__ribbon { fill: none; stroke-width: 80; stroke-linecap: round; }
.path-text__edge { fill: none; stroke: color-mix(in srgb, var(--primary-2) 55%, var(--surface-deep)); stroke-width: 46; stroke-linecap: round; }
.path-text__tape { fill: none; stroke: var(--surface-deep); stroke-width: 42; stroke-linecap: round; }
.path-text__words, .path-text__ticker { fill: var(--text-inverse); dominant-baseline: central; text-rendering: geometricPrecision; }
.path-text__words { font: 600 34px var(--font-display); letter-spacing: 0.02em; }
.path-text__ticker { font: 500 20px var(--font-mono); letter-spacing: 0.14em; }
.path-text--open .path-text__track { mask: none; } /* fully unrolled: drop the masks, they cost a repaint per frame */

/* Demo scroll room */
.path-text-demo__intro, .path-text-demo__outro {
  display: grid; place-content: center; justify-items: center; gap: 0.75rem; min-height: 70vh; min-height: 70svh;
  padding: 3rem var(--gutter); background: var(--surface-muted); color: var(--text-muted); font-family: var(--font-sans); text-align: center;
}
.path-text-demo__intro p, .path-text-demo__outro p { max-width: 24rem; margin: 0; color: var(--text-main); font: 600 clamp(1.25rem, 1rem + 1vw, 1.75rem)/1.2 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.path-text-demo__hint { font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }

@media (min-width: 768px) {
  .path-text__head { grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr); align-items: end; gap: 3rem; }
  .path-text__svg { aspect-ratio: 2 / 1; }
}
@media (min-width: 1024px) {
  .path-text__svg { aspect-ratio: 5 / 2; }
}
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-path-text]').forEach((root, n) => {
  const band = root.querySelector('.path-text__band');
  const svg = band?.querySelector('svg');
  if (reduce.matches || !svg) return; // static, fully drawn banner

  // Each copy gets its own mask ids, so instances unroll independently
  root.querySelectorAll('mask[id]').forEach((mask) => {
    const id = `${mask.id}-${n}`;
    root.querySelectorAll(`[mask="url(#${mask.id})"]`).forEach((el) => el.setAttribute('mask', `url(#${id})`));
    mask.id = id;
  });

  // A track is text riding a curve, plus the mask stroke that unrolls it
  const tracks = [...root.querySelectorAll('[data-path-text-track]')].map((group) => {
    const [from, to, delay = 0] = group.dataset.pathTextTrack.split(' ').map(Number);
    const words = group.querySelector('textPath');
    const curve = svg.querySelector(words.getAttribute('href'));
    const total = curve.getTotalLength();
    const xs = Array.from({ length: 121 }, (_, k) => curve.getPointAtLength((total * k) / 120).x);
    const reveal = root.querySelector(`${group.getAttribute('mask').slice(4, -1)} .path-text__reveal`);
    reveal.style.strokeDasharray = `${total} ${total}`;
    return { from, to, delay, words, total, xs, reveal, enter: 0, leave: total };
  });

  // Where each curve enters and leaves the visible crop (the viewBox is sliced to the band's aspect ratio)
  const measure = () => {
    const r = svg.getBoundingClientRect();
    const vb = svg.viewBox.baseVal;
    const half = r.width / Math.max(r.width / vb.width, r.height / vb.height) / 2;
    tracks.forEach((t) => {
      const at = (x) => (t.total * Math.max(0, t.xs.findIndex((v) => v >= x))) / 120;
      t.enter = at(vb.width / 2 - half) - 60;
      t.leave = at(vb.width / 2 + half) + 60;
    });
  };

  const opened = band.getBoundingClientRect().top < innerHeight; // already on screen at load: never hide it
  const progress = () => {
    const r = band.getBoundingClientRect();
    return Math.min(1, Math.max(0, (innerHeight - r.top) / (innerHeight + r.height)));
  };
  const draw = (p) => {
    let open = true;
    tracks.forEach((t) => {
      t.words.setAttribute('startOffset', (t.from + (t.to - t.from) * p).toFixed(1));
      const q = opened ? 1 : Math.min(1, Math.max(0, (p - t.delay) / 0.4)); // unroll during the first 40%
      t.reveal.style.strokeDashoffset = (t.total - (t.enter + (t.leave - t.enter) * q)).toFixed(1);
      open &&= q >= 1;
    });
    root.classList.toggle('path-text--open', open);
  };

  // Scroll scrub with a short settle, only while the band is near the viewport
  let target = 0, current = 0, frame = 0, last = 0, near = false;
  const tick = (now) => {
    const dt = Math.min(48, now - (last || now));
    last = now;
    current += (target - current) * (1 - Math.exp(-dt / 110));
    if (Math.abs(target - current) < 0.0005) current = target;
    draw(current);
    if (current !== target) frame = requestAnimationFrame(tick);
    else frame = last = 0;
  };
  const onScroll = () => {
    if (!near) return;
    target = progress();
    if (!frame) frame = requestAnimationFrame(tick);
  };
  new IntersectionObserver(([entry]) => {
    near = entry.isIntersecting;
    if (near) { measure(); current = target = progress(); draw(current); }
  }, { rootMargin: '15% 0px' }).observe(band);
  addEventListener('scroll', onScroll, { passive: true });
  addEventListener('resize', () => { if (near) { measure(); onScroll(); } }, { passive: true });
});
```

## Notes

- Accessibility: the SVG scene is `aria-hidden`, and a visually hidden list carries the five trades. The tape's promises are repeated in the visible lead, and the heading, lead and links are ordinary HTML, so nothing depends on moving text.
- The text moves only while you scroll (`startOffset` follows the band's scroll progress, read in a passive rAF loop gated by an IntersectionObserver). The unroll is a `stroke-dashoffset` on a round-capped mask stroke; once both tracks are fully drawn the masks are dropped (`.path-text--open`), so later scrolling only repaints text.
- Without JS, or under reduced motion, the banner is static and fully drawn, with the text at mid-travel. If the band is already on screen at load it stays drawn, so nothing flashes away.
- Mobile: one 1600×640 scene with `preserveAspectRatio="xMidYMid slice"` is cropped by the band's CSS `aspect-ratio` (4:5 on phones, 2:1 from 768px, 5:2 from 1024px). The steep middle of the curves fills the crop, and the type stays at about 20px or more on the ribbon.
- Contrast: white ribbon text runs from 4.9:1 on `--primary` to 5.1:1 on the deepened teal end; tape text is 18.8:1 on `--surface-deep`. To change a curve, keep it x-monotonic and about 700 units off-canvas on the left, so `startOffset` (the `data-path-text-track` from, to and delay values) never shows an empty start.
