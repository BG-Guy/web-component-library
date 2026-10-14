# Gesture Drawer

A side drawer that tracks your finger: swipe in from the left edge or grab the open drawer, and it follows the pointer 1:1, rubber-banding past fully open while a deep scrim fades and the page recedes (a slight push and scale) in step. On release, position and fling velocity decide open or closed, and a real spring carries that velocity into the settle (you can even catch the drawer mid-flight); the burger opens it too. Inside are a brand header with live opening status, a nav list with icons and counts, a promo card and footer actions. Built for phones (85% of the screen, safe-area aware), it works the same with a mouse. Depends on `tokens/variables.css`.

**Motion:** 1:1 drag on transforms · rubber-band overshoot · scrim and page push/scale tied to progress · velocity-aware spring settle (rAF, damping ratio about 0.73) · nav rows parallax-slide with the drawer · press feedback on `--ease-spring`.

## HTML

```html
<div class="swipe-drawer" data-swipe-drawer data-swipe-drawer-demo>
  <div class="swipe-drawer__panel" id="swipe-drawer-panel">
    <header class="swipe-drawer__head">
      <span class="swipe-drawer__mark" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M3 10.5 12 3l9 7.5" /><path d="M5.5 9v11a1 1 0 0 0 1 1H10v-6h4v6h3.5a1 1 0 0 0 1-1V9" /></svg>
      </span>
      <div class="swipe-drawer__brand">
        <h2 class="swipe-drawer__title" id="swipe-drawer-title">Brand<span class="swipe-drawer__sr"> menu</span></h2>
        <p class="swipe-drawer__status"><span class="swipe-drawer__led" aria-hidden="true"></span>Open now · until 8 pm</p>
      </div>
      <button class="swipe-drawer__close" type="button" aria-label="Close menu" hidden>
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
      </button>
    </header>

    <div class="swipe-drawer__scroll">
      <nav aria-label="Main">
        <ul class="swipe-drawer__list" role="list">
          <li style="--swipe-drawer-i: 0"><a class="swipe-drawer__link" href="/" aria-current="page">
            <span class="swipe-drawer__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M3 10.5 12 3l9 7.5" /><path d="M5.5 9v11a1 1 0 0 0 1 1H10v-6h4v6h3.5a1 1 0 0 0 1-1V9" /></svg></span>
            <span class="swipe-drawer__label">Home</span>
          </a></li>
          <li style="--swipe-drawer-i: 1"><a class="swipe-drawer__link" href="/services">
            <span class="swipe-drawer__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z" /></svg></span>
            <span class="swipe-drawer__label">Services</span><span class="swipe-drawer__count">14</span>
          </a></li>
          <li style="--swipe-drawer-i: 2"><a class="swipe-drawer__link" href="/projects">
            <span class="swipe-drawer__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><rect x="3" y="3" width="18" height="18" rx="3" /><circle cx="9" cy="9" r="2" /><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21" /></svg></span>
            <span class="swipe-drawer__label">Projects</span><span class="swipe-drawer__count">48</span>
          </a></li>
          <li style="--swipe-drawer-i: 3"><a class="swipe-drawer__link" href="/reviews">
            <span class="swipe-drawer__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg></span>
            <span class="swipe-drawer__label">Reviews</span><span class="swipe-drawer__count">1.2k</span>
          </a></li>
          <li style="--swipe-drawer-i: 4"><a class="swipe-drawer__link" href="/messages">
            <span class="swipe-drawer__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z" /></svg></span>
            <span class="swipe-drawer__label">Messages</span><span class="swipe-drawer__count swipe-drawer__count--new">2 new</span>
          </a></li>
          <li style="--swipe-drawer-i: 5"><a class="swipe-drawer__link" href="/areas">
            <span class="swipe-drawer__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z" /><circle cx="12" cy="10" r="2.5" /></svg></span>
            <span class="swipe-drawer__label">Areas we cover</span><span class="swipe-drawer__count">6</span>
          </a></li>
        </ul>
      </nav>

      <div class="swipe-drawer__promo">
        <p class="swipe-drawer__promo-tag">Winter offer</p>
        <h3 class="swipe-drawer__promo-title">Boiler check, $79</h3>
        <p class="swipe-drawer__promo-text">Book before 30 Nov in Westlake, Northside or Riverside.</p>
        <a class="swipe-drawer__promo-link" href="/offers/boiler-check">
          Claim the offer
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
      </div>
    </div>

    <footer class="swipe-drawer__foot">
      <a class="swipe-drawer__action swipe-drawer__action--primary" href="tel:+15555550123">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
        <span class="swipe-drawer__sr">Call </span>(555) 555-0123
      </a>
      <a class="swipe-drawer__action" href="mailto:hello@example.com">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2" /><path d="m3 7 9 6 9-6" /></svg>
        Email
      </a>
    </footer>
  </div>

  <div class="swipe-drawer__page">
    <header class="swipe-drawer-demo__bar">
      <button class="swipe-drawer__burger" type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="swipe-drawer-panel" hidden>
        <span class="swipe-drawer__sr">Menu</span>
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M4 7h16M4 12h10M4 17h16" /></svg>
      </button>
      <span class="swipe-drawer-demo__brand">Brand</span>
      <a class="swipe-drawer-demo__call" href="tel:+15555550123" aria-label="Call (555) 555-0123">
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
      </a>
    </header>

    <div class="swipe-drawer-demo__body">
      <p class="swipe-drawer-demo__hint"><span aria-hidden="true"></span>Swipe in from the left edge, or tap the menu</p>
      <h2 class="swipe-drawer-demo__title">Leaks, boilers and wiring, fixed today.</h2>
      <p class="swipe-drawer-demo__lead">Licensed Springfield technicians with flat-rate prices and a 12-month guarantee on every job.</p>
      <div class="swipe-drawer-demo__art" aria-hidden="true"><span></span><span></span></div>
      <ul class="swipe-drawer-demo__cards" role="list">
        <li><strong>Emergency call-outs</strong><span>On site in 60 minutes across Westlake and Northside.</span></li>
        <li><strong>Boiler servicing</strong><span>Annual checks, repairs and same-week installs.</span></li>
        <li><strong>Electrical</strong><span>Fuse boards, sockets, lighting and EV chargers.</span></li>
      </ul>
    </div>
  </div>

  <span class="swipe-drawer__edge" aria-hidden="true"></span>
  <span class="swipe-drawer__scrim" aria-hidden="true"></span>
</div>
```

## CSS

```css
/* One progress value (0 closed → 1 open) is written to the panel, scrim and page.
   It doesn't inherit, so a drag frame never restyles the whole page tree. */
@property --swipe-drawer-p { syntax: "<number>"; inherits: false; initial-value: 0; }

.swipe-drawer { overflow-x: clip; color: var(--text-main); font-family: var(--font-sans); }
.swipe-drawer.is-dragging { cursor: grabbing; -webkit-user-select: none; user-select: none; }
html:has(.swipe-drawer.is-open) { overflow: hidden; }

/* Demo page */
.swipe-drawer__page {
  min-height: 100vh; min-height: 100svh;
  background: radial-gradient(28rem 18rem at 100% 0%, color-mix(in srgb, var(--primary) 12%, transparent), transparent 70%), var(--surface-muted);
}
.swipe-drawer-demo__bar {
  position: sticky; top: 0; z-index: var(--z-sticky); display: flex; align-items: center; gap: var(--space-sm);
  height: calc(3.75rem + env(safe-area-inset-top, 0px)); padding: env(safe-area-inset-top, 0px) var(--gutter) 0;
  background: color-mix(in srgb, var(--surface-muted) 88%, transparent); box-shadow: inset 0 -1px 0 var(--border-subtle);
}
@supports (backdrop-filter: blur(1px)) {
  .swipe-drawer-demo__bar { background: color-mix(in srgb, var(--surface-muted) 70%, transparent); backdrop-filter: blur(var(--blur-md)) saturate(1.4); }
}
.swipe-drawer-demo__brand { flex: 1; font: 600 1.0625rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.swipe-drawer-demo__call, .swipe-drawer__burger {
  flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%;
  background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  cursor: pointer; transition: scale var(--dur-3) var(--ease-spring);
}
.swipe-drawer__burger[hidden] { display: none; }
.swipe-drawer-demo__call:active, .swipe-drawer__burger:active { scale: 0.92; }
.swipe-drawer-demo__call svg, .swipe-drawer__burger svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.swipe-drawer-demo__body { max-width: min(var(--container-max), 40rem); margin-inline: auto; padding: var(--space-lg) var(--gutter) var(--space-2xl); }
.swipe-drawer-demo__hint {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.4375rem 0.75rem; border-radius: var(--radius-full);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle); color: var(--text-muted); font: 500 0.75rem/1.2 var(--font-mono);
}
.swipe-drawer-demo__hint span { width: 1.25rem; height: 0.375rem; border-radius: var(--radius-full); background: linear-gradient(90deg, var(--primary), transparent); }
.swipe-drawer-demo__title { margin: 1.25rem 0 0; font: 600 clamp(1.875rem, 1.3rem + 2.4vw, 2.75rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.swipe-drawer-demo__lead { max-width: 32rem; margin: 0.875rem 0 0; color: var(--text-muted); line-height: 1.55; }
.swipe-drawer-demo__art {
  position: relative; height: 10rem; margin-top: var(--space-xl); overflow: hidden; border-radius: var(--radius-2xl);
  background:
    radial-gradient(70% 90% at 85% 10%, color-mix(in srgb, var(--primary-2) 75%, transparent), transparent 70%),
    radial-gradient(70% 90% at 10% 100%, color-mix(in srgb, var(--primary) 85%, transparent), transparent 70%),
    var(--surface-deep);
  box-shadow: var(--shadow-xl);
}
.swipe-drawer-demo__art span { position: absolute; border-radius: 50%; box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 22%, transparent); }
.swipe-drawer-demo__art span:first-child { left: 58%; top: 18%; width: 9rem; aspect-ratio: 1; }
.swipe-drawer-demo__art span:last-child { left: 70%; top: 42%; width: 4rem; aspect-ratio: 1; background: color-mix(in srgb, var(--surface-light) 10%, transparent); }
.swipe-drawer-demo__cards { display: grid; gap: 0.75rem; margin: var(--space-lg) 0 0; padding: 0; list-style: none; }
.swipe-drawer-demo__cards li { display: grid; gap: 0.25rem; padding: 1rem 1.125rem; border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-sm); }
.swipe-drawer-demo__cards strong { font: 600 1rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.swipe-drawer-demo__cards span { color: var(--text-muted); font-size: 0.875rem; line-height: 1.5; }

/* Panel. Without JS it's a static nav section at the top of the page. */
.swipe-drawer__panel {
  --swipe-drawer-k: var(--swipe-drawer-p); /* inheritable copy for the panel's own children */
  position: relative; box-sizing: border-box; display: flex; flex-direction: column;
  width: min(100% - 2 * var(--gutter), 40rem); margin: var(--space-md) auto 0; border-radius: var(--radius-2xl);
  background: linear-gradient(180deg, color-mix(in srgb, var(--primary) 5%, var(--surface-light)), var(--surface-light) 9rem);
  box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-lg);
}
.swipe-drawer__head { flex: none; display: flex; align-items: center; gap: 0.75rem; padding: var(--space-md) var(--space-md) var(--space-sm) 1.25rem; }
.swipe-drawer__mark { flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-lg); background: var(--gradient-brand); color: var(--text-inverse); box-shadow: var(--highlight), 0 10px 20px -10px var(--primary); }
.swipe-drawer__mark svg, .swipe-drawer__icon svg, .swipe-drawer__close svg, .swipe-drawer__action svg, .swipe-drawer__promo-link svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.swipe-drawer__brand { flex: 1; min-width: 0; }
.swipe-drawer__title { margin: 0; font: 600 1.125rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.swipe-drawer__status { display: flex; align-items: center; gap: 0.375rem; margin: 0.375rem 0 0; color: var(--success); font: 500 0.75rem/1 var(--font-mono); }
.swipe-drawer__led { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 18%, transparent); }
.swipe-drawer__close {
  flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-muted); color: var(--text-muted);
  transition: background-color var(--dur-2), color var(--dur-2), rotate var(--dur-3) var(--ease-spring);
}
.swipe-drawer__close[hidden] { display: none; }
.swipe-drawer__close:hover { background: var(--border-subtle); color: var(--text-main); rotate: 90deg; }

.swipe-drawer__scroll { flex: 1; min-height: 0; overflow-y: auto; overscroll-behavior: contain; padding: var(--space-sm) 0.75rem var(--space-md); }
.swipe-drawer__list { display: grid; gap: 0.125rem; margin: 0; padding: 0; list-style: none; }
.swipe-drawer__link {
  display: flex; align-items: center; gap: 0.75rem; min-height: 3rem; padding: 0.375rem 0.75rem 0.375rem 0.5rem; border-radius: var(--radius-lg);
  color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: background-color var(--dur-2), scale var(--dur-3) var(--ease-spring);
}
.swipe-drawer__link:hover { background: var(--surface-muted); }
.swipe-drawer__link:active { scale: 0.98; }
.swipe-drawer__icon {
  flex: none; display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 0.75rem;
  background: color-mix(in srgb, var(--primary) 9%, var(--surface-light)); color: var(--primary);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 12%, transparent);
}
.swipe-drawer__label { flex: 1; min-width: 0; }
.swipe-drawer__count { flex: none; padding: 0.25rem 0.5rem; border-radius: var(--radius-full); background: var(--surface-muted); color: var(--text-muted); font: 600 0.75rem/1 var(--font-mono); }
.swipe-drawer__count--new { background: color-mix(in srgb, var(--danger) 10%, var(--surface-light)); color: color-mix(in srgb, var(--danger) 80%, var(--text-main)); }
.swipe-drawer__link[aria-current="page"] { background: color-mix(in srgb, var(--primary) 8%, var(--surface-light)); }
.swipe-drawer__link[aria-current="page"] .swipe-drawer__icon { background: var(--gradient-brand); color: var(--text-inverse); box-shadow: var(--highlight), 0 8px 16px -8px var(--primary); }

.swipe-drawer__promo {
  position: relative; overflow: hidden; margin-top: var(--space-md); padding: 1.125rem; border-radius: var(--radius-xl); color: var(--text-inverse);
  background:
    radial-gradient(80% 90% at 100% 0%, color-mix(in srgb, var(--primary-2) 60%, transparent), transparent 70%),
    radial-gradient(70% 80% at 0% 100%, color-mix(in srgb, var(--primary) 70%, transparent), transparent 70%),
    var(--surface-deep);
  box-shadow: var(--highlight-inverse), var(--shadow-lg);
}
.swipe-drawer__promo::after {
  content: ""; position: absolute; right: -2.5rem; top: -2.5rem; width: 8rem; aspect-ratio: 1; border-radius: 50%; pointer-events: none;
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-inverse) 18%, transparent), 0 0 0 1.25rem color-mix(in srgb, var(--text-inverse) 4%, transparent);
}
.swipe-drawer__promo-tag { margin: 0; color: color-mix(in srgb, var(--accent) 70%, var(--text-inverse)); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.swipe-drawer__promo-title { margin: 0.5rem 0 0; font: 600 1.375rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.swipe-drawer__promo-text { max-width: 16rem; margin: 0.375rem 0 0; font-size: 0.8125rem; line-height: 1.45; }
.swipe-drawer__promo-link { display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; margin-top: 0.25rem; color: var(--text-inverse); font-size: 0.875rem; font-weight: 600; text-decoration: none; }
.swipe-drawer__promo-link svg { transition: translate var(--dur-3) var(--ease-spring); }
.swipe-drawer__promo-link:hover svg { translate: 3px 0; }

.swipe-drawer__foot { flex: none; display: grid; grid-template-columns: 1fr auto; gap: 0.5rem; padding: 0.75rem var(--space-md) var(--space-md); box-shadow: inset 0 1px 0 var(--border-subtle); }
.swipe-drawer__action {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; height: 3rem; padding: 0 1rem; border-radius: var(--radius-full);
  background: var(--surface-muted); color: var(--text-main); font-size: 0.875rem; font-weight: 600; text-decoration: none; font-variant-numeric: tabular-nums;
  box-shadow: inset 0 0 0 1px var(--border-subtle); transition: scale var(--dur-3) var(--ease-spring), background-color var(--dur-2);
}
.swipe-drawer__action--primary { background: var(--text-main); color: var(--surface-light); box-shadow: var(--highlight-inverse), 0 10px 22px -12px color-mix(in srgb, var(--text-main) 80%, transparent); }
.swipe-drawer__action:active { scale: 0.97; }
.swipe-drawer :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }
.swipe-drawer .swipe-drawer__promo-link:focus-visible { outline-color: var(--text-inverse); }
.swipe-drawer__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Enhanced: a fixed drawer driven by --swipe-drawer-p */
.swipe-drawer__scrim, .swipe-drawer__edge { display: none; }
.swipe-drawer--js .swipe-drawer__panel {
  position: fixed; inset: 0 auto 0 0; z-index: calc(var(--z-overlay) + 1);
  width: min(85vw, 20rem); margin: 0; border-radius: 0 var(--radius-2xl) var(--radius-2xl) 0;
  padding: env(safe-area-inset-top, 0px) 0 env(safe-area-inset-bottom, 0px) env(safe-area-inset-left, 0px);
  box-shadow: 1px 0 0 var(--border-subtle), 24px 0 60px -20px color-mix(in srgb, var(--surface-deep) 45%, transparent);
  translate: calc((var(--swipe-drawer-p) - 1) * 100%) 0;
  visibility: hidden; touch-action: pan-y;
}
.swipe-drawer--js .swipe-drawer__panel::before { /* bleed that fills the gap while rubber-banding past open */
  content: ""; position: absolute; top: 0; bottom: 0; right: 100%; width: 3.5rem; background: inherit;
}
.swipe-drawer--js .swipe-drawer__list li { translate: calc((1 - min(var(--swipe-drawer-k), 1)) * (var(--swipe-drawer-i) + 2) * -0.625rem) 0; }
.swipe-drawer--js .swipe-drawer__scrim {
  display: block; position: fixed; inset: 0; z-index: var(--z-overlay); visibility: hidden; pointer-events: none; touch-action: pan-y;
  background: color-mix(in srgb, var(--surface-deep) 62%, transparent); opacity: min(var(--swipe-drawer-p), 1);
}
.swipe-drawer--js .swipe-drawer__edge { display: block; position: fixed; inset: 0 auto 0 0; z-index: var(--z-overlay); width: 0.875rem; cursor: grab; touch-action: pan-y; }
.swipe-drawer--js .swipe-drawer__edge::after {
  content: ""; position: absolute; left: 0.25rem; top: 50%; width: 0.25rem; height: 2.5rem; margin-top: -1.25rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--text-main) 20%, transparent);
  transition: opacity var(--dur-2), scale var(--dur-3) var(--ease-spring), background-color var(--dur-2);
}
.swipe-drawer--js .swipe-drawer__edge:hover::after { scale: 1.4 1.15; background: color-mix(in srgb, var(--primary) 55%, transparent); }
.swipe-drawer--js.is-active .swipe-drawer__panel, .swipe-drawer--js.is-active .swipe-drawer__scrim { visibility: visible; }
.swipe-drawer--js.is-active .swipe-drawer__edge::after { opacity: 0; }
.swipe-drawer--js.is-open .swipe-drawer__scrim { pointer-events: auto; }
/* The page recedes with the drag (origin is set to the viewport centre by JS) */
.swipe-drawer--js.is-active .swipe-drawer__page {
  translate: calc(min(var(--swipe-drawer-p), 1) * 2.5rem) 0;
  scale: calc(1 - min(var(--swipe-drawer-p), 1) * 0.06);
}

/* Reduced motion: dragging still tracks the finger, but the page no longer moves or scales */
@media (prefers-reduced-motion: reduce) {
  .swipe-drawer--js.is-active .swipe-drawer__page { translate: none; scale: none; }
}
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const STIFFNESS = 420; // spring constant, per second squared (progress units)
const DAMPING = 30;    // about 0.73 of critical: a soft settle with a hint of overshoot
let uid = 0;

document.querySelectorAll('[data-swipe-drawer]').forEach((root) => {
  const panel = root.querySelector('.swipe-drawer__panel');
  const page = root.querySelector('.swipe-drawer__page');
  const scrim = root.querySelector('.swipe-drawer__scrim');
  const edge = root.querySelector('.swipe-drawer__edge');
  const burger = root.querySelector('.swipe-drawer__burger');
  const close = root.querySelector('.swipe-drawer__close');
  const title = root.querySelector('.swipe-drawer__title');
  let progress = 0; // 0 closed … 1 open; may pass 1 while the spring overshoots
  let isOpen = false;
  let frame = 0;
  let queued = 0;
  let drag = null;

  // Enhance the static nav section into a modal drawer (unique ids per instance)
  const id = `swipe-drawer-${++uid}`;
  panel.id = `${id}-panel`;
  title.id = `${id}-title`;
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-modal', 'true');
  panel.setAttribute('aria-labelledby', title.id);
  burger.setAttribute('aria-controls', panel.id);
  burger.hidden = false;
  close.hidden = false;
  panel.inert = true;
  root.classList.add('swipe-drawer--js');

  // Paint one number into the three layers; overshoot past open is rubber-banded
  const render = () => {
    const over = progress - 1;
    const shown = over > 0 ? 1 + over / (1 + 6 * over) : Math.max(0, progress);
    for (const el of [panel, scrim, page]) el.style.setProperty('--swipe-drawer-p', shown.toFixed(4));
  };
  const setActive = (on) => {
    if (on && !root.classList.contains('is-active')) page.style.transformOrigin = `100% ${innerHeight / 2 - page.getBoundingClientRect().top}px`;
    root.classList.toggle('is-active', on);
  };
  // Logical state flips as soon as the outcome is known: inert, ARIA, focus
  const setOpen = (open) => {
    if (open === isOpen) return;
    isOpen = open;
    root.classList.toggle('is-open', open);
    page.inert = open;
    panel.inert = !open;
    burger.setAttribute('aria-expanded', String(open));
    (open ? close : burger).focus({ preventScroll: true });
  };

  // Spring to 0 or 1, starting from the release velocity (progress units per second)
  const settle = (target, velocity = 0) => {
    cancelAnimationFrame(frame);
    setOpen(target === 1);
    let v = velocity;
    let last = performance.now();
    const finish = () => {
      progress = target;
      render();
      if (target === 0) setActive(false);
    };
    if (reduce.matches) return finish();
    const step = (now) => {
      const dt = Math.min((now - last) / 1000, 1 / 30);
      last = now;
      v += (-STIFFNESS * (progress - target) - DAMPING * v) * dt;
      progress += v * dt;
      if (Math.abs(progress - target) < 0.002 && Math.abs(v) < 0.02) return finish();
      render();
      frame = requestAnimationFrame(step);
    };
    frame = requestAnimationFrame(step);
  };

  burger.addEventListener('click', () => { setActive(true); settle(1); });
  close.addEventListener('click', () => settle(0));
  scrim.addEventListener('click', () => { if (isOpen) settle(0); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && isOpen) settle(0); });

  // Gestures: an edge swipe opens; the open panel or scrim can be dragged shut.
  // Pointer capture keeps the drag alive anywhere on screen; grabbing mid-flight stops the spring.
  const begin = (e) => {
    cancelAnimationFrame(frame);
    drag.live = true;
    drag.x = e.clientX;
    drag.from = Math.min(progress, 1);
    root.setPointerCapture(e.pointerId);
    root.classList.add('is-dragging');
    setActive(true);
  };
  root.addEventListener('pointerdown', (e) => {
    if (!e.isPrimary || e.button > 0) return;
    const fromEdge = !isOpen && e.target === edge;
    if (!fromEdge && !(isOpen && (panel.contains(e.target) || e.target === scrim))) return;
    drag = { id: e.pointerId, x: e.clientX, y: e.clientY, from: progress, live: false, samples: [] };
    if (fromEdge) begin(e);
  });
  root.addEventListener('pointermove', (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    if (!drag.live) {
      const dx = Math.abs(e.clientX - drag.x);
      if (dx < 8 || dx < Math.abs(e.clientY - drag.y)) return; // wait for a clear sideways intent
      begin(e);
    }
    drag.samples.push([e.clientX, e.timeStamp]);
    if (drag.samples.length > 6) drag.samples.shift();
    progress = drag.from + (e.clientX - drag.x) / panel.offsetWidth; // 1:1 with the finger
    queued ||= requestAnimationFrame(() => { queued = 0; render(); });
  }, { passive: true });
  const release = (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    const { live, samples } = drag;
    drag = null;
    root.classList.remove('is-dragging');
    if (!live) return;
    // A fling beats position: velocity over the last few samples, in panel widths per second
    const [x0, t0] = samples[0] ?? [0, 0];
    const [x1, t1] = samples[samples.length - 1] ?? [0, 0];
    const v = t1 > t0 ? ((x1 - x0) / (t1 - t0)) * 1000 / panel.offsetWidth : 0;
    settle(Math.abs(v) > 1.2 ? Number(v > 0) : Number(progress > 0.5), v);
  };
  root.addEventListener('pointerup', release);
  root.addEventListener('pointercancel', release);

  // Demo only (data-swipe-drawer-demo): links mark the current page and close the drawer
  if (root.hasAttribute('data-swipe-drawer-demo')) {
    const links = [...panel.querySelectorAll('a[href^="/"]')];
    links.forEach((link) => link.addEventListener('click', (e) => {
      e.preventDefault();
      if (link.classList.contains('swipe-drawer__link')) {
        links.forEach((other) => (other === link ? other.setAttribute('aria-current', 'page') : other.removeAttribute('aria-current')));
      }
      settle(0);
    }));
  }
});
```

## Notes

- **Accessibility:** when enhanced, the panel becomes `role="dialog"` with `aria-modal="true"`, named by its heading ("Brand menu"). While it's open the page is `inert`, so focus and the reading cursor stay in the drawer. Focus lands on the close button and returns to the burger (`aria-haspopup="dialog"`, `aria-expanded`) on close. Escape, the close button and a tap on the scrim all close it. Every control is at least 44px, and nav rows are 48px.
- **Gesture model:** Pointer Events with pointer capture on the root, `touch-action: pan-y` (vertical scrolling still belongs to the browser), an 8px sideways slop before a drag claims the pointer, and transforms only. Release velocity over the last six samples beats position: a fling over 1.2 panel-widths per second opens or closes regardless of distance. The spring is a small damped integrator seeded with that velocity, and grabbing mid-flight cancels it. Overshoot rubber-bands, and a 3.5rem bleed behind the panel hides the gap.
- **Reduced motion:** no spring (it snaps to open or closed on release) and no page push or scale. Dragging still follows the finger 1:1, and the scrim still tracks progress.
- **No JS:** the panel renders as a static nav section at the top of the page: brand, status, the full link list with counts, the promo and both contact actions. The burger, close button, edge zone and scrim stay hidden.
- **Contrast:** promo text is `--text-inverse` over `--surface-deep` with brand glows (at least 8:1 at the darkest glow), and the tag is about 4.9:1. Counts are `--text-muted` on `--surface-muted` (4.6:1); "2 new" uses a darkened `--danger` on its tint (5.4:1).
- **Wiring:** wrap your page content in `.swipe-drawer__page` and keep the panel, edge and scrim as siblings inside `.swipe-drawer`. Anything outside the root, such as a site footer, must also go `inert` while the drawer is open. Add `viewport-fit=cover` for the safe-area padding. On iOS and Android, the system back-swipe owns the screen's outermost edge, so the 14px edge zone is a convenience and the burger stays the primary entry. Drop `data-swipe-drawer-demo` so links navigate.
