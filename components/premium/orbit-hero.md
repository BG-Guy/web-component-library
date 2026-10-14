# Orbit Hero

A deep, split hero: "Every trade. One call." on the left, and on the right a glowing brand mark with tilted elliptical orbits around it. Six service planets travel the rings in real 3D, so they pass in front of and behind the core and the dashed rings, while a gradient comet runs each ring. Hover or focus a planet and its ring stops, the planet swells and lifts to the front, and a label card shows the offer ("Same-day leak repair · from $89"). On phones the orbit sits below the copy and drops its outer ring. Depends on `tokens/variables.css`.

**Motion:** copy rises line by line (`--dur-5`, `--ease-out`, `--stagger`) · core blooms in, rings expand, planets pop in sequence (`--ease-spring`) · planets orbit with counter-rotation that keeps their icons upright (linear loops, 32–48s, the middle ring runs the other way) · comets circle each ring · the halo breathes (`--ease-in-out`) · hover/focus swell and label card (`--ease-spring`). A pause button stops every loop; they also freeze off-screen.

## HTML

```html
<section class="orbit-hero" aria-labelledby="orbit-hero-title" data-orbit-hero>
  <div class="orbit-hero__inner">
    <div class="orbit-hero__copy">
      <p class="orbit-hero__eyebrow" style="--orbit-hero-i: 0"><span class="orbit-hero__eyebrow-dot" aria-hidden="true"></span>6 trades · 1 licensed team</p>
      <h1 id="orbit-hero-title" class="orbit-hero__title">
        <span class="orbit-hero__line" style="--orbit-hero-i: 1">Every trade.</span>
        <span class="orbit-hero__line orbit-hero__grad" style="--orbit-hero-i: 2">One call.</span>
      </h1>
      <p class="orbit-hero__lead" style="--orbit-hero-i: 3">Plumbing, electrical, HVAC, roofing, solar and locks, handled by one Springfield crew with one schedule and one upfront invoice.</p>
      <div class="orbit-hero__actions" style="--orbit-hero-i: 4">
        <a class="orbit-hero__btn orbit-hero__btn--primary" href="#book">
          Book any service
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="orbit-hero__btn orbit-hero__btn--glass" href="tel:+15555550123">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          (555) 555-0123
        </a>
      </div>
      <div class="orbit-hero__proof" style="--orbit-hero-i: 5">
        <span class="orbit-hero__faces" aria-hidden="true"><span>JM</span><span>AK</span><span>RS</span></span>
        <p><strong>4.9/5</strong> from 2,300 Springfield reviews<span>Licensed &amp; insured · 1-year guarantee</span></p>
      </div>
    </div>

    <div class="orbit-hero__stage">
      <div class="orbit-hero__system">
        <div class="orbit-hero__orbit orbit-hero__orbit--c" aria-hidden="true">
          <svg viewBox="0 0 100 100" focusable="false"><circle cx="50" cy="50" r="49.5" pathLength="100" /></svg>
          <span class="orbit-hero__comet"></span>
        </div>
        <div class="orbit-hero__orbit orbit-hero__orbit--b" aria-hidden="true">
          <svg viewBox="0 0 100 100" focusable="false"><circle cx="50" cy="50" r="49.5" pathLength="100" /></svg>
          <span class="orbit-hero__comet"></span>
        </div>
        <div class="orbit-hero__orbit orbit-hero__orbit--a" aria-hidden="true">
          <svg viewBox="0 0 100 100" focusable="false"><circle cx="50" cy="50" r="49.5" pathLength="100" /></svg>
          <span class="orbit-hero__comet"></span>
        </div>

        <div class="orbit-hero__core" aria-hidden="true">
          <span class="orbit-hero__halo"></span>
          <span class="orbit-hero__mark">
            <svg viewBox="0 0 24 24" width="40" height="40" focusable="false"><path d="M3 11 12 4l9 7M5 10v10h14V10M9.5 15l2 2 3.5-4" /></svg>
          </span>
        </div>

        <ul class="orbit-hero__planets" role="list" aria-label="Services">
          <li class="orbit-hero__item orbit-hero__item--a" style="--orbit-hero-phase: 10deg; --orbit-hero-i: 0; --orbit-hero-tint: var(--primary)">
            <a class="orbit-hero__planet" href="#plumbing">
              <span class="orbit-hero__disc"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 3s6 6.2 6 11a6 6 0 0 1-12 0c0-4.8 6-11 6-11z" /></svg></span>
              <span class="orbit-hero__label"><strong>Plumbing</strong><span>Same-day leak repair · from $89</span></span>
            </a>
          </li>
          <li class="orbit-hero__item orbit-hero__item--a" style="--orbit-hero-phase: 130deg; --orbit-hero-i: 1; --orbit-hero-tint: var(--accent)">
            <a class="orbit-hero__planet" href="#electrical">
              <span class="orbit-hero__disc"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg></span>
              <span class="orbit-hero__label"><strong>Electrical</strong><span>Panel and outlet fixes · from $99</span></span>
            </a>
          </li>
          <li class="orbit-hero__item orbit-hero__item--a" style="--orbit-hero-phase: 250deg; --orbit-hero-i: 2; --orbit-hero-tint: var(--primary-2)">
            <a class="orbit-hero__planet" href="#hvac">
              <span class="orbit-hero__disc"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 12c0-3 1-6 4-6s3 3 0 4.5M12 12c3 0 6 1 6 4s-3 3-4.5 0M12 12c0 3-1 6-4 6s-3-3 0-4.5M12 12c-3 0-6-1-6-4s3-3 4.5 0" /></svg></span>
              <span class="orbit-hero__label"><strong>HVAC</strong><span>AC and furnace tune-ups · from $79</span></span>
            </a>
          </li>
          <li class="orbit-hero__item orbit-hero__item--b" style="--orbit-hero-phase: 70deg; --orbit-hero-i: 3; --orbit-hero-tint: var(--primary-2)">
            <a class="orbit-hero__planet" href="#roofing">
              <span class="orbit-hero__disc"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M3 11 12 4l9 7M5 10v10h14V10M10 20v-6h4v6" /></svg></span>
              <span class="orbit-hero__label"><strong>Roofing</strong><span>Leak patch within 48h · from $249</span></span>
            </a>
          </li>
          <li class="orbit-hero__item orbit-hero__item--b" style="--orbit-hero-phase: 190deg; --orbit-hero-i: 4; --orbit-hero-tint: var(--accent)">
            <a class="orbit-hero__planet" href="#solar">
              <span class="orbit-hero__disc"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" /></svg></span>
              <span class="orbit-hero__label"><strong>Solar</strong><span>Free roof assessment · $0</span></span>
            </a>
          </li>
          <li class="orbit-hero__item orbit-hero__item--b" style="--orbit-hero-phase: 310deg; --orbit-hero-i: 5; --orbit-hero-tint: var(--primary)">
            <a class="orbit-hero__planet" href="#locks">
              <span class="orbit-hero__disc"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M7 11h10a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1v-8a1 1 0 0 1 1-1zM8 11V7a4 4 0 0 1 8 0v4" /></svg></span>
              <span class="orbit-hero__label"><strong>Locks</strong><span>Lockouts in 30 min · from $69</span></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>

  <button class="orbit-hero__pause" type="button" aria-pressed="false" aria-label="Pause animation" hidden>
    <svg class="orbit-hero__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
    <svg class="orbit-hero__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
  </button>
</section>
```

## CSS

```css
/* Section: deep space, a faint star field and a pool of brand light behind the orbit */
.orbit-hero {
  --orbit-hero-size: min(18rem, calc(100vw - 2 * var(--gutter)));
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(36rem 30rem at 50% 78%, color-mix(in srgb, var(--primary) 20%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.orbit-hero::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background-image:
    radial-gradient(color-mix(in srgb, var(--text-inverse) 40%, transparent) 1px, transparent 1.5px),
    radial-gradient(color-mix(in srgb, var(--text-inverse) 22%, transparent) 1px, transparent 1.5px);
  background-size: 97px 89px, 53px 61px;
  background-position: 13px 29px, 31px 7px;
  -webkit-mask-image: radial-gradient(ellipse 70% 70% at 60% 55%, black, transparent);
  mask-image: radial-gradient(ellipse 70% 70% at 60% 55%, black, transparent);
}
.orbit-hero__inner {
  display: grid; gap: 1.5rem; align-items: center;
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4.5rem, 11vw, 7rem) var(--gutter) clamp(4rem, 9vw, 6rem);
}

/* Copy: rises line by line */
.orbit-hero__eyebrow, .orbit-hero__line, .orbit-hero__lead, .orbit-hero__actions, .orbit-hero__proof {
  animation: orbit-hero-rise var(--dur-5) var(--ease-out) calc(120ms + var(--orbit-hero-i) * var(--stagger) * 2) backwards;
}
.orbit-hero__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.875rem 0.375rem 0.625rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse-muted); font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.orbit-hero__eyebrow-dot { width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--gradient-brand); box-shadow: 0 0 10px var(--primary-2); }
.orbit-hero__title { margin: 1.5rem 0 0; font: 600 clamp(2.625rem, 1.3rem + 5.6vw, 5.75rem)/0.98 var(--font-display); letter-spacing: var(--tracking-display); }
.orbit-hero__line { display: block; }
.orbit-hero__grad {
  width: fit-content; padding-bottom: 0.06em;
  background: linear-gradient(95deg, color-mix(in srgb, var(--primary) 45%, var(--text-inverse)), color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.orbit-hero__lead { max-width: 32rem; margin: 1.5rem 0 0; color: var(--text-inverse-muted); font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; text-wrap: pretty; }

/* CTAs */
.orbit-hero__actions { display: grid; gap: 0.75rem; margin-top: 2.25rem; }
.orbit-hero__btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.5rem;
  border-radius: var(--radius-full); font: 600 0.9375rem/1 var(--font-sans); text-decoration: none;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out), background-color var(--dur-2);
}
.orbit-hero__btn svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.orbit-hero__btn:hover { transform: translateY(-2px); }
.orbit-hero__btn:active { transform: scale(0.97); }
.orbit-hero__btn--primary { background: var(--surface-light); color: var(--text-main); box-shadow: var(--highlight), 0 12px 40px -12px color-mix(in srgb, var(--primary) 90%, transparent); }
.orbit-hero__btn--primary:hover { box-shadow: var(--highlight), 0 16px 48px -10px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.orbit-hero__btn--primary:hover svg { transform: translateX(3px); }
.orbit-hero__btn--glass { background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); }
.orbit-hero__btn--glass:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.orbit-hero :is(.orbit-hero__btn, .orbit-hero__pause):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Proof */
.orbit-hero__proof { display: flex; align-items: center; gap: 0.875rem; margin-top: 2rem; color: var(--text-inverse-muted); font-size: 0.875rem; line-height: 1.45; }
.orbit-hero__proof p { margin: 0; }
.orbit-hero__proof strong { color: var(--text-inverse); }
.orbit-hero__proof p span { display: block; font-size: 0.8125rem; }
.orbit-hero__faces { display: flex; flex: none; }
.orbit-hero__faces span {
  display: grid; place-items: center; width: 2rem; height: 2rem; margin-left: -0.5rem; border: 2px solid var(--surface-deep); border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-size: 0.6875rem; font-weight: 700;
}
.orbit-hero__faces span:first-child { margin-left: 0; }
.orbit-hero__faces span:nth-child(2) { background: linear-gradient(135deg, var(--primary-2), color-mix(in srgb, var(--primary-2) 50%, var(--surface-deep))); }
.orbit-hero__faces span:nth-child(3) { background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 50%, var(--primary))); color: var(--text-main); }

/* The system: one orthographic 3D context, so planets and rings sort in front of and behind the core */
.orbit-hero__stage { display: grid; place-items: center; padding-block: 3rem 2rem; }
.orbit-hero__system { position: relative; width: var(--orbit-hero-size); aspect-ratio: 1; transform-style: preserve-3d; }

/* Ring geometry, shared by each drawn ring and the planets that ride it */
.orbit-hero__orbit--a, .orbit-hero__item--a { --orbit-hero-r: calc(var(--orbit-hero-size) * 0.3); --orbit-hero-tilt: -18deg; --orbit-hero-lean: 68deg; --orbit-hero-speed: 32s; }
.orbit-hero__orbit--b, .orbit-hero__item--b { --orbit-hero-r: calc(var(--orbit-hero-size) * 0.43); --orbit-hero-tilt: 14deg; --orbit-hero-lean: 64deg; --orbit-hero-speed: 48s; }
.orbit-hero__orbit--c { --orbit-hero-r: calc(var(--orbit-hero-size) * 0.5); --orbit-hero-tilt: -6deg; --orbit-hero-lean: 76deg; }

/* Rings: a dashed SVG circle seen at an angle (an ellipse) plus a comet running round it */
.orbit-hero__orbit {
  position: absolute; left: 50%; top: 50%; width: calc(var(--orbit-hero-r) * 2); aspect-ratio: 1; pointer-events: none;
  transform: translate(-50%, -50%) rotateZ(var(--orbit-hero-tilt)) rotateX(var(--orbit-hero-lean));
  animation: orbit-hero-ring calc(var(--dur-5) * 1.4) var(--ease-out) 250ms backwards;
}
.orbit-hero__orbit--b { animation-delay: 350ms; }
.orbit-hero__orbit--c { display: none; animation-delay: 450ms; }
.orbit-hero__orbit svg { position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible; fill: none; stroke: color-mix(in srgb, var(--text-inverse) 28%, transparent); stroke-width: 0.55; stroke-dasharray: 0.7 1.3; }
.orbit-hero__comet {
  --orbit-hero-comet: conic-gradient(transparent 0 58%, color-mix(in srgb, var(--primary) 60%, transparent) 86%, color-mix(in srgb, var(--primary-2) 50%, var(--text-inverse)) 99.3%, transparent 99.5%);
  position: absolute; inset: 0; border-radius: 50%; background: var(--orbit-hero-comet);
  -webkit-mask-image: radial-gradient(farthest-side, transparent calc(100% - 7px), black calc(100% - 2px), black calc(100% - 0.5px), transparent);
  mask-image: radial-gradient(farthest-side, transparent calc(100% - 7px), black calc(100% - 2px), black calc(100% - 0.5px), transparent);
}
.orbit-hero__orbit--b .orbit-hero__comet { /* runs the other way, so the head sits at the other end */
  --orbit-hero-comet: conic-gradient(transparent 0 0.5%, color-mix(in srgb, var(--primary-2) 50%, var(--text-inverse)) 0.7%, color-mix(in srgb, var(--primary-2) 60%, transparent) 14%, transparent 42%);
}
.orbit-hero--live .orbit-hero__comet { animation: orbit-hero-spin 9s linear infinite; }
.orbit-hero--live .orbit-hero__orbit--b .orbit-hero__comet { animation-duration: 13s; animation-delay: -5s; }
.orbit-hero--live .orbit-hero__orbit--c .orbit-hero__comet { animation-duration: 21s; animation-delay: -11s; }

/* Core: the glowing brand mark; its halo breathes */
.orbit-hero__core {
  position: absolute; left: 50%; top: 50%; width: calc(var(--orbit-hero-size) * 0.24); aspect-ratio: 1; translate: -50% -50%; pointer-events: none;
  animation: orbit-hero-core var(--dur-5) var(--ease-out) 120ms backwards;
}
.orbit-hero__halo {
  position: absolute; inset: -110%; border-radius: 50%;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 42%, transparent), color-mix(in srgb, var(--primary-2) 14%, transparent) 55%, transparent);
}
.orbit-hero--live .orbit-hero__halo { animation: orbit-hero-breathe 6s var(--ease-in-out) infinite alternate; }
.orbit-hero__mark {
  position: absolute; inset: 0; display: grid; place-items: center; border-radius: 50%; color: var(--text-inverse);
  background: radial-gradient(circle at 35% 28%, color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)), var(--primary) 52%, color-mix(in srgb, var(--primary) 55%, var(--surface-deep)));
  box-shadow:
    inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 50%, transparent), inset 0 -10px 24px color-mix(in srgb, var(--surface-deep) 45%, transparent),
    0 0 0 1px color-mix(in srgb, var(--text-inverse) 18%, transparent), 0 0 0 10px color-mix(in srgb, var(--primary) 12%, transparent),
    0 0 48px color-mix(in srgb, var(--primary) 75%, transparent), 0 0 120px color-mix(in srgb, var(--primary-2) 45%, transparent);
}
.orbit-hero__mark svg { width: 46%; height: 46%; fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }

/* Planets: each <li> is an arm (ring transform + phase), each link counter-rotates so its net transform is a pure translation */
.orbit-hero__planets { position: absolute; inset: 0; margin: 0; padding: 0; list-style: none; transform-style: preserve-3d; pointer-events: none; }
.orbit-hero__item {
  position: absolute; left: 50%; top: 50%; width: 0; height: 0; transform-style: preserve-3d;
  transform: rotateZ(var(--orbit-hero-tilt)) rotateX(var(--orbit-hero-lean)) rotateZ(var(--orbit-hero-phase)) translateX(var(--orbit-hero-r));
}
.orbit-hero__planet {
  --orbit-hero-disc: 2.75rem;
  position: absolute; left: calc(var(--orbit-hero-disc) / -2); top: calc(var(--orbit-hero-disc) / -2);
  width: var(--orbit-hero-disc); height: var(--orbit-hero-disc); border-radius: 50%;
  color: var(--text-inverse); text-decoration: none; pointer-events: auto; outline: none;
  transform: rotateZ(calc(-1 * var(--orbit-hero-phase))) rotateX(calc(-1 * var(--orbit-hero-lean))) rotateZ(calc(-1 * var(--orbit-hero-tilt))) translateZ(var(--orbit-hero-lift, 0px));
}
.orbit-hero--live .orbit-hero__item { animation: orbit-hero-orbit var(--orbit-hero-speed) linear infinite; }
.orbit-hero--live .orbit-hero__planet { animation: orbit-hero-counter var(--orbit-hero-speed) linear infinite; }
.orbit-hero--live :is(.orbit-hero__item--b, .orbit-hero__item--b .orbit-hero__planet, .orbit-hero__orbit--b .orbit-hero__comet) { animation-direction: reverse; }

/* Hovering or focusing a planet stops its whole ring (the planet alone where :has() is missing) */
.orbit-hero__item:is(:hover, :focus-within), .orbit-hero__item:is(:hover, :focus-within) .orbit-hero__planet { animation-play-state: paused; }
.orbit-hero__system:has(.orbit-hero__item--a :is(:hover, :focus-visible)) :is(.orbit-hero__item--a, .orbit-hero__item--a .orbit-hero__planet, .orbit-hero__orbit--a .orbit-hero__comet),
.orbit-hero__system:has(.orbit-hero__item--b :is(:hover, :focus-visible)) :is(.orbit-hero__item--b, .orbit-hero__item--b .orbit-hero__planet, .orbit-hero__orbit--b .orbit-hero__comet) { animation-play-state: paused; }
.orbit-hero:is([data-paused], [data-offscreen]) :is(.orbit-hero__item, .orbit-hero__planet, .orbit-hero__comet, .orbit-hero__halo) { animation-play-state: paused; }

/* Glass disc, upright icon; on hover/focus it swells and lifts in front of the core */
.orbit-hero__disc {
  display: grid; place-items: center; width: 100%; height: 100%; border-radius: 50%;
  background:
    radial-gradient(circle at 32% 26%, color-mix(in srgb, var(--orbit-hero-tint) 55%, transparent), transparent 62%),
    color-mix(in srgb, var(--surface-deep) 72%, var(--orbit-hero-tint));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--orbit-hero-tint) 50%, var(--border-inverse)), var(--highlight-inverse), 0 10px 26px -10px color-mix(in srgb, var(--orbit-hero-tint) 80%, transparent);
  transition: scale var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
  animation: orbit-hero-pop var(--dur-4) var(--ease-spring) calc(700ms + var(--orbit-hero-i) * var(--stagger) * 1.5) backwards;
}
.orbit-hero__disc svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.orbit-hero__planet:is(:hover, :focus-visible) { --orbit-hero-lift: 30rem; }
.orbit-hero__planet:is(:hover, :focus-visible) .orbit-hero__disc {
  scale: 1.25;
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--orbit-hero-tint) 70%, var(--text-inverse)), var(--highlight-inverse), 0 0 0 4px color-mix(in srgb, var(--orbit-hero-tint) 30%, transparent), 0 14px 36px -8px color-mix(in srgb, var(--orbit-hero-tint) 90%, transparent);
}
.orbit-hero__planet:focus-visible .orbit-hero__disc { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Label card: part of the link's name, shown on hover/focus, nudged by JS to stay on screen */
.orbit-hero__label {
  position: absolute; left: 50%; bottom: calc(100% + 0.875rem);
  display: grid; gap: 0.125rem; width: max-content; max-width: 13rem; padding: 0.625rem 0.875rem; border-radius: var(--radius-lg);
  background: var(--surface-light); color: var(--text-main); box-shadow: var(--shadow-xl); text-align: left;
  font-size: 0.75rem; line-height: 1.4; pointer-events: none;
  opacity: 0; translate: calc(-50% + var(--orbit-hero-nudge, 0px)) 0.375rem; scale: 0.92; transform-origin: 50% 100%;
  transition: opacity var(--dur-2) var(--ease-out), translate var(--dur-3) var(--ease-spring), scale var(--dur-3) var(--ease-spring);
}
.orbit-hero__label strong { font: 600 0.875rem/1.2 var(--font-display); letter-spacing: -0.01em; }
.orbit-hero__label span { color: var(--text-muted); }
.orbit-hero__planet:is(:hover, :focus-visible) .orbit-hero__label { opacity: 1; translate: calc(-50% + var(--orbit-hero-nudge, 0px)) 0; scale: 1; pointer-events: auto; }
.orbit-hero.is-quiet .orbit-hero__label { opacity: 0; pointer-events: none; }

/* Pause control */
.orbit-hero__pause {
  position: absolute; right: var(--gutter); bottom: 1rem; display: grid; place-items: center;
  width: 2.5rem; height: 2.5rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse-muted); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: color var(--dur-2), background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.orbit-hero__pause:hover { color: var(--text-inverse); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.orbit-hero__pause:active { transform: scale(0.92); }
.orbit-hero__pause[hidden] { display: none; }
.orbit-hero__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.orbit-hero__icon-play, .orbit-hero__pause[aria-pressed="true"] .orbit-hero__icon-pause { display: none; }
.orbit-hero__pause[aria-pressed="true"] .orbit-hero__icon-play { display: block; }

@media (min-width: 768px) {
  .orbit-hero { --orbit-hero-size: 28rem; }
  .orbit-hero__actions { display: flex; flex-wrap: wrap; }
  .orbit-hero__orbit--c { display: block; }
  .orbit-hero__planet { --orbit-hero-disc: 3rem; }
}
@media (min-width: 1024px) {
  .orbit-hero { --orbit-hero-size: min(32rem, 42vw); background: radial-gradient(36rem 30rem at 76% 50%, color-mix(in srgb, var(--primary) 20%, transparent), transparent 70%), var(--surface-deep); }
  .orbit-hero__inner { grid-template-columns: 1fr 1fr; gap: 3rem; }
  .orbit-hero__stage { padding-block: 2rem; }
}
@media (prefers-reduced-motion: reduce) {
  .orbit-hero *, .orbit-hero *::before, .orbit-hero *::after { animation: none !important; }
}

@keyframes orbit-hero-rise { from { opacity: 0; transform: translateY(14px); filter: blur(8px); } }
@keyframes orbit-hero-core { from { opacity: 0; scale: 0.4; filter: blur(14px); } }
@keyframes orbit-hero-ring { from { opacity: 0; scale: 0.8; } }
@keyframes orbit-hero-pop { from { opacity: 0; scale: 0.3; } }
@keyframes orbit-hero-spin { to { rotate: 360deg; } }
@keyframes orbit-hero-breathe { from { opacity: 0.75; scale: 0.92; } to { opacity: 1; scale: 1.06; } }
@keyframes orbit-hero-orbit {
  from { transform: rotateZ(var(--orbit-hero-tilt)) rotateX(var(--orbit-hero-lean)) rotateZ(var(--orbit-hero-phase)) translateX(var(--orbit-hero-r)); }
  to { transform: rotateZ(var(--orbit-hero-tilt)) rotateX(var(--orbit-hero-lean)) rotateZ(calc(var(--orbit-hero-phase) + 360deg)) translateX(var(--orbit-hero-r)); }
}
@keyframes orbit-hero-counter {
  from { transform: rotateZ(calc(-1 * var(--orbit-hero-phase))) rotateX(calc(-1 * var(--orbit-hero-lean))) rotateZ(calc(-1 * var(--orbit-hero-tilt))) translateZ(var(--orbit-hero-lift, 0px)); }
  to { transform: rotateZ(calc(-1 * var(--orbit-hero-phase) - 360deg)) rotateX(calc(-1 * var(--orbit-hero-lean))) rotateZ(calc(-1 * var(--orbit-hero-tilt))) translateZ(var(--orbit-hero-lift, 0px)); }
}
```

## JS

```js
document.querySelectorAll('[data-orbit-hero]').forEach((hero) => {
  const pause = hero.querySelector('.orbit-hero__pause');

  // The orbits start only alongside their pause button, and never under reduced motion
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
    hero.classList.add('orbit-hero--live');
    pause.hidden = false;
  }
  pause.addEventListener('click', () => {
    pause.setAttribute('aria-pressed', String(hero.toggleAttribute('data-paused')));
  });
  new IntersectionObserver(([entry]) => hero.toggleAttribute('data-offscreen', !entry.isIntersecting)).observe(hero);

  // Keep a planet's label card on screen; the ring is stopped while the card shows, so one measure is enough
  const nudge = (planet) => {
    const { left, width } = planet.getBoundingClientRect();
    const half = planet.querySelector('.orbit-hero__label').offsetWidth / 2;
    const centre = left + width / 2;
    const edge = 12;
    const room = document.documentElement.clientWidth - edge;
    const shift = Math.min(0, room - (centre + half)) || Math.max(0, edge - (centre - half));
    planet.style.setProperty('--orbit-hero-nudge', `${shift}px`);
  };
  hero.querySelectorAll('.orbit-hero__planet').forEach((planet) => {
    planet.addEventListener('pointerenter', () => nudge(planet));
    planet.addEventListener('focus', () => nudge(planet));
  });

  // WCAG 1.4.13: Escape hides the card without moving focus; the next move or focus brings it back
  hero.addEventListener('keydown', (e) => { if (e.key === 'Escape') hero.classList.add('is-quiet'); });
  hero.addEventListener('focusin', () => hero.classList.remove('is-quiet'));
  hero.addEventListener('pointermove', () => hero.classList.remove('is-quiet'), { passive: true });
});
```

## Notes

- The planets are ordinary links in a labelled list (`aria-label="Services"`), in reading order: Plumbing, Electrical, HVAC, Roofing, Solar, Locks. The label card is part of each link's text, so its name is the full offer ("Plumbing Same-day leak repair · from $89"). Hover or focus stops the ring (the whole ring via `:has()`, otherwise just that planet), swells the planet, lifts it in front of the core (`translateZ`) and shows the card. Escape hides the card (WCAG 1.4.13), and the card itself can be hovered. Rings, comets and the core are `aria-hidden`.
- How the 3D works: each `<li>` carries its ring's transform plus a phase angle, and the link counter-rotates by the same amounts, so its net transform is a pure translation and the icon stays upright and undistorted. The system is an orthographic `preserve-3d` context, so planets and rings really pass in front of and behind the core. Tune a ring with `--orbit-hero-r`, `--orbit-hero-tilt`, `--orbit-hero-lean` and `--orbit-hero-speed`, and place a planet with `--orbit-hero-phase` and `--orbit-hero-tint`.
- Without JS, and under reduced motion, it's a static constellation: every planet sits at its phase, the comets are still arcs, and there's no entrance or halo breathing. JS only starts the loops (`.orbit-hero--live`) together with the pause button; an `IntersectionObserver` freezes them off-screen.
- Mobile: the orbit sits below the copy at `min(18rem, 100vw − gutters)` with two rings; the outer ring and its comet return from 768px. Planet discs are 44px (48px from 768px). From 1024px the hero splits into two columns.
- Contrast on `--surface-deep`: the lead and proof use `--text-inverse-muted` (about 8:1); the gradient phrase is 9:1 or better; the label card is `--text-main`/`--text-muted` on white (14.6:1 and 4.8:1); the primary CTA label is 14.6:1.
- Browser support: plane sorting in `preserve-3d` works in current Chromium, Safari and Firefox. The `translateZ` lift relies on `var()` updating inside running keyframes (current engines); where it doesn't, a planet behind the core still pauses and shows its card.
