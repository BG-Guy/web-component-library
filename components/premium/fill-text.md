# Scroll-Fill Statement

A three-line promise set huge in outlined display type on a deep surface. As each line passes through the reading zone, the brand gradient sweeps into it from left to right (`background-clip: text` with a scroll-driven `background-size`), and the line being filled glows softly while a numbered rail fills alongside it. CSS scroll timelines drive it where supported, with a per-line JS fallback elsewhere. On phones the lines wrap and every wrapped row fills in step, with a slimmer number gutter. Depends on `tokens/variables.css`.

**Motion:** per-line gradient fill (scroll-scrubbed, linear `view()` timeline or rAF fallback) · glow peaking mid-fill · rail growth (`transform: scaleY`) · outline fading once filled · link arrow and press (`--dur-3`, `--ease-spring`).

## HTML

```html
<div class="fill-text-demo">
  <div class="fill-text-demo__intro">
    <p>Three promises, filled in as you read them.</p>
    <span class="fill-text-demo__hint">Scroll</span>
  </div>

  <section class="fill-text" aria-labelledby="fill-text-title" data-fill-text>
    <div class="fill-text__inner">
      <p class="fill-text__eyebrow">The Brand promise</p>
      <h2 id="fill-text-title" class="fill-text__title">
        <span class="fill-text__line"><span class="fill-text__ink">We show up.</span></span>
        <span class="fill-text__line"><span class="fill-text__ink">We fix it right.</span></span>
        <span class="fill-text__line"><span class="fill-text__ink">We clean up after.</span></span>
      </h2>
      <div class="fill-text__foot">
        <p class="fill-text__sign">
          <span class="fill-text__avatar" aria-hidden="true">DR</span>
          <span><strong>Dana Ruiz</strong> Founder · Springfield since 2009</span>
        </p>
        <a class="fill-text__link" href="#guarantee">
          Read our guarantee
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
      </div>
    </div>
  </section>

  <div class="fill-text-demo__outro">
    <p>Scroll back up to empty the lines again.</p>
    <span class="fill-text-demo__hint">End of demo</span>
  </div>
</div>
```

## CSS

```css
/* One number drives everything: 0 = outlined, 1 = filled. It starts at 1, so any fallback is fully filled. */
@property --fill-text-p { syntax: "<number>"; inherits: true; initial-value: 1; }

/* Section: deep surface, light gathering behind the statement */
.fill-text {
  --fill-text-ink: linear-gradient(90deg,
    color-mix(in srgb, var(--primary) 70%, var(--text-inverse)),
    color-mix(in srgb, var(--primary-2) 72%, var(--text-inverse)) 80%, transparent);
  --fill-text-glow: color-mix(in srgb, var(--primary) 60%, var(--primary-2));
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(55% 45% at 12% 35%, color-mix(in srgb, var(--primary) 20%, transparent), transparent 70%),
    radial-gradient(45% 40% at 92% 85%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.fill-text__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4.5rem, 10vw, 8rem) var(--gutter); }
.fill-text a:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.fill-text__eyebrow { display: inline-flex; align-items: center; gap: 0.75rem; margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }
.fill-text__eyebrow::before { content: ""; width: 2rem; height: 1px; background: var(--gradient-brand); }

/* Statement: a numbered gutter with a hairline rail, then three lines */
.fill-text__title {
  --fill-text-size: clamp(2.125rem, 0.9rem + 6.4vw, 7.5rem);
  --fill-text-gutter: 2rem;
  counter-reset: fill-text;
  margin: clamp(1.5rem, 4vw, 2.5rem) 0 0; padding-left: var(--fill-text-gutter);
  font: 700 var(--fill-text-size)/1.04 var(--font-display); letter-spacing: var(--tracking-display);
  background: linear-gradient(var(--border-inverse), var(--border-inverse)) calc(var(--fill-text-gutter) - 0.75rem) 0 / 1px 100% no-repeat;
}
.fill-text__line {
  --fill-text-g: calc(4 * var(--fill-text-p, 1) * (1 - var(--fill-text-p, 1))); /* glow: 0 at rest, peaks mid-fill */
  position: relative; display: block; counter-increment: fill-text;
  filter: drop-shadow(0 0 0.12em color-mix(in srgb, var(--fill-text-glow) calc(var(--fill-text-g) * 70%), transparent));
}
.fill-text__line + .fill-text__line { margin-top: 0.06em; }
.fill-text__line::before {
  content: "0" counter(fill-text);
  content: "0" counter(fill-text) / "";
  position: absolute; left: calc(var(--fill-text-gutter) * -1); top: calc(var(--fill-text-size) * 0.24);
  color: color-mix(in srgb, var(--primary-2) calc(var(--fill-text-p, 1) * 60%), color-mix(in srgb, var(--text-inverse) 55%, var(--surface-deep)));
  font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em;
}
.fill-text__line::after {
  content: ""; position: absolute; top: 0; bottom: 0; left: -0.75rem; width: 1px;
  background: var(--gradient-brand); box-shadow: 0 0 10px color-mix(in srgb, var(--fill-text-glow) 70%, transparent);
  transform: scaleY(var(--fill-text-p, 1)); transform-origin: top;
}

/* The ink: outlined glyphs, gradient swept in by background-size; wrapped rows fill in step */
.fill-text__ink {
  color: transparent;
  -webkit-text-stroke: max(1px, 0.016em) color-mix(in srgb, var(--text-inverse) clamp(16%, (1 - var(--fill-text-p, 1)) * 500%, 50%), transparent);
  background: var(--fill-text-ink) 0 0 / calc(var(--fill-text-p, 1) * 125%) 100% no-repeat;
  -webkit-background-clip: text; background-clip: text;
  -webkit-box-decoration-break: clone; box-decoration-break: clone;
}

/* Sign-off */
.fill-text__foot {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1.25rem 2rem;
  margin-top: clamp(2.5rem, 6vw, 4rem); padding-top: 1.5rem; border-top: 1px solid var(--border-inverse);
}
.fill-text__sign { display: flex; align-items: center; gap: 0.75rem; margin: 0; color: var(--text-inverse-muted); font-size: 0.9375rem; line-height: 1.4; }
.fill-text__sign strong { display: block; color: var(--text-inverse); font-weight: 600; }
.fill-text__avatar {
  flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  color: var(--text-inverse); font-size: 0.8125rem; font-weight: 700;
  box-shadow: var(--highlight-inverse), 0 0 0 3px color-mix(in srgb, var(--primary) 25%, transparent);
}
.fill-text__link {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.25rem; border-radius: 999px;
  background: var(--glass-inverse); color: var(--text-inverse); font-weight: 600; text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.fill-text__link:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.fill-text__link:active { transform: scale(0.97); }
.fill-text__link svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.fill-text__link:hover svg { translate: 3px 0; }

/* Demo scroll room */
.fill-text-demo__intro, .fill-text-demo__outro {
  display: grid; place-content: center; justify-items: center; gap: 0.75rem; min-height: 70vh; min-height: 70svh;
  padding: 3rem var(--gutter); background: var(--surface-deep); color: var(--text-inverse-muted); font-family: var(--font-sans); text-align: center;
}
.fill-text-demo__intro { border-bottom: 1px solid var(--border-inverse); }
.fill-text-demo__outro { border-top: 1px solid var(--border-inverse); }
.fill-text-demo__intro p, .fill-text-demo__outro p { max-width: 24rem; margin: 0; color: var(--text-inverse); font: 600 clamp(1.25rem, 1rem + 1vw, 1.75rem)/1.2 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.fill-text-demo__hint { font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }

@media (min-width: 768px) {
  .fill-text__title { --fill-text-gutter: 4.5rem; }
}

/* Scroll-driven fill: each line fills while it moves from about 70% to 45% of the viewport height.
   Only with JS and motion allowed; otherwise --fill-text-p stays 1 (filled). */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  @supports (animation-timeline: view()) {
    .fill-text__line { animation: fill-text-fill linear both; animation-timeline: view(); animation-range: cover 30% cover 55%; }
  }
  @supports not (animation-timeline: view()) {
    .fill-text__line { --fill-text-p: 0; } /* the JS fallback writes the real value per line */
  }
}
@keyframes fill-text-fill { from { --fill-text-p: 0; } to { --fill-text-p: 1; } }
```

## JS

```js
// Fallback for browsers without CSS scroll timelines: same mapping as `animation-range: cover 30% cover 55%`
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const native = CSS.supports('animation-timeline: view()');

document.querySelectorAll('[data-fill-text]').forEach((root) => {
  if (native || reduce.matches) return; // CSS handles it, or the statement stays filled
  const lines = [...root.querySelectorAll('.fill-text__line')];
  let frame = 0;

  // Read every line first, then write, so one frame never forces layout twice
  const update = () => {
    frame = 0;
    const values = lines.map((line) => {
      const r = line.getBoundingClientRect();
      const cover = (innerHeight - r.top) / (innerHeight + r.height);
      return Math.min(1, Math.max(0, (cover - 0.3) / 0.25));
    });
    lines.forEach((line, i) => line.style.setProperty('--fill-text-p', values[i].toFixed(4)));
  };
  const queue = () => { if (!frame) frame = requestAnimationFrame(update); };

  // Listen only while the statement is near the viewport
  new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      update();
      addEventListener('scroll', queue, { passive: true });
      addEventListener('resize', queue, { passive: true });
    } else {
      removeEventListener('scroll', queue);
      removeEventListener('resize', queue);
    }
  }, { rootMargin: '10% 0px' }).observe(root);
});
```

## Notes

- Accessibility: the statement is one real `<h2>` with plain text in each line, so screen readers read it normally. The gutter numbers use `content: … / ""` so they aren't announced. Nothing is split or hidden, and `color: transparent` gives way to system colours in forced-colours mode.
- Contrast on `--surface-deep`: the unfilled outline is `--text-inverse` at 50%, which is 5.1:1, comfortably above the 3:1 needed to read as large text. The fill gradient runs from 6.4:1 (light blue) to 7.6:1 (light teal), and gutter numbers stay at 5:1 or better. Once a line is filled, its outline fades to a faint 16% rim.
- Without JS, or under reduced motion, every line is fully filled (`--fill-text-p` is registered with an initial value of 1). With JS, browsers that have `animation-timeline: view()` run the fill in CSS; others start outlined (via `@media (scripting: enabled)`) and a passive, rAF-throttled, IntersectionObserver-gated listener writes each line's progress. Since outlined text stays readable, a failed script never hides content.
- The fill completes as a line reaches about the middle of the viewport, so it needs roughly half a viewport of page after it; the demo's outro block provides that room.
- Adapt: change the words freely, since lines are plain spans. Retheme with `--fill-text-ink` (keep the transparent tail; it makes the soft leading edge) and `--fill-text-glow`, and move the reading zone by editing `animation-range` together with the `0.3`/`0.25` in the fallback.
