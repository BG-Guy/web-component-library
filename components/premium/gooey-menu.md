# Gooey Action Menu

A floating action button for the actions people actually want on a phone: call, text, get a quote, directions. Tapping the plus squeezes four brand-gradient droplets out of the button. They stretch like a column of liquid, pinch off one by one and settle in a stack, and a label pill slides out beside each one. Closing pulls them back in, and they merge into the button again. The goo is an SVG filter applied only to a layer of plain circles; the real links ride on top, so their icons and text stay crisp. It works the same on phones and desktop, anchored bottom-right inside the safe area. Depends on `tokens/variables.css`.

**Motion:** droplet ooze along a stretched column (`--dur-5` + `--ease-spring`, reverse `--stagger`) · button swell and squish on open (`--ease-out`/`--ease-spring`) · plus spins into × (`--ease-spring`) · label pills slide out once settled (`--dur-4` + `--ease-out`) · scrim fade with backdrop blur · merge back on close (`--dur-4` + `--ease-in-out`).

## HTML

```html
<div class="gooey-menu-demo">
  <header class="gooey-menu-demo__bar">
    <a class="gooey-menu-demo__logo" href="#">
      <span class="gooey-menu-demo__mark" aria-hidden="true"></span>Brand
    </a>
    <p class="gooey-menu-demo__status"><span class="gooey-menu-demo__dot" aria-hidden="true"></span>Open until 8 pm</p>
  </header>

  <main class="gooey-menu-demo__page">
    <p class="gooey-menu-demo__eyebrow">Plumbing &amp; heating · Springfield</p>
    <h2 class="gooey-menu-demo__title">Fixed today. Guaranteed for a year.</h2>
    <p class="gooey-menu-demo__lead">Licensed local plumbers, upfront prices and a two-hour arrival window. Tap the plus to call, text or get a quote.</p>

    <section class="gooey-menu-demo__card" aria-labelledby="gooey-menu-slots">
      <div class="gooey-menu-demo__card-head">
        <h3 id="gooey-menu-slots">Next available</h3>
        <span>Westlake · Northside · Riverside</span>
      </div>
      <ul class="gooey-menu-demo__slots" role="list">
        <li><span>Today</span><strong>2–4 pm</strong><em class="gooey-menu-demo__low">2 left</em></li>
        <li><span>Today</span><strong>4–6 pm</strong><em>Open</em></li>
        <li><span>Wed 15</span><strong>8–10 am</strong><em>Open</em></li>
      </ul>
    </section>
    <p class="gooey-menu-demo__proof"><strong>4.9/5</strong> from 1,200+ Springfield homeowners</p>
  </main>

  <div class="gooey-menu" data-gooey-menu>
    <div class="gooey-menu__scrim" aria-hidden="true"></div>

    <!-- Goo layer: plain circles only, run through the SVG filter -->
    <div class="gooey-menu__goo" aria-hidden="true">
      <span class="gooey-menu__core"></span>
      <span class="gooey-menu__drop" style="--gooey-menu-i: 0"></span>
      <span class="gooey-menu__drop" style="--gooey-menu-i: 1"></span>
      <span class="gooey-menu__drop" style="--gooey-menu-i: 2"></span>
      <span class="gooey-menu__drop" style="--gooey-menu-i: 3"></span>
    </div>

    <button class="gooey-menu__fab" type="button" aria-expanded="false" aria-controls="gooey-menu-list" aria-label="Quick actions">
      <svg class="gooey-menu__plus" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg>
    </button>

    <!-- Real links: unfiltered, at the same positions as the circles -->
    <ul class="gooey-menu__list" id="gooey-menu-list" role="list" aria-label="Quick actions">
      <li class="gooey-menu__item" style="--gooey-menu-i: 0">
        <a class="gooey-menu__action" href="tel:+15555550123">
          <span class="gooey-menu__label"><strong>Call</strong><small>(555) 555-0123</small></span>
          <span class="gooey-menu__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg></span>
        </a>
      </li>
      <li class="gooey-menu__item" style="--gooey-menu-i: 1">
        <a class="gooey-menu__action" href="sms:+15555550123">
          <span class="gooey-menu__label"><strong>Text</strong><small>Replies in ~5 min</small></span>
          <span class="gooey-menu__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2zM8 9h8M8 13h5" /></svg></span>
        </a>
      </li>
      <li class="gooey-menu__item" style="--gooey-menu-i: 2">
        <a class="gooey-menu__action" href="#quote">
          <span class="gooey-menu__label"><strong>Get a quote</strong><small>Free · 2 minutes</small></span>
          <span class="gooey-menu__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8zM14 3v5h5M9 13h6M9 17h4" /></svg></span>
        </a>
      </li>
      <li class="gooey-menu__item" style="--gooey-menu-i: 3">
        <a class="gooey-menu__action" href="https://maps.google.com/?q=Springfield">
          <span class="gooey-menu__label"><strong>Directions</strong><small>Westlake depot</small></span>
          <span class="gooey-menu__icon"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M3 11 22 2l-9 19-2-8z" /></svg></span>
        </a>
      </li>
    </ul>

    <svg class="gooey-menu__defs" width="0" height="0" aria-hidden="true" focusable="false">
      <filter id="gooey-menu-goo" x="-50%" y="-50%" width="200%" height="200%" color-interpolation-filters="sRGB">
        <feGaussianBlur in="SourceGraphic" stdDeviation="9" result="blur" />
        <feColorMatrix in="blur" mode="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 22 -10" result="goo" />
        <feComposite in="SourceGraphic" in2="goo" operator="atop" />
      </filter>
    </svg>
  </div>
</div>
```

## CSS

```css
/* Demo page: light, with a faint wash of brand light */
.gooey-menu-demo {
  min-height: 100vh; min-height: 100svh; color: var(--text-main); font-family: var(--font-sans);
  background:
    radial-gradient(40rem 24rem at 100% 0%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%),
    radial-gradient(32rem 22rem at 0% 100%, color-mix(in srgb, var(--primary-2) 8%, transparent), transparent 70%),
    var(--surface-muted);
}
.gooey-menu-demo__bar { display: flex; align-items: center; justify-content: space-between; gap: var(--space-md); max-width: var(--container-max); margin-inline: auto; padding: var(--space-md) var(--gutter); }
.gooey-menu-demo__logo { display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.75rem; color: var(--text-main); font: 600 1.125rem var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none; }
.gooey-menu-demo__mark { width: 1.25rem; height: 1.25rem; border-radius: 50% 0 50% 50%; rotate: -45deg; background: var(--gradient-brand); box-shadow: var(--highlight), var(--shadow-glow); }
.gooey-menu-demo__status {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.75rem; border-radius: var(--radius-full);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm); color: var(--text-muted); font-size: 0.8125rem; font-weight: 500;
}
.gooey-menu-demo__dot { width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 18%, transparent); }
.gooey-menu-demo :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

.gooey-menu-demo__page { max-width: var(--container-max); margin-inline: auto; padding: clamp(2rem, 6vw, 4.5rem) var(--gutter) 7rem; }
.gooey-menu-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.gooey-menu-demo__title { max-width: 14ch; margin: 0.75rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 3.8vw, 3.75rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.gooey-menu-demo__lead { max-width: 32rem; margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.gooey-menu-demo__card { max-width: 26rem; margin-top: var(--space-xl); padding: 1.25rem; border-radius: var(--radius-2xl); background: var(--surface-light); box-shadow: var(--shadow-xl), inset 0 0 0 1px var(--border-subtle); }
.gooey-menu-demo__card-head { display: flex; flex-wrap: wrap; align-items: baseline; justify-content: space-between; gap: 0.25rem var(--space-md); }
.gooey-menu-demo__card-head h3 { margin: 0; font: 600 1rem var(--font-display); letter-spacing: var(--tracking-tight); }
.gooey-menu-demo__card-head span { color: var(--text-muted); font: 500 0.6875rem var(--font-mono); }
.gooey-menu-demo__slots { display: grid; gap: var(--space-sm); margin: var(--space-md) 0 0; padding: 0; list-style: none; }
.gooey-menu-demo__slots li { display: grid; grid-template-columns: 4.25rem 1fr auto; align-items: center; padding: 0.75rem 0.875rem; border-radius: var(--radius-lg); background: var(--surface-muted); font-size: 0.875rem; }
.gooey-menu-demo__slots span { color: var(--text-muted); }
.gooey-menu-demo__slots strong { font: 600 0.875rem var(--font-mono); }
.gooey-menu-demo__slots em { padding: 0.125rem 0.5rem; border-radius: var(--radius-full); background: color-mix(in srgb, var(--success) 10%, transparent); color: var(--success); font-size: 0.75rem; font-style: normal; font-weight: 600; }
.gooey-menu-demo__slots .gooey-menu-demo__low { background: color-mix(in srgb, var(--warning) 10%, transparent); color: var(--warning); }
.gooey-menu-demo__proof { margin: 1.25rem 0 0; color: var(--text-muted); font-size: 0.875rem; }
.gooey-menu-demo__proof strong { color: var(--text-main); }

/* Menu sizes; --gooey-menu-x/y keep the button inside the safe area */
.gooey-menu {
  --gooey-menu-fab: 3.5rem;
  --gooey-menu-bubble: 3rem;
  --gooey-menu-step: 4.25rem; /* centre to centre, far enough apart that resting drops separate */
  --gooey-menu-count: 4;
  --gooey-menu-x: max(var(--space-lg), env(safe-area-inset-right));
  --gooey-menu-y: max(var(--space-lg), env(safe-area-inset-bottom));
  max-width: var(--container-max); margin-inline: auto; padding: 0 var(--gutter) var(--space-2xl);
  font-family: var(--font-sans);
}

/* Without JS: a static stack of action pills */
.gooey-menu__list { display: grid; gap: var(--space-sm); max-width: 22rem; margin: 0; padding: 0; list-style: none; }
.gooey-menu__action {
  display: flex; flex-direction: row-reverse; justify-content: flex-end; align-items: center; gap: 0.75rem;
  padding: 0.375rem; border-radius: var(--radius-full); color: var(--text-main); text-decoration: none;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
}
.gooey-menu__action:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.gooey-menu__label { display: grid; line-height: 1.25; }
.gooey-menu__label strong { font-size: 0.9375rem; font-weight: 600; transition: color var(--dur-2); }
.gooey-menu__label small { color: var(--text-muted); font: 500 0.75rem var(--font-mono); }
.gooey-menu__icon { flex: none; display: grid; place-items: center; width: var(--gooey-menu-bubble); height: var(--gooey-menu-bubble); border-radius: 50%; background: var(--gradient-brand); color: var(--text-inverse); }
.gooey-menu__icon svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: scale var(--dur-3) var(--ease-spring); }
.gooey-menu:not(.gooey-menu--js) :is(.gooey-menu__goo, .gooey-menu__scrim) { display: none; }
.gooey-menu__defs { position: absolute; width: 0; height: 0; overflow: hidden; }

/* The button is in place from first paint, so nothing jumps while the script loads */
.gooey-menu__fab {
  position: fixed; right: var(--gooey-menu-x); bottom: var(--gooey-menu-y); z-index: var(--z-overlay);
  display: grid; place-items: center; width: var(--gooey-menu-fab); height: var(--gooey-menu-fab);
  padding: 0; border: 0; border-radius: 50%; cursor: pointer; -webkit-tap-highlight-color: transparent;
  background: var(--gradient-brand); color: var(--text-inverse); box-shadow: var(--highlight), var(--shadow-glow);
  transition: scale var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.gooey-menu__fab:hover { box-shadow: var(--highlight), 0 16px 44px -10px color-mix(in srgb, var(--primary) 75%, transparent); }
.gooey-menu__fab:active { scale: 0.92; }
.gooey-menu__fab:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.gooey-menu__plus { fill: none; stroke: currentColor; stroke-width: 2.25; stroke-linecap: round; transition: rotate var(--dur-4) var(--ease-spring); }
@media (scripting: none) { .gooey-menu__fab { display: none; } }
/* Failsafe: if the script never runs, show the static stack after 3s */
@media (scripting: enabled) {
  .gooey-menu:not(.gooey-menu--js) .gooey-menu__list { max-height: 0; overflow: hidden; visibility: hidden; animation: gooey-menu-failsafe 0s 3s forwards; }
  .gooey-menu:not(.gooey-menu--js) .gooey-menu__fab { animation: gooey-menu-failsafe-out 0s 3s forwards; }
}

/* Enhanced: a viewport layer that only catches clicks where something is shown */
.gooey-menu--js { position: fixed; inset: 0; z-index: var(--z-overlay); max-width: none; margin: 0; padding: 0; pointer-events: none; }
.gooey-menu--js .gooey-menu__fab { position: absolute; z-index: 3; pointer-events: auto; }
html:has(.gooey-menu.is-open) { overflow: hidden; }

.gooey-menu__scrim {
  position: absolute; inset: 0; pointer-events: auto;
  background: color-mix(in srgb, var(--surface-light) 60%, transparent);
  -webkit-backdrop-filter: blur(6px) saturate(1.3); backdrop-filter: blur(6px) saturate(1.3);
  opacity: 0; visibility: hidden; transition: opacity var(--dur-4) var(--ease-out), visibility 0s var(--dur-4);
}
.gooey-menu.is-open .gooey-menu__scrim { opacity: 1; visibility: visible; transition-delay: 0s; }

/* Goo layer: plain circles through the SVG filter. The drop shadow follows the merged shape */
.gooey-menu__goo {
  position: absolute; z-index: 1; width: 8rem; height: calc(var(--gooey-menu-step) * var(--gooey-menu-count) + 8rem);
  right: calc(var(--gooey-menu-x) + var(--gooey-menu-fab) / 2 - 4rem);
  bottom: calc(var(--gooey-menu-y) + var(--gooey-menu-fab) / 2 - 4rem);
  filter: url(#gooey-menu-goo) drop-shadow(0 10px 14px color-mix(in srgb, var(--primary) 30%, transparent));
  visibility: hidden; transition: visibility 0s var(--dur-4);
}
.gooey-menu.is-open .gooey-menu__goo { visibility: visible; transition-delay: 0s; }
.gooey-menu__core, .gooey-menu__drop { position: absolute; left: 50%; bottom: 4rem; border-radius: 50%; }
.gooey-menu__core {
  width: var(--gooey-menu-fab); height: var(--gooey-menu-fab); margin: 0 0 calc(var(--gooey-menu-fab) / -2) calc(var(--gooey-menu-fab) / -2);
  background: var(--gradient-brand);
}
/* Drops run from blue next to the button to teal at the top of the column */
.gooey-menu__drop {
  width: var(--gooey-menu-bubble); height: var(--gooey-menu-bubble); margin: 0 0 calc(var(--gooey-menu-bubble) / -2) calc(var(--gooey-menu-bubble) / -2);
  background: linear-gradient(160deg,
    color-mix(in oklab, var(--primary) calc(80% - var(--gooey-menu-i) * 20%), var(--primary-2)),
    color-mix(in oklab, var(--primary) calc(50% - var(--gooey-menu-i) * 14%), var(--primary-2)));
}

/* Drops and links share one motion: the column leads with its tip, pinches into drops and springs */
.gooey-menu__drop, .gooey-menu--js .gooey-menu__item {
  transform: translateY(0) scale(0.5);
  transition: transform var(--dur-4) var(--ease-in-out) calc(var(--gooey-menu-i) * var(--stagger) / 2);
}
.gooey-menu.is-open .gooey-menu__drop, .gooey-menu--js.is-open .gooey-menu__item {
  transform: translateY(calc((var(--gooey-menu-i) + 1) * var(--gooey-menu-step) * -1)) scale(1);
  transition: transform var(--dur-5) var(--ease-spring) calc((var(--gooey-menu-count) - 1 - var(--gooey-menu-i)) * var(--stagger));
}
.gooey-menu.is-open .gooey-menu__core { animation: gooey-menu-swell var(--dur-5) var(--ease-out); }
.gooey-menu.is-open .gooey-menu__fab { animation: gooey-menu-squish var(--dur-4) var(--ease-out); }
.gooey-menu.is-open .gooey-menu__plus { rotate: 135deg; }

/* Real links: anchored on the button's centre, icons ride on the drops */
.gooey-menu--js .gooey-menu__list {
  position: absolute; z-index: 2; display: block; width: 0; height: 0; max-width: none;
  right: calc(var(--gooey-menu-x) + var(--gooey-menu-fab) / 2);
  bottom: calc(var(--gooey-menu-y) + var(--gooey-menu-fab) / 2);
  visibility: hidden; transition: visibility 0s var(--dur-4);
}
.gooey-menu--js.is-open .gooey-menu__list { visibility: visible; transition-delay: 0s; }
.gooey-menu--js .gooey-menu__item {
  position: absolute; right: calc(var(--gooey-menu-bubble) / -2); bottom: calc(var(--gooey-menu-bubble) / -2);
  transform-origin: calc(100% - var(--gooey-menu-bubble) / 2) 50%;
}
.gooey-menu--js .gooey-menu__action { flex-direction: row; gap: 0.625rem; padding: 0; background: none; box-shadow: none; white-space: nowrap; pointer-events: auto; -webkit-tap-highlight-color: transparent; }
.gooey-menu--js .gooey-menu__icon { background: none; }
.gooey-menu--js .gooey-menu__label {
  padding: 0.375rem 0.875rem; border-radius: var(--radius-full); text-align: right;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-lg);
  opacity: 0; translate: 1rem 0; scale: 0.92; filter: blur(4px);
  transition: opacity var(--dur-2) var(--ease-out), translate var(--dur-2) var(--ease-out), scale var(--dur-2) var(--ease-out), filter var(--dur-2) var(--ease-out);
}
.gooey-menu--js.is-open .gooey-menu__label { opacity: 1; translate: 0 0; scale: 1; filter: none; transition-duration: var(--dur-4); transition-delay: calc(var(--dur-3) + var(--gooey-menu-i) * var(--stagger)); }
.gooey-menu--js .gooey-menu__action:hover .gooey-menu__icon svg { scale: 1.15; }
.gooey-menu--js .gooey-menu__action:hover .gooey-menu__label strong { color: var(--primary); }

@media (min-width: 768px) {
  .gooey-menu { --gooey-menu-x: max(var(--space-xl), env(safe-area-inset-right)); --gooey-menu-y: max(var(--space-xl), env(safe-area-inset-bottom)); }
}
@media (prefers-reduced-motion: reduce) {
  .gooey-menu--js.is-open .gooey-menu__fab, .gooey-menu.is-open .gooey-menu__core { animation: none; }
}

@keyframes gooey-menu-swell { 35% { scale: 1.16; } }
@keyframes gooey-menu-squish { 30% { scale: 0.88; } 65% { scale: 1.05; } }
@keyframes gooey-menu-failsafe { to { max-height: none; visibility: visible; } }
@keyframes gooey-menu-failsafe-out { to { visibility: hidden; } }
```

## JS

```js
// While open, everything outside the menu is inert (only what we changed is restored)
const inertOutside = (keep, on, store) => {
  if (!on) { store.forEach((el) => { el.inert = false; }); store.clear(); return; }
  for (let node = keep; node.parentElement && node !== document.body; node = node.parentElement) {
    for (const sib of node.parentElement.children) {
      if (sib !== node && !sib.inert) { sib.inert = true; store.add(sib); }
    }
  }
};

document.querySelectorAll('[data-gooey-menu]').forEach((root, n) => {
  const fab = root.querySelector('.gooey-menu__fab');
  const list = root.querySelector('.gooey-menu__list');
  const actions = [...list.querySelectorAll('.gooey-menu__action')];
  const inerted = new Set();
  root.classList.add('gooey-menu--js');
  if (n) list.id = `${list.id}-${n + 1}`; // unique ids for repeated instances
  fab.setAttribute('aria-controls', list.id);

  const isOpen = () => root.classList.contains('is-open');
  const onKey = (e) => { if (e.key === 'Escape') { e.preventDefault(); setOpen(false); } };
  const setOpen = (open) => {
    if (open === isOpen()) return;
    root.classList.toggle('is-open', open);
    fab.setAttribute('aria-expanded', String(open));
    inertOutside(root, open, inerted);
    document[open ? 'addEventListener' : 'removeEventListener']('keydown', onKey);
    (open ? actions[0] : fab).focus({ preventScroll: true });
  };

  fab.addEventListener('click', () => setOpen(!isOpen()));
  // Outside click: the scrim covers everything except the button and the actions
  root.querySelector('.gooey-menu__scrim').addEventListener('click', () => setOpen(false));
  list.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
});
```

## Notes

- Disclosure model: the button has `aria-expanded` and `aria-controls` and opens a labelled list of real links (`tel:`, `sms:`, quote page, maps). Opening moves focus to Call, makes everything outside the menu `inert` and locks scrolling through `html:has()`. Escape, a click on the scrim or choosing an action closes it and returns focus to the button. Closed actions are hidden with `visibility`, so they leave the tab order and the accessibility tree.
- The goo filter (`feGaussianBlur` plus an alpha-threshold `feColorMatrix`, then `feComposite atop` for clean edges) touches only `.gooey-menu__goo`, which holds plain circles. The links sit in an unfiltered layer driven by the same transforms, so text and icons stay sharp. Include the filter `<svg>` once per page. Keep `--gooey-menu-step` above about 4rem, or resting drops stay joined by a bridge.
- No JS (`@media (scripting: none)`): the button is hidden and the actions render as a static stack of pills after the content. With scripting on, the button is in place from first paint. If the module fails to run, a 3s CSS failsafe swaps the button for the static stack.
- Reduced motion: no ooze, swell or squish. Drops, icons and labels appear instantly in their resting places because the motion tokens collapse.
- Contrast: label pills are `--surface-light` with `--text-main` (14.6:1) and `--text-muted` meta (4.8:1). White icons on the drops stay above 3:1 at the tealest stop (non-text contrast). SVG filters on HTML elements work in all current engines. Without `backdrop-filter`, the scrim is a flat 60% wash.
- Adapting: add or remove matching `<li>` and drop pairs (same `--gooey-menu-i`) and update `--gooey-menu-count`. Retheme through `--primary`/`--primary-2`. On a real page, put `.gooey-menu` at the end of `<body>`: the script inerts everything outside it while open, so nothing else needs wiring.
