# Dynamic Island Nav

A near-black pill floats at the top centre like the iPhone's Dynamic Island, showing live status: "Open now · Tech nearby 12 min", with a ping that settles after a few seconds. Tap it and the island springs open into a card holding the technician's live ETA, a six-link nav grid, and Book now and Call actions: width, height and radius morph together while the content blurs in. Shortly after load it plays one live activity: the pill widens to show a new five-star review, announced to screen readers, then folds back. On phones it hugs the top safe area; the card is never wider than the screen. Depends on `tokens/variables.css`.

**Motion:** size and radius morph (`--dur-4`, `--ease-spring`; `interpolate-size` in CSS, measured spring elsewhere) · content crossfade with blur (`--dur-3`, `--ease-out`) · status ping, 3 pulses then still · review stars pop in turn (`--ease-spring`, `--stagger`) · scrim fade.

## HTML

```html
<div class="island-nav-demo">
  <div class="island-nav" data-island-nav data-island-nav-demo>
    <span class="island-nav__scrim" aria-hidden="true"></span>
    <div class="island-nav__shell">
      <div class="island-nav__row">
        <p class="island-nav__status">
          <span class="island-nav__dot" aria-hidden="true"></span>
          <span class="island-nav__open">Open now</span>
          <span class="island-nav__sep" aria-hidden="true">·</span>
          <span class="island-nav__near">Tech nearby</span>
          <span class="island-nav__eta">12 min</span>
        </p>
        <button class="island-nav__toggle" type="button" aria-expanded="false" hidden>
          <span class="island-nav__sr">Menu</span>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
        </button>
      </div>

      <div class="island-nav__alert" aria-hidden="true">
        <span class="island-nav__alert-face">DR</span>
        <span class="island-nav__alert-text"><strong>New review</strong><span>Dana R. · Westlake</span></span>
        <span class="island-nav__stars">
          <svg style="--island-nav-i: 0" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg style="--island-nav-i: 1" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg style="--island-nav-i: 2" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg style="--island-nav-i: 3" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          <svg style="--island-nav-i: 4" viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
        </span>
      </div>

      <div class="island-nav__body">
        <div class="island-nav__trip">
          <span class="island-nav__face" aria-hidden="true">SK</span>
          <p class="island-nav__trip-text"><strong>Sam is on the way</strong><span>Leak repair · arriving 2:40 pm</span></p>
          <span class="island-nav__mins">12 min</span>
          <span class="island-nav__route" aria-hidden="true"><span></span></span>
        </div>

        <nav class="island-nav__nav" aria-label="Main">
          <ul class="island-nav__grid" role="list">
            <li style="--island-nav-i: 0"><a class="island-nav__link" href="/" aria-current="page"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M3 10.5 12 3l9 7.5" /><path d="M5.5 9v11a1 1 0 0 0 1 1H10v-6h4v6h3.5a1 1 0 0 0 1-1V9" /></svg>Home</a></li>
            <li style="--island-nav-i: 1"><a class="island-nav__link" href="/services"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z" /></svg>Services</a></li>
            <li style="--island-nav-i: 2"><a class="island-nav__link" href="/pricing"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z" /><circle cx="7.5" cy="7.5" r="1.5" /></svg>Pricing</a></li>
            <li style="--island-nav-i: 3"><a class="island-nav__link" href="/reviews"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>Reviews</a></li>
            <li style="--island-nav-i: 4"><a class="island-nav__link" href="/areas"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z" /><circle cx="12" cy="10" r="2.5" /></svg>Areas</a></li>
            <li style="--island-nav-i: 5"><a class="island-nav__link" href="/contact"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2" /><path d="m3 7 9 6 9-6" /></svg>Contact</a></li>
          </ul>
        </nav>

        <div class="island-nav__actions">
          <a class="island-nav__cta" href="/book">
            Book now
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
          <a class="island-nav__call" href="tel:+15555550123" aria-label="Call (555) 555-0123">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
          </a>
        </div>
      </div>
    </div>
    <p class="island-nav__sr" role="status" aria-live="polite"></p>
  </div>

  <div class="island-nav-demo__page">
    <p class="island-nav-demo__eyebrow">Brand · Springfield</p>
    <h2 class="island-nav-demo__title">Same-day repairs, tracked to the minute.</h2>
    <p class="island-nav-demo__lead">Tap the island at the top for the menu. It also carries your technician's live arrival time.</p>
    <div class="island-nav-demo__map" aria-hidden="true">
      <svg viewBox="0 0 320 180" preserveAspectRatio="none" focusable="false"><path class="island-nav-demo__trail" d="M24 150C90 150 80 70 150 82" /><path class="island-nav-demo__ahead" d="M150 82C220 94 230 30 296 36" /></svg>
      <span class="island-nav-demo__pin island-nav-demo__pin--van"></span>
      <span class="island-nav-demo__pin island-nav-demo__pin--home"></span>
    </div>
    <ul class="island-nav-demo__points" role="list">
      <li><strong>Live arrival</strong><span>Watch your technician's van across Northside and Riverside.</span></li>
      <li><strong>Flat-rate pricing</strong><span>The quote you approve is the price you pay.</span></li>
      <li><strong>12-month guarantee</strong><span>Every repair, parts and labour.</span></li>
    </ul>
  </div>
</div>
```

## CSS

```css
/* Demo page: light, with a live-route card so the island has something to talk about */
.island-nav-demo {
  min-height: 100vh; min-height: 100svh; color: var(--text-main); font-family: var(--font-sans);
  background: radial-gradient(32rem 20rem at 50% -6rem, color-mix(in srgb, var(--primary) 12%, transparent), transparent 70%), var(--surface-muted);
}
.island-nav-demo__page { max-width: min(var(--container-max), 40rem); margin-inline: auto; padding: var(--space-xl) var(--gutter) var(--space-2xl); }
.island-nav-demo__eyebrow { margin: 0; color: var(--primary); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.island-nav-demo__title { margin: 0.75rem 0 0; font: 600 clamp(1.875rem, 1.3rem + 2.4vw, 2.75rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.island-nav-demo__lead { max-width: 32rem; margin: 0.875rem 0 0; color: var(--text-muted); line-height: 1.55; }
.island-nav-demo__map {
  position: relative; height: 11rem; margin-top: var(--space-xl); overflow: hidden; border-radius: var(--radius-2xl);
  background:
    linear-gradient(color-mix(in srgb, var(--text-main) 6%, transparent) 1px, transparent 1px) 0 0 / 1.75rem 1.75rem,
    linear-gradient(90deg, color-mix(in srgb, var(--text-main) 6%, transparent) 1px, transparent 1px) 0 0 / 1.75rem 1.75rem,
    radial-gradient(60% 80% at 85% 15%, color-mix(in srgb, var(--primary-2) 20%, transparent), transparent 70%),
    var(--surface-light);
  box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-lg);
}
.island-nav-demo__map svg { position: absolute; inset: 0; width: 100%; height: 100%; }
.island-nav-demo__map path { fill: none; stroke-width: 4; stroke-linecap: round; vector-effect: non-scaling-stroke; }
.island-nav-demo__trail { stroke: color-mix(in srgb, var(--text-main) 18%, transparent); stroke-dasharray: 2 8; }
.island-nav-demo__ahead { stroke: var(--primary); filter: drop-shadow(0 4px 6px color-mix(in srgb, var(--primary) 45%, transparent)); }
.island-nav-demo__pin { position: absolute; width: 1rem; height: 1rem; border-radius: 50%; translate: -50% -50%; }
.island-nav-demo__pin--van { left: 46.9%; top: 45.6%; background: var(--primary); box-shadow: 0 0 0 6px color-mix(in srgb, var(--primary) 20%, transparent), 0 6px 14px -4px var(--primary); }
.island-nav-demo__pin--home { left: 92.5%; top: 20%; background: var(--surface-light); box-shadow: inset 0 0 0 4px var(--text-main), var(--shadow-md); }
.island-nav-demo__points { display: grid; gap: 0.75rem; margin: var(--space-lg) 0 0; padding: 0; list-style: none; }
.island-nav-demo__points li { display: grid; gap: 0.25rem; padding: 1rem 1.125rem; border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-sm); }
.island-nav-demo__points strong { font: 600 1rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.island-nav-demo__points span { color: var(--text-muted); font-size: 0.875rem; line-height: 1.5; }

/* Island. Without scripting it renders as the open card, in flow at the top of the page. */
.island-nav { display: flex; justify-content: center; padding: var(--space-md) var(--gutter) 0; font-family: var(--font-sans); interpolate-size: allow-keywords; }
.island-nav__shell {
  position: relative; display: flex; flex-direction: column; overflow: hidden;
  width: min(22.5rem, 100%); max-height: calc(100vh - 1rem); max-height: calc(100dvh - 1rem); border-radius: 2rem;
  background: radial-gradient(120% 70% at 100% 0%, color-mix(in srgb, var(--primary) 24%, transparent), transparent 60%), var(--surface-deep);
  color: var(--text-inverse);
  box-shadow:
    inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse),
    0 2px 6px color-mix(in srgb, var(--surface-deep) 20%, transparent), 0 18px 40px -16px color-mix(in srgb, var(--surface-deep) 75%, transparent);
}
.island-nav__scrim, .island-nav__alert { display: none; }
.island-nav__row { flex: none; display: flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 0.4375rem 0 1rem; }
.island-nav__status { display: flex; align-items: center; gap: 0.4375rem; min-width: 0; margin: 0; font-size: 0.8125rem; font-weight: 500; white-space: nowrap; }
.island-nav__body { box-sizing: border-box; display: grid; gap: 0.625rem; min-height: 0; overflow-y: auto; padding: 0.25rem 0.75rem 0.75rem; }

/* Scripting on: start as the compact pill from the first paint (no flash of the open card).
   Failsafe: if the script never runs, the card unfolds in place after 2s. */
@media (scripting: enabled) {
  .island-nav {
    position: fixed; inset: 0 0 auto; z-index: var(--z-sticky); pointer-events: none;
    padding: max(var(--space-sm), env(safe-area-inset-top, 0px)) var(--space-sm) 0;
  }
  .island-nav ~ .island-nav-demo__page { padding-top: 5.5rem; }
  .island-nav__shell {
    width: fit-content; height: 2.75rem; border-radius: 1.375rem; pointer-events: auto;
    transition: width var(--dur-4) var(--ease-spring), height var(--dur-4) var(--ease-spring), border-radius var(--dur-4) var(--ease-spring);
  }
  .island-nav__scrim {
    display: block; position: fixed; inset: 0; z-index: -1; opacity: 0;
    background: color-mix(in srgb, var(--surface-deep) 30%, transparent);
    transition: opacity var(--dur-3) var(--ease-out);
  }
  .island-nav__status { transition: opacity var(--dur-3) var(--ease-out), filter var(--dur-3) var(--ease-out), scale var(--dur-4) var(--ease-spring); }
  .island-nav__alert {
    position: absolute; inset: 0; display: flex; align-items: center; gap: 0.625rem; padding: 0 1.125rem 0 0.5rem;
    opacity: 0; filter: blur(6px); scale: 0.92; visibility: hidden; pointer-events: none;
    transition: opacity var(--dur-3) var(--ease-out), filter var(--dur-3) var(--ease-out), scale var(--dur-4) var(--ease-spring), visibility 0s linear var(--dur-3);
  }
  .island-nav__body {
    width: 0; min-width: 100%; /* never widens the compact pill */
    opacity: 0; filter: blur(8px); translate: 0 -0.5rem; visibility: hidden;
    transition: opacity var(--dur-3) var(--ease-out), filter var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-spring), visibility 0s linear var(--dur-3);
  }
  .island-nav:not(.island-nav--js) .island-nav__shell { animation: island-nav-unfold 0.01ms 2s both; }
  .island-nav:not(.island-nav--js) .island-nav__body { animation: island-nav-reveal 0.01ms 2s both; }
}

/* States (set by JS): activity and expanded */
.island-nav[data-state="expanded"] { z-index: var(--z-popover); }
.island-nav[data-state="activity"] .island-nav__shell { width: min(20rem, 100%); height: 3.5rem; border-radius: 1.75rem; }
.island-nav[data-state="expanded"] .island-nav__shell { width: min(22.5rem, 100%); height: auto; border-radius: 2rem; }
/* Browsers without interpolate-size: JS measures both sizes and springs between them */
.island-nav--fallback .island-nav__shell { transition-property: border-radius; }
.island-nav[data-state="expanded"] .island-nav__scrim { opacity: 1; pointer-events: auto; }
.island-nav[data-state="activity"] .island-nav__status { opacity: 0; filter: blur(6px); scale: 0.9; }
.island-nav[data-state="activity"] .island-nav__alert { opacity: 1; filter: none; scale: 1; visibility: visible; transition-delay: 90ms, 90ms, 90ms, 0s; }
.island-nav[data-state="expanded"] .island-nav__body { opacity: 1; filter: none; translate: 0 0; visibility: visible; transition-delay: 80ms, 80ms, 80ms, 0s; }
.island-nav[data-state="expanded"] .island-nav__row { position: relative; }

/* Status row */
.island-nav__open { color: color-mix(in srgb, var(--success) 45%, var(--text-inverse)); font-weight: 600; }
.island-nav__sep, .island-nav__near { color: var(--text-inverse-muted); }
.island-nav__eta { margin-left: 0.25rem; padding: 0.25rem 0.4375rem; border-radius: var(--radius-full); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); font: 600 0.75rem/1 var(--font-mono); }
.island-nav__dot { position: relative; flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 8px color-mix(in srgb, var(--success) 80%, transparent); }
.island-nav__dot::after { content: ""; position: absolute; inset: 0; border-radius: 50%; background: var(--success); animation: island-nav-ping 1.6s var(--ease-out) 0.6s 3; }

/* Toggle: invisible while compact, its ::after stretches over the whole pill; an × once open */
.island-nav__toggle {
  flex: none; display: grid; place-items: center; width: 0; height: 1.875rem; margin-left: auto; padding: 0; border: 0; border-radius: 50%;
  background: transparent; color: var(--text-inverse-muted); cursor: pointer; opacity: 0; -webkit-tap-highlight-color: transparent;
  transition: width var(--dur-3) var(--ease-out), opacity var(--dur-2) var(--ease-out), background-color var(--dur-2), color var(--dur-2);
}
.island-nav__toggle[hidden] { display: none; }
.island-nav__toggle::after { content: ""; position: absolute; inset: 0; }
.island-nav__toggle svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }
.island-nav[data-state="expanded"] .island-nav__toggle { width: 1.875rem; opacity: 1; background: var(--glass-inverse); }
.island-nav__toggle:hover { color: var(--text-inverse); }
.island-nav:not([data-state="expanded"]) .island-nav__shell:has(.island-nav__toggle:focus-visible) { outline: 2px solid var(--primary); outline-offset: 3px; }
.island-nav :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* Live activity: a new review crossfades in over the status */
.island-nav__alert-face {
  flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 45%, var(--danger))); color: var(--text-main); font-size: 0.75rem; font-weight: 700;
}
.island-nav__alert-text { flex: 1; display: grid; gap: 0.125rem; min-width: 0; white-space: nowrap; }
.island-nav__alert-text strong { font-size: 0.875rem; }
.island-nav__alert-text span { overflow: hidden; color: var(--text-inverse-muted); font-size: 0.75rem; text-overflow: ellipsis; }
.island-nav__stars { flex: none; display: flex; gap: 0.125rem; color: var(--accent); }
.island-nav__stars svg { fill: currentColor; stroke: currentColor; stroke-width: 1.5; stroke-linejoin: round; }
.island-nav[data-state="activity"] .island-nav__stars svg { animation: island-nav-star var(--dur-3) var(--ease-spring) calc(200ms + var(--island-nav-i) * var(--stagger)) both; }

/* Card body */
.island-nav__trip {
  display: grid; grid-template-columns: auto minmax(0, 1fr) auto; align-items: center; gap: 0 0.75rem; padding: 0.75rem; border-radius: 1.25rem;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.island-nav__face { display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 50%; background: var(--gradient-brand); font-size: 0.75rem; font-weight: 700; }
.island-nav__trip-text { display: grid; gap: 0.125rem; margin: 0; }
.island-nav__trip-text strong { font-size: 0.875rem; }
.island-nav__trip-text span { overflow: hidden; color: var(--text-inverse-muted); font-size: 0.75rem; white-space: nowrap; text-overflow: ellipsis; }
.island-nav__mins { color: color-mix(in srgb, var(--success) 45%, var(--text-inverse)); font: 600 0.875rem/1 var(--font-mono); }
.island-nav__route { grid-column: 1 / -1; height: 0.3125rem; margin-top: 0.75rem; border-radius: var(--radius-full); background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.island-nav__route span { position: relative; display: block; width: 68%; height: 100%; border-radius: inherit; background: var(--gradient-brand); }
.island-nav__route span::after {
  content: ""; position: absolute; right: -0.3125rem; top: 50%; width: 0.625rem; height: 0.625rem; margin-top: -0.3125rem; border-radius: 50%;
  background: var(--text-inverse); box-shadow: 0 0 0 3px color-mix(in srgb, var(--primary-2) 45%, transparent), 0 0 12px var(--primary-2);
}

.island-nav__grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.5rem; margin: 0; padding: 0; list-style: none; }
.island-nav[data-state="expanded"] .island-nav__grid li { animation: island-nav-tile var(--dur-4) var(--ease-out) calc(120ms + var(--island-nav-i) * 35ms) both; }
.island-nav__link {
  display: grid; justify-items: center; gap: 0.375rem; padding: 0.75rem 0.25rem 0.625rem; border-radius: 1rem;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse);
  color: var(--text-inverse-muted); font-size: 0.75rem; font-weight: 600; text-decoration: none;
  transition: background-color var(--dur-2), color var(--dur-2), scale var(--dur-3) var(--ease-spring);
}
.island-nav__link svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.island-nav__link:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); color: var(--text-inverse); }
.island-nav__link:active { scale: 0.95; }
.island-nav__link[aria-current="page"] {
  color: var(--text-inverse);
  background: linear-gradient(160deg, color-mix(in srgb, var(--primary) 55%, transparent), color-mix(in srgb, var(--primary-2) 30%, transparent));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 50%, transparent), var(--highlight-inverse);
}

.island-nav__actions { display: flex; gap: 0.5rem; }
.island-nav__cta {
  flex: 1; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; height: 3rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: 0 10px 30px -12px color-mix(in srgb, var(--primary) 90%, transparent);
  transition: scale var(--dur-3) var(--ease-spring);
}
.island-nav__cta svg, .island-nav__call svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.island-nav__cta svg { transition: translate var(--dur-3) var(--ease-spring); }
.island-nav__cta:hover svg { translate: 3px 0; }
.island-nav__cta:active, .island-nav__call:active { scale: 0.96; }
.island-nav__call {
  flex: none; display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 50%;
  background: color-mix(in srgb, var(--success) 80%, var(--surface-deep)); color: var(--text-inverse); box-shadow: var(--highlight-inverse);
  transition: scale var(--dur-3) var(--ease-spring);
}
.island-nav__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Reduced motion: drop the ping, star pop and tile stagger (the zero-length failsafe stays) */
@media (prefers-reduced-motion: reduce) {
  .island-nav__dot::after, .island-nav__stars svg, .island-nav__grid li { animation: none !important; }
}

@keyframes island-nav-ping { to { transform: scale(2.8); opacity: 0; } }
@keyframes island-nav-star { from { opacity: 0; scale: 0.3; rotate: -40deg; } }
@keyframes island-nav-tile { from { opacity: 0; translate: 0 0.5rem; scale: 0.96; } }
@keyframes island-nav-unfold { to { width: min(22.5rem, 100%); height: auto; border-radius: 2rem; } }
@keyframes island-nav-reveal { to { opacity: 1; filter: none; translate: 0 0; visibility: visible; } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const native = CSS.supports('interpolate-size', 'allow-keywords');
let uid = 0;

document.querySelectorAll('[data-island-nav]').forEach((root) => {
  const shell = root.querySelector('.island-nav__shell');
  const toggle = root.querySelector('.island-nav__toggle');
  const body = root.querySelector('.island-nav__body');
  const status = root.querySelector('.island-nav__status');
  const live = root.querySelector('[role="status"]');
  const id = `island-nav-${++uid}`;
  let anim = null;

  // Enhance the static card into a compact island with a disclosure button
  body.id = `${id}-menu`;
  status.id = `${id}-status`;
  toggle.setAttribute('aria-controls', body.id);
  toggle.setAttribute('aria-describedby', status.id);
  toggle.hidden = false;
  body.inert = true;
  root.dataset.state = 'compact';
  root.classList.add('island-nav--js');
  root.classList.toggle('island-nav--fallback', !native);

  // Morph between compact, activity and expanded. CSS handles it where interpolate-size exists;
  // elsewhere we measure the old and new natural sizes and spring between them.
  const setState = (state) => {
    if (root.dataset.state === state) return;
    const from = shell.getBoundingClientRect();
    anim?.cancel();
    root.dataset.state = state;
    body.inert = state !== 'expanded';
    toggle.setAttribute('aria-expanded', String(state === 'expanded'));
    if (native || reduce.matches) return;
    const to = shell.getBoundingClientRect();
    const css = getComputedStyle(root);
    let easing = css.getPropertyValue('--ease-spring').trim();
    if (!CSS.supports('transition-timing-function', easing)) easing = 'ease-out';
    anim = shell.animate(
      { width: [`${from.width}px`, `${to.width}px`], height: [`${from.height}px`, `${to.height}px`] },
      { duration: parseFloat(css.getPropertyValue('--dur-4')) || 560, easing },
    );
  };

  toggle.addEventListener('click', () => setState(root.dataset.state === 'expanded' ? 'compact' : 'expanded'));

  // Escape folds the island and returns focus to the toggle; outside taps and tabbing away fold it too
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape' || root.dataset.state !== 'expanded') return;
    const inside = root.contains(document.activeElement);
    setState('compact');
    if (inside) toggle.focus();
  });
  document.addEventListener('pointerdown', (e) => {
    if (root.dataset.state === 'expanded' && !shell.contains(e.target)) setState('compact');
  }, { passive: true });
  root.addEventListener('focusout', (e) => {
    if (root.dataset.state === 'expanded' && e.relatedTarget && !shell.contains(e.relatedTarget)) setState('compact');
  });

  // One-time live activity a few seconds in: announce politely, show it, fold back.
  // Skipped under reduced motion.
  if (!reduce.matches) {
    setTimeout(() => {
      if (root.dataset.state !== 'compact') return;
      live.textContent = 'New five-star review from Dana R. in Westlake';
      setState('activity');
      setTimeout(() => { if (root.dataset.state === 'activity') setState('compact'); }, 3800);
    }, 2600);
  }

  // Demo only (data-island-nav-demo): links mark the current page and fold the island instead of navigating
  if (root.hasAttribute('data-island-nav-demo')) {
    const links = [...root.querySelectorAll('.island-nav__link')];
    body.addEventListener('click', (e) => {
      const link = e.target.closest('a[href^="/"]');
      if (!link) return;
      e.preventDefault();
      if (links.includes(link)) links.forEach((other) => (other === link ? other.setAttribute('aria-current', 'page') : other.removeAttribute('aria-current')));
      setState('compact');
      toggle.focus();
    });
  }
});
```

## Notes

- **Accessibility:** this is the APG disclosure pattern. The island's toggle is a real `<button>` named "Menu", with `aria-expanded` and `aria-controls`, and the live status as its `aria-describedby`. Its `::after` stretches over the whole pill, so the entire island is the 44px-tall target. The collapsed card is `inert` and `visibility: hidden`. Escape folds the island and returns focus to the toggle; a tap outside (the scrim) or tabbing out of the card also folds it. The new review is announced once through a polite `role="status"` region; the visual alert is `aria-hidden`.
- **Morph:** with `interpolate-size: allow-keywords` (Chromium 129+), CSS springs `width: fit-content` → length and `height: 2.75rem` → `auto`. Other browsers get the same spring through a measured Web Animations size tween that reads `--ease-spring` and `--dur-4` from the tokens. The open body is `width: 0; min-width: 100%`, so it never widens the compact pill, and it scrolls if the viewport is short.
- **Timing:** the ping runs three times (about 5s) and stops, so it needs no pause control. The live activity plays once, about 2.6s after load, for about 3.8s. Under reduced motion the morph is instant, and the ping, star pop and live activity are skipped.
- **No JS:** with scripting off, the island renders as the open card in the page flow: status row, ETA, nav grid and actions, all usable. With scripting on, `@media (scripting: enabled)` paints the compact pill from the first frame, so the card never flashes. If the script then fails to run, a zero-length CSS failsafe unfolds the card after 2s.
- **Contrast** on `--surface-deep`: body text `--text-inverse` is about 18:1, secondary `--text-inverse-muted` 7.7:1, and the green status text (45% `--success` mixed with `--text-inverse`) about 9:1. "Book now" is `--text-main` on white (14.6:1).
- **Wiring:** place the island as the first child of the page wrapper and give the first content block about 5.5rem of top padding (the demo does this inside the `scripting: enabled` block). Add `viewport-fit=cover` so it clears the notch via `safe-area-inset-top`. Drop `data-island-nav-demo` so links navigate, and feed live status text into `.island-nav__status`.
