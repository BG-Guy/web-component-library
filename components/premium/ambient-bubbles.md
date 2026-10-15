# Icon Bubbles

A light, sky-gradient ambient layer of glass bubbles, each carrying a small service icon (wrench, drop, bolt, flame, leaf, house, key). As you scroll down they rise a little faster than the page, each at its own speed, swaying side to side with scroll position, so they stop when you stop. A bubble that reaches the top of the screen pops in a quick ring-and-droplet burst and respawns below the fold; brush one with the cursor and it pops too. On phones there are fewer, smaller bubbles. Depends on `tokens/variables.css`.

**Motion:** scroll-driven rise (1.05–1.45× scroll, eased glide to rest) with scroll-position sway · one-shot pop (ring 480ms, six droplets 560ms, `--ease-out`) at the top edge or under the cursor · respawn below the fold · loop stops when the glide settles.

## HTML

```html
<div class="amb-bubbles-demo">
  <div class="amb-bubbles" aria-hidden="true">
    <svg class="amb-bubbles__sprite" focusable="false">
      <symbol id="amb-bubbles-wrench" viewBox="0 0 24 24"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z" /></symbol>
      <symbol id="amb-bubbles-drop" viewBox="0 0 24 24"><path d="M12 3s6 6.4 6 10.5a6 6 0 0 1-12 0C6 9.4 12 3 12 3z" /></symbol>
      <symbol id="amb-bubbles-bolt" viewBox="0 0 24 24"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></symbol>
      <symbol id="amb-bubbles-flame" viewBox="0 0 24 24"><path d="M12 22a7 7 0 0 0 7-7c0-3-2-5.5-3.5-7-.5 2-1.5 3-3 3.5C13 8 12 5 9 3c0 3-4 6-4 12a7 7 0 0 0 7 7z" /></symbol>
      <symbol id="amb-bubbles-leaf" viewBox="0 0 24 24"><path d="M5 19c0-8 5-14 15-15-1 10-7 15-15 15zM5 19l7-7" /></symbol>
      <symbol id="amb-bubbles-house" viewBox="0 0 24 24"><path d="M3 11 12 4l9 7M5 10v10h14V10M10 20v-6h4v6" /></symbol>
      <symbol id="amb-bubbles-key" viewBox="0 0 24 24"><path d="M10.7 12.3 21 2M16 7l3 3M19 4l2 2M7.5 11a4.5 4.5 0 1 0 0 9 4.5 4.5 0 1 0 0-9z" /></symbol>
    </svg>
    <div class="amb-bubbles__stage">
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 8; --amb-bubbles-y: 24; --amb-bubbles-size: 5.5; --amb-bubbles-c: var(--primary)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-drop" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 20; --amb-bubbles-y: 80; --amb-bubbles-size: 3.2; --amb-bubbles-c: var(--accent)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-bolt" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 90; --amb-bubbles-y: 30; --amb-bubbles-size: 6; --amb-bubbles-c: var(--primary-2)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-leaf" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 80; --amb-bubbles-y: 86; --amb-bubbles-size: 3.6; --amb-bubbles-c: var(--primary)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-wrench" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 54; --amb-bubbles-y: 108; --amb-bubbles-size: 4.4; --amb-bubbles-c: var(--accent)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-flame" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 5; --amb-bubbles-y: 60; --amb-bubbles-size: 3; --amb-bubbles-c: var(--primary-2)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-key" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 95; --amb-bubbles-y: 64; --amb-bubbles-size: 3.4; --amb-bubbles-c: var(--accent)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-house" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 34; --amb-bubbles-y: 126; --amb-bubbles-size: 5; --amb-bubbles-c: var(--primary)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-house" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 68; --amb-bubbles-y: 118; --amb-bubbles-size: 2.8; --amb-bubbles-c: var(--primary-2)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-drop" /></svg></span>
      <span class="amb-bubbles__bubble" style="--amb-bubbles-x: 74; --amb-bubbles-y: 48; --amb-bubbles-size: 2.6; --amb-bubbles-c: var(--primary)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-flame" /></svg></span>
      <span class="amb-bubbles__bubble amb-bubbles__bubble--wide" style="--amb-bubbles-x: 14; --amb-bubbles-y: 112; --amb-bubbles-size: 4; --amb-bubbles-c: var(--accent)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-wrench" /></svg></span>
      <span class="amb-bubbles__bubble amb-bubbles__bubble--wide" style="--amb-bubbles-x: 88; --amb-bubbles-y: 110; --amb-bubbles-size: 4.6; --amb-bubbles-c: var(--primary)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-key" /></svg></span>
      <span class="amb-bubbles__bubble amb-bubbles__bubble--wide" style="--amb-bubbles-x: 62; --amb-bubbles-y: 14; --amb-bubbles-size: 2.4; --amb-bubbles-c: var(--primary-2)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-bolt" /></svg></span>
      <span class="amb-bubbles__bubble amb-bubbles__bubble--wide" style="--amb-bubbles-x: 28; --amb-bubbles-y: 42; --amb-bubbles-size: 2.4; --amb-bubbles-c: var(--accent)"><svg class="amb-bubbles__icon" viewBox="0 0 24 24" focusable="false"><use href="#amb-bubbles-leaf" /></svg></span>
      <span class="amb-bubbles__burst"><i class="amb-bubbles__ring"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i></span>
      <span class="amb-bubbles__burst"><i class="amb-bubbles__ring"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i></span>
      <span class="amb-bubbles__burst"><i class="amb-bubbles__ring"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i></span>
      <span class="amb-bubbles__burst"><i class="amb-bubbles__ring"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i><i class="amb-bubbles__drop"></i></span>
    </div>
  </div>

  <section class="amb-bubbles-demo__section amb-bubbles-demo__section--hero" aria-labelledby="amb-bubbles-hero-title">
    <div class="amb-bubbles-demo__inner">
      <p class="amb-bubbles-demo__eyebrow">Brand Home Care · Springfield</p>
      <h2 id="amb-bubbles-hero-title" class="amb-bubbles-demo__title">All your home fixes, <em>one friendly crew.</em></h2>
      <p class="amb-bubbles-demo__lead">Plumbing, electrical, heating, locks and the garden too. One number to call, one tidy team, and one bill with no surprises.</p>
      <div class="amb-bubbles-demo__actions">
        <a class="amb-bubbles-demo__btn amb-bubbles-demo__btn--primary" href="#amb-bubbles-book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-bubbles-demo__btn" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
      <p class="amb-bubbles-demo__hint">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
        Scroll
      </p>
    </div>
  </section>

  <section class="amb-bubbles-demo__section" aria-labelledby="amb-bubbles-services-title">
    <div class="amb-bubbles-demo__inner">
      <header class="amb-bubbles-demo__head">
        <p class="amb-bubbles-demo__eyebrow">Services</p>
        <h2 id="amb-bubbles-services-title" class="amb-bubbles-demo__h2">Six trades under one roof.</h2>
        <p class="amb-bubbles-demo__intro">Licensed, insured and background-checked. Prices are fixed before we start.</p>
      </header>
      <ul class="amb-bubbles-demo__grid" role="list">
        <li class="amb-bubbles-demo__card" style="--amb-bubbles-c: var(--primary)">
          <svg class="amb-bubbles-demo__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><use href="#amb-bubbles-drop" /></svg>
          <h3><a class="amb-bubbles-demo__link" href="#amb-bubbles-book">Plumbing</a></h3>
          <p>Leaks, clogs, water heaters and fixtures.</p>
          <p class="amb-bubbles-demo__price">from <strong>$89</strong></p>
        </li>
        <li class="amb-bubbles-demo__card" style="--amb-bubbles-c: var(--accent)">
          <svg class="amb-bubbles-demo__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><use href="#amb-bubbles-bolt" /></svg>
          <h3><a class="amb-bubbles-demo__link" href="#amb-bubbles-book">Electrical</a></h3>
          <p>Outlets, lighting, panels and EV chargers.</p>
          <p class="amb-bubbles-demo__price">from <strong>$99</strong></p>
        </li>
        <li class="amb-bubbles-demo__card" style="--amb-bubbles-c: var(--primary-2)">
          <svg class="amb-bubbles-demo__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><use href="#amb-bubbles-flame" /></svg>
          <h3><a class="amb-bubbles-demo__link" href="#amb-bubbles-book">Heating &amp; cooling</a></h3>
          <p>Tune-ups, repairs and smart thermostats.</p>
          <p class="amb-bubbles-demo__price">from <strong>$129</strong></p>
        </li>
        <li class="amb-bubbles-demo__card" style="--amb-bubbles-c: var(--primary-2)">
          <svg class="amb-bubbles-demo__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><use href="#amb-bubbles-leaf" /></svg>
          <h3><a class="amb-bubbles-demo__link" href="#amb-bubbles-book">Garden</a></h3>
          <p>Hedges, lawns, gutters and seasonal clear-ups.</p>
          <p class="amb-bubbles-demo__price">from <strong>$59</strong></p>
        </li>
        <li class="amb-bubbles-demo__card" style="--amb-bubbles-c: var(--primary)">
          <svg class="amb-bubbles-demo__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><use href="#amb-bubbles-key" /></svg>
          <h3><a class="amb-bubbles-demo__link" href="#amb-bubbles-book">Locks</a></h3>
          <p>Lock-outs, rekeys and smart locks fitted.</p>
          <p class="amb-bubbles-demo__price">from <strong>$79</strong></p>
        </li>
        <li class="amb-bubbles-demo__card" style="--amb-bubbles-c: var(--accent)">
          <svg class="amb-bubbles-demo__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><use href="#amb-bubbles-wrench" /></svg>
          <h3><a class="amb-bubbles-demo__link" href="#amb-bubbles-book">Handyman</a></h3>
          <p>Doors, shelves, drywall and the to-do list.</p>
          <p class="amb-bubbles-demo__price">from <strong>$69</strong></p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-bubbles-demo__section" aria-labelledby="amb-bubbles-proof-title">
    <div class="amb-bubbles-demo__inner">
      <div class="amb-bubbles-demo__proof">
        <figure class="amb-bubbles-demo__quote">
          <h2 id="amb-bubbles-proof-title" class="amb-bubbles-demo__eyebrow">From the neighbours</h2>
          <blockquote><p>"Booked a plumber for the leak and asked about the dead porch light. Same visit, same crew, both fixed by noon."</p></blockquote>
          <figcaption><span class="amb-bubbles-demo__avatar" aria-hidden="true">AK</span><span><strong>Ana K.</strong> Northside</span></figcaption>
        </figure>
        <dl class="amb-bubbles-demo__stats">
          <div><dt>Average rating</dt><dd>4.9<small>/5</small></dd></div>
          <div><dt>Homes looked after</dt><dd>3,400</dd></div>
          <div><dt>Guarantee on every job</dt><dd>12<small>mo</small></dd></div>
        </dl>
      </div>
    </div>
  </section>

  <section class="amb-bubbles-demo__section" id="amb-bubbles-book" aria-labelledby="amb-bubbles-cta-title">
    <div class="amb-bubbles-demo__inner">
      <div class="amb-bubbles-demo__panel">
        <h2 id="amb-bubbles-cta-title" class="amb-bubbles-demo__h2">One call, everything sorted.</h2>
        <p class="amb-bubbles-demo__intro">Same-week visits across Westlake, Northside and Riverside.</p>
        <div class="amb-bubbles-demo__actions">
          <a class="amb-bubbles-demo__btn amb-bubbles-demo__btn--primary" href="#amb-bubbles-book">
            Book a visit
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
          <a class="amb-bubbles-demo__btn" href="mailto:hello@example.com">hello@example.com</a>
        </div>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Layer: decorative, first child of a relative + isolated host; a sticky, viewport-tall sky holds the bubbles */
.amb-bubbles {
  --amb-bubbles-k: 0.72; /* bubble scale: phones */
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-bubbles--page { position: fixed; }
.amb-bubbles__sprite { position: absolute; width: 0; height: 0; overflow: hidden; }
.amb-bubbles__stage {
  position: sticky; top: 0; height: 100vh; height: 100svh; overflow: clip;
  background:
    radial-gradient(60% 45% at 86% 6%, color-mix(in srgb, var(--accent) 16%, transparent), transparent 70%),
    linear-gradient(180deg, color-mix(in srgb, var(--primary) 15%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 7%, var(--surface-light)) 62%, var(--surface-light));
}
.amb-bubbles--page .amb-bubbles__stage { position: relative; height: 100%; }
/* Contrast guard: --amb-bubbles-scrim (0–1) fades a light veil over sky and bubbles */
.amb-bubbles__stage::after { content: ""; position: absolute; inset: 0; background: color-mix(in srgb, var(--surface-light) calc(var(--amb-bubbles-scrim, 0) * 100%), transparent); }

/* Glass bubble: clear centre, tinted rim, iridescent kisses, highlight crescent and glint; sized in em */
.amb-bubbles__bubble {
  position: absolute; left: calc(var(--amb-bubbles-x) * 1%); top: calc(var(--amb-bubbles-y) * 1%);
  width: 1em; height: 1em; margin: -0.5em 0 0 -0.5em; border-radius: 50%;
  font-size: calc(var(--amb-bubbles-size) * var(--amb-bubbles-k) * 1rem);
  background:
    radial-gradient(circle at 30% 72%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 42%),
    radial-gradient(circle at 74% 78%, color-mix(in srgb, var(--accent) 16%, transparent), transparent 40%),
    radial-gradient(circle, color-mix(in srgb, var(--surface-light) 18%, transparent) 48%, color-mix(in srgb, var(--amb-bubbles-c) 16%, transparent) 74%, color-mix(in srgb, var(--amb-bubbles-c) 34%, transparent));
  box-shadow: inset 0 0 0 max(1px, 0.02em) color-mix(in srgb, var(--amb-bubbles-c) 40%, transparent),
    0 0.12em 0.3em -0.12em color-mix(in srgb, var(--amb-bubbles-c) 30%, transparent);
}
.amb-bubbles__bubble::before { /* highlight crescent */
  content: ""; position: absolute; inset: 8%; border-radius: 50%; rotate: 10deg;
  box-shadow: inset 0.045em 0.055em 0.015em -0.012em color-mix(in srgb, var(--surface-light) 92%, transparent);
}
.amb-bubbles__bubble::after { /* glint */
  content: ""; position: absolute; left: 24%; top: 17%; width: 11%; height: 7%; border-radius: 50%; rotate: -38deg;
  background: var(--surface-light);
}
.amb-bubbles__bubble--wide { display: none; }
.amb-bubbles__icon {
  position: absolute; left: 29%; top: 29%; width: 42%; height: 42%;
  fill: none; stroke: color-mix(in srgb, var(--amb-bubbles-c) 60%, transparent); stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round;
}

/* Pop burst (pooled, played by JS with one-shot animations; hidden whenever idle) */
.amb-bubbles__burst { position: absolute; left: 0; top: 0; width: 4rem; aspect-ratio: 1; color: var(--amb-bubbles-c, var(--primary)); }
.amb-bubbles__ring, .amb-bubbles__drop { position: absolute; border-radius: 50%; visibility: hidden; }
.amb-bubbles__ring { inset: 0; box-shadow: inset 0 0 0 2px color-mix(in srgb, currentColor 55%, transparent), 0 0 0 1px color-mix(in srgb, var(--surface-light) 70%, transparent); }
.amb-bubbles__drop { left: 50%; top: 50%; width: 0.4rem; height: 0.4rem; margin: -0.2rem; background: color-mix(in srgb, currentColor 55%, var(--surface-light)); }

@media (min-width: 768px) {
  .amb-bubbles { --amb-bubbles-k: 0.9; }
  .amb-bubbles__bubble--wide { display: block; }
}
@media (min-width: 1200px) { .amb-bubbles { --amb-bubbles-k: 1; } }

/* ---- Demo page (light sky) ---- */
.amb-bubbles-demo {
  position: relative; isolation: isolate; overflow-x: clip; background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
  --amb-bubbles-soft: color-mix(in srgb, var(--text-main) 80%, var(--surface-light));
}
.amb-bubbles-demo__section { padding-block: clamp(5rem, 10vw, 7.5rem); }
.amb-bubbles-demo__section--hero { display: grid; align-items: center; min-height: 90vh; min-height: 90svh; text-align: center; }
.amb-bubbles-demo__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); box-sizing: border-box; }

.amb-bubbles-demo__eyebrow {
  display: inline-block; margin: 0; padding: 0.375rem 0.875rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-light) 90%, transparent); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
  font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.amb-bubbles-demo__title {
  max-width: 14ch; margin: 1.25rem auto 0; font: 600 clamp(2.5rem, 1.2rem + 5.4vw, 5.25rem)/1 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-bubbles-demo__title em {
  font-style: normal; background: linear-gradient(100deg, var(--primary), color-mix(in srgb, var(--primary-2) 75%, var(--text-main)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.amb-bubbles-demo__lead { max-width: 34rem; margin: 1.25rem auto 0; font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.amb-bubbles-demo__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.amb-bubbles-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-bubbles-demo__btn:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-lg); }
.amb-bubbles-demo__btn:active { transform: scale(0.97); }
.amb-bubbles-demo__btn--primary {
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 12px 28px -12px var(--primary);
}
.amb-bubbles-demo__btn--primary:hover { box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 16px 34px -12px var(--primary); }
.amb-bubbles-demo__section svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-bubbles-demo :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.amb-bubbles-demo__hint {
  display: flex; flex-direction: column; align-items: center; gap: 0.375rem; margin: 3.5rem 0 0;
  font: 500 0.6875rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.amb-bubbles-demo__hint svg { animation: amb-bubbles-nudge 1.4s var(--ease-in-out) 3; } /* three nudges, then still */

/* Section heads */
.amb-bubbles-demo__head { max-width: 38rem; margin: 0 auto 3rem; text-align: center; }
.amb-bubbles-demo__h2 { margin: 1rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.8vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.amb-bubbles-demo__intro { max-width: 32rem; margin: 1rem auto 0; font-size: 1.0625rem; line-height: 1.6; }

/* Service cards: opaque white, the icon sits in a little glass bubble */
.amb-bubbles-demo__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.amb-bubbles-demo__card {
  position: relative; display: flex; flex-direction: column; gap: 0.5rem; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-lg);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-bubbles-demo__card:hover { transform: translateY(-4px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl); }
.amb-bubbles-demo__icon {
  box-sizing: content-box; width: 1.5rem; height: 1.5rem; padding: 0.75rem; border-radius: 50%; color: color-mix(in srgb, var(--amb-bubbles-c) 75%, var(--text-main));
  background: radial-gradient(circle, transparent 50%, color-mix(in srgb, var(--amb-bubbles-c) 22%, transparent));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--amb-bubbles-c) 35%, transparent), inset 0.25rem 0.3rem 0 -0.15rem var(--surface-light);
}
.amb-bubbles-demo__card h3 { margin: 0.75rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-bubbles-demo__card p { margin: 0; color: var(--amb-bubbles-soft); line-height: 1.55; }
.amb-bubbles-demo__link { color: inherit; text-decoration: none; }
.amb-bubbles-demo__link::after { content: ""; position: absolute; inset: 0; border-radius: inherit; }
.amb-bubbles-demo .amb-bubbles-demo__link:focus-visible { outline: none; }
.amb-bubbles-demo__link:focus-visible::after { outline: 2px solid var(--primary); outline-offset: 3px; }
.amb-bubbles-demo__card .amb-bubbles-demo__price { margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--border-subtle); font: 500 0.8125rem var(--font-mono); }
.amb-bubbles-demo__price strong { color: var(--text-main); font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }

/* Proof */
.amb-bubbles-demo__proof { display: grid; gap: 1rem; max-width: 64rem; margin-inline: auto; }
.amb-bubbles-demo__quote {
  display: grid; justify-items: start; gap: 1.25rem; margin: 0; padding: clamp(1.5rem, 4vw, 2.5rem); border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.amb-bubbles-demo__quote blockquote { margin: 0; }
.amb-bubbles-demo__quote blockquote p { margin: 0; font: 500 clamp(1.25rem, 1rem + 1vw, 1.75rem)/1.4 var(--font-display); letter-spacing: -0.01em; }
.amb-bubbles-demo__quote figcaption { display: flex; align-items: center; gap: 0.75rem; color: var(--amb-bubbles-soft); font-size: 0.875rem; }
.amb-bubbles-demo__quote figcaption strong { display: block; color: var(--text-main); }
.amb-bubbles-demo__avatar { display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%; background: var(--gradient-brand); color: var(--text-inverse); font: 700 0.75rem var(--font-sans); }
.amb-bubbles-demo__stats { display: grid; gap: 1rem; margin: 0; }
.amb-bubbles-demo__stats div {
  display: flex; flex-direction: column-reverse; justify-content: center; gap: 0.375rem; padding: 1.25rem 1.5rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md);
}
.amb-bubbles-demo__stats dt { color: var(--amb-bubbles-soft); font: 500 0.75rem var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.amb-bubbles-demo__stats dd { margin: 0; font: 600 clamp(2rem, 1.6rem + 1.6vw, 2.75rem)/1 var(--font-display); letter-spacing: var(--tracking-display); }
.amb-bubbles-demo__stats small { margin-left: 0.125rem; color: var(--primary); font-size: 0.45em; letter-spacing: 0; }

/* CTA panel */
.amb-bubbles-demo__panel {
  max-width: 44rem; margin-inline: auto; padding: clamp(2rem, 6vw, 3.5rem) clamp(1.25rem, 5vw, 3rem); border-radius: var(--radius-2xl); text-align: center;
  background: radial-gradient(80% 60% at 50% 0%, color-mix(in srgb, var(--primary) 8%, transparent), transparent 70%), var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.amb-bubbles-demo__panel .amb-bubbles-demo__h2 { margin-top: 0; }

@media (min-width: 600px) { .amb-bubbles-demo__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1024px) {
  .amb-bubbles-demo__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .amb-bubbles-demo__proof { grid-template-columns: 1.5fr 1fr; }
}

@media (prefers-reduced-motion: reduce) {
  .amb-bubbles__bubble { transform: none !important; }
  .amb-bubbles-demo__hint svg { animation: none; }
}
@keyframes amb-bubbles-nudge { 50% { transform: translateY(5px); } }
```

## JS

```js
// Icon Bubbles: glass bubbles rise a little faster than the page as you scroll and sway with scroll
// position. Near the top, or under the cursor, a bubble pops (one-shot burst) and respawns below the fold.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const EASE = 'cubic-bezier(0.16, 1, 0.3, 1)'; // --ease-out

document.querySelectorAll('.amb-bubbles').forEach((layer) => {
  if (reduce.matches) return; // the resting bubbles are the reduced-motion still
  const page = layer.classList.contains('amb-bubbles--page');
  const host = layer.parentElement;
  const stage = layer.querySelector('.amb-bubbles__stage');
  const bursts = [...layer.querySelectorAll('.amb-bubbles__burst')];
  const bubbles = [...layer.querySelectorAll('.amb-bubbles__bubble')].map((el, i) => ({ el, phase: i * 2.4, off: 0, dx: 0, r: 0 }));
  let raf = 0, on = false, sy = scrollY, h = 0, left = 0, hostTop = 0, hostH = 0, ptr = null, next = 0;

  // Sizes and resting centres are cached on resize; bubbles hidden on phones measure 0 and are skipped
  const measure = () => {
    const s = stage.getBoundingClientRect(), r = host.getBoundingClientRect();
    [h, left, hostTop, hostH] = [s.height, s.left, r.top + scrollY, r.height];
    for (const b of bubbles) {
      b.r = b.el.offsetWidth / 2;
      b.x0 = b.el.offsetLeft + b.r;
      b.y0 = b.el.offsetTop + b.r;
      b.speed = 1.05 + Math.min(0.4, b.r / 120); // bigger, nearer bubbles rise faster
      b.sway = 6 + b.r * 0.35;
    }
  };
  const stageTop = () => (page ? 0 : Math.max(Math.min(0, hostTop + hostH - h - scrollY), hostTop - scrollY));
  const place = (b) => {
    b.dx = Math.sin(sy * 0.0045 + b.phase) * b.sway; // sway follows scroll position, so it stops when you do
    b.el.style.transform = `translate3d(${b.dx.toFixed(1)}px, ${b.off.toFixed(1)}px, 0)`;
  };
  const respawn = (b) => { b.off = h * (1.04 + Math.random() * 0.5) + b.r - b.y0; }; // just below the fold

  // Pop: a pooled ring + six droplets, one-shot (≤ 560ms), then the bubble starts again below the fold
  const pop = (b) => {
    const burst = bursts[next++ % bursts.length];
    const [ring, ...drops] = burst.children;
    const show = { visibility: 'visible' };
    burst.style.setProperty('--amb-bubbles-c', b.el.style.getPropertyValue('--amb-bubbles-c'));
    burst.style.width = `${b.r * 2}px`;
    burst.style.transform = `translate3d(${b.x0 + b.dx - b.r}px, ${b.y0 + b.off - b.r}px, 0)`;
    ring.animate([{ ...show, opacity: 0.9, transform: 'scale(0.75)' }, { ...show, opacity: 0, transform: 'scale(1.55)' }], { duration: 480, easing: EASE });
    drops.forEach((d, k) => {
      const turn = `rotate(${k * 60 + 25}deg)`;
      d.animate([{ ...show, opacity: 1, transform: `${turn} translateY(0) scale(1)` },
        { ...show, opacity: 0, transform: `${turn} translateY(${-b.r * 1.5}px) scale(0.3)` }], { duration: 560, easing: EASE });
    });
    respawn(b);
    place(b);
  };

  const tick = () => {
    const y = scrollY, prev = sy;
    sy = Math.abs(y - sy) < 0.5 ? y : sy + (y - sy) * 0.22; // eased scroll: bubbles glide to rest
    const dy = sy - prev, top = stageTop();
    for (const b of bubbles) {
      if (!b.r) continue;
      b.off -= dy * b.speed;
      const vy = b.y0 + b.off + top; // centre, in viewport pixels
      if (dy > 0 && vy - b.r < h * 0.08) {
        if (vy + b.r > 0) pop(b); else respawn(b); // pop where it can be seen; recycle silently otherwise
      } else if (dy < 0 && vy - b.r > h * 1.6) {
        b.off -= h * 1.6 + b.r * 2; // scrolling back up: re-enter from just above the top
      }
      place(b);
    }
    if (ptr) { // the cursor pops what it touches; the layer itself never takes pointer events
      const px = ptr.x - left, py = ptr.y - top;
      for (const b of bubbles) if (b.r && Math.hypot(px - b.x0 - b.dx, py - b.y0 - b.off) < b.r) pop(b);
      ptr = null;
    }
    raf = sy !== y ? requestAnimationFrame(tick) : 0;
  };

  // Run only while the layer is on screen, the tab is visible and the glide is still moving
  const wake = () => {
    if (raf || !on || reduce.matches || document.visibilityState === 'hidden') return;
    raf = requestAnimationFrame(tick);
  };
  const sleep = () => { cancelAnimationFrame(raf); raf = 0; };

  measure();
  new ResizeObserver(measure).observe(stage);
  new IntersectionObserver(([e]) => { on = e.isIntersecting; sy = scrollY; if (on) wake(); else sleep(); }).observe(layer);
  addEventListener('resize', measure, { passive: true });
  addEventListener('scroll', wake, { passive: true });
  addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'touch') { ptr = { x: e.clientX, y: e.clientY }; wake(); }
  }, { passive: true });
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') sleep(); else { sy = scrollY; wake(); }
  });
});
```

## Notes

- **Layer contract:** `.amb-bubbles` is decorative (`aria-hidden="true"`, `pointer-events: none`). Make it the first child of a `position: relative; isolation: isolate` host, at `z-index: -1`; the host can be one long section or, as in the demo, a wrapper around several (sections stay transparent so the sky shows). A sticky, viewport-tall stage holds the sky and the bubbles. Cursor pops are hit-tested from a passive `pointermove` listener on `window` (mouse and pen), so the layer never takes a click. `.amb-bubbles--page` fixes it behind the whole page. Include the icon sprite once per page (its ids must stay unique). Use one ambient background per page.
- **Contrast:** bubbles are clear glass: the centre is at most 18% white, the rim at most 34% tint and the icons 60% of a colour token. Worst case under the demo's body copy is `--text-main` over a `--primary` icon stroke on the bluest part of the sky: 5.2:1. The softer secondary text only sits on opaque cards, and the headline gradient stays at 4.2:1 or better. `--amb-bubbles-scrim: 0.5` fades a light veil over the sky and bubbles (secondary text over an icon then reaches 4.7:1).
- **Performance:** one rAF loop per layer. Scroll is eased, so the bubbles glide to rest about half a second after you stop, then the loop ends until the next scroll or pointer move; it never runs off screen or in a hidden tab. Each frame writes one `transform` per bubble (14 on desktop, 10 on phones). Pops reuse a pool of four bursts animated with one-shot Web Animations on `transform` and `opacity`; their pieces are `visibility: hidden` when idle. Geometry is cached on resize, with no layout reads per frame. No blur and no `backdrop-filter`.
- **No JS and reduced motion:** the bubbles rest in the sky as a still composition, with nothing rising or popping. The scroll hint also skips its three nudges.
- **Adapting:** place each bubble with `--amb-bubbles-x`/`--amb-bubbles-y` (% of the viewport-tall stage; y above 100 starts below the fold) and size it with `--amb-bubbles-size` (rem). Tint it with `--amb-bubbles-c` (any colour token) and pick its icon with `<use href="#amb-bubbles-…">`. Add `--wide` to keep a bubble off phones. Rise speed (1.05–1.45× scroll) and sway come from each bubble's size in the JS. The loop listens to window scroll.
