# Pinned Horizontal Scroll

A "Recent work" section that pins while vertical scroll carries a row of six tall project panels sideways. Each photo drifts inside its frame more slowly than the track, the panel under the focus line lifts to full brightness while the rest sit dimmed, and a rolling mono counter ("03 / 06") rides a gradient progress rail. Below 768px, under reduced motion and without JS it becomes a native swipeable scroll-snap row of 85vw panels. Depends on `tokens/variables.css`.

**Motion:** track travel, in-frame photo parallax, focus lift and dim, and rail fill, all scrubbed by scroll · counter digit roll (`--dur-4`, `--ease-spring`) · hover photo push (`--dur-5`, `--ease-out`) and arrow nudge (`--ease-spring`).

## HTML

```html
<div class="hscroll-demo">
  <div class="hscroll-demo__note">
    <p>The section pins and the projects travel sideways as you scroll.</p>
    <span class="hscroll-demo__hint">Scroll <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg></span>
  </div>

  <section class="hscroll" aria-labelledby="hscroll-title" data-hscroll>
    <div class="hscroll__stage">
      <header class="hscroll__head">
        <div>
          <p class="hscroll__eyebrow">Recent work</p>
          <h2 id="hscroll-title" class="hscroll__title">Homes we've rebuilt, <span>room by room.</span></h2>
        </div>
        <div class="hscroll__aside">
          <p class="hscroll__lead">Six recent projects across Springfield, each delivered on schedule and signed off by the family who lives there.</p>
          <a class="hscroll__all" href="#projects">
            All projects
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
        </div>
      </header>

      <div class="hscroll__viewport">
        <ul class="hscroll__track" role="list" aria-label="Recent projects">
          <li class="hscroll__panel">
            <div class="hscroll__card">
              <h3 class="hscroll__name"><a class="hscroll__link" href="#alder-street">The Alder Street kitchen<svg class="hscroll__arrow" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></a></h3>
              <p class="hscroll__chip">Kitchen · Northside</p>
              <p class="hscroll__year"><time datetime="2026">2026</time></p>
              <div class="hscroll__frame"><img class="hscroll__img" src="northside-kitchen.jpg" width="960" height="1200" alt="Kitchen with white oak cabinets, a quartz island and three brass pendants" loading="lazy" decoding="async"></div>
            </div>
          </li>
          <li class="hscroll__panel">
            <div class="hscroll__card">
              <h3 class="hscroll__name"><a class="hscroll__link" href="#spa-bath">A spa bath under the eaves<svg class="hscroll__arrow" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></a></h3>
              <p class="hscroll__chip">Bathroom · Westlake</p>
              <p class="hscroll__year"><time datetime="2026">2026</time></p>
              <div class="hscroll__frame"><img class="hscroll__img" src="westlake-bath.jpg" width="960" height="1200" alt="Freestanding tub beneath a sloped skylight with green zellige tile" loading="lazy" decoding="async"></div>
            </div>
          </li>
          <li class="hscroll__panel">
            <div class="hscroll__card">
              <h3 class="hscroll__name"><a class="hscroll__link" href="#farmhouse">Riverside farmhouse, rewired<svg class="hscroll__arrow" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></a></h3>
              <p class="hscroll__chip">Whole home · Riverside</p>
              <p class="hscroll__year"><time datetime="2025">2025</time></p>
              <div class="hscroll__frame"><img class="hscroll__img" src="riverside-farmhouse.jpg" width="960" height="1200" alt="Farmhouse living room with exposed beams and a limestone fireplace" loading="lazy" decoding="async"></div>
            </div>
          </li>
          <li class="hscroll__panel">
            <div class="hscroll__card">
              <h3 class="hscroll__name"><a class="hscroll__link" href="#lower-level">A lower level worth living in<svg class="hscroll__arrow" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></a></h3>
              <p class="hscroll__chip">Basement · Springfield</p>
              <p class="hscroll__year"><time datetime="2025">2025</time></p>
              <div class="hscroll__frame"><img class="hscroll__img" src="springfield-basement.jpg" width="960" height="1200" alt="Finished basement with a walnut media wall and built-in shelving" loading="lazy" decoding="async"></div>
            </div>
          </li>
          <li class="hscroll__panel">
            <div class="hscroll__card">
              <h3 class="hscroll__name"><a class="hscroll__link" href="#cedar-porch">Cedar porch, new roofline<svg class="hscroll__arrow" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></a></h3>
              <p class="hscroll__chip">Exterior · Westlake</p>
              <p class="hscroll__year"><time datetime="2024">2024</time></p>
              <div class="hscroll__frame"><img class="hscroll__img" src="westlake-porch.jpg" width="960" height="1200" alt="Cedar front porch with tapered columns under a standing-seam roof" loading="lazy" decoding="async"></div>
            </div>
          </li>
          <li class="hscroll__panel">
            <div class="hscroll__card">
              <h3 class="hscroll__name"><a class="hscroll__link" href="#garden-room">A garden room for all seasons<svg class="hscroll__arrow" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></a></h3>
              <p class="hscroll__chip">Addition · Northside</p>
              <p class="hscroll__year"><time datetime="2024">2024</time></p>
              <div class="hscroll__frame"><img class="hscroll__img" src="northside-garden-room.jpg" width="960" height="1200" alt="Glazed garden room addition opening onto a brick patio" loading="lazy" decoding="async"></div>
            </div>
          </li>
        </ul>
      </div>

      <div class="hscroll__meter" aria-hidden="true" hidden>
        <p class="hscroll__count"><span class="hscroll__window"><span class="hscroll__digits"></span></span><span class="hscroll__total"></span></p>
        <span class="hscroll__rail"><span class="hscroll__fill"></span><span class="hscroll__spark"></span></span>
      </div>
    </div>
  </section>

  <div class="hscroll-demo__note">
    <p>The pin releases after the last project and the page carries on.</p>
  </div>
</div>
```

## CSS

```css
/* Section: deep surface. --hscroll-edge lines the header, track and rail up with the page container */
.hscroll {
  --hscroll-w: clamp(16rem, 26vw, 23rem);
  --hscroll-gap: clamp(1rem, 0.5rem + 1.5vw, 1.75rem);
  --hscroll-edge: max(var(--gutter), (100% - var(--container-max)) / 2);
  --hscroll-lift: 1.25rem;
  position: relative; isolation: isolate; overflow-x: clip;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.hscroll :where(h2, h3, p) { margin: 0; }
.hscroll__stage { position: relative; display: grid; gap: clamp(2rem, 4vw, 3rem); padding-block: clamp(4rem, 9vw, 7rem); }
.hscroll__stage::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background:
    radial-gradient(55% 45% at 8% 0%, color-mix(in srgb, var(--primary) 24%, transparent), transparent 70%),
    radial-gradient(45% 40% at 96% 100%, color-mix(in srgb, var(--primary-2) 20%, transparent), transparent 70%);
}

/* Header */
.hscroll__head { display: grid; gap: 1.25rem 4rem; align-items: end; padding-inline: var(--hscroll-edge); }
.hscroll__eyebrow { display: flex; align-items: center; gap: 0.75rem; color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.hscroll__eyebrow::before { content: ""; width: 1.75rem; height: 1px; background: var(--gradient-brand); }
.hscroll__title { margin-top: 1rem; font: 600 clamp(2rem, 1.2rem + 2.8vw, 3.5rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.hscroll__title span { color: var(--text-inverse-muted); }
.hscroll__aside { display: grid; gap: 1.25rem; justify-items: start; }
.hscroll__lead { max-width: 28rem; color: var(--text-inverse-muted); line-height: 1.6; }
.hscroll__all {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: background-color var(--dur-2) var(--ease-out);
}
.hscroll__all:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.hscroll__all svg, .hscroll__arrow { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.hscroll__all:hover svg { transform: translateX(3px); }
.hscroll :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Track: a native scroll-snap row until JS pins it */
.hscroll__track {
  position: relative; display: flex; gap: var(--hscroll-gap); margin: 0; padding: 0.875rem var(--hscroll-edge) 1.25rem; list-style: none;
  overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x mandatory; scroll-padding-inline: var(--hscroll-edge);
  scrollbar-width: thin; scrollbar-color: var(--border-inverse) transparent;
}
.hscroll__panel { flex: none; width: min(85vw, 24rem); scroll-snap-align: start; }

/* Card: title row under a framed photo; the chip floats on the photo */
.hscroll__card { position: relative; display: grid; grid-template-columns: minmax(0, 1fr) auto; grid-template-rows: auto auto; gap: 1rem 1.25rem; }
.hscroll__frame {
  grid-area: 1 / 1 / 2 / 3; position: relative; isolation: isolate; aspect-ratio: 4 / 5; overflow: hidden; border-radius: var(--radius-2xl);
  background:
    radial-gradient(80% 60% at 20% 10%, color-mix(in srgb, var(--primary-2) 45%, transparent), transparent 70%),
    linear-gradient(160deg, color-mix(in srgb, var(--primary) 45%, var(--surface-deep)), var(--surface-dark));
  box-shadow: 0 30px 60px -30px color-mix(in srgb, var(--primary) 45%, transparent);
}
.hscroll__img {
  position: absolute; top: 0; left: -12%; display: block; width: 124%; max-width: none; height: 100%; object-fit: cover;
  transition: scale var(--dur-5) var(--ease-out);
}
.hscroll__frame::before { /* focus dim: deepens every panel except the one under the focus line */
  content: ""; position: absolute; inset: 0; z-index: 1; pointer-events: none;
  background: var(--surface-deep); opacity: calc((1 - var(--hscroll-f, 1)) * 0.55);
}
.hscroll__frame::after { /* hairline and top sheen */
  content: ""; position: absolute; inset: 0; z-index: 2; border-radius: inherit; pointer-events: none;
  background: linear-gradient(180deg, color-mix(in srgb, var(--surface-deep) 40%, transparent), transparent 28%);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.hscroll__chip {
  grid-area: 1 / 1; z-index: 3; align-self: start; justify-self: start; margin: 0.875rem;
  padding: 0.4375rem 0.75rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 70%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
}
.hscroll__name { grid-area: 2 / 1; align-self: baseline; font: 600 clamp(1.0625rem, 0.95rem + 0.4vw, 1.3125rem)/1.25 var(--font-display); letter-spacing: var(--tracking-tight); }
.hscroll__link { color: inherit; text-decoration: none; }
.hscroll__link::after { content: ""; position: absolute; inset: -0.375rem; z-index: 4; border-radius: calc(var(--radius-2xl) + 0.375rem); }
.hscroll .hscroll__link:focus-visible { outline: 2px solid transparent; }
.hscroll__link:focus-visible::after { outline: 2px solid var(--text-inverse); outline-offset: 2px; }
.hscroll__arrow { display: inline-block; margin-left: 0.375rem; vertical-align: -0.125em; color: var(--text-inverse-muted); }
.hscroll__year { grid-area: 2 / 2; align-self: baseline; color: var(--text-inverse-muted); font: 500 0.8125rem var(--font-mono); font-variant-numeric: tabular-nums; }
.hscroll__card:hover .hscroll__img { scale: 1.05; }
.hscroll__card:hover .hscroll__arrow { transform: translate(2px, -2px); color: var(--text-inverse); }

/* Meter: rolling counter and gradient rail (JS only) */
.hscroll__meter { display: flex; align-items: center; gap: clamp(1rem, 3vw, 2rem); padding-inline: var(--hscroll-edge); }
.hscroll__meter[hidden] { display: none; }
.hscroll__count { display: flex; align-items: center; gap: 0.5rem; font: 500 clamp(1.75rem, 1.2rem + 1.6vw, 2.75rem)/1 var(--font-mono); letter-spacing: -0.06em; }
.hscroll__window { display: inline-block; height: 1em; overflow: hidden; }
.hscroll__digits { display: block; transform: translateY(calc(var(--hscroll-i, 0) * -1em)); transition: transform var(--dur-4) var(--ease-spring); }
.hscroll__digits span {
  display: block; height: 1em;
  background: linear-gradient(180deg, var(--text-inverse) 20%, color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hscroll__total { color: var(--text-inverse-muted); font-size: 0.42em; letter-spacing: 0; }
.hscroll__total::before { content: "/ "; }
.hscroll__rail { position: relative; flex: 1; height: 2px; border-radius: 2px; background: var(--border-inverse); }
.hscroll__fill { position: absolute; inset: 0; border-radius: inherit; background: var(--gradient-brand); transform: scaleX(var(--hscroll-p, 0)); transform-origin: left; }
.hscroll__spark { position: absolute; inset: 0; transform: translateX(calc(var(--hscroll-p, 0) * 100%)); pointer-events: none; }
.hscroll__spark::before {
  content: ""; position: absolute; left: -4px; top: -3px; width: 8px; height: 8px; border-radius: 50%; background: var(--text-inverse);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--primary-2) 30%, transparent), 0 0 18px 2px color-mix(in srgb, var(--primary-2) 80%, transparent);
}

@media (min-width: 768px) {
  .hscroll__head { grid-template-columns: minmax(0, 1.3fr) minmax(0, 0.7fr); }
}

/* Pinned (JS, 768px+, motion allowed): tall wrapper, sticky stage, track moved by --hscroll-p */
.hscroll--pinned { height: calc(100vh + var(--hscroll-h, 0px)); height: calc(100svh + var(--hscroll-h, 0px)); }
.hscroll--pinned .hscroll__stage {
  position: sticky; top: 0; height: 100vh; height: 100svh; overflow: clip;
  grid-template-rows: auto minmax(0, 1fr) auto; gap: clamp(1.25rem, 3.5vh, 2.5rem);
  padding-block: clamp(2rem, 7vh, 4.5rem) clamp(1.25rem, 4vh, 2.5rem);
}
.hscroll--pinned .hscroll__title { font-size: clamp(1.75rem, 6.4vh, 3.5rem); }
.hscroll--pinned .hscroll__viewport { overflow: clip; container-type: size; }
.hscroll--pinned .hscroll__track {
  box-sizing: border-box; width: max-content; height: 100%; padding-block: 0.875rem var(--hscroll-lift); overflow: visible; scroll-snap-type: none;
  transform: translate3d(calc(var(--hscroll-p, 0) * var(--hscroll-h, 0px) * -1), 0, 0); will-change: transform;
}
.hscroll--pinned .hscroll__panel { width: var(--hscroll-w); width: min(var(--hscroll-w), 62cqh); }
.hscroll--pinned .hscroll__card { height: 100%; grid-template-rows: minmax(0, 1fr) auto; transform: translate3d(0, calc((1 - var(--hscroll-f, 1)) * var(--hscroll-lift)), 0); }
.hscroll--pinned .hscroll__frame { aspect-ratio: auto; }
.hscroll--pinned .hscroll__img { transform: translate3d(calc(var(--hscroll-d, 0) * -9%), 0, 0); }

/* Demo scroll room */
.hscroll-demo { background: var(--surface-deep); color: var(--text-inverse-muted); font-family: var(--font-sans); }
.hscroll-demo__note { display: grid; place-content: center; justify-items: center; gap: 1rem; min-height: 70vh; padding: 2rem var(--gutter); text-align: center; }
.hscroll-demo__note p { margin: 0; max-width: 30rem; font-size: 1.0625rem; line-height: 1.6; }
.hscroll-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--text-inverse); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.hscroll-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const wide = matchMedia('(min-width: 768px)');
const clamp = (v, min = 0, max = 1) => Math.min(max, Math.max(min, v));
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? Math.min(1, Math.max(0, -r.top / range)) : 0; };

document.querySelectorAll('[data-hscroll]').forEach((root) => {
  const viewport = root.querySelector('.hscroll__viewport');
  const track = root.querySelector('.hscroll__track');
  const panels = [...track.children];
  const meter = root.querySelector('.hscroll__meter');
  const pad = (n) => String(n).padStart(2, '0');
  let pinned = false, near = false, frame = 0, overflow = 0, half = 0, step = 1, span = 0, centers = [], current = -1;

  // The counter is a rolling strip of 01…0n; it only exists with JS
  meter.querySelector('.hscroll__digits').innerHTML = panels.map((_, i) => `<span>${pad(i + 1)}</span>`).join('');
  meter.querySelector('.hscroll__total').textContent = pad(panels.length);
  meter.hidden = false;

  // Shift = how far the track has travelled: page scroll while pinned, the row's own scroll otherwise
  const render = () => {
    frame = 0;
    const shift = pinned ? progress(root) * overflow : track.scrollLeft;
    const p = overflow ? clamp(shift / overflow) : 0;
    const focus = centers[0] + p * span; // focus line walks from the first panel to the last
    root.style.setProperty('--hscroll-p', p.toFixed(4));
    panels.forEach((panel, i) => {
      panel.style.setProperty('--hscroll-d', clamp((centers[i] - shift - half) / (half + step), -1).toFixed(3));
      panel.style.setProperty('--hscroll-f', clamp(1 - Math.abs(centers[i] - focus) / step).toFixed(3));
    });
    const index = Math.round((focus - centers[0]) / step);
    if (index !== current) root.style.setProperty('--hscroll-i', (current = index));
  };
  const queue = () => { if (!frame) frame = requestAnimationFrame(render); };

  // Pin only on wide screens with motion allowed; the wrapper grows by exactly the track overflow
  const measure = () => {
    pinned = wide.matches && !reduce.matches;
    root.classList.toggle('hscroll--pinned', pinned);
    overflow = Math.max(0, track.scrollWidth - viewport.clientWidth);
    root.style.setProperty('--hscroll-h', `${overflow}px`);
    half = viewport.clientWidth / 2;
    centers = panels.map((el) => el.offsetLeft + el.offsetWidth / 2);
    step = centers[1] - centers[0] || 1;
    span = centers[centers.length - 1] - centers[0];
    render();
  };

  // Keyboard: focusing a panel's link while pinned scrolls the page to where that panel is in focus
  track.addEventListener('focusin', (e) => {
    const panel = e.target.closest('.hscroll__panel');
    if (!pinned || !panel || !e.target.matches(':focus-visible')) return;
    const p = span ? (centers[panels.indexOf(panel)] - centers[0]) / span : 0;
    const top = root.getBoundingClientRect().top + scrollY + p * (root.offsetHeight - innerHeight);
    scrollTo({ top, behavior: reduce.matches ? 'auto' : 'smooth' });
  });

  new IntersectionObserver((entries) => { near = entries.at(-1).isIntersecting; if (near) queue(); }, { rootMargin: '25% 0px' }).observe(root);
  addEventListener('scroll', () => { if (near && pinned) queue(); }, { passive: true });
  track.addEventListener('scroll', () => { if (!pinned) queue(); }, { passive: true });
  const resize = new ResizeObserver(measure);
  resize.observe(viewport);
  resize.observe(track);
  wide.addEventListener('change', measure);
  reduce.addEventListener('change', measure);
  measure();
});
```

## Notes

- Projects are a real list: each panel has an `<h3>` link (stretched over the card, with the focus ring drawn round the whole card), a descriptive `alt`, and a `<time>` year. The counter and rail are decorative (`aria-hidden`). While pinned, tabbing to a panel's link smooth-scrolls the page (instantly under reduced motion) to the point where that panel is the lit one.
- Fallback below 768px, under reduced motion and without JS: no pin. The track is a native scroll-snap row (85vw panels, capped at 24rem) that works with touch, trackpad, keyboard and a thin scrollbar. With JS, the counter, rail and dimming follow the row's own scroll. Without JS the meter stays `hidden`.
- Pinned mechanics: the section's height is `100svh + --hscroll-h` (the track's overflow, re-measured by `ResizeObserver`), the stage is `position: sticky`, and the track moves by `translate3d(-p × overflow)`. A focus line walks from the first panel to the last, so the counter reads 01 at the start and 06 at the end. Clipping uses `overflow: clip`, which keeps sticky working.
- Contrast: titles are `--text-inverse` on `--surface-deep` (19:1), and years, lead and the muted half of the heading are `--text-inverse-muted` (7:1). The chip sits on 70% deep glass, which holds 7.2:1 even over a pure-white photo. Dimming only darkens photos, never text.
- Panels size to the stage height with container query units (`62cqh`). Browsers without them use the fixed `--hscroll-w`. Add or remove panels freely; the counter builds itself, and `--hscroll-lift` sets the lift height.
