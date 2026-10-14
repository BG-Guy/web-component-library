# Estimate Calculator

A renovation price calculator with light controls (a home-size slider, a bathrooms stepper, material-tier cards and add-on switches) beside a deep result card. Every change rolls the big total like an odometer, column by column, while the labour / materials / permits bar re-proportions itself and the range and monthly cost update. On phones the result card follows the controls, and a sticky peek bar keeps the live total in view with a jump to the breakdown. Depends on `tokens/variables.css`.

**Motion:** odometer digit roll (`--dur-5`, `--ease-spring`, staggered from the right) · breakdown bar re-proportions (`grid-template-columns`, `--dur-5`, `--ease-out`) · "live" ping on each update · slider bubble lift and thumb grow (`--ease-spring`) · stepper count pop and limit nudge · switch knob and tier badge springs.

## HTML

```html
<section class="estimator" aria-labelledby="estimator-title" data-estimator>
  <div class="estimator__inner">
    <header class="estimator__head">
      <p class="estimator__eyebrow">Renovation calculator</p>
      <h2 id="estimator-title" class="estimator__title">What will your refresh cost?</h2>
      <p class="estimator__lede">Move the dials for a realistic range, priced from 1,400+ Springfield projects. No email needed.</p>
    </header>

    <form class="estimator__form" action="/estimate" method="get">
      <div class="estimator__controls">
        <div class="estimator__group">
          <div class="estimator__label-row">
            <label class="estimator__label" for="estimator-size">Home size</label>
            <span class="estimator__hint">Finished floor area</span>
          </div>
          <div class="estimator__slider" style="--estimator-p: 0.2889">
            <span class="estimator__bubble" aria-hidden="true">1,800 sq ft</span>
            <input class="estimator__range" id="estimator-size" type="range" name="size" min="500" max="5000" step="50" value="1800" aria-valuetext="1,800 square feet">
            <span class="estimator__scale" aria-hidden="true"><span>500</span><span>5,000 sq ft</span></span>
          </div>
        </div>

        <div class="estimator__group estimator__group--row">
          <div>
            <label class="estimator__label" for="estimator-baths">Bathrooms</label>
            <span class="estimator__hint">Full or half, 1 to 6</span>
          </div>
          <div class="estimator__stepper">
            <button class="estimator__step" type="button" aria-label="Remove a bathroom" aria-controls="estimator-baths">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14" /></svg>
            </button>
            <input class="estimator__count" id="estimator-baths" type="number" name="baths" min="1" max="6" step="1" value="2" inputmode="numeric">
            <button class="estimator__step" type="button" aria-label="Add a bathroom" aria-controls="estimator-baths">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg>
            </button>
          </div>
        </div>

        <fieldset class="estimator__group estimator__fieldset">
          <legend class="estimator__label">Material tier</legend>
          <div class="estimator__tiers">
            <label class="estimator__tier">
              <input type="radio" name="tier" value="standard" checked>
              <span class="estimator__tier-name">Standard</span>
              <span class="estimator__tier-cost" aria-hidden="true">$<span>$$</span></span>
              <small>Builder-grade fixtures, vinyl plank</small>
            </label>
            <label class="estimator__tier">
              <input type="radio" name="tier" value="premium">
              <span class="estimator__tier-name">Premium</span>
              <span class="estimator__tier-cost" aria-hidden="true">$$<span>$</span></span>
              <small>Designer fixtures, quartz, oak</small>
            </label>
            <label class="estimator__tier">
              <input type="radio" name="tier" value="luxury">
              <span class="estimator__tier-name">Luxury</span>
              <span class="estimator__tier-cost" aria-hidden="true">$$$</span>
              <small>Natural stone, custom millwork</small>
            </label>
          </div>
        </fieldset>

        <fieldset class="estimator__group estimator__fieldset">
          <legend class="estimator__label">Add-ons</legend>
          <div class="estimator__addons">
            <label class="estimator__addon"><span>Heated bathroom floors<small>+$900 per bathroom</small></span><input class="estimator__switch" type="checkbox" role="switch" name="addons" value="heated-floors" data-cost="900" data-per="bath"><span class="estimator__track" aria-hidden="true"></span></label>
            <label class="estimator__addon"><span>Smart home package<small>+$1,200</small></span><input class="estimator__switch" type="checkbox" role="switch" name="addons" value="smart-home" data-cost="1200"><span class="estimator__track" aria-hidden="true"></span></label>
            <label class="estimator__addon"><span>Fresh paint throughout<small>+$1.10 per sq ft</small></span><input class="estimator__switch" type="checkbox" role="switch" name="addons" value="paint" data-cost="1.1" data-per="sqft"><span class="estimator__track" aria-hidden="true"></span></label>
            <label class="estimator__addon"><span>Haul-away &amp; deep clean<small>+$450</small></span><input class="estimator__switch" type="checkbox" role="switch" name="addons" value="clean-up" data-cost="450"><span class="estimator__track" aria-hidden="true"></span></label>
          </div>
        </fieldset>

        <a class="estimator__peek" href="#estimator-result">
          <span class="estimator__peek-label">Estimate</span>
          <strong class="estimator__peek-total">$9,300</strong>
          <span class="estimator__peek-link">Breakdown<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg></span>
        </a>
      </div>

      <div class="estimator__result" id="estimator-result">
        <div class="estimator__result-head">
          <h3 class="estimator__result-title">Your estimate</h3>
          <span class="estimator__badge"><span class="estimator__dot" aria-hidden="true"><span class="estimator__ping"></span></span>Live</span>
        </div>

        <div class="estimator__live-only">
          <p class="estimator__total"><span class="estimator__odometer" aria-hidden="true">$9,300</span><span class="estimator__sr estimator__total-text">$9,300</span></p>
          <p class="estimator__range-line">Typical range <strong class="estimator__range-text">$8,400 – $10,200</strong></p>
          <div class="estimator__breakdown">
            <div class="estimator__bar" style="grid-template-columns: 4540fr 4320fr 401fr" aria-hidden="true">
              <span class="estimator__seg estimator__seg--labour"></span><span class="estimator__seg estimator__seg--materials"></span><span class="estimator__seg estimator__seg--permits"></span>
            </div>
            <dl class="estimator__legend">
              <div><dt><span class="estimator__swatch estimator__swatch--labour" aria-hidden="true"></span>Labour</dt><dd data-part="labour">$4,540</dd></div>
              <div><dt><span class="estimator__swatch estimator__swatch--materials" aria-hidden="true"></span>Materials</dt><dd data-part="materials">$4,320</dd></div>
              <div><dt><span class="estimator__swatch estimator__swatch--permits" aria-hidden="true"></span>Permits</dt><dd data-part="permits">$400</dd></div>
            </dl>
          </div>
          <p class="estimator__finance"><span>Or from <strong class="estimator__monthly">$188/mo</strong></span><small>60 months at 7.99% APR, subject to approval</small></p>
        </div>

        <p class="estimator__nojs">Press calculate to see your price range, the labour / materials / permits breakdown and a monthly cost.</p>
        <button class="estimator__submit" type="submit">Calculate my estimate</button>
        <a class="estimator__cta" href="#book">
          Book a free site visit
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <p class="estimator__fine">Includes labour, materials and permits. Your fixed quote follows a free 30-minute walkthrough.</p>
        <p class="estimator__sr estimator__live" aria-live="polite"></p>
      </div>
    </form>
  </div>
</section>
```

## CSS

```css
/* Section */
.estimator {
  --estimator-grad: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  --estimator-fill-image: var(--estimator-grad);
  --estimator-thumb: 1.75rem;
  background:
    radial-gradient(50% 40% at 100% 0%, color-mix(in srgb, var(--primary-2) 10%, transparent), transparent 70%),
    radial-gradient(40% 40% at 0% 100%, color-mix(in srgb, var(--primary) 7%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.estimator__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3.5rem, 8vw, 6rem) var(--gutter); }
.estimator__head { max-width: 38rem; margin-bottom: clamp(2rem, 4vw, 3rem); }
.estimator__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.estimator__title { margin: 0.875rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.6vw, 3rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.estimator__lede { margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
:where(.estimator) svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.estimator__form { display: grid; gap: 1.25rem; align-items: start; }

/* Controls panel */
.estimator__controls {
  position: relative; container-type: inline-size; padding: 0.25rem 1.25rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.estimator__group { min-width: 0; margin: 0; padding: 1.5rem 0; border: 0; }
.estimator__group + .estimator__group { border-top: 1px solid var(--border-subtle); }
.estimator__label-row { display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 0.25rem 1rem; }
.estimator__label { display: block; padding: 0; font-size: 1rem; font-weight: 600; }
.estimator__fieldset > .estimator__label { float: left; width: 100%; margin-bottom: 1rem; }
.estimator__hint { display: block; margin-top: 0.125rem; color: var(--text-muted); font-size: 0.8125rem; }

/* Home size: gradient-filled slider with a value bubble riding the thumb */
.estimator__slider { position: relative; margin-top: 2.75rem; }
.estimator__bubble {
  position: absolute; bottom: calc(100% - 0.25rem); left: clamp(2.75rem, calc(var(--estimator-thumb) / 2 + (100% - var(--estimator-thumb)) * var(--estimator-p, 0)), calc(100% - 2.75rem));
  padding: 0.4375rem 0.625rem; border-radius: var(--radius-md); background: var(--text-main); color: var(--surface-light);
  font: 600 0.8125rem/1 var(--font-mono); font-variant-numeric: tabular-nums; white-space: nowrap; pointer-events: none;
  translate: -50% 0; transform-origin: 50% 100%; transition: transform var(--dur-3) var(--ease-spring);
}
.estimator__bubble::after { content: ""; position: absolute; top: 100%; left: 50%; border: 5px solid transparent; border-top-color: var(--text-main); translate: -50% 0; }
.estimator__slider:has(.estimator__range:active) .estimator__bubble { transform: translateY(-4px) scale(1.08); }
.estimator__range { display: block; width: 100%; height: 2.75rem; margin: 0; background: none; cursor: pointer; -webkit-appearance: none; appearance: none; }
.estimator__range:focus-visible { outline: 2px solid transparent; }
.estimator__range::-webkit-slider-runnable-track {
  height: 0.5rem; border-radius: var(--radius-full);
  background: var(--estimator-fill-image) 0 0 / calc(var(--estimator-thumb) / 2 + (100% - var(--estimator-thumb)) * var(--estimator-p, 0)) 100% no-repeat, var(--border-subtle);
}
.estimator__range::-moz-range-track {
  height: 0.5rem; border-radius: var(--radius-full);
  background: var(--estimator-fill-image) 0 0 / calc(var(--estimator-thumb) / 2 + (100% - var(--estimator-thumb)) * var(--estimator-p, 0)) 100% no-repeat, var(--border-subtle);
}
.estimator__range::-webkit-slider-thumb {
  width: var(--estimator-thumb); height: var(--estimator-thumb); margin-top: calc((0.5rem - var(--estimator-thumb)) / 2); border: 0; border-radius: 50%; -webkit-appearance: none; appearance: none;
  background: var(--surface-light); box-shadow: inset 0 0 0 2px var(--primary), 0 6px 14px -4px color-mix(in srgb, var(--primary) 60%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2);
}
.estimator__range::-moz-range-thumb {
  width: var(--estimator-thumb); height: var(--estimator-thumb); border: 0; border-radius: 50%;
  background: var(--surface-light); box-shadow: inset 0 0 0 2px var(--primary), 0 6px 14px -4px color-mix(in srgb, var(--primary) 60%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2);
}
.estimator__range:active::-webkit-slider-thumb { transform: scale(1.15); }
.estimator__range:active::-moz-range-thumb { transform: scale(1.15); }
.estimator__range:focus-visible::-webkit-slider-thumb { box-shadow: inset 0 0 0 2px var(--primary), var(--focus-ring); }
.estimator__range:focus-visible::-moz-range-thumb { box-shadow: inset 0 0 0 2px var(--primary), var(--focus-ring); }
.estimator__scale { display: flex; justify-content: space-between; color: var(--text-muted); font: 500 0.75rem var(--font-mono); }

/* Bathrooms: a native number input between − and + */
.estimator__group--row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.estimator__stepper { display: flex; flex: none; align-items: center; gap: 0.25rem; padding: 0.25rem; border-radius: var(--radius-full); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.estimator__step {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: transform var(--dur-3) var(--ease-spring), color var(--dur-2);
}
.estimator__step:active { transform: scale(0.88); }
.estimator__step[aria-disabled="true"] { cursor: default; color: color-mix(in srgb, var(--text-muted) 50%, transparent); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.estimator__count {
  width: 3rem; height: 2.75rem; padding: 0; border: 0; border-radius: var(--radius-md); background: transparent; color: var(--text-main);
  font: 600 1.375rem/1 var(--font-display); font-variant-numeric: tabular-nums; text-align: center; -moz-appearance: textfield; appearance: textfield;
}
.estimator__count::-webkit-inner-spin-button, .estimator__count::-webkit-outer-spin-button { margin: 0; -webkit-appearance: none; }
.estimator__step:focus-visible, .estimator__count:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Material tier: radio cards with a $-meter and a check badge */
.estimator__tiers { display: grid; gap: 0.625rem; }
.estimator__tier {
  position: relative; display: grid; grid-template-columns: 1fr auto; align-items: center; gap: 0.25rem 1rem; padding: 0.875rem 1rem; border-radius: var(--radius-xl); cursor: pointer;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: background-color var(--dur-3), box-shadow var(--dur-3), transform var(--dur-3) var(--ease-spring);
}
.estimator__tier input { position: absolute; opacity: 0; pointer-events: none; }
.estimator__tier-name { font-weight: 600; }
.estimator__tier-cost { color: var(--primary); font: 600 0.875rem var(--font-mono); letter-spacing: 0.1em; }
.estimator__tier-cost span { color: color-mix(in srgb, var(--text-muted) 40%, transparent); }
.estimator__tier small { grid-column: 1 / -1; color: var(--text-muted); font-size: 0.8125rem; line-height: 1.4; }
.estimator__tier::before, .estimator__tier::after { content: ""; position: absolute; opacity: 0; transition: opacity var(--dur-2), transform var(--dur-4) var(--ease-spring); }
.estimator__tier::after { top: -0.4375rem; right: -0.4375rem; width: 1.375rem; height: 1.375rem; border-radius: 50%; background: var(--estimator-grad); box-shadow: 0 0 0 3px var(--surface-light); transform: scale(0); }
.estimator__tier::before { z-index: 1; top: -0.125rem; right: 0.0625rem; width: 0.3125rem; height: 0.5625rem; border: solid var(--text-inverse); border-width: 0 2px 2px 0; transform: rotate(45deg) scale(0); }
.estimator__tier:hover { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 40%, var(--border-subtle)), var(--shadow-md); }
.estimator__tier:active { transform: scale(0.98); }
.estimator__tier:has(:checked) { background: color-mix(in srgb, var(--primary) 5%, var(--surface-light)); box-shadow: inset 0 0 0 2px var(--primary), 0 12px 24px -14px color-mix(in srgb, var(--primary) 70%, transparent); }
.estimator__tier:has(:checked)::after { opacity: 1; transform: scale(1); }
.estimator__tier:has(:checked)::before { opacity: 1; transform: rotate(45deg) scale(1); }
.estimator__tier:has(:focus-visible) { outline: 2px solid transparent; box-shadow: var(--focus-ring), inset 0 0 0 2px var(--primary); }

/* Add-ons: native checkboxes (role="switch") driving a visual track */
.estimator__addon { position: relative; display: flex; align-items: center; justify-content: space-between; gap: 1rem; min-height: 3rem; padding: 0.625rem 0; cursor: pointer; font-weight: 500; }
.estimator__addon + .estimator__addon { border-top: 1px dashed var(--border-subtle); }
.estimator__addon small { display: block; margin-top: 0.125rem; color: var(--text-muted); font: 500 0.75rem var(--font-mono); }
.estimator__switch { position: absolute; opacity: 0; pointer-events: none; }
.estimator__track {
  position: relative; flex: none; width: 2.875rem; height: 1.75rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--text-muted) 80%, var(--surface-light)); transition: background-color var(--dur-3);
}
.estimator__track::before {
  content: ""; position: absolute; top: 0.1875rem; left: 0.1875rem; width: 1.375rem; height: 1.375rem; border-radius: 50%;
  background: var(--surface-light); box-shadow: var(--shadow-md); transition: transform var(--dur-4) var(--ease-spring);
}
.estimator__addon:active .estimator__track::before { transform: scaleX(1.15); }
.estimator__switch:checked + .estimator__track { background: var(--primary); }
.estimator__switch:checked + .estimator__track::before { transform: translateX(1.125rem); }
.estimator__switch:focus-visible + .estimator__track { box-shadow: var(--focus-ring); }

/* Phones and tablets: a sticky peek at the live total */
.estimator__peek {
  position: sticky; bottom: max(0.75rem, env(safe-area-inset-bottom)); z-index: var(--z-sticky);
  display: flex; align-items: center; gap: 0.75rem; margin: 0.25rem -0.5rem 1rem; padding: 0.5rem 0.5rem 0.5rem 1.125rem; border-radius: var(--radius-full);
  background: var(--surface-deep); color: var(--text-inverse); text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-inverse), 0 16px 32px -12px color-mix(in srgb, var(--surface-deep) 60%, transparent);
}
.estimator__peek:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.estimator__peek-label { color: var(--text-inverse-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.estimator__peek-total { font: 600 1.125rem/1 var(--font-display); font-variant-numeric: tabular-nums; }
.estimator__peek-link { display: inline-flex; align-items: center; gap: 0.25rem; margin-left: auto; padding: 0.625rem 0.875rem; border-radius: var(--radius-full); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); font-size: 0.8125rem; font-weight: 600; }

/* Result card: deep surface, gradient light, a faint blueprint grid */
.estimator__result {
  position: relative; isolation: isolate; overflow: hidden; container-type: inline-size; padding: 1.5rem; border-radius: var(--radius-2xl); scroll-margin-top: 1rem;
  background:
    radial-gradient(90% 70% at 100% 0%, color-mix(in srgb, var(--primary-2) 30%, transparent), transparent 65%),
    radial-gradient(80% 70% at 0% 100%, color-mix(in srgb, var(--primary) 34%, transparent), transparent 65%),
    var(--surface-deep);
  color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 40px 80px -30px color-mix(in srgb, var(--surface-deep) 70%, transparent);
}
.estimator__result::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background-image: linear-gradient(var(--border-inverse) 1px, transparent 1px), linear-gradient(90deg, var(--border-inverse) 1px, transparent 1px);
  background-size: 28px 28px;
  -webkit-mask-image: radial-gradient(ellipse 60% 50% at 90% 8%, black, transparent 70%);
  mask-image: radial-gradient(ellipse 60% 50% at 90% 8%, black, transparent 70%);
}
.estimator__result :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.estimator__result-head { display: flex; align-items: center; justify-content: space-between; gap: 1rem; }
.estimator__result-title { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.estimator__badge { display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.3125rem 0.625rem; border-radius: var(--radius-full); background: color-mix(in srgb, var(--success) 24%, transparent); font-size: 0.75rem; font-weight: 600; }
.estimator__dot { position: relative; width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: color-mix(in srgb, var(--success) 70%, var(--text-inverse)); }
.estimator__ping { position: absolute; inset: 0; border-radius: inherit; background: inherit; opacity: 0; }

/* The odometer: one column per digit, each a strip of 0–9 that rolls to its value */
.estimator__total { margin: 1.25rem 0 0; font: 600 clamp(3rem, 2.3rem + 3vw, 4.25rem)/1.1 var(--font-display); font-variant-numeric: tabular-nums; letter-spacing: var(--tracking-tight); }
.estimator__odometer { display: inline-flex; }
.estimator__odometer > span { height: 1.1em; line-height: 1.1; }
.estimator__digit { overflow: hidden; }
.estimator__digit > span {
  display: flex; flex-direction: column; transform: translateY(calc(var(--estimator-d, 0) * -10%));
  transition: transform var(--dur-5) var(--ease-spring) calc(var(--estimator-i, 0) * var(--stagger) * 0.6);
}
.estimator__range-line { margin: 0.5rem 0 0; color: var(--text-inverse-muted); font-size: 0.9375rem; }
.estimator__range-line strong { color: var(--text-inverse); font-weight: 600; font-variant-numeric: tabular-nums; }

/* Breakdown: one bar whose three segments re-proportion */
.estimator__breakdown { margin-top: 1.5rem; padding: 1rem; border-radius: var(--radius-xl); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.estimator__bar { display: grid; gap: 3px; height: 0.75rem; transition: grid-template-columns var(--dur-5) var(--ease-out); }
.estimator__seg { min-width: 0; border-radius: var(--radius-full); }
.estimator__seg--labour, .estimator__swatch--labour { background: var(--primary); }
.estimator__seg--materials, .estimator__swatch--materials { background: color-mix(in srgb, var(--primary-2) 85%, var(--text-inverse)); }
.estimator__seg--permits, .estimator__swatch--permits { background: var(--accent); }
.estimator__legend { display: grid; gap: 0.5rem; margin: 1rem 0 0; }
.estimator__legend div { display: flex; align-items: center; justify-content: space-between; gap: 1rem; font-size: 0.875rem; }
.estimator__legend dt { display: flex; align-items: center; gap: 0.5rem; color: var(--text-inverse-muted); }
.estimator__legend dd { margin: 0; font: 500 0.875rem var(--font-mono); font-variant-numeric: tabular-nums; }
.estimator__swatch { width: 0.625rem; height: 0.625rem; border-radius: 0.1875rem; }
.estimator__finance { display: grid; gap: 0.25rem; margin: 1.25rem 0 0; color: var(--text-inverse-muted); font-size: 0.9375rem; }
.estimator__finance strong { color: var(--text-inverse); font: 600 1.25rem var(--font-display); font-variant-numeric: tabular-nums; }
.estimator__finance small { font-size: 0.8125rem; }

/* Actions */
.estimator__cta, .estimator__submit {
  display: flex; align-items: center; justify-content: center; gap: 0.5rem; width: 100%; height: 3.25rem; margin-top: 1.5rem; padding: 0 1.25rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--surface-light); color: var(--text-main); font: 600 1rem var(--font-sans); text-decoration: none;
  box-shadow: 0 14px 34px -14px color-mix(in srgb, var(--primary) 90%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3);
}
.estimator__submit { background: var(--estimator-grad); color: var(--text-inverse); }
.estimator__submit[hidden] { display: none; }
.estimator__cta svg { transition: transform var(--dur-3) var(--ease-spring); }
.estimator__cta:hover { transform: translateY(-1px); box-shadow: 0 18px 40px -14px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.estimator__cta:hover svg { transform: translateX(3px); }
.estimator__cta:active, .estimator__submit:active { transform: scale(0.98); }
.estimator__fine { margin: 1rem 0 0; color: var(--text-inverse-muted); font-size: 0.8125rem; line-height: 1.5; text-align: center; }
.estimator__nojs { display: none; margin: 1.25rem 0 0; color: var(--text-inverse-muted); line-height: 1.6; }
.estimator__sr { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* No JS: hide live-only parts; the form posts to /estimate. JS on: the submit waits (3s failsafe) */
@media (scripting: none) {
  .estimator__live-only, .estimator__badge, .estimator__peek { display: none; }
  .estimator__nojs { display: block; }
  .estimator__cta { margin-top: 0.75rem; background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); }
}
@media (scripting: enabled) {
  .estimator:not(.estimator--js) .estimator__submit { overflow: clip; animation: estimator-failsafe 1ms 3s both; }
}

@container (min-width: 32rem) {
  .estimator__tiers { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .estimator__tier { grid-template-columns: 1fr; align-content: start; }
  .estimator__tier-cost { order: -1; }
}
@container (min-width: 40rem) {
  .estimator__live-only { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); grid-template-areas: "total breakdown" "range breakdown" "finance breakdown"; column-gap: 2rem; align-items: start; }
  .estimator__total { grid-area: total; }
  .estimator__range-line { grid-area: range; }
  .estimator__finance { grid-area: finance; }
  .estimator__breakdown { grid-area: breakdown; }
}
@media (min-width: 768px) {
  .estimator__controls { padding-inline: 1.75rem; }
  .estimator__result { padding: 2rem; }
}
@media (min-width: 1024px) {
  .estimator__form { grid-template-columns: minmax(0, 1.12fr) minmax(0, 0.88fr); gap: 2rem; }
  .estimator__result { position: sticky; top: 1.5rem; }
  .estimator__peek { display: none; }
}

/* The failsafe is an instant step, not motion, so it stays on under prefers-reduced-motion */
@keyframes estimator-failsafe { from { visibility: hidden; max-height: 0; margin: 0; padding: 0; } }
```

## JS

```js
const TIERS = { standard: 1, premium: 1.35, luxury: 1.85 };
const SPRING = 'cubic-bezier(0.34, 1.56, 0.64, 1)';
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const usd = (n) => `$${Math.round(n).toLocaleString('en-US')}`;
const near = (n, step) => Math.round(n / step) * step;

document.querySelectorAll('[data-estimator]').forEach((root) => {
  const $ = (s) => root.querySelector(s);
  const form = $('.estimator__form'), size = form.elements.size, baths = form.elements.baths;
  const odometer = $('.estimator__odometer'), slider = $('.estimator__slider');
  const [minus, plus] = root.querySelectorAll('.estimator__step');
  let timer = 0, first = true;

  // Live results replace the round trip, so the no-JS submit stands down
  root.classList.add('estimator--js');
  $('.estimator__submit').hidden = true;
  form.addEventListener('submit', (e) => e.preventDefault());
  const clampBaths = () => Math.min(+baths.max, Math.max(+baths.min, Math.round(+baths.value) || +baths.min));

  // Demo price model: labour and materials scale with size, bathrooms and tier; add-ons split evenly; permits ≈ 2.5% + filing
  const price = () => {
    const sqft = +size.value, n = clampBaths(), tier = TIERS[form.elements.tier.value];
    let labour = sqft * 1.8 + n * 650, materials = (sqft * 1.4 + n * 900) * tier;
    form.querySelectorAll('[name="addons"]:checked').forEach((box) => {
      const cost = box.dataset.cost * ({ bath: n, sqft }[box.dataset.per] || 1);
      labour += cost / 2;
      materials += cost / 2;
    });
    const permits = (labour + materials) * 0.025 + 180;
    return { labour, materials, permits, total: labour + materials + permits };
  };

  // Odometer: one column per digit (a 0–9 strip); columns roll to their digit, rippling in from the right
  const roll = (text) => {
    const chars = [...text];
    if (odometer.children.length !== chars.length) {
      odometer.innerHTML = chars.map((c) => (/\d/.test(c)
        ? `<span class="estimator__digit"><span>${'0123456789'.replace(/\d/g, '<span>$&</span>')}</span></span>`
        : `<span>${c}</span>`)).join('');
      if (!first) void odometer.offsetWidth; // fresh columns start at 0 and roll up (not on load)
    }
    [...odometer.children].forEach((col, i) => {
      if (!/\d/.test(chars[i])) return;
      col.style.setProperty('--estimator-d', chars[i]);
      col.style.setProperty('--estimator-i', chars.length - i);
    });
  };

  const render = () => {
    const p = price(), total = near(p.total, 100), low = near(p.total * 0.91, 100), high = near(p.total * 1.1, 100);
    const rate = 0.0799 / 12, monthly = (p.total * rate) / (1 - (1 + rate) ** -60);
    const sqft = (+size.value).toLocaleString('en-US');
    roll(usd(total));
    root.querySelectorAll('.estimator__total-text, .estimator__peek-total').forEach((el) => { el.textContent = usd(total); });
    $('.estimator__range-text').textContent = `${usd(low)} – ${usd(high)}`;
    $('.estimator__monthly').textContent = `${usd(monthly)}/mo`;
    $('.estimator__bar').style.gridTemplateColumns = `${p.labour}fr ${p.materials}fr ${p.permits}fr`;
    root.querySelectorAll('[data-part]').forEach((dd) => { dd.textContent = usd(near(p[dd.dataset.part], 10)); });
    slider.style.setProperty('--estimator-p', (size.value - size.min) / (size.max - size.min));
    $('.estimator__bubble').textContent = `${sqft} sq ft`;
    size.setAttribute('aria-valuetext', `${sqft} square feet`);
    minus.setAttribute('aria-disabled', String(clampBaths() <= +baths.min));
    plus.setAttribute('aria-disabled', String(clampBaths() >= +baths.max));
    if (first) { first = false; return; }
    if (!reduce.matches) $('.estimator__ping').animate({ transform: ['scale(1)', 'scale(3)'], opacity: [0.8, 0] }, { duration: 700, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' });
    // One calm summary for screen readers once the input settles
    clearTimeout(timer);
    timer = setTimeout(() => {
      $('.estimator__live').textContent = `Estimated total ${usd(total)}, typical range ${usd(low)} to ${usd(high)}, or about ${usd(monthly)} a month.`;
    }, 800);
  };

  // Stepper: −/+ drive the native number input; a press at the limit nudges instead
  [minus, plus].forEach((btn) => btn.addEventListener('click', () => {
    const before = baths.value;
    if (btn === plus) baths.stepUp(); else baths.stepDown();
    if (reduce.matches) return render();
    if (baths.value === before) baths.animate({ transform: ['none', `translateX(${btn === plus ? 4 : -4}px)`, 'none'] }, { duration: 260, easing: 'ease-out' });
    else baths.animate({ transform: ['scale(1.35)', 'none'] }, { duration: 420, easing: SPRING });
    render();
  }));
  baths.addEventListener('change', () => { baths.value = clampBaths(); render(); });
  form.addEventListener('input', render);
  render();
});
```

## Notes

- Native inputs throughout: a labelled range with `aria-valuetext` ("1,800 square feet"), a number input whose −/+ buttons call `stepDown()`/`stepUp()` (named, `aria-controls`, `aria-disabled` at the limits), the material tier as a radio group in `fieldset`/`legend`, and add-ons as checkboxes with `role="switch"`. The odometer and bar are `aria-hidden`; a visually hidden total and the legend carry the values, and one polite live summary is spoken 800ms after input settles.
- Without JS the form submits to `/estimate` (GET, so results are linkable) and the card shows a "Calculate my estimate" button instead of stale figures. With JS the figures are already rendered for the defaults, so nothing flashes on load, and the submit button only reappears through a 3s CSS failsafe if the script never runs.
- Reduced motion: digits, bar, springs and bubble move instantly (token durations), and the update ping and stepper nudges are skipped.
- Contrast: on the result card, `--text-inverse` stays ≥ 13:1 and `--text-inverse-muted` ≥ 5.3:1 where the 30–34% brand light is strongest. The off switch track is ≥ 3:1 against white, the thumb ring and checked track use `--primary` (5.2:1), and the bar colours are ≥ 3:1 against `--surface-deep`.
- The price model in `price()` is illustrative: replace the rates, `TIERS` and the add-ons' `data-cost`/`data-per` with your own, or fetch a quote and pass the numbers to `render`. `grid-template-columns` interpolation (Chrome 107+, Safari 16+, Firefox 66+) animates the bar; older browsers snap.
