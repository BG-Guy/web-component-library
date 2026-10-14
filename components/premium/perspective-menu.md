# Perspective Push Menu

Opening the menu pushes the whole page back in 3D, like a card swept aside on a table. The page turns away (about -12° on Y), slides about 60% to the right and shrinks to 85% with rounded corners, a deep shadow and shading on its far edge. A translucent ghost card trails behind it for stacked depth. Underneath is a deep gradient surface, and the menu links slide in from the left one after another, followed by a contact block. Tapping the pushed page closes the menu. On desktop the page moves a shorter distance and the perspective flattens, so the menu gets a comfortable column. Depends on `tokens/variables.css`.

**Motion:** page push with perspective, shift, scale and rounded corners (`--dur-5` + `--ease-out`) · ghost card trails one `--stagger` behind · links and contact slide in from the left (`--dur-5` + `--ease-out`, `--stagger`) · edge shading fade · burger to × on the toggle (`--ease-spring`) · swing back on close (`--dur-4` + `--ease-in-out`).

## HTML

```html
<div class="persp-menu" data-persp-menu>
  <nav class="persp-menu__nav" id="persp-menu-nav" aria-label="Main">
    <div class="persp-menu__inner">
      <p class="persp-menu__eyebrow" style="--persp-menu-i: 0">Brand · Springfield</p>
      <ul class="persp-menu__list" role="list">
        <li class="persp-menu__item" style="--persp-menu-i: 1"><a class="persp-menu__link" href="#" aria-current="page">Home</a></li>
        <li class="persp-menu__item" style="--persp-menu-i: 2"><a class="persp-menu__link" href="#services">Services</a></li>
        <li class="persp-menu__item" style="--persp-menu-i: 3"><a class="persp-menu__link" href="#projects">Projects</a></li>
        <li class="persp-menu__item" style="--persp-menu-i: 4"><a class="persp-menu__link" href="#reviews">Reviews</a></li>
        <li class="persp-menu__item" style="--persp-menu-i: 5"><a class="persp-menu__link" href="#contact">Contact</a></li>
      </ul>
      <div class="persp-menu__contact" style="--persp-menu-i: 6">
        <a class="persp-menu__book" href="#book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="persp-menu__line" href="tel:+15555550123">(555) 555-0123</a>
        <a class="persp-menu__line" href="mailto:hello@example.com">hello@example.com</a>
        <p class="persp-menu__hours">Mon–Sat · 7 am–8 pm</p>
      </div>
    </div>
  </nav>

  <div class="persp-menu__ghost" aria-hidden="true"></div>

  <!-- Wrap your whole page (header, main, footer) in __content -->
  <div class="persp-menu__page">
    <div class="persp-menu__content">
      <header class="persp-menu__bar">
        <a class="persp-menu__logo" href="#"><span class="persp-menu__mark" aria-hidden="true"></span>Brand</a>
        <button class="persp-menu__toggle" type="button" aria-expanded="false" aria-controls="persp-menu-nav">
          <span class="persp-menu__burger" aria-hidden="true"></span>Menu
        </button>
      </header>

      <main class="persp-menu-demo">
        <p class="persp-menu-demo__eyebrow">Springfield · since 1998</p>
        <h2 class="persp-menu-demo__title">Home services that show up on time.</h2>
        <p class="persp-menu-demo__lead">Plumbing, heating and electrical, booked in a minute and backed by a one-year guarantee.</p>
        <dl class="persp-menu-demo__stats">
          <div><dt>Arrival window</dt><dd>2 hr</dd></div>
          <div><dt>Rating</dt><dd>4.9</dd></div>
          <div><dt>Guarantee</dt><dd>1 yr</dd></div>
        </dl>
        <section class="persp-menu-demo__card" aria-labelledby="persp-menu-crew">
          <h3 id="persp-menu-crew">Today's crew</h3>
          <ul class="persp-menu-demo__crew" role="list">
            <li><span class="persp-menu-demo__avatar" aria-hidden="true">MR</span><span><strong>Maria R.</strong><small>Westlake · Boiler service</small></span></li>
            <li><span class="persp-menu-demo__avatar" aria-hidden="true">SK</span><span><strong>Sam K.</strong><small>Northside · Leak repair</small></span></li>
            <li><span class="persp-menu-demo__avatar" aria-hidden="true">JP</span><span><strong>Jo P.</strong><small>Riverside · Rewire</small></span></li>
          </ul>
        </section>
      </main>
    </div>
    <button class="persp-menu__shield" type="button" aria-label="Close menu" hidden></button>
  </div>
</div>
```

## CSS

```css
/* Root: the menu underneath, a ghost card and the page on top */
.persp-menu {
  --persp-menu-shift: 60%;
  --persp-menu-scale: 0.85;
  --persp-menu-tilt: -12deg;
  --persp-menu-depth: 1200px;
  --persp-menu-ghost-shift: 48%;
  --persp-menu-ghost-scale: 0.74;
  --persp-menu-room: 64%; /* menu column: stays clear of the pushed page */
  --persp-menu-bar: 4.25rem;
  position: relative; isolation: isolate; font-family: var(--font-sans);
}

/* Menu surface. Without JS it is a deep band above the page */
.persp-menu__nav {
  color: var(--text-inverse);
  background:
    radial-gradient(60% 45% at 0% 100%, color-mix(in srgb, var(--primary-2) 26%, transparent), transparent 70%),
    linear-gradient(160deg, color-mix(in srgb, var(--surface-deep) 80%, var(--primary)), var(--surface-deep) 70%);
}
.persp-menu__inner { max-width: var(--container-max); margin-inline: auto; padding: var(--space-lg) var(--gutter); }
.persp-menu__eyebrow { margin: 0 0 var(--space-md); color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.persp-menu__list { display: flex; flex-wrap: wrap; gap: var(--space-xs) var(--space-lg); margin: 0; padding: 0; list-style: none; }
.persp-menu__link {
  position: relative; display: inline-flex; align-items: center; gap: 0.75rem; min-height: 2.75rem;
  color: var(--text-inverse); font: 600 1.375rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none;
}
.persp-menu__link::after {
  content: ""; position: absolute; left: 0; right: 0; bottom: 0.25rem; height: 2px; border-radius: 2px;
  background: linear-gradient(90deg, var(--primary-2), color-mix(in srgb, var(--primary) 55%, var(--text-inverse)));
  scale: 0 1; transform-origin: left; transition: scale var(--dur-3) var(--ease-out);
}
.persp-menu__link:hover::after { scale: 1 1; }
.persp-menu__link[aria-current="page"]::before {
  content: ""; flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%;
  background: var(--gradient-brand); box-shadow: 0 0 12px color-mix(in srgb, var(--primary-2) 80%, transparent);
}
.persp-menu__contact { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-sm) var(--space-md); margin-top: var(--space-lg); }
.persp-menu__book {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight), 0 12px 32px -12px color-mix(in srgb, var(--primary-2) 70%, transparent);
  transition: scale var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.persp-menu__book:hover { box-shadow: var(--highlight), 0 16px 40px -10px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.persp-menu__book:active { scale: 0.96; }
.persp-menu__book svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.persp-menu__book:hover svg { translate: 3px 0; }
.persp-menu__line { display: inline-flex; align-items: center; min-height: 2.75rem; color: var(--text-inverse); font: 500 0.875rem var(--font-mono); text-decoration: none; text-underline-offset: 4px; }
.persp-menu__line:hover { text-decoration: underline; }
.persp-menu__hours { margin: 0; color: var(--text-inverse-muted); font-size: 0.8125rem; }
.persp-menu__nav :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.persp-menu__ghost { display: none; }

/* The page: an opaque card with a sticky bar (sticky, not fixed: see Notes) */
.persp-menu__page { position: relative; z-index: 2; min-height: 100vh; min-height: 100svh; background: var(--surface-light); color: var(--text-main); }
.persp-menu__bar {
  position: sticky; top: 0; z-index: 3; display: flex; align-items: center; justify-content: space-between; gap: var(--space-md);
  height: var(--persp-menu-bar); padding-inline: max(var(--gutter), calc((100% - var(--container-max)) / 2 + var(--gutter)));
  background: var(--glass); -webkit-backdrop-filter: blur(var(--blur-md)) saturate(1.6); backdrop-filter: blur(var(--blur-md)) saturate(1.6);
  box-shadow: inset 0 -1px 0 var(--border-subtle);
}
.persp-menu__logo { display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.75rem; color: var(--text-main); font: 600 1.125rem var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none; }
.persp-menu__mark {
  width: 1.25rem; height: 1.25rem; border-radius: var(--radius-sm); background: var(--gradient-brand);
  box-shadow: 4px -4px 0 -1px color-mix(in srgb, var(--primary-2) 35%, transparent); transform: perspective(60px) rotateY(-18deg);
}
.persp-menu__toggle {
  display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.75rem; padding: 0 1rem 0 0.875rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--text-main); color: var(--surface-light); font: 600 0.875rem var(--font-sans);
  box-shadow: var(--highlight-inverse), 0 10px 24px -12px color-mix(in srgb, var(--text-main) 70%, transparent);
  transition: scale var(--dur-3) var(--ease-spring);
}
.persp-menu__toggle:active { scale: 0.95; }
.persp-menu__burger { position: relative; width: 1rem; height: 0.5rem; }
.persp-menu__burger::before, .persp-menu__burger::after {
  content: ""; position: absolute; left: 0; width: 100%; height: 2px; border-radius: 2px; background: currentColor;
  transition: translate var(--dur-3) var(--ease-out), rotate var(--dur-4) var(--ease-spring);
}
.persp-menu__burger::before { top: 0; }
.persp-menu__burger::after { bottom: 0; }
.persp-menu.is-open .persp-menu__burger::before { translate: 0 3px; rotate: 45deg; }
.persp-menu.is-open .persp-menu__burger::after { translate: 0 -3px; rotate: -45deg; }
.persp-menu__content :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.persp-menu__shield {
  position: absolute; inset: 0; z-index: 5; width: 100%; height: 100%; margin: 0; padding: 0; border: 0; border-radius: inherit;
  background: transparent; cursor: pointer; -webkit-tap-highlight-color: transparent;
}
.persp-menu__shield:focus-visible { outline: 3px solid var(--primary); outline-offset: -6px; }

/* Demo page content */
.persp-menu-demo { display: block; max-width: var(--container-max); margin-inline: auto; padding: clamp(1.5rem, 5vw, 4rem) var(--gutter) var(--space-2xl); }
.persp-menu-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.persp-menu-demo__title { max-width: 15ch; margin: 0.75rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 3.8vw, 4rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.persp-menu-demo__lead { max-width: 32rem; margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.persp-menu-demo__stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.75rem; max-width: 30rem; margin: var(--space-xl) 0 0; }
.persp-menu-demo__stats div { padding: 0.875rem 1rem; border-radius: var(--radius-xl); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.persp-menu-demo__stats dt { color: var(--text-muted); font-size: 0.75rem; }
.persp-menu-demo__stats dd { margin: 0.25rem 0 0; font: 600 1.5rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.persp-menu-demo__card { max-width: 30rem; margin-top: var(--space-lg); padding: 1.25rem; border-radius: var(--radius-2xl); background: var(--surface-light); box-shadow: var(--shadow-xl), inset 0 0 0 1px var(--border-subtle); }
.persp-menu-demo__card h3 { margin: 0; font: 600 1rem var(--font-display); letter-spacing: var(--tracking-tight); }
.persp-menu-demo__crew { display: grid; gap: 0.75rem; margin: var(--space-md) 0 0; padding: 0; list-style: none; }
.persp-menu-demo__crew li { display: flex; align-items: center; gap: 0.75rem; }
.persp-menu-demo__crew strong { display: block; font-size: 0.875rem; }
.persp-menu-demo__crew small { color: var(--text-muted); font-size: 0.75rem; }
.persp-menu-demo__avatar { display: grid; place-items: center; flex: none; width: 2.25rem; height: 2.25rem; border-radius: var(--radius-lg); background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-size: 0.6875rem; font-weight: 700; }

@media (scripting: none) { .persp-menu__toggle { display: none; } }
/* Failsafe: if the script never runs, the plain band comes back after 3s */
@media (scripting: enabled) {
  .persp-menu:not(.persp-menu--js) .persp-menu__nav { max-height: 0; overflow: hidden; visibility: hidden; animation: persp-menu-failsafe 0s 3s forwards; }
  .persp-menu:not(.persp-menu--js) .persp-menu__toggle { animation: persp-menu-failsafe-out 0s 3s forwards; }
}

/* Enhanced: the menu waits underneath, lit from behind the page */
.persp-menu--js .persp-menu__nav {
  position: fixed; inset: 0; z-index: 0; overflow-y: auto; overscroll-behavior: contain; visibility: hidden;
  background:
    radial-gradient(70% 55% at 85% 20%, color-mix(in srgb, var(--primary) 55%, transparent), transparent 70%),
    radial-gradient(60% 45% at 0% 100%, color-mix(in srgb, var(--primary-2) 26%, transparent), transparent 70%),
    linear-gradient(160deg, color-mix(in srgb, var(--surface-deep) 80%, var(--primary)), var(--surface-deep) 70%);
}
.persp-menu.is-active .persp-menu__nav { visibility: visible; }
.persp-menu--js .persp-menu__inner {
  display: flex; flex-direction: column; justify-content: center; width: var(--persp-menu-room); max-width: none; min-height: 100%; margin: 0;
  padding: calc(var(--persp-menu-bar) + var(--space-md)) var(--space-md) var(--space-xl) max(var(--gutter), calc((100vw - var(--container-max)) / 2 + var(--gutter)));
}
.persp-menu--js .persp-menu__list { flex-direction: column; flex-wrap: nowrap; gap: var(--space-xs); }
.persp-menu--js .persp-menu__link { font-size: clamp(1.875rem, 1.2rem + 3vw, 3rem); letter-spacing: var(--tracking-display); }
.persp-menu--js .persp-menu__contact { flex-direction: column; align-items: flex-start; gap: 0; margin-top: var(--space-xl); }
.persp-menu--js .persp-menu__book { margin-bottom: var(--space-sm); }

/* Links and contact slide in from the left, one after another */
.persp-menu--js :is(.persp-menu__eyebrow, .persp-menu__item, .persp-menu__contact) {
  opacity: 0; translate: -2.5rem 0;
  transition: opacity var(--dur-2) var(--ease-out), translate var(--dur-3) var(--ease-in-out);
}
.persp-menu.is-open :is(.persp-menu__eyebrow, .persp-menu__item, .persp-menu__contact) {
  opacity: 1; translate: 0 0;
  transition:
    opacity var(--dur-4) var(--ease-out) calc(var(--dur-2) + var(--persp-menu-i) * var(--stagger)),
    translate var(--dur-5) var(--ease-out) calc(var(--dur-2) + var(--persp-menu-i) * var(--stagger));
}

/* Active: the page is pinned as a viewport-sized card and its content becomes the scroller */
html:has(.persp-menu.is-active) { overflow: hidden; }
.persp-menu--js .persp-menu__page { transition: transform var(--dur-4) var(--ease-in-out), border-radius var(--dur-4) var(--ease-in-out), box-shadow var(--dur-4) var(--ease-in-out); }
.persp-menu.is-active .persp-menu__page {
  position: fixed; inset: 0; min-height: 0; overflow: hidden;
  transform: perspective(var(--persp-menu-depth)) translateX(0) scale(1) rotateY(0deg);
}
.persp-menu.is-active .persp-menu__content { height: 100%; overflow: hidden; }
/* Open: swept aside in 3D with rounded corners, a deep shadow and shading on the far edge */
.persp-menu.is-open .persp-menu__page {
  border-radius: var(--radius-2xl);
  transform: perspective(var(--persp-menu-depth)) translateX(var(--persp-menu-shift)) scale(var(--persp-menu-scale)) rotateY(var(--persp-menu-tilt));
  box-shadow: 0 50px 100px -30px color-mix(in srgb, var(--surface-deep) 90%, transparent), -24px 0 60px -30px color-mix(in srgb, var(--primary) 50%, transparent);
  transition-duration: var(--dur-5); transition-timing-function: var(--ease-out);
}
.persp-menu__page::after {
  content: ""; position: absolute; inset: 0; z-index: 4; pointer-events: none; opacity: 0;
  background: linear-gradient(90deg, color-mix(in srgb, var(--surface-deep) 34%, transparent), transparent 55%);
  transition: opacity var(--dur-4) var(--ease-in-out);
}
.persp-menu.is-open .persp-menu__page::after { opacity: 1; transition: opacity var(--dur-5) var(--ease-out); }

/* Ghost card: further back, more transparent, a beat behind the page */
.persp-menu--js .persp-menu__ghost {
  position: fixed; inset: 0; z-index: 1; display: block; border-radius: var(--radius-2xl); pointer-events: none; visibility: hidden; opacity: 0;
  background: linear-gradient(120deg, color-mix(in srgb, var(--surface-light) 26%, transparent), color-mix(in srgb, var(--surface-light) 8%, transparent));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 28%, transparent), 0 30px 60px -24px color-mix(in srgb, var(--surface-deep) 70%, transparent);
  transform: perspective(var(--persp-menu-depth)) translateX(0) scale(1) rotateY(0deg);
  transition: transform var(--dur-4) var(--ease-in-out), opacity var(--dur-3) var(--ease-out);
}
.persp-menu.is-active .persp-menu__ghost { visibility: visible; }
.persp-menu.is-open .persp-menu__ghost {
  opacity: 1;
  transform: perspective(var(--persp-menu-depth)) translateX(var(--persp-menu-ghost-shift)) scale(var(--persp-menu-ghost-scale)) rotateY(var(--persp-menu-tilt));
  transition: transform var(--dur-5) var(--ease-out) var(--stagger), opacity var(--dur-4) var(--ease-out) var(--stagger);
}

/* Desktop: a shorter push and flatter perspective give the menu a wide column */
@media (min-width: 768px) {
  .persp-menu {
    --persp-menu-shift: 40%; --persp-menu-scale: 0.8; --persp-menu-depth: 1800px;
    --persp-menu-ghost-shift: 31%; --persp-menu-ghost-scale: 0.7; --persp-menu-room: 48%; --persp-menu-bar: 4.75rem;
  }
}
/* Reduced motion: a plain slide, no 3D and no ghost (and instant, as the tokens collapse) */
@media (prefers-reduced-motion: reduce) {
  .persp-menu.is-open .persp-menu__page { transform: perspective(var(--persp-menu-depth)) translateX(calc(var(--persp-menu-shift) + 8%)) scale(1) rotateY(0deg); }
  .persp-menu--js .persp-menu__ghost { display: none; }
}

@keyframes persp-menu-failsafe { to { max-height: none; visibility: visible; } }
@keyframes persp-menu-failsafe-out { to { visibility: hidden; } }
```

## JS

```js
document.querySelectorAll('[data-persp-menu]').forEach((root, n) => {
  const nav = root.querySelector('.persp-menu__nav');
  const page = root.querySelector('.persp-menu__page');
  const content = root.querySelector('.persp-menu__content');
  const toggle = root.querySelector('.persp-menu__toggle');
  const shield = root.querySelector('.persp-menu__shield');
  const firstLink = nav.querySelector('a');
  let wantOpen = false;
  let timer = 0;
  root.classList.add('persp-menu--js');
  if (n) nav.id = `${nav.id}-${n + 1}`; // unique ids for repeated instances
  toggle.setAttribute('aria-controls', nav.id);

  const onKey = (e) => { if (e.key === 'Escape') { e.preventDefault(); close(); } };

  // Open: pin the page where it is (its content takes over the scroll offset), then push it back
  const open = () => {
    if (wantOpen) return;
    wantOpen = true;
    clearTimeout(timer);
    if (!root.classList.contains('is-active')) {
      const y = window.scrollY;
      root.classList.add('is-active');
      content.scrollTop = y;
    }
    content.inert = true;
    shield.hidden = false;
    toggle.setAttribute('aria-expanded', 'true');
    document.addEventListener('keydown', onKey);
    firstLink.focus({ preventScroll: true });
    requestAnimationFrame(() => requestAnimationFrame(() => { if (wantOpen) root.classList.add('is-open'); }));
  };

  // Close: swing back, then hand the scroll offset back to the document
  const close = () => {
    if (!wantOpen) return;
    wantOpen = false;
    root.classList.remove('is-open');
    content.inert = false;
    shield.hidden = true;
    toggle.setAttribute('aria-expanded', 'false');
    document.removeEventListener('keydown', onKey);
    toggle.focus({ preventScroll: true });
    const finish = () => {
      clearTimeout(timer);
      page.removeEventListener('transitionend', onEnd);
      if (wantOpen) return; // reopened while swinging back
      const y = content.scrollTop; // includes any same-page link the menu just followed
      root.classList.remove('is-active');
      window.scrollTo({ top: y, behavior: 'instant' });
    };
    const onEnd = (e) => { if (e.target === page && e.propertyName === 'transform') finish(); };
    page.addEventListener('transitionend', onEnd);
    timer = setTimeout(finish, 1200);
  };

  toggle.addEventListener('click', open);
  shield.addEventListener('click', close);
  nav.addEventListener('click', (e) => { if (e.target.closest('a')) close(); });
});
```

## Notes

- Model: the toggle has `aria-expanded` and `aria-controls` and reveals the `<nav>` underneath. While open, the page content is `inert` and a full-size transparent button labelled "Close menu" covers the pushed page. Escape, that button or following a link closes the menu. Focus moves to the first link on open and returns to the toggle on close. The nav is `visibility: hidden` whenever the page covers it.
- Transforms on `.persp-menu__page` break `position: fixed` inside it: while open, the page becomes the containing block for every fixed descendant, so fixed headers, chat bubbles or cookie bars inside it would ride along with the card or jump. Make the header `position: sticky`, as here, and keep truly fixed UI outside `.persp-menu__page`.
- Scrolling: on open, the page is pinned with `position: fixed` and its content takes over the current scroll offset, so the 3D push acts on a viewport-sized card. `html:has(.persp-menu.is-active)` locks everything else. On close, the document scroll returns to wherever the content ended up, so same-page links in the menu still land on their target.
- Wiring a real page: make `.persp-menu` the first child of `<body>` holding `__nav`, `__ghost` and `__page`. Move your existing header, `<main>` and footer into `.persp-menu__content`, keep the shield as the last child of `__page`, and give the page an opaque background.
- No JS (`@media (scripting: none)`): the toggle is hidden and the menu renders as a deep band of links and contact details above the page. A 3s CSS failsafe does the same if the module never runs. Reduced motion: no rotation, scale or ghost. The page simply sits slid aside, and the change is instant.
- Contrast: the menu column sits on the darker side of the gradient (no lighter than about 20% `--primary` in `--surface-deep`). `--text-inverse` reads at about 16:1 there and `--text-inverse-muted` at 5:1 or better (over the teal glow at the bottom). The brand glow is placed behind the pushed page, away from text. Retune the push with `--persp-menu-shift`, `--persp-menu-scale`, `--persp-menu-tilt` and `--persp-menu-depth`.
