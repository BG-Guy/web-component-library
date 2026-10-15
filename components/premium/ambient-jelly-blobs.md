# Jelly Blobs

A deep ambient layer of four big, soft blobs that behave like jelly. Scroll fast and they stretch along the motion and squash across it; stop, and a damped spring wobbles them back to round. Each blob also drifts at its own rate with scroll position, and their colours flow from blue and teal at the top of the page to teal and amber at the bottom, mixed live from the brand tokens. On phones the blobs scale with the viewport and the same springs run. Depends on `tokens/variables.css`.

**Motion:** squash and stretch on per-blob damped springs from scroll velocity · lag-and-jiggle offset · scroll-position drift at four rates (eased) · `color-mix()` colour flow from a progress variable · everything settles in about 1.5s, then the loop stops.

## HTML

```html
<div class="amb-jelly-demo">
  <div class="amb-jelly" aria-hidden="true">
    <div class="amb-jelly__stage">
      <span class="amb-jelly__blob" style="--amb-jelly-x: 14%; --amb-jelly-y: 18%; --amb-jelly-size: 54vmax; --amb-jelly-from: var(--primary); --amb-jelly-to: var(--primary-2)"></span>
      <span class="amb-jelly__blob" style="--amb-jelly-x: 88%; --amb-jelly-y: 30%; --amb-jelly-size: 46vmax; --amb-jelly-from: var(--primary-2); --amb-jelly-to: var(--accent)"></span>
      <span class="amb-jelly__blob" style="--amb-jelly-x: 28%; --amb-jelly-y: 88%; --amb-jelly-size: 50vmax; --amb-jelly-from: var(--primary); --amb-jelly-to: var(--accent)"></span>
      <span class="amb-jelly__blob" style="--amb-jelly-x: 80%; --amb-jelly-y: 84%; --amb-jelly-size: 40vmax; --amb-jelly-from: var(--accent); --amb-jelly-to: var(--primary)"></span>
    </div>
  </div>

  <section class="amb-jelly-demo__section amb-jelly-demo__section--hero" aria-labelledby="amb-jelly-hero-title">
    <div class="amb-jelly-demo__inner">
      <p class="amb-jelly-demo__eyebrow"><span class="amb-jelly-demo__pulse"></span>Brand · Springfield home services</p>
      <h2 id="amb-jelly-hero-title" class="amb-jelly-demo__title">Home repairs, <em>without the wobble.</em></h2>
      <p class="amb-jelly-demo__lead">Licensed plumbers, electricians and handymen across Springfield. Flat-rate quotes, two-hour arrival windows and a 12-month guarantee on every job.</p>
      <div class="amb-jelly-demo__actions">
        <a class="amb-jelly-demo__btn amb-jelly-demo__btn--primary" href="#amb-jelly-book">
          Get a free quote
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-jelly-demo__btn" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
      <p class="amb-jelly-demo__hint"><span class="amb-jelly-demo__mouse"></span>Scroll</p>
    </div>
  </section>

  <section class="amb-jelly-demo__section" aria-labelledby="amb-jelly-services-title">
    <div class="amb-jelly-demo__inner">
      <header class="amb-jelly-demo__head">
        <p class="amb-jelly-demo__eyebrow">What we fix</p>
        <h2 id="amb-jelly-services-title" class="amb-jelly-demo__h2">Four trades, one tidy team.</h2>
        <p class="amb-jelly-demo__intro">Every visit starts with a written price. No call-out fees, no surprises on the invoice.</p>
      </header>
      <ul class="amb-jelly-demo__grid" role="list">
        <li class="amb-jelly-demo__card">
          <span class="amb-jelly-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 3s6 6.4 6 10.5a6 6 0 0 1-12 0C6 9.4 12 3 12 3z" /></svg></span>
          <h3><a class="amb-jelly-demo__link" href="#amb-jelly-book">Plumbing</a></h3>
          <p>Leaks, clogs, water heaters and new fixtures.</p>
          <p class="amb-jelly-demo__price"><span>from</span> $89</p>
        </li>
        <li class="amb-jelly-demo__card">
          <span class="amb-jelly-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg></span>
          <h3><a class="amb-jelly-demo__link" href="#amb-jelly-book">Electrical</a></h3>
          <p>Outlets, lighting, EV chargers and panels.</p>
          <p class="amb-jelly-demo__price"><span>from</span> $99</p>
        </li>
        <li class="amb-jelly-demo__card">
          <span class="amb-jelly-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 22a7 7 0 0 0 7-7c0-3-2-5.5-3.5-7-.5 2-1.5 3-3 3.5C13 8 12 5 9 3c0 3-4 6-4 12a7 7 0 0 0 7 7z" /></svg></span>
          <h3><a class="amb-jelly-demo__link" href="#amb-jelly-book">Heating &amp; cooling</a></h3>
          <p>Furnace tune-ups, AC repair and smart thermostats.</p>
          <p class="amb-jelly-demo__price"><span>from</span> $129</p>
        </li>
        <li class="amb-jelly-demo__card">
          <span class="amb-jelly-demo__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z" /></svg></span>
          <h3><a class="amb-jelly-demo__link" href="#amb-jelly-book">Handyman</a></h3>
          <p>Doors, shelves, drywall and the odd jobs list.</p>
          <p class="amb-jelly-demo__price"><span>from</span> $69</p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-jelly-demo__section" aria-labelledby="amb-jelly-proof-title">
    <div class="amb-jelly-demo__inner amb-jelly-demo__inner--split">
      <header class="amb-jelly-demo__head amb-jelly-demo__head--start">
        <p class="amb-jelly-demo__eyebrow">Why Springfield calls us</p>
        <h2 id="amb-jelly-proof-title" class="amb-jelly-demo__h2">Trusted in 3,400 local homes.</h2>
        <dl class="amb-jelly-demo__stats">
          <div><dt>Average rating</dt><dd>4.9</dd></div>
          <div><dt>Arrival window</dt><dd>2h</dd></div>
          <div><dt>Guarantee</dt><dd>12mo</dd></div>
        </dl>
      </header>
      <figure class="amb-jelly-demo__quote">
        <blockquote><p>"Sam found the leak behind the dishwasher in ten minutes, quoted before touching anything, and left the floor cleaner than he found it."</p></blockquote>
        <figcaption><span class="amb-jelly-demo__avatar" aria-hidden="true">JP</span><span><strong>Jo P.</strong> Riverside · Leak repair</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="amb-jelly-demo__section amb-jelly-demo__section--cta" id="amb-jelly-book" aria-labelledby="amb-jelly-cta-title">
    <div class="amb-jelly-demo__inner">
      <p class="amb-jelly-demo__eyebrow">Same-week visits</p>
      <h2 id="amb-jelly-cta-title" class="amb-jelly-demo__title amb-jelly-demo__title--cta">Got a drip, a dead outlet or a draft?</h2>
      <p class="amb-jelly-demo__lead">Tell us what's wrong and get a fixed price back in minutes. Westlake, Northside and Riverside included.</p>
      <div class="amb-jelly-demo__actions">
        <a class="amb-jelly-demo__btn amb-jelly-demo__btn--primary" href="#amb-jelly-book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-jelly-demo__btn" href="mailto:hello@example.com">hello@example.com</a>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Layer: decorative, first child of a relative + isolated host; a sticky, viewport-tall stage keeps the blobs in view */
.amb-jelly {
  --amb-jelly-p: 0.3; /* colour progress, 0 = top of the host, 1 = bottom; JS writes it while you scroll */
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-jelly--page { position: fixed; }
.amb-jelly__stage { position: sticky; top: 0; height: 100vh; height: 100svh; overflow: clip; }
.amb-jelly--page .amb-jelly__stage { position: relative; height: 100%; }
/* Contrast guard: --amb-jelly-scrim (0–1) fades a deep veil over the blobs */
.amb-jelly__stage::after { content: ""; position: absolute; inset: 0; background: color-mix(in srgb, var(--surface-deep) calc(var(--amb-jelly-scrim, 0) * 100%), transparent); }

/* Blobs: pre-softened radial gradients (never a blur filter). Each mixes its two tokens by progress. */
.amb-jelly__blob {
  --amb-jelly-c: color-mix(in oklab, var(--amb-jelly-to) calc(var(--amb-jelly-p) * 100%), var(--amb-jelly-from));
  position: absolute; left: var(--amb-jelly-x); top: var(--amb-jelly-y); width: var(--amb-jelly-size); aspect-ratio: 1;
  border-radius: 50%; translate: -50% -50%;
  background: radial-gradient(closest-side,
    color-mix(in srgb, var(--amb-jelly-c) 38%, transparent),
    color-mix(in srgb, var(--amb-jelly-c) 28%, transparent) 45%,
    color-mix(in srgb, var(--amb-jelly-c) 12%, transparent) 75%, transparent);
}
.amb-jelly[data-moving] .amb-jelly__blob { will-change: transform; } /* only while the springs are live */

/* ---- Demo page (deep) ---- */
.amb-jelly-demo {
  position: relative; isolation: isolate; overflow-x: clip;
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans);
}
.amb-jelly-demo__section { padding-block: clamp(5rem, 11vw, 8rem); }
.amb-jelly-demo__section--hero, .amb-jelly-demo__section--cta { text-align: center; }
.amb-jelly-demo__section--hero { display: grid; align-items: center; min-height: 92vh; min-height: 92svh; }
.amb-jelly-demo__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); box-sizing: border-box; }

.amb-jelly-demo__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.875rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 70%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-jelly-demo__pulse { width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 30%, transparent); }
.amb-jelly-demo__title {
  max-width: 15ch; margin: 1.25rem auto 0; font: 600 clamp(2.5rem, 1.2rem + 5.6vw, 5.5rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-jelly-demo__title em {
  font-style: normal; padding-bottom: 0.06em;
  background: linear-gradient(100deg, var(--text-inverse) 10%, color-mix(in srgb, var(--primary-2) 30%, var(--text-inverse)) 55%, color-mix(in srgb, var(--accent) 50%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.amb-jelly-demo__title--cta { max-width: 18ch; font-size: clamp(2.25rem, 1.3rem + 4vw, 4.25rem); }
.amb-jelly-demo__lead { max-width: 36rem; margin: 1.25rem auto 0; font-size: clamp(1.0625rem, 1rem + 0.4vw, 1.25rem); line-height: 1.6; }
.amb-jelly-demo__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2.25rem; }
.amb-jelly-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 60%, transparent); color: var(--text-inverse); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2) var(--ease-out), box-shadow var(--dur-3) var(--ease-out);
}
.amb-jelly-demo__btn:hover { transform: translateY(-2px); background: color-mix(in srgb, var(--surface-deep) 40%, transparent); }
.amb-jelly-demo__btn:active { transform: scale(0.97); }
.amb-jelly-demo__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: 0 14px 40px -14px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.amb-jelly-demo__btn--primary:hover { background: var(--surface-light); box-shadow: 0 18px 48px -12px color-mix(in srgb, var(--accent) 70%, transparent); }
.amb-jelly-demo svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-jelly-demo :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.amb-jelly-demo__hint {
  display: flex; flex-direction: column; align-items: center; gap: 0.5rem; margin: 3.5rem 0 0;
  font: 500 0.6875rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.amb-jelly-demo__mouse { position: relative; width: 1.25rem; height: 2rem; border-radius: var(--radius-full); box-shadow: inset 0 0 0 1.5px var(--text-inverse); }
.amb-jelly-demo__mouse::after {
  content: ""; position: absolute; left: 50%; top: 0.375rem; width: 0.25rem; height: 0.375rem; margin-left: -0.125rem; border-radius: var(--radius-full);
  background: var(--text-inverse); animation: amb-jelly-wheel 1.5s var(--ease-in-out) 3; /* three rolls, then still */
}

/* Section heads */
.amb-jelly-demo__head { max-width: 38rem; margin: 0 auto 3rem; text-align: center; }
.amb-jelly-demo__head--start { margin: 0; }
.amb-jelly-demo__h2 { margin: 1rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.8vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.amb-jelly-demo__intro { max-width: 32rem; margin: 1rem auto 0; font-size: 1.0625rem; line-height: 1.6; }

/* Service cards: deep, translucent panels (no backdrop blur over moving blobs) */
.amb-jelly-demo__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.amb-jelly-demo__card {
  position: relative; display: flex; flex-direction: column; gap: 0.5rem; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-deep) 78%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 30px 60px -30px var(--surface-deep);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-jelly-demo__card:hover {
  transform: translateY(-4px);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 55%, transparent), var(--highlight-inverse), 0 30px 60px -24px color-mix(in srgb, var(--primary-2) 45%, transparent);
}
.amb-jelly-demo__card h3 { margin: 0.75rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-jelly-demo__card p { margin: 0; color: var(--text-inverse-muted); line-height: 1.55; }
.amb-jelly-demo__icon {
  display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 0.875rem; color: var(--text-inverse);
  background: radial-gradient(circle at 30% 20%, color-mix(in srgb, var(--surface-light) 35%, transparent), transparent 50%), var(--gradient-brand);
  box-shadow: var(--highlight-inverse), 0 10px 24px -10px var(--primary);
}
.amb-jelly-demo__card:nth-child(even) .amb-jelly-demo__icon { background: radial-gradient(circle at 30% 20%, color-mix(in srgb, var(--surface-light) 35%, transparent), transparent 50%), linear-gradient(135deg, var(--primary-2), color-mix(in srgb, var(--accent) 70%, var(--primary-2))); }
.amb-jelly-demo__link { color: inherit; text-decoration: none; }
.amb-jelly-demo__link::after { content: ""; position: absolute; inset: 0; border-radius: inherit; }
.amb-jelly-demo .amb-jelly-demo__link:focus-visible { outline: none; }
.amb-jelly-demo__link:focus-visible::after { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.amb-jelly-demo__card .amb-jelly-demo__price {
  display: flex; align-items: baseline; gap: 0.375rem; margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--border-inverse);
  color: var(--text-inverse); font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight);
}
.amb-jelly-demo__price span { color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.04em; }

/* Proof */
.amb-jelly-demo__inner--split { display: grid; gap: 2.5rem; align-items: center; }
.amb-jelly-demo__stats {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); margin: 2rem 0 0; padding: 0.5rem; border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-deep) 72%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.amb-jelly-demo__stats div { display: flex; flex-direction: column-reverse; gap: 0.375rem; padding: 1rem 0.5rem; text-align: center; }
.amb-jelly-demo__stats div + div { box-shadow: -1px 0 0 var(--border-inverse); }
.amb-jelly-demo__stats dt { color: var(--text-inverse-muted); font: 500 0.6875rem var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.amb-jelly-demo__stats dd { margin: 0; font: 600 clamp(1.75rem, 1.4rem + 1.6vw, 2.75rem)/1 var(--font-display); letter-spacing: var(--tracking-display); }
.amb-jelly-demo__quote {
  display: grid; gap: 1.5rem; margin: 0; padding: clamp(1.5rem, 4vw, 2.5rem); border-radius: var(--radius-2xl);
  background: color-mix(in srgb, var(--surface-deep) 78%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 40px 80px -40px var(--surface-deep);
}
.amb-jelly-demo__quote blockquote { margin: 0; }
.amb-jelly-demo__quote blockquote p { margin: 0; font: 500 clamp(1.1875rem, 1rem + 0.8vw, 1.5rem)/1.45 var(--font-display); letter-spacing: -0.01em; }
.amb-jelly-demo__quote figcaption { display: flex; align-items: center; gap: 0.75rem; color: var(--text-inverse-muted); font-size: 0.875rem; }
.amb-jelly-demo__quote figcaption strong { display: block; color: var(--text-inverse); }
.amb-jelly-demo__avatar { display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%; background: var(--gradient-brand); font: 700 0.75rem var(--font-sans); }

@media (min-width: 600px) { .amb-jelly-demo__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1024px) {
  .amb-jelly-demo__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .amb-jelly-demo__inner--split { grid-template-columns: 1fr 1fr; gap: 4rem; }
}

@media (prefers-reduced-motion: reduce) {
  .amb-jelly__blob { transform: none !important; }
  .amb-jelly-demo__mouse::after { animation: none; }
}
@keyframes amb-jelly-wheel { 0% { opacity: 0; transform: translateY(-0.125rem); } 30% { opacity: 1; } 100% { opacity: 0; transform: translateY(0.5rem); } }
```

## JS

```js
// Jelly Blobs: damped springs turn scroll speed into squash and stretch; scroll position drives
// drift and colour. One rAF loop per layer, running only while something is still moving.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('.amb-jelly').forEach((layer) => {
  const page = layer.classList.contains('amb-jelly--page');
  const host = layer.parentElement;
  // Each blob gets its own drift rate, sway and spring, so they wobble out of step
  const blobs = [...layer.querySelectorAll('.amb-jelly__blob')].map((el, i) => ({
    el, rate: (i % 2 ? -1 : 1) * (0.28 + 0.12 * i), sway: 18 + 10 * i, phase: i * 1.7,
    k: 0.075 + 0.012 * i, d: 0.87 - 0.012 * i, e: 0, ev: 0, l: 0, lv: 0,
  }));
  const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));
  let raf = 0, on = false, lastY = scrollY, lastT = 0, vel = 0, pe = -1, lastQ = -1, top = 0, range = 1, vh = innerHeight;

  // Host geometry is cached on resize; the frame loop reads no layout
  const measure = () => {
    vh = innerHeight;
    if (page) { top = 0; range = Math.max(1, document.documentElement.scrollHeight - vh); return; }
    const r = host.getBoundingClientRect();
    top = r.top + scrollY;
    range = Math.max(1, r.height - vh);
  };

  const tick = (t) => {
    const dt = lastT ? Math.min(64, t - lastT) : 16.7;
    const y = scrollY;
    vel += ((y - lastY) / dt - vel) * 0.35; // smoothed scroll speed, px per ms
    lastT = t;
    lastY = y;
    const p = clamp((y - top) / range, 0, 1);
    pe = pe < 0 ? p : pe + (p - pe) * (1 - 0.86 ** (dt / 16.7));
    const q = Math.round(pe * 100) / 100; // colours repaint in 1% steps only
    if (q !== lastQ) { layer.style.setProperty('--amb-jelly-p', q); lastQ = q; }
    // Stretch target follows speed; when it drops to 0 the springs overshoot into a squash and wobble back
    const stretch = Math.min(0.3, Math.abs(vel) * 0.11);
    const lag = clamp(-vel * 24, -70, 70);
    let moving = Math.abs(p - pe) > 0.0005 || Math.abs(vel) > 0.004;
    for (const b of blobs) {
      b.ev = (b.ev + (stretch - b.e) * b.k) * b.d;
      b.e += b.ev;
      b.lv = (b.lv + (lag - b.l) * b.k) * b.d;
      b.l += b.lv;
      if (Math.abs(b.e) + Math.abs(b.ev) > 0.0015 || Math.abs(b.l) + Math.abs(b.lv) > 0.15) moving = true;
      const x = Math.sin(pe * 6.283 + b.phase) * b.sway;
      const dy = (0.5 - pe) * b.rate * vh + b.l;
      b.el.style.transform = `translate3d(${x.toFixed(1)}px, ${dy.toFixed(1)}px, 0) scale(${(1 - b.e * 0.5).toFixed(4)}, ${(1 + b.e).toFixed(4)})`;
    }
    raf = moving ? requestAnimationFrame(tick) : 0;
    layer.toggleAttribute('data-moving', moving);
  };

  // Run only while the layer is on screen, the tab is visible and motion is allowed
  const wake = () => {
    if (raf || !on || reduce.matches || document.visibilityState === 'hidden') return;
    lastY = scrollY;
    lastT = 0;
    raf = requestAnimationFrame(tick);
  };
  const sleep = () => { cancelAnimationFrame(raf); raf = 0; layer.removeAttribute('data-moving'); };

  measure();
  new IntersectionObserver(([e]) => { on = e.isIntersecting; if (on) wake(); else sleep(); }).observe(layer);
  new ResizeObserver(() => { measure(); wake(); }).observe(host);
  addEventListener('resize', measure, { passive: true });
  addEventListener('scroll', wake, { passive: true });
  document.addEventListener('visibilitychange', () => (document.visibilityState === 'hidden' ? sleep() : wake()));
});
```

## Notes

- **Layer contract:** `.amb-jelly` is decorative (`aria-hidden="true"`, `pointer-events: none`). Make it the first child of a `position: relative; isolation: isolate` host, at `z-index: -1`; the host can be one long section or, as in the demo, a wrapper around several. A sticky, viewport-tall stage keeps the blobs on screen while the host scrolls past, and progress (0–1) runs from the host's top to its bottom. `.amb-jelly--page` fixes the layer behind the whole page (sections need transparent backgrounds) and maps progress to the whole document. Use one ambient background per page.
- **Contrast:** each blob is at most 38% colour over `--surface-deep` at its centre. The colour lanes never make more than two blobs amber at once, so the worst case under `--text-inverse` body copy is two amber centres overlapping: 4.7:1. Muted text only sits on the 72–78% deep panels (5.9:1 or better there), and the headline gradient stays at 3.3:1 or better (large text). `--amb-jelly-scrim: 0.3` adds a deep veil and lifts the worst case to 7.6:1.
- **Performance:** one rAF loop per layer, and it runs only while the layer is on screen, the tab is visible and a spring is still live. Everything settles about 1.5s after scrolling stops, then the loop ends until the next scroll. Each frame writes four `transform`s. `will-change` is on only while the layer carries `data-moving`. Colour progress is written in 1% steps, so the gradients repaint rarely. No blur filters, and no layout reads per frame (host geometry is cached on resize).
- **No JS and reduced motion:** the blobs are round and still, coloured from the mid-page mix (`--amb-jelly-p: 0.3`). Under reduced motion the loop never starts, and the scroll hint skips its three rolls.
- **Support and adapting:** needs `color-mix()` with `calc()` percentages (current Chrome, Safari and Firefox); `svh` falls back to `vh`. Each blob takes `--amb-jelly-x`, `--amb-jelly-y`, `--amb-jelly-size`, plus `--amb-jelly-from` and `--amb-jelly-to` (any colour tokens) for its top-to-bottom lane. Set `--amb-jelly-p` yourself for a fixed palette. The loop listens to window scroll.
