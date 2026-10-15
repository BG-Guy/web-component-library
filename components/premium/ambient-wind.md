# Scroll Wind

A seasonal particle layer on canvas with three themes, set with `data-amb-wind-theme`: `leaves` (autumn gutter season, light), `snow` (winter heating, cool light) and `sparks` (electrical, designed for a deep section). Particles fall gently at idle. Scrolling raises a gust in proportion to scroll speed: scroll down and they lift and blow sideways with turbulence, leaves flutter faster, sparks stretch into streaks, then the gust dies away. Counts scale with screen area (up to 60, or 25 on phones), and a pause control in the page content stops the idle fall. Depends on `tokens/variables.css`.

**Motion:** idle fall and sway (continuous, with a pause control) · scroll gust with a fast attack and about 0.6s decay · leaf flutter (scaleX from a cosine) · spark flicker · canvas fade-in (`--dur-5`, `--ease-out`) · theme change cross-tints the demo surface over `--dur-5` (registered colours).

## HTML

```html
<div class="amb-wind-demo">
  <div class="amb-wind" data-amb-wind-theme="leaves" aria-hidden="true">
    <div class="amb-wind__frame">
      <svg class="amb-wind__still" viewBox="0 0 1200 800" preserveAspectRatio="xMidYMid slice" focusable="false">
        <g class="amb-wind__still-leaves">
          <path class="amb-wind__p1" transform="translate(24 69) rotate(104) scale(0.95)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p2" transform="translate(1059 109) rotate(119) scale(1.33)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p3" transform="translate(350 164) rotate(246) scale(1.25)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p1" transform="translate(1097 208) rotate(135) scale(1.3)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p2" transform="translate(326 256) rotate(246) scale(1.13)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p3" transform="translate(1142 341) rotate(44) scale(1.16)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p1" transform="translate(423 392) rotate(232) scale(1.2)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p2" transform="translate(1138 456) rotate(134) scale(1.03)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p3" transform="translate(386 488) rotate(55) scale(1.01)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p1" transform="translate(929 542) rotate(337) scale(1.19)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p2" transform="translate(339 621) rotate(21) scale(0.99)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p3" transform="translate(986 662) rotate(152) scale(0.94)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
          <path class="amb-wind__p1" transform="translate(417 699) rotate(132) scale(1.04)" d="M-12 0C-4.5-9.5 6.2-6.7 12.3 0C6.2 6.7-4.5 9.5-12 0Z" />
        </g>
        <g class="amb-wind__still-snow">
          <circle class="amb-wind__p1" cx="24" cy="50" r="3.7" /><circle class="amb-wind__p2" cx="764" cy="102" r="4.1" />
          <circle class="amb-wind__p3" cx="248" cy="123" r="4.4" /><circle class="amb-wind__p1" cx="866" cy="149" r="5.4" />
          <circle class="amb-wind__p2" cx="85" cy="191" r="4.9" /><circle class="amb-wind__p3" cx="1101" cy="227" r="2.8" />
          <circle class="amb-wind__p1" cx="118" cy="277" r="4.9" /><circle class="amb-wind__p2" cx="984" cy="303" r="3.4" />
          <circle class="amb-wind__p3" cx="157" cy="352" r="2.5" /><circle class="amb-wind__p1" cx="827" cy="379" r="5.4" />
          <circle class="amb-wind__p2" cx="30" cy="407" r="6" /><circle class="amb-wind__p3" cx="970" cy="432" r="4.9" />
          <circle class="amb-wind__p1" cx="438" cy="477" r="6.1" /><circle class="amb-wind__p2" cx="752" cy="529" r="5.7" />
          <circle class="amb-wind__p3" cx="434" cy="547" r="3.2" /><circle class="amb-wind__p1" cx="1089" cy="610" r="5.4" />
          <circle class="amb-wind__p2" cx="456" cy="640" r="4.2" /><circle class="amb-wind__p3" cx="854" cy="669" r="2.6" />
          <circle class="amb-wind__p1" cx="435" cy="713" r="3.9" /><circle class="amb-wind__p2" cx="1122" cy="716" r="5.2" />
        </g>
        <g class="amb-wind__still-sparks">
          <path class="amb-wind__p1" transform="translate(24 33) rotate(79) scale(1.03)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p2" transform="translate(854 93) rotate(64) scale(1.07)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p3" transform="translate(293 172) rotate(101) scale(1.27)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p1" transform="translate(792 244) rotate(71) scale(0.81)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p2" transform="translate(213 279) rotate(101) scale(1.02)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p3" transform="translate(1004 364) rotate(87) scale(0.94)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p1" transform="translate(224 397) rotate(66) scale(0.72)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p2" transform="translate(989 457) rotate(107) scale(1.02)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p3" transform="translate(40 516) rotate(106) scale(1.03)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p1" transform="translate(982 588) rotate(100) scale(0.94)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p2" transform="translate(319 656) rotate(91) scale(0.9)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
          <path class="amb-wind__p3" transform="translate(1169 719) rotate(86) scale(0.91)" d="M-26 0L10-2.4A2.4 2.4 0 0 1 10 2.4Z" />
        </g>
      </svg>
      <canvas class="amb-wind__canvas"></canvas>
    </div>
  </div>

  <section class="amb-wind-demo__hero" aria-labelledby="amb-wind-title">
    <div class="amb-wind-demo__inner">
      <p class="amb-wind-demo__eyebrow">Brand Home Services · Springfield</p>
      <h2 id="amb-wind-title" class="amb-wind-demo__display">Ready for whatever <span>the season blows in.</span></h2>
      <p class="amb-wind-demo__lead">Gutters cleared before the leaves fall, furnaces tuned before the frost, and wiring checked before the storms.</p>
      <div class="amb-wind-demo__actions">
        <a class="amb-wind-demo__btn amb-wind-demo__btn--primary" href="#amb-wind-book">
          Book a seasonal visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-wind-demo__btn amb-wind-demo__btn--ghost" href="tel:+15555550123">(555) 555-0123</a>
      </div>
      <div class="amb-wind-demo__controls">
        <div class="amb-wind-demo__themes" role="group" aria-label="Background theme">
          <button type="button" aria-pressed="true" data-amb-wind-set-theme="leaves">
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 19c0-8.5 5.5-13.5 14-14 0 9-5.5 14-14 14z" /><path d="M5 19 13 11" /></svg>
            Leaves
          </button>
          <button type="button" aria-pressed="false" data-amb-wind-set-theme="snow">
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9M9.5 4.5 12 6l2.5-1.5M9.5 19.5 12 18l2.5 1.5" /></svg>
            Snow
          </button>
          <button type="button" aria-pressed="false" data-amb-wind-set-theme="sparks">
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M13 3 5 14h6l-1 7 8-11h-6z" /></svg>
            Sparks
          </button>
        </div>
        <button class="amb-wind__pause" type="button" aria-pressed="false" hidden>
          <span class="amb-wind__sr">Pause animation</span>
          <svg class="amb-wind__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
          <svg class="amb-wind__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
        </button>
      </div>
      <p class="amb-wind-demo__hint">Scroll quickly to raise a gust</p>
    </div>
  </section>

  <section class="amb-wind-demo__section" aria-labelledby="amb-wind-services">
    <div class="amb-wind-demo__inner">
      <header class="amb-wind-demo__head">
        <p class="amb-wind-demo__eyebrow">Seasonal services</p>
        <h2 id="amb-wind-services" class="amb-wind-demo__title">One visit a season keeps the house running.</h2>
      </header>
      <ul class="amb-wind-demo__cards" role="list">
        <li class="amb-wind-demo__card">
          <span class="amb-wind-demo__tag">Autumn</span>
          <h3><a href="#amb-wind-book">Gutter cleaning</a></h3>
          <p>Cleared, flushed and checked before the leaves pile up.</p>
          <p class="amb-wind-demo__price">from <b>$129</b></p>
        </li>
        <li class="amb-wind-demo__card">
          <span class="amb-wind-demo__tag">Winter</span>
          <h3><a href="#amb-wind-book">Furnace tune-up</a></h3>
          <p>Cleaned, tested and safety-checked before the first frost.</p>
          <p class="amb-wind-demo__price">from <b>$89</b></p>
        </li>
        <li class="amb-wind-demo__card">
          <span class="amb-wind-demo__tag">All year</span>
          <h3><a href="#amb-wind-book">Electrical safety check</a></h3>
          <p>Panel, outlets and surge protection inspected in an hour.</p>
          <p class="amb-wind-demo__price">from <b>$149</b></p>
        </li>
        <li class="amb-wind-demo__card">
          <span class="amb-wind-demo__tag">Spring</span>
          <h3><a href="#amb-wind-book">Storm prep</a></h3>
          <p>Shingles, downspouts and the sump pump readied for heavy rain.</p>
          <p class="amb-wind-demo__price">from <b>$99</b></p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-wind-demo__section" aria-labelledby="amb-wind-proof">
    <div class="amb-wind-demo__inner amb-wind-demo__proof">
      <div>
        <p class="amb-wind-demo__eyebrow">Season after season</p>
        <h2 id="amb-wind-proof" class="amb-wind-demo__title">We remember, so you don't have to.</h2>
        <dl class="amb-wind-demo__stats">
          <div><dt>homes on a seasonal plan</dt><dd>3,200</dd></div>
          <div><dt>average rating, 900+ reviews</dt><dd>4.9</dd></div>
          <div><dt>reminder before each season</dt><dd>1 text</dd></div>
        </dl>
      </div>
      <figure class="amb-wind-demo__quote">
        <blockquote><p>"They text me before I've even thought about the gutters. Fifteen years in this house and the basement has never been wetter than a sponge."</p></blockquote>
        <figcaption><strong>Marcus T.</strong> · Riverside</figcaption>
      </figure>
    </div>
  </section>

  <section class="amb-wind-demo__section amb-wind-demo__cta" id="amb-wind-book" aria-labelledby="amb-wind-cta">
    <div class="amb-wind-demo__inner">
      <h2 id="amb-wind-cta" class="amb-wind-demo__display amb-wind-demo__display--sm">Book once. <span>We'll remind you every season.</span></h2>
      <div class="amb-wind-demo__actions">
        <a class="amb-wind-demo__btn amb-wind-demo__btn--primary" href="mailto:hello@example.com">
          Start a seasonal plan
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-wind-demo__btn amb-wind-demo__btn--ghost" href="tel:+15555550123">Call (555) 555-0123</a>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Layer: behind its section by default, behind the whole page with --page.
   Each theme sets three particle colours, a vein/rim colour and an opacity cap for the canvas. */
.amb-wind {
  --amb-wind-c1: color-mix(in srgb, var(--accent) 85%, var(--surface-light));
  --amb-wind-c2: color-mix(in srgb, var(--accent) 50%, var(--danger));
  --amb-wind-c3: color-mix(in srgb, var(--success) 55%, var(--accent));
  --amb-wind-vein: color-mix(in srgb, var(--surface-light) 55%, transparent);
  --amb-wind-cap: 0.7;
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-wind[data-amb-wind-theme="snow"] {
  --amb-wind-c1: var(--surface-light);
  --amb-wind-c2: color-mix(in srgb, var(--primary) 12%, var(--surface-light));
  --amb-wind-c3: color-mix(in srgb, var(--primary-2) 8%, var(--surface-light));
  --amb-wind-vein: color-mix(in srgb, var(--primary) 45%, transparent);
  --amb-wind-cap: 0.9;
}
.amb-wind[data-amb-wind-theme="sparks"] {
  --amb-wind-c1: color-mix(in srgb, var(--accent) 85%, var(--surface-light));
  --amb-wind-c2: color-mix(in srgb, var(--primary) 60%, var(--text-inverse));
  --amb-wind-c3: color-mix(in srgb, var(--accent) 60%, var(--danger));
  --amb-wind-cap: 0.5;
}
.amb-wind--page { position: fixed; }

/* A viewport-tall frame that sticks while its section scrolls past */
.amb-wind__frame { position: sticky; top: 0; height: 100vh; height: 100svh; max-height: 100%; overflow: hidden; }
.amb-wind__frame::after { /* contrast guard: a veil of the page colour, 0–1 */
  content: ""; position: absolute; inset: 0;
  background: var(--surface-light); opacity: var(--amb-wind-scrim, 0);
}
.amb-wind[data-amb-wind-theme="sparks"] .amb-wind__frame::after { background: var(--surface-deep); }
/* The cap bounds every pixel: particles never exceed it, even where they overlap */
.amb-wind__canvas, .amb-wind__still { position: absolute; inset: 0; width: 100%; height: 100%; opacity: var(--amb-wind-cap); }

/* Still scatter: no JS or reduced motion; one group per theme */
.amb-wind__still g { display: none; }
.amb-wind:not([data-amb-wind-theme="snow"]):not([data-amb-wind-theme="sparks"]) .amb-wind__still-leaves,
.amb-wind[data-amb-wind-theme="snow"] .amb-wind__still-snow,
.amb-wind[data-amb-wind-theme="sparks"] .amb-wind__still-sparks { display: inline; }
.amb-wind__p1 { fill: var(--amb-wind-c1); }
.amb-wind__p2 { fill: var(--amb-wind-c2); }
.amb-wind__p3 { fill: var(--amb-wind-c3); }
.amb-wind__still-snow circle { stroke: var(--amb-wind-vein); stroke-width: 1; }
.amb-wind:not(.is-live) .amb-wind__canvas, .amb-wind.is-live .amb-wind__still { display: none; }
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  /* JS will animate: hold the still back so it doesn't flash (it returns after 2s if JS never runs) */
  .amb-wind:not(.is-live) .amb-wind__still { opacity: 0; animation: amb-wind-failsafe 0.4s 2s forwards; }
  .amb-wind.is-live .amb-wind__canvas { animation: amb-wind-in var(--dur-5) var(--ease-out) both; }
}
@keyframes amb-wind-failsafe { to { opacity: var(--amb-wind-cap); } }
@keyframes amb-wind-in { from { opacity: 0; } }

/* Pause control: lives in the page content (the layer itself takes no pointer events) */
.amb-wind__pause {
  display: grid; place-items: center; flex: none; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: color-mix(in srgb, currentColor 8%, transparent); color: inherit;
  box-shadow: inset 0 0 0 1px color-mix(in srgb, currentColor 22%, transparent);
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.amb-wind__pause:hover { background: color-mix(in srgb, currentColor 14%, transparent); }
.amb-wind__pause:active { transform: scale(0.94); }
.amb-wind__pause:focus-visible { outline: 2px solid currentColor; outline-offset: 3px; }
.amb-wind__pause[hidden] { display: none; }
.amb-wind__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-wind__icon-play, .amb-wind__pause[aria-pressed="true"] .amb-wind__icon-pause { display: none; }
.amb-wind__pause[aria-pressed="true"] .amb-wind__icon-play { display: block; }
.amb-wind__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Demo page: a seasonal services page whose surface follows the theme */
@property --amb-wind-sky { syntax: "<color>"; inherits: true; initial-value: transparent; }
@property --amb-wind-ground { syntax: "<color>"; inherits: true; initial-value: transparent; }
.amb-wind-demo {
  --amb-wind-sky: color-mix(in srgb, var(--accent) 14%, var(--surface-light));
  --amb-wind-ground: color-mix(in srgb, var(--accent) 5%, var(--surface-light));
  --amb-wind-fg: var(--text-main);
  --amb-wind-soft: var(--text-muted);
  --amb-wind-card: var(--surface-light);
  --amb-wind-line: var(--border-subtle);
  --amb-wind-focus: var(--primary);
  position: relative; isolation: isolate; color: var(--amb-wind-fg); font-family: var(--font-sans);
  background: linear-gradient(var(--amb-wind-sky), var(--amb-wind-ground) 44rem) var(--amb-wind-ground);
  transition: --amb-wind-sky var(--dur-5) var(--ease-out), --amb-wind-ground var(--dur-5) var(--ease-out), color var(--dur-4) var(--ease-out);
}
.amb-wind-demo:has(.amb-wind[data-amb-wind-theme="snow"]) {
  --amb-wind-sky: color-mix(in srgb, var(--primary) 18%, var(--surface-light));
  --amb-wind-ground: color-mix(in srgb, var(--primary) 7%, var(--surface-light));
}
.amb-wind-demo:has(.amb-wind[data-amb-wind-theme="sparks"]) {
  --amb-wind-sky: color-mix(in srgb, var(--primary) 22%, var(--surface-deep));
  --amb-wind-ground: var(--surface-deep);
  --amb-wind-fg: var(--text-inverse);
  --amb-wind-soft: var(--text-inverse-muted);
  --amb-wind-card: color-mix(in srgb, var(--surface-deep) 92%, var(--text-inverse));
  --amb-wind-line: var(--border-inverse);
  --amb-wind-focus: var(--text-inverse);
}
.amb-wind-demo__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.amb-wind-demo__hero { display: grid; align-items: center; min-height: 92vh; min-height: 92svh; padding-block: 4rem; }
.amb-wind-demo__section { padding-block: clamp(4rem, 9vw, 6.5rem); }
.amb-wind-demo__eyebrow {
  display: flex; align-items: center; gap: 0.625rem; margin: 0;
  font: 600 0.75rem/1.3 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-wind-demo__eyebrow::before { content: ""; flex: none; width: 1.5rem; height: 2px; border-radius: 2px; background: linear-gradient(90deg, var(--accent), var(--danger)); }
.amb-wind-demo__display {
  max-width: 15ch; margin: 1.25rem 0 0; font: 600 clamp(2.5rem, 1.3rem + 5vw, 5rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-wind-demo__display span { color: color-mix(in srgb, var(--amb-wind-fg) 72%, var(--danger)); }
.amb-wind-demo__display--sm { max-width: 18ch; font-size: clamp(2.25rem, 1.4rem + 3.6vw, 3.75rem); }
.amb-wind-demo__lead { max-width: 34rem; margin: 1.5rem 0 0; font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.amb-wind-demo__title {
  margin: 0.875rem 0 0; font: 600 clamp(1.875rem, 1.2rem + 2.6vw, 3rem)/1.05 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-wind-demo__head { max-width: 38rem; }
.amb-wind-demo a:focus-visible, .amb-wind-demo__themes button:focus-visible { outline: 2px solid var(--amb-wind-focus); outline-offset: 3px; }

/* Buttons */
.amb-wind-demo__actions { display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 2rem; }
.amb-wind-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem;
  border-radius: var(--radius-full); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-4) var(--ease-out), color var(--dur-4) var(--ease-out);
}
.amb-wind-demo__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-wind-demo__btn:hover { transform: translateY(-2px); }
.amb-wind-demo__btn:active { transform: scale(0.97); }
.amb-wind-demo__btn--primary { background: var(--amb-wind-fg); color: var(--amb-wind-card); box-shadow: var(--shadow-lg); }
.amb-wind-demo__btn--ghost { background: var(--amb-wind-card); color: var(--amb-wind-fg); box-shadow: inset 0 0 0 1px var(--amb-wind-line), var(--shadow-sm); }

/* Theme switcher (demo) and the pause button */
.amb-wind-demo__controls { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem; margin-top: 2.25rem; }
.amb-wind-demo__themes {
  display: inline-flex; gap: 0.25rem; padding: 0.25rem; border-radius: var(--radius-full);
  background: var(--amb-wind-card); box-shadow: inset 0 0 0 1px var(--amb-wind-line), var(--shadow-md);
}
.amb-wind-demo__themes button {
  display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.5rem; padding: 0 0.75rem; border: 0; border-radius: var(--radius-full);
  background: transparent; color: var(--amb-wind-soft); font: 600 0.8125rem var(--font-sans); cursor: pointer;
  transition: background-color var(--dur-3) var(--ease-out), color var(--dur-3) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
.amb-wind-demo__themes button svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-wind-demo__themes button:hover { color: var(--amb-wind-fg); }
.amb-wind-demo__themes button:active { transform: scale(0.95); }
.amb-wind-demo__themes button[aria-pressed="true"] { background: var(--amb-wind-fg); color: var(--amb-wind-card); }
@media (scripting: none) { .amb-wind-demo__themes { display: none; } } /* the picks need JS */
.amb-wind-demo__hint { margin: 1.25rem 0 0; font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }

/* Service cards: opaque surfaces, so muted copy keeps its contrast over particles */
.amb-wind-demo__cards {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr)); gap: 1rem;
  margin: 2.5rem 0 0; padding: 0; list-style: none;
}
.amb-wind-demo__card {
  position: relative; display: grid; align-content: start; gap: 0.5rem; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: var(--amb-wind-card); box-shadow: inset 0 0 0 1px var(--amb-wind-line), var(--shadow-lg);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-4) var(--ease-out);
}
.amb-wind-demo__card:hover { transform: translateY(-4px); }
.amb-wind-demo__card h3 { margin: 0.5rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-wind-demo__card h3 a { color: inherit; text-decoration: none; }
.amb-wind-demo__card h3 a::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-2xl); }
.amb-wind-demo__card h3 a:focus-visible { outline: none; }
.amb-wind-demo__card h3 a:focus-visible::after { outline: 2px solid var(--amb-wind-focus); outline-offset: 3px; }
.amb-wind-demo__card p { margin: 0; color: var(--amb-wind-soft); line-height: 1.55; }
.amb-wind-demo__card .amb-wind-demo__price { margin-top: 0.75rem; color: var(--amb-wind-fg); font: 500 0.8125rem var(--font-mono); }
.amb-wind-demo__price b { font-size: 1.125rem; font-weight: 600; }
.amb-wind-demo__tag {
  justify-self: start; padding: 0.25rem 0.625rem; border-radius: var(--radius-full);
  box-shadow: inset 0 0 0 1px var(--amb-wind-line); font: 600 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}

/* Proof */
.amb-wind-demo__proof { display: grid; gap: 2.5rem; align-items: center; }
.amb-wind-demo__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; margin: 2rem 0 0; }
.amb-wind-demo__stats div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.375rem; padding-top: 1rem; border-top: 1px solid color-mix(in srgb, currentColor 18%, transparent); }
.amb-wind-demo__stats dt { font-size: 0.8125rem; line-height: 1.4; }
.amb-wind-demo__stats dd { margin: 0; font: 600 clamp(1.5rem, 1.2rem + 1.4vw, 2.25rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-wind-demo__quote { margin: 0; padding: 1.75rem; border-radius: var(--radius-2xl); background: var(--amb-wind-card); box-shadow: inset 0 0 0 1px var(--amb-wind-line), var(--shadow-xl); }
.amb-wind-demo__quote blockquote { margin: 0; }
.amb-wind-demo__quote blockquote p { margin: 0; font: 500 clamp(1.125rem, 1rem + 0.6vw, 1.375rem)/1.45 var(--font-display); letter-spacing: -0.01em; }
.amb-wind-demo__quote figcaption { margin-top: 1.25rem; color: var(--amb-wind-soft); font-size: 0.875rem; }
.amb-wind-demo__quote strong { color: var(--amb-wind-fg); }
.amb-wind-demo__cta { padding-bottom: clamp(6rem, 18vh, 10rem); }

@media (min-width: 768px) {
  .amb-wind-demo__proof { grid-template-columns: 1.1fr 0.9fr; gap: 4rem; }
}
```

## JS

```js
document.querySelectorAll('.amb-wind').forEach((layer) => {
  const page = layer.classList.contains('amb-wind--page'), host = page ? document.documentElement : layer.parentElement;
  const scope = page ? document : host; // the pause button and theme picks live in the content, not in the layer
  const canvas = layer.querySelector('.amb-wind__canvas'), ctx = canvas.getContext('2d');
  const pause = scope.querySelector('.amb-wind__pause'), picks = [...scope.querySelectorAll('[data-amb-wind-set-theme]')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)'), coarse = matchMedia('(pointer: coarse)');
  // Per theme: idle fall and sway (px/s), gust push and lift (px/s at full gust), spin and flutter (rad/s)
  const THEMES = {
    leaves: { fall: 42, sway: 28, push: 320, lift: 260, spin: 1.2, flutter: 2.4 },
    snow: { fall: 26, sway: 14, push: 240, lift: 220, spin: 0, flutter: 0 },
    sparks: { fall: 70, sway: 12, push: 360, lift: 280, spin: 0, flutter: 0 },
  };
  const live = !!ctx && !reduce.matches;
  let theme = 'leaves', sprites = [], parts = [], W = 0, H = 0, dpr = 1;
  let raf = 0, last = 0, pos = null, vel = 0, gust = 0, dir = 1, visible = page;

  // Optional theme picks: buttons with data-amb-wind-set-theme and aria-pressed
  const sync = () => picks.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.ambWindSetTheme === layer.dataset.ambWindTheme)));
  picks.forEach((b) => b.addEventListener('click', () => {
    layer.dataset.ambWindTheme = b.dataset.ambWindSetTheme;
    sync();
    if (live) { build(); draw(); }
  }));
  sync();
  if (!live) return; // reduced motion or no canvas: the still scatter stays and the pause button stays hidden

  // Sprites: drawn once per theme and size, in colours read from the tokens
  const ink = (name) => { canvas.style.color = `var(${name})`; return getComputedStyle(canvas).color; };
  const sprite = (w, h, paint) => { const c = document.createElement('canvas'); c.width = w; c.height = h; paint(c.getContext('2d'), w, h); return c; };
  const build = () => {
    theme = THEMES[layer.dataset.ambWindTheme] ? layer.dataset.ambWindTheme : 'leaves';
    const s = Math.round(28 * dpr), vein = ink('--amb-wind-vein'), glow = Math.min(8, 4 * dpr);
    sprites = ['--amb-wind-c1', '--amb-wind-c2', '--amb-wind-c3'].map((name) => {
      const col = ink(name);
      if (theme === 'sparks') return sprite(s * 2, s / 2, (g, w, h) => { // tapered streak, head on the right, soft glow
        Object.assign(g, { fillStyle: col, shadowColor: col, shadowBlur: glow });
        g.beginPath(); g.moveTo(w * 0.06, h / 2); g.lineTo(w * 0.86, h * 0.34);
        g.arc(w * 0.86, h / 2, h * 0.16, -Math.PI / 2, Math.PI / 2); g.closePath(); g.fill();
      });
      if (theme === 'snow') return sprite(s, s, (g) => { // soft disc with a cool rim
        Object.assign(g, { fillStyle: col, shadowColor: vein, shadowBlur: glow });
        g.beginPath(); g.arc(s / 2, s / 2, s * 0.2, 0, 2 * Math.PI); g.fill();
      });
      return sprite(s, s, (g) => { // leaf with a midrib
        g.translate(s / 2, s / 2);
        g.beginPath(); g.moveTo(-s * 0.42, 0);
        g.bezierCurveTo(-s * 0.16, -s * 0.34, s * 0.22, -s * 0.24, s * 0.44, 0);
        g.bezierCurveTo(s * 0.22, s * 0.24, -s * 0.16, s * 0.34, -s * 0.42, 0);
        g.fillStyle = col; g.fill();
        g.beginPath(); g.moveTo(-s * 0.48, 0); g.lineTo(s * 0.3, 0);
        Object.assign(g, { strokeStyle: vein, lineWidth: s * 0.035, lineCap: 'round' }); g.stroke();
      });
    });
  };
  const spawn = () => ({ x: Math.random() * W, y: Math.random() * H, z: 0.5 + Math.random() * 0.5, c: (Math.random() * 3) | 0,
    ph: Math.random() * 7, fl: Math.random() * 7, rot: Math.random() * 7, sp: Math.random() < 0.5 ? -1 : 1, vx: 0, vy: 0 });

  const draw = (t = 0) => {
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (const p of parts) {
      const img = sprites[p.c], k = p.z * 1.15, x = p.x * dpr, y = p.y * dpr;
      ctx.globalAlpha = 0.3 + 1.4 * (p.z - 0.5); // nearer particles are larger and stronger
      if (theme === 'sparks') { // streak along its velocity, longer when fast, flickering
        const a = Math.atan2(p.vy, p.vx), len = k * Math.min(1.8, 0.5 + Math.hypot(p.vx, p.vy) / 180);
        ctx.globalAlpha *= 0.65 + 0.35 * Math.sin(t * 23 + p.ph * 7);
        ctx.setTransform(Math.cos(a) * len, Math.sin(a) * len, -Math.sin(a) * k, Math.cos(a) * k, x, y);
        ctx.drawImage(img, -img.width * 0.86, -img.height / 2);
      } else { // leaves flutter by flipping scaleX with a cosine; snow just drifts
        const fl = THEMES[theme].flutter ? Math.cos(p.fl) : 1, c = Math.cos(p.rot) * k, s = Math.sin(p.rot) * k;
        ctx.setTransform(c * fl, s * fl, -s, c, x, y);
        ctx.drawImage(img, -img.width / 2, -img.height / 2);
      }
    }
  };

  const step = (dt, t) => {
    const th = THEMES[theme], ease = Math.min(1, dt * 2.4);
    for (const p of parts) {
      const tx = th.sway * Math.sin(t * 0.8 + p.ph) + gust * (dir * th.push + 130 * Math.sin(t * 2.3 + p.ph * 3)); // sideways + turbulence
      const ty = th.fall - gust * (dir * th.lift - 100 * Math.cos(t * 1.9 + p.ph * 2)); // scrolling down lifts them
      p.vx += (tx * p.z - p.vx) * ease; p.vy += (ty * p.z - p.vy) * ease;
      p.x += p.vx * dt; p.y += p.vy * dt;
      p.rot += th.spin * p.sp * (1 + gust * 3) * dt; p.fl += th.flutter * (1 + gust * 3) * dt;
      if (p.y > H + 32 || p.y < -48) Object.assign(p, { y: p.y > 0 ? -32 : H + 32, x: Math.random() * W });
      if (p.x > W + 32) p.x = -32; else if (p.x < -32) p.x = W + 32;
    }
  };

  const tick = (now) => {
    raf = 0;
    const dt = last ? Math.min(0.05, (now - last) / 1000) : 1 / 60, y = -host.getBoundingClientRect().top; // one layout read
    last = now;
    if (pos === null) pos = y;
    vel += ((y - pos) / Math.max(dt, 0.004) - vel) * 0.25; pos = y; // smoothed scroll speed, px/s
    const want = Math.min(1.6, Math.abs(vel) / 1100);
    gust = want > gust ? gust + (want - gust) * Math.min(1, dt * 8) : gust * Math.exp(-dt / 0.6); // fast attack, ~0.6s decay
    if (Math.abs(vel) > 30) dir = Math.sign(vel);
    step(dt, now / 1000);
    draw(now / 1000);
    wake();
  };
  const wake = () => {
    if (raf || !visible || layer.hasAttribute('data-paused') || document.visibilityState !== 'visible') return;
    raf = requestAnimationFrame(tick);
  };
  const resume = () => { if (!raf) { last = 0; pos = null; } wake(); }; // after a pause: no fake gust

  new ResizeObserver(() => {
    dpr = Math.min(devicePixelRatio || 1, coarse.matches ? 1.5 : 2);
    W = canvas.clientWidth; H = canvas.clientHeight;
    canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
    const n = Math.min(coarse.matches || W < 768 ? 25 : 60, Math.round((W * H) / 14000)); // count scales with area
    while (parts.length < n) parts.push(spawn());
    parts.length = n;
    build(); draw();
  }).observe(canvas);

  // Pause control (WCAG 2.2.2): the idle fall never stops on its own
  if (pause) {
    pause.hidden = false;
    pause.addEventListener('click', () => { pause.setAttribute('aria-pressed', String(layer.toggleAttribute('data-paused'))); resume(); });
  }
  document.addEventListener('visibilitychange', resume);
  layer.classList.add('is-live');
  if (page) resume();
  else new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; resume(); }).observe(host);
});
```

## Notes

- **Placement.** The layer is decorative (`aria-hidden`, `pointer-events: none`). By default it's the first child of a `position: relative; isolation: isolate` section, with a sticky, viewport-tall frame holding the canvas. Add `.amb-wind--page` to fix it behind the whole page instead; every section then needs a transparent background, and the pause button and theme picks can live anywhere in the document. Use one ambient background per page, and match the theme to the section: `leaves` and `snow` suit light surfaces, and `sparks` is designed for `--surface-deep`.
- **Pause and motion.** The idle fall loops, so the component needs its pause button: an `aria-pressed` toggle labelled "Pause animation". Because the layer can't take clicks, the button sits in the section content. It sets `data-paused` on the layer and stops the rAF loop. The loop also stops while the section is off-screen and while the tab is hidden, and a resume never turns stale scroll into a fake gust. The gust is driven by scroll speed, with a fast attack and about 0.6s decay.
- **Contrast.** The canvas's CSS opacity (`--amb-wind-cap`) bounds every pixel, even where particles overlap, and particles are composited source-over, never additively. Worst case in the demo: body text in `--text-main` over the darkest leaf (olive, cap 0.7) is 6.0:1; snow only lightens the sky (9.9:1 over a flake rim); and `--text-inverse` over the brightest spark (amber, cap 0.5, where the deep sky is bluest) is 5.2:1. The tinted display words stay at 3.3:1 or better (large text). Muted copy appears only on the opaque cards (4.76:1 light, 6.5:1 deep). Set `--amb-wind-scrim` (0–1) to veil the layer with the page colour.
- **Performance.** There's one canvas and one rAF loop. The particle count scales with area (one per 14,000 px²) and is capped at 60, or 25 on coarse pointers and screens under 768px. Each particle is a pre-rendered sprite (`drawImage` with a single `setTransform`), built once per theme and size; the sprite glows use an 8px maximum `shadowBlur`, computed once, never per frame. The backing store is capped at DPR 2 (1.5 on coarse pointers), and a `ResizeObserver` handles resizes. Each frame takes one `getBoundingClientRect`.
- **Reduced motion and no JS.** The layer shows a static SVG scatter of the current theme (CSS switches the group), with no canvas and no loop, and the pause button stays hidden. The theme picks still work. With scripting on, the still is held back so it doesn't flash before the canvas fades in; a 2s CSS failsafe brings it back if JS never runs.
- **Adapting.** Each theme is just three colours, a vein/rim colour and a cap, set in CSS on `[data-amb-wind-theme]`, plus a physics row in `THEMES`. The theme picks are optional: any button with `data-amb-wind-set-theme` inside the host works.
