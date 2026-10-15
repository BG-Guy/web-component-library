# Rising Tide

A light, water-tinted layer for a plumbing page: a strip of water along the bottom of the viewport rises with reading progress, from 6% of the screen to 35% at most. Three SVG waves take their phase from the scroll position, and a damped "slosh" spring turns scroll speed into wave height and tilt that rocks back and settles when you stop. Bubbles rise only while you scroll, and reaching the end throws a one-shot splash. Phones get the same layer with fewer wave points and true-to-size wavelengths. Depends on `tokens/variables.css`.

**Motion:** water level and wave phase scrubbed by scroll · slosh spring for amplitude and tilt (settles in under 2s) · bubbles rising while scrolling (Web Animations, 1.1–1.7s) · end splash with a surface ring (under 1s) · cards and buttons lift with `--ease-spring` over `--dur-3`.

## HTML

```html
<div class="amb-tide-demo">
  <div class="amb-tide" aria-hidden="true">
    <div class="amb-tide__frame">
      <div class="amb-tide__body"></div>
      <svg class="amb-tide__waves" viewBox="0 0 1200 120" preserveAspectRatio="none" focusable="false">
        <path class="amb-tide__wave amb-tide__wave--back" d="M0 52C70 42.7 130 42.7 200 52S330 61.3 400 52S530 42.7 600 52S730 61.3 800 52S930 42.7 1000 52S1130 61.3 1200 52V122H0Z" />
        <path class="amb-tide__wave amb-tide__wave--mid" d="M0 62C53 70 98 70 150 62S248 54 300 62S398 70 450 62S548 54 600 62S698 70 750 62S848 54 900 62S998 70 1050 62S1148 54 1200 62V122H0Z" />
        <path class="amb-tide__wave amb-tide__wave--front" d="M0 72C84 65.3 156 65.3 240 72S396 78.7 480 72S636 65.3 720 72S876 78.7 960 72S1116 65.3 1200 72V122H0Z" />
      </svg>
      <div class="amb-tide__bubbles">
        <span class="amb-tide__bubble"></span><span class="amb-tide__bubble"></span><span class="amb-tide__bubble"></span>
        <span class="amb-tide__bubble"></span><span class="amb-tide__bubble"></span><span class="amb-tide__bubble"></span>
        <span class="amb-tide__bubble"></span><span class="amb-tide__bubble"></span><span class="amb-tide__bubble"></span>
        <span class="amb-tide__bubble"></span><span class="amb-tide__bubble"></span><span class="amb-tide__bubble"></span>
      </div>
      <div class="amb-tide__splash">
        <span class="amb-tide__ring"></span>
        <span class="amb-tide__drop"></span><span class="amb-tide__drop"></span><span class="amb-tide__drop"></span><span class="amb-tide__drop"></span><span class="amb-tide__drop"></span>
        <span class="amb-tide__drop"></span><span class="amb-tide__drop"></span><span class="amb-tide__drop"></span><span class="amb-tide__drop"></span><span class="amb-tide__drop"></span>
      </div>
    </div>
  </div>

  <section class="amb-tide-demo__hero" aria-labelledby="amb-tide-title">
    <div class="amb-tide-demo__inner">
      <p class="amb-tide-demo__eyebrow">Brand Plumbing · Springfield</p>
      <h2 id="amb-tide-title" class="amb-tide-demo__display">Plumbing that keeps the water <span>where it belongs.</span></h2>
      <p class="amb-tide-demo__lead">Leaks, drains and water heaters fixed by licensed plumbers, at a flat price you agree to before we start.</p>
      <div class="amb-tide-demo__actions">
        <a class="amb-tide-demo__btn amb-tide-demo__btn--primary" href="#amb-tide-book">
          Book a plumber
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-tide-demo__btn amb-tide-demo__btn--ghost" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
      <p class="amb-tide-demo__hint">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
        Scroll to raise the tide
      </p>
    </div>
  </section>

  <section class="amb-tide-demo__section" aria-labelledby="amb-tide-services">
    <div class="amb-tide-demo__inner">
      <header class="amb-tide-demo__head">
        <p class="amb-tide-demo__eyebrow">What we fix</p>
        <h2 id="amb-tide-services" class="amb-tide-demo__title">Every pipe, from the main to the tap.</h2>
      </header>
      <ul class="amb-tide-demo__cards" role="list">
        <li class="amb-tide-demo__card">
          <span class="amb-tide-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11z" /><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5" /></svg></span>
          <h3><a href="#amb-tide-book">Leak repair</a></h3>
          <p>Traced with acoustic detection, fixed without tearing up the floor.</p>
          <p class="amb-tide-demo__price">from <b>$149</b></p>
        </li>
        <li class="amb-tide-demo__card">
          <span class="amb-tide-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9" /><path d="M8 9h8M7 12h10M8 15h8" /></svg></span>
          <h3><a href="#amb-tide-book">Drain cleaning</a></h3>
          <p>Hydro-jetting clears roots and grease, not just today's clog.</p>
          <p class="amb-tide-demo__price">from <b>$99</b></p>
        </li>
        <li class="amb-tide-demo__card">
          <span class="amb-tide-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><rect x="6" y="2.5" width="12" height="18" rx="3" /><path d="M9 20.5v1.5M15 20.5v1.5M12 8.5c-1.2 1.5-1.8 2.5-1.8 3.3a1.8 1.8 0 0 0 3.6 0c0-.8-.6-1.8-1.8-3.3z" /></svg></span>
          <h3><a href="#amb-tide-book">Water heaters</a></h3>
          <p>Tank or tankless, fitted the same day with the old one hauled away.</p>
          <p class="amb-tide-demo__price">from <b>$1,290</b></p>
        </li>
        <li class="amb-tide-demo__card">
          <span class="amb-tide-demo__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M3 8a2 2 0 0 1 2-2h2l1.5-2h7L17 6h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" /><circle cx="12" cy="12.5" r="3.5" /></svg></span>
          <h3><a href="#amb-tide-book">Sewer camera</a></h3>
          <p>See inside the line on video before anyone picks up a shovel.</p>
          <p class="amb-tide-demo__price">from <b>$189</b></p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-tide-demo__section" aria-labelledby="amb-tide-proof">
    <div class="amb-tide-demo__inner amb-tide-demo__proof">
      <div>
        <p class="amb-tide-demo__eyebrow">Why Springfield calls us</p>
        <h2 id="amb-tide-proof" class="amb-tide-demo__title">Fast when it floods. Tidy when it doesn't.</h2>
        <dl class="amb-tide-demo__stats">
          <div><dt>average rating, 1,200+ reviews</dt><dd>4.9</dd></div>
          <div><dt>average emergency arrival</dt><dd>38 min</dd></div>
          <div><dt>real dispatcher, no call centre</dt><dd>24/7</dd></div>
          <div><dt>licensed in Springfield since</dt><dd>1998</dd></div>
        </dl>
      </div>
      <figure class="amb-tide-demo__quote">
        <span class="amb-tide-demo__stars" role="img" aria-label="5 out of 5 stars">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
        </span>
        <blockquote><p>"Our basement was filling up at 2 a.m. Sam was at the door in 40 minutes and the pump was running by three."</p></blockquote>
        <figcaption><span class="amb-tide-demo__avatar" aria-hidden="true">DR</span><span><strong>Dana R.</strong> · Northside</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="amb-tide-demo__section amb-tide-demo__cta" id="amb-tide-book" aria-labelledby="amb-tide-cta">
    <div class="amb-tide-demo__inner">
      <p class="amb-tide-demo__eyebrow">Same-day slots</p>
      <h2 id="amb-tide-cta" class="amb-tide-demo__display amb-tide-demo__display--sm">Fix it before the <span>next drip.</span></h2>
      <p class="amb-tide-demo__lead">Westlake, Northside, Riverside and the rest of Springfield. Upfront pricing, licensed and insured.</p>
      <div class="amb-tide-demo__actions">
        <a class="amb-tide-demo__btn amb-tide-demo__btn--primary" href="mailto:hello@example.com">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-tide-demo__btn amb-tide-demo__btn--ghost" href="tel:+15555550123">Call (555) 555-0123</a>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Layer: behind its section by default, behind the whole page with --page */
.amb-tide {
  --amb-tide-p: 0.5; /* level 0–1; JS writes it, still layouts sit at mid level */
  --amb-tide-shallow: color-mix(in srgb, var(--primary-2) 12%, var(--surface-light));
  --amb-tide-mid: color-mix(in srgb, color-mix(in srgb, var(--primary) 50%, var(--primary-2)) 14%, var(--surface-light));
  --amb-tide-front: color-mix(in srgb, var(--primary) 17%, var(--surface-light));
  --amb-tide-deep: color-mix(in srgb, var(--primary) 24%, var(--surface-light));
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-tide--page { position: fixed; }
/* JS will drive the level: start low so nothing drops on load */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .amb-tide { --amb-tide-p: 0; }
}

/* A viewport-tall frame that sticks while its section scrolls past */
.amb-tide__frame {
  position: sticky; top: 0; height: 100vh; height: 100svh; max-height: 100%;
  overflow: hidden; container-type: size;
}
.amb-tide__frame > * {
  --amb-tide-y: calc((94 - 29 * var(--amb-tide-p)) * 1vh); /* surface line: 6% → 35% from the bottom */
  position: absolute; top: 0; left: 0; width: 100%;
}
@supports (height: 1cqh) {
  .amb-tide__frame > * { --amb-tide-y: calc((94 - 29 * var(--amb-tide-p)) * 1cqh); }
}
/* Contrast guard: a veil of the page colour, 0–1 */
.amb-tide__frame::after {
  content: ""; position: absolute; inset: 0;
  background: var(--surface-light); opacity: var(--amb-tide-scrim, 0);
}

/* Water: a pre-lit body plus three wave bands drawn by JS */
.amb-tide__body {
  height: 100%; transform: translateY(var(--amb-tide-y));
  background:
    radial-gradient(55% 22% at 22% 2%, color-mix(in srgb, var(--surface-light) 60%, transparent), transparent 70%),
    radial-gradient(40% 16% at 80% 7%, color-mix(in srgb, var(--surface-light) 40%, transparent), transparent 70%),
    linear-gradient(var(--amb-tide-front), var(--amb-tide-deep) 38%);
}
.amb-tide__waves {
  display: block; height: 7.5rem; overflow: hidden;
  transform: translateY(calc(var(--amb-tide-y) - 4.5rem)); /* front wave's mean line sits on the surface */
}
.amb-tide__wave--back { fill: var(--amb-tide-shallow); }
.amb-tide__wave--mid { fill: var(--amb-tide-mid); }
.amb-tide__wave--front {
  fill: var(--amb-tide-front); stroke: color-mix(in srgb, var(--surface-light) 80%, transparent);
  stroke-width: 2; vector-effect: non-scaling-stroke;
}
.amb-tide.is-moving .amb-tide__body, .amb-tide.is-moving .amb-tide__waves { will-change: transform; }

/* Bubbles and splash: pooled, hidden until a Web Animation plays them */
.amb-tide__bubbles { height: 100%; }
.amb-tide__splash { height: 0; transform: translateY(var(--amb-tide-y)); }
.amb-tide__bubble, .amb-tide__ring, .amb-tide__drop { position: absolute; visibility: hidden; opacity: 0; }
.amb-tide__bubble {
  left: 0; bottom: -0.5rem; width: 0.625rem; height: 0.625rem; border-radius: 50%;
  background:
    radial-gradient(circle at 34% 30%, var(--surface-light) 0 16%, transparent 24%),
    color-mix(in srgb, var(--surface-light) 35%, transparent);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 40%, var(--surface-light));
}
.amb-tide__ring {
  left: 50%; top: -1.25rem; width: 16rem; height: 2.5rem; margin-left: -8rem; border-radius: 50%;
  box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--primary) 45%, var(--surface-light));
}
.amb-tide__drop {
  left: 50%; top: -0.25rem; width: 0.5rem; height: 0.5rem; margin-left: -0.25rem; border-radius: 50%;
  background:
    radial-gradient(circle at 34% 30%, var(--surface-light) 0 18%, transparent 30%),
    color-mix(in srgb, var(--primary) 32%, var(--surface-light));
}
.amb-tide__drop:nth-child(odd) { width: 0.375rem; height: 0.375rem; }
@media (prefers-reduced-motion: reduce) {
  .amb-tide__bubbles, .amb-tide__splash { display: none; }
}

/* Demo page: a plumbing landing page with the tide behind it */
.amb-tide-demo {
  position: relative; isolation: isolate;
  background: linear-gradient(var(--surface-muted), var(--surface-light) 40rem);
  color: var(--text-main); font-family: var(--font-sans);
}
.amb-tide-demo__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.amb-tide-demo__hero { display: grid; align-items: center; min-height: 88vh; min-height: 88svh; padding-block: 4rem 5rem; }
.amb-tide-demo__section { padding-block: clamp(4rem, 9vw, 6.5rem); }
.amb-tide-demo__eyebrow {
  display: flex; align-items: center; gap: 0.625rem; margin: 0;
  color: var(--primary-hover); font: 600 0.75rem/1.3 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-tide-demo__eyebrow::before { content: ""; flex: none; width: 1.5rem; height: 2px; border-radius: 2px; background: var(--gradient-brand); }
.amb-tide-demo__display {
  max-width: 14ch; margin: 1.25rem 0 0;
  font: 600 clamp(2.5rem, 1.3rem + 5.2vw, 5.25rem)/0.98 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-tide-demo__display span {
  background: linear-gradient(100deg, var(--primary-hover), color-mix(in srgb, var(--primary-2) 70%, var(--text-main)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.amb-tide-demo__display--sm { font-size: clamp(2.25rem, 1.4rem + 3.8vw, 4rem); }
.amb-tide-demo__lead { max-width: 34rem; margin: 1.5rem 0 0; font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.amb-tide-demo__title {
  margin: 0.875rem 0 0; font: 600 clamp(1.875rem, 1.2rem + 2.6vw, 3rem)/1.05 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-tide-demo__head { max-width: 38rem; }

/* Buttons */
.amb-tide-demo__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.amb-tide-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem;
  border-radius: var(--radius-full); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-tide-demo__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-tide-demo__btn:hover { transform: translateY(-2px); }
.amb-tide-demo__btn:active { transform: scale(0.97); }
.amb-tide-demo__btn--primary {
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 14px 30px -14px var(--primary);
}
.amb-tide-demo__btn--ghost { background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-md); }
.amb-tide-demo a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.amb-tide-demo__hint {
  display: flex; align-items: center; gap: 0.5rem; margin: 3rem 0 0;
  font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-tide-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* Service cards: an opaque surface, so muted copy keeps 4.7:1 over any water */
.amb-tide-demo__cards {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr)); gap: 1rem;
  margin: 2.5rem 0 0; padding: 0; list-style: none;
}
.amb-tide-demo__card {
  position: relative; display: grid; align-content: start; gap: 0.5rem; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-lg);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-tide-demo__card:hover { transform: translateY(-4px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl); }
.amb-tide-demo__card h3 { margin: 0.75rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-tide-demo__card h3 a { color: inherit; text-decoration: none; }
.amb-tide-demo__card h3 a::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-2xl); }
.amb-tide-demo__card h3 a:focus-visible { outline: none; }
.amb-tide-demo__card h3 a:focus-visible::after { outline: 2px solid var(--primary); outline-offset: 3px; }
.amb-tide-demo__card p { margin: 0; color: var(--text-muted); line-height: 1.55; }
.amb-tide-demo__card .amb-tide-demo__price { margin-top: 0.75rem; color: var(--text-main); font: 500 0.8125rem var(--font-mono); }
.amb-tide-demo__price b { font-size: 1.125rem; font-weight: 600; }
.amb-tide-demo__icon {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-lg); color: var(--primary-hover);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 14%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 16%, var(--surface-light)));
  box-shadow: var(--highlight);
}
.amb-tide-demo__icon svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }

/* Proof: stats and a review */
.amb-tide-demo__proof { display: grid; gap: 2.5rem; align-items: center; }
.amb-tide-demo__stats { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem 1.25rem; margin: 2rem 0 0; }
.amb-tide-demo__stats div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.375rem; padding-top: 1rem; border-top: 1px solid color-mix(in srgb, var(--text-main) 16%, transparent); }
.amb-tide-demo__stats dt { font-size: 0.875rem; line-height: 1.45; }
.amb-tide-demo__stats dd { margin: 0; font: 600 clamp(2rem, 1.5rem + 2vw, 2.75rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-tide-demo__quote {
  margin: 0; padding: 1.75rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.amb-tide-demo__stars { display: flex; gap: 0.125rem; color: var(--accent); }
.amb-tide-demo__stars svg { fill: currentColor; stroke: currentColor; stroke-width: 1; stroke-linejoin: round; }
.amb-tide-demo__quote blockquote { margin: 1rem 0 0; }
.amb-tide-demo__quote blockquote p { margin: 0; font: 500 clamp(1.125rem, 1rem + 0.6vw, 1.375rem)/1.45 var(--font-display); letter-spacing: -0.01em; }
.amb-tide-demo__quote figcaption { display: flex; align-items: center; gap: 0.75rem; margin-top: 1.5rem; color: var(--text-muted); font-size: 0.875rem; }
.amb-tide-demo__quote strong { color: var(--text-main); }
.amb-tide-demo__avatar {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-size: 0.75rem; font-weight: 700;
}

/* Closing CTA: content clears the high-water mark */
.amb-tide-demo__cta { padding-bottom: calc(35vh + 3rem); padding-bottom: calc(35svh + 3rem); text-align: center; }
.amb-tide-demo__cta .amb-tide-demo__eyebrow { justify-content: center; }
.amb-tide-demo__cta .amb-tide-demo__display, .amb-tide-demo__cta .amb-tide-demo__lead { margin-inline: auto; }
.amb-tide-demo__cta .amb-tide-demo__actions { justify-content: center; }

@media (min-width: 768px) {
  .amb-tide-demo__proof { grid-template-columns: 1.1fr 0.9fr; gap: 4rem; }
  .amb-tide-demo__quote { padding: 2.25rem; }
}
```

## JS

```js
document.querySelectorAll('.amb-tide').forEach((layer) => {
  const page = layer.classList.contains('amb-tide--page'), host = page ? document.documentElement : layer.parentElement;
  const $ = (sel) => [...layer.querySelectorAll(sel)];
  const [frame] = $('.amb-tide__frame'), [svg] = $('.amb-tide__waves'), [ring] = $('.amb-tide__ring');
  const paths = $('.amb-tide__wave'), bubbles = $('.amb-tide__bubble'), drops = $('.amb-tide__drop');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  // Per wave: mean line (share of the band), resting amplitude (px), wavenumber (rad/px), phase speed
  const WAVES = [[0.43, 7, 0.0062, 0.7], [0.52, 6, 0.0081, -0.9], [0.6, 5, 0.0105, 1.2]];
  let W = 0, H = 0, FH = 0, VH = 0, raf = 0, last = 0, scrolled = 0, visible = page, pos = null, phase = 0;
  let vel = 0, level = 0, s = 0, sv = 0, spawn = 0, next = 0, splashed = false;
  const f = (n) => n.toFixed(1);
  const rand = (a, b) => a + Math.random() * (b - a);
  // Pooled one-shots: transform + opacity only; back to visibility: hidden when they finish
  const play = (el, frames, opts) => el.animate(frames.map((k) => ({ ...k, visibility: 'visible' })), opts);

  // Three smooth wave paths: phase from scroll, amplitude and tilt from the slosh spring
  const draw = () => {
    const n = Math.max(12, Math.min(40, Math.round(W / 36)));
    paths.forEach((path, i) => {
      const [mean, amp, k, speed] = WAVES[i], a = amp * (1 + 2.2 * Math.abs(s)), tilt = s * (12 + 6 * i), ph = phase * speed;
      const pt = (j) => { const x = (j / n) * W; return [x, H * mean + a * (0.65 * Math.sin(x * k + ph) + 0.35 * Math.sin(x * k * 2.3 - ph * 1.4 + i)) + tilt * (j / n - 0.5)]; };
      let prev = pt(1), d = `M-2 ${H + 2}L-2 ${f(pt(0)[1])}`;
      for (let j = 1; j < n; j++) {
        const nx = pt(j + 1);
        d += `Q${f(prev[0])} ${f(prev[1])} ${f((prev[0] + nx[0]) / 2)} ${f((prev[1] + nx[1]) / 2)}`;
        prev = nx;
      }
      path.setAttribute('d', `${d}L${W + 2} ${f(prev[1])}L${W + 2} ${H + 2}Z`);
    });
  };

  // A bubble rises from the deep to the surface and pops
  const bubble = () => {
    const el = bubbles[next++ % bubbles.length];
    if (!el || el.getAnimations().length) return;
    const rise = FH * (0.06 + 0.29 * level), y0 = -rand(0, rise * 0.35), x = rand(0, W), w = rand(-9, 9), sc = rand(0.5, 1.3);
    play(el, [
      { transform: `translate(${x}px, ${y0}px) scale(${sc * 0.4})`, opacity: 0 },
      { transform: `translate(${x + w}px, ${(y0 - rise) / 2}px) scale(${sc})`, opacity: 0.9, offset: 0.55 },
      { transform: `translate(${x - w / 2}px, ${10 - rise}px) scale(${sc * 1.3})`, opacity: 0 },
    ], { duration: rand(1100, 1700), easing: 'cubic-bezier(0.45, 0, 0.75, 1)' });
  };

  // One-shot splash at the high-water mark: a surface ring and a crown of droplets (under 1s)
  const splash = () => {
    play(ring, [{ transform: 'scale(0.12, 0.3)', opacity: 1 }, { transform: 'scale(1)', opacity: 0 }], { duration: 900, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' });
    drops.forEach((el, i) => {
      const t = i / (drops.length - 1) - 0.5, peak = 45 + rand(0, 80) * (1 - Math.abs(t)), dx = t * 240 + rand(-15, 15);
      play(el, [
        { transform: 'translate(0, 0) scale(0.4)', opacity: 0, easing: 'cubic-bezier(0.2, 0.7, 0.4, 1)' },
        { transform: `translate(${dx * 0.55}px, ${-peak}px) scale(1)`, opacity: 1, offset: 0.45, easing: 'cubic-bezier(0.6, 0, 0.8, 0.5)' },
        { transform: `translate(${dx}px, ${peak * 0.2}px) scale(0.6)`, opacity: 0 },
      ], { duration: rand(800, 950), delay: Math.abs(t) * 60 });
    });
  };

  const tick = (now) => {
    raf = 0;
    const r = host.getBoundingClientRect(), y = -r.top; // the one layout read per frame
    const dt = last ? Math.min(0.05, Math.max(0.004, (now - last) / 1000)) : 1 / 60, p = Math.min(1, Math.max(0, y / Math.max(1, r.height - VH)));
    if (pos === null) { pos = y; level = p; } // first frame in view: snap, no fake velocity
    vel += ((y - pos) / dt - vel) * 0.25; // smoothed scroll speed, px/s
    last = now; pos = y; phase = y * 0.006;
    level += (p - level) * Math.min(1, dt * 7);
    sv += ((Math.max(-1, Math.min(1, vel / 2400)) - s) * 60 - sv * 7) * dt; s += sv * dt; // damped slosh spring
    layer.style.setProperty('--amb-tide-p', level.toFixed(4));
    draw();
    for (spawn += Math.min(Math.abs(vel), 3000) * dt / 200; spawn >= 1; spawn--) bubble();
    if (p > 0.985 && vel > 30 && !splashed) { splashed = true; sv += 2.4; splash(); }
    if (p < 0.85) splashed = false;
    const moving = now - scrolled < 150 || Math.abs(vel) > 3 || Math.abs(s) > 0.004 || Math.abs(sv) > 0.02 || Math.abs(p - level) > 0.0005;
    if (moving && visible && document.visibilityState === 'visible') raf = requestAnimationFrame(tick);
    else { vel = s = sv = spawn = 0; layer.classList.remove('is-moving'); }
  };

  // Scroll wakes the loop; it stops itself once everything has settled
  const wake = () => {
    if (raf || !visible || reduce.matches || document.visibilityState !== 'visible') return;
    layer.classList.add('is-moving'); last = 0; raf = requestAnimationFrame(tick);
  };
  new ResizeObserver(() => {
    ({ width: W, height: H } = svg.getBoundingClientRect()); FH = frame.clientHeight; VH = innerHeight;
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`); draw();
  }).observe(frame);
  addEventListener('scroll', () => { scrolled = performance.now(); wake(); }, { passive: true });
  document.addEventListener('visibilitychange', wake);
  if (page) wake();
  else new IntersectionObserver(([e]) => { visible = e.isIntersecting; pos = null; wake(); }).observe(host);
});
```

## Notes

- **Placement.** The layer is decorative (`aria-hidden`, `pointer-events: none`). Section placement is the default. Make it the first child of a `position: relative; isolation: isolate` section; a sticky, viewport-tall frame inside keeps the water at the bottom of the screen while that section scrolls past, and progress runs from the section's top to its end. Add `.amb-tide--page` to fix it behind the whole page instead: progress then follows the document, and every section above it needs a transparent background. Use one ambient background per page, and give the host at least a viewport of height.
- **Contrast.** The water is 12–24% tints of `--primary`/`--primary-2` on `--surface-light`. Worst case in the demo: body copy in `--text-main` over the deepest tint is 10.4:1, the `--primary-hover` eyebrows are 4.75:1, and the gradient end of the display headings is 3.96:1 (large text only). `--text-muted` drops to 3.4:1 over the water, so it's used only inside the opaque white cards (4.76:1). Set `--amb-tide-scrim` (0–1) on the layer or any ancestor to lay a `--surface-light` veil over the water.
- **Performance.** One rAF loop per layer. It runs only while the section is on screen and the tab is visible, reads one `getBoundingClientRect` per frame, and redraws three paths of up to 40 points. It stops once scroll speed, the slosh spring (stiffness 60, damping 7) and the level have all settled, which takes under 2s. Bubbles (a pool of 12) and the splash (10 drops and a ring) are transform/opacity Web Animations that sit at `visibility: hidden` when idle. `will-change` is applied only while the loop runs. There's no blur and no canvas.
- **Motion budget.** Nothing moves on its own: the waves freeze when scrolling stops, bubbles spawn only from scroll speed, and the splash (under 1s) plays once on reaching the end and re-arms after you scroll back above 85%. No pause control is needed.
- **Reduced motion and no JS.** The water is a still composition at mid level (CSS default `--amb-tide-p: 0.5`): the waves are drawn once to the real width, with no bubbles, splash or loop. Without JS, the authored SVG paths stretch to fit. `@media (scripting: enabled)` starts the level low only when JS will drive it. The level uses container query units (`cqh`) and falls back to `vh`.
- **Retheme.** Change the four `--amb-tide-*` tints (or `--primary`/`--primary-2`), then re-check text over `--amb-tide-deep`. The wave shapes live in the `WAVES` table: mean line, resting amplitude, wavenumber and phase speed.
