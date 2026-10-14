# Curtain Strip Menu

A full-screen menu built like falling slats. When it opens, five vertical strips in alternating shades of the brand gradient drop from the top one after another, each settling with a small spring bounce, and together they form the menu's background. Big links then rise out of their masks, followed by a contact block and a "Book now" button. On close the strips retract upwards in reverse order. The toggle is a text button whose label rolls from "Menu" to "Close". On phones everything stacks in one column. On desktop the links get display-sized type, with the contact block and button anchored bottom-right. Depends on `tokens/variables.css`.

**Motion:** strips drop with a staggered spring (`--dur-5` + `--ease-spring`, `--stagger`) · links rise from masks (`--dur-5` + `--ease-out`, `--stagger`) · contact and button follow · label roll on the toggle (`--dur-4` + `--ease-spring`) · hover underline wipe (`--ease-out`) · strips retract in reverse stagger on close (`--dur-4` + `--ease-in-out`).

## HTML

```html
<div class="curtain-menu-demo">
  <header class="curtain-menu" data-curtain-menu>
    <div class="curtain-menu__bar">
      <a class="curtain-menu__logo" href="#"><span class="curtain-menu__mark" aria-hidden="true"><span></span><span></span><span></span></span>Brand</a>
      <button class="curtain-menu__toggle" type="button" aria-expanded="false" aria-controls="curtain-menu-panel">
        <span class="curtain-menu__roll" aria-hidden="true"><span>Menu</span><span>Close</span></span>
        <span class="curtain-menu__sr">Menu</span>
      </button>
    </div>

    <nav class="curtain-menu__panel" id="curtain-menu-panel" aria-label="Main">
      <div class="curtain-menu__strips" aria-hidden="true">
        <span class="curtain-menu__strip" style="--curtain-menu-i: 0"></span>
        <span class="curtain-menu__strip" style="--curtain-menu-i: 1"></span>
        <span class="curtain-menu__strip" style="--curtain-menu-i: 2"></span>
        <span class="curtain-menu__strip" style="--curtain-menu-i: 3"></span>
        <span class="curtain-menu__strip" style="--curtain-menu-i: 4"></span>
      </div>

      <div class="curtain-menu__body">
        <ul class="curtain-menu__list" role="list">
          <li style="--curtain-menu-i: 0"><a class="curtain-menu__link" href="#services"><span class="curtain-menu__mask"><span class="curtain-menu__word">Services</span></span></a></li>
          <li style="--curtain-menu-i: 1"><a class="curtain-menu__link" href="#projects"><span class="curtain-menu__mask"><span class="curtain-menu__word">Projects</span></span></a></li>
          <li style="--curtain-menu-i: 2"><a class="curtain-menu__link" href="#about"><span class="curtain-menu__mask"><span class="curtain-menu__word">About</span></span></a></li>
          <li style="--curtain-menu-i: 3"><a class="curtain-menu__link" href="#reviews"><span class="curtain-menu__mask"><span class="curtain-menu__word">Reviews</span></span></a></li>
          <li style="--curtain-menu-i: 4"><a class="curtain-menu__link" href="#contact"><span class="curtain-menu__mask"><span class="curtain-menu__word">Contact</span></span></a></li>
        </ul>

        <div class="curtain-menu__aside">
          <dl class="curtain-menu__contact">
            <div><dt>Call</dt><dd><a href="tel:+15555550123">(555) 555-0123</a></dd></div>
            <div><dt>Email</dt><dd><a href="mailto:hello@example.com">hello@example.com</a></dd></div>
            <div class="curtain-menu__wide"><dt>Hours</dt><dd>Mon–Sat, 7 am–8 pm · Westlake, Northside, Riverside</dd></div>
          </dl>
          <a class="curtain-menu__book" href="#book">
            Book now
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
          </a>
        </div>
      </div>
    </nav>
  </header>

  <main class="curtain-menu-demo__page">
    <p class="curtain-menu-demo__eyebrow">Bathrooms · Kitchens · Repairs</p>
    <h2 class="curtain-menu-demo__title">Small jobs, done with big-job care.</h2>
    <p class="curtain-menu-demo__lead">One Springfield crew for the dripping tap, the new vanity and everything in between. Fixed prices, tidy finishes.</p>
    <div class="curtain-menu-demo__shots" aria-hidden="true">
      <span class="curtain-menu-demo__shot"><small>Riverside · Walk-in shower</small></span>
      <span class="curtain-menu-demo__shot"><small>Westlake · Kitchen refit</small></span>
    </div>
    <p class="curtain-menu-demo__proof"><strong>4.9/5</strong> from 1,200+ homeowners</p>
  </main>
</div>
```

## CSS

```css
/* Demo page behind the menu (light) */
.curtain-menu-demo { min-height: 100vh; min-height: 100svh; background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.curtain-menu-demo__page { max-width: var(--container-max); margin-inline: auto; padding: clamp(1.5rem, 5vw, 4rem) var(--gutter) var(--space-2xl); }
.curtain-menu-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.curtain-menu-demo__title { max-width: 15ch; margin: 0.75rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 3.8vw, 4rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.curtain-menu-demo__lead { max-width: 32rem; margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.curtain-menu-demo__shots { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.75rem; max-width: 36rem; margin-top: var(--space-xl); }
.curtain-menu-demo__shot {
  display: flex; align-items: flex-end; aspect-ratio: 4 / 5; padding: 0.75rem; border-radius: var(--radius-xl); box-shadow: var(--shadow-lg);
  background:
    repeating-linear-gradient(90deg, transparent 0 18%, color-mix(in srgb, var(--surface-light) 12%, transparent) 18% 20%),
    radial-gradient(80% 60% at 30% 20%, color-mix(in srgb, var(--surface-light) 45%, transparent), transparent 70%),
    linear-gradient(160deg, var(--primary), var(--primary-2));
}
.curtain-menu-demo__shot:nth-child(2) {
  background:
    repeating-linear-gradient(90deg, transparent 0 18%, color-mix(in srgb, var(--surface-light) 12%, transparent) 18% 20%),
    radial-gradient(80% 60% at 70% 30%, color-mix(in srgb, var(--accent) 55%, transparent), transparent 70%),
    linear-gradient(200deg, var(--primary-2), color-mix(in srgb, var(--primary) 70%, var(--surface-deep)));
}
.curtain-menu-demo__shot small { padding: 0.25rem 0.5rem; border-radius: var(--radius-full); background: var(--glass); color: var(--text-main); font: 500 0.6875rem var(--font-mono); }
.curtain-menu-demo__proof { margin: 1.25rem 0 0; color: var(--text-muted); font-size: 0.875rem; }
.curtain-menu-demo__proof strong { color: var(--text-main); }

/* Header with the strip palette. The panel inside is fixed: keep transform and filter off this element */
.curtain-menu {
  --curtain-menu-bar: 4.25rem;
  --curtain-menu-s1: color-mix(in oklab, var(--primary) 68%, var(--surface-deep));
  --curtain-menu-s2: color-mix(in oklab, color-mix(in oklab, var(--primary-2) 25%, var(--primary)) 54%, var(--surface-deep));
  --curtain-menu-s3: color-mix(in oklab, color-mix(in oklab, var(--primary-2) 50%, var(--primary)) 68%, var(--surface-deep));
  --curtain-menu-s4: color-mix(in oklab, color-mix(in oklab, var(--primary-2) 75%, var(--primary)) 54%, var(--surface-deep));
  --curtain-menu-s5: color-mix(in oklab, var(--primary-2) 68%, var(--surface-deep));
  --curtain-menu-fill: linear-gradient(120deg, var(--curtain-menu-s1), var(--curtain-menu-s3) 55%, var(--curtain-menu-s5));
  position: relative; z-index: var(--z-sticky); font-family: var(--font-sans);
}
.curtain-menu--js { position: sticky; top: 0; }
.curtain-menu.is-open { z-index: var(--z-overlay); }
html:has(.curtain-menu.is-open) { overflow: hidden; }

/* Bar: glass over the page, transparent over the strips (the logo flips once a strip covers it) */
.curtain-menu__bar {
  position: relative; z-index: 1; display: flex; align-items: center; justify-content: space-between; gap: var(--space-md);
  height: var(--curtain-menu-bar); padding-inline: max(var(--gutter), calc((100% - var(--container-max)) / 2 + var(--gutter)));
  color: var(--text-main); transition: color var(--dur-2) var(--ease-out) calc(var(--dur-4) + var(--dur-3));
}
.curtain-menu__bar::before {
  content: ""; position: absolute; inset: 0; z-index: -1; box-shadow: inset 0 -1px 0 var(--border-subtle);
  background: var(--glass); -webkit-backdrop-filter: blur(var(--blur-md)) saturate(1.6); backdrop-filter: blur(var(--blur-md)) saturate(1.6);
  transition: opacity var(--dur-2) var(--ease-out) calc(var(--dur-4) + var(--dur-3));
}
.curtain-menu.is-open .curtain-menu__bar { color: var(--text-inverse); transition-delay: var(--dur-3); }
.curtain-menu.is-open .curtain-menu__bar::before { opacity: 0; transition-delay: 0s; }
.curtain-menu__logo { display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.75rem; color: inherit; font: 600 1.125rem var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none; }
.curtain-menu__mark { display: inline-flex; gap: 2px; height: 1.25rem; }
.curtain-menu__mark span { width: 0.3125rem; border-radius: 1px; background: var(--primary); }
.curtain-menu__mark span:nth-child(2) { translate: 0 2px; background: color-mix(in oklab, var(--primary) 50%, var(--primary-2)); }
.curtain-menu__mark span:nth-child(3) { translate: 0 4px; background: var(--primary-2); }
.curtain-menu :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.curtain-menu.is-open .curtain-menu__bar :is(a, button):focus-visible, .curtain-menu__panel :is(a, button):focus-visible { outline-color: var(--text-inverse); }

/* Text toggle: "Menu" rolls up and "Close" rolls in; the accessible name stays "Menu" */
.curtain-menu__toggle {
  display: inline-flex; align-items: center; min-height: 2.75rem; padding: 0 1.25rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--text-main); color: var(--surface-light); font: 600 0.9375rem var(--font-sans);
  box-shadow: var(--highlight-inverse), 0 10px 24px -12px color-mix(in srgb, var(--text-main) 70%, transparent);
  transition: background-color var(--dur-3) var(--ease-out), color var(--dur-3) var(--ease-out), scale var(--dur-3) var(--ease-spring);
}
.curtain-menu__toggle:active { scale: 0.95; }
.curtain-menu.is-open .curtain-menu__toggle { background: var(--surface-light); color: var(--text-main); box-shadow: var(--highlight), 0 12px 30px -12px color-mix(in srgb, var(--surface-deep) 60%, transparent); }
.curtain-menu__roll { display: grid; height: 1.25em; overflow: clip; line-height: 1.25; }
.curtain-menu__roll span { transition: translate var(--dur-4) var(--ease-spring); }
.curtain-menu.is-open .curtain-menu__roll span { translate: 0 -100%; }
.curtain-menu__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Without JS: a gradient band under the bar */
.curtain-menu__panel { position: relative; background: var(--curtain-menu-fill); color: var(--text-inverse); }
.curtain-menu__strips { display: none; }
.curtain-menu__body { max-width: var(--container-max); margin-inline: auto; padding: var(--space-xl) var(--gutter); }
.curtain-menu__list { display: grid; gap: var(--space-xs); margin: 0; padding: 0; list-style: none; }
.curtain-menu__link { position: relative; display: inline-block; color: var(--text-inverse); text-decoration: none; }
.curtain-menu__link::after {
  content: ""; position: absolute; left: 0; right: 0; bottom: 0.06em; height: 3px; border-radius: 3px; background: currentColor;
  scale: 0 1; transform-origin: right; transition: scale var(--dur-3) var(--ease-out);
}
.curtain-menu__link:hover::after { scale: 1 1; transform-origin: left; }
.curtain-menu__mask { display: block; overflow: clip; padding-bottom: 0.06em; }
.curtain-menu__word { display: block; font: 600 clamp(2rem, 1.25rem + 3vw, 3rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); }
.curtain-menu__aside { display: grid; gap: var(--space-lg); margin-top: var(--space-xl); }
.curtain-menu__contact { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: var(--space-md); margin: 0; }
.curtain-menu__wide { grid-column: 1 / -1; }
.curtain-menu__contact dt { font: 500 0.6875rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.curtain-menu__contact dd { margin: 0.25rem 0 0; font-size: 0.9375rem; line-height: 1.45; }
.curtain-menu__contact a {
  display: inline-flex; align-items: center; min-height: 1.75rem; color: var(--text-inverse); overflow-wrap: anywhere;
  text-decoration: underline; text-decoration-color: color-mix(in srgb, var(--text-inverse) 40%, transparent); text-underline-offset: 4px;
  transition: text-decoration-color var(--dur-2);
}
.curtain-menu__contact a:hover { text-decoration-color: currentColor; }
.curtain-menu__book {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.5rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight), 0 18px 40px -16px color-mix(in srgb, var(--surface-deep) 70%, transparent);
  transition: scale var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.curtain-menu__book:hover { box-shadow: var(--highlight), 0 22px 48px -14px color-mix(in srgb, var(--surface-deep) 80%, transparent); }
.curtain-menu__book:active { scale: 0.97; }
.curtain-menu__book svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.curtain-menu__book:hover svg { translate: 3px 0; }

@media (scripting: none) { .curtain-menu__toggle { display: none; } }
/* Failsafe: if the script never runs, the plain band comes back after 3s */
@media (scripting: enabled) {
  .curtain-menu:not(.curtain-menu--js) .curtain-menu__panel { max-height: 0; overflow: hidden; visibility: hidden; animation: curtain-menu-failsafe 0s 3s forwards; }
  .curtain-menu:not(.curtain-menu--js) .curtain-menu__toggle { animation: curtain-menu-failsafe-out 0s 3s forwards; }
}

/* Enhanced: a fixed panel whose background is five falling strips */
.curtain-menu--js .curtain-menu__panel {
  position: fixed; inset: 0; z-index: 0; overflow: hidden; background: none;
  visibility: hidden; transition: visibility 0s calc(var(--dur-1) + 4 * var(--stagger) + var(--dur-4));
}
.curtain-menu--js.is-open .curtain-menu__panel { visibility: visible; transition-delay: 0s; }
.curtain-menu--js .curtain-menu__strips { position: absolute; inset: 0; display: block; pointer-events: none; }
/* Each strip is 3rem taller than the screen, so the spring's overshoot never opens a gap at the top */
.curtain-menu__strip {
  position: absolute; top: -3rem; left: calc(var(--curtain-menu-i) * 20%); width: calc(20% + 1px); height: calc(100% + 3rem);
  background: linear-gradient(180deg, var(--curtain-menu-c), color-mix(in oklab, var(--curtain-menu-c) 72%, var(--surface-deep)));
  box-shadow: inset 1px 0 0 color-mix(in srgb, var(--text-inverse) 7%, transparent);
  transform: translateY(-100%);
  transition: transform var(--dur-4) var(--ease-in-out) calc(var(--dur-1) + (4 - var(--curtain-menu-i)) * var(--stagger));
}
.curtain-menu__strip:nth-child(1) { --curtain-menu-c: var(--curtain-menu-s1); }
.curtain-menu__strip:nth-child(2) { --curtain-menu-c: var(--curtain-menu-s2); }
.curtain-menu__strip:nth-child(3) { --curtain-menu-c: var(--curtain-menu-s3); }
.curtain-menu__strip:nth-child(4) { --curtain-menu-c: var(--curtain-menu-s4); }
.curtain-menu__strip:nth-child(5) { --curtain-menu-c: var(--curtain-menu-s5); }
.curtain-menu.is-open .curtain-menu__strip { transform: none; transition: transform var(--dur-5) var(--ease-spring) calc(var(--curtain-menu-i) * var(--stagger)); }

.curtain-menu--js .curtain-menu__body {
  position: relative; display: flex; flex-direction: column; justify-content: space-between; gap: var(--space-xl); height: 100%;
  padding: calc(var(--curtain-menu-bar) + var(--space-lg)) var(--gutter) max(var(--space-xl), env(safe-area-inset-bottom));
  overflow-y: auto; overscroll-behavior: contain;
}
.curtain-menu--js .curtain-menu__list { flex: 1 0 auto; align-content: center; }
.curtain-menu--js .curtain-menu__word { font-size: clamp(2.5rem, 1.5rem + 6vw, 4rem); transform: translateY(105%); transition: transform var(--dur-2) var(--ease-in-out); }
.curtain-menu--js.is-open .curtain-menu__word { transform: none; transition: transform var(--dur-5) var(--ease-out) calc(var(--dur-4) + var(--curtain-menu-i) * var(--stagger)); }
.curtain-menu--js .curtain-menu__aside { margin-top: 0; }
/* Contact, then the button, once the links are up */
.curtain-menu--js :is(.curtain-menu__contact, .curtain-menu__book) {
  opacity: 0; translate: 0 1rem;
  transition: opacity var(--dur-2) var(--ease-out), translate var(--dur-2) var(--ease-out), scale var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.curtain-menu--js.is-open .curtain-menu__contact { opacity: 1; translate: 0 0; transition-duration: var(--dur-4); transition-delay: calc(var(--dur-4) + 5 * var(--stagger)); }
.curtain-menu--js.is-open .curtain-menu__book {
  opacity: 1; translate: 0 0;
  transition: opacity var(--dur-4) var(--ease-out) calc(var(--dur-4) + 7 * var(--stagger)), translate var(--dur-4) var(--ease-spring) calc(var(--dur-4) + 7 * var(--stagger)), scale var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}

/* Desktop: display-size links on the left, contact and button anchored bottom-right */
@media (min-width: 768px) {
  .curtain-menu { --curtain-menu-bar: 4.75rem; }
  .curtain-menu--js .curtain-menu__body {
    display: grid; grid-template-columns: minmax(0, 1fr) minmax(16rem, 22rem); align-items: end; column-gap: var(--space-2xl);
  }
  .curtain-menu--js .curtain-menu__list { align-self: center; }
  .curtain-menu--js .curtain-menu__word { font-size: clamp(3.5rem, min(7vw, 12vh), 7rem); }
  .curtain-menu--js .curtain-menu__contact { grid-template-columns: 1fr; }
  .curtain-menu--js .curtain-menu__book { justify-self: start; }
}
/* Reduced motion: no strips, just an instant gradient background */
@media (prefers-reduced-motion: reduce) {
  .curtain-menu--js .curtain-menu__strips { display: none; }
  .curtain-menu--js .curtain-menu__panel { background: var(--curtain-menu-fill); }
}

@keyframes curtain-menu-failsafe { to { max-height: none; visibility: visible; } }
@keyframes curtain-menu-failsafe-out { to { visibility: hidden; } }
```

## JS

```js
// While open, everything outside the header is inert (only what we changed is restored)
const inertOutside = (keep, on, store) => {
  if (!on) { store.forEach((el) => { el.inert = false; }); store.clear(); return; }
  for (let node = keep; node.parentElement && node !== document.body; node = node.parentElement) {
    for (const sib of node.parentElement.children) {
      if (sib !== node && !sib.inert) { sib.inert = true; store.add(sib); }
    }
  }
};

document.querySelectorAll('[data-curtain-menu]').forEach((root, n) => {
  const toggle = root.querySelector('.curtain-menu__toggle');
  const panel = root.querySelector('.curtain-menu__panel');
  const firstLink = panel.querySelector('a');
  const inerted = new Set();
  root.classList.add('curtain-menu--js');
  if (n) panel.id = `${panel.id}-${n + 1}`; // unique ids for repeated instances
  toggle.setAttribute('aria-controls', panel.id);

  const isOpen = () => root.classList.contains('is-open');
  const onKey = (e) => { if (e.key === 'Escape') { e.preventDefault(); setOpen(false); } };
  // The strips, links and label roll are all CSS transitions keyed off .is-open
  const setOpen = (open) => {
    if (open === isOpen()) return;
    root.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    inertOutside(root, open, inerted);
    document[open ? 'addEventListener' : 'removeEventListener']('keydown', onKey);
    (open ? firstLink : toggle).focus({ preventScroll: true });
  };

  toggle.addEventListener('click', () => setOpen(!isOpen()));
  panel.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
});
```

## Notes

- Disclosure model with a modal state: the toggle has `aria-expanded` and `aria-controls`. Its accessible name stays "Menu", because the rolling label is `aria-hidden` and the state comes from `aria-expanded`. Opening focuses the first link, makes everything outside the header `inert` and locks scrolling through `html:has()`. Escape, the toggle or following a link closes the menu and returns focus to the toggle.
- The strips are decorative (`aria-hidden`) spans moved with `translateY`. Each is 3rem taller than the screen, so the spring's overshoot never opens a gap at the top. On close the links drop first, the strips retract right to left, and the panel stays visible (`visibility` delay) until the last strip has gone.
- No JS (`@media (scripting: none)`): the toggle is hidden and the nav renders as a gradient band of links, contact details and Book now under the bar. With scripting on, the overlay starts closed from first paint, and a 3s CSS failsafe restores the band if the module never runs.
- Reduced motion: no strips. The panel gets a static brand-gradient fill, and the links, contact block and button appear instantly as the motion tokens collapse.
- Contrast: the strips mix the brand colours with 32–46% `--surface-deep` in OKLab, so `--text-inverse` stays at about 6.8:1 or better on every strip, for the large links and the small contact text alike. No muted grey is used on the strips. Book now is `--text-main` on `--surface-light` (14.6:1).
- Adapting: the strip shades live in `--curtain-menu-s1` to `--curtain-menu-s5`. For a different strip count, change the 20% width and position step, the `4 - i` reverse stagger and the panel's `visibility` delay. The panel is `position: fixed` inside the sticky header, so keep `transform`, `filter` and `backdrop-filter` off `.curtain-menu` itself.
