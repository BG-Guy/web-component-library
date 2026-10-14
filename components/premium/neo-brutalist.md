# Neo-Brutalist Section

A loud services section on cream: a tilted caution-tape marquee, three flat-colour service cards with 3px ink borders and hard offset shadows, rotated SVG stickers, an alerts form with a matching switch and email field, and a big CTA. The signature moment is the physical press: every face lifts off its shadow on hover and slams flat into it on click, using transforms only, so the shadow seems to grow and then collapse. On phones the cards stack full width, the rating sticker tucks beside the eyebrow and the form's button wraps under the field. Depends on `tokens/variables.css`.

**Motion:** tape marquee (36s linear loop, pausable, frozen off-screen) · face lift on hover (`--dur-2`, `--ease-spring`) and press on click (`--dur-1`) · icon tilt, arrow turn and sticker swing (`--dur-3`, `--ease-spring`) · switch knob spring (`--dur-3`) · status sticker pop (`--dur-4`, `--ease-spring`).

## HTML

```html
<section class="brutal-kit" aria-labelledby="brutal-kit-title" data-brutal-kit>
  <div class="brutal-kit__tape">
    <div class="brutal-kit__tape-track">
      <ul class="brutal-kit__tape-list" role="list">
        <li>Same-day repairs</li>
        <li>Flat-rate pricing</li>
        <li>Licensed + insured</li>
        <li>No call-out fee</li>
        <li>Westlake · Northside · Riverside</li>
      </ul>
      <ul class="brutal-kit__tape-list" role="list" aria-hidden="true">
        <li>Same-day repairs</li>
        <li>Flat-rate pricing</li>
        <li>Licensed + insured</li>
        <li>No call-out fee</li>
        <li>Westlake · Northside · Riverside</li>
      </ul>
    </div>
    <button class="brutal-kit__press brutal-kit__pause" type="button" aria-label="Pause tape animation" aria-pressed="false" hidden>
      <span class="brutal-kit__face">
        <svg class="brutal-kit__icon-pause" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
        <svg class="brutal-kit__icon-play" viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
      </span>
    </button>
  </div>

  <div class="brutal-kit__inner">
    <header class="brutal-kit__head">
      <p class="brutal-kit__eyebrow">What we fix</p>
      <h2 id="brutal-kit-title" class="brutal-kit__title">Home repairs with <span class="brutal-kit__mark">zero fluff.</span></h2>
      <p class="brutal-kit__lead">One call, one flat price, one tidy pro at your door. No mystery fees and no "we'll see" quotes.</p>
      <svg class="brutal-kit__sticker brutal-kit__sticker--rating" viewBox="0 0 100 100" width="96" height="96" role="img" aria-label="Rated 4.9 out of 5 by Springfield homeowners">
        <circle class="brutal-kit__sticker-base" cx="50" cy="50" r="46" />
        <circle class="brutal-kit__sticker-ring" cx="50" cy="50" r="39" />
        <text class="brutal-kit__sticker-small" x="50" y="31" text-anchor="middle">Rated</text>
        <text x="50" y="57" text-anchor="middle">4.9</text>
        <polygon class="brutal-kit__sticker-star" points="50,63 52,68.25 57.61,68.53 53.23,72.05 54.7,77.47 50,74.4 45.3,77.47 46.77,72.05 42.39,68.53 48,68.25" />
      </svg>
    </header>

    <ul class="brutal-kit__grid" role="list">
      <li class="brutal-kit__press brutal-kit__card brutal-kit__card--coral">
        <article class="brutal-kit__face">
          <span class="brutal-kit__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" /></svg></span>
          <h3 class="brutal-kit__card-title">Plumbing</h3>
          <p class="brutal-kit__card-text">Leaks, clogs and tired water heaters. Fixed today, mopped up after.</p>
          <p class="brutal-kit__meta">Avg. 47 min to your door</p>
          <div class="brutal-kit__card-foot">
            <span class="brutal-kit__price">From $89</span>
            <a class="brutal-kit__card-link" href="#brutal-kit-cta">Book plumbing <span class="brutal-kit__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span></a>
          </div>
        </article>
      </li>
      <li class="brutal-kit__press brutal-kit__card brutal-kit__card--lemon">
        <article class="brutal-kit__face">
          <span class="brutal-kit__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M14 14.76V3.5a2.5 2.5 0 0 0-5 0v11.26a4.5 4.5 0 1 0 5 0zM11.5 17.5V9" /></svg></span>
          <h3 class="brutal-kit__card-title">Heating &amp; cooling</h3>
          <p class="brutal-kit__card-text">Tune-ups, repairs and heat pumps, with the price agreed before we start.</p>
          <p class="brutal-kit__meta">NATE-certified techs</p>
          <div class="brutal-kit__card-foot">
            <span class="brutal-kit__price">From $129</span>
            <a class="brutal-kit__card-link" href="#brutal-kit-cta">Book HVAC <span class="brutal-kit__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span></a>
          </div>
        </article>
      </li>
      <li class="brutal-kit__press brutal-kit__card brutal-kit__card--mint">
        <article class="brutal-kit__face">
          <svg class="brutal-kit__sticker brutal-kit__sticker--new" viewBox="0 0 100 100" width="80" height="80" role="img" aria-label="New service">
            <polygon class="brutal-kit__sticker-base" points="50,2 60.09,12.33 74,8.43 77.58,22.42 91.57,26 87.67,39.91 98,50 87.67,60.09 91.57,74 77.58,77.58 74,91.57 60.09,87.67 50,98 39.91,87.67 26,91.57 22.42,77.58 8.43,74 12.33,60.09 2,50 12.33,39.91 8.43,26 22.42,22.42 26,8.43 39.91,12.33" />
            <text x="50" y="58" text-anchor="middle">NEW!</text>
          </svg>
          <span class="brutal-kit__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z" /></svg></span>
          <h3 class="brutal-kit__card-title">Smart home</h3>
          <p class="brutal-kit__card-text">Thermostats, video doorbells and EV chargers, installed and explained.</p>
          <p class="brutal-kit__meta">Licensed electricians</p>
          <div class="brutal-kit__card-foot">
            <span class="brutal-kit__price">From $149</span>
            <a class="brutal-kit__card-link" href="#brutal-kit-cta">Book install <span class="brutal-kit__go" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span></a>
          </div>
        </article>
      </li>
    </ul>

    <div class="brutal-kit__row">
      <form class="brutal-kit__panel brutal-kit__form" action="#" method="post">
        <h3 class="brutal-kit__panel-title">First dibs on same-day slots</h3>
        <p class="brutal-kit__panel-text">Cancellations go out at 7am. They're usually gone by 7:15.</p>
        <div class="brutal-kit__fields">
          <label class="brutal-kit__label">
            <span class="brutal-kit__label-text">Email address</span>
            <span class="brutal-kit__press brutal-kit__field">
              <input class="brutal-kit__input" type="email" name="email" autocomplete="email" placeholder="you@example.com" required>
            </span>
          </label>
          <button class="brutal-kit__press brutal-kit__submit" type="submit"><span class="brutal-kit__face">Notify me</span></button>
        </div>
        <label class="brutal-kit__switch">
          <input class="brutal-kit__switch-input" type="checkbox" role="switch" name="sms" checked>
          <span class="brutal-kit__switch-track" aria-hidden="true"><span class="brutal-kit__switch-knob"></span></span>
          Text me as well
        </label>
        <p class="brutal-kit__status" role="status"></p>
      </form>

      <div class="brutal-kit__panel brutal-kit__cta" id="brutal-kit-cta">
        <h3 class="brutal-kit__panel-title">Drip, draft or dead outlet?</h3>
        <a class="brutal-kit__press brutal-kit__big" href="#book">
          <span class="brutal-kit__face">Book a pro <svg viewBox="0 0 24 24" width="28" height="28" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span>
        </a>
        <p class="brutal-kit__cta-note">Or call <a href="tel:+15555550123">(555) 555-0123</a>, 7am–9pm daily.</p>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
/* Palette, cream dot-grid surface and shadow settings */
.brutal-kit {
  --brutal-kit-cream: #fff4dc;
  --brutal-kit-ink: #141210;
  --brutal-kit-lemon: #ffe14d;
  --brutal-kit-lilac: #c4a7ff;
  --brutal-kit-mint: #7fe0b0;
  --brutal-kit-coral: #ff7a5c;
  --brutal-kit-line: 3px solid var(--brutal-kit-ink);
  --brutal-kit-drop: 6px;                    /* resting shadow offset */
  --brutal-kit-lift: 4px;                    /* hover rise: the shadow then reads as drop + lift */
  --brutal-kit-cast: var(--brutal-kit-ink);  /* shadow colour */
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(circle, color-mix(in srgb, var(--brutal-kit-ink) 16%, transparent) 1px, transparent 1.6px) 0 0 / 22px 22px,
    var(--brutal-kit-cream);
  color: var(--brutal-kit-ink); font-family: var(--font-sans);
}
.brutal-kit__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3rem, 7vw, 5.5rem) var(--gutter) clamp(4rem, 8vw, 6.5rem); }

/* Press recipe: the wrapper paints the hard shadow, the face moves over it (transforms only) */
.brutal-kit__press {
  --brutal-kit-up: calc(var(--brutal-kit-lift) * -1);
  position: relative; isolation: isolate; display: inline-grid; padding: 0; border: 0; border-radius: var(--radius-md);
  background: none; color: inherit; font: inherit; text-decoration: none; cursor: pointer;
}
.brutal-kit__press::before {
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit;
  background: var(--brutal-kit-cast); translate: var(--brutal-kit-drop) var(--brutal-kit-drop);
}
.brutal-kit__face {
  box-sizing: border-box; display: flex; align-items: center; justify-content: center; gap: 0.5rem;
  border: var(--brutal-kit-line); border-radius: inherit; background: var(--surface-light);
  transition: translate var(--dur-2) var(--ease-spring);
}

/* Tape: tilted caution tape that overhangs both edges */
.brutal-kit__tape {
  position: relative; margin: 2.5rem -1rem 0; rotate: -2deg;
  border-block: var(--brutal-kit-line); background: var(--brutal-kit-lemon);
  box-shadow: 0 var(--brutal-kit-drop) 0 var(--brutal-kit-ink);
}
.brutal-kit__tape-track { display: flex; width: max-content; }
.brutal-kit--js .brutal-kit__tape-track { animation: brutal-kit-tape 36s linear infinite; }
.brutal-kit__tape-list {
  display: flex; flex: none; gap: 2.25rem; margin: 0; padding: 0.875rem 2.25rem 0.875rem 0; list-style: none;
  font: 800 clamp(1rem, 0.9rem + 0.45vw, 1.25rem)/1 var(--font-display); letter-spacing: -0.01em; text-transform: uppercase; white-space: nowrap;
}
.brutal-kit__tape-list li { display: flex; align-items: center; gap: 2.25rem; }
.brutal-kit__tape-list li::before {
  content: ""; flex: none; width: 1.1em; height: 1.1em; background: currentColor;
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 0c.6 6.3 5.7 11.4 12 12-6.3.6-11.4 5.7-12 12-.6-6.3-5.7-11.4-12-12 6.3-.6 11.4-5.7 12-12z'/%3E%3C/svg%3E") center / contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M12 0c.6 6.3 5.7 11.4 12 12-6.3.6-11.4 5.7-12 12-.6-6.3-5.7-11.4-12-12 6.3-.6 11.4-5.7 12-12z'/%3E%3C/svg%3E") center / contain no-repeat;
}
.brutal-kit__pause { --brutal-kit-drop: 3px; --brutal-kit-lift: 2px; position: absolute; top: 50%; right: calc(1rem + var(--gutter)); translate: 0 -50%; border-radius: var(--radius-full); }
.brutal-kit__pause[hidden] { display: none; }
.brutal-kit__pause .brutal-kit__face { width: 2.5rem; height: 2.5rem; background: var(--brutal-kit-cream); }
.brutal-kit__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.brutal-kit__icon-play, .brutal-kit__pause[aria-pressed="true"] .brutal-kit__icon-pause { display: none; }
.brutal-kit__pause[aria-pressed="true"] .brutal-kit__icon-play { display: block; }

/* Heading block: mono eyebrow, chunky title with a stuck-on highlight, rating sticker */
.brutal-kit__head { display: grid; grid-template-columns: 1fr auto; align-items: center; column-gap: 1rem; max-width: 64rem; }
.brutal-kit__eyebrow {
  justify-self: start; margin: 0; padding: 0.5rem 0.875rem; border: var(--brutal-kit-line); border-radius: var(--radius-full);
  background: var(--brutal-kit-lemon); box-shadow: 3px 3px 0 var(--brutal-kit-ink);
  font: 700 0.8125rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.brutal-kit__title {
  grid-column: 1 / -1; margin: 1.5rem 0 0;
  font: 800 clamp(2.5rem, 1.4rem + 4.8vw, 5.5rem)/0.95 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance;
}
.brutal-kit__mark {
  display: inline-block; margin-top: 0.12em; padding: 0 0.14em 0.06em; border: var(--brutal-kit-line); border-radius: var(--radius-md);
  background: var(--brutal-kit-lilac); box-shadow: var(--brutal-kit-drop) var(--brutal-kit-drop) 0 var(--brutal-kit-ink); rotate: -2deg;
}
.brutal-kit__lead {
  grid-column: 1 / -1; max-width: 34rem; margin: 1.25rem 0 0;
  color: color-mix(in srgb, var(--brutal-kit-ink) 80%, var(--brutal-kit-cream)); font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.55;
}

/* Stickers: SVG shapes with a hard drop shadow */
.brutal-kit__sticker { overflow: visible; filter: drop-shadow(3px 3px 0 var(--brutal-kit-ink)); }
.brutal-kit__sticker-base { stroke: var(--brutal-kit-ink); stroke-width: 3; vector-effect: non-scaling-stroke; }
.brutal-kit__sticker-ring { fill: none; stroke: var(--brutal-kit-ink); stroke-width: 1.5; stroke-dasharray: 3 4; vector-effect: non-scaling-stroke; }
.brutal-kit__sticker-star { fill: var(--brutal-kit-ink); }
.brutal-kit__sticker text { fill: var(--brutal-kit-ink); font: 800 28px var(--font-display); letter-spacing: -0.02em; }
.brutal-kit__sticker .brutal-kit__sticker-small { font: 700 10px var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.brutal-kit__sticker--rating {
  grid-column: 2; grid-row: 1; width: 5.25rem; height: 5.25rem; fill: var(--brutal-kit-mint);
  rotate: 10deg; transition: rotate var(--dur-3) var(--ease-spring);
}
.brutal-kit__sticker--new {
  position: absolute; top: -1.75rem; right: -0.5rem; width: 4.75rem; height: 4.75rem; fill: var(--brutal-kit-coral);
  rotate: 14deg; transition: rotate var(--dur-3) var(--ease-spring);
}
.brutal-kit__sticker--new text { font-size: 22px; }

/* Service cards: flat fills, the whole card is the "Book" link's hit area */
.brutal-kit__grid { display: grid; gap: 2rem; margin: 3rem 0 0; padding: 0; list-style: none; }
.brutal-kit__card { display: grid; border-radius: var(--radius-lg); }
.brutal-kit__card .brutal-kit__face {
  position: relative; display: grid; align-content: start; justify-content: stretch; justify-items: start; gap: 0.75rem;
  padding: 1.5rem 1.375rem 1.25rem; background: var(--brutal-kit-fill, var(--surface-light));
}
.brutal-kit__card--coral { --brutal-kit-fill: var(--brutal-kit-coral); }
.brutal-kit__card--lemon { --brutal-kit-fill: var(--brutal-kit-lemon); }
.brutal-kit__card--mint { --brutal-kit-fill: var(--brutal-kit-mint); }
.brutal-kit__icon {
  box-sizing: border-box; display: grid; place-items: center; width: 3rem; height: 3rem;
  border: var(--brutal-kit-line); border-radius: var(--radius-md); background: var(--brutal-kit-cream);
  box-shadow: 3px 3px 0 var(--brutal-kit-ink); transition: rotate var(--dur-3) var(--ease-spring);
}
.brutal-kit__icon svg, .brutal-kit__go svg, .brutal-kit__big svg { fill: none; stroke: currentColor; stroke-width: 2.25; stroke-linecap: round; stroke-linejoin: round; }
.brutal-kit__card-title { margin: 0.5rem 0 0; font: 800 clamp(1.625rem, 1.35rem + 0.9vw, 2rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.brutal-kit__card-text { margin: 0; font-size: 1rem; line-height: 1.5; }
.brutal-kit__meta {
  margin: 0; padding: 0.25rem 0.5rem; border: 2px solid var(--brutal-kit-ink); border-radius: var(--radius-sm);
  font: 600 0.75rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.brutal-kit__card-foot {
  justify-self: stretch; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem;
  margin-top: 0.5rem; padding-top: 1rem; border-top: var(--brutal-kit-line);
}
.brutal-kit__price {
  padding: 0.4375rem 0.75rem; border: var(--brutal-kit-line); border-radius: var(--radius-full); background: var(--brutal-kit-cream);
  font: 700 0.8125rem/1 var(--font-mono); text-transform: uppercase;
}
.brutal-kit__card-link { display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.75rem; color: inherit; font-weight: 800; text-decoration: none; }
.brutal-kit__card-link::after { content: ""; position: absolute; inset: -3px; border-radius: var(--radius-lg); }
.brutal-kit__go {
  display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 50%;
  background: var(--brutal-kit-ink); color: var(--brutal-kit-cream); transition: rotate var(--dur-3) var(--ease-spring);
}
.brutal-kit__card:focus-within .brutal-kit__go { rotate: -45deg; }

/* Alerts form: email field and switch in the same ink-and-shadow language */
.brutal-kit__row { display: grid; gap: 2.25rem; margin-top: 3.5rem; }
.brutal-kit__panel {
  padding: clamp(1.5rem, 1rem + 2vw, 2.25rem); border: var(--brutal-kit-line); border-radius: var(--radius-lg);
  box-shadow: var(--brutal-kit-drop) var(--brutal-kit-drop) 0 var(--brutal-kit-ink);
}
.brutal-kit__panel-title { margin: 0; font: 800 clamp(1.625rem, 1.25rem + 1.3vw, 2.25rem)/1.02 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.brutal-kit__panel-text { margin: 0.625rem 0 0; line-height: 1.5; }
.brutal-kit__form { background: var(--brutal-kit-lilac); }
.brutal-kit__fields { display: flex; flex-wrap: wrap; align-items: flex-end; gap: 1rem; margin-top: 1.5rem; }
.brutal-kit__label { display: grid; gap: 0.5rem; flex: 1 1 14rem; }
.brutal-kit__label-text { font: 700 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.brutal-kit__field { display: grid; cursor: text; }
.brutal-kit__input {
  box-sizing: border-box; width: 100%; min-height: 3.25rem; margin: 0; padding: 0 1rem;
  border: var(--brutal-kit-line); border-radius: inherit; background: var(--surface-light); color: var(--brutal-kit-ink);
  font: 600 1rem var(--font-sans); transition: translate var(--dur-2) var(--ease-spring);
}
.brutal-kit__input::placeholder { color: color-mix(in srgb, var(--brutal-kit-ink) 62%, var(--surface-light)); opacity: 1; }
.brutal-kit__field:focus-within .brutal-kit__input { translate: -3px -3px; }
.brutal-kit__submit .brutal-kit__face { min-height: 3.25rem; padding: 0 1.375rem; background: var(--brutal-kit-lemon); font-weight: 800; }
.brutal-kit__switch { position: relative; display: inline-flex; align-items: center; gap: 0.75rem; min-height: 2.75rem; margin-top: 1.25rem; font-weight: 700; cursor: pointer; }
.brutal-kit__switch-input { position: absolute; width: 1px; height: 1px; margin: 0; opacity: 0; pointer-events: none; }
.brutal-kit__switch-track {
  position: relative; flex: none; box-sizing: border-box; width: 3.5rem; height: 2rem;
  border: var(--brutal-kit-line); border-radius: var(--radius-full); background: var(--surface-light);
  box-shadow: 3px 3px 0 var(--brutal-kit-ink); transition: background-color var(--dur-2) var(--ease-out);
}
.brutal-kit__switch-knob {
  position: absolute; top: 0.1875rem; left: 0.1875rem; width: 1.25rem; height: 1.25rem; border-radius: 50%;
  background: var(--brutal-kit-ink); transition: translate var(--dur-3) var(--ease-spring);
}
.brutal-kit__switch-input:checked + .brutal-kit__switch-track { background: var(--brutal-kit-mint); }
.brutal-kit__switch-input:checked + .brutal-kit__switch-track .brutal-kit__switch-knob { translate: 1.5rem 0; }
.brutal-kit__status { margin: 1rem 0 0; font-weight: 700; }
.brutal-kit__status:empty { margin: 0; }
.brutal-kit__status:not(:empty) {
  display: inline-block; padding: 0.5rem 0.875rem; border: var(--brutal-kit-line); border-radius: var(--radius-md);
  background: var(--brutal-kit-mint); rotate: -1.5deg; animation: brutal-kit-pop var(--dur-4) var(--ease-spring) both;
}

/* Closing CTA on an ink panel */
.brutal-kit__cta {
  --brutal-kit-cast: var(--brutal-kit-coral);
  display: grid; align-content: center; justify-items: start; gap: 1.5rem;
  background:
    radial-gradient(circle, color-mix(in srgb, var(--brutal-kit-cream) 14%, transparent) 1px, transparent 1.6px) 0 0 / 22px 22px,
    var(--brutal-kit-ink);
  box-shadow: var(--brutal-kit-drop) var(--brutal-kit-drop) 0 var(--brutal-kit-coral);
  color: var(--brutal-kit-cream);
}
.brutal-kit__big { --brutal-kit-drop: 8px; --brutal-kit-lift: 5px; border-radius: var(--radius-lg); }
.brutal-kit__big .brutal-kit__face {
  min-height: 4.5rem; padding: 0 1.75rem; gap: 0.75rem; border-color: var(--brutal-kit-cream);
  background: var(--brutal-kit-lemon); color: var(--brutal-kit-ink);
  font: 800 clamp(1.625rem, 1.15rem + 1.7vw, 2.5rem)/1 var(--font-display); letter-spacing: var(--tracking-tight);
}
.brutal-kit__big svg { width: 1em; height: 1em; transition: translate var(--dur-3) var(--ease-spring); }
.brutal-kit__cta-note { margin: 0; color: color-mix(in srgb, var(--brutal-kit-cream) 82%, var(--brutal-kit-ink)); }
.brutal-kit__cta-note a { color: var(--brutal-kit-cream); font-weight: 700; text-decoration-color: var(--brutal-kit-lemon); text-decoration-thickness: 2px; text-underline-offset: 3px; }

/* Lift on hover (pointer devices), lift on keyboard focus, slam flat on press */
@media (hover: hover) {
  .brutal-kit__press:hover .brutal-kit__face { translate: var(--brutal-kit-up) var(--brutal-kit-up); }
  .brutal-kit__card:hover .brutal-kit__icon { rotate: -8deg; }
  .brutal-kit__card:hover .brutal-kit__go { rotate: -45deg; }
  .brutal-kit__card:hover .brutal-kit__sticker--new { rotate: -8deg; }
  .brutal-kit__head:hover .brutal-kit__sticker--rating { rotate: -4deg; }
  .brutal-kit__big:hover svg { translate: 0.25em 0; }
}
.brutal-kit__press:focus-visible .brutal-kit__face { translate: var(--brutal-kit-up) var(--brutal-kit-up); }
.brutal-kit__press:has(:focus-visible) .brutal-kit__face { translate: var(--brutal-kit-up) var(--brutal-kit-up); }
.brutal-kit__press:active .brutal-kit__face { translate: var(--brutal-kit-drop) var(--brutal-kit-drop); transition-duration: var(--dur-1); }

/* Focus: blue ring on cream, light ring on the ink panel; pressable faces carry their own ring */
.brutal-kit :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.brutal-kit :is(.brutal-kit__press, .brutal-kit__card-link):focus-visible { outline: none; }
.brutal-kit__press:focus-visible .brutal-kit__face,
.brutal-kit__card-link:focus-visible::after,
.brutal-kit__input:focus-visible,
.brutal-kit__switch-input:focus-visible + .brutal-kit__switch-track { outline: 2px solid var(--primary); outline-offset: 3px; }
.brutal-kit__cta :is(a, button):focus-visible,
.brutal-kit__cta .brutal-kit__press:focus-visible .brutal-kit__face { outline-color: var(--text-inverse); }

/* Paused or off-screen: freeze the tape */
.brutal-kit[data-paused] .brutal-kit__tape-track,
.brutal-kit[data-offscreen] .brutal-kit__tape-track { animation-play-state: paused; }

@media (min-width: 768px) {
  .brutal-kit__tape { margin-inline: -2rem; }
  .brutal-kit__pause { right: calc(2rem + var(--gutter)); }
  .brutal-kit__title, .brutal-kit__lead { grid-column: 1; }
  .brutal-kit__sticker--rating { grid-row: 1 / span 3; width: 9rem; height: 9rem; }
  .brutal-kit__sticker--new { right: -1rem; }
  .brutal-kit__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.75rem; }
  .brutal-kit__row { grid-template-columns: 1.15fr 0.85fr; }
}
@media (prefers-reduced-motion: reduce) {
  .brutal-kit *, .brutal-kit *::before, .brutal-kit *::after { animation: none !important; }
}
@keyframes brutal-kit-tape { to { transform: translateX(-50%); } }
@keyframes brutal-kit-pop { from { opacity: 0; scale: 0.6; } }
```

## JS

```js
document.querySelectorAll('[data-brutal-kit]').forEach((root) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const pause = root.querySelector('.brutal-kit__pause');
  const form = root.querySelector('.brutal-kit__form');
  const status = root.querySelector('.brutal-kit__status');

  // The tape only scrolls once a pause button can be offered (WCAG 2.2.2); no button when motion is off
  root.classList.add('brutal-kit--js');
  const syncMotion = () => { pause.hidden = reduce.matches; };
  syncMotion();
  reduce.addEventListener('change', syncMotion);
  pause.addEventListener('click', () => {
    pause.setAttribute('aria-pressed', String(root.toggleAttribute('data-paused')));
  });

  // Freeze the loop while the section is off screen, without touching the button state
  new IntersectionObserver(([entry]) => root.toggleAttribute('data-offscreen', !entry.isIntersecting)).observe(root);

  // Demo submit: confirm inline with a sticker instead of leaving the page
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const sms = form.elements.sms.checked;
    status.textContent = '';
    void status.offsetWidth; // restart the pop for repeat sign-ups
    status.textContent = sms ? "You're in! Alerts by email and text from 7am." : "You're in! Watch your inbox at 7am.";
    form.elements.email.value = '';
  });
});
```

## Notes

- Accessibility: the tape is a real list (the loop copy is `aria-hidden`). Each card is an `<article>` with an `<h3>` and one "Book …" link whose `::after` stretches over the card, so the whole card is clickable but announced once, and its focus ring wraps the full card. The switch is a native checkbox with `role="switch"`, the email field has a visible label, and the confirmation is a `role="status"` region.
- No JS: the tape sits still (its loop starts only once JS can show the pause button) and the form posts normally. With JS, the `aria-pressed` pause button stops the loop and an IntersectionObserver freezes it off-screen.
- Reduced motion: the tape is static and the pause button is hidden; lifts, presses, the switch and sticker swings become instant through the duration tokens.
- Contrast, ink `#141210` text on each fill: cream 17.1:1, lemon 14.4:1, mint 13.1:1, lilac 9.2:1, coral 7.3:1. Cream on the ink panel is 17.1:1, the lead (80% ink) 9.6:1, the CTA note (82% cream) 11.6:1 and the placeholder (62% ink on white) 5.2:1.
- The hard shadow is a wrapper `::before` that never moves while the face translates, so the shadow "grows" and "collapses" with transforms only. Tune `--brutal-kit-drop` / `--brutal-kit-lift` per element, or retheme by swapping the six palette variables. Headings use Geist 800, so include that weight in the page's Geist link.
