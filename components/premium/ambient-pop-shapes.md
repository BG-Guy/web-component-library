# Pop Shapes

A light ambient layer of glossy shapes built purely in CSS (spheres with a specular highlight, pills, conic rings, soft rounded cubes and a few stars) parked in the margins of each section. When a section scrolls into view its shapes pop in on a spring, one after another; while you scroll they drift by their depth and tilt with your scroll speed, then settle, and the loop stops. On phones fewer, smaller shapes peek in from the screen edges, in the padding bands above and below the copy. Depends on `tokens/variables.css`.

**Motion:** staggered pop-in with overshoot and a twist (`--dur-5`, `--ease-out`, `--stagger`) · depth parallax eased from scroll position · damped-spring tilt from scroll velocity · loop stops once everything settles.

## HTML

```html
<div class="amb-pop-demo">
  <section class="amb-pop-demo__section amb-pop-demo__section--hero" aria-labelledby="amb-pop-hero-title">
    <div class="amb-pop" aria-hidden="true">
      <span class="amb-pop__shape amb-pop__shape--sphere" style="--amb-pop-x: 7; --amb-pop-y: 24; --amb-pop-mx: 4; --amb-pop-my: 6; --amb-pop-size: 6; --amb-pop-depth: 0.9; --amb-pop-c: var(--primary); --amb-pop-i: 0"></span>
      <span class="amb-pop__shape amb-pop__shape--ring" style="--amb-pop-x: 92; --amb-pop-y: 18; --amb-pop-mx: 97; --amb-pop-my: 5; --amb-pop-size: 6.5; --amb-pop-depth: 0.5; --amb-pop-c: var(--primary-2); --amb-pop-i: 1"></span>
      <span class="amb-pop__shape amb-pop__shape--pill" style="--amb-pop-x: 89; --amb-pop-y: 72; --amb-pop-mx: 97; --amb-pop-my: 95; --amb-pop-size: 5.5; --amb-pop-depth: 1.1; --amb-pop-r: -28deg; --amb-pop-c: var(--accent); --amb-pop-i: 2"></span>
      <span class="amb-pop__shape amb-pop__shape--cube" style="--amb-pop-x: 9; --amb-pop-y: 78; --amb-pop-mx: 3; --amb-pop-my: 95; --amb-pop-size: 4; --amb-pop-depth: 0.7; --amb-pop-r: 16deg; --amb-pop-c: var(--primary); --amb-pop-i: 3"></span>
      <span class="amb-pop__shape amb-pop__shape--star amb-pop__shape--wide" style="--amb-pop-x: 19; --amb-pop-y: 12; --amb-pop-size: 2.4; --amb-pop-depth: 1.3; --amb-pop-r: 12deg; --amb-pop-c: var(--accent); --amb-pop-i: 4"></span>
      <span class="amb-pop__shape amb-pop__shape--sphere amb-pop__shape--wide" style="--amb-pop-x: 86; --amb-pop-y: 44; --amb-pop-size: 2.2; --amb-pop-depth: 1.4; --amb-pop-c: var(--accent); --amb-pop-i: 5"></span>
      <span class="amb-pop__shape amb-pop__shape--cube amb-pop__shape--wide" style="--amb-pop-x: 14; --amb-pop-y: 52; --amb-pop-size: 2.6; --amb-pop-depth: -0.6; --amb-pop-r: -10deg; --amb-pop-c: var(--primary-2); --amb-pop-i: 6"></span>
    </div>
    <div class="amb-pop-demo__inner">
      <p class="amb-pop-demo__eyebrow"><span class="amb-pop-demo__dot"></span>Brand Home Services · Springfield</p>
      <h2 id="amb-pop-hero-title" class="amb-pop-demo__title">Home repairs that <em>make you smile.</em></h2>
      <p class="amb-pop-demo__lead">Plumbing, electrical and handyman jobs by licensed local pros. Flat-rate prices, on-time arrivals and a spotless finish.</p>
      <div class="amb-pop-demo__actions">
        <a class="amb-pop-demo__btn amb-pop-demo__btn--primary" href="#amb-pop-book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="amb-pop-demo__btn" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
      <p class="amb-pop-demo__hint">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
        Scroll
      </p>
    </div>
  </section>

  <section class="amb-pop-demo__section" aria-labelledby="amb-pop-services-title">
    <div class="amb-pop" aria-hidden="true">
      <span class="amb-pop__shape amb-pop__shape--pill" style="--amb-pop-x: 5; --amb-pop-y: 9; --amb-pop-mx: 3; --amb-pop-my: 3; --amb-pop-size: 5; --amb-pop-depth: 0.8; --amb-pop-r: 32deg; --amb-pop-c: var(--primary); --amb-pop-i: 0"></span>
      <span class="amb-pop__shape amb-pop__shape--sphere" style="--amb-pop-x: 95; --amb-pop-y: 14; --amb-pop-mx: 97; --amb-pop-my: 3; --amb-pop-size: 4.2; --amb-pop-depth: 1.1; --amb-pop-c: var(--accent); --amb-pop-i: 1"></span>
      <span class="amb-pop__shape amb-pop__shape--star" style="--amb-pop-x: 93; --amb-pop-y: 90; --amb-pop-mx: 96; --amb-pop-my: 97.5; --amb-pop-size: 2.6; --amb-pop-depth: 1.2; --amb-pop-r: -8deg; --amb-pop-c: var(--primary); --amb-pop-i: 2"></span>
      <span class="amb-pop__shape amb-pop__shape--ring amb-pop__shape--wide" style="--amb-pop-x: 4; --amb-pop-y: 66; --amb-pop-size: 5; --amb-pop-depth: 0.6; --amb-pop-c: var(--primary); --amb-pop-i: 3"></span>
      <span class="amb-pop__shape amb-pop__shape--cube amb-pop__shape--wide" style="--amb-pop-x: 97; --amb-pop-y: 52; --amb-pop-size: 3.6; --amb-pop-depth: 0.9; --amb-pop-r: 24deg; --amb-pop-c: var(--accent); --amb-pop-i: 4"></span>
      <span class="amb-pop__shape amb-pop__shape--sphere amb-pop__shape--wide" style="--amb-pop-x: 9; --amb-pop-y: 94; --amb-pop-size: 2.8; --amb-pop-depth: 1.3; --amb-pop-c: var(--primary-2); --amb-pop-i: 5"></span>
    </div>
    <div class="amb-pop-demo__inner">
      <header class="amb-pop-demo__head">
        <p class="amb-pop-demo__eyebrow">Services</p>
        <h2 id="amb-pop-services-title" class="amb-pop-demo__h2">One call fixes most things.</h2>
        <p class="amb-pop-demo__intro">A written price before we start and a 12-month guarantee after we leave.</p>
      </header>
      <ul class="amb-pop-demo__grid" role="list">
        <li class="amb-pop-demo__card">
          <span class="amb-pop-demo__icon" style="--amb-pop-c: var(--primary)"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 3s6 6.4 6 10.5a6 6 0 0 1-12 0C6 9.4 12 3 12 3zM9.5 14a2.5 2.5 0 0 0 2.5 2.5" /></svg></span>
          <h3><a class="amb-pop-demo__link" href="#amb-pop-book">Plumbing</a></h3>
          <p>Leaks, clogs and new fixtures, sorted the same day.</p>
          <p class="amb-pop-demo__price">from <strong>$89</strong><span class="amb-pop-demo__go">Book<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span></p>
        </li>
        <li class="amb-pop-demo__card">
          <span class="amb-pop-demo__icon" style="--amb-pop-c: var(--accent)"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg></span>
          <h3><a class="amb-pop-demo__link" href="#amb-pop-book">Electrical</a></h3>
          <p>Outlets, lighting and panel upgrades, done to code.</p>
          <p class="amb-pop-demo__price">from <strong>$99</strong><span class="amb-pop-demo__go">Book<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span></p>
        </li>
        <li class="amb-pop-demo__card">
          <span class="amb-pop-demo__icon" style="--amb-pop-c: var(--primary-2)"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 22a7 7 0 0 0 7-7c0-3-2-5.5-3.5-7-.5 2-1.5 3-3 3.5C13 8 12 5 9 3c0 3-4 6-4 12a7 7 0 0 0 7 7z" /></svg></span>
          <h3><a class="amb-pop-demo__link" href="#amb-pop-book">Heating &amp; cooling</a></h3>
          <p>Tune-ups and repairs before the weather turns.</p>
          <p class="amb-pop-demo__price">from <strong>$129</strong><span class="amb-pop-demo__go">Book<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span></p>
        </li>
        <li class="amb-pop-demo__card">
          <span class="amb-pop-demo__icon" style="--amb-pop-c: var(--primary)"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.6 2.6-2.4-.6-.6-2.4z" /></svg></span>
          <h3><a class="amb-pop-demo__link" href="#amb-pop-book">Handyman</a></h3>
          <p>Shelves, doors and the to-do list, in one visit.</p>
          <p class="amb-pop-demo__price">from <strong>$69</strong><span class="amb-pop-demo__go">Book<svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></span></p>
        </li>
      </ul>
    </div>
  </section>

  <section class="amb-pop-demo__section" aria-labelledby="amb-pop-proof-title">
    <div class="amb-pop" aria-hidden="true">
      <span class="amb-pop__shape amb-pop__shape--ring" style="--amb-pop-x: 94; --amb-pop-y: 22; --amb-pop-mx: 97; --amb-pop-my: 4; --amb-pop-size: 5.5; --amb-pop-depth: 0.7; --amb-pop-c: var(--accent); --amb-pop-i: 0"></span>
      <span class="amb-pop__shape amb-pop__shape--cube" style="--amb-pop-x: 6; --amb-pop-y: 30; --amb-pop-mx: 3; --amb-pop-my: 5; --amb-pop-size: 4.2; --amb-pop-depth: 0.9; --amb-pop-r: -14deg; --amb-pop-c: var(--primary-2); --amb-pop-i: 1"></span>
      <span class="amb-pop__shape amb-pop__shape--sphere" style="--amb-pop-x: 92; --amb-pop-y: 86; --amb-pop-mx: 96; --amb-pop-my: 96; --amb-pop-size: 3.6; --amb-pop-depth: 1.2; --amb-pop-c: var(--primary); --amb-pop-i: 2"></span>
      <span class="amb-pop__shape amb-pop__shape--pill amb-pop__shape--wide" style="--amb-pop-x: 8; --amb-pop-y: 82; --amb-pop-size: 5; --amb-pop-depth: 0.6; --amb-pop-r: 70deg; --amb-pop-c: var(--primary-2); --amb-pop-i: 3"></span>
      <span class="amb-pop__shape amb-pop__shape--star amb-pop__shape--wide" style="--amb-pop-x: 15; --amb-pop-y: 9; --amb-pop-size: 2.2; --amb-pop-depth: 1.4; --amb-pop-r: 20deg; --amb-pop-c: var(--primary-2); --amb-pop-i: 4"></span>
    </div>
    <div class="amb-pop-demo__inner">
      <header class="amb-pop-demo__head">
        <p class="amb-pop-demo__eyebrow">Proof</p>
        <h2 id="amb-pop-proof-title" class="amb-pop-demo__h2">Springfield's five-star fixers.</h2>
      </header>
      <dl class="amb-pop-demo__stats">
        <div><dt>Average rating</dt><dd>4.9<small>/5</small></dd></div>
        <div><dt>Average arrival</dt><dd>45<small>min</small></dd></div>
        <div><dt>Jobs finished</dt><dd>12k<small>+</small></dd></div>
      </dl>
      <figure class="amb-pop-demo__quote">
        <svg class="amb-pop-demo__stars" viewBox="0 0 120 24" width="100" height="20" role="img" aria-label="5 out of 5 stars" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9zm24 0 2.7 5.6 6.1.9-4.4 4.3 1 6.1L36 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9zm24 0 2.7 5.6 6.1.9-4.4 4.3 1 6.1L60 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9zm24 0 2.7 5.6 6.1.9-4.4 4.3 1 6.1L84 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9zm24 0 2.7 5.6 6.1.9-4.4 4.3 1 6.1-5.4-2.9-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
        <blockquote><p>"Our boiler died on a Sunday. They were here in forty minutes and had the heat back on by lunch."</p></blockquote>
        <figcaption><span class="amb-pop-demo__avatar" aria-hidden="true">MR</span><span><strong>Maria R.</strong> Westlake</span></figcaption>
      </figure>
    </div>
  </section>

  <section class="amb-pop-demo__section" id="amb-pop-book" aria-labelledby="amb-pop-cta-title">
    <div class="amb-pop" aria-hidden="true">
      <span class="amb-pop__shape amb-pop__shape--sphere" style="--amb-pop-x: 8; --amb-pop-y: 30; --amb-pop-mx: 3; --amb-pop-my: 5; --amb-pop-size: 5; --amb-pop-depth: 0.8; --amb-pop-c: var(--primary); --amb-pop-i: 0"></span>
      <span class="amb-pop__shape amb-pop__shape--pill" style="--amb-pop-x: 92; --amb-pop-y: 26; --amb-pop-mx: 97; --amb-pop-my: 6; --amb-pop-size: 5.5; --amb-pop-depth: 1; --amb-pop-r: -20deg; --amb-pop-c: var(--accent); --amb-pop-i: 1"></span>
      <span class="amb-pop__shape amb-pop__shape--ring" style="--amb-pop-x: 90; --amb-pop-y: 82; --amb-pop-mx: 97; --amb-pop-my: 95; --amb-pop-size: 4.5; --amb-pop-depth: 0.6; --amb-pop-c: var(--primary-2); --amb-pop-i: 2"></span>
      <span class="amb-pop__shape amb-pop__shape--cube amb-pop__shape--wide" style="--amb-pop-x: 12; --amb-pop-y: 78; --amb-pop-size: 3.4; --amb-pop-depth: 1.2; --amb-pop-r: 30deg; --amb-pop-c: var(--primary); --amb-pop-i: 3"></span>
      <span class="amb-pop__shape amb-pop__shape--star amb-pop__shape--wide" style="--amb-pop-x: 84; --amb-pop-y: 10; --amb-pop-size: 2.4; --amb-pop-depth: 1.4; --amb-pop-r: -12deg; --amb-pop-c: var(--accent); --amb-pop-i: 4"></span>
    </div>
    <div class="amb-pop-demo__inner">
      <div class="amb-pop-demo__panel">
        <p class="amb-pop-demo__eyebrow">Book a visit</p>
        <h2 id="amb-pop-cta-title" class="amb-pop-demo__h2">Ready when you are.</h2>
        <p class="amb-pop-demo__intro">Book online in under a minute, or call and talk to a real person in Springfield.</p>
        <div class="amb-pop-demo__actions">
          <a class="amb-pop-demo__btn amb-pop-demo__btn--primary" href="#amb-pop-book">
            Book online
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
          <a class="amb-pop-demo__btn" href="tel:+15555550123">(555) 555-0123</a>
        </div>
        <p class="amb-pop-demo__small">Mon–Sat, 7am–8pm · <a href="mailto:hello@example.com">hello@example.com</a></p>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Layer: decorative, first child of a relative + isolated section, behind its content */
.amb-pop {
  --amb-pop-k: 0.62;       /* shape scale: phones */
  --amb-pop-travel: 0.22;  /* parallax strength: phones */
  position: absolute; inset: 0; z-index: -1; overflow: clip; pointer-events: none;
}
.amb-pop--page { position: fixed; }
/* Contrast guard: --amb-pop-scrim (0–1) fades a surface-coloured veil over the shapes */
.amb-pop::after { content: ""; position: absolute; inset: 0; background: color-mix(in srgb, var(--surface-light) calc(var(--amb-pop-scrim, 0) * 100%), transparent); }

/* Shapes: placed by custom properties, sized in em so every highlight and shadow scales with them */
.amb-pop__shape {
  position: absolute; width: 1em; height: 1em;
  left: calc(var(--amb-pop-mx, var(--amb-pop-x)) * 1%);
  top: calc(var(--amb-pop-my, var(--amb-pop-y)) * 1%);
  font-size: calc(var(--amb-pop-size) * var(--amb-pop-k) * 1rem);
  translate: -50% calc(-50% + var(--amb-pop-shift, 0px) * var(--amb-pop-depth) * var(--amb-pop-travel));
  rotate: calc(var(--amb-pop-r, 0deg) + var(--amb-pop-tilt, 0deg) * var(--amb-pop-depth));
}
.amb-pop__shape--wide { display: none; }

.amb-pop__shape--sphere {
  border-radius: 50%;
  background:
    radial-gradient(circle at 32% 27%, color-mix(in srgb, var(--surface-light) 95%, transparent) 0 6%, transparent 25%),
    radial-gradient(circle at 36% 34%, color-mix(in srgb, var(--amb-pop-c) 30%, var(--surface-light)), var(--amb-pop-c) 58%, color-mix(in srgb, var(--amb-pop-c) 72%, var(--text-main)));
  box-shadow: inset -0.06em -0.1em 0.2em color-mix(in srgb, var(--text-main) 20%, transparent),
    0 0.32em 0.5em -0.28em color-mix(in srgb, var(--amb-pop-c) 60%, transparent);
}
.amb-pop__shape--pill {
  height: 0.42em; border-radius: var(--radius-full);
  background:
    radial-gradient(42% 30% at 30% 26%, color-mix(in srgb, var(--surface-light) 90%, transparent), transparent),
    linear-gradient(180deg, color-mix(in srgb, var(--amb-pop-c) 40%, var(--surface-light)), var(--amb-pop-c) 55%, color-mix(in srgb, var(--amb-pop-c) 75%, var(--text-main)));
  box-shadow: inset 0 -0.05em 0.08em color-mix(in srgb, var(--text-main) 18%, transparent),
    0 0.24em 0.36em -0.2em color-mix(in srgb, var(--amb-pop-c) 60%, transparent);
}
.amb-pop__shape--ring {
  border-radius: 50%;
  background: conic-gradient(from 200deg, var(--amb-pop-c), var(--primary-2), var(--accent), color-mix(in srgb, var(--primary) 55%, var(--surface-light)), var(--amb-pop-c));
  -webkit-mask: radial-gradient(farthest-side, transparent 57%, black 60% 96%, transparent);
  mask: radial-gradient(farthest-side, transparent 57%, black 60% 96%, transparent);
}
.amb-pop__shape--ring::before { /* specular glint, clipped to the ring by the mask */
  content: ""; position: absolute; inset: 0; border-radius: 50%;
  background: radial-gradient(circle at 26% 22%, color-mix(in srgb, var(--surface-light) 90%, transparent) 0 7%, transparent 20%);
}
.amb-pop__shape--cube {
  border-radius: 28%;
  background:
    radial-gradient(70% 55% at 30% 20%, color-mix(in srgb, var(--surface-light) 75%, transparent), transparent 62%),
    linear-gradient(145deg, color-mix(in srgb, var(--amb-pop-c) 45%, var(--surface-light)), var(--amb-pop-c) 55%, color-mix(in srgb, var(--amb-pop-c) 70%, var(--text-main)));
  box-shadow: inset 0.05em 0.07em 0.08em color-mix(in srgb, var(--surface-light) 65%, transparent),
    inset -0.06em -0.09em 0.14em color-mix(in srgb, var(--text-main) 22%, transparent),
    0 0.3em 0.5em -0.26em color-mix(in srgb, var(--amb-pop-c) 60%, transparent);
}
.amb-pop__shape--star {
  clip-path: polygon(50% 0, 62% 34%, 98% 35%, 69% 57%, 79% 92%, 50% 71%, 21% 92%, 31% 57%, 2% 35%, 38% 34%);
  background:
    radial-gradient(circle at 42% 34%, color-mix(in srgb, var(--surface-light) 85%, transparent) 0 9%, transparent 32%),
    linear-gradient(160deg, color-mix(in srgb, var(--amb-pop-c) 45%, var(--surface-light)), var(--amb-pop-c) 60%, color-mix(in srgb, var(--amb-pop-c) 70%, var(--text-main)));
}

/* Pop-in: hidden from first paint only when JS will run; a failsafe pops them if it never does */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .amb-pop__shape { visibility: hidden; scale: 0; }
  .amb-pop:not(.amb-pop--js) .amb-pop__shape { animation: amb-pop-in var(--dur-5) var(--ease-out) 2.5s both; }
  .amb-pop.is-in .amb-pop__shape { animation: amb-pop-in var(--dur-5) var(--ease-out) calc(var(--amb-pop-i, 0) * var(--stagger) * 1.5) both; }
}
@keyframes amb-pop-in {
  0% { visibility: visible; scale: 0; transform: rotate(-35deg); }
  55% { scale: 1.16; transform: rotate(7deg); }
  78% { scale: 0.95; transform: rotate(-2deg); }
  100% { visibility: visible; scale: 1; transform: none; }
}

@media (min-width: 768px) {
  .amb-pop { --amb-pop-k: 0.8; --amb-pop-travel: 1; }
  .amb-pop__shape { left: calc(var(--amb-pop-x) * 1%); top: calc(var(--amb-pop-y) * 1%); }
  .amb-pop__shape--wide { display: block; }
}
@media (min-width: 1200px) { .amb-pop { --amb-pop-k: 1; } }

/* ---- Demo page (light) ---- */
.amb-pop-demo {
  overflow-x: clip; color: var(--text-main); font-family: var(--font-sans);
  --amb-pop-demo-soft: color-mix(in srgb, var(--text-main) 80%, var(--surface-light));
  background:
    radial-gradient(56rem 36rem at 88% 0%, color-mix(in srgb, var(--primary) 7%, transparent), transparent 70%),
    radial-gradient(48rem 40rem at 0% 42%, color-mix(in srgb, var(--accent) 8%, transparent), transparent 70%),
    radial-gradient(48rem 40rem at 100% 88%, color-mix(in srgb, var(--primary-2) 7%, transparent), transparent 70%),
    var(--surface-light);
}
.amb-pop-demo__section { position: relative; isolation: isolate; padding-block: clamp(5rem, 10vw, 7.5rem); }
.amb-pop-demo__section--hero { display: grid; align-items: center; min-height: 88vh; min-height: 88svh; text-align: center; }
.amb-pop-demo__inner { width: 100%; max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); box-sizing: border-box; }

.amb-pop-demo__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.875rem; border-radius: var(--radius-full);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.amb-pop-demo__dot { width: 0.5rem; height: 0.5rem; border-radius: 50%; background: radial-gradient(circle at 35% 30%, var(--surface-light), var(--accent) 60%); }
.amb-pop-demo__title {
  max-width: 13ch; margin: 1.25rem auto 0; font: 600 clamp(2.5rem, 1.2rem + 5.4vw, 5.25rem)/1 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.amb-pop-demo__title em {
  font-style: normal; background: linear-gradient(100deg, var(--primary), color-mix(in srgb, var(--primary-2) 80%, var(--text-main)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.amb-pop-demo__lead { max-width: 34rem; margin: 1.25rem auto 0; color: var(--amb-pop-demo-soft); font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; }
.amb-pop-demo__actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 0.75rem; margin-top: 2rem; }
.amb-pop-demo__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-md);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-pop-demo__btn:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-lg); }
.amb-pop-demo__btn:active { transform: scale(0.97); }
.amb-pop-demo__btn--primary { background: var(--text-main); color: var(--surface-light); box-shadow: var(--highlight-inverse), 0 14px 30px -14px color-mix(in srgb, var(--primary) 85%, transparent); }
.amb-pop-demo__btn--primary:hover { box-shadow: var(--highlight-inverse), 0 18px 36px -14px color-mix(in srgb, var(--primary) 95%, transparent); }
.amb-pop-demo svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.amb-pop-demo :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.amb-pop-demo__hint {
  display: flex; flex-direction: column; align-items: center; gap: 0.375rem; margin: 3.5rem 0 0; color: var(--amb-pop-demo-soft);
  font: 500 0.6875rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.amb-pop-demo__hint svg { animation: amb-pop-nudge 1.4s var(--ease-in-out) 3; } /* three nudges, then still */

/* Section heads */
.amb-pop-demo__head { max-width: 38rem; margin: 0 auto 3rem; text-align: center; }
.amb-pop-demo__h2 { margin: 1rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.8vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.amb-pop-demo__intro { max-width: 32rem; margin: 1rem auto 0; color: var(--amb-pop-demo-soft); font-size: 1.0625rem; line-height: 1.6; }

/* Service cards: opaque, so shapes peek out from behind them */
.amb-pop-demo__grid { display: grid; gap: 1rem; margin: 0; padding: 0; list-style: none; }
.amb-pop-demo__card {
  position: relative; display: flex; flex-direction: column; gap: 0.5rem; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: linear-gradient(180deg, var(--surface-light) 60%, var(--surface-muted));
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-lg);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.amb-pop-demo__card:hover { transform: translateY(-4px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl); }
.amb-pop-demo__card h3 { margin: 0.75rem 0 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-pop-demo__card p { margin: 0; color: var(--amb-pop-demo-soft); line-height: 1.55; }
.amb-pop-demo__icon {
  display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 0.875rem; color: var(--surface-light);
  background:
    radial-gradient(circle at 30% 22%, color-mix(in srgb, var(--surface-light) 55%, transparent), transparent 45%),
    linear-gradient(145deg, color-mix(in srgb, var(--amb-pop-c) 70%, var(--surface-light)), var(--amb-pop-c) 60%, color-mix(in srgb, var(--amb-pop-c) 75%, var(--text-main)));
  box-shadow: inset 0 -0.15rem 0.3rem color-mix(in srgb, var(--text-main) 18%, transparent), 0 10px 18px -10px var(--amb-pop-c);
}
.amb-pop-demo__link { color: inherit; text-decoration: none; }
.amb-pop-demo__link::after { content: ""; position: absolute; inset: 0; border-radius: inherit; }
.amb-pop-demo .amb-pop-demo__link:focus-visible { outline: none; }
.amb-pop-demo__link:focus-visible::after { outline: 2px solid var(--primary); outline-offset: 3px; }
.amb-pop-demo__card .amb-pop-demo__price {
  display: flex; align-items: baseline; gap: 0.375rem; margin-top: auto; padding-top: 1rem; border-top: 1px solid var(--border-subtle);
  font: 500 0.8125rem var(--font-mono);
}
.amb-pop-demo__price strong { color: var(--text-main); font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.amb-pop-demo__go { display: inline-flex; align-items: center; gap: 0.25rem; margin-left: auto; color: var(--primary); font: 600 0.875rem var(--font-sans); }
.amb-pop-demo__go svg { transition: transform var(--dur-3) var(--ease-spring); }
.amb-pop-demo__card:hover .amb-pop-demo__go svg { transform: translateX(3px); }

/* Proof */
.amb-pop-demo__stats { display: grid; gap: 1rem; max-width: 56rem; margin: 0 auto; }
.amb-pop-demo__stats div {
  display: flex; flex-direction: column-reverse; gap: 0.375rem; padding: 1.25rem 1.5rem; border-radius: var(--radius-2xl); text-align: center;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md);
}
.amb-pop-demo__stats dt { color: var(--amb-pop-demo-soft); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.amb-pop-demo__stats dd { margin: 0; font: 600 clamp(2.25rem, 1.8rem + 1.6vw, 3rem)/1 var(--font-display); letter-spacing: var(--tracking-display); }
.amb-pop-demo__stats small { margin-left: 0.125rem; color: var(--primary); font-size: 0.45em; letter-spacing: 0; }
.amb-pop-demo__quote {
  display: grid; justify-items: center; gap: 1rem; max-width: 40rem; margin: 2rem auto 0; padding: 2rem 1.5rem; border-radius: var(--radius-2xl); text-align: center;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.amb-pop-demo__stars path { fill: var(--accent); stroke: none; }
.amb-pop-demo__quote blockquote { margin: 0; }
.amb-pop-demo__quote blockquote p { margin: 0; font: 500 clamp(1.125rem, 1rem + 0.6vw, 1.375rem)/1.45 var(--font-display); letter-spacing: -0.01em; text-wrap: balance; }
.amb-pop-demo__quote figcaption { display: flex; align-items: center; gap: 0.75rem; color: var(--amb-pop-demo-soft); font-size: 0.875rem; text-align: left; }
.amb-pop-demo__quote figcaption strong { display: block; color: var(--text-main); }
.amb-pop-demo__avatar { display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%; background: var(--gradient-brand); color: var(--text-inverse); font: 700 0.75rem var(--font-sans); }

/* CTA panel */
.amb-pop-demo__panel {
  max-width: 44rem; margin-inline: auto; padding: clamp(2rem, 6vw, 3.5rem) clamp(1.25rem, 5vw, 3rem); border-radius: var(--radius-2xl); text-align: center;
  background:
    radial-gradient(80% 60% at 50% 0%, color-mix(in srgb, var(--primary) 8%, transparent), transparent 70%),
    var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.amb-pop-demo__small { margin: 1.5rem 0 0; color: var(--amb-pop-demo-soft); font: 500 0.8125rem var(--font-mono); }
.amb-pop-demo__small a { color: var(--primary); }

@media (min-width: 600px) {
  .amb-pop-demo__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .amb-pop-demo__stats { grid-template-columns: repeat(3, minmax(0, 1fr)); }
}
@media (min-width: 1024px) { .amb-pop-demo__grid { grid-template-columns: repeat(4, minmax(0, 1fr)); } }

@media (prefers-reduced-motion: reduce) {
  .amb-pop__shape { animation: none !important; translate: -50% -50%; rotate: var(--amb-pop-r, 0deg); }
  .amb-pop-demo__hint svg { animation: none; }
}
@keyframes amb-pop-nudge { 50% { transform: translateY(5px); } }
```

## JS

```js
// Pop Shapes: one shared, self-stopping rAF loop drives every .amb-pop layer on the page
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const layers = new Map([...document.querySelectorAll('.amb-pop')].map((el) => [el, {
  on: false, top: 0, h: 0, cur: 0, page: el.classList.contains('amb-pop--page'),
}]));

if (layers.size) {
  const clamp = (v, m) => Math.max(-m, Math.min(m, v));
  let raf = 0, lastY = scrollY, lastT = 0, tilt = 0, spin = 0, vh = innerHeight, maxScroll = 1;

  // Geometry is cached on resize, so the frame loop itself never reads layout
  const measure = () => {
    vh = innerHeight;
    maxScroll = Math.max(1, document.documentElement.scrollHeight - vh);
    layers.forEach((s, el) => { const r = el.getBoundingClientRect(); s.top = r.top + scrollY; s.h = r.height; });
  };

  const tick = (t) => {
    const dt = lastT ? Math.min(64, t - lastT) : 16.7;
    const y = scrollY;
    const v = (y - lastY) / dt; // px per ms
    lastT = t;
    lastY = y;
    // Tilt chases scroll speed on a damped spring, so it wobbles back to 0 when scrolling stops
    spin = (spin + (clamp(v * 9, 14) - tilt) * 0.1) * 0.78;
    tilt += spin;
    const ease = 1 - 0.88 ** (dt / 16.7);
    let moving = Math.abs(tilt) + Math.abs(spin) > 0.04;
    layers.forEach((s, el) => {
      if (!s.on) return;
      // Section centre vs viewport centre; the page-wide layer uses whole-page progress instead
      const off = s.page ? (y / maxScroll - 0.5) * vh : s.top - y + (s.h - vh) / 2;
      const target = clamp(off * -0.18, 150);
      s.cur += (target - s.cur) * ease;
      if (Math.abs(target - s.cur) > 0.15) moving = true;
      el.style.setProperty('--amb-pop-shift', `${s.cur.toFixed(2)}px`);
      el.style.setProperty('--amb-pop-tilt', `${tilt.toFixed(2)}deg`);
    });
    raf = moving ? requestAnimationFrame(tick) : 0;
  };

  // Run only while a layer is on screen, the tab is visible and motion is allowed
  const wake = () => {
    if (raf || reduce.matches || document.visibilityState === 'hidden') return;
    for (const s of layers.values()) {
      if (!s.on) continue;
      lastY = scrollY;
      lastT = 0;
      raf = requestAnimationFrame(tick);
      return;
    }
  };

  // Pop in once a little of the section shows; reset when it leaves, so the next visit pops again
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      layers.get(e.target).on = e.isIntersecting;
      if (e.intersectionRatio >= 0.12) e.target.classList.add('is-in');
      else if (!e.isIntersecting) e.target.classList.remove('is-in');
    });
    wake();
  }, { threshold: [0, 0.12] });

  measure();
  layers.forEach((s, el) => { el.classList.add('amb-pop--js'); io.observe(el); });
  new ResizeObserver(() => { measure(); wake(); }).observe(document.documentElement);
  addEventListener('resize', measure, { passive: true });
  addEventListener('scroll', wake, { passive: true });
  document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'hidden') { cancelAnimationFrame(raf); raf = 0; } else wake();
  });
}
```

## Notes

- **Layer contract:** each `.amb-pop` is decorative (`aria-hidden="true"`, `pointer-events: none`) and is the first child of a `position: relative; isolation: isolate` section, at `z-index: -1` behind that section's content. Give every section its own layer: its shapes belong to it and pop when it arrives. `.amb-pop--page` instead fixes one layer behind the whole page (sections need transparent backgrounds); its shapes pop once on load and drift with whole-page scroll progress. Use one ambient background style per page.
- **Performance:** one shared rAF loop for every layer. It runs only while a layer intersects the viewport, the tab is visible and something is still moving; drift and tilt settle within about a second, then it stops until the next scroll. No layout reads per frame (offsets are cached on resize via `ResizeObserver`), no blur and no `will-change`: each frame writes two custom properties per visible layer, which move `translate` and `rotate` only. The demo has 23 shapes on desktop and 13 on phones.
- **Contrast:** body copy never sits on a shape. Shapes stay in the side margins on desktop, and in the screen edges of the top/bottom padding bands on phones; elsewhere they hide behind opaque cards. Worst case under copy is the stacked tint wash: the soft body colour (`--text-main` 80% with `--surface-light`) reaches 6.1:1 there, and the gradient headline 3.9:1 (large text). If your layout puts copy over shapes, set `--amb-pop-scrim: 0.7` on the layer or any ancestor: the soft body colour over the darkest shape tone becomes 4.7:1.
- **No JS and reduced motion:** with scripting off, the shapes are simply there. With JS, they're hidden from first paint by `@media (scripting: enabled)`, and a 2.5s CSS failsafe pops them in if the script never runs. Under reduced motion the layer is a still composition: no pop, parallax or tilt, and the scroll hint skips its three nudges.
- **Support:** individual transform properties (`translate`, `rotate`, `scale`), `color-mix()` and `@media (scripting)` (browsers without it show the shapes statically, without the pop). The loop listens to window scroll.
- **Adapting:** add `.amb-pop__shape--{sphere|pill|ring|cube|star}` spans with `--amb-pop-x`/`--amb-pop-y` (% of the section) and optional phone positions `--amb-pop-mx`/`--amb-pop-my`. Set `--amb-pop-size` (rem), `--amb-pop-depth` (negative drifts the other way), `--amb-pop-r` (base angle), `--amb-pop-c` (any colour token) and `--amb-pop-i` (stagger step). Add `--wide` to keep a shape off phones.
