# Variable Weight Wave

A type-specimen section whose headline behaves like a lens. Each letter's Geist weight (400 to 800) and a slight lift follow the cursor with a smooth Gaussian falloff, and a blue-to-teal tint rides the crest, so a magnifying wave rolls through the words. As the heading enters view a single wave sweeps it left to right, a light pools on the baseline under the crest, and a mono readout shows the live weight. On touch you drag across the headline to push the wave, and it coasts on after you let go. Depends on `tokens/variables.css`.

**Motion:** intro sweep (1.6s, ease-in-out) · crest follow (rAF, exponential ease) · touch push with momentum decay · per-letter weight, lift and tint from one Gaussian · baseline glow and link arrow (`--dur-3`, `--ease-spring`).

## HTML

```html
<section class="weight-wave" aria-labelledby="weight-wave-title" data-weight-wave>
  <div class="weight-wave__inner">
    <div class="weight-wave__top">
      <p class="weight-wave__eyebrow">Full-service care</p>
      <p class="weight-wave__specimen" aria-hidden="true">Specimen 01 · Geist Variable</p>
    </div>

    <div class="weight-wave__stage">
      <h2 id="weight-wave-title" class="weight-wave__title">
        <span class="weight-wave__line">We do the</span>
        <span class="weight-wave__line">heavy lifting.</span>
      </h2>
      <div class="weight-wave__rule" aria-hidden="true">
        <p class="weight-wave__hint" hidden>
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 8l-4 4 4 4M17 8l4 4-4 4M3 12h18" /></svg>
          <span class="weight-wave__hint-hover">Move across the type</span><span class="weight-wave__hint-touch">Drag across the type</span>
        </p>
        <p class="weight-wave__axis">wght <span class="weight-wave__value">400–800</span></p>
      </div>
    </div>

    <div class="weight-wave__foot">
      <div class="weight-wave__intro">
        <p class="weight-wave__lead">From permits to parts runs and the final sweep, one crew handles the whole job, so none of it lands on you.</p>
        <a class="weight-wave__link" href="#included">
          See what's included
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
      </div>
      <ol class="weight-wave__list" role="list">
        <li class="weight-wave__item"><span class="weight-wave__num" aria-hidden="true">01</span>Permits and paperwork</li>
        <li class="weight-wave__item"><span class="weight-wave__num" aria-hidden="true">02</span>Parts, hauling and disposal</li>
        <li class="weight-wave__item"><span class="weight-wave__num" aria-hidden="true">03</span>A spotless cleanup before we leave</li>
      </ol>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: light paper with faint brand light */
.weight-wave {
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(50% 60% at 88% 8%, color-mix(in srgb, var(--primary-2) 8%, transparent), transparent 70%),
    radial-gradient(45% 55% at 4% 92%, color-mix(in srgb, var(--primary) 7%, transparent), transparent 70%),
    var(--surface-light);
  color: var(--text-main); font-family: var(--font-sans);
}
.weight-wave__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.weight-wave a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; border-radius: 0.375rem; }

/* Specimen header */
.weight-wave__top {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.5rem 1.5rem;
  padding-bottom: 1rem; border-bottom: 1px solid var(--border-subtle);
}
.weight-wave__eyebrow, .weight-wave__specimen { margin: 0; font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.weight-wave__eyebrow { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--primary); }
.weight-wave__eyebrow::before { content: ""; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--gradient-brand); box-shadow: 0 0 0 3px color-mix(in srgb, var(--primary) 14%, transparent); }
.weight-wave__specimen { color: var(--text-muted); }

/* Stage: dotted specimen paper behind the headline */
.weight-wave__stage { position: relative; padding-top: clamp(2rem, 5vw, 3.5rem); }
.weight-wave__stage::before {
  content: ""; position: absolute; inset: 0 calc(var(--gutter) * -1) -1rem; z-index: -1; pointer-events: none;
  background: radial-gradient(circle, color-mix(in srgb, var(--text-main) 14%, transparent) 1px, transparent 1.5px) 0 0 / 1.5rem 1.5rem;
  -webkit-mask-image: radial-gradient(ellipse 65% 75% at 40% 45%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 65% 75% at 40% 45%, black, transparent 75%);
}
.weight-wave__title {
  position: relative; margin: 0; font: 600 clamp(2.75rem, 0.9rem + 8.4vw, 8rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); font-synthesis: none; touch-action: pan-y pinch-zoom;
}
.weight-wave__line { display: block; }

/* Letters (built by JS): fixed boxes; weight, lift and tint all come from --weight-wave-g (0–1) */
.weight-wave__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
.weight-wave__word { display: inline-block; white-space: nowrap; }
.weight-wave__char {
  display: inline-block; margin-right: -0.04em; letter-spacing: 0; text-align: center;
  font-weight: calc(400 + 400 * var(--weight-wave-g, 0));
  translate: 0 calc(var(--weight-wave-g, 0) * -0.08em);
  color: color-mix(in srgb,
    color-mix(in srgb, var(--primary) var(--weight-wave-s, 50%), var(--primary-2)) calc(var(--weight-wave-g, 0) * 100%),
    var(--text-main));
}
.weight-wave__title.is-measuring .weight-wave__char { width: auto; font-weight: 800; }

/* Baseline rule: light pools under the crest; hint and live weight readout */
.weight-wave__rule {
  position: relative; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem 1.5rem;
  margin-top: clamp(1.25rem, 3vw, 2rem); padding-top: 0.875rem; border-top: 1px solid var(--border-subtle);
}
.weight-wave__rule::before {
  content: ""; position: absolute; top: -2px; left: 0; width: clamp(8rem, 18vw, 16rem); height: 3px; border-radius: 999px; pointer-events: none;
  background: linear-gradient(90deg, transparent, var(--primary) 30%, var(--primary-2) 70%, transparent);
  box-shadow: 0 0 18px 2px color-mix(in srgb, var(--primary) 30%, transparent);
  translate: calc(var(--weight-wave-x, 0) * 1px - 50%) 0; opacity: var(--weight-wave-a, 0);
}
.weight-wave__hint, .weight-wave__axis { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; color: var(--text-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.06em; }
.weight-wave__hint { text-transform: uppercase; }
.weight-wave__hint[hidden] { display: none; }
.weight-wave__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.weight-wave__hint-touch { display: none; }
.weight-wave__axis { margin-left: auto; }
.weight-wave__value {
  min-width: 4.5rem; padding: 0.375rem 0.625rem; border-radius: 0.5rem; text-align: center;
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight);
  color: var(--text-main); font-variant-numeric: tabular-nums;
}

/* Foot: lead, link and what the crew carries */
.weight-wave__foot { display: grid; gap: 2rem; margin-top: clamp(2.5rem, 6vw, 4rem); }
.weight-wave__lead { max-width: 30rem; margin: 0; color: var(--text-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
.weight-wave__link { display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; margin-top: 0.75rem; color: var(--primary); font-weight: 600; text-decoration: none; }
.weight-wave__link svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.weight-wave__link:hover svg { translate: 3px 0; }
.weight-wave__list { display: grid; margin: 0; padding: 0; list-style: none; border-top: 1px solid var(--border-subtle); }
.weight-wave__item {
  display: flex; align-items: baseline; gap: 1rem; padding: 1rem 0; border-bottom: 1px solid var(--border-subtle);
  font: 600 clamp(1.0625rem, 1rem + 0.4vw, 1.25rem)/1.3 var(--font-display); letter-spacing: -0.01em;
}
.weight-wave__num { flex: none; color: var(--primary); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; }

/* Before the script runs, rest at the wave's base weight so nothing jumps */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .weight-wave__title { font-weight: 400; letter-spacing: 0.01em; }
}
@media (hover: none) {
  .weight-wave__hint-hover { display: none; }
  .weight-wave__hint-touch { display: inline; }
}
@media (min-width: 768px) {
  .weight-wave__foot { grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); align-items: start; gap: 4rem; }
}
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const span = (className, textContent = '') => Object.assign(document.createElement('span'), { className, textContent });

document.querySelectorAll('[data-weight-wave]').forEach((root) => {
  const stage = root.querySelector('.weight-wave__stage');
  const title = root.querySelector('.weight-wave__title');
  const value = root.querySelector('.weight-wave__value');
  if (reduce.matches || !title) return; // static medium weight

  // A hidden copy keeps the heading's text; letters go in one aria-hidden layer, grouped in no-wrap words
  const layer = span('weight-wave__letters');
  layer.setAttribute('aria-hidden', 'true');
  layer.append(...title.childNodes);
  const walker = document.createTreeWalker(layer, NodeFilter.SHOW_TEXT);
  const texts = [];
  while (walker.nextNode()) texts.push(walker.currentNode);
  texts.forEach((node) => node.replaceWith(...node.data.split(/(\s+)/).filter(Boolean).map((part) => {
    if (!part.trim()) return ' ';
    const word = span('weight-wave__word');
    word.append(...[...part].map((ch) => span('weight-wave__char', ch)));
    return word;
  })));
  title.append(span('weight-wave__sr', layer.textContent.replace(/\s+/g, ' ').trim()), layer);
  const chars = [...layer.querySelectorAll('.weight-wave__char')];
  const gs = chars.map(() => 0);
  let boxes = [];
  let sigma = 60;

  // Fix each letter's box at its weight-800 width, in em, so fluid font sizes need no re-measure
  const measure = () => {
    chars.forEach((c) => { c.style.width = ''; });
    title.classList.add('is-measuring');
    const size = parseFloat(getComputedStyle(title).fontSize);
    const widths = chars.map((c) => c.getBoundingClientRect().width / size);
    title.classList.remove('is-measuring');
    chars.forEach((c, i) => { c.style.width = `${widths[i].toFixed(4)}em`; });
    boxes = chars.map((c) => ({ x: c.offsetLeft + c.offsetWidth / 2, y: c.offsetTop + c.offsetHeight / 2 }));
    sigma = size * 0.75;
  };

  // One crest eases towards its target; every letter reads a Gaussian of its distance from it
  const crest = { x: 0, y: 0, a: 0 };
  const aim = { x: 0, y: 0, a: 0, vx: 0 };
  let sweep = null, drag = null, frame = 0, last = 0;
  const render = (now) => {
    const dt = Math.min(48, now - (last || now));
    last = now;
    if (sweep) {
      const k = Math.min(1, (now - sweep.start) / 1600);
      crest.x = aim.x = sweep.from + (sweep.to - sweep.from) * (k < 0.5 ? 4 * k ** 3 : 1 - (2 - 2 * k) ** 3 / 2);
      crest.a = aim.a = k < 1 ? 1 : 0;
      if (k === 1) sweep = null;
    } else {
      if (!drag && aim.vx) { // a pushed wave coasts, then slows to a stop
        aim.x += aim.vx * dt;
        aim.vx = Math.abs(aim.vx) < 0.02 ? 0 : aim.vx * Math.exp(-dt / 240);
      }
      const follow = 1 - Math.exp(-dt / 70);
      crest.x += (aim.x - crest.x) * follow;
      crest.y += (aim.y - crest.y) * follow;
      crest.a += (aim.a - crest.a) * (1 - Math.exp(-dt / 180));
    }
    const live = sweep || drag || aim.a || aim.vx || crest.a > 0.003;
    let peak = 0;
    chars.forEach((c, i) => {
      const dx = (boxes[i].x - crest.x) / sigma;
      const dy = sweep ? 0 : (boxes[i].y - crest.y) / (sigma * 0.8);
      const g = live ? crest.a * Math.exp(-(dx * dx + dy * dy) / 2) : 0;
      peak = Math.max(peak, g);
      if (Math.abs(g - gs[i]) < 0.004 && (g || !gs[i])) return;
      gs[i] = g;
      c.style.setProperty('--weight-wave-g', g.toFixed(3));
      c.style.setProperty('--weight-wave-s', `${Math.round(Math.min(100, Math.max(0, 50 - dx * 30)))}%`); // blue behind, teal ahead
    });
    root.style.setProperty('--weight-wave-x', crest.x.toFixed(1));
    root.style.setProperty('--weight-wave-a', live ? crest.a.toFixed(3) : '0');
    const weight = String(Math.round(400 + 400 * peak));
    if (value.textContent !== weight) value.textContent = weight;
    if (live) frame = requestAnimationFrame(render);
    else frame = last = 0;
  };
  const wake = () => { if (!frame) frame = requestAnimationFrame(render); };
  const point = (e) => { const r = title.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; };

  // Mouse: the crest follows the cursor. Touch or pen: drag across the type to push the wave
  stage.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse' && !drag) return;
    const p = point(e);
    if (drag) {
      aim.vx = Math.max(-2, Math.min(2, (p.x - drag.x) / Math.max(8, e.timeStamp - drag.t)));
      drag = { x: p.x, t: e.timeStamp };
    }
    sweep = null;
    Object.assign(aim, { x: p.x, y: p.y, a: 1 });
    wake();
  });
  stage.addEventListener('pointerleave', (e) => { if (e.pointerType === 'mouse') { aim.a = 0; wake(); } });
  title.addEventListener('pointerdown', (e) => {
    if (e.pointerType === 'mouse') return;
    const p = point(e);
    drag = { x: p.x, t: e.timeStamp };
    sweep = null;
    Object.assign(aim, { x: p.x, y: p.y, a: 1, vx: 0 });
    Object.assign(crest, { x: p.x, y: p.y });
    wake();
  });
  const release = () => { if (drag) { drag = null; aim.a = 0; wake(); } };
  title.addEventListener('pointerup', release);
  title.addEventListener('pointercancel', release);

  // Intro: one wave sweeps left to right the first time the heading is in view
  const io = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    io.disconnect();
    if (aim.a || drag) return; // someone is already playing with it
    sweep = { from: -2.5 * sigma, to: title.offsetWidth + 2.5 * sigma, start: performance.now() };
    wake();
  }, { threshold: 0.6 });

  measure();
  let width = stage.clientWidth;
  new ResizeObserver(() => { if (stage.clientWidth !== width) { width = stage.clientWidth; measure(); } }).observe(stage);
  document.fonts?.ready.then(measure);
  io.observe(title);
  value.textContent = '400';
  root.querySelector('.weight-wave__hint').hidden = false;
});
```

## Notes

- Accessibility: the `<h2>` keeps a visually hidden copy of its text, and the letter spans live in one `aria-hidden` layer, so screen readers read "We do the heavy lifting." as words. The hint, readout and baseline glow are decorative; the list keeps its `<ol>` semantics with `role="list"`.
- No jitter: each letter is measured at weight 800 and its box fixed in `em`, centred, so weight changes never move a neighbour and fluid font sizes need no re-measuring. Kerning between letters is traded for that stability. Needs Geist's variable weight axis across 400–800, which the library's standard link (`family=Geist:wght@400..800`) provides; with static weights the browser snaps between them.
- Without JS it's a plain `<h2>` at weight 600. Under reduced motion the script never splits the heading, so it stays a static weight-600 heading with no intro sweep. With JS, `@media (scripting: enabled)` sets the resting weight 400 before the script runs, so nothing jumps on load.
- Touch: the heading uses `touch-action: pan-y pinch-zoom`, so vertical scrolling and zoom keep working while a horizontal drag pushes the wave, which coasts with momentum after release.
- Contrast on white: resting `--text-main` is 14.6:1; at the crest the tint reaches `--primary` (5.2:1) and `--primary-2` (3.7:1), which this display size treats as large text (3:1). Tune the lens with `sigma` (0.75em) and the lift in `.weight-wave__char`.
