# Chameleon Sections

A page canvas that changes mood as you scroll. Four sections (night, sand, ocean, ink on paper) each declare a palette. As one crosses the middle of the viewport, the whole wrapper's background, text, buttons, chips, rules and CSS-drawn scene glide into its colours together, and that section's scene settles: the moon rises, the sun comes up, the waves swell, a stamp lands. On phones each scene becomes a wide banner above its copy. Depends on `tokens/variables.css`.

**Motion:** palette morph on seven registered colour properties (backgrounds `--dur-5` `--ease-in-out`; text colours change in a `--dur-3` window centred on that glide) · scene settle as a section becomes active (`--dur-5` `--ease-out`, sequenced with `--stagger`; drop and stamp land with `--ease-spring`) · button lift and press (`--dur-2`, `--ease-spring`) · link underline colour (`--dur-2`).

## HTML

```html
<div class="chameleon">
  <section class="chameleon__section" data-chameleon="night" aria-labelledby="chameleon-night-title">
    <div class="chameleon__inner">
      <div class="chameleon__copy">
        <p class="chameleon__eyebrow"><span class="chameleon__time">02:14</span> Northside · Emergency line</p>
        <h2 id="chameleon-night-title" class="chameleon__title">Burst pipe at 2&nbsp;a.m.? Someone picks up.</h2>
        <p class="chameleon__lead">Our night crew answers in three rings and is usually at your door within the hour. Same rates as daytime, with no call-out surcharge.</p>
        <div class="chameleon__meta">
          <ul class="chameleon__chips" role="list">
            <li class="chameleon__chip">24/7 dispatch</li>
            <li class="chameleon__chip">41 min average arrival</li>
            <li class="chameleon__chip">No night surcharge</li>
          </ul>
          <div class="chameleon__actions">
            <a class="chameleon__btn" href="tel:+15555550123">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
              Call (555) 555-0123
            </a>
            <a class="chameleon__link" href="#emergency">
              How emergencies work
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </div>
        </div>
        <p class="chameleon__hint">
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
          Scroll to change the hour
        </p>
      </div>
      <div class="chameleon__art chameleon__art--night" aria-hidden="true">
        <span class="chameleon__stars"></span>
        <span class="chameleon__moon"></span>
        <span class="chameleon__roofs"></span>
        <span class="chameleon__window"></span>
        <span class="chameleon__window chameleon__window--dim"></span>
      </div>
    </div>
  </section>

  <section class="chameleon__section chameleon__section--flip" data-chameleon="sand" aria-labelledby="chameleon-sand-title">
    <div class="chameleon__inner">
      <div class="chameleon__copy">
        <p class="chameleon__eyebrow"><span class="chameleon__time">07:30</span> Westlake · Weekend visits</p>
        <h2 id="chameleon-sand-title" class="chameleon__title">Saturday slots, booked before the coffee's ready.</h2>
        <p class="chameleon__lead">Weekend visits at weekday prices. Pick a two-hour window and we'll text you the moment the van leaves the depot.</p>
        <div class="chameleon__meta">
          <ul class="chameleon__chips" role="list">
            <li class="chameleon__chip">Sat &amp; Sun</li>
            <li class="chameleon__chip">2-hour windows</li>
            <li class="chameleon__chip">Live text updates</li>
          </ul>
          <div class="chameleon__actions">
            <a class="chameleon__btn" href="#weekend">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /></svg>
              See weekend times
            </a>
            <a class="chameleon__link" href="#pricing">
              Weekday prices, explained
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </div>
        </div>
      </div>
      <div class="chameleon__art chameleon__art--sand" aria-hidden="true">
        <span class="chameleon__sun"></span>
        <span class="chameleon__dune"></span>
        <span class="chameleon__dune chameleon__dune--near"></span>
      </div>
    </div>
  </section>

  <section class="chameleon__section" data-chameleon="ocean" aria-labelledby="chameleon-ocean-title">
    <div class="chameleon__inner">
      <div class="chameleon__copy">
        <p class="chameleon__eyebrow"><span class="chameleon__time">12:45</span> Riverside · Water heaters</p>
        <h2 id="chameleon-ocean-title" class="chameleon__title">Old tank out, hot water back by dinner.</h2>
        <p class="chameleon__lead">We swap water heaters in an afternoon, haul the old unit away and register the 10-year warranty in your name.</p>
        <div class="chameleon__meta">
          <ul class="chameleon__chips" role="list">
            <li class="chameleon__chip">Same-day install</li>
            <li class="chameleon__chip">10-year warranty</li>
            <li class="chameleon__chip">Old unit removed</li>
          </ul>
          <div class="chameleon__actions">
            <a class="chameleon__btn" href="#heater-quote">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 2.7S6 9 6 14a6 6 0 0 0 12 0c0-5-6-11.3-6-11.3z" /></svg>
              Get a heater quote
            </a>
            <a class="chameleon__link" href="#tankless">
              Tank or tankless?
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </div>
        </div>
      </div>
      <div class="chameleon__art chameleon__art--ocean" aria-hidden="true">
        <span class="chameleon__drop"></span>
        <span class="chameleon__ripple"></span>
        <span class="chameleon__wave"></span>
        <span class="chameleon__wave chameleon__wave--mid"></span>
        <span class="chameleon__wave chameleon__wave--near"></span>
      </div>
    </div>
  </section>

  <section class="chameleon__section chameleon__section--flip" data-chameleon="paper" aria-labelledby="chameleon-paper-title">
    <div class="chameleon__inner">
      <div class="chameleon__copy">
        <p class="chameleon__eyebrow"><span class="chameleon__time">17:20</span> Your inbox · Written quote</p>
        <h2 id="chameleon-paper-title" class="chameleon__title">The invoice matches the quote. Every time.</h2>
        <p class="chameleon__lead">You get an itemised price in writing before we pick up a tool. If the job runs long, that's on us, not you.</p>
        <div class="chameleon__meta">
          <ul class="chameleon__chips" role="list">
            <li class="chameleon__chip">Fixed-price quotes</li>
            <li class="chameleon__chip">Pay when it's done</li>
            <li class="chameleon__chip">Receipts kept for you</li>
          </ul>
          <div class="chameleon__actions">
            <a class="chameleon__btn" href="#quote">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8zM14 3v5h5M9 13h6M9 17h4" /></svg>
              Request a written quote
            </a>
            <a class="chameleon__link" href="mailto:hello@example.com">
              hello@example.com
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </div>
        </div>
      </div>
      <div class="chameleon__art chameleon__art--paper" aria-hidden="true">
        <span class="chameleon__doc"><span class="chameleon__doc-total"><span>Total</span><span>$149.00</span></span></span>
        <span class="chameleon__stamp">Paid</span>
      </div>
    </div>
  </section>
</div>
```

## CSS

```css
/* Registered colours: the wrapper transitions these; every child inherits the in-between values */
@property --chameleon-bg { syntax: "<color>"; inherits: true; initial-value: transparent; }
@property --chameleon-fg { syntax: "<color>"; inherits: true; initial-value: transparent; }
@property --chameleon-muted { syntax: "<color>"; inherits: true; initial-value: transparent; }
@property --chameleon-accent { syntax: "<color>"; inherits: true; initial-value: transparent; }
@property --chameleon-on-accent { syntax: "<color>"; inherits: true; initial-value: transparent; }
@property --chameleon-glow { syntax: "<color>"; inherits: true; initial-value: transparent; }
@property --chameleon-spark { syntax: "<color>"; inherits: true; initial-value: transparent; }

/* Four moods built from tokens. With JS the wrapper wears the active one; without JS each section wears its own */
.chameleon,
.chameleon[data-chameleon-active="night"],
.chameleon:not(.chameleon--js) [data-chameleon="night"] {
  --chameleon-bg: color-mix(in srgb, var(--surface-deep) 94%, var(--primary));
  --chameleon-fg: var(--text-inverse);
  --chameleon-muted: var(--text-inverse-muted);
  --chameleon-accent: color-mix(in srgb, var(--primary) 45%, var(--text-inverse));
  --chameleon-on-accent: var(--surface-deep);
  --chameleon-glow: var(--primary);
  --chameleon-spark: var(--accent);
}
.chameleon[data-chameleon-active="sand"],
.chameleon:not(.chameleon--js) [data-chameleon="sand"] {
  --chameleon-bg: color-mix(in srgb, var(--accent) 22%, var(--surface-light));
  --chameleon-fg: color-mix(in srgb, var(--warning) 30%, var(--surface-deep));
  --chameleon-muted: color-mix(in srgb, var(--warning) 65%, var(--text-main));
  --chameleon-accent: color-mix(in srgb, var(--warning) 85%, var(--surface-deep));
  --chameleon-on-accent: var(--surface-light);
  --chameleon-glow: var(--accent);
  --chameleon-spark: color-mix(in srgb, var(--accent) 65%, var(--danger));
}
.chameleon[data-chameleon-active="ocean"],
.chameleon:not(.chameleon--js) [data-chameleon="ocean"] {
  --chameleon-bg: color-mix(in srgb, var(--primary-2) 42%, var(--surface-deep));
  --chameleon-fg: var(--text-inverse);
  --chameleon-muted: color-mix(in srgb, var(--primary-2) 20%, var(--text-inverse));
  --chameleon-accent: color-mix(in srgb, var(--primary-2) 45%, var(--text-inverse));
  --chameleon-on-accent: var(--surface-deep);
  --chameleon-glow: var(--primary-2);
  --chameleon-spark: color-mix(in srgb, var(--accent) 60%, var(--text-inverse));
}
.chameleon[data-chameleon-active="paper"],
.chameleon:not(.chameleon--js) [data-chameleon="paper"] {
  --chameleon-bg: color-mix(in srgb, var(--surface-light) 96%, var(--accent));
  --chameleon-fg: var(--surface-dark);
  --chameleon-muted: color-mix(in srgb, var(--text-muted) 80%, var(--surface-dark));
  --chameleon-accent: var(--primary);
  --chameleon-on-accent: var(--surface-light);
  --chameleon-glow: color-mix(in srgb, var(--primary) 70%, var(--primary-2));
  --chameleon-spark: var(--danger);
}

/* Derived tones are re-declared on sections so each one mixes from the colours it actually wears */
.chameleon, .chameleon__section {
  --chameleon-line: color-mix(in srgb, var(--chameleon-fg) 14%, transparent);
  --chameleon-tint: color-mix(in srgb, var(--chameleon-fg) 6%, transparent);
}

/* Canvas */
.chameleon { background-color: var(--chameleon-bg); color: var(--chameleon-fg); font-family: var(--font-sans); }
/* Live morph: backgrounds glide; text colours change in a short window centred on that glide */
.chameleon.is-live {
  --chameleon-ink-delay: calc((var(--dur-5) - var(--dur-3)) / 2);
  transition:
    --chameleon-bg var(--dur-5) var(--ease-in-out),
    --chameleon-glow var(--dur-5) var(--ease-in-out),
    --chameleon-spark var(--dur-5) var(--ease-in-out),
    --chameleon-fg var(--dur-3) var(--ease-in-out) var(--chameleon-ink-delay),
    --chameleon-muted var(--dur-3) var(--ease-in-out) var(--chameleon-ink-delay),
    --chameleon-accent var(--dur-3) var(--ease-in-out) var(--chameleon-ink-delay),
    --chameleon-on-accent var(--dur-3) var(--ease-in-out) var(--chameleon-ink-delay);
}

/* Sections: full-height bands with a soft glow in the live palette */
.chameleon__section { position: relative; display: grid; align-items: center; min-height: 100vh; min-height: 100svh; overflow: clip; }
.chameleon:not(.chameleon--js) .chameleon__section { background-color: var(--chameleon-bg); color: var(--chameleon-fg); }
.chameleon__section::before {
  content: ""; position: absolute; right: -20%; bottom: -35%; width: 80%; aspect-ratio: 1; pointer-events: none;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--chameleon-glow) 20%, transparent), transparent);
}
.chameleon__section--flip::before { right: auto; left: -20%; }
.chameleon__inner {
  position: relative; display: grid; gap: clamp(2rem, 5vw, 4.5rem); align-items: center;
  width: 100%; max-width: var(--container-max); margin-inline: auto;
  padding: clamp(3.5rem, 11vh, 7rem) var(--gutter);
}

/* Copy */
.chameleon__copy { max-width: 36rem; }
.chameleon__eyebrow {
  display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 0.75rem; margin: 0;
  color: var(--chameleon-muted); font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
}
.chameleon__eyebrow::before {
  content: ""; width: 0.5rem; height: 0.5rem; border-radius: var(--radius-full); background: var(--chameleon-accent);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--chameleon-accent) 22%, transparent);
}
.chameleon__time { color: var(--chameleon-accent); font-weight: 600; letter-spacing: 0.02em; }
.chameleon__title {
  margin: 1.25rem 0 0; font: 600 clamp(2.25rem, 1.25rem + 3.6vw, 4rem)/1.02 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.chameleon__lead { margin: 1.25rem 0 0; color: var(--chameleon-muted); font-size: clamp(1.0625rem, 1rem + 0.3vw, 1.1875rem); line-height: 1.6; }

/* Rule with an accent tick, chips and actions */
.chameleon__meta { position: relative; margin-top: 2rem; padding-top: 1.5rem; border-top: 1px solid var(--chameleon-line); }
.chameleon__meta::before { content: ""; position: absolute; left: 0; top: -1px; width: 3rem; height: 1px; background: var(--chameleon-accent); }
.chameleon__chips { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.chameleon__chip {
  display: inline-flex; align-items: center; gap: 0.5rem; padding: 0.4375rem 0.75rem; border-radius: var(--radius-full);
  background: var(--chameleon-tint); box-shadow: inset 0 0 0 1px var(--chameleon-line); font: 500 0.8125rem/1.2 var(--font-mono);
}
.chameleon__chip::before { content: ""; flex: none; width: 0.375rem; height: 0.375rem; border-radius: var(--radius-full); background: var(--chameleon-accent); }
.chameleon__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.75rem 1.5rem; margin-top: 1.75rem; }
.chameleon__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--chameleon-accent); color: var(--chameleon-on-accent); font: 600 0.9375rem/1.2 var(--font-sans); text-decoration: none;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 30%, transparent), 0 14px 32px -16px var(--chameleon-glow);
  transition: transform var(--dur-2) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.chameleon__btn:hover { transform: translateY(-2px); box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 30%, transparent), 0 20px 40px -16px var(--chameleon-glow); }
.chameleon__btn:active { transform: scale(0.97); }
.chameleon__link {
  display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; color: inherit; font-size: 0.9375rem; font-weight: 600;
  text-decoration: underline; text-decoration-color: var(--chameleon-line); text-decoration-thickness: 1px; text-underline-offset: 0.35em;
  transition: text-decoration-color var(--dur-2) var(--ease-out);
}
.chameleon__link:hover { text-decoration-color: var(--chameleon-accent); }
.chameleon__link svg { transition: transform var(--dur-3) var(--ease-spring); }
.chameleon__link:hover svg { transform: translateX(3px); }
.chameleon :is(.chameleon__btn, .chameleon__link, .chameleon__hint) svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.chameleon :is(.chameleon__btn, .chameleon__link):focus-visible { outline: 2px solid var(--chameleon-fg); outline-offset: 3px; }
.chameleon__hint {
  display: flex; align-items: center; gap: 0.5rem; margin: 3rem 0 0; color: var(--chameleon-muted);
  font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}

/* Scene frame: CSS illustration in the live palette (decorative) */
.chameleon__art {
  --chameleon-glow-at: 72% 14%;
  position: relative; isolation: isolate; overflow: hidden; container-type: inline-size; order: -1;
  aspect-ratio: 16 / 9; border-radius: var(--radius-2xl);
  background:
    radial-gradient(75% 65% at var(--chameleon-glow-at), color-mix(in srgb, var(--chameleon-glow) 40%, transparent), transparent 72%),
    linear-gradient(180deg, color-mix(in srgb, var(--chameleon-fg) 3%, transparent), color-mix(in srgb, var(--chameleon-fg) 9%, transparent));
  box-shadow: 0 40px 80px -40px color-mix(in srgb, var(--chameleon-glow) 70%, transparent);
}
.chameleon__art > * { position: absolute; }
.chameleon__art::after {
  content: ""; position: absolute; inset: 0; z-index: 2; border-radius: inherit; pointer-events: none;
  box-shadow: inset 0 0 0 1px var(--chameleon-line), inset 0 1px 0 color-mix(in srgb, var(--chameleon-fg) 14%, transparent);
}

/* Night: stars, a crescent moon, rooftops with one lit window */
.chameleon__stars {
  inset: 0 0 38%; opacity: 0.8;
  background:
    radial-gradient(circle at 8% 18%, var(--chameleon-fg) 0 1px, transparent 1.6px),
    radial-gradient(circle at 21% 44%, var(--chameleon-fg) 0 1.2px, transparent 1.8px),
    radial-gradient(circle at 33% 12%, var(--chameleon-fg) 0 1px, transparent 1.6px),
    radial-gradient(circle at 46% 32%, var(--chameleon-fg) 0 0.8px, transparent 1.4px),
    radial-gradient(circle at 57% 9%, var(--chameleon-fg) 0 1.2px, transparent 1.8px),
    radial-gradient(circle at 62% 52%, var(--chameleon-fg) 0 1px, transparent 1.6px),
    radial-gradient(circle at 90% 62%, var(--chameleon-fg) 0 1px, transparent 1.6px),
    radial-gradient(circle at 13% 72%, var(--chameleon-fg) 0 0.8px, transparent 1.4px),
    radial-gradient(circle at 40% 78%, var(--chameleon-fg) 0 1px, transparent 1.6px);
}
.chameleon__moon {
  top: 13%; right: 15%; width: 19cqi; aspect-ratio: 1; border-radius: 50%; rotate: -20deg;
  box-shadow: inset -4cqi 1.5cqi 0 0 var(--chameleon-accent);
  filter: drop-shadow(0 0 3cqi color-mix(in srgb, var(--chameleon-accent) 50%, transparent));
}
.chameleon__art--night::before {
  content: ""; position: absolute; inset: auto 0 0; height: 42%; background: color-mix(in srgb, var(--chameleon-fg) 6%, transparent);
  clip-path: polygon(0 40%, 8% 40%, 8% 22%, 16% 22%, 16% 48%, 30% 48%, 30% 30%, 37% 30%, 37% 14%, 44% 14%, 44% 44%, 62% 44%, 62% 26%, 72% 26%, 72% 50%, 84% 50%, 84% 20%, 92% 20%, 92% 38%, 100% 38%, 100% 100%, 0 100%);
}
.chameleon__roofs {
  inset: auto 0 0; height: 36%; background: color-mix(in srgb, var(--chameleon-fg) 12%, var(--chameleon-bg));
  clip-path: polygon(0 86%, 4% 86%, 4% 52%, 15% 20%, 26% 52%, 26% 86%, 34% 86%, 34% 40%, 50% 0, 66% 40%, 66% 86%, 74% 86%, 74% 54%, 85% 24%, 96% 54%, 96% 86%, 100% 86%, 100% 100%, 0 100%);
}
.chameleon__window {
  top: 80%; left: 42.5%; width: 4.5cqi; height: 5cqi; border-radius: 0.5cqi; background: var(--chameleon-spark);
  box-shadow: 0 0 5cqi 1cqi color-mix(in srgb, var(--chameleon-spark) 45%, transparent);
}
.chameleon__window--dim { left: 53%; background: color-mix(in srgb, var(--chameleon-fg) 22%, var(--chameleon-bg)); box-shadow: none; }

/* Sand: a banded sun rising over two dunes */
.chameleon__art--sand { --chameleon-glow-at: 50% 58%; }
.chameleon__art--sand::before { content: ""; position: absolute; inset: 62% 0 auto; height: 1px; background: var(--chameleon-line); }
.chameleon__sun {
  top: 20%; left: 50%; width: 40cqi; aspect-ratio: 1; margin-left: -20cqi; border-radius: 50%;
  background: linear-gradient(180deg, var(--chameleon-glow), var(--chameleon-spark));
  -webkit-mask: linear-gradient(180deg, black 50%, transparent 50% 55%, black 55% 63%, transparent 63% 67%, black 67% 74%, transparent 74% 77%, black 77%);
  mask: linear-gradient(180deg, black 50%, transparent 50% 55%, black 55% 63%, transparent 63% 67%, black 67% 74%, transparent 74% 77%, black 77%);
}
.chameleon__dune { top: 60%; left: -30%; width: 100%; height: 90%; border-radius: 50%; background: color-mix(in srgb, var(--chameleon-spark) 18%, var(--chameleon-bg)); }
.chameleon__dune--near { top: 71%; left: 28%; width: 110%; background: color-mix(in srgb, var(--chameleon-fg) 14%, var(--chameleon-bg)); }

/* Ocean: a falling drop, its ripple and three scalloped waves */
.chameleon__art--ocean { --chameleon-glow-at: 50% 8%; }
.chameleon__drop {
  top: 10%; left: 50%; width: 12cqi; aspect-ratio: 1; margin-left: -6cqi; border-radius: 0 50% 50% 50%; rotate: 45deg;
  background: linear-gradient(135deg, var(--chameleon-fg), var(--chameleon-accent));
  box-shadow: 0 2cqi 6cqi -1cqi color-mix(in srgb, var(--chameleon-glow) 70%, transparent);
}
.chameleon__ripple {
  top: 41%; left: 50%; width: 36cqi; height: 7cqi; margin-left: -18cqi; border-radius: 50%;
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--chameleon-fg) 30%, transparent), 0 0 0 3cqi color-mix(in srgb, var(--chameleon-fg) 6%, transparent);
}
.chameleon__wave {
  --chameleon-wave-w: 18cqi; --chameleon-wave-h: 3.5cqi; --chameleon-wave-x: 0cqi;
  left: -10%; right: -10%; bottom: 0; height: 52%; background: color-mix(in srgb, var(--chameleon-glow) 26%, var(--chameleon-bg));
  -webkit-mask:
    radial-gradient(55% 100% at 50% 100%, black 96%, transparent) var(--chameleon-wave-x) 0 / var(--chameleon-wave-w) var(--chameleon-wave-h) repeat-x,
    linear-gradient(black, black) 0 var(--chameleon-wave-h) / 100% 100% no-repeat;
  mask:
    radial-gradient(55% 100% at 50% 100%, black 96%, transparent) var(--chameleon-wave-x) 0 / var(--chameleon-wave-w) var(--chameleon-wave-h) repeat-x,
    linear-gradient(black, black) 0 var(--chameleon-wave-h) / 100% 100% no-repeat;
}
.chameleon__wave--mid { --chameleon-wave-w: 24cqi; --chameleon-wave-h: 4.5cqi; --chameleon-wave-x: 8cqi; height: 38%; background: color-mix(in srgb, var(--chameleon-glow) 48%, var(--chameleon-bg)); }
.chameleon__wave--near { --chameleon-wave-w: 32cqi; --chameleon-wave-h: 6cqi; --chameleon-wave-x: 15cqi; height: 24%; background: color-mix(in srgb, var(--chameleon-accent) 55%, var(--chameleon-bg)); }

/* Ink on paper: a written quote on a second sheet, and a stamp */
.chameleon__art--paper { --chameleon-glow-at: 22% 18%; }
.chameleon__art--paper::before, .chameleon__doc {
  top: 12%; left: 50%; height: 76%; aspect-ratio: 3 / 4; border-radius: 1.5cqi;
  box-shadow: inset 0 0 0 1px var(--chameleon-line), 0 3cqi 6cqi -3cqi color-mix(in srgb, var(--surface-deep) 35%, transparent);
}
.chameleon__art--paper::before { content: ""; position: absolute; translate: -42% 2%; rotate: 6deg; background: color-mix(in srgb, var(--chameleon-bg) 90%, var(--chameleon-fg)); }
.chameleon__doc {
  translate: -56% 0; rotate: -3deg;
  background:
    linear-gradient(var(--chameleon-accent), var(--chameleon-accent)) 12% 11% / 34% 5% no-repeat,
    linear-gradient(var(--chameleon-line), var(--chameleon-line)) 12% 20% / 22% 2% no-repeat,
    repeating-linear-gradient(180deg, var(--chameleon-line) 0 1px, transparent 1px 20%) 12% 36% / 76% 34% no-repeat,
    color-mix(in srgb, var(--chameleon-bg) 80%, var(--surface-light));
}
.chameleon__doc-total {
  position: absolute; left: 12%; right: 12%; bottom: 12%; display: flex; justify-content: space-between;
  padding-top: 1.2cqi; border-top: 1px dashed var(--chameleon-line); font: 600 2.4cqi/1 var(--font-mono);
}
.chameleon__stamp {
  right: 16%; bottom: 17%; padding: 1cqi 1.8cqi; border: 0.45cqi solid var(--chameleon-spark); border-radius: 1cqi; rotate: -14deg;
  color: var(--chameleon-spark); font: 700 3cqi/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}

/* Scene settle: inactive scenes rest off their mark, the active one glides home (JS + motion allowed) */
@media (prefers-reduced-motion: no-preference) {
  .chameleon--js .chameleon__section:not(.is-active) .chameleon__moon { translate: -40% 60%; }
  .chameleon--js .chameleon__section:not(.is-active) .chameleon__window:not(.chameleon__window--dim) { opacity: 0.15; }
  .chameleon--js .chameleon__section:not(.is-active) .chameleon__sun { translate: 0 45%; }
  .chameleon--js .chameleon__section:not(.is-active) .chameleon__wave { translate: -6% 30%; }
  .chameleon--js .chameleon__section:not(.is-active) .chameleon__drop { translate: 0 -70%; opacity: 0; }
  .chameleon--js .chameleon__section:not(.is-active) .chameleon__ripple { scale: 0.3; opacity: 0; }
  .chameleon--js .chameleon__section:not(.is-active) .chameleon__doc { translate: -56% 8%; }
  .chameleon--js .chameleon__section:not(.is-active) .chameleon__stamp { scale: 1.8; opacity: 0; }
}
.chameleon.is-live :is(.chameleon__moon, .chameleon__window, .chameleon__sun, .chameleon__wave, .chameleon__drop, .chameleon__ripple, .chameleon__doc, .chameleon__stamp) {
  transition: translate var(--dur-5) var(--ease-out), opacity var(--dur-4) var(--ease-out), scale var(--dur-4) var(--ease-spring);
  transition-delay: var(--chameleon-delay, 0ms);
}
.chameleon.is-live .chameleon__drop { transition-timing-function: var(--ease-spring), var(--ease-out), var(--ease-spring); }
.chameleon__window, .chameleon__stamp { --chameleon-delay: calc(var(--stagger) * 5); }
.chameleon__wave--mid, .chameleon__drop { --chameleon-delay: calc(var(--stagger) * 2); }
.chameleon__wave--near { --chameleon-delay: calc(var(--stagger) * 4); }
.chameleon__ripple { --chameleon-delay: calc(var(--stagger) * 7); }

@media (min-width: 768px) {
  .chameleon__inner { grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr); }
  .chameleon__art { order: 0; aspect-ratio: 5 / 4; }
  .chameleon__section--flip .chameleon__art { order: -1; }
}
```

## JS

```js
document.querySelectorAll('.chameleon').forEach((root) => {
  const sections = [...root.querySelectorAll('[data-chameleon]')];
  if (!sections.length || !('IntersectionObserver' in window)) return;

  // The wrapper wears the active section's palette; that section's scene settles
  const activate = (section) => {
    root.dataset.chameleonActive = section.dataset.chameleon;
    sections.forEach((s) => s.classList.toggle('is-active', s === section));
  };

  // Start on the section under the viewport's centre line and commit it before transitions exist, so nothing flashes
  const middle = innerHeight / 2;
  activate(sections.find((s) => {
    const r = s.getBoundingClientRect();
    return r.top <= middle && r.bottom > middle;
  }) || sections[0]);
  root.classList.add('chameleon--js');
  void root.offsetWidth;
  root.classList.add('is-live');

  // A thin band across the middle of the viewport decides which palette is live; the incoming section wins
  const band = new IntersectionObserver((entries) => {
    entries.forEach((entry) => { if (entry.isIntersecting) activate(entry.target); });
  }, { rootMargin: '-45% 0px -45% 0px' });
  sections.forEach((s) => band.observe(s));
});
```

## Notes

- Each `<section data-chameleon>` is an ordinary section with its own `<h2>`, so reading order and landmarks never depend on the effect. An IntersectionObserver band across the middle 10% of the viewport picks the section crossing it. The wrapper then transitions seven registered `@property` colours, and every child inherits the in-between values, so buttons, chips, rules and scenes stay in step. Scenes are CSS art, marked `aria-hidden`.
- Contrast for each palette (text / muted / accent text against the background, and button text against the accent): night 18.1 / 7.4 / 9.3, 9.7 · sand 12.6 / 6.4 / 5.4, 6.3 · ocean 10.4 / 8.2 / 6.0, 10.9 · paper 17.3 / 6.1 / 5.0, 5.2. Text colours change in a `--dur-3` window centred on the background's `--dur-5` glide, so the low-contrast midpoint of a dark-to-light morph lasts about a third of a second. Focus rings use the live `--chameleon-fg`, which clears 10:1 against every palette.
- Without JS, each section paints its own palette, so the page reads as four finished colour bands with scenes in their resting poses. Under reduced motion the duration tokens collapse, so palettes switch instantly and scenes don't move. Browsers without `@property` also switch palettes instantly.
- The starting palette is picked and committed before the `is-live` class adds transitions, so a page loaded mid-scroll doesn't flash night colours first.
- To retheme, edit the seven colours in a palette rule. To add a mood, copy a rule with a new `data-chameleon` value (both selectors) and keep text against background at 4.5:1 or above. Sections can be shorter than full height, but keep them at least about 55vh so each one crosses the centre band.
