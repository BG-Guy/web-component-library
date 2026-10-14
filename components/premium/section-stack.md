# Section Stack

Full-viewport sections that stack like a deck. Each one pins to the top while the next slides up over it, and the covered section sinks back: it scales to 0.9, rounds its corners to `--radius-2xl`, dims and drifts up, while the incoming section's top corners flatten as it lands. The last section scrolls away normally so the page carries on. On phones the same deck runs with compact content, and any section taller than the screen pins by its bottom edge so nothing is covered unread. Depends on `tokens/variables.css`.

**Motion:** scroll-scrubbed deck (linear scrub from one rAF scroll listener): the covered section scales to 0.9, rounds to `--radius-2xl` with `clip-path`, dims under a deep overlay and drifts up 3vh, while the incoming one's top corners flatten · button lift and press (`--dur-2`, `--ease-spring`) · arrow nudge (`--dur-3`).

## HTML

```html
<div class="section-stack-demo">
  <div class="section-stack-demo__block">
    <p class="section-stack-demo__note">Full-screen sections that stack like a deck. Each one slides over the last and pushes it back.</p>
    <p class="section-stack-demo__hint">
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
      Scroll
    </p>
  </div>

  <div class="section-stack" data-section-stack>
    <section class="section-stack__card section-stack__card--deep" aria-labelledby="section-stack-crew">
      <div class="section-stack__bar" aria-hidden="true"><span>Brand · Springfield</span><span>01 / 04</span></div>
      <div class="section-stack__inner">
        <div class="section-stack__copy">
          <p class="section-stack__eyebrow">How we work</p>
          <h2 id="section-stack-crew" class="section-stack__title">One crew for the whole house.</h2>
          <p class="section-stack__text">Plumbing, heating and electrical under one roof. Book once and we send the right people in the right order, with the parts already on the van.</p>
          <div class="section-stack__actions">
            <a class="section-stack__btn" href="#how-it-works">
              See how it works
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <a class="section-stack__btn section-stack__btn--ghost" href="tel:+15555550123">
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
              (555) 555-0123
            </a>
          </div>
        </div>
        <div class="section-stack__crew" aria-hidden="true">
          <div class="section-stack__trade">
            <span class="section-stack__trade-icon"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" /></svg></span>
            <span><strong>Plumbing</strong><small>Sam K. · 12 yrs</small></span>
            <span class="section-stack__trade-status">On call</span>
          </div>
          <div class="section-stack__trade">
            <span class="section-stack__trade-icon"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.07-2.14-.22-4.05 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.15.43-2.29 1-3a2.5 2.5 0 0 0 2.5 2.5z" /></svg></span>
            <span><strong>Heating</strong><small>Maria R. · 9 yrs</small></span>
            <span class="section-stack__trade-status">On call</span>
          </div>
          <div class="section-stack__trade">
            <span class="section-stack__trade-icon"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z" /></svg></span>
            <span><strong>Electrical</strong><small>Jo P. · 15 yrs</small></span>
            <span class="section-stack__trade-status">On call</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section-stack__card section-stack__card--brand" aria-labelledby="section-stack-numbers">
      <div class="section-stack__bar" aria-hidden="true"><span>Brand · Springfield</span><span>02 / 04</span></div>
      <div class="section-stack__inner section-stack__inner--single">
        <div class="section-stack__copy">
          <p class="section-stack__eyebrow">Track record</p>
          <h2 id="section-stack-numbers" class="section-stack__title">Numbers we'd paint on the van.</h2>
          <p class="section-stack__text">Every job is logged, timed and reviewed, so these numbers keep themselves honest.</p>
        </div>
        <dl class="section-stack__stats">
          <div class="section-stack__stat"><dt>Average from 2,300 reviews</dt><dd>4.9<small>/5</small></dd></div>
          <div class="section-stack__stat"><dt>Emergency arrival</dt><dd>41<small>min</small></dd></div>
          <div class="section-stack__stat"><dt>Jobs since 2014</dt><dd>12.8<small>k</small></dd></div>
          <div class="section-stack__stat"><dt>Guarantee on labour</dt><dd>2<small>yrs</small></dd></div>
        </dl>
      </div>
    </section>

    <section class="section-stack__card section-stack__card--light" aria-labelledby="section-stack-pricing">
      <div class="section-stack__bar" aria-hidden="true"><span>Brand · Springfield</span><span>03 / 04</span></div>
      <div class="section-stack__inner">
        <div class="section-stack__copy">
          <p class="section-stack__eyebrow">Pricing</p>
          <h2 id="section-stack-pricing" class="section-stack__title">Prices in writing, before we start.</h2>
          <p class="section-stack__text">Your quote is itemised, fixed and on your phone before a tool comes out. If the job runs long, that's our problem, not yours.</p>
          <div class="section-stack__actions">
            <a class="section-stack__btn" href="#quote">
              Get a free quote
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <a class="section-stack__link" href="#prices">See sample prices</a>
          </div>
        </div>
        <div class="section-stack__receipt" aria-hidden="true">
          <div class="section-stack__receipt-head"><strong>Quote #2291</strong><span>Leak repair · Westlake</span></div>
          <div class="section-stack__receipt-row"><span>Labour, 1.5 h</span><b>$120</b></div>
          <div class="section-stack__receipt-row"><span>Parts</span><b>$29</b></div>
          <div class="section-stack__receipt-row"><span>Call-out</span><b>$0</b></div>
          <div class="section-stack__receipt-row section-stack__receipt-row--total"><span>Total</span><b>$149</b></div>
          <span class="section-stack__receipt-stamp">Fixed price</span>
        </div>
      </div>
    </section>

    <section class="section-stack__card section-stack__card--photo" aria-labelledby="section-stack-book">
      <img class="section-stack__photo" src="northside-kitchen.jpg" alt="" width="1600" height="1067" loading="lazy" decoding="async">
      <div class="section-stack__bar" aria-hidden="true"><span>Brand · Springfield</span><span>04 / 04</span></div>
      <div class="section-stack__inner section-stack__inner--single">
        <div class="section-stack__copy">
          <p class="section-stack__eyebrow">Northside · last Tuesday</p>
          <h2 id="section-stack-book" class="section-stack__title">Your neighbours already called.</h2>
          <figure class="section-stack__quote">
            <blockquote><p>"Booked at nine, fixed by eleven, and they left the kitchen cleaner than they found it."</p></blockquote>
            <figcaption>Priya S. · Northside</figcaption>
          </figure>
          <div class="section-stack__actions">
            <a class="section-stack__btn" href="#book">
              Book a visit
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <p class="section-stack__rating">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
              <span><strong>4.9 out of 5</strong> from 2,300 reviews</span>
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>

  <div class="section-stack-demo__block">
    <p class="section-stack-demo__note">The last section isn't sticky, so the page simply carries on.</p>
  </div>
</div>
```

## CSS

```css
/* Demo scroll room (demo only) */
.section-stack-demo__block {
  display: grid; place-content: center; justify-items: center; gap: 1rem; min-height: 70vh; padding: 3rem var(--gutter);
  background: var(--surface-muted); color: var(--text-muted); font-family: var(--font-sans); text-align: center;
}
.section-stack-demo__note { max-width: 26rem; margin: 0; color: var(--text-main); font: 500 1.125rem/1.5 var(--font-display); letter-spacing: -0.01em; }
.section-stack-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.section-stack-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* Deck: a deep stage shows around each section as it sinks back */
.section-stack { position: relative; background: var(--surface-deep); font-family: var(--font-sans); }
.section-stack__card {
  --section-stack-p: 0;
  --section-stack-in: 1;
  --section-stack-fg: var(--text-inverse);
  --section-stack-muted: var(--text-inverse-muted);
  --section-stack-line: var(--border-inverse);
  --section-stack-focus: var(--text-inverse);
  position: sticky; top: var(--section-stack-top, 0px); isolation: isolate; overflow: clip;
  display: grid; align-items: center; min-height: 100vh; min-height: 100svh;
  color: var(--section-stack-fg);
}
.section-stack__card:last-child { position: relative; top: 0; }
/* No JS on a short screen: plain flow, so a tall section is never covered before it's read */
@media (max-height: 37.5rem) {
  .section-stack:not(.section-stack--js) .section-stack__card { position: relative; top: 0; }
}

/* Depth (JS + motion allowed): driven by --section-stack-p (being covered) and --section-stack-in (landing) */
.section-stack__card::after {
  content: ""; position: absolute; inset: 0; z-index: 1; opacity: 0; pointer-events: none;
  background: linear-gradient(180deg, color-mix(in srgb, var(--surface-deep) 45%, transparent), color-mix(in srgb, var(--surface-deep) 90%, transparent));
}
.section-stack--fx .section-stack__card {
  --section-stack-r-top: calc(var(--radius-2xl) * max(1 - var(--section-stack-in), var(--section-stack-p)));
  --section-stack-r-bottom: calc(var(--radius-2xl) * var(--section-stack-p));
  transform-origin: 50% calc(50vh - var(--section-stack-top, 0px));
  transform: translateY(calc(var(--section-stack-p) * -3vh)) scale(calc(1 - var(--section-stack-p) * 0.1));
  clip-path: inset(0 round var(--section-stack-r-top) var(--section-stack-r-top) var(--section-stack-r-bottom) var(--section-stack-r-bottom));
}
.section-stack--fx .section-stack__card::after { opacity: calc(var(--section-stack-p) * 0.85); }

/* Surfaces */
.section-stack__card--deep {
  background:
    radial-gradient(55% 60% at 85% 15%, color-mix(in srgb, var(--primary) 30%, transparent), transparent 70%),
    radial-gradient(50% 55% at 10% 95%, color-mix(in srgb, var(--primary-2) 25%, transparent), transparent 70%),
    var(--surface-deep);
}
.section-stack__card--deep::before {
  content: ""; position: absolute; inset: 0; z-index: -1;
  background-image: linear-gradient(var(--border-inverse) 1px, transparent 1px), linear-gradient(90deg, var(--border-inverse) 1px, transparent 1px);
  background-size: 3.5rem 3.5rem;
  -webkit-mask-image: radial-gradient(ellipse 70% 60% at 70% 40%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 70% 60% at 70% 40%, black, transparent 75%);
}
.section-stack__card--brand {
  --section-stack-muted: color-mix(in srgb, var(--text-inverse) 90%, transparent);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 85%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 75%, var(--surface-deep)));
}
.section-stack__card--brand::before {
  content: ""; position: absolute; inset: 0; z-index: -1;
  background: repeating-radial-gradient(circle at 100% 0%, transparent 0 4rem, color-mix(in srgb, var(--text-inverse) 8%, transparent) 4rem calc(4rem + 1px));
  -webkit-mask-image: radial-gradient(circle at 100% 0%, black, transparent 55%);
  mask-image: radial-gradient(circle at 100% 0%, black, transparent 55%);
}
.section-stack__card--light {
  --section-stack-fg: var(--text-main);
  --section-stack-muted: var(--text-muted);
  --section-stack-line: var(--border-subtle);
  --section-stack-focus: var(--primary);
  background: var(--surface-light);
}
.section-stack__card--light::before {
  content: ""; position: absolute; inset: 0; z-index: -1;
  background: radial-gradient(circle, var(--border-subtle) 1px, transparent 1.5px) 0 0 / 1.5rem 1.5rem;
  -webkit-mask-image: linear-gradient(90deg, transparent 30%, black);
  mask-image: linear-gradient(90deg, transparent 30%, black);
}
.section-stack__card--photo { --section-stack-muted: color-mix(in srgb, var(--text-inverse) 85%, transparent); background: var(--surface-deep); }
.section-stack__photo { position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover; }
.section-stack__card--photo::before {
  content: ""; position: absolute; inset: 0; z-index: -1;
  background: linear-gradient(180deg, color-mix(in srgb, var(--surface-deep) 72%, transparent), color-mix(in srgb, var(--surface-deep) 90%, transparent));
}

/* Deck tab: brand on the left, position in the deck on the right */
.section-stack__bar {
  position: absolute; inset: 1.25rem 0 auto; display: flex; justify-content: space-between; gap: 1rem;
  max-width: var(--container-max); margin-inline: auto; padding: 0 var(--gutter) 0.875rem;
  color: var(--section-stack-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase;
}
.section-stack__bar::after { content: ""; position: absolute; left: var(--gutter); right: var(--gutter); bottom: 0; height: 1px; background: var(--section-stack-line); }

/* Layout and type */
.section-stack__inner {
  position: relative; display: grid; gap: 2.5rem; align-items: center;
  width: 100%; max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4.5rem, 12vh, 7rem) var(--gutter) clamp(2.5rem, 8vh, 5rem);
}
.section-stack__copy { max-width: 38rem; }
.section-stack__eyebrow {
  display: flex; align-items: center; gap: 0.625rem; margin: 0;
  color: var(--section-stack-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.section-stack__eyebrow::before { content: ""; width: 1.5rem; height: 1px; background: currentColor; }
.section-stack__title {
  margin: 1rem 0 0; font: 600 clamp(2.25rem, 1.2rem + 3.8vw, 4.5rem)/1 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.section-stack__text { max-width: 34rem; margin: 1.25rem 0 0; color: var(--section-stack-muted); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6; }

/* Actions */
.section-stack__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.25rem; margin-top: 2rem; }
.section-stack__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem/1.2 var(--font-sans); text-decoration: none;
  box-shadow: var(--highlight), 0 14px 36px -14px color-mix(in srgb, var(--primary) 80%, transparent);
  transition: transform var(--dur-2) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.section-stack__btn:hover { transform: translateY(-2px); }
.section-stack__btn:active { transform: scale(0.97); }
.section-stack__btn--ghost { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.section-stack__card--light .section-stack__btn {
  background: var(--text-main); color: var(--surface-light);
  box-shadow: var(--highlight-inverse), 0 14px 32px -14px color-mix(in srgb, var(--text-main) 70%, transparent);
}
.section-stack__link {
  display: inline-flex; align-items: center; min-height: 2.75rem; color: var(--primary); font-size: 0.9375rem; font-weight: 600;
  text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 0.3em;
}
.section-stack :is(.section-stack__btn, .section-stack__trade-icon, .section-stack__rating) svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.section-stack__btn svg { transition: transform var(--dur-3) var(--ease-spring); }
.section-stack__btn:not(.section-stack__btn--ghost):hover svg { transform: translateX(3px); }
.section-stack :is(.section-stack__btn, .section-stack__link):focus-visible { outline: 2px solid var(--section-stack-focus); outline-offset: 3px; }

/* Deep: the crew, fanned like a hand of cards (decorative, from 768px) */
.section-stack__crew { display: none; }
.section-stack__trade {
  display: flex; align-items: center; gap: 0.875rem; padding: 1rem 1.125rem; border-radius: var(--radius-xl);
  background: var(--glass-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 24px 48px -24px color-mix(in srgb, var(--surface-deep) 90%, transparent);
}
.section-stack__trade:nth-child(2) { translate: 1.5rem 0; }
.section-stack__trade:nth-child(3) { translate: 3rem 0; }
.section-stack__trade-icon { flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: var(--radius-lg); background: var(--gradient-brand); color: var(--text-inverse); }
.section-stack__trade strong { display: block; font: 600 1rem/1.25 var(--font-display); }
.section-stack__trade small { color: var(--text-inverse-muted); font: 500 0.75rem/1.4 var(--font-mono); }
.section-stack__trade-status {
  margin-left: auto; padding: 0.25rem 0.5rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--success) 28%, transparent); color: var(--text-inverse); font-size: 0.6875rem; font-weight: 600;
}

/* Brand: stat row */
.section-stack__stats { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem 1rem; margin: 0; }
.section-stack__stat { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.5rem; padding-top: 1rem; border-top: 1px solid var(--section-stack-line); }
.section-stack__stat dt { color: var(--section-stack-muted); font: 500 0.75rem/1.35 var(--font-mono); letter-spacing: 0.04em; text-transform: uppercase; }
.section-stack__stat dd { margin: 0; font: 600 clamp(2.5rem, 1.5rem + 3.5vw, 4.5rem)/1 var(--font-display); letter-spacing: var(--tracking-display); }
.section-stack__stat small { margin-left: 0.15em; color: var(--section-stack-muted); font-size: 0.4em; letter-spacing: 0; }

/* Light: an itemised quote (decorative, from 768px) */
.section-stack__receipt { display: none; }
.section-stack__receipt-head { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; padding-bottom: 1rem; border-bottom: 1px dashed var(--border-subtle); }
.section-stack__receipt-head strong { font: 600 1rem/1.2 var(--font-display); }
.section-stack__receipt-head span { color: var(--text-muted); font-size: 0.75rem; }
.section-stack__receipt-row { display: flex; justify-content: space-between; gap: 1rem; color: var(--text-muted); font-size: 0.875rem; }
.section-stack__receipt-row b { color: var(--text-main); font: 600 0.875rem/1.4 var(--font-mono); }
.section-stack__receipt-row--total { padding-top: 0.875rem; border-top: 1px solid var(--border-subtle); color: var(--text-main); font-weight: 600; }
.section-stack__receipt-row--total b { font-size: 1.25rem; }
.section-stack__receipt-stamp {
  justify-self: end; padding: 0.25rem 0.625rem; border: 2px solid var(--success); border-radius: var(--radius-md); rotate: -6deg;
  color: var(--success); font: 700 0.8125rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase;
}

/* Photo: review and rating */
.section-stack__quote { max-width: 36rem; margin: 1.5rem 0 0; }
.section-stack__quote blockquote { margin: 0; font: 500 clamp(1.25rem, 1rem + 1vw, 1.625rem)/1.4 var(--font-display); letter-spacing: -0.01em; }
.section-stack__quote p { margin: 0; }
.section-stack__quote figcaption { margin-top: 0.875rem; color: var(--section-stack-muted); font: 500 0.8125rem/1.4 var(--font-mono); }
.section-stack__rating { display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; color: var(--section-stack-muted); font-size: 0.875rem; }
.section-stack .section-stack__rating svg { color: var(--accent); fill: currentColor; }
.section-stack__rating strong { color: var(--section-stack-fg); }

@media (min-width: 768px) {
  .section-stack__inner { grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr); gap: 4rem; }
  .section-stack__inner--single { grid-template-columns: minmax(0, 1fr); }
  .section-stack__stats { grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 2rem; }
  .section-stack__crew { display: grid; gap: 0.75rem; justify-self: center; width: min(100%, 20rem); }
  .section-stack__receipt {
    display: grid; gap: 0.875rem; justify-self: center; width: min(100%, 21rem); padding: 1.5rem; border-radius: var(--radius-2xl); rotate: 2deg;
    background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl);
  }
}
```

## JS

```js
document.querySelectorAll('[data-section-stack]').forEach((stack) => {
  const cards = [...stack.querySelectorAll('.section-stack__card')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  let starts = [];
  let frame = 0;
  stack.classList.add('section-stack--js');

  const set = (el, name, value) => {
    if (el.style.getPropertyValue(name) !== value) el.style.setProperty(name, value);
  };

  // Cover progress per card (0–1): how far the next card has risen over it. Read from layout offsets, so the transforms it drives never feed back
  const update = () => {
    frame = 0;
    const fx = !reduce.matches;
    stack.classList.toggle('section-stack--fx', fx);
    if (!fx) return;
    const top = stack.getBoundingClientRect().top;
    cards.forEach((card, i) => {
      const next = cards[i + 1];
      const p = next ? Math.min(1, Math.max(0, 1 - (top + starts[i + 1]) / innerHeight)).toFixed(3) : '0';
      set(card, '--section-stack-p', p);
      if (next) set(next, '--section-stack-in', p);
    });
  };

  // Cards taller than the screen pin by their bottom edge, so their lower content is read before the next card covers it
  const measure = () => {
    let y = 0;
    starts = cards.map((card) => {
      const start = y;
      y += card.offsetHeight;
      set(card, '--section-stack-top', `${Math.min(0, innerHeight - card.offsetHeight)}px`);
      return start;
    });
    update();
  };

  // One rAF-throttled, passive scroll listener, attached only while the deck is near the viewport
  const onScroll = () => { if (!frame) frame = requestAnimationFrame(update); };
  new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) { addEventListener('scroll', onScroll, { passive: true }); onScroll(); }
    else removeEventListener('scroll', onScroll);
  }, { rootMargin: '100px 0px' }).observe(stack);
  new ResizeObserver(measure).observe(stack);
  addEventListener('resize', measure, { passive: true });
  reduce.addEventListener('change', update);
  measure();

  // Keyboard focus never lands under the next card: scroll its own card back into view first
  stack.addEventListener('focusin', (e) => {
    const i = cards.findIndex((card) => card.contains(e.target));
    const next = cards[i + 1];
    if (i < 0 || !next || next.getBoundingClientRect().top >= e.target.getBoundingClientRect().bottom) return;
    let offset = 0;
    for (let el = e.target; el && el !== cards[i]; el = el.offsetParent) offset += el.offsetTop;
    const start = scrollY + stack.getBoundingClientRect().top + starts[i];
    const pin = parseFloat(cards[i].style.getPropertyValue('--section-stack-top')) || 0;
    scrollTo({ top: Math.min(start - pin, start + offset - innerHeight / 3), behavior: 'instant' });
  });
});
```

## Notes

- Each card is an ordinary `<section>` with its own `<h2>`. The deck is visual only, so reading and tab order follow the DOM, and the dimming overlays are `pointer-events: none`. If keyboard focus moves into a card that's covered, the script first scrolls that card back into view, so focus never sits hidden under the next one (WCAG 2.4.11).
- The scroll recipe is one rAF-throttled, passive listener, gated by an IntersectionObserver. It writes `--section-stack-p` (how far the next card has covered this one) and `--section-stack-in` (how far this one has landed), computed from layout offsets so the transforms they drive never skew the measurement. CSS turns those into the 0.9 scale, the `--radius-2xl` `clip-path`, the overlay and a 3vh drift; only `transform`, `clip-path` and `opacity` change while scrolling.
- Cards taller than the viewport get a negative sticky `top` (`--section-stack-top`), so they pin by their bottom edge and nothing is covered unread. Without JS, viewports under 600px tall drop the stacking and flow normally.
- Without JS or under reduced motion, it's plain sticky stacking: sections slide over each other with no scale, rounding or dimming, and the scroll itself is the only motion. The last card isn't sticky, so the page carries on after the deck.
- Contrast: deep 18.8 (text), 7.7 (muted; 5.8 under the glow) · brand gradient: white 6.2–5.5, 90% white 5.3–4.8 · light 14.6 / 4.8 (link 5.2) · photo under its 72–90% deep scrim: white at least 7.8, 85% white at least 6.2.
- Any number of cards works. Keep `.section-stack__card` on each direct child with no margins between them (the script sums their heights), and add surfaces as new card modifiers.
