# Text Mask Zoom

A giant "HOME" is cut out of a deep overlay, and through the letters you see a vivid dusk scene: an aurora sky built from brand tokens over an SVG rooftop skyline with lit windows. As the section pins, the letters scale up dramatically around a point inside the O's stroke, so you fly through the letter. The scene fills the screen, the overlay fades away, and the real content (heading, copy and three stats) rises onto the sky. On phones the word fits the width through its viewBox. Depends on `tokens/variables.css`.

**Motion:** letter zoom inside the SVG mask (cubic `1 + 29t³`), overlay fade, sky push-in, skyline rise, and content rise with de-blur, all scrubbed by scroll.

## HTML

```html
<div class="mask-zoom-demo">
  <div class="mask-zoom-demo__note">
    <p>Fly through the letters into the neighbourhood.</p>
    <span class="mask-zoom-demo__hint">Scroll <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg></span>
  </div>

  <section class="mask-zoom" aria-labelledby="mask-zoom-title" data-mask-zoom>
    <div class="mask-zoom__stage">
      <div class="mask-zoom__scene" aria-hidden="true">
        <span class="mask-zoom__sky"></span>
        <svg class="mask-zoom__skyline" viewBox="0 0 1440 360" preserveAspectRatio="xMidYMax slice" focusable="false">
          <path class="mask-zoom__far" d="M0 360V262l40-22 40 22v-14l70-40 70 40v10h40v-36l26-18 26 18v24l60-34 60 34v-8l50-30 50 30v18h30v-46h24v-20h20v20h24v46l40-24 40 24v-12l64-36 64 36v14l46-26 46 26v-20l58-32 58 32v8h36v-30l30-20 30 20v30l52-30 52 30v-6l44-26 44 26h46l30-18 30 18V360z" />
          <path class="mask-zoom__near" d="M0 360V236l112-82 112 82v124zM150 200v-40h20v40zM244 360V252l56-46h124l50 46v108zM502 360v-48a40 40 0 1 1 18 0v48zM548 360V206l112-92 112 92v154zM712 180v-48h22v48zM792 360V262l92-62 92 62v98zM996 360V244l58-50 58 50 56-52 58 52v116zM1246 360V228l97-70 97 70v132z" />
          <g class="mask-zoom__windows">
            <rect x="52" y="266" width="24" height="30" rx="2" /><rect x="140" y="266" width="24" height="30" rx="2" />
            <rect x="606" y="226" width="22" height="28" rx="2" /><rect x="692" y="226" width="22" height="28" rx="2" /><rect x="648" y="166" width="24" height="24" rx="12" />
            <rect x="868" y="282" width="32" height="26" rx="2" /><rect x="1036" y="262" width="22" height="28" rx="2" /><rect x="1150" y="262" width="22" height="28" rx="2" />
            <rect x="1300" y="250" width="26" height="32" rx="2" /><rect x="1362" y="250" width="26" height="32" rx="2" />
          </g>
        </svg>
      </div>

      <div class="mask-zoom__panel" aria-hidden="true">
        <svg class="mask-zoom__overlay" viewBox="0 0 1130 600" preserveAspectRatio="xMidYMid meet" focusable="false">
          <defs>
            <mask id="mask-zoom-cut" maskUnits="userSpaceOnUse" x="-20000" y="-20000" width="40000" height="40000">
              <rect x="-20000" y="-20000" width="40000" height="40000" fill="white" />
              <g class="mask-zoom__word" fill="black"><g transform="translate(60 150)">
                <path d="M40 30h64v96h72V30h64v240h-64v-96h-72v96H40z" />
                <path d="M390 30a120 120 0 1 1 0 240a120 120 0 1 1 0-240zm0 64a56 56 0 1 0 0 112a56 56 0 1 0 0-112z" fill-rule="evenodd" />
                <path d="M540 270V30h72l53 120 53-120h72v240h-64V140l-43 100h-36l-43-100v130z" />
                <path d="M820 30h150v52h-86v42h76v52h-76v42h86v52H820z" />
              </g></g>
            </mask>
          </defs>
          <rect class="mask-zoom__shade" x="-20000" y="-20000" width="40000" height="40000" mask="url(#mask-zoom-cut)" />
          <g class="mask-zoom__word mask-zoom__edge"><g transform="translate(60 150)">
            <path d="M40 30h64v96h72V30h64v240h-64v-96h-72v96H40z" />
            <path d="M390 30a120 120 0 1 1 0 240a120 120 0 1 1 0-240zm0 64a56 56 0 1 0 0 112a56 56 0 1 0 0-112z" />
            <path d="M540 270V30h72l53 120 53-120h72v240h-64V140l-43 100h-36l-43-100v130z" />
            <path d="M820 30h150v52h-86v42h76v52h-76v42h86v52H820z" />
          </g></g>
        </svg>
        <p class="mask-zoom__tag">Brand · Springfield · Est. 2009</p>
        <p class="mask-zoom__cue">Scroll to come inside <svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg></p>
      </div>

      <div class="mask-zoom__content">
        <p class="mask-zoom__eyebrow">Springfield's home team</p>
        <h2 id="mask-zoom-title" class="mask-zoom__title">We treat every house like it's our own.</h2>
        <p class="mask-zoom__lead">A family-run crew of licensed plumbers, electricians and carpenters, looking after Westlake, Northside and Riverside homes since 2009.</p>
        <ul class="mask-zoom__stats" role="list">
          <li><strong>17</strong><span>years in Springfield</span></li>
          <li><strong>9,400+</strong><span>homes cared for</span></li>
          <li><strong>4.9/5</strong><span>average rating</span></li>
        </ul>
      </div>
    </div>
  </section>

  <div class="mask-zoom-demo__note">
    <p>The scene lets go and the page carries on.</p>
  </div>
</div>
```

## CSS

```css
/* Section: a deep overlay with a vivid scene behind. --mask-zoom-origin is in the word's user units */
.mask-zoom {
  --mask-zoom-origin: 538px 300px; /* user units: inside the right stroke of the O */
  position: relative; isolation: isolate; overflow-x: clip;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.mask-zoom :where(h2, p, ul) { margin: 0; }
.mask-zoom__stage { position: relative; isolation: isolate; }

/* Scene: aurora sky from brand tokens, stars, and a two-layer rooftop skyline */
.mask-zoom__scene { position: absolute; inset: 0; z-index: -1; overflow: hidden; }
.mask-zoom__sky {
  position: absolute; inset: 0;
  background:
    radial-gradient(1.5px 1.5px at 12% 14%, var(--text-inverse), transparent),
    radial-gradient(1px 1px at 31% 8%, var(--text-inverse), transparent),
    radial-gradient(1.5px 1.5px at 58% 12%, var(--text-inverse), transparent),
    radial-gradient(1px 1px at 72% 22%, var(--text-inverse), transparent),
    radial-gradient(1.5px 1.5px at 88% 9%, var(--text-inverse), transparent),
    radial-gradient(1px 1px at 46% 26%, var(--text-inverse), transparent),
    linear-gradient(112deg, transparent 28%, color-mix(in srgb, var(--primary-2) 38%, transparent) 42%, transparent 58%),
    radial-gradient(60% 42% at 22% 30%, color-mix(in srgb, var(--primary-2) 50%, transparent), transparent 70%),
    radial-gradient(50% 38% at 78% 18%, color-mix(in srgb, var(--primary) 65%, transparent), transparent 70%),
    radial-gradient(75% 32% at 50% 88%, color-mix(in srgb, var(--accent) 60%, transparent), transparent 70%),
    linear-gradient(180deg, var(--surface-deep) 0%, color-mix(in srgb, var(--primary) 55%, var(--surface-deep)) 55%, color-mix(in srgb, var(--primary-2) 45%, var(--primary)) 100%);
}
.mask-zoom__skyline { position: absolute; left: 0; bottom: 0; width: 100%; height: min(42%, 22rem); }
.mask-zoom__far { fill: color-mix(in srgb, var(--surface-deep) 70%, var(--primary)); }
.mask-zoom__near { fill: var(--surface-deep); }
.mask-zoom__windows { fill: color-mix(in srgb, var(--accent) 80%, var(--surface-light)); }
.mask-zoom__windows rect:nth-child(3n + 2) { opacity: 0.35; }

/* Overlay: one deep rect, cut by black letters in an SVG mask */
.mask-zoom__panel { position: relative; height: 78vh; height: 78svh; min-height: 24rem; max-height: 46rem; }
.mask-zoom__overlay {
  position: absolute; inset: 0; width: 100%; height: 100%;
  -webkit-mask-image: linear-gradient(black 72%, transparent); mask-image: linear-gradient(black 72%, transparent);
}
.mask-zoom__shade { fill: var(--surface-deep); }
.mask-zoom__word { transform-box: view-box; transform-origin: var(--mask-zoom-origin); }
.mask-zoom__edge { fill: none; stroke: color-mix(in srgb, var(--primary-2) 60%, var(--text-inverse)); stroke-opacity: 0.55; }
.mask-zoom__edge path { stroke-width: 1.5; vector-effect: non-scaling-stroke; }
.mask-zoom__tag, .mask-zoom__cue {
  position: absolute; left: 50%; translate: -50% 0; display: inline-flex; align-items: center; gap: 0.5rem; white-space: nowrap;
  color: var(--text-inverse-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase;
}
.mask-zoom__tag { top: clamp(1.5rem, 9%, 4rem); }
.mask-zoom__cue { bottom: clamp(1.5rem, 9%, 4rem); display: none; }
.mask-zoom__cue svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* Content: the real heading, copy and stats on the scene */
.mask-zoom__content {
  position: relative; display: grid; justify-items: center; gap: 1.25rem; max-width: var(--container-max); margin-inline: auto;
  padding: clamp(1.5rem, 5vw, 3rem) var(--gutter) clamp(4rem, 10vw, 7rem); text-align: center;
}
.mask-zoom__content::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--surface-deep) 60%, transparent), transparent);
}
.mask-zoom__eyebrow { font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; }
.mask-zoom__title {
  max-width: 16ch; font: 600 clamp(2.25rem, 1.3rem + 3.6vw, 4.25rem)/1 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance;
  text-shadow: 0 2px 32px color-mix(in srgb, var(--surface-deep) 55%, transparent);
}
.mask-zoom__lead { max-width: 36rem; font-size: clamp(1rem, 0.95rem + 0.3vw, 1.1875rem); line-height: 1.6; text-wrap: pretty; }
.mask-zoom__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.5rem; width: min(100%, 40rem); margin-top: 0.75rem; padding: 0; list-style: none; }
.mask-zoom__stats li {
  display: grid; align-content: start; gap: 0.375rem; padding: 0.875rem 0.5rem; border-radius: var(--radius-xl);
  background: color-mix(in srgb, var(--surface-deep) 75%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
}
.mask-zoom__stats strong { font: 600 clamp(1.25rem, 0.9rem + 2vw, 2.25rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.mask-zoom__stats span { color: var(--text-inverse-muted); font-size: clamp(0.6875rem, 0.65rem + 0.2vw, 0.8125rem); line-height: 1.3; }
@media (min-width: 768px) {
  .mask-zoom__stats { gap: 0.75rem; }
  .mask-zoom__stats li { padding: 1.125rem 1rem; }
}

/* Pinned (JS, motion allowed): one scrub value, phases derived here */
.mask-zoom--pinned {
  --mask-zoom-t: clamp(0, (var(--mask-zoom-p, 0) - 0.06) / 0.66, 1);
  --mask-zoom-s: calc(1 + 29 * var(--mask-zoom-t) * var(--mask-zoom-t) * var(--mask-zoom-t));
  --mask-zoom-fade: clamp(0, (var(--mask-zoom-p, 0) - 0.58) / 0.16, 1);
  --mask-zoom-c: clamp(0, (var(--mask-zoom-p, 0) - 0.7) / 0.22, 1);
  --mask-zoom-k: calc(var(--mask-zoom-c) * (2 - var(--mask-zoom-c)));
  height: 240vh; height: 240svh;
}
.mask-zoom--pinned .mask-zoom__stage { position: sticky; top: 0; height: 100vh; height: 100svh; overflow: clip; }
.mask-zoom--pinned .mask-zoom__panel { position: absolute; inset: 0; height: auto; min-height: 0; max-height: none; }
.mask-zoom--pinned .mask-zoom__overlay { -webkit-mask-image: none; mask-image: none; opacity: calc(1 - var(--mask-zoom-fade)); }
.mask-zoom--pinned .mask-zoom__word { transform: scale(var(--mask-zoom-s)); }
.mask-zoom--pinned .mask-zoom__tag, .mask-zoom--pinned .mask-zoom__cue { opacity: calc(1 - var(--mask-zoom-t) * 6); }
.mask-zoom--pinned .mask-zoom__cue { display: inline-flex; }
.mask-zoom--pinned .mask-zoom__sky { transform: scale(calc(1 + var(--mask-zoom-t) * 0.1)); }
.mask-zoom--pinned .mask-zoom__skyline { transform: translate3d(0, calc((1 - var(--mask-zoom-t)) * 14%), 0); }
.mask-zoom--pinned .mask-zoom__content {
  position: absolute; inset: 0; z-index: 1; align-content: center; max-width: none; padding-block: var(--gutter);
  opacity: var(--mask-zoom-k); transform: translate3d(0, calc((1 - var(--mask-zoom-k)) * 3rem), 0); filter: blur(calc((1 - var(--mask-zoom-k)) * 8px));
}
.mask-zoom.is-through .mask-zoom__overlay { visibility: hidden; }
@media (min-width: 768px) {
  .mask-zoom--pinned { height: 300vh; height: 300svh; }
}

/* Demo scroll room */
.mask-zoom-demo { background: var(--surface-deep); color: var(--text-inverse-muted); font-family: var(--font-sans); }
.mask-zoom-demo__note { display: grid; place-content: center; justify-items: center; gap: 1rem; min-height: 70vh; padding: 2rem var(--gutter); text-align: center; }
.mask-zoom-demo__note p { margin: 0; max-width: 30rem; font-size: 1.0625rem; line-height: 1.6; }
.mask-zoom-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--text-inverse); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.mask-zoom-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? Math.min(1, Math.max(0, -r.top / range)) : 0; };

document.querySelectorAll('[data-mask-zoom]').forEach((root, n) => {
  const mask = root.querySelector('mask');
  const shade = root.querySelector('.mask-zoom__shade');
  let pinned = false, near = false, frame = 0;

  // Each instance needs its own mask id, or every copy would cut with the first one's zoom
  mask.id = `mask-zoom-cut-${n + 1}`;
  shade.setAttribute('mask', `url(#${mask.id})`);

  // One scrub value; CSS derives the zoom, fade, parallax and content rise.
  // Once the overlay has faded it's hidden, so the browser stops repainting the mask.
  const render = () => {
    frame = 0;
    if (!pinned) return;
    const p = progress(root);
    root.style.setProperty('--mask-zoom-p', p.toFixed(4));
    root.classList.toggle('is-through', p > 0.75);
  };
  const queue = () => { if (!frame) frame = requestAnimationFrame(render); };

  // Pin only when motion is allowed; otherwise the static word and content stay
  const measure = () => {
    pinned = !reduce.matches;
    root.classList.toggle('mask-zoom--pinned', pinned);
    if (!pinned) root.classList.remove('is-through');
    render();
  };

  new IntersectionObserver((entries) => { near = entries.at(-1).isIntersecting; if (near) queue(); }, { rootMargin: '25% 0px' }).observe(root);
  addEventListener('scroll', () => { if (near && pinned) queue(); }, { passive: true });
  new ResizeObserver(queue).observe(root);
  reduce.addEventListener('change', measure);
  measure();
});
```

## Notes

- Accessibility: the word, its captions and the scene are decorative (`aria-hidden`, SVGs `focusable="false"`). The real `<h2>`, copy and stats list live in the content block, in reading order, and contain nothing focusable, so the scrubbed fade-in never hides a focus target.
- Fallback without JS and under reduced motion: no pin and no zoom. A 78svh panel shows the static word with the scene through it and fades into the content block below, which sits on the same scene. JS adds `.mask-zoom--pinned` only when motion is allowed and follows the setting if it changes.
- How it's built: the overlay is a single SVG, a deep rect masked by a white rect with black letters. The letters are paths, so the cut and the zoom origin are identical in every font. JS writes `--mask-zoom-p`, and CSS scales the letters inside the mask by `1 + 29t³` around `--mask-zoom-origin`. The SVG itself stays viewport-sized, so nothing huge is rasterised. The overlay fades over 0.58–0.74 and is then `visibility: hidden`, so the mask stops repainting.
- Contrast: content text is `--text-inverse` over a 60% deep radial scrim, ≥ 7:1 against the brightest sky behind it. Stat labels sit on 75% deep glass, ≥ 4.8:1 even over the amber horizon. The overlay captions are `--text-inverse-muted` on deep (7:1).
- To change the word, redraw the paths (keep the viewBox centred on them) and move `--mask-zoom-origin` into a thick stroke of one letter, in user units. A point inside a counter would fly into the overlay instead of the scene. Multiple instances get unique mask ids from JS.
