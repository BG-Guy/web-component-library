# Zoom-Through Image

An Apple-style "scroll into the picture" moment on a light page. A centred headline sits above a small rounded photo. As the section pins, the photo's clip opens from an inset card to the full viewport while the image counter-scales for depth and the headline recedes into a blur. Then a glass caption card with two stat chips rises over a soft vignette. Phones get a shorter run and a wider starting card; reduced motion and no-JS get a still figure with the caption beneath it. Depends on `tokens/variables.css`.

**Motion:** clip-path inset and radius opening, image counter-scale 1.25 → 1, headline scale, blur and fade, vignette fade, and caption rise, all scrubbed by scroll with quadratic ease-out phases derived in CSS.

## HTML

```html
<div class="zoom-through-demo">
  <div class="zoom-through-demo__note">
    <p>A featured project you scroll straight into.</p>
    <span class="zoom-through-demo__hint">Scroll <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg></span>
  </div>

  <section class="zoom-through" aria-labelledby="zoom-through-title" data-zoom-through>
    <div class="zoom-through__stage">
      <header class="zoom-through__head">
        <p class="zoom-through__eyebrow">Featured project</p>
        <h2 id="zoom-through-title" class="zoom-through__title">Step inside a home we <span>rebuilt</span>.</h2>
        <p class="zoom-through__lead">Fourteen weeks, one family and every room reworked, from the footings to the light switches.</p>
        <p class="zoom-through__cue" aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>Scroll to step inside</p>
      </header>

      <figure class="zoom-through__media">
        <div class="zoom-through__frame">
          <img class="zoom-through__img" src="westlake-remodel.jpg" width="2400" height="1600" alt="Open-plan kitchen and living room after the Westlake remodel, with oak floors and a wall of steel-framed windows" loading="eager" decoding="async">
          <span class="zoom-through__scrim" aria-hidden="true"></span>
        </div>
        <figcaption class="zoom-through__caption">
          <p class="zoom-through__kicker"><span class="zoom-through__dot" aria-hidden="true"></span>Completed 2026</p>
          <p class="zoom-through__name">Westlake whole-home remodel</p>
          <p class="zoom-through__meta">14 weeks · on budget</p>
          <ul class="zoom-through__stats" role="list">
            <li>
              <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M3 17 17 3l4 4L7 21zM7 13l2 2M10 10l2 2M13 7l2 2" /></svg>
              <span><strong>2,850</strong> sq ft renovated</span>
            </li>
            <li>
              <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 3 5 6v6c0 4.4 3 7.6 7 9 4-1.4 7-4.6 7-9V6zM9 12l2 2 4-4" /></svg>
              <span><strong>0</strong> change orders</span>
            </li>
          </ul>
        </figcaption>
      </figure>
    </div>
  </section>

  <div class="zoom-through-demo__note">
    <p>The photo hands the page back once the caption has landed.</p>
  </div>
</div>
```

## CSS

```css
/* Section: light surface. The start window is tuned with the four --zoom-through-* insets */
.zoom-through {
  --zoom-through-top: 54%;
  --zoom-through-side: var(--gutter);
  --zoom-through-bottom: 8%;
  --zoom-through-radius: var(--radius-xl);
  position: relative; isolation: isolate; overflow-x: clip;
  background: var(--surface-muted); color: var(--text-main); font-family: var(--font-sans);
}
.zoom-through :where(h2, p, ul, figure) { margin: 0; }
.zoom-through__stage { position: relative; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.zoom-through__stage::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background:
    radial-gradient(55% 40% at 50% 0%, color-mix(in srgb, var(--primary) 10%, transparent), transparent 70%),
    radial-gradient(35% 30% at 88% 18%, color-mix(in srgb, var(--primary-2) 9%, transparent), transparent 70%);
}

/* Headline block */
.zoom-through__head { display: grid; justify-items: center; gap: 1rem; max-width: 46rem; margin: 0 auto clamp(2.5rem, 6vw, 4rem); text-align: center; }
.zoom-through__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.4375rem 0.75rem; border-radius: var(--radius-full);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
  color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase;
}
.zoom-through__eyebrow::before { content: ""; width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--gradient-brand); }
.zoom-through__title { font: 600 clamp(2.25rem, 1.2rem + 4vw, 4.5rem)/0.98 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.zoom-through__title span { padding-bottom: 0.06em; background: var(--gradient-brand); -webkit-background-clip: text; background-clip: text; color: transparent; }
.zoom-through__lead { max-width: 32rem; color: var(--text-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; text-wrap: pretty; }
.zoom-through__cue { display: none; }

/* Figure: a rounded photo with the caption card tucked under it */
.zoom-through__media { position: relative; display: grid; }
.zoom-through__frame {
  position: relative; overflow: hidden; aspect-ratio: 4 / 5; border-radius: var(--radius-2xl); box-shadow: var(--shadow-xl);
  background: linear-gradient(150deg, color-mix(in srgb, var(--primary) 30%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 35%, var(--surface-light)));
}
.zoom-through__img { display: block; width: 100%; height: 100%; object-fit: cover; }
.zoom-through__scrim {
  display: none; position: absolute; inset: 0; pointer-events: none;
  background:
    linear-gradient(to top, color-mix(in srgb, var(--surface-deep) 78%, transparent), color-mix(in srgb, var(--surface-deep) 55%, transparent) 40%, transparent 72%),
    radial-gradient(130% 95% at 50% 35%, transparent 50%, color-mix(in srgb, var(--surface-deep) 50%, transparent));
}
.zoom-through__caption {
  position: relative; z-index: 1; display: grid; gap: 0.375rem; margin: -2.5rem var(--space-md) 0; padding: 1.25rem 1.25rem 1.375rem;
  border-radius: var(--radius-xl); background: var(--surface-deep); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), var(--shadow-xl);
}
.zoom-through__kicker { display: flex; align-items: center; gap: 0.5rem; color: var(--text-inverse-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }
.zoom-through__dot { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 28%, transparent); }
.zoom-through__name { margin-top: 0.375rem; font: 600 clamp(1.25rem, 1.1rem + 0.6vw, 1.625rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.zoom-through__meta { color: var(--text-inverse-muted); font-size: 0.9375rem; }
.zoom-through__stats { display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.75rem; padding: 0; list-style: none; }
.zoom-through__stats li {
  display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.375rem 0.875rem 0.375rem 0.375rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse-muted); font-size: 0.8125rem;
}
.zoom-through__stats svg {
  flex: none; box-sizing: content-box; padding: 0.3125rem; border-radius: 50%; background: color-mix(in srgb, var(--primary) 45%, transparent); color: var(--text-inverse);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.zoom-through__stats strong { color: var(--text-inverse); font: 600 0.9375rem var(--font-mono); }

@media (min-width: 768px) {
  .zoom-through { --zoom-through-top: 52%; --zoom-through-side: max(var(--gutter), (100% - 46rem) / 2); --zoom-through-bottom: 9%; --zoom-through-radius: var(--radius-2xl); }
  .zoom-through__frame { aspect-ratio: 16 / 9; }
  .zoom-through__caption { justify-self: start; width: min(26rem, 100%); margin: -4rem 0 0 2rem; }
}

/* Pinned (JS, motion allowed): one scrub value, eased phases derived here */
.zoom-through--pinned {
  --zoom-through-a: clamp(0, var(--zoom-through-p, 0) / 0.7, 1);
  --zoom-through-e: calc(var(--zoom-through-a) * (2 - var(--zoom-through-a)));
  --zoom-through-h: clamp(0, var(--zoom-through-p, 0) / 0.3, 1);
  --zoom-through-v: clamp(0, (var(--zoom-through-p, 0) - 0.45) / 0.3, 1);
  --zoom-through-c: clamp(0, (var(--zoom-through-p, 0) - 0.68) / 0.22, 1);
  --zoom-through-k: calc(var(--zoom-through-c) * (2 - var(--zoom-through-c)));
  height: 180vh; height: 180svh;
}
.zoom-through--pinned .zoom-through__stage { position: sticky; top: 0; height: 100vh; height: 100svh; max-width: none; padding: 0; overflow: clip; }
.zoom-through--pinned .zoom-through__head {
  position: absolute; left: 0; right: 0; bottom: calc(100% - var(--zoom-through-top)); margin: 0 auto;
  padding: 0 var(--gutter) clamp(1.25rem, 3.5vh, 2.25rem); transform-origin: 50% 100%;
  transform: translate3d(0, calc(var(--zoom-through-h) * -1.5rem), 0) scale(calc(1 - var(--zoom-through-h) * 0.16));
  filter: blur(calc(var(--zoom-through-h) * 12px)); opacity: calc(1 - var(--zoom-through-h) * 1.15);
}
.zoom-through--pinned .zoom-through__title { font-size: min(clamp(2.25rem, 1.2rem + 4vw, 4.5rem), 8.5vh); }
.zoom-through--pinned .zoom-through__cue {
  display: inline-flex; align-items: center; gap: 0.5rem; margin-top: 0.25rem;
  color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.zoom-through__cue svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.zoom-through--pinned .zoom-through__media { position: absolute; inset: 0; z-index: 1; display: block; }
.zoom-through--pinned .zoom-through__frame {
  position: absolute; inset: 0; aspect-ratio: auto; border-radius: 0; box-shadow: none;
  clip-path: inset(
    calc((1 - var(--zoom-through-e)) * var(--zoom-through-top)) calc((1 - var(--zoom-through-e)) * var(--zoom-through-side))
    calc((1 - var(--zoom-through-e)) * var(--zoom-through-bottom)) calc((1 - var(--zoom-through-e)) * var(--zoom-through-side))
    round calc((1 - var(--zoom-through-e)) * var(--zoom-through-radius)));
}
.zoom-through--pinned .zoom-through__img { transform: scale(calc(1.25 - var(--zoom-through-e) * 0.25)); transform-origin: 50% 72%; will-change: transform; }
.zoom-through--pinned .zoom-through__scrim { display: block; opacity: var(--zoom-through-v); }
.zoom-through--pinned .zoom-through__caption {
  position: absolute; left: max(var(--gutter), (100% - var(--container-max)) / 2); right: var(--gutter); bottom: clamp(1.25rem, 6vh, 3.5rem);
  width: auto; max-width: 26rem; margin: 0;
  background: color-mix(in srgb, var(--surface-deep) 80%, transparent);
  -webkit-backdrop-filter: blur(var(--blur-md)) saturate(1.3); backdrop-filter: blur(var(--blur-md)) saturate(1.3);
  opacity: var(--zoom-through-k);
  transform: translate3d(0, calc((1 - var(--zoom-through-k)) * 3rem), 0) scale(calc(0.96 + var(--zoom-through-k) * 0.04));
}
@media (min-width: 768px) {
  .zoom-through--pinned { height: 260vh; height: 260svh; }
}
@media (max-height: 640px) {
  .zoom-through--pinned .zoom-through__cue { display: none; }
}

/* Demo scroll room */
.zoom-through-demo { background: var(--surface-muted); color: var(--text-muted); font-family: var(--font-sans); }
.zoom-through-demo__note { display: grid; place-content: center; justify-items: center; gap: 1rem; min-height: 70vh; padding: 2rem var(--gutter); text-align: center; }
.zoom-through-demo__note p { margin: 0; max-width: 30rem; font-size: 1.0625rem; line-height: 1.6; }
.zoom-through-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--text-main); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.zoom-through-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? Math.min(1, Math.max(0, -r.top / range)) : 0; };

document.querySelectorAll('[data-zoom-through]').forEach((root) => {
  let pinned = false, near = false, frame = 0;

  // One scrub value; CSS derives the clip, zoom, headline exit and caption rise from it
  const render = () => {
    frame = 0;
    if (pinned) root.style.setProperty('--zoom-through-p', progress(root).toFixed(4));
  };
  const queue = () => { if (!frame) frame = requestAnimationFrame(render); };

  // Pin only when motion is allowed; otherwise the still figure stays
  const measure = () => {
    pinned = !reduce.matches;
    root.classList.toggle('zoom-through--pinned', pinned);
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

- Semantics: a `<figure>` with descriptive `alt` and a real `<figcaption>`, and the section is labelled by its `<h2>`. The scrubbed fades are presentational, not hidden states. The fading headline and the caption that hasn't risen yet stay in the accessibility tree in reading order, and neither contains anything focusable.
- No JS or reduced motion: no pin and no zoom. You get a rounded full-width photo (16:9, or 4:5 on phones) with a solid deep caption card tucked under it. JS adds `.zoom-through--pinned` only when motion is allowed, and it follows the setting if it changes.
- Mechanics: the section is 260svh (180svh on phones) with a sticky 100svh stage. JS writes only `--zoom-through-p`, and CSS derives the eased phases with `clamp()` and `calc()`: the clip opens over 0–0.7, the headline leaves over 0–0.3, the vignette arrives from 0.45, and the caption rises over 0.68–0.9, then holds. The headline sits under the photo, so the opening picture slides over it as it recedes.
- Contrast: the headline is `--text-main` on `--surface-muted` (14:1), the lead is `--text-muted` (4.6:1), and the gradient word stays ≥ 3.7:1 as large display text. The pinned caption is 80% deep glass over the vignette (≥ 55% deep across the lower 40% of the frame), which keeps `--text-inverse` ≥ 15:1 and `--text-inverse-muted` ≥ 6:1 even over a pure-white photo. The fallback card is solid deep (19:1 and 7:1).
- The photo is `loading="eager"` because it's the section's hero. Retune the starting card with `--zoom-through-top`, `--zoom-through-side`, `--zoom-through-bottom` and `--zoom-through-radius`. The headline block anchors itself to `--zoom-through-top`, so it always sits just above the card.
