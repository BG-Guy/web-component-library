# Radial Quick Menu

A thumb-zone menu for phones. A deep-glass hub at the bottom centre, with a gradient ring and an aperture icon, closes like a camera shutter when pressed. Five icon buttons spring out of it along curved paths into a semicircular fan, while a translucent arc track sweeps in behind them. The highlighted item grows and its name appears inside the hub. Press and hold the hub, slide towards an item and let go to open it, like a haptic menu, or just tap. Arrow keys drive it from the keyboard. On desktop the fan is a little wider and works the same way. Depends on `tokens/variables.css`.

**Motion:** items spiral out on an arc (`--dur-5` + `--ease-spring`, `--stagger`) · conic arc-track sweep (`@property` angle, `--dur-5` + `--ease-out`) · shutter press and iris-to-× morph (`--ease-spring`) · ring spin and flash on open · highlight scale (`--dur-3` + `--ease-spring`) · hub label rise · fold back in reverse (`--dur-4` + `--ease-in-out`).

## HTML

```html
<div class="radial-menu-demo">
  <header class="radial-menu-demo__bar">
    <a class="radial-menu-demo__logo" href="#">
      <span class="radial-menu-demo__mark" aria-hidden="true"></span>Brand
    </a>
    <a class="radial-menu-demo__call" href="tel:+15555550123">(555) 555-0123</a>
  </header>

  <main class="radial-menu-demo__page">
    <p class="radial-menu-demo__eyebrow">Heating · Cooling · Plumbing</p>
    <h2 class="radial-menu-demo__title">Comfort, fixed on your schedule.</h2>
    <p class="radial-menu-demo__lead">Tap the button at the bottom, or hold it and slide to where you want to go.</p>
    <ul class="radial-menu-demo__tiles" role="list">
      <li><span class="radial-menu-demo__glyph" aria-hidden="true"></span><strong>Boiler service</strong><span>from $89</span></li>
      <li><span class="radial-menu-demo__glyph" aria-hidden="true"></span><strong>Leak repair</strong><span>from $149</span></li>
      <li><span class="radial-menu-demo__glyph" aria-hidden="true"></span><strong>AC tune-up</strong><span>from $99</span></li>
      <li><span class="radial-menu-demo__glyph" aria-hidden="true"></span><strong>Heat pumps</strong><span>Free survey</span></li>
    </ul>
  </main>

  <div class="radial-menu" data-radial-menu>
    <div class="radial-menu__scrim" aria-hidden="true"></div>

    <button class="radial-menu__hub" type="button" aria-expanded="false" aria-controls="radial-menu-nav" aria-label="Quick menu">
      <span class="radial-menu__ring" aria-hidden="true"></span>
      <svg class="radial-menu__iris" viewBox="0 0 24 24" width="28" height="28" aria-hidden="true" focusable="false"><path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zM14.3 8l5.8 9.9M9.7 8h11.5M7.4 12l5.7-9.9M9.7 16 4 6.1M14.3 16H2.8M16.6 12l-5.7 9.9" /></svg>
      <svg class="radial-menu__close" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg>
      <span class="radial-menu__readout" aria-hidden="true"></span>
    </button>

    <nav class="radial-menu__nav" id="radial-menu-nav" aria-label="Quick menu">
      <span class="radial-menu__track" aria-hidden="true"></span>
      <ul class="radial-menu__list" role="list">
        <li class="radial-menu__item" style="--radial-menu-i: 0">
          <a class="radial-menu__link" href="#">
            <span class="radial-menu__disc"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z" /></svg></span>
            <span class="radial-menu__name">Home</span>
          </a>
        </li>
        <li class="radial-menu__item" style="--radial-menu-i: 1">
          <a class="radial-menu__link" href="#services">
            <span class="radial-menu__disc"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9l-3.8 3.8z" /></svg></span>
            <span class="radial-menu__name">Services</span>
          </a>
        </li>
        <li class="radial-menu__item" style="--radial-menu-i: 2">
          <a class="radial-menu__link" href="#book">
            <span class="radial-menu__disc"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM9 15l2 2 4-4" /></svg></span>
            <span class="radial-menu__name">Book</span>
          </a>
        </li>
        <li class="radial-menu__item" style="--radial-menu-i: 3">
          <a class="radial-menu__link" href="#reviews">
            <span class="radial-menu__disc"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg></span>
            <span class="radial-menu__name">Reviews</span>
          </a>
        </li>
        <li class="radial-menu__item" style="--radial-menu-i: 4">
          <a class="radial-menu__link" href="tel:+15555550123">
            <span class="radial-menu__disc"><svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg></span>
            <span class="radial-menu__name">Call</span>
          </a>
        </li>
      </ul>
    </nav>
  </div>
</div>
```

## CSS

```css
@property --radial-menu-sweep { syntax: "<angle>"; inherits: false; initial-value: 0deg; }

/* Demo page: light, with brand light pooling where the menu opens */
.radial-menu-demo {
  min-height: 100vh; min-height: 100svh; color: var(--text-main); font-family: var(--font-sans);
  background: radial-gradient(40rem 22rem at 50% 110%, color-mix(in srgb, var(--primary) 12%, transparent), transparent 70%), var(--surface-muted);
}
.radial-menu-demo__bar { display: flex; align-items: center; justify-content: space-between; gap: var(--space-md); max-width: var(--container-max); margin-inline: auto; padding: var(--space-md) var(--gutter); }
.radial-menu-demo__logo { display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.75rem; color: var(--text-main); font: 600 1.125rem var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none; }
.radial-menu-demo__mark {
  width: 1.375rem; height: 1.375rem; border-radius: 50%; background: conic-gradient(from 210deg, var(--primary), var(--primary-2), var(--primary));
  -webkit-mask: radial-gradient(closest-side, transparent 44%, black 48%); mask: radial-gradient(closest-side, transparent 44%, black 48%);
}
.radial-menu-demo__call {
  display: inline-flex; align-items: center; min-height: 2.75rem; padding: 0 0.875rem; border-radius: var(--radius-full);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  color: var(--text-main); font: 500 0.8125rem var(--font-mono); text-decoration: none;
}
.radial-menu-demo__bar :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.radial-menu-demo__page { max-width: var(--container-max); margin-inline: auto; padding: clamp(2rem, 6vw, 4.5rem) var(--gutter) 8rem; }
.radial-menu-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.radial-menu-demo__title { max-width: 13ch; margin: 0.75rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 3.8vw, 3.75rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.radial-menu-demo__lead { max-width: 30rem; margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.radial-menu-demo__tiles { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.75rem; max-width: 40rem; margin: var(--space-xl) 0 0; padding: 0; list-style: none; }
.radial-menu-demo__tiles li { display: grid; gap: 0.25rem; padding: var(--space-md); border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: var(--shadow-md), inset 0 0 0 1px var(--border-subtle); }
.radial-menu-demo__tiles strong { font: 600 0.9375rem var(--font-display); letter-spacing: var(--tracking-tight); }
.radial-menu-demo__tiles li > span:last-child { color: var(--text-muted); font: 500 0.75rem var(--font-mono); }
.radial-menu-demo__glyph { width: 2rem; height: 2rem; margin-bottom: var(--space-sm); border-radius: 0.625rem; background: var(--gradient-brand); box-shadow: var(--highlight); }
.radial-menu-demo__tiles li:nth-child(2) .radial-menu-demo__glyph { background: linear-gradient(135deg, var(--primary-2), var(--primary)); }
.radial-menu-demo__tiles li:nth-child(3) .radial-menu-demo__glyph { background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 55%, var(--surface-light)), var(--primary)); }
.radial-menu-demo__tiles li:nth-child(4) .radial-menu-demo__glyph { background: linear-gradient(135deg, var(--accent), var(--primary-2)); }

/* Menu geometry: items sit on an arc of --radial-menu-spread, --radial-menu-r from the hub centre */
.radial-menu {
  --radial-menu-hub: 4.5rem;
  --radial-menu-disc: 3.25rem;
  --radial-menu-r: min(7.5rem, 36vw);
  --radial-menu-band: 4.5rem;
  --radial-menu-spread: 160deg;
  --radial-menu-count: 5;
  --radial-menu-y: max(var(--space-lg), env(safe-area-inset-bottom));
  max-width: var(--container-max); margin-inline: auto; padding: 0 var(--gutter) var(--space-2xl);
  font-family: var(--font-sans);
}

/* Without JS: a plain row of links */
.radial-menu__list { display: flex; flex-wrap: wrap; gap: var(--space-sm); margin: 0; padding: 0; list-style: none; }
.radial-menu__link {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0.25rem 1rem 0.25rem 0.25rem;
  border-radius: var(--radius-full); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  color: var(--text-main); font-size: 0.875rem; font-weight: 600; text-decoration: none; -webkit-tap-highlight-color: transparent;
}
.radial-menu__link:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.radial-menu__disc { position: relative; display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 50%; background: var(--surface-deep); color: var(--text-inverse); }
.radial-menu__disc svg { position: relative; fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.radial-menu__track, .radial-menu:not(.radial-menu--js) .radial-menu__scrim { display: none; }

/* Hub: deep glass, gradient ring, aperture that closes like a shutter when pressed */
.radial-menu__hub {
  position: fixed; left: 50%; bottom: var(--radial-menu-y); z-index: var(--z-overlay); translate: -50% 0;
  display: grid; place-items: center; width: var(--radial-menu-hub); height: var(--radial-menu-hub);
  padding: 0; border: 0; border-radius: 50%; cursor: pointer; color: var(--text-inverse);
  background: color-mix(in srgb, var(--surface-deep) 88%, transparent);
  box-shadow: var(--highlight-inverse), inset 0 0 0 1px var(--border-inverse), 0 18px 36px -12px color-mix(in srgb, var(--surface-deep) 70%, transparent), var(--shadow-glow);
  touch-action: none; user-select: none; -webkit-user-select: none; -webkit-touch-callout: none; -webkit-tap-highlight-color: transparent;
  transition: scale var(--dur-3) var(--ease-spring);
}
@supports ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) {
  .radial-menu__hub { background: color-mix(in srgb, var(--surface-deep) 74%, transparent); -webkit-backdrop-filter: blur(var(--blur-md)) saturate(1.4); backdrop-filter: blur(var(--blur-md)) saturate(1.4); }
}
.radial-menu__hub:active { scale: 0.93; }
.radial-menu__hub:focus-visible { outline: 2px solid var(--primary); outline-offset: 4px; }
.radial-menu__ring {
  position: absolute; inset: -3px; border-radius: 50%; pointer-events: none;
  background: conic-gradient(from 20deg, var(--primary), var(--primary-2), color-mix(in srgb, var(--primary-2) 15%, transparent), var(--primary));
  -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 2.5px), black calc(100% - 2px));
  mask: radial-gradient(farthest-side, transparent calc(100% - 2.5px), black calc(100% - 2px));
  transition: rotate var(--dur-5) var(--ease-spring);
}
.radial-menu__hub::after { /* shutter flash on open */
  content: ""; position: absolute; inset: -3px; border-radius: 50%; pointer-events: none; opacity: 0;
  box-shadow: 0 0 0 2px color-mix(in srgb, var(--primary-2) 70%, transparent), 0 0 28px color-mix(in srgb, var(--primary) 55%, transparent);
}
.radial-menu__iris, .radial-menu__close, .radial-menu__readout {
  grid-area: 1 / 1;
  transition: opacity var(--dur-3) var(--ease-out), rotate var(--dur-4) var(--ease-spring), scale var(--dur-4) var(--ease-spring);
}
.radial-menu__iris, .radial-menu__close { fill: none; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
.radial-menu__close { stroke-width: 2; opacity: 0; rotate: -90deg; scale: 0.5; }
.radial-menu__readout { opacity: 0; scale: 0.7; font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; white-space: nowrap; }
.radial-menu__hub:active .radial-menu__iris { rotate: 60deg; scale: 0.8; }
.radial-menu.is-open .radial-menu__iris { opacity: 0; rotate: 150deg; scale: 0.4; }
.radial-menu.is-open .radial-menu__close { opacity: 1; rotate: 0deg; scale: 1; }
.radial-menu.is-open .radial-menu__ring { rotate: 180deg; }
.radial-menu.is-open .radial-menu__hub::after { animation: radial-menu-flash var(--dur-4) var(--ease-out); }
.radial-menu.is-aiming .radial-menu__close { opacity: 0; scale: 0.5; }
.radial-menu.is-aiming .radial-menu__readout { opacity: 1; scale: 1; }

@media (scripting: none) { .radial-menu__hub { display: none; } }
/* Failsafe: if the script never runs, the plain row comes back after 3s */
@media (scripting: enabled) {
  .radial-menu:not(.radial-menu--js) .radial-menu__nav { max-height: 0; overflow: hidden; visibility: hidden; animation: radial-menu-failsafe 0s 3s forwards; }
  .radial-menu:not(.radial-menu--js) .radial-menu__hub { animation: radial-menu-failsafe-out 0s 3s forwards; }
}

/* Enhanced: a viewport layer; only the hub, scrim and open items take clicks */
.radial-menu--js { position: fixed; inset: 0; z-index: var(--z-overlay); max-width: none; margin: 0; padding: 0; pointer-events: none; }
.radial-menu--js .radial-menu__hub { position: absolute; z-index: 2; pointer-events: auto; }
html:has(.radial-menu.is-open) { overflow: hidden; }

.radial-menu__scrim {
  position: absolute; inset: 0; pointer-events: auto;
  background:
    radial-gradient(130% 60% at 50% 100%, color-mix(in srgb, var(--primary) 16%, transparent), transparent 70%),
    color-mix(in srgb, var(--surface-light) 55%, transparent);
  -webkit-backdrop-filter: blur(5px); backdrop-filter: blur(5px);
  opacity: 0; visibility: hidden; transition: opacity var(--dur-4) var(--ease-out), visibility 0s var(--dur-4);
}
.radial-menu.is-open .radial-menu__scrim { opacity: 1; visibility: visible; transition-delay: 0s; }

.radial-menu--js .radial-menu__nav {
  position: absolute; z-index: 1; left: 50%; bottom: calc(var(--radial-menu-y) + var(--radial-menu-hub) / 2); width: 0; height: 0;
  visibility: hidden; transition: visibility 0s var(--dur-4);
}
.radial-menu--js.is-open .radial-menu__nav { visibility: visible; transition-delay: 0s; }

/* Arc track: a ring band, revealed by a conic mask whose angle sweeps from left to right */
.radial-menu--js .radial-menu__track {
  position: absolute; left: 0; top: 0; display: block; translate: -50% -50%;
  width: calc(var(--radial-menu-r) * 2 + var(--radial-menu-band)); aspect-ratio: 1; border-radius: 50%;
  background:
    radial-gradient(closest-side, color-mix(in srgb, var(--primary-2) 14%, transparent) 72%, color-mix(in srgb, var(--primary) 36%, transparent)),
    color-mix(in srgb, var(--surface-deep) 86%, transparent);
  -webkit-mask:
    radial-gradient(closest-side, transparent calc(100% - var(--radial-menu-band)), black calc(100% - var(--radial-menu-band) + 1px) calc(100% - 1px), transparent),
    conic-gradient(from 260deg, transparent 0deg, black min(10deg, var(--radial-menu-sweep) / 2) calc(var(--radial-menu-sweep) - 10deg), transparent var(--radial-menu-sweep));
  -webkit-mask-composite: source-in;
  mask:
    radial-gradient(closest-side, transparent calc(100% - var(--radial-menu-band)), black calc(100% - var(--radial-menu-band) + 1px) calc(100% - 1px), transparent),
    conic-gradient(from 260deg, transparent 0deg, black min(10deg, var(--radial-menu-sweep) / 2) calc(var(--radial-menu-sweep) - 10deg), transparent var(--radial-menu-sweep));
  mask-composite: intersect;
  transition: --radial-menu-sweep var(--dur-4) var(--ease-in-out);
}
.radial-menu.is-open .radial-menu__track { --radial-menu-sweep: 200deg; transition: --radial-menu-sweep var(--dur-5) var(--ease-out); }

/* Items: rotate to their angle, push out, counter-rotate to stay upright. Interpolating the
   same function list makes them spiral out of the hub along curved paths. */
.radial-menu--js .radial-menu__list { display: block; }
.radial-menu--js .radial-menu__item {
  --radial-menu-a: calc(var(--radial-menu-spread) / -2 + var(--radial-menu-i) * var(--radial-menu-spread) / (var(--radial-menu-count) - 1));
  position: absolute; left: 0; top: 0; width: var(--radial-menu-disc); height: var(--radial-menu-disc);
  margin: calc(var(--radial-menu-disc) / -2) 0 0 calc(var(--radial-menu-disc) / -2);
  transform: rotate(0deg) translateY(0) rotate(0deg) scale(0.3);
  transition: transform var(--dur-4) var(--ease-in-out) calc((var(--radial-menu-count) - 1 - var(--radial-menu-i)) * var(--stagger) / 2);
}
.radial-menu--js.is-open .radial-menu__item {
  transform: rotate(var(--radial-menu-a)) translateY(calc(var(--radial-menu-r) * -1)) rotate(calc(var(--radial-menu-a) * -1)) scale(1);
  transition: transform var(--dur-5) var(--ease-spring) calc(var(--radial-menu-i) * var(--stagger));
}
.radial-menu--js .radial-menu__link { display: block; width: 100%; height: 100%; min-height: 0; padding: 0; border-radius: 50%; background: none; box-shadow: none; pointer-events: auto; }
.radial-menu--js .radial-menu__link:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.radial-menu--js .radial-menu__disc {
  width: 100%; height: 100%; background: color-mix(in srgb, var(--text-inverse) 9%, transparent);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: scale var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.radial-menu--js .radial-menu__disc::before { content: ""; position: absolute; inset: 0; border-radius: inherit; background: var(--gradient-brand); opacity: 0; transition: opacity var(--dur-2) var(--ease-out); }
.radial-menu__item.is-active .radial-menu__disc { scale: 1.2; box-shadow: inset 0 0 0 1px var(--border-inverse), 0 12px 28px -8px color-mix(in srgb, var(--primary) 80%, transparent); }
.radial-menu__item.is-active .radial-menu__disc::before { opacity: 1; }
.radial-menu--js .radial-menu__name { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

@media (min-width: 768px) {
  .radial-menu { --radial-menu-hub: 5rem; --radial-menu-disc: 3.5rem; --radial-menu-r: 8.75rem; --radial-menu-band: 5rem; --radial-menu-y: max(var(--space-xl), env(safe-area-inset-bottom)); }
  .radial-menu-demo__tiles { grid-template-columns: repeat(4, minmax(0, 1fr)); }
}
@media (prefers-reduced-motion: reduce) {
  .radial-menu.is-open .radial-menu__hub::after { animation: none; }
}

@keyframes radial-menu-flash { from { opacity: 0.9; scale: 0.92; } to { opacity: 0; scale: 1.6; } }
@keyframes radial-menu-failsafe { to { max-height: none; visibility: visible; } }
@keyframes radial-menu-failsafe-out { to { visibility: hidden; } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

// While open, everything outside the menu is inert (only what we changed is restored)
const inertOutside = (keep, on, store) => {
  if (!on) { store.forEach((el) => { el.inert = false; }); store.clear(); return; }
  for (let node = keep; node.parentElement && node !== document.body; node = node.parentElement) {
    for (const sib of node.parentElement.children) {
      if (sib !== node && !sib.inert) { sib.inert = true; store.add(sib); }
    }
  }
};

document.querySelectorAll('[data-radial-menu]').forEach((root, n) => {
  const hub = root.querySelector('.radial-menu__hub');
  const nav = root.querySelector('.radial-menu__nav');
  const items = [...nav.querySelectorAll('.radial-menu__item')];
  const links = items.map((item) => item.querySelector('a'));
  const readout = root.querySelector('.radial-menu__readout');
  const inerted = new Set();
  let active = -1;
  let press = null; // the current press-and-drag gesture
  let swallowClick = false;
  let frame = 0;
  root.classList.add('radial-menu--js');
  if (n) nav.id = `${nav.id}-${n + 1}`; // unique ids for repeated instances
  hub.setAttribute('aria-controls', nav.id);

  const isOpen = () => root.classList.contains('is-open');

  // Highlight an item: it grows and its name rises into the hub
  const highlight = (i) => {
    if (i === active) return;
    items[active]?.classList.remove('is-active');
    active = i;
    root.classList.toggle('is-aiming', i >= 0);
    if (i < 0) return;
    items[i].classList.add('is-active');
    readout.textContent = links[i].textContent.trim();
    if (!reduce.matches) readout.animate({ opacity: [0, 1], transform: ['translateY(4px)', 'none'] }, { duration: 260, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' });
    if (press) navigator.vibrate?.(8);
  };

  // Arrows (and Home/End) move around the arc; Enter follows the focused link natively
  const onKey = (e) => {
    if (e.key === 'Escape') { e.preventDefault(); setOpen(false); return; }
    const steps = { ArrowLeft: -1, ArrowUp: -1, ArrowRight: 1, ArrowDown: 1 };
    if (!(e.key in steps) && e.key !== 'Home' && e.key !== 'End') return;
    e.preventDefault();
    const i = links.indexOf(document.activeElement);
    const next = e.key === 'Home' ? 0 : e.key === 'End' ? links.length - 1
      : i < 0 ? Math.max(active, 0) : (i + steps[e.key] + links.length) % links.length;
    links[next].focus();
  };

  const setOpen = (open, focusFirst = true) => {
    if (open === isOpen()) return;
    root.classList.toggle('is-open', open);
    hub.setAttribute('aria-expanded', String(open));
    inertOutside(root, open, inerted);
    document[open ? 'addEventListener' : 'removeEventListener']('keydown', onKey);
    if (open && focusFirst) links[0].focus({ preventScroll: true });
    if (!open) { highlight(-1); hub.focus({ preventScroll: true }); }
  };

  // Which item is the pointer aiming at? The nearest by angle, once it's clear of the hub
  const pick = (x, y) => {
    const h = hub.getBoundingClientRect();
    const px = x - (h.left + h.width / 2);
    const py = y - (h.top + h.height / 2);
    if (Math.hypot(px, py) < h.width * 0.7) return -1;
    let best = -1;
    let bestAngle = 0.42; // radians: half the gap between items, plus a little
    items.forEach((item, i) => {
      const r = item.getBoundingClientRect();
      const ix = r.left + r.width / 2 - (h.left + h.width / 2);
      const iy = r.top + r.height / 2 - (h.top + h.height / 2);
      const angle = Math.abs(Math.atan2(ix * py - iy * px, ix * px + iy * py));
      if (angle < bestAngle) { bestAngle = angle; best = i; }
    });
    return best;
  };

  // Press and hold the hub, slide towards an item, release to open it
  hub.addEventListener('pointerdown', (e) => {
    if (e.button !== 0) return;
    swallowClick = false;
    press = { id: e.pointerId, x: e.clientX, y: e.clientY, moved: false, opened: !isOpen() };
    hub.setPointerCapture(e.pointerId);
    if (press.opened) setOpen(true, false);
  });
  hub.addEventListener('pointermove', (e) => {
    if (!press || e.pointerId !== press.id) return;
    press.moved ||= Math.hypot(e.clientX - press.x, e.clientY - press.y) > 10;
    if (!press.moved || frame) return;
    const { clientX, clientY } = e;
    frame = requestAnimationFrame(() => { frame = 0; if (press) highlight(pick(clientX, clientY)); });
  }, { passive: true });
  const release = (e) => {
    if (!press || e.pointerId !== press.id) return;
    const { moved, opened } = press;
    press = null;
    cancelAnimationFrame(frame);
    frame = 0;
    if (!moved && !opened) return; // a plain tap on the open hub: the click closes it
    swallowClick = true;
    if (e.type === 'pointerup' && moved && active >= 0) links[active].click();
    else if (!moved) links[0].focus({ preventScroll: true }); // a tap opened it
    else if (opened) setOpen(false); // slid away from everything: cancel
    else highlight(-1);
  };
  hub.addEventListener('pointerup', release);
  hub.addEventListener('pointercancel', release);
  // Keyboard and assistive-tech clicks (and taps we didn't handle) toggle normally
  hub.addEventListener('click', (e) => {
    const skip = swallowClick && e.detail !== 0;
    swallowClick = false;
    if (!skip) setOpen(!isOpen());
  });

  items.forEach((item, i) => item.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') highlight(i); }));
  nav.addEventListener('pointerleave', (e) => { if (e.pointerType === 'mouse' && !nav.contains(document.activeElement)) highlight(-1); });
  nav.addEventListener('focusin', (e) => highlight(links.indexOf(e.target)));
  nav.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
  root.querySelector('.radial-menu__scrim').addEventListener('click', () => setOpen(false));
});
```

## Notes

- Disclosure model: the hub has `aria-expanded` and `aria-controls` and opens a `<nav>` list of five real links. Their text names are visually hidden in the fan and visible without JS. Opening focuses Home, makes everything outside the menu `inert` and locks scrolling through `html:has()`. Arrow keys and Home/End move focus around the arc, and the highlight follows focus. Enter follows the link. Escape, the scrim, the hub or choosing an item closes the menu and returns focus to the hub.
- Press-and-drag uses Pointer Events with pointer capture on the hub (`touch-action: none`). Once the pointer clears the hub, the nearest item by angle is highlighted, at most once per frame. Releasing on it fires the link's real `click()`. Sliding away from everything cancels a menu the press opened. Plain taps and keyboard or assistive-tech clicks toggle normally. Where `navigator.vibrate` exists (Android), each new highlight gives a light tick.
- No JS (`@media (scripting: none)`): the hub is hidden and the items render as a plain row of labelled links after the content. With scripting on, a 3s CSS failsafe restores that row if the module never runs.
- Reduced motion: no stagger, spring, sweep or flash. The fan, track and highlight snap into place because the motion tokens collapse, and the hub label skips its rise.
- Contrast: white icons and the hub label sit on `--surface-deep` at 74–88% over the light scrim (about 9:1 or better). Highlighted icons on the brand gradient stay at 3.7:1 or better (non-text). The sweep animates a registered `@property` angle; without `@property` the track simply appears. `mask-composite` has a `-webkit-` path for Safari.
- Adapting: set `--radial-menu-count` and `--radial-menu-spread` for 3–7 items, keeping `--radial-menu-i` in order. `--radial-menu-r` sizes the arc. On a real page, put `.radial-menu` at the end of `<body>`; nothing else needs wiring.
