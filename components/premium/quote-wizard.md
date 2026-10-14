# Quote Wizard

A "Get your estimate" flow in one form on a light card over a soft gradient. Four steps (service, job details, contact, review) slide in from the side you're travelling to while the card's height glides to fit, under a gradient progress line whose dots draw their checks. A dark estimate pill re-rolls its price ("$240–$380") on every change, invalid steps shake with linked messages, and sending draws a check. On phones the service cards go two-up and the contact fields stack; without JS it's one long, fully working form. Depends on `tokens/variables.css`.

**Motion:** direction-aware step slide + viewport height glide (WAAPI, `--ease-out`) · progress fill (`--dur-5`) and dot check draw · estimate roll (translate + blur) · option badge and segmented pill springs (`--ease-spring`) · floating labels (`--dur-3`) · error shake · review rows stagger (`--stagger`) · success ring and check draw.

## HTML

```html
<section class="quote-wizard" aria-labelledby="quote-wizard-title" data-quote-wizard>
  <div class="quote-wizard__inner">
    <div class="quote-wizard__card">
      <header class="quote-wizard__head">
        <div>
          <p class="quote-wizard__eyebrow">Free · no obligation · 2 minutes</p>
          <h2 id="quote-wizard-title" class="quote-wizard__title">Get your estimate</h2>
        </div>
        <p class="quote-wizard__pill"><span class="quote-wizard__pill-label">Estimate</span> <span class="quote-wizard__chip"><strong class="quote-wizard__amount">From $120</strong></span></p>
      </header>

      <div class="quote-wizard__progress" aria-hidden="true">
        <span class="quote-wizard__bar"><span class="quote-wizard__fill"></span></span>
        <ol class="quote-wizard__dots" role="list">
          <li class="quote-wizard__dot"><span class="quote-wizard__mark"><span>1</span><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>Service</li>
          <li class="quote-wizard__dot"><span class="quote-wizard__mark"><span>2</span><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>Details</li>
          <li class="quote-wizard__dot"><span class="quote-wizard__mark"><span>3</span><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>Contact</li>
          <li class="quote-wizard__dot"><span class="quote-wizard__mark"><span>4</span><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg></span>Review</li>
        </ol>
      </div>

      <form class="quote-wizard__form" action="/quote" method="post">
        <div class="quote-wizard__viewport">
          <!-- Step 1: service (radio cards) -->
          <fieldset class="quote-wizard__step" role="radiogroup">
            <legend class="quote-wizard__legend"><span class="quote-wizard__count">Step 1 of 4</span><h3 class="quote-wizard__step-title" tabindex="-1">What do you need help with?</h3></legend>
            <div class="quote-wizard__field" data-error="Choose a service to continue.">
              <div class="quote-wizard__options">
                <label class="quote-wizard__option">
                  <input type="radio" name="service" value="Plumbing" data-low="180" data-high="280" required>
                  <span class="quote-wizard__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M12 3s6 6.4 6 11a6 6 0 0 1-12 0c0-4.6 6-11 6-11z" /><path d="M9.5 14.5a2.5 2.5 0 0 0 2.5 2.5" /></svg></span>
                  <span class="quote-wizard__option-name">Plumbing</span>
                  <small class="quote-wizard__note">Leaks, drains, water heaters</small>
                  <small class="quote-wizard__from">from $180</small>
                </label>
                <label class="quote-wizard__option">
                  <input type="radio" name="service" value="Electrical" data-low="200" data-high="320" required>
                  <span class="quote-wizard__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg></span>
                  <span class="quote-wizard__option-name">Electrical</span>
                  <small class="quote-wizard__note">Outlets, lighting, panels</small>
                  <small class="quote-wizard__from">from $200</small>
                </label>
                <label class="quote-wizard__option">
                  <input type="radio" name="service" value="Heating &amp; cooling" data-low="240" data-high="380" required>
                  <span class="quote-wizard__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M14 14.8V5a2 2 0 0 0-4 0v9.8a4 4 0 1 0 4 0z" /><path d="M12 9v7" /></svg></span>
                  <span class="quote-wizard__option-name">Heating &amp; cooling</span>
                  <small class="quote-wizard__note">Furnaces, AC, heat pumps</small>
                  <small class="quote-wizard__from">from $240</small>
                </label>
                <label class="quote-wizard__option">
                  <input type="radio" name="service" value="Roofing" data-low="450" data-high="900" required>
                  <span class="quote-wizard__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="m2 11 10-7 10 7" /><path d="M5 9.5V20h14V9.5M10 20v-5h4v5" /></svg></span>
                  <span class="quote-wizard__option-name">Roofing</span>
                  <small class="quote-wizard__note">Repairs, gutters, storm damage</small>
                  <small class="quote-wizard__from">from $450</small>
                </label>
                <label class="quote-wizard__option">
                  <input type="radio" name="service" value="Painting" data-low="320" data-high="560" required>
                  <span class="quote-wizard__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M4 4h13v5H4z" /><path d="M17 6.5h3v5h-9v3" /><path d="M10 14.5h2V21h-2z" /></svg></span>
                  <span class="quote-wizard__option-name">Painting</span>
                  <small class="quote-wizard__note">Rooms, trim, exteriors</small>
                  <small class="quote-wizard__from">from $320</small>
                </label>
                <label class="quote-wizard__option">
                  <input type="radio" name="service" value="Handyman" data-low="120" data-high="220" required>
                  <span class="quote-wizard__icon"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z" /></svg></span>
                  <span class="quote-wizard__option-name">Handyman</span>
                  <small class="quote-wizard__note">Odd jobs, assembly, fixes</small>
                  <small class="quote-wizard__from">from $120</small>
                </label>
              </div>
              <p class="quote-wizard__error"></p>
            </div>
          </fieldset>

          <!-- Step 2: size slider + urgency segmented control -->
          <fieldset class="quote-wizard__step">
            <legend class="quote-wizard__legend"><span class="quote-wizard__count">Step 2 of 4</span><h3 class="quote-wizard__step-title" tabindex="-1">Tell us about the job</h3></legend>
            <label class="quote-wizard__size">
              <span class="quote-wizard__size-head">
                <span class="quote-wizard__size-label">How big is the job?</span>
                <span class="quote-wizard__size-value" aria-hidden="true">Medium · about half a day</span>
              </span>
              <input class="quote-wizard__range" type="range" name="size" min="1" max="5" step="1" value="3" aria-valuetext="Medium, about half a day">
              <span class="quote-wizard__ticks" aria-hidden="true"><span>Quick fix</span><span>Small</span><span>Medium</span><span>Large</span><span>Project</span></span>
            </label>
            <fieldset class="quote-wizard__urgency">
              <legend class="quote-wizard__urgency-label">How soon do you need us?</legend>
              <div class="quote-wizard__seg">
                <span class="quote-wizard__seg-pill" aria-hidden="true"></span>
                <label class="quote-wizard__seg-option"><input type="radio" name="urgency" value="Flexible" data-factor="0.9"><span class="quote-wizard__seg-body">Flexible<small>Save 10%</small></span></label>
                <label class="quote-wizard__seg-option"><input type="radio" name="urgency" value="This week" data-factor="1" checked><span class="quote-wizard__seg-body">This week<small>Standard</small></span></label>
                <label class="quote-wizard__seg-option"><input type="radio" name="urgency" value="Within 24 hours" data-factor="1.35"><span class="quote-wizard__seg-body">Within 24h<small>Priority</small></span></label>
              </div>
            </fieldset>
          </fieldset>

          <!-- Step 3: contact (floating labels) -->
          <fieldset class="quote-wizard__step">
            <legend class="quote-wizard__legend"><span class="quote-wizard__count">Step 3 of 4</span><h3 class="quote-wizard__step-title" tabindex="-1">Where can we reach you?</h3></legend>
            <div class="quote-wizard__fields">
              <div class="quote-wizard__field" data-error="Tell us your name.">
                <label class="quote-wizard__float"><input class="quote-wizard__input" name="name" autocomplete="name" placeholder=" " required><span class="quote-wizard__label">Full name</span></label>
                <p class="quote-wizard__error"></p>
              </div>
              <div class="quote-wizard__field" data-error="Enter a 5-digit ZIP code.">
                <label class="quote-wizard__float"><input class="quote-wizard__input" name="zip" autocomplete="postal-code" inputmode="numeric" pattern="\d{5}" maxlength="5" placeholder=" " required><span class="quote-wizard__label">ZIP code</span></label>
                <p class="quote-wizard__error"></p>
              </div>
              <div class="quote-wizard__field" data-error="Enter a 10-digit number, like (555) 555-0123.">
                <label class="quote-wizard__float"><input class="quote-wizard__input" name="phone" type="tel" autocomplete="tel" pattern="\(?\d{3}\)?[\s.\-]?\d{3}[\s.\-]?\d{4}" placeholder=" " required><span class="quote-wizard__label">Phone</span></label>
                <p class="quote-wizard__error"></p>
              </div>
              <div class="quote-wizard__field" data-error="Check the email, like hello@example.com.">
                <label class="quote-wizard__float"><input class="quote-wizard__input" name="email" type="email" autocomplete="email" placeholder=" "><span class="quote-wizard__label">Email (optional)</span></label>
                <p class="quote-wizard__error"></p>
              </div>
              <label class="quote-wizard__float quote-wizard__float--wide"><textarea class="quote-wizard__input" name="notes" rows="2" placeholder=" "></textarea><span class="quote-wizard__label">Anything we should know? (optional)</span></label>
            </div>
          </fieldset>

          <!-- Step 4: review and send -->
          <fieldset class="quote-wizard__step">
            <legend class="quote-wizard__legend"><span class="quote-wizard__count">Step 4 of 4</span><h3 class="quote-wizard__step-title" tabindex="-1">Check and send</h3></legend>
            <dl class="quote-wizard__review" hidden>
              <div class="quote-wizard__row" style="--quote-wizard-i: 0"><dt>Service</dt><dd><span data-review="service"></span><button class="quote-wizard__edit" type="button" data-goto="0">Edit<span class="quote-wizard__sr"> service</span></button></dd></div>
              <div class="quote-wizard__row" style="--quote-wizard-i: 1"><dt>The job</dt><dd><span data-review="job"></span><button class="quote-wizard__edit" type="button" data-goto="1">Edit<span class="quote-wizard__sr"> job details</span></button></dd></div>
              <div class="quote-wizard__row" style="--quote-wizard-i: 2"><dt>Contact</dt><dd><span data-review="contact"></span><button class="quote-wizard__edit" type="button" data-goto="2">Edit<span class="quote-wizard__sr"> contact details</span></button></dd></div>
            </dl>
            <p class="quote-wizard__total" hidden><span>Your estimate</span><strong class="quote-wizard__amount">From $120</strong><small>The final price is agreed on site, before any work starts.</small></p>
            <p class="quote-wizard__fine">We'll call or text within 2 business hours to confirm a time. No spam, ever.</p>
          </fieldset>
        </div>

        <div class="quote-wizard__nav">
          <button class="quote-wizard__back" type="button" hidden>
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M19 12H5M11 6l-6 6 6 6" /></svg>Back
          </button>
          <button class="quote-wizard__next" type="button" hidden>
            Next<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </button>
          <button class="quote-wizard__submit" type="submit">
            Send my request<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4z" /></svg>
          </button>
        </div>
      </form>

      <div class="quote-wizard__done" hidden>
        <svg class="quote-wizard__tick" viewBox="0 0 64 64" width="76" height="76" aria-hidden="true" focusable="false"><circle cx="32" cy="32" r="28" pathLength="1" /><path d="m21 33 8 8 15-17" pathLength="1" /></svg>
        <h3 class="quote-wizard__done-title" tabindex="-1">Request sent</h3>
        <p class="quote-wizard__done-text">Thanks! A coordinator will call you within 2 business hours to lock in a time. Your estimate: <strong class="quote-wizard__amount">From $120</strong>.</p>
        <button class="quote-wizard__restart" type="button">Start a new estimate</button>
      </div>

      <p class="quote-wizard__sr quote-wizard__live" aria-live="polite"></p>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: a soft gradient field behind one white card */
.quote-wizard {
  --quote-wizard-grad: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  --quote-wizard-fill-image: var(--quote-wizard-grad);
  --quote-wizard-pad: 1.25rem;
  --quote-wizard-thumb: 1.75rem;
  background:
    radial-gradient(60% 50% at 0% 0%, color-mix(in srgb, var(--primary) 16%, transparent), transparent 70%),
    radial-gradient(55% 55% at 100% 35%, color-mix(in srgb, var(--primary-2) 16%, transparent), transparent 70%),
    radial-gradient(50% 40% at 40% 100%, color-mix(in srgb, var(--accent) 12%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.quote-wizard__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3rem, 8vw, 6rem) var(--gutter); }
:where(.quote-wizard) svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.quote-wizard :is(button, .quote-wizard__input):focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Card */
.quote-wizard__card {
  position: relative; box-sizing: border-box; container-type: inline-size; max-width: 42rem; margin-inline: auto; padding: var(--quote-wizard-pad);
  border-radius: var(--radius-2xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.quote-wizard__card::before { /* a thread of brand light along the top edge */
  content: ""; position: absolute; inset: 0 12% auto; height: 1px; pointer-events: none;
  background: linear-gradient(90deg, transparent, var(--primary), var(--primary-2), transparent);
}

/* Header with the live estimate pill */
.quote-wizard__head { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 1rem; }
.quote-wizard__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.quote-wizard__title { margin: 0.5rem 0 0; font: 600 clamp(1.75rem, 1.4rem + 1.4vw, 2.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); }
.quote-wizard__pill {
  display: inline-flex; align-items: center; gap: 0.625rem; margin: 0; padding: 0.3125rem 0.3125rem 0.3125rem 0.875rem; border-radius: var(--radius-full);
  background: var(--text-main); color: var(--surface-light);
  box-shadow: var(--highlight-inverse), 0 14px 30px -16px color-mix(in srgb, var(--primary) 90%, transparent);
}
.quote-wizard__pill-label { color: color-mix(in srgb, var(--surface-light) 70%, var(--text-main)); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.quote-wizard__chip {
  display: inline-block; min-width: 6.75rem; overflow: hidden; padding: 0.5rem 0.875rem; border-radius: var(--radius-full); text-align: center;
  background: color-mix(in srgb, var(--surface-light) 12%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse);
}
.quote-wizard__chip .quote-wizard__amount { display: inline-block; font: 600 1rem/1 var(--font-display); font-variant-numeric: tabular-nums; letter-spacing: var(--tracking-tight); white-space: nowrap; }

/* Progress: a gradient line fills between numbered dots, which draw a check when done */
.quote-wizard__progress { position: relative; margin: 1.75rem 0 2rem; }
.quote-wizard__bar { position: absolute; top: 0.875rem; left: 12.5%; right: 12.5%; height: 2px; translate: 0 -50%; overflow: hidden; border-radius: 2px; background: var(--border-subtle); }
.quote-wizard__fill { position: absolute; inset: 0; background: var(--quote-wizard-grad); transform: scaleX(var(--quote-wizard-progress, 0)); transform-origin: left; transition: transform var(--dur-5) var(--ease-out); }
.quote-wizard__dots { position: relative; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); margin: 0; padding: 0; list-style: none; }
.quote-wizard__dot { display: grid; justify-items: center; gap: 0.5rem; color: var(--text-muted); font-size: 0.75rem; font-weight: 500; transition: color var(--dur-3); }
.quote-wizard__mark {
  display: grid; place-items: center; width: 1.75rem; height: 1.75rem; border-radius: 50%;
  background: var(--surface-light); box-shadow: inset 0 0 0 1.5px var(--border-subtle); font: 600 0.75rem/1 var(--font-mono);
  transition: background-color var(--dur-3), box-shadow var(--dur-3), color var(--dur-3), transform var(--dur-4) var(--ease-spring);
}
.quote-wizard__mark > * { grid-area: 1 / 1; }
.quote-wizard__mark span { transition: opacity var(--dur-2), scale var(--dur-3) var(--ease-out); }
.quote-wizard__mark svg { stroke-width: 3; stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset var(--dur-4) var(--ease-out) var(--dur-2); }
.quote-wizard__dot.is-current, .quote-wizard__dot.is-done { color: var(--text-main); }
.quote-wizard__dot.is-current .quote-wizard__mark { color: var(--primary); box-shadow: inset 0 0 0 2px var(--primary), 0 0 0 5px color-mix(in srgb, var(--primary) 14%, transparent); transform: scale(1.1); }
.quote-wizard__dot.is-done .quote-wizard__mark { background: var(--quote-wizard-grad); color: var(--text-inverse); box-shadow: 0 6px 14px -6px color-mix(in srgb, var(--primary) 70%, transparent); }
.quote-wizard__dot.is-done .quote-wizard__mark span { opacity: 0; scale: 0.5; }
.quote-wizard__dot.is-done .quote-wizard__mark svg { stroke-dashoffset: 0; }

/* Steps: stacked with JS (one grid cell, slid by script); a long form without it */
.quote-wizard__form[hidden] { display: none; }
.quote-wizard__viewport { box-sizing: border-box; }
.quote-wizard--js .quote-wizard__viewport { display: grid; align-items: start; }
.quote-wizard--js .quote-wizard__step { grid-area: 1 / 1; }
.quote-wizard__viewport.is-moving { overflow: clip; }
.quote-wizard__step { min-width: 0; margin: 0; padding: 0; border: 0; }
.quote-wizard:not(.quote-wizard--js) .quote-wizard__step + .quote-wizard__step { margin-top: 2.25rem; padding-top: 2rem; border-top: 1px dashed var(--border-subtle); }
.quote-wizard__legend { margin-bottom: 1.25rem; padding: 0; }
.quote-wizard__count { display: block; color: var(--text-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.quote-wizard__step-title { margin: 0.5rem 0 0; font: 600 1.375rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.quote-wizard__step-title:focus, .quote-wizard__done-title:focus { outline: none; }

/* Step 1: service cards */
.quote-wizard__options { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.625rem; }
.quote-wizard__option {
  position: relative; display: grid; align-content: start; gap: 0.25rem; min-height: 7.5rem; padding: 0.875rem; border-radius: var(--radius-xl); cursor: pointer;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: background-color var(--dur-3), box-shadow var(--dur-3), transform var(--dur-3) var(--ease-spring);
}
.quote-wizard__option input { position: absolute; opacity: 0; pointer-events: none; }
.quote-wizard__icon {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; margin-bottom: 0.5rem; border-radius: var(--radius-lg);
  background: color-mix(in srgb, var(--primary) 9%, transparent); color: var(--primary);
  transition: background-color var(--dur-3), color var(--dur-3), transform var(--dur-4) var(--ease-spring);
}
.quote-wizard__option-name { font-size: 0.9375rem; font-weight: 600; line-height: 1.25; }
.quote-wizard__note { display: none; color: var(--text-muted); font-size: 0.8125rem; line-height: 1.4; }
.quote-wizard__from { margin-top: auto; padding-top: 0.375rem; color: var(--text-muted); font: 500 0.75rem var(--font-mono); }
.quote-wizard__option::before, .quote-wizard__option::after { /* check badge: gradient disc + drawn tick */
  content: ""; position: absolute; opacity: 0; transition: opacity var(--dur-2), transform var(--dur-4) var(--ease-spring);
}
.quote-wizard__option::after { top: 0.75rem; right: 0.75rem; width: 1.375rem; height: 1.375rem; border-radius: 50%; background: var(--quote-wizard-grad); transform: scale(0); }
.quote-wizard__option::before { z-index: 1; top: 1.0625rem; right: 1.25rem; width: 0.3125rem; height: 0.5625rem; border: solid var(--text-inverse); border-width: 0 2px 2px 0; transform: rotate(45deg) scale(0); }
.quote-wizard__option:hover { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 40%, var(--border-subtle)), var(--shadow-md); transform: translateY(-2px); }
.quote-wizard__option:active { transform: scale(0.97); }
.quote-wizard__option:has(:checked) { background: color-mix(in srgb, var(--primary) 5%, var(--surface-light)); box-shadow: inset 0 0 0 2px var(--primary), 0 12px 24px -14px color-mix(in srgb, var(--primary) 70%, transparent); }
.quote-wizard__option:has(:checked)::after { opacity: 1; transform: scale(1); }
.quote-wizard__option:has(:checked)::before { opacity: 1; transform: rotate(45deg) scale(1); }
.quote-wizard__option:has(:checked) .quote-wizard__icon { background: var(--quote-wizard-grad); color: var(--text-inverse); transform: scale(1.06) rotate(-6deg); }
.quote-wizard__option:has(:focus-visible) { outline: 2px solid transparent; box-shadow: var(--focus-ring), inset 0 0 0 2px var(--primary); }
.quote-wizard__field.is-invalid .quote-wizard__option { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--danger) 50%, var(--border-subtle)); }

/* Step 2: size slider with a gradient fill, urgency as a segmented control */
.quote-wizard__size { display: grid; gap: 0.5rem; }
.quote-wizard__size-head { display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 0.25rem 1rem; }
.quote-wizard__size-label, .quote-wizard__urgency-label { font-size: 0.9375rem; font-weight: 600; }
.quote-wizard__size-value { color: var(--primary); font: 600 0.8125rem var(--font-mono); }
.quote-wizard__range { width: 100%; height: 2.75rem; margin: 0; background: none; cursor: pointer; -webkit-appearance: none; appearance: none; }
.quote-wizard__range:focus-visible { outline: 2px solid transparent; }
.quote-wizard__range::-webkit-slider-runnable-track {
  height: 0.5rem; border-radius: var(--radius-full);
  background: var(--quote-wizard-fill-image) 0 0 / calc(var(--quote-wizard-thumb) / 2 + (100% - var(--quote-wizard-thumb)) * var(--quote-wizard-fill, 0.5)) 100% no-repeat, var(--border-subtle);
}
.quote-wizard__range::-moz-range-track {
  height: 0.5rem; border-radius: var(--radius-full);
  background: var(--quote-wizard-fill-image) 0 0 / calc(var(--quote-wizard-thumb) / 2 + (100% - var(--quote-wizard-thumb)) * var(--quote-wizard-fill, 0.5)) 100% no-repeat, var(--border-subtle);
}
.quote-wizard__range::-webkit-slider-thumb {
  width: var(--quote-wizard-thumb); height: var(--quote-wizard-thumb); margin-top: calc((0.5rem - var(--quote-wizard-thumb)) / 2); border: 0; border-radius: 50%; -webkit-appearance: none; appearance: none;
  background: var(--surface-light); box-shadow: inset 0 0 0 2px var(--primary), 0 6px 14px -4px color-mix(in srgb, var(--primary) 60%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2);
}
.quote-wizard__range::-moz-range-thumb {
  width: var(--quote-wizard-thumb); height: var(--quote-wizard-thumb); border: 0; border-radius: 50%;
  background: var(--surface-light); box-shadow: inset 0 0 0 2px var(--primary), 0 6px 14px -4px color-mix(in srgb, var(--primary) 60%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2);
}
.quote-wizard__range:active::-webkit-slider-thumb { transform: scale(1.15); }
.quote-wizard__range:active::-moz-range-thumb { transform: scale(1.15); }
.quote-wizard__range:focus-visible::-webkit-slider-thumb { box-shadow: inset 0 0 0 2px var(--primary), var(--focus-ring); }
.quote-wizard__range:focus-visible::-moz-range-thumb { box-shadow: inset 0 0 0 2px var(--primary), var(--focus-ring); }
.quote-wizard__ticks { display: flex; justify-content: space-between; padding-inline: calc(var(--quote-wizard-thumb) / 2); color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); }
.quote-wizard__ticks span { display: flex; justify-content: center; width: 0; white-space: nowrap; }
.quote-wizard__ticks span:not(:first-child, :last-child) { visibility: hidden; }
.quote-wizard__ticks span:first-child { justify-content: flex-start; margin-left: calc(var(--quote-wizard-thumb) / -2); }
.quote-wizard__ticks span:last-child { justify-content: flex-end; margin-right: calc(var(--quote-wizard-thumb) / -2); }

.quote-wizard__urgency { min-width: 0; margin: 1.75rem 0 0; padding: 0; border: 0; }
.quote-wizard__urgency-label { margin-bottom: 0.75rem; padding: 0; }
.quote-wizard__seg { position: relative; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); padding: 0.25rem; border-radius: var(--radius-xl); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.quote-wizard__seg-pill {
  position: absolute; top: 0.25rem; bottom: 0.25rem; left: 0.25rem; width: calc((100% - 0.5rem) / 3); border-radius: var(--radius-lg);
  background: var(--surface-light); box-shadow: var(--shadow-md), inset 0 0 0 1px var(--border-subtle);
  transition: transform var(--dur-4) var(--ease-spring);
}
.quote-wizard__seg:has(.quote-wizard__seg-option:nth-of-type(2) :checked) .quote-wizard__seg-pill { transform: translateX(100%); }
.quote-wizard__seg:has(.quote-wizard__seg-option:nth-of-type(3) :checked) .quote-wizard__seg-pill { transform: translateX(200%); }
.quote-wizard__seg-option { position: relative; cursor: pointer; }
.quote-wizard__seg-option input { position: absolute; opacity: 0; pointer-events: none; }
.quote-wizard__seg-body {
  display: grid; align-content: center; justify-items: center; gap: 0.25rem; min-height: 3.25rem; padding: 0.5rem 0.25rem; border-radius: var(--radius-lg);
  color: var(--text-muted); font-size: 0.875rem; font-weight: 600; text-align: center; transition: color var(--dur-3), box-shadow var(--dur-2);
}
.quote-wizard__seg-body small { font: 500 0.6875rem/1 var(--font-mono); }
.quote-wizard__seg-option input:checked + .quote-wizard__seg-body { color: var(--text-main); }
.quote-wizard__seg-option input:checked + .quote-wizard__seg-body small { color: var(--primary); }
.quote-wizard__seg-option input:focus-visible + .quote-wizard__seg-body { box-shadow: var(--focus-ring); }
@supports not selector(:has(*)) {
  .quote-wizard__seg-pill { display: none; }
  .quote-wizard__seg-option input:checked + .quote-wizard__seg-body { background: var(--surface-light); box-shadow: var(--shadow-md); }
}

/* Step 3: floating labels, a tick on valid fields, inline errors */
.quote-wizard__fields { display: grid; gap: 0.875rem; }
.quote-wizard__float { position: relative; display: block; }
.quote-wizard__float--wide { grid-column: 1 / -1; }
.quote-wizard__input {
  box-sizing: border-box; display: block; width: 100%; height: 3.5rem; padding: 1.375rem 2.5rem 0.375rem 0.875rem; border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-light); color: var(--text-main); font: 500 1rem/1.3 var(--font-sans);
  transition: border-color var(--dur-2), box-shadow var(--dur-2);
}
.quote-wizard__float--wide .quote-wizard__input { height: auto; min-height: 5.75rem; padding-top: 1.625rem; resize: vertical; field-sizing: content; }
.quote-wizard__input:hover { border-color: color-mix(in srgb, var(--text-muted) 45%, var(--border-subtle)); }
.quote-wizard__input:focus-visible { border-color: var(--primary); }
.quote-wizard__label {
  position: absolute; top: 1.0625rem; left: 0.875rem; right: 2.5rem; overflow: hidden; pointer-events: none;
  color: var(--text-muted); font-size: 1rem; line-height: 1.3; white-space: nowrap; text-overflow: ellipsis;
  transform-origin: 0 0; transition: transform var(--dur-3) var(--ease-out), color var(--dur-2);
}
.quote-wizard__input:focus + .quote-wizard__label, .quote-wizard__input:not(:placeholder-shown) + .quote-wizard__label { transform: translateY(-0.625rem) scale(0.75); }
.quote-wizard__input:focus + .quote-wizard__label { color: var(--primary); }
.quote-wizard__float::after {
  content: ""; position: absolute; top: 50%; right: 0.875rem; width: 1.125rem; height: 1.125rem; margin-top: -0.5625rem; pointer-events: none;
  background: var(--success); scale: 0; transition: scale var(--dur-4) var(--ease-spring);
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m5 12.5 4.5 4.5L19 7.5'/%3E%3C/svg%3E") center / contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='m5 12.5 4.5 4.5L19 7.5'/%3E%3C/svg%3E") center / contain no-repeat;
}
.quote-wizard__float:has(.quote-wizard__input:valid:not(:placeholder-shown))::after { scale: 1; }
.quote-wizard__float--wide::after { content: none; }
.quote-wizard__error { display: flex; align-items: center; gap: 0.375rem; margin: 0.5rem 0 0; color: var(--danger); font-size: 0.8125rem; font-weight: 500; }
.quote-wizard__error:empty { display: none; }
.quote-wizard__error::before {
  content: "!"; content: "!" / ""; flex: none; display: grid; place-items: center; width: 1rem; height: 1rem; border-radius: 50%;
  background: var(--danger); color: var(--surface-light); font: 700 0.6875rem/1 var(--font-sans);
}
.quote-wizard__field.is-invalid .quote-wizard__input { border-color: var(--danger); }

/* Step 4: review rows stagger in, each with an Edit jump */
.quote-wizard__review { margin: 0; border-radius: var(--radius-xl); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.quote-wizard__review[hidden], .quote-wizard__total[hidden] { display: none; }
.quote-wizard__row { display: grid; gap: 0.375rem; padding: 0.875rem 1rem; }
.quote-wizard__row + .quote-wizard__row { border-top: 1px solid var(--border-subtle); }
.quote-wizard__row dt { color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.quote-wizard__row dd { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin: 0; font-weight: 500; line-height: 1.4; overflow-wrap: anywhere; }
.quote-wizard__step:not([hidden]) .quote-wizard__row { animation: quote-wizard-in var(--dur-4) var(--ease-out) calc(var(--quote-wizard-i, 0) * var(--stagger) + 120ms) backwards; }
.quote-wizard__edit {
  flex: none; min-height: 2rem; padding: 0 0.75rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: color-mix(in srgb, var(--primary) 8%, transparent); color: var(--primary-hover); font: 600 0.8125rem var(--font-sans);
  transition: background-color var(--dur-2);
}
.quote-wizard__edit:hover { background: color-mix(in srgb, var(--primary) 14%, transparent); }
.quote-wizard__total { display: grid; gap: 0.375rem; margin: 1rem 0 0; padding: 1rem 1.125rem; border-radius: var(--radius-xl); background: color-mix(in srgb, var(--primary) 4%, var(--surface-light)); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 20%, transparent); }
.quote-wizard__total span { color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.quote-wizard__total .quote-wizard__amount { font: 600 1.875rem/1.1 var(--font-display); font-variant-numeric: tabular-nums; letter-spacing: var(--tracking-tight); }
.quote-wizard__total small { color: var(--text-muted); font-size: 0.8125rem; }
.quote-wizard__fine { margin: 1rem 0 0; color: var(--text-muted); font-size: 0.875rem; line-height: 1.5; }

/* Navigation */
.quote-wizard__nav { display: flex; align-items: center; gap: 0.75rem; margin-top: 1.75rem; padding-top: 1.25rem; border-top: 1px solid var(--border-subtle); }
.quote-wizard__back, .quote-wizard__next, .quote-wizard__submit, .quote-wizard__restart {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  font: 600 0.9375rem var(--font-sans); transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2), box-shadow var(--dur-3);
}
.quote-wizard__nav [hidden] { display: none; }
.quote-wizard__nav svg { transition: transform var(--dur-3) var(--ease-spring); }
.quote-wizard__back { padding-left: 1rem; background: transparent; color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.quote-wizard__back:hover { background: var(--surface-muted); }
.quote-wizard__back:hover svg { transform: translateX(-3px); }
.quote-wizard__next, .quote-wizard__submit {
  margin-left: auto; padding-right: 1.125rem; background: var(--quote-wizard-grad); color: var(--text-inverse);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 12px 26px -12px color-mix(in srgb, var(--primary) 80%, transparent);
}
.quote-wizard__next:hover svg, .quote-wizard__submit:hover svg { transform: translateX(3px); }
.quote-wizard__back:active, .quote-wizard__next:active, .quote-wizard__submit:active, .quote-wizard__restart:active { transform: scale(0.97); }

/* Success: ring and check draw over a soft glow */
.quote-wizard__done { position: relative; display: grid; justify-items: center; gap: 0.75rem; padding: 1.5rem 0 0.5rem; text-align: center; }
.quote-wizard__done[hidden] { display: none; }
.quote-wizard__done::before {
  content: ""; position: absolute; top: -1.5rem; left: 50%; width: 13rem; height: 13rem; translate: -50% 0; border-radius: 50%; pointer-events: none;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--success) 16%, transparent), transparent);
  animation: quote-wizard-pop var(--dur-5) var(--ease-out) both;
}
.quote-wizard__done > * { position: relative; }
.quote-wizard__tick { animation: quote-wizard-pop var(--dur-5) var(--ease-spring) 200ms both; }
.quote-wizard__tick circle, .quote-wizard__tick path { stroke-dasharray: 1; }
.quote-wizard__tick circle { stroke: color-mix(in srgb, var(--success) 28%, transparent); stroke-width: 4; animation: quote-wizard-draw var(--dur-5) var(--ease-out) both; }
.quote-wizard__tick path { stroke: var(--success); stroke-width: 5; animation: quote-wizard-draw var(--dur-4) var(--ease-out) 350ms both; }
.quote-wizard__done-title { margin: 0.25rem 0 0; font: 600 1.75rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.quote-wizard__done-text { max-width: 26rem; margin: 0; color: var(--text-muted); line-height: 1.6; }
.quote-wizard__done-text .quote-wizard__amount { color: var(--text-main); }
.quote-wizard__restart { margin-top: 0.75rem; background: var(--text-main); color: var(--surface-light); }

.quote-wizard__sr { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* JS on: show step 1 only while the script boots; a 3s failsafe restores the long form if it never runs */
@media (scripting: enabled) {
  .quote-wizard:not(.quote-wizard--js) .quote-wizard__step ~ .quote-wizard__step,
  .quote-wizard:not(.quote-wizard--js) .quote-wizard__submit { overflow: clip; animation: quote-wizard-failsafe 1ms 3s both; }
}
/* No JS: no progress, no stale slider readout or fill */
@media (scripting: none) {
  .quote-wizard { --quote-wizard-fill-image: none; }
  .quote-wizard__progress, .quote-wizard__size-value { display: none; }
}

@container (min-width: 28rem) {
  .quote-wizard__ticks span:not(:first-child, :last-child) { visibility: visible; }
  .quote-wizard__fields { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@container (min-width: 34rem) {
  .quote-wizard__options { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .quote-wizard__note { display: block; }
}
@media (min-width: 768px) {
  .quote-wizard { --quote-wizard-pad: 2.25rem; }
}

@media (prefers-reduced-motion: reduce) {
  .quote-wizard__row, .quote-wizard__done::before, .quote-wizard__tick, .quote-wizard__tick circle, .quote-wizard__tick path { animation: none !important; }
}
@keyframes quote-wizard-in { from { opacity: 0; transform: translateY(0.5rem); } }
@keyframes quote-wizard-pop { from { opacity: 0; transform: scale(0.6); } }
@keyframes quote-wizard-draw { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
@keyframes quote-wizard-failsafe { from { visibility: hidden; max-height: 0; margin: 0; padding: 0; border-width: 0; } }
```

## JS

```js
const EASE = 'cubic-bezier(0.16, 1, 0.3, 1)';
const SIZES = [['Quick fix', 'under an hour', 0.5], ['Small', '1–2 hours', 0.75], ['Medium', 'about half a day', 1], ['Large', 'a full day', 1.6], ['Project', '2 days or more', 2.5]];
const SHAKE = { transform: ['translateX(0)', 'translateX(-6px)', 'translateX(5px)', 'translateX(-3px)', 'translateX(0)'] };
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const money = (n) => `$${(Math.round(n / 10) * 10).toLocaleString('en-US')}`;
let uid = 0;

document.querySelectorAll('[data-quote-wizard]').forEach((root) => {
  const $ = (s) => root.querySelector(s);
  const form = $('.quote-wizard__form'), card = $('.quote-wizard__card'), view = $('.quote-wizard__viewport'), done = $('.quote-wizard__done');
  const steps = [...root.querySelectorAll('.quote-wizard__step')], dots = [...root.querySelectorAll('.quote-wizard__dot')];
  const [back, next, submit] = ['back', 'next', 'submit'].map((name) => $(`.quote-wizard__${name}`));
  const pill = $('.quote-wizard__chip .quote-wizard__amount'), range = form.elements.size, last = steps.length - 1;
  const id = `quote-wizard-${++uid}`;
  let cur = 0, timer = 0;

  // Enhance: our own messages instead of native bubbles, each wired to its field by a unique id
  root.classList.add('quote-wizard--js');
  form.noValidate = true;
  root.querySelectorAll('.quote-wizard__review, .quote-wizard__total').forEach((el) => { el.hidden = false; });
  root.querySelectorAll('.quote-wizard__field').forEach((field, i) => {
    const err = field.querySelector('.quote-wizard__error');
    err.id = `${id}-err-${i}`;
    (field.closest('[role="radiogroup"]') || field.querySelector('input, textarea')).setAttribute('aria-describedby', err.id);
  });

  // Live estimate: service range × job size × urgency. The pill re-rolls; screen readers hear it once input settles
  const update = (announce) => {
    const size = SIZES[range.value - 1], service = form.querySelector('[name="service"]:checked');
    const factor = size[2] * form.querySelector('[name="urgency"]:checked').dataset.factor;
    const text = service ? `${money(service.dataset.low * factor)}–${money(service.dataset.high * factor)}` : 'From $120';
    range.style.setProperty('--quote-wizard-fill', (range.value - range.min) / (range.max - range.min));
    range.setAttribute('aria-valuetext', `${size[0]}, ${size[1]}`);
    $('.quote-wizard__size-value').textContent = `${size[0]} · ${size[1]}`;
    if (text === pill.textContent) return;
    root.querySelectorAll('.quote-wizard__amount').forEach((el) => { el.textContent = text; });
    if (!reduce.matches) pill.animate({ transform: ['translateY(1.1em)', 'none'], opacity: [0, 1], filter: ['blur(4px)', 'none'] }, { duration: 460, easing: EASE });
    clearTimeout(timer);
    if (announce) timer = setTimeout(() => { $('.quote-wizard__live').textContent = `Estimate updated: ${text.replace('–', ' to ')}`; }, 900);
  };

  // One field: message + aria-invalid when shown; an error clears as soon as the value is fixed
  const check = (field, show) => {
    const inputs = [...field.querySelectorAll('input, textarea')], ok = inputs.every((el) => el.checkValidity());
    if (ok || show) {
      const target = field.closest('[role="radiogroup"]') || inputs[0];
      if (ok) target.removeAttribute('aria-invalid'); else target.setAttribute('aria-invalid', 'true');
      field.querySelector('.quote-wizard__error').textContent = ok ? '' : field.dataset.error;
      field.classList.toggle('is-invalid', !ok);
    }
    return ok;
  };
  // A whole step: shake what's wrong and put focus on the first problem
  const validate = (i) => {
    const bad = [...steps[i].querySelectorAll('.quote-wizard__field')].filter((field) => !check(field, true));
    if (!reduce.matches) bad.forEach((field) => field.animate(SHAKE, { duration: 400, easing: 'cubic-bezier(0.36, 0.07, 0.19, 0.97)' }));
    bad[0]?.querySelector('input, textarea').focus();
    return !bad.length;
  };

  // Review: read the answers back
  const review = () => {
    const el = form.elements, size = SIZES[range.value - 1];
    const text = {
      service: el.service.value,
      job: `${size[0]} (${size[1]}) · ${el.urgency.value}`,
      contact: ['name', 'phone', 'email', 'zip'].map((k) => el.namedItem(k).value.trim()).filter(Boolean).join(' · '),
    };
    root.querySelectorAll('[data-review]').forEach((dd) => { dd.textContent = text[dd.dataset.review]; });
  };

  // Show step n: it slides in from the side you're travelling to while the viewport height glides to fit
  const go = (n, instant) => {
    [view, ...steps].forEach((el) => el.getAnimations().forEach((a) => a.finish()));
    const from = steps[cur], to = steps[n], dir = Math.sign(n - cur);
    if (n !== cur) {
      const h = view.offsetHeight;
      from.inert = true;
      to.inert = to.hidden = false;
      if (instant || reduce.matches) from.hidden = true;
      else {
        view.classList.add('is-moving');
        view.animate({ height: [`${h}px`, `${to.offsetHeight}px`] }, { duration: 560, easing: EASE }).onfinish = () => { if (!view.getAnimations().length) view.classList.remove('is-moving'); };
        from.animate({ transform: ['none', `translateX(${-dir * 32}%)`], opacity: [1, 0] }, { duration: 360, easing: EASE }).onfinish = () => { if (steps[cur] !== from) from.hidden = true; };
        to.animate({ transform: [`translateX(${dir * 32}%)`, 'none'], opacity: [0, 1] }, { duration: 560, easing: EASE });
      }
    }
    cur = n;
    root.style.setProperty('--quote-wizard-progress', n / last);
    dots.forEach((dot, i) => { dot.classList.toggle('is-done', i < n); dot.classList.toggle('is-current', i === n); });
    back.hidden = n === 0;
    next.hidden = n === last;
    submit.hidden = n !== last;
    if (n === last) review();
    if (instant) return;
    to.querySelector('.quote-wizard__step-title').focus({ preventScroll: true });
    if (card.getBoundingClientRect().top < 0) card.scrollIntoView({ block: 'start', behavior: reduce.matches ? 'auto' : 'smooth' });
  };

  next.addEventListener('click', () => { if (validate(cur)) go(cur + 1); });
  back.addEventListener('click', () => go(cur - 1));
  root.querySelectorAll('[data-goto]').forEach((b) => b.addEventListener('click', () => go(+b.dataset.goto)));
  form.addEventListener('input', (e) => {
    update(true);
    const field = e.target.closest('.quote-wizard__field');
    if (field?.classList.contains('is-invalid')) check(field);
  });

  // Send: Enter mid-flow acts as Next; the real submit swaps in the success view and draws the check
  form.addEventListener('submit', (e) => {
    e.preventDefault(); // Demo only: POST new FormData(form) to form.action, then show success
    if (cur < last) { next.click(); return; }
    const bad = steps.findIndex((step) => ![...step.querySelectorAll('.quote-wizard__field')].every((field) => check(field)));
    if (bad > -1) { go(bad); validate(bad); return; }
    const h = card.offsetHeight;
    form.hidden = true;
    done.hidden = false;
    dots.forEach((dot) => { dot.classList.add('is-done'); dot.classList.remove('is-current'); });
    root.style.setProperty('--quote-wizard-progress', 1);
    if (!reduce.matches) card.animate({ height: [`${h}px`, `${card.offsetHeight}px`] }, { duration: 560, easing: EASE });
    $('.quote-wizard__done-title').focus();
  });
  $('.quote-wizard__restart').addEventListener('click', () => {
    form.reset();
    form.hidden = false;
    done.hidden = true;
    go(0, true);
    update(false);
    steps[0].querySelector('.quote-wizard__step-title').focus();
  });

  steps.forEach((step, i) => { step.hidden = i > 0; });
  go(0, true);
  update(false);
});
```

## Notes

- One native `<form>`: each step is a `fieldset` whose `legend` holds an `h3`, and focus moves to that heading on every step change. The service cards are a radio group (the step fieldset carries `role="radiogroup"`), urgency is a second radio group, and job size is a native range with `aria-valuetext`. Leaving steps are `inert`, then `hidden`.
- Validation: Next checks only the current step. Each message is linked by `aria-describedby` (unique ids per instance), sets `aria-invalid`, shakes and focuses the first problem, and clears as soon as the value is fixed. Back never blocks, Enter mid-flow acts as Next, and a final check runs on submit. The estimate is announced once, 900ms after the input settles.
- Without JS every step shows as one long form with native `required`/`pattern` validation, posting to `/quote`, and the progress, slider readout and slider fill are omitted. With JS, a `scripting: enabled` rule shows only step 1 while the module boots, and a 3s CSS failsafe restores the long form if it never runs.
- Reduced motion: steps and heights swap instantly, the price stops rolling, no shake, and the review stagger and success draw are off. Token-driven springs (badge, segmented pill, floating labels) become instant.
- Contrast: white on the button and badge gradient (`--primary` → teal deepened with 30% `--surface-deep`) is ≥ 4.9:1. The pill amount on `--text-main` is ≥ 12:1 and its label 7.6:1. The Edit text uses `--primary-hover` (≥ 5.7:1 on its tint), and `--text-muted` on the 4% primary total panel is 4.6:1.
- Retheme with `--quote-wizard-grad`. Prices live in each service radio's `data-low`/`data-high`, job-size multipliers in `SIZES` and urgency in `data-factor`. Replace the demo `submit` handler with a `fetch` POST of `new FormData(form)`. Uses `:has()` (segmented pill, card states), container queries and `field-sizing`, each with a plain fallback.
