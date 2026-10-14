# Curtain Split

A pinned section hidden behind two brand-gradient doors. One artwork (a line-drawn room of nested arches and floorboards, plus the headline "Ready for something new?") runs across the seam, so each door carries its half. As you scroll, the doors slide apart like sliding doors, leaning slightly as they move and casting soft edge shadows onto a light stage underneath, where a finished-room photo and three stats scale up from 0.92 and come into focus. On phones the run is shorter and the stage stacks into one column. Depends on `tokens/variables.css`.

**Motion:** door slide (scroll scrub, smoothstep) with a parabolic lean (`skewY`) · edge shadows fading in · photo, copy and stats scale 0.92 → 1 and un-blur, staggered · link arrow nudge on hover (`--ease-spring`).

## HTML

```html
<div class="curtain-split-demo">
  <div class="curtain-split-demo__intro">
    <p class="curtain-split-demo__kicker">Remodels</p>
    <p class="curtain-split-demo__line">Something's behind the doors.</p>
    <span class="curtain-split-demo__hint" aria-hidden="true">Scroll
      <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
    </span>
  </div>

  <section class="curtain-split" aria-labelledby="curtain-split-title" data-curtain-split>
    <div class="curtain-split__stage">
      <div class="curtain-split__cover">
        <div class="curtain-split__door curtain-split__door--left">
          <div class="curtain-split__panel">
            <div class="curtain-split__art">
              <svg class="curtain-split__lines" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">
                <path d="M490 800V470A110 110 0 0 1 710 470V800M410 800V420A190 190 0 0 1 790 420V800M330 800V370A270 270 0 0 1 870 370V800M250 800V320A350 350 0 0 1 950 320V800M170 800V270A430 430 0 0 1 1030 270V800M90 800V220A510 510 0 0 1 1110 220V800" />
                <path class="curtain-split__floor" d="M-200 640H1400M85.7 640L-600 800M235.7 640L-250 800M385.7 640L100 800M514.3 640L400 800M685.7 640L800 800M814.3 640L1100 800M964.3 640L1450 800M1114.3 640L1800 800" />
              </svg>
              <div class="curtain-split__headline">
                <p class="curtain-split__kicker">Remodels · Springfield</p>
                <h2 id="curtain-split-title" class="curtain-split__title">Ready for something new?</h2>
                <p class="curtain-split__sub">Kitchens, baths and whole floors, designed and built by one team.</p>
              </div>
              <p class="curtain-split__hint" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M9 12H3m0 0 3-3m-3 3 3 3M15 12h6m0 0-3-3m3 3-3 3" /></svg>
                Scroll to open
              </p>
            </div>
          </div>
        </div>
        <!-- Right door: the same artwork, offset to show its half. A visual duplicate, hidden from assistive tech. -->
        <div class="curtain-split__door curtain-split__door--right" aria-hidden="true">
          <div class="curtain-split__panel">
            <div class="curtain-split__art">
              <svg class="curtain-split__lines" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice" focusable="false">
                <path d="M490 800V470A110 110 0 0 1 710 470V800M410 800V420A190 190 0 0 1 790 420V800M330 800V370A270 270 0 0 1 870 370V800M250 800V320A350 350 0 0 1 950 320V800M170 800V270A430 430 0 0 1 1030 270V800M90 800V220A510 510 0 0 1 1110 220V800" />
                <path class="curtain-split__floor" d="M-200 640H1400M85.7 640L-600 800M235.7 640L-250 800M385.7 640L100 800M514.3 640L400 800M685.7 640L800 800M814.3 640L1100 800M964.3 640L1450 800M1114.3 640L1800 800" />
              </svg>
              <div class="curtain-split__headline">
                <p class="curtain-split__kicker">Remodels · Springfield</p>
                <p class="curtain-split__title">Ready for something new?</p>
                <p class="curtain-split__sub">Kitchens, baths and whole floors, designed and built by one team.</p>
              </div>
              <p class="curtain-split__hint">
                <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M9 12H3m0 0 3-3m-3 3 3 3M15 12h6m0 0-3-3m3 3-3 3" /></svg>
                Scroll to open
              </p>
            </div>
          </div>
        </div>
      </div>

      <div class="curtain-split__content">
        <div class="curtain-split__inner">
          <div class="curtain-split__info curtain-split__reveal" style="--curtain-split-i: 1">
            <p class="curtain-split__eyebrow">Recent project · Westlake</p>
            <h3 class="curtain-split__heading">A dated galley, opened up in six weeks</h3>
            <p class="curtain-split__copy">We took out a wall, moved the sink to a new island and finished on budget, with the same crew from demolition to final clean.</p>
            <a class="curtain-split__link" href="#project">
              See the full project
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </div>
          <figure class="curtain-split__media curtain-split__reveal" style="--curtain-split-i: 0">
            <img class="curtain-split__photo" src="finished-kitchen.jpg" width="1600" height="1100" alt="Finished open-plan kitchen with a white island, oak floors and three pendant lights" loading="lazy" decoding="async">
            <figcaption class="curtain-split__caption">Westlake kitchen · finished May 2026</figcaption>
          </figure>
          <dl class="curtain-split__stats">
            <div class="curtain-split__stat curtain-split__reveal" style="--curtain-split-i: 2"><dt>Remodels this year</dt><dd>48</dd></div>
            <div class="curtain-split__stat curtain-split__reveal" style="--curtain-split-i: 3"><dt>Average build</dt><dd>6 wks</dd></div>
            <div class="curtain-split__stat curtain-split__reveal" style="--curtain-split-i: 4"><dt>Homeowner rating</dt><dd>4.9</dd></div>
          </dl>
        </div>
      </div>
    </div>
  </section>

  <div class="curtain-split-demo__outro">
    <p class="curtain-split-demo__kicker">Free design visit</p>
    <p class="curtain-split-demo__line">Tell us about the room. We'll draw the rest.</p>
  </div>
</div>
```

## CSS

```css
@property --curtain-split-p { syntax: "<number>"; inherits: true; initial-value: 0; }

/* Base layout (no JS, reduced motion, older engines): the cover is a header band above the content */
.curtain-split {
  --curtain-split-run: 200vh;
  --curtain-split-cover: linear-gradient(135deg, color-mix(in srgb, var(--primary) 88%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 78%, var(--surface-deep)));
  --curtain-split-t: clamp(0, (var(--curtain-split-p, 0) - 0.06) / 0.66, 1);
  --curtain-split-o: calc(var(--curtain-split-t) * var(--curtain-split-t) * (3 - 2 * var(--curtain-split-t)));
  --curtain-split-lean: calc(4 * var(--curtain-split-o) * (1 - var(--curtain-split-o)) * 2.5deg);
  position: relative; background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
}
.curtain-split__stage, .curtain-split__cover, .curtain-split__panel { position: relative; }
.curtain-split__panel { overflow: hidden; }
.curtain-split__door--right { display: none; }

/* Cover artwork: one composition, so it lines up across both doors */
.curtain-split__art {
  box-sizing: border-box; position: relative; left: 0; display: grid; place-items: center;
  min-height: clamp(20rem, 50vh, 30rem); padding: clamp(3rem, 8vw, 5rem) var(--gutter); text-align: center;
  background:
    radial-gradient(42% 52% at 50% 46%, color-mix(in srgb, var(--primary-2) 30%, transparent), transparent 70%),
    radial-gradient(120% 90% at 50% 50%, transparent 55%, color-mix(in srgb, var(--surface-deep) 35%, transparent)),
    var(--curtain-split-cover);
  color: var(--text-inverse);
}
.curtain-split__lines { position: absolute; inset: 0; width: 100%; height: 100%; fill: none; stroke: color-mix(in srgb, var(--text-inverse) 16%, transparent); stroke-width: 1.25; }
.curtain-split__lines path { vector-effect: non-scaling-stroke; }
.curtain-split__lines .curtain-split__floor { stroke: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.curtain-split__headline { position: relative; max-width: 60rem; }
.curtain-split__kicker { margin: 0; font: 500 0.75rem var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; }
.curtain-split__title {
  max-width: 11ch; margin: 1rem auto 0; font: 600 clamp(2.75rem, 1.4rem + 6.4vw, 7.5rem)/0.95 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.curtain-split__sub { max-width: 30rem; margin: 1.25rem auto 0; font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.55; }
.curtain-split__hint { display: none; }

/* Content stage: photo, project copy and three stats */
.curtain-split__content { background: radial-gradient(70% 60% at 100% 0%, color-mix(in srgb, var(--primary) 6%, transparent), transparent 70%), var(--surface-light); }
.curtain-split__inner {
  box-sizing: border-box; display: grid; grid-template-areas: "info" "media" "stats"; gap: 1.25rem;
  width: 100%; max-width: var(--container-max); margin-inline: auto; padding: clamp(2.5rem, 6vw, 4rem) var(--gutter);
}
.curtain-split__info { grid-area: info; }
.curtain-split__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.curtain-split__heading { margin: 0.5rem 0 0; font: 600 clamp(1.5rem, 1.1rem + 1.8vw, 2.5rem)/1.08 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.curtain-split__copy { max-width: 32rem; margin: 0.75rem 0 0; color: var(--text-muted); line-height: 1.6; }
.curtain-split__link { display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; margin-top: 0.25rem; color: var(--primary); font-weight: 600; text-decoration: none; text-underline-offset: 0.3em; }
.curtain-split__link svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.curtain-split__link:hover { text-decoration: underline; }
.curtain-split__link:hover svg { translate: 3px 0; }
.curtain-split__link:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; border-radius: var(--radius-sm); }
.curtain-split__media { grid-area: media; position: relative; margin: 0; overflow: hidden; aspect-ratio: 4 / 3; border-radius: var(--radius-2xl); box-shadow: var(--shadow-xl); }
.curtain-split__photo {
  display: block; width: 100%; height: 100%; object-fit: cover;
  background: linear-gradient(135deg, color-mix(in srgb, var(--accent) 22%, var(--surface-light)), color-mix(in srgb, var(--primary) 16%, var(--surface-muted)));
}
.curtain-split__caption {
  position: absolute; left: 0.75rem; bottom: 0.75rem; padding: 0.375rem 0.75rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-light) 88%, transparent); box-shadow: var(--highlight), var(--shadow-md);
  color: var(--text-main); font: 500 0.75rem var(--font-mono); backdrop-filter: blur(var(--blur-md));
}
.curtain-split__stats { grid-area: stats; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.75rem; margin: 0; }
.curtain-split__stat { padding: 0.875rem 1rem; border-radius: var(--radius-xl); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight); }
.curtain-split__stat dt { color: var(--text-muted); font: 500 0.6875rem/1.3 var(--font-mono); letter-spacing: 0.04em; }
.curtain-split__stat dd { margin: 0.375rem 0 0; font: 600 clamp(1.375rem, 1.1rem + 1.2vw, 2rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }

@media (min-width: 768px) {
  .curtain-split { --curtain-split-run: 260vh; }
  .curtain-split__inner {
    grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); grid-template-areas: "media info" "media stats";
    column-gap: clamp(2rem, 4vw, 3.5rem); row-gap: 1.5rem; align-items: end;
  }
  .curtain-split__media { aspect-ratio: auto; min-height: 22rem; }
  .curtain-split__stats { align-self: start; }
}

/* The curtain: only with scripting on and motion allowed */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .curtain-split { height: var(--curtain-split-run); }
  .curtain-split:not(.is-live) { animation: curtain-split-failsafe 1.4s var(--ease-in-out) 2.5s both; }
  .curtain-split__stage { position: sticky; top: 0; height: 100vh; height: 100svh; overflow: hidden; }
  .curtain-split__content { position: absolute; inset: 0; display: grid; align-content: center; }
  .curtain-split__copy { display: none; }
  .curtain-split__cover { position: absolute; inset: 0; z-index: 2; pointer-events: none; }
  .curtain-split__door { position: absolute; top: -6%; bottom: -6%; width: 50%; pointer-events: auto; will-change: transform; }
  .curtain-split__door--left { left: 0; transform-origin: 0 50%; transform: translateX(calc(var(--curtain-split-o) * -104%)) skewY(calc(var(--curtain-split-lean) * -1)); }
  .curtain-split__door--right { display: block; right: 0; transform-origin: 100% 50%; transform: translateX(calc(var(--curtain-split-o) * 104%)) skewY(var(--curtain-split-lean)); }
  .curtain-split__panel { position: absolute; inset: 0; }
  .curtain-split__art { position: absolute; top: calc(100% * 6 / 112); width: 200%; height: calc(100% * 100 / 112); min-height: 0; }
  .curtain-split__door--right .curtain-split__art { left: -100%; }
  .curtain-split__hint {
    position: absolute; left: 50%; bottom: clamp(1.25rem, 5vh, 2.5rem); translate: -50% 0;
    display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.5rem 0.875rem; border-radius: var(--radius-full);
    background: color-mix(in srgb, var(--surface-deep) 25%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
    font: 500 0.75rem var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase;
  }
  .curtain-split__hint svg { fill: none; stroke: var(--accent); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

  /* Door edges: a lit seam line, and a shadow cast on the stage as the doors part */
  .curtain-split__door::before {
    content: ""; position: absolute; top: 0; bottom: 0; z-index: 1; width: 2px;
    background: linear-gradient(transparent, color-mix(in srgb, var(--text-inverse) 45%, transparent) 30% 70%, transparent);
  }
  .curtain-split__door--left::before { right: 0; }
  .curtain-split__door--right::before { left: 0; }
  .curtain-split__door::after { content: ""; position: absolute; top: 0; bottom: 0; width: clamp(2.5rem, 7vw, 6rem); opacity: min(1, var(--curtain-split-o) * 6); }
  .curtain-split__door--left::after { left: 100%; background: linear-gradient(to right, color-mix(in srgb, var(--surface-deep) 34%, transparent), transparent); }
  .curtain-split__door--right::after { right: 100%; background: linear-gradient(to left, color-mix(in srgb, var(--surface-deep) 34%, transparent), transparent); }

  /* Reveal: scale up from 0.92 and come into focus, staggered by --curtain-split-i */
  .curtain-split__reveal {
    --curtain-split-r: clamp(0, var(--curtain-split-o) * 1.3 - var(--curtain-split-i, 0) * 0.08, 1);
    scale: calc(0.92 + 0.08 * var(--curtain-split-r));
    filter: blur(calc((1 - var(--curtain-split-r)) * 12px));
    will-change: scale, filter;
  }
  @media (min-width: 768px) {
    .curtain-split__media { min-height: min(60vh, 34rem); }
  }
  @media (min-height: 740px), (min-width: 1024px) {
    .curtain-split__copy { display: block; }
  }
}
@keyframes curtain-split-failsafe { from { --curtain-split-p: 0; } to { --curtain-split-p: 0.8; } }

/* Demo scroll room */
.curtain-split-demo__intro, .curtain-split-demo__outro {
  display: grid; place-content: center; justify-items: center; gap: 0.75rem; min-height: 70vh; padding: 3rem var(--gutter);
  font-family: var(--font-sans); text-align: center;
}
.curtain-split-demo__intro { background: var(--surface-muted); color: var(--text-main); }
.curtain-split-demo__outro { background: var(--surface-deep); color: var(--text-inverse); }
.curtain-split-demo__kicker { margin: 0; font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.curtain-split-demo__line { max-width: 22ch; margin: 0; font: 600 clamp(1.5rem, 1.1rem + 2vw, 2.5rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.curtain-split-demo__hint { display: inline-flex; align-items: center; gap: 0.375rem; margin-top: 1rem; color: var(--text-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.curtain-split-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: curtain-split-nudge 1.6s var(--ease-in-out) 3; }
@keyframes curtain-split-nudge { 50% { translate: 0 4px; } }
@media (prefers-reduced-motion: reduce) {
  .curtain-split-demo *, .curtain-split-demo *::before, .curtain-split-demo *::after { animation: none !important; }
}
```

## JS

```js
const clamp01 = (n) => Math.min(1, Math.max(0, n));
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? clamp01(-r.top / range) : 0; };
// Same condition as the CSS gate: the curtain only exists with scripting on and motion allowed
const live = matchMedia('(scripting: enabled) and (prefers-reduced-motion: no-preference)');

document.querySelectorAll('[data-curtain-split]').forEach((root) => {
  const content = root.querySelector('.curtain-split__content');
  let near = false;
  let frame = 0;

  const render = () => {
    frame = 0;
    if (live.matches) root.style.setProperty('--curtain-split-p', progress(root).toFixed(4));
    else root.style.removeProperty('--curtain-split-p');
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(render); };

  // Keyboard focus landing behind closed doors scrolls the run on until they're open, so focus is never hidden
  content.addEventListener('focusin', () => {
    if (!live.matches || progress(root) > 0.75) return;
    const run = root.offsetHeight - innerHeight;
    scrollTo({ top: root.getBoundingClientRect().top + scrollY + run * 0.8, behavior: 'smooth' });
  });

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; queue(); }, { rootMargin: '25% 0px' }).observe(root);
  addEventListener('scroll', queue, { passive: true });
  addEventListener('resize', queue, { passive: true });
  live.addEventListener('change', render);
  render();
  root.classList.add('is-live'); // takes over from the CSS failsafe
});
```

## Notes

- There is one real `<h2>`, in the left door. The right door is a visual duplicate marked `aria-hidden`. The project heading, captioned photo, `<dl>` stats and link stay in the accessibility tree in reading order. If keyboard focus lands on the link while the doors are shut, the page scrolls the run forward until they're open, so focus is never hidden behind the cover.
- The curtain layout only exists under `@media (scripting: enabled) and (prefers-reduced-motion: no-preference)`. Without JS, with reduced motion, or in engines without that media feature, the cover renders as a normal brand header band above the content, with no long scroll. If the script fails, a CSS failsafe opens the doors after 2.5s.
- Contrast: the cover gradient is `--primary`/`--primary-2` mixed with 12%/22% `--surface-deep`, so `--text-inverse` is 5.2–5.9:1, and 5.0:1 on the centre glow, so the sub-line passes as body text. Content uses `--text-main` (14.6:1), `--text-muted` (4.8:1) and `--primary` links (5.2:1). The caption chip is `--text-main` on 88% white glass.
- The doors move with `transform` only (composited). The reveal animates `scale` and `filter: blur()` on four elements while the doors open, then holds at identity. Doors are 12% taller than the stage, so the lean never opens a gap.
- To adapt it, swap the photo (keep `width`/`height`), redraw the line art in `.curtain-split__lines`, or recolour `--curtain-split-cover`. The run is `--curtain-split-run` (200vh on phones, 260vh from 768px), and the door timing is the `--curtain-split-t` range.
