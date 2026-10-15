# Scroll Doodles

A warm-paper ambient layer of hand-drawn doodles in the margins: a curly arrow, a star, a sparkle, a swirl, an underline scribble, a wrench, a little house, a water drop, a heart and a circle scribble. Each doodle draws itself as it rises into view, scrubbed by its own position: fully inked once it's comfortably on screen, still inked after you pass it, and un-drawn if you scroll back up past it. Scroll speed gives every doodle a springy wobble. On phones and tablets fewer, smaller doodles sit at the screen edges in the padding bands, never behind copy. Depends on `tokens/variables.css`.

**Motion:** stroke draw scrubbed by viewport position (`stroke-dashoffset` with `pathLength="1"`) · opening draw-in eased over 900ms · damped-spring rotation wobble from scroll velocity · the loop stops once the wobble settles.
**Fonts:** Caveat for two handwritten notes: https://fonts.googleapis.com/css2?family=Caveat:wght@600&display=swap

## HTML

```html
<div class="amb-doodle-demo">
  <section class="amb-doodle-demo__section amb-doodle-demo__section--hero" aria-labelledby="amb-doodle-hero-title">
    <div class="amb-doodle" aria-hidden="true">
      <svg class="amb-doodle__item" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 10; --amb-doodle-y: 68; --amb-doodle-mx: 9; --amb-doodle-my: 94; --amb-doodle-size: 7.5; --amb-doodle-r: -6deg; --amb-doodle-flex: 1.2; --amb-doodle-c: var(--primary)"><path pathLength="1" d="M12 78c10-14 24-30 40-30 14 0 20 12 10 20-9 7-20-2-15-14 6-15 26-26 40-30m-9-8 10 8-8 9" /></svg>
      <svg class="amb-doodle__item" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 89; --amb-doodle-y: 20; --amb-doodle-mx: 90; --amb-doodle-my: 6; --amb-doodle-size: 5.5; --amb-doodle-r: 8deg; --amb-doodle-flex: -1.4; --amb-doodle-c: var(--accent)"><path pathLength="1" d="M46 12c3 22 10 31 34 36-24 4-31 12-34 38-4-26-11-33-34-37 23-5 30-13 34-37zM80 14v12m-6-6h12" /></svg>
      <svg class="amb-doodle__item amb-doodle__item--wide" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 90; --amb-doodle-y: 74; --amb-doodle-size: 6.5; --amb-doodle-r: 0deg; --amb-doodle-flex: 1; --amb-doodle-c: var(--primary-2)"><path pathLength="1" d="M52 52c-1-6 7-8 9-2 3 8-8 14-15 9-10-7-6-23 7-27 16-5 30 6 29 23-1 18-19 29-37 25-21-5-31-26-24-45 6-17 22-27 40-27" /></svg>
      <svg class="amb-doodle__item amb-doodle__item--wide" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 12; --amb-doodle-y: 18; --amb-doodle-size: 5; --amb-doodle-r: -12deg; --amb-doodle-flex: -1.2; --amb-doodle-c: var(--accent)"><path pathLength="1" d="M50 9l10 28 31 2-24 19 9 30-26-17-25 17 8-30-24-19 31-2 11-27" /></svg>
    </div>
    <div class="amb-doodle-demo__inner">
      <p class="amb-doodle-demo__eyebrow">Brand · Springfield handyman &amp; home repair</p>
      <h2 id="amb-doodle-hero-title" class="amb-doodle-demo__title">Little fixes, <em>big relief.</em></h2>
      <p class="amb-doodle-demo__lead">The dripping tap, the sticky door, the light that flickers. Send us the list and one friendly pro sorts the lot in a single visit.</p>
      <div class="amb-doodle-demo__actions">
        <a class="amb-doodle-demo__btn amb-doodle-demo__btn--primary" href="#amb-doodle-book">
          Send us your list
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-doodle-demo__btn" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
      <p class="amb-doodle-demo__note">we pick up on the second ring</p>
      <p class="amb-doodle-demo__hint">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
        Scroll
      </p>
    </div>
  </section>

  <section class="amb-doodle-demo__section" aria-labelledby="amb-doodle-services-title">
    <div class="amb-doodle" aria-hidden="true">
      <svg class="amb-doodle__item" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 84; --amb-doodle-y: 12; --amb-doodle-mx: 90; --amb-doodle-my: 3; --amb-doodle-size: 6.5; --amb-doodle-r: 18deg; --amb-doodle-flex: 1.3; --amb-doodle-c: var(--text-main)"><path pathLength="1" d="M62 14c-11-4-23 4-22 17 0 4 2 7 0 9L14 66c-4 4-3 11 2 15 4 3 10 2 13-1l26-26c3-2 6 0 10 0 12 1 21-10 18-22l-10 9-10-3-2-10 10-9c-3-1-6-2-9-1zM18 74a2.5 2.5 0 1 0 5 0 2.5 2.5 0 1 0-5 0" /></svg>
      <svg class="amb-doodle__item" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 14; --amb-doodle-y: 16; --amb-doodle-mx: 9; --amb-doodle-my: 97; --amb-doodle-size: 5.5; --amb-doodle-r: -10deg; --amb-doodle-flex: -1.1; --amb-doodle-c: var(--primary)"><path pathLength="1" d="M50 10c-8 17-25 33-25 51 0 15 11 27 25 27s26-12 26-27c0-18-17-34-26-51zM38 60c-1 8 3 14 9 17" /></svg>
      <svg class="amb-doodle__item amb-doodle__item--wide" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 88; --amb-doodle-y: 95; --amb-doodle-size: 8; --amb-doodle-r: -4deg; --amb-doodle-flex: 0.8; --amb-doodle-c: var(--primary-2)"><path pathLength="1" d="M8 50c20-4 50-6 84-2-26 0-58 4-76 12 22-3 46-4 66-1" /></svg>
    </div>
    <div class="amb-doodle-demo__inner">
      <header class="amb-doodle-demo__head">
        <p class="amb-doodle-demo__eyebrow">Services</p>
        <h2 id="amb-doodle-services-title" class="amb-doodle-demo__h2">Small jobs welcome.</h2>
        <p class="amb-doodle-demo__intro">Fixed prices per task, posted up front. Book one job or bundle the whole list.</p>
      </header>
      <ul class="amb-doodle-demo__grid" role="list">
        <li class="amb-doodle-demo__card">
          <span class="amb-doodle-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 3s6 6.4 6 10.5a6 6 0 0 1-12 0C6 9.4 12 3 12 3z" /></svg></span>
          <h3><a class="amb-doodle-demo__link" href="#amb-doodle-book">Leaks &amp; taps</a></h3>
          <p>Drips, running toilets and new washers.</p>
          <p class="amb-doodle-demo__price">from <strong>$69</strong></p>
        </li>
        <li class="amb-doodle-demo__card">
          <span class="amb-doodle-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.4 1 1.1 1 1.9V16h5v-.2c0-.8.4-1.5 1-1.9A6 6 0 0 0 12 3z" /></svg></span>
          <h3><a class="amb-doodle-demo__link" href="#amb-doodle-book">Lights &amp; outlets</a></h3>
          <p>Flicker fixes, dimmers and new fittings.</p>
          <p class="amb-doodle-demo__price">from <strong>$79</strong></p>
        </li>
        <li class="amb-doodle-demo__card">
          <span class="amb-doodle-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M6 21V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v17M3 21h18M14 12h.01" /></svg></span>
          <h3><a class="amb-doodle-demo__link" href="#amb-doodle-book">Doors &amp; windows</a></h3>
          <p>Sticking, squeaking or letting in a draft.</p>
          <p class="amb-doodle-demo__price">from <strong>$59</strong></p>
        </li>
        <li class="amb-doodle-demo__card">
          <span class="amb-doodle-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z" /></svg></span>
          <h3><a class="amb-doodle-demo__link" href="#amb-doodle-book">The odd-jobs list</a></h3>
          <p>Shelves, art, caulk and flat-pack, by the hour.</p>
          <p class="amb-doodle-demo__price">from <strong>$55</strong>/hr</p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-doodle-demo__section" aria-labelledby="amb-doodle-proof-title">
    <div class="amb-doodle" aria-hidden="true">
      <svg class="amb-doodle__item" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 12; --amb-doodle-y: 30; --amb-doodle-mx: 9; --amb-doodle-my: 5; --amb-doodle-size: 6; --amb-doodle-r: -8deg; --amb-doodle-flex: 1.4; --amb-doodle-c: var(--danger)"><path pathLength="1" d="M50 85C34 72 13 58 15 36c2-14 19-20 30-10 3 3 5 6 6 9 2-6 7-13 16-15 13-3 23 8 20 22-4 20-22 31-38 44" /></svg>
      <svg class="amb-doodle__item amb-doodle__item--wide" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 88; --amb-doodle-y: 70; --amb-doodle-size: 7; --amb-doodle-r: 6deg; --amb-doodle-flex: -1; --amb-doodle-c: var(--primary)"><path pathLength="1" d="M30 26c18-12 50-10 60 10 9 19-6 40-30 46-24 6-48-6-50-26-2-18 16-32 38-34 14-1 26 2 34 8" /></svg>
    </div>
    <div class="amb-doodle-demo__inner">
      <figure class="amb-doodle-demo__quote">
        <h2 id="amb-doodle-proof-title" class="amb-doodle-demo__eyebrow">Neighbours say it best</h2>
        <blockquote><p>"Seven little jobs I'd put off for a year, done before lunch. He even fixed the gate latch I forgot to mention."</p></blockquote>
        <figcaption><span class="amb-doodle-demo__sign">Maria R.</span> Westlake · 4 hours, 7 jobs</figcaption>
      </figure>
      <ul class="amb-doodle-demo__chips" role="list">
        <li><strong>4.9</strong> average from 1,200+ reviews</li>
        <li><strong>98%</strong> fixed on the first visit</li>
        <li><strong>12-month</strong> workmanship guarantee</li>
      </ul>
    </div>
  </section>

  <section class="amb-doodle-demo__section" id="amb-doodle-book" aria-labelledby="amb-doodle-cta-title">
    <div class="amb-doodle" aria-hidden="true">
      <svg class="amb-doodle__item" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 12; --amb-doodle-y: 46; --amb-doodle-mx: 10; --amb-doodle-my: 6; --amb-doodle-size: 7; --amb-doodle-r: -4deg; --amb-doodle-flex: 1.1; --amb-doodle-c: var(--text-main)"><path pathLength="1" d="M13 51c12-11 24-22 37-33 12 10 24 21 37 32M24 43c-1 14 0 28 1 41 17 1 34 0 51-1 0-14 1-27-1-40M44 84c0-7-1-13 0-20 4 0 8-1 12 0 1 7 0 13 0 20M66 33c0-4 0-9 1-13h8c0 6 1 13 0 19" /></svg>
      <svg class="amb-doodle__item amb-doodle__item--wide" viewBox="0 0 100 100" focusable="false" style="--amb-doodle-x: 86; --amb-doodle-y: 58; --amb-doodle-size: 6.5; --amb-doodle-r: 10deg; --amb-doodle-flex: -1.3; --amb-doodle-c: var(--primary)"><path pathLength="1" d="M86 82C70 66 52 56 22 50m10-12-12 12 14 9" /></svg>
    </div>
    <div class="amb-doodle-demo__inner">
      <div class="amb-doodle-demo__panel">
        <h2 id="amb-doodle-cta-title" class="amb-doodle-demo__h2">Got a list? We'll bring the toolbox.</h2>
        <p class="amb-doodle-demo__intro">Pick a two-hour window this week. Westlake, Northside and Riverside.</p>
        <div class="amb-doodle-demo__actions">
          <a class="amb-doodle-demo__btn amb-doodle-demo__btn--primary" href="#amb-doodle-book">
            Book a visit
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
          <a class="amb-doodle-demo__btn" href="mailto:hello@example.com">hello@example.com</a>
        </div>
        <p class="amb-doodle-demo__note">no call-out fee, ever</p>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
@property --amb-doodle-d { syntax: "<number>"; inherits: true; initial-value: 1; } /* draw progress, 0–1 */

/* Layer: decorative, first child of a relative + isolated section, behind its content */
.amb-doodle {
  --amb-doodle-k: 0.6; /* doodle scale: phones */
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-doodle--page { position: fixed; }
/* Contrast guard: --amb-doodle-scrim (0–1) fades a paper-coloured veil over the doodles */
.amb-doodle::after {
  content: ""; position: absolute; inset: 0;
  background: color-mix(in srgb, color-mix(in srgb, var(--accent) 7%, var(--surface-light)) calc(var(--amb-doodle-scrim, 0) * 100%), transparent);
}

/* Doodles: phones and tablets use the edge positions (mx/my) in the padding bands */
.amb-doodle__item {
  position: absolute; overflow: visible; aspect-ratio: 1; height: auto;
  left: calc(var(--amb-doodle-mx, var(--amb-doodle-x)) * 1%);
  top: calc(var(--amb-doodle-my, var(--amb-doodle-y)) * 1%);
  width: calc(var(--amb-doodle-size) * var(--amb-doodle-k) * 1rem);
  translate: -50% -50%;
  rotate: calc(var(--amb-doodle-r, 0deg) + var(--amb-doodle-wobble, 0deg) * var(--amb-doodle-flex, 1));
}
.amb-doodle__item--wide { display: none; }
/* pathLength="1" makes every stroke 1 unit long; a 1-on, 2-off dash slides in as the offset falls */
.amb-doodle__item path {
  fill: none; stroke: var(--amb-doodle-c, var(--text-main)); stroke-width: 3.4; stroke-linecap: round; stroke-linejoin: round;
  stroke-dasharray: 1 2; stroke-dashoffset: calc(1.01 - 1.01 * var(--amb-doodle-d));
}

/* Undrawn from first paint only when JS will run; a failsafe inks them if it never does */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .amb-doodle__item { --amb-doodle-d: 0; }
  .amb-doodle:not(.amb-doodle--js) .amb-doodle__item { animation: amb-doodle-ink var(--dur-5) var(--ease-out) 2.5s forwards; }
}
@keyframes amb-doodle-ink { to { --amb-doodle-d: 1; } }

@media (min-width: 768px) { .amb-doodle { --amb-doodle-k: 0.75; } }
@media (min-width: 1024px) {
  .amb-doodle { --amb-doodle-k: 1; }
  .amb-doodle__item { left: calc(var(--amb-doodle-x) * 1%); top: calc(var(--amb-doodle-y) * 1%); }
  .amb-doodle__item--wide { display: block; }
}

/* ---- Demo page (warm paper) ---- */
.amb-doodle-demo {
  --amb-doodle-paper: color-mix(in srgb, var(--accent) 7%, var(--surface-light));
  --amb-doodle-soft: color-mix(in srgb, var(--text-main) 80%, var(--surface-light));
  --amb-doodle-hand: "Caveat", var(--font-display);
  overflow-x: clip; color: var(--text-main); font-family: var(--font-sans);
  background:
    radial-gradient(circle, color-mix(in srgb, var(--text-main) 11%, transparent) 1px, transparent 1.5px) 0 0 / 1.5rem 1.5rem,
    var(--amb-doodle-paper);
}
.amb-doodle-demo__section { position: relative; isolation: isolate; padding-block: clamp(5rem, 10vw, 7.5rem); }
.amb-doodle-demo__section--hero { display: grid; align-items: center; min-height: 88vh; min-height: 88svh; text-align: center; }
.amb-doodle-demo__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); box-sizing: border-box; }

.amb-doodle-demo__eyebrow { margin: 0; color: var(--amb-doodle-soft); font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.amb-doodle-demo__title {
  max-width: 12ch; margin: 1rem auto 0; font: 600 clamp(2.75rem, 1.4rem + 5.6vw, 5.5rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-doodle-demo__title em { /* highlighter stroke */
  font-style: normal; padding-inline: 0.06em; -webkit-box-decoration-break: clone; box-decoration-break: clone;
  background: linear-gradient(transparent 58%, color-mix(in srgb, var(--accent) 45%, transparent) 58% 90%, transparent 90%);
}
.amb-doodle-demo__lead { max-width: 34rem; margin: 1.25rem auto 0; color: var(--amb-doodle-soft); font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.amb-doodle-demo__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.amb-doodle-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  box-shadow: inset 0 0 0 1.5px var(--text-main), 0 3px 0 var(--text-main);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2) var(--ease-out);
}
.amb-doodle-demo__btn:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1.5px var(--text-main), 0 5px 0 var(--text-main); }
.amb-doodle-demo__btn:active { transform: translateY(2px); box-shadow: inset 0 0 0 1.5px var(--text-main), 0 1px 0 var(--text-main); }
.amb-doodle-demo__btn--primary { background: var(--primary); color: var(--text-inverse); }
.amb-doodle-demo__inner svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-doodle-demo :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 4px; }
.amb-doodle-demo__note { margin: 0.75rem 0 0; color: var(--primary); font: 600 1.5rem/1.2 var(--amb-doodle-hand); rotate: -2deg; }
.amb-doodle-demo__hint {
  display: flex; flex-direction: column; align-items: center; gap: 0.375rem; margin: 3rem 0 0; color: var(--amb-doodle-soft);
  font: 500 0.6875rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.amb-doodle-demo__hint svg { animation: amb-doodle-nudge 1.4s var(--ease-in-out) 3; } /* three nudges, then still */

/* Section heads */
.amb-doodle-demo__head { max-width: 36rem; margin: 0 auto 3rem; text-align: center; }
.amb-doodle-demo__h2 { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.8vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.amb-doodle-demo__intro { max-width: 32rem; margin: 1rem auto 0; color: var(--amb-doodle-soft); font-size: 1.0625rem; line-height: 1.6; }

/* Service cards: index cards with a strip of tape, straightening on hover */
.amb-doodle-demo__grid { display: grid; gap: 1.5rem 1.25rem; margin: 0; padding: 0; list-style: none; }
.amb-doodle-demo__card {
  position: relative; display: flex; flex-direction: column; gap: 0.5rem; padding: 1.75rem 1.5rem 1.5rem; border-radius: var(--radius-lg);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-lg);
  rotate: -0.6deg; transition: rotate var(--dur-4) var(--ease-spring), translate var(--dur-4) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-doodle-demo__card:nth-child(even) { rotate: 0.5deg; }
.amb-doodle-demo__card:hover { rotate: 0deg; translate: 0 -4px; box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl); }
.amb-doodle-demo__card::before {
  content: ""; position: absolute; top: -0.625rem; left: 50%; width: 4.5rem; height: 1.25rem; translate: -50% 0; rotate: -3deg;
  background: color-mix(in srgb, var(--accent) 32%, transparent); box-shadow: var(--shadow-sm);
}
.amb-doodle-demo__icon {
  display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 50%; color: var(--primary);
  background: color-mix(in srgb, var(--primary) 9%, var(--surface-light)); box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--primary) 35%, transparent);
}
.amb-doodle-demo__card h3 { margin: 0.75rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-doodle-demo__card p { margin: 0; color: var(--amb-doodle-soft); line-height: 1.55; }
.amb-doodle-demo__link { color: inherit; text-decoration: none; }
.amb-doodle-demo__link::after { content: ""; position: absolute; inset: 0; border-radius: inherit; }
.amb-doodle-demo .amb-doodle-demo__link:focus-visible { outline: none; }
.amb-doodle-demo__link:focus-visible::after { outline: 2px solid var(--primary); outline-offset: 4px; }
.amb-doodle-demo__card .amb-doodle-demo__price { margin-top: auto; padding-top: 1rem; border-top: 1px dashed var(--border-subtle); font: 500 0.8125rem var(--font-mono); }
.amb-doodle-demo__price strong { color: var(--text-main); font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }

/* Proof */
.amb-doodle-demo__quote { max-width: 46rem; margin: 0 auto; text-align: center; }
.amb-doodle-demo__quote blockquote { margin: 1.25rem 0 0; }
.amb-doodle-demo__quote blockquote p { margin: 0; font: 500 clamp(1.5rem, 1.1rem + 1.8vw, 2.5rem)/1.25 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.amb-doodle-demo__quote figcaption { margin-top: 1.25rem; color: var(--amb-doodle-soft); font-size: 0.9375rem; }
.amb-doodle-demo__sign { display: block; color: var(--primary); font: 600 2rem/1 var(--amb-doodle-hand); rotate: -3deg; }
.amb-doodle-demo__chips { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin: 2.5rem 0 0; padding: 0; list-style: none; }
.amb-doodle-demo__chips li {
  padding: 0.625rem 1rem; border-radius: var(--radius-full); background: var(--surface-light); color: var(--amb-doodle-soft); font-size: 0.875rem;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
}
.amb-doodle-demo__chips strong { color: var(--text-main); font-family: var(--font-display); }

/* CTA panel, taped to the page */
.amb-doodle-demo__panel {
  position: relative; max-width: 42rem; margin-inline: auto; padding: clamp(2.25rem, 6vw, 3.5rem) clamp(1.25rem, 5vw, 3rem); text-align: center;
  border-radius: var(--radius-lg); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl);
}
.amb-doodle-demo__panel::before, .amb-doodle-demo__panel::after {
  content: ""; position: absolute; top: -0.625rem; width: 5rem; height: 1.25rem;
  background: color-mix(in srgb, var(--primary-2) 22%, transparent); box-shadow: var(--shadow-sm);
}
.amb-doodle-demo__panel::before { left: 1.25rem; rotate: -8deg; }
.amb-doodle-demo__panel::after { right: 1.25rem; rotate: 7deg; }
.amb-doodle-demo__panel .amb-doodle-demo__h2 { margin-top: 0; }

@media (min-width: 600px) { .amb-doodle-demo__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1024px) { .amb-doodle-demo__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); } }

@media (prefers-reduced-motion: reduce) {
  .amb-doodle__item { --amb-doodle-d: 1 !important; rotate: var(--amb-doodle-r, 0deg); animation: none !important; }
  .amb-doodle-demo__hint svg { animation: none; }
}
@keyframes amb-doodle-nudge { 50% { transform: translateY(5px); } }
```

## JS

```js
// Scroll Doodles: each stroke is scrubbed by its doodle's own place in the viewport; scroll speed adds a
// springy wobble. One shared rAF loop for every .amb-doodle layer, stopped whenever nothing moves.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const layers = [...document.querySelectorAll('.amb-doodle')];

if (layers.length && !reduce.matches) {
  const shown = new Set();
  const items = layers.flatMap((layer) => [...layer.querySelectorAll('.amb-doodle__item')].map((el, i, all) => ({
    el, page: layer.classList.contains('amb-doodle--page'), at: ((i + 1) / (all.length + 1)) * 0.8, top: 0, h: 0, d: -1,
  })));
  const clamp01 = (v) => Math.min(1, Math.max(0, v));
  let raf = 0, lastY = scrollY, lastT = 0, start = 0, wob = 0, spin = 0, vh = innerHeight, maxScroll = 1;

  // Positions are cached on resize, so the loop reads no layout (hidden doodles measure 0 and are skipped)
  const measure = () => {
    vh = innerHeight;
    maxScroll = Math.max(1, document.documentElement.scrollHeight - vh);
    for (const it of items) { const r = it.el.getBoundingClientRect(); it.top = r.top + scrollY; it.h = r.height; }
  };

  const tick = (t) => {
    const dt = lastT ? Math.min(64, t - lastT) : 16.7;
    const y = scrollY;
    const v = (y - lastY) / dt; // px per ms
    lastT = t;
    lastY = y;
    start ||= t;
    const intro = 1 - (1 - Math.min(1, (t - start) / 900)) ** 3; // opening draw-in, ease-out
    // One damped spring kicked by scroll speed; each doodle scales it by its own --amb-doodle-flex
    spin = (spin + (Math.max(-14, Math.min(14, v * 10)) - wob) * 0.12) * 0.8;
    wob += spin;
    const moving = intro < 1 || Math.abs(wob) + Math.abs(spin) > 0.03;
    for (const it of items) {
      if (!it.h) continue;
      // Ink from when the doodle's centre reaches the bottom edge until it sits 30% up the screen.
      // The page-wide layer inks its doodles one after another across the whole page instead.
      const target = it.page
        ? clamp01((y / maxScroll - it.at) * 5 + 0.5)
        : clamp01((vh * 1.02 - (it.top + it.h / 2 - y)) / (vh * 0.32));
      const d = Math.round(target * intro * 1000) / 1000;
      if (d !== it.d) { it.el.style.setProperty('--amb-doodle-d', d); it.d = d; }
    }
    shown.forEach((layer) => layer.style.setProperty('--amb-doodle-wobble', `${wob.toFixed(2)}deg`));
    raf = moving ? requestAnimationFrame(tick) : 0;
  };

  // Run only while a layer is on screen, the tab is visible and motion is allowed
  const wake = () => {
    if (raf || !shown.size || reduce.matches || document.visibilityState === 'hidden') return;
    lastY = scrollY;
    lastT = 0;
    raf = requestAnimationFrame(tick);
  };

  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => (e.isIntersecting ? shown.add(e.target) : shown.delete(e.target)));
    wake();
  });
  measure();
  layers.forEach((layer) => { layer.classList.add('amb-doodle--js'); io.observe(layer); });
  new ResizeObserver(() => { measure(); wake(); }).observe(document.documentElement);
  addEventListener('resize', measure, { passive: true });
  addEventListener('scroll', wake, { passive: true });
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') { cancelAnimationFrame(raf); raf = 0; } else wake();
  });
}
```

## Notes

- **Layer contract:** each `.amb-doodle` is decorative (`aria-hidden="true"`, `pointer-events: none`, and every SVG is `focusable="false"`). It's the first child of a `position: relative; isolation: isolate` section, at `z-index: -1` behind that section's content. Give each section its own layer, so its doodles sit beside its copy. `.amb-doodle--page` fixes one layer behind the whole page (sections need transparent backgrounds) and inks its doodles one after another as the page scrolls. Use one ambient background per page.
- **Contrast:** doodles never sit behind copy. On desktop they're in the margins beside centred text; below 1024px they move to the screen edges inside the top and bottom padding bands. Worst case under body copy is the paper's dot grid: the soft body colour (`--text-main` 80% with `--surface-light`) still reaches 5.9:1 over a dot, the highlighted headline 10:1, and the handwritten notes 4:1 (large text). If your copy has to overlap doodles, `--amb-doodle-scrim` (0–1) fades a paper-coloured veil over them.
- **Performance:** one shared rAF loop. It runs only while a layer is on screen, the tab is visible and the opening draw or the wobble spring is live; the wobble settles in under a second, then the loop stops until the next scroll. Each frame writes `--amb-doodle-d` only for doodles whose progress changed, plus one wobble angle per visible layer. Positions are cached on resize, so there are no layout reads per frame. No filters or blur. The demo has 11 doodles on desktop and 6 on phones and tablets.
- **No JS and reduced motion:** the registered `--amb-doodle-d` defaults to 1, so without JS every doodle is fully drawn and still. With JS they're undrawn from first paint (`@media (scripting: enabled)`), and a 2.5s CSS failsafe inks them if the script never runs. Under reduced motion they're fully drawn with no wobble, and the scroll hint skips its three nudges.
- **Support:** `@property` lets the failsafe ink smoothly (without it, the failsafe snaps). Also uses individual transform properties, `@media (scripting)` and `color-mix()`. Caveat is used only for the two handwritten notes and falls back to `--font-display`. The loop listens to window scroll.
- **Adapting:** any stroke drawing works. Give each doodle one `<path pathLength="1">` (several subpaths are fine; at 0 the whole path is hidden and at 1 it is complete). Place it with `--amb-doodle-x`/`--amb-doodle-y` (% of the section), and below 1024px with `--amb-doodle-mx`/`--amb-doodle-my`. Set `--amb-doodle-size` (rem), `--amb-doodle-r` (angle), `--amb-doodle-flex` (wobble strength; negative turns the other way) and `--amb-doodle-c` (any colour token). Add `--wide` to keep a doodle to desktop.
