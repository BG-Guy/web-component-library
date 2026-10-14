# Wipe Gallery

Scrollytelling for four project transformations. A pinned, full-height frame stacks four photos, and scroll wipes each one in with its own shape: a diagonal slash, a circle opening from a corner, vertical blinds and a centre split. Each incoming photo settles from a slight zoom while the outgoing one dims. A smoked-glass panel on the left holds the heading and swaps the active project's title and stats with a masked rise, and a vertical 01–04 index fills as you go. Below 768px the figures stack and each reveals once with its own shape. Depends on `tokens/variables.css`.

**Motion:** four clip/mask wipes, photo settle (1.12 → 1) and outgoing dim, all scrubbed by scroll · caption mask rise (`--dur-4`, `--ease-out`, `--stagger`) · index fill (scrubbed) and number colour (`--dur-3`) · mobile one-time reveal (`--dur-5`, `--ease-out`, via `@property`).

## HTML

```html
<div class="wipe-gallery-demo">
  <div class="wipe-gallery-demo__note">
    <p>Four homes, each one wiped in its own way.</p>
    <span class="wipe-gallery-demo__hint">Scroll <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg></span>
  </div>

  <section class="wipe-gallery" aria-labelledby="wipe-gallery-title" data-wipe-gallery>
    <div class="wipe-gallery__stage">
      <div class="wipe-gallery__panel">
        <p class="wipe-gallery__eyebrow">Transformations</p>
        <h2 id="wipe-gallery-title" class="wipe-gallery__title">Four homes, transformed.</h2>
        <p class="wipe-gallery__lead">Recent projects across Springfield, from first sketch to final walkthrough.</p>
        <div class="wipe-gallery__swap" aria-hidden="true" hidden></div>
      </div>

      <div class="wipe-gallery__frame">
        <figure class="wipe-gallery__figure wipe-gallery__figure--slash">
          <div class="wipe-gallery__media"><img class="wipe-gallery__img" src="alder-kitchen.jpg" width="1600" height="1000" alt="Open kitchen with a long oak island where two walls used to stand" loading="lazy" decoding="async"></div>
          <figcaption class="wipe-gallery__caption">
            <span class="wipe-gallery__chip">Kitchen · Northside</span>
            <strong class="wipe-gallery__name">The Alder Street kitchen</strong>
            <ul class="wipe-gallery__stats" role="list"><li><b>6</b> weeks</li><li><b>2</b> walls removed</li><li><b>0</b> days over</li></ul>
          </figcaption>
        </figure>
        <figure class="wipe-gallery__figure wipe-gallery__figure--circle">
          <div class="wipe-gallery__media"><img class="wipe-gallery__img" src="westlake-spa-bath.jpg" width="1600" height="1000" alt="Bathroom with a freestanding tub lit by a new skylight" loading="lazy" decoding="async"></div>
          <figcaption class="wipe-gallery__caption">
            <span class="wipe-gallery__chip">Bathroom · Westlake</span>
            <strong class="wipe-gallery__name">A spa bath under the eaves</strong>
            <ul class="wipe-gallery__stats" role="list"><li><b>4</b> weeks</li><li><b>1</b> skylight added</li><li><b>$0</b> over quote</li></ul>
          </figcaption>
        </figure>
        <figure class="wipe-gallery__figure wipe-gallery__figure--blinds">
          <div class="wipe-gallery__media"><img class="wipe-gallery__img" src="riverside-living-room.jpg" width="1600" height="1000" alt="Farmhouse living room with exposed beams and tall new windows" loading="lazy" decoding="async"></div>
          <figcaption class="wipe-gallery__caption">
            <span class="wipe-gallery__chip">Living room · Riverside</span>
            <strong class="wipe-gallery__name">Riverside farmhouse, opened up</strong>
            <ul class="wipe-gallery__stats" role="list"><li><b>9</b> weeks</li><li><b>3</b> beams exposed</li><li><b>40%</b> more daylight</li></ul>
          </figcaption>
        </figure>
        <figure class="wipe-gallery__figure wipe-gallery__figure--split">
          <div class="wipe-gallery__media"><img class="wipe-gallery__img" src="elm-court-exterior.jpg" width="1600" height="1000" alt="Craftsman house with new cedar siding, a deep porch and a standing-seam roof" loading="lazy" decoding="async"></div>
          <figcaption class="wipe-gallery__caption">
            <span class="wipe-gallery__chip">Exterior · Springfield</span>
            <strong class="wipe-gallery__name">Elm Court, new from the curb</strong>
            <ul class="wipe-gallery__stats" role="list"><li><b>3</b> weeks</li><li><b>1,900</b> sq ft of siding</li><li><b>0</b> callbacks</li></ul>
          </figcaption>
        </figure>
      </div>

      <div class="wipe-gallery__index" aria-hidden="true" hidden>
        <span class="wipe-gallery__rail"><span class="wipe-gallery__fill"></span></span>
        <ol class="wipe-gallery__nums" role="list"></ol>
      </div>
    </div>
  </section>

  <div class="wipe-gallery-demo__note">
    <p>The frame releases after the last project.</p>
  </div>
</div>
```

## CSS

```css
/* One number per figure drives every shape; registering it lets the mobile reveal transition it */
@property --wipe-gallery-w { syntax: "<number>"; inherits: true; initial-value: 1; }

/* Section: deep surface */
.wipe-gallery { position: relative; isolation: isolate; overflow-x: clip; background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans); }
.wipe-gallery :where(h2, p, ul, ol, figure) { margin: 0; }
.wipe-gallery__stage { position: relative; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }

/* Panel: the real heading; the caption swap inside it is a decorative duplicate (pinned only) */
.wipe-gallery__panel { max-width: 40rem; margin-bottom: clamp(2.5rem, 6vw, 4rem); }
.wipe-gallery__eyebrow { display: flex; align-items: center; gap: 0.75rem; color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.wipe-gallery__eyebrow::before { content: ""; width: 0.5rem; height: 0.5rem; border-radius: 2px; rotate: 45deg; background: var(--gradient-brand); }
.wipe-gallery__title { margin-top: 0.875rem; font: 600 clamp(2rem, 1.2rem + 3vw, 3.5rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.wipe-gallery__lead { margin-top: 0.875rem; max-width: 30rem; color: var(--text-inverse-muted); line-height: 1.6; }
.wipe-gallery__swap { display: none; }
.wipe-gallery .wipe-gallery__swap[hidden], .wipe-gallery .wipe-gallery__index[hidden] { display: none; }

/* Figures: a stacked column until JS pins them */
.wipe-gallery__frame { display: grid; gap: clamp(2.5rem, 6vw, 4rem); }
.wipe-gallery__figure { display: grid; gap: 1.125rem; }
.wipe-gallery__media {
  position: relative; isolation: isolate; overflow: hidden; aspect-ratio: 4 / 3; border-radius: var(--radius-2xl);
  background:
    radial-gradient(70% 60% at 80% 10%, color-mix(in srgb, var(--primary-2) 40%, transparent), transparent 70%),
    linear-gradient(150deg, color-mix(in srgb, var(--primary) 40%, var(--surface-deep)), var(--surface-dark));
}
.wipe-gallery__img { display: block; width: 100%; height: 100%; object-fit: cover; }
.wipe-gallery__media::before { /* hairline and sheen */
  content: ""; position: absolute; inset: 0; z-index: 2; border-radius: inherit; pointer-events: none;
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.wipe-gallery__media::after { /* outgoing dim (pinned) */
  content: ""; position: absolute; inset: 0; z-index: 1; pointer-events: none; background: var(--surface-deep); opacity: 0;
}
.wipe-gallery__caption { display: grid; justify-items: start; gap: 0.625rem; }
.wipe-gallery__chip {
  display: inline-flex; padding: 0.4375rem 0.75rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.wipe-gallery__name { display: block; font: 600 clamp(1.375rem, 1.1rem + 1vw, 2rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.wipe-gallery__stats { display: flex; flex-wrap: wrap; gap: 0.5rem 1.75rem; padding: 0; list-style: none; color: var(--text-inverse-muted); font-size: 0.875rem; }
.wipe-gallery__stats b { display: block; margin-bottom: 0.125rem; color: var(--text-inverse); font: 600 1.25rem/1.1 var(--font-mono); letter-spacing: -0.02em; }
.wipe-gallery__index { display: none; }

/* Shapes, all driven by --wipe-gallery-w (0 → 1) */
:is(.wipe-gallery--pinned, .wipe-gallery--reveal) .wipe-gallery__figure--slash .wipe-gallery__media {
  clip-path: polygon(0 0, calc(var(--wipe-gallery-w, 1) * 130%) 0, calc(var(--wipe-gallery-w, 1) * 130% - 30%) 100%, 0 100%);
}
:is(.wipe-gallery--pinned, .wipe-gallery--reveal) .wipe-gallery__figure--circle .wipe-gallery__media {
  clip-path: circle(calc(var(--wipe-gallery-w, 1) * 150%) at 100% 100%);
}
:is(.wipe-gallery--pinned, .wipe-gallery--reveal) .wipe-gallery__figure--blinds .wipe-gallery__media {
  --wipe-gallery-h: calc((1 - var(--wipe-gallery-w, 1)) * 6.3%); /* each of 8 blinds opens from its centre */
  --wipe-gallery-full: clamp(0, (var(--wipe-gallery-w, 1) - 0.97) * 40, 1); /* seals the seams at the end */
  -webkit-mask-image:
    repeating-linear-gradient(90deg, transparent 0 var(--wipe-gallery-h), black var(--wipe-gallery-h) calc(12.5% - var(--wipe-gallery-h)), transparent calc(12.5% - var(--wipe-gallery-h)) 12.5%),
    linear-gradient(color-mix(in srgb, black calc(var(--wipe-gallery-full) * 100%), transparent) 0 0);
  mask-image:
    repeating-linear-gradient(90deg, transparent 0 var(--wipe-gallery-h), black var(--wipe-gallery-h) calc(12.5% - var(--wipe-gallery-h)), transparent calc(12.5% - var(--wipe-gallery-h)) 12.5%),
    linear-gradient(color-mix(in srgb, black calc(var(--wipe-gallery-full) * 100%), transparent) 0 0);
}
:is(.wipe-gallery--pinned, .wipe-gallery--reveal) .wipe-gallery__figure--split .wipe-gallery__media {
  clip-path: inset(calc((1 - var(--wipe-gallery-w, 1)) * 10%) calc((1 - var(--wipe-gallery-w, 1)) * 50%));
}

/* Below 768px with motion allowed: each figure reveals once with its shape */
.wipe-gallery--reveal .wipe-gallery__figure { --wipe-gallery-w: 0; }
.wipe-gallery--reveal .wipe-gallery__figure.is-revealed { --wipe-gallery-w: 1; transition: --wipe-gallery-w calc(var(--dur-5) * 1.2) var(--ease-out); }
.wipe-gallery--reveal .wipe-gallery__img { transform: scale(calc(1.08 - var(--wipe-gallery-w, 1) * 0.08)); }

/* Pinned (JS, 768px+, motion allowed): the k-th of n photos wipes over the first 60% of its segment */
.wipe-gallery--pinned { height: calc(100vh + var(--wipe-gallery-n, 4) * 85vh); height: calc(100svh + var(--wipe-gallery-n, 4) * 85svh); }
.wipe-gallery--pinned .wipe-gallery__stage { position: sticky; top: 0; height: 100vh; height: 100svh; max-width: none; padding: 0; overflow: clip; }
.wipe-gallery--pinned .wipe-gallery__frame {
  position: absolute; inset: clamp(0.5rem, 1.25vw, 1rem); display: block; isolation: isolate; overflow: hidden; border-radius: var(--radius-2xl);
  background:
    repeating-linear-gradient(135deg, var(--border-inverse) 0 1px, transparent 1px 14px),
    radial-gradient(60% 60% at 70% 40%, color-mix(in srgb, var(--primary) 30%, transparent), transparent 70%), var(--surface-dark);
  box-shadow: inset 0 0 0 1px var(--border-inverse);
}
.wipe-gallery--pinned .wipe-gallery__frame::after { /* left scrim under the glass panel */
  content: ""; position: absolute; inset: 0; z-index: 1; pointer-events: none;
  background: linear-gradient(90deg, color-mix(in srgb, var(--surface-deep) 72%, transparent), color-mix(in srgb, var(--surface-deep) 50%, transparent) 34%, transparent 62%);
}
.wipe-gallery--pinned .wipe-gallery__figure {
  --wipe-gallery-w: clamp(0, (var(--wipe-gallery-p, 0) * var(--wipe-gallery-n, 4) - var(--wipe-gallery-k, 0)) / 0.6, 1);
  --wipe-gallery-dim: clamp(0, (var(--wipe-gallery-p, 0) * var(--wipe-gallery-n, 4) - var(--wipe-gallery-k, 0) - 1) / 0.6, 1);
  position: absolute; inset: 0; display: block;
}
.wipe-gallery--pinned .wipe-gallery__media { position: absolute; inset: 0; aspect-ratio: auto; border-radius: 0; }
.wipe-gallery--pinned .wipe-gallery__media::before { display: none; }
.wipe-gallery--pinned .wipe-gallery__media::after { opacity: calc(var(--wipe-gallery-dim) * 0.55); }
.wipe-gallery--pinned .wipe-gallery__img { transform: scale(calc(1.12 - var(--wipe-gallery-w, 1) * 0.12)); will-change: transform; }
.wipe-gallery--pinned .wipe-gallery__caption { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

.wipe-gallery--pinned .wipe-gallery__panel {
  position: absolute; z-index: 2; left: clamp(1.5rem, 4vw, 3.5rem); top: 50%; translate: 0 -50%;
  width: min(25rem, 40vw); max-width: none; margin: 0; padding: clamp(1.25rem, 2.5vw, 2rem); border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-deep) 78%, transparent);
  -webkit-backdrop-filter: blur(var(--blur-md)) saturate(1.4); backdrop-filter: blur(var(--blur-md)) saturate(1.4);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 30px 60px -20px color-mix(in srgb, var(--surface-deep) 70%, transparent);
}
.wipe-gallery--pinned .wipe-gallery__title { font-size: clamp(1.625rem, 1.1rem + 1.6vw, 2.5rem); }
.wipe-gallery--pinned .wipe-gallery__lead { font-size: 0.9375rem; }
.wipe-gallery--pinned .wipe-gallery__swap { display: grid; margin-top: 1.25rem; padding-top: 1.25rem; border-top: 1px solid var(--border-inverse); }

/* Caption swap: every line rises out of its own mask; leaving lines exit upwards */
.wipe-gallery__set { grid-area: 1 / 1; display: grid; justify-items: start; gap: 0.625rem; }
.wipe-gallery__line { display: block; overflow: hidden; padding-block: 0.08em; }
.wipe-gallery__line > * { transform: translate3d(0, 115%, 0); transition: transform var(--dur-4) var(--ease-out); }
.wipe-gallery__set.is-past .wipe-gallery__line > * { transform: translate3d(0, -115%, 0); }
.wipe-gallery__set.is-active .wipe-gallery__line > * { transform: none; transition-delay: calc(var(--wipe-gallery-d, 0) * var(--stagger) + 140ms); }
.wipe-gallery__swap .wipe-gallery__name { font-size: clamp(1.375rem, 1rem + 1.2vw, 2rem); }
.wipe-gallery__swap .wipe-gallery__stats { gap: 0.5rem 1.25rem; font-size: 0.8125rem; }
.wipe-gallery__swap .wipe-gallery__stats b { font-size: 1.125rem; }

/* Vertical index: fills with progress, numbers light up as each project lands */
.wipe-gallery--pinned .wipe-gallery__index {
  position: absolute; z-index: 2; right: clamp(1.25rem, 3vw, 2.5rem); top: 50%; translate: 0 -50%;
  display: grid; grid-template-columns: auto auto; gap: 0.875rem; padding: 1rem 0.875rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 60%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
}
.wipe-gallery__rail { position: relative; width: 2px; border-radius: 2px; background: var(--border-inverse); }
.wipe-gallery__fill { position: absolute; inset: 0; border-radius: inherit; background: linear-gradient(180deg, var(--primary-2), var(--primary)); transform: scaleY(var(--wipe-gallery-p, 0)); transform-origin: top; }
.wipe-gallery__nums { display: grid; gap: 1.75rem; padding: 0; list-style: none; color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); }
.wipe-gallery__num { transition: color var(--dur-3) var(--ease-out); }
.wipe-gallery__num.is-on { color: var(--text-inverse); }

/* Demo scroll room */
.wipe-gallery-demo { background: var(--surface-deep); color: var(--text-inverse-muted); font-family: var(--font-sans); }
.wipe-gallery-demo__note { display: grid; place-content: center; justify-items: center; gap: 1rem; min-height: 70vh; padding: 2rem var(--gutter); text-align: center; }
.wipe-gallery-demo__note p { margin: 0; max-width: 30rem; font-size: 1.0625rem; line-height: 1.6; }
.wipe-gallery-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--text-inverse); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.wipe-gallery-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const wide = matchMedia('(min-width: 768px)');
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? Math.min(1, Math.max(0, -r.top / range)) : 0; };

document.querySelectorAll('[data-wipe-gallery]').forEach((root) => {
  const figures = [...root.querySelectorAll('.wipe-gallery__figure')];
  const swap = root.querySelector('.wipe-gallery__swap');
  const index = root.querySelector('.wipe-gallery__index');
  const nums = index.querySelector('.wipe-gallery__nums');
  const n = figures.length;
  let pinned = false, near = false, frame = 0, current = -1;

  // The glass panel's captions are decorative copies of each figcaption, one masked line per part
  const sets = figures.map((figure, k) => {
    figure.style.setProperty('--wipe-gallery-k', k);
    const set = document.createElement('div');
    set.className = 'wipe-gallery__set';
    figure.querySelectorAll('.wipe-gallery__chip, .wipe-gallery__name, .wipe-gallery__stats').forEach((part, i) => {
      const line = document.createElement('div');
      line.className = 'wipe-gallery__line';
      line.style.setProperty('--wipe-gallery-d', i);
      line.append(part.cloneNode(true));
      set.append(line);
    });
    swap.append(set);
    return set;
  });
  nums.innerHTML = figures.map((_, k) => `<li class="wipe-gallery__num">${String(k + 1).padStart(2, '0')}</li>`).join('');
  const marks = [...nums.children];
  root.style.setProperty('--wipe-gallery-n', n);

  // One scrub value; each figure derives its own wipe in CSS. Captions swap once a wipe is half done.
  const render = () => {
    frame = 0;
    if (!pinned) return;
    const p = progress(root);
    root.style.setProperty('--wipe-gallery-p', p.toFixed(4));
    const active = Math.min(n - 1, Math.max(0, Math.floor(p * n - 0.3)));
    if (active === current) return;
    current = active;
    sets.forEach((set, k) => { set.classList.toggle('is-active', k === active); set.classList.toggle('is-past', k < active); });
    marks.forEach((mark, k) => mark.classList.toggle('is-on', k <= active));
  };
  const queue = () => { if (!frame) frame = requestAnimationFrame(render); };

  // Below 768px with motion allowed: reveal each figure once as it enters (no flash for ones already on screen)
  const reveal = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (entry.isIntersecting) { entry.target.classList.add('is-revealed'); reveal.unobserve(entry.target); }
  }), { threshold: 0.2 });

  const measure = () => {
    pinned = wide.matches && !reduce.matches;
    const revealing = !wide.matches && !reduce.matches;
    if (revealing && !root.classList.contains('wipe-gallery--reveal')) {
      figures.forEach((figure) => {
        const r = figure.getBoundingClientRect();
        if (r.top < innerHeight && r.bottom > 0) figure.classList.add('is-revealed');
        else if (!figure.classList.contains('is-revealed')) reveal.observe(figure);
      });
    }
    root.classList.toggle('wipe-gallery--reveal', revealing);
    root.classList.toggle('wipe-gallery--pinned', pinned);
    swap.hidden = index.hidden = !pinned;
    current = -1;
    render();
  };

  new IntersectionObserver((entries) => { near = entries.at(-1).isIntersecting; if (near) queue(); }, { rootMargin: '25% 0px' }).observe(root);
  addEventListener('scroll', () => { if (near && pinned) queue(); }, { passive: true });
  new ResizeObserver(queue).observe(root);
  wide.addEventListener('change', measure);
  reduce.addEventListener('change', measure);
  measure();
});
```

## Notes

- Accessibility: each project is a `<figure>` (photo with `alt`, plus a figcaption with title and stats), in reading order. While pinned, the figcaptions are visually hidden but still announced. The glass panel's swapping captions and the 01–04 index are decorative duplicates (`aria-hidden`) that JS builds from the figcaptions, so they never drift out of sync. The `<h2>` is real and always visible.
- Fallback below 768px, under reduced motion and without JS: no pin, and the figures stack with visible captions. With JS and motion allowed below 768px, each figure reveals once with its own shape as it enters. Figures already on screen at load are marked revealed before the gate class goes on, so nothing flashes.
- Mechanics: the section is `100svh + n × 85svh` tall with a sticky stage. JS writes `--wipe-gallery-p`, and each figure derives `--wipe-gallery-w` in CSS from its index, wiping over the first 60% of its segment. The shapes are a polygon slash, a `circle()` from the bottom-right corner, a repeating-gradient mask for eight blinds that open from their centres, and an `inset()` centre split. The incoming photo settles from 1.12×, and the outgoing one dims under a 55% deep overlay.
- `@property --wipe-gallery-w` registers the one number that drives every shape, which is what lets the mobile reveal transition it. Browsers without `@property` show the figures instantly. Clip shapes only apply in the pinned and reveal modes.
- Contrast: panel text sits on 78% deep glass over a left scrim (≥ 40% deep under the text). That keeps `--text-inverse` ≥ 13:1 and `--text-inverse-muted` ≥ 5.5:1 even over a pure-white photo. Stacked captions sit on `--surface-deep` (19:1 and 7:1).
