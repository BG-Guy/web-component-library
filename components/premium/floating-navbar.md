# Floating Navbar

Detached glass navbar that tightens as the page scrolls. A pill glides between links on hover and rests on the current page. On mobile, the menu opens as a full-screen panel revealed in a circle from the toggle, with links rising in sequence. Depends on `tokens/variables.css`.

**Motion:** bar narrows and lifts on scroll (`--dur-5`, ease-out) · hover pill springs between links · burger morphs into an X · circular clip-path reveal · staggered link rise with blur.

## HTML

```html
<header class="glass-nav" data-glass-nav>
  <nav class="glass-nav__bar" aria-label="Primary">
    <a class="glass-nav__brand" href="/">
      <span class="glass-nav__logo" aria-hidden="true"></span>
      Brand
    </a>

    <div class="glass-nav__track">
      <span class="glass-nav__pill" aria-hidden="true"></span>
      <ul class="glass-nav__links" role="list">
        <li><a href="#services" aria-current="page">Services</a></li>
        <li><a href="#work">Our work</a></li>
        <li><a href="#pricing">Pricing</a></li>
        <li><a href="#reviews">Reviews</a></li>
      </ul>
    </div>

    <a class="glass-nav__cta" href="#quote">
      Get a quote
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
    </a>

    <button class="glass-nav__toggle" type="button" aria-label="Open menu" aria-haspopup="dialog"
            aria-controls="glass-nav-menu" hidden>
      <span class="glass-nav__burger" aria-hidden="true"></span>
    </button>
  </nav>

  <dialog class="glass-nav__menu" id="glass-nav-menu" aria-label="Menu">
    <div class="glass-nav__menu-top">
      <a class="glass-nav__brand" href="/"><span class="glass-nav__logo" aria-hidden="true"></span>Brand</a>
      <button class="glass-nav__close" type="button" aria-label="Close menu" autofocus>
        <span class="glass-nav__burger glass-nav__burger--x" aria-hidden="true"></span>
      </button>
    </div>
    <ul class="glass-nav__menu-links" role="list">
      <li style="--i: 0"><a href="#services" aria-current="page">Services <span aria-hidden="true">→</span></a></li>
      <li style="--i: 1"><a href="#work">Our work <span aria-hidden="true">→</span></a></li>
      <li style="--i: 2"><a href="#pricing">Pricing <span aria-hidden="true">→</span></a></li>
      <li style="--i: 3"><a href="#reviews">Reviews <span aria-hidden="true">→</span></a></li>
    </ul>
    <div class="glass-nav__menu-foot" style="--i: 4">
      <a class="glass-nav__menu-cta" href="#quote">Get a free quote</a>
      <p>(555) 555-0123 · hello@example.com</p>
    </div>
  </dialog>
</header>
```

## CSS

```css
/* Shell: sticky and transparent, so only the floating bar catches clicks */
.glass-nav {
  position: sticky; top: 0; z-index: var(--z-sticky);
  padding: 0.75rem var(--gutter) 0;
  pointer-events: none;
  font-family: var(--font-sans);
}
.glass-nav__bar {
  pointer-events: auto;
  display: flex; align-items: center; gap: 0.75rem;
  max-width: 72rem; height: 3.75rem; margin-inline: auto; padding: 0 0.5rem 0 1rem;
  border: 1px solid color-mix(in srgb, var(--text-main) 8%, transparent);
  border-radius: 1.25rem;
  background: var(--surface-light);
  box-shadow: var(--shadow-sm), var(--highlight);
  transition: max-width var(--dur-5) var(--ease-out), height var(--dur-4) var(--ease-out),
              box-shadow var(--dur-4) var(--ease-out), background-color var(--dur-4);
}
@supports (backdrop-filter: blur(1px)) {
  .glass-nav__bar { background: var(--glass); backdrop-filter: saturate(1.6) blur(var(--blur-md)); }
}
/* Scrolled: narrower, shorter, floating higher */
.glass-nav[data-scrolled] .glass-nav__bar { max-width: 58rem; height: 3.25rem; box-shadow: var(--shadow-xl), var(--highlight); }

/* Brand mark: gradient tile with an open ring */
.glass-nav__brand {
  display: inline-flex; align-items: center; gap: 0.625rem; flex: none; margin-right: auto;
  color: var(--text-main); font: 650 1.0625rem/1 var(--font-display); letter-spacing: -0.02em; text-decoration: none;
}
.glass-nav__logo {
  position: relative; width: 1.75rem; height: 1.75rem; border-radius: 0.5rem;
  background: var(--gradient-brand);
  box-shadow: var(--highlight), 0 6px 16px -6px color-mix(in srgb, var(--primary) 70%, transparent);
}
.glass-nav__logo::after {
  content: ""; position: absolute; inset: 0.4375rem; border-radius: 50%;
  border: 2px solid var(--surface-light); border-right-color: transparent; transform: rotate(-45deg);
}

/* Desktop links with the gliding hover pill */
.glass-nav__track { position: relative; justify-self: center; }
.glass-nav__links { position: relative; display: flex; gap: 0.125rem; margin: 0; padding: 0; list-style: none; }
.glass-nav__links a {
  display: block; padding: 0.5rem 0.875rem; border-radius: 999px;
  color: var(--text-muted); font-size: 0.9375rem; font-weight: 500; text-decoration: none;
  transition: color var(--dur-2);
}
.glass-nav__links a:hover, .glass-nav__links [aria-current="page"] { color: var(--text-main); }
.glass-nav__pill {
  position: absolute; top: 0; bottom: 0; left: 0;
  width: var(--w, 0); transform: translateX(var(--x, 0)); opacity: 0;
  border-radius: 999px; background: color-mix(in srgb, var(--text-main) 6%, transparent);
  transition: transform var(--dur-4) var(--ease-spring), width var(--dur-4) var(--ease-spring), opacity var(--dur-2);
}

/* Ink CTA with an arrow that nudges forward */
.glass-nav__cta {
  display: none; align-items: center; gap: 0.375rem; justify-self: end; flex: none;
  height: 2.5rem; padding: 0 0.875rem 0 1rem; border-radius: 999px;
  background: var(--text-main); color: var(--surface-light);
  font-size: 0.875rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight-inverse), 0 6px 16px -8px color-mix(in srgb, var(--text-main) 60%, transparent);
  transition: transform var(--dur-2) var(--ease-out), box-shadow var(--dur-3);
}
.glass-nav__cta svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.glass-nav__cta:hover { transform: translateY(-1px); }
.glass-nav__cta:hover svg { transform: translateX(3px); }
.glass-nav__cta:active { transform: scale(0.97); }

/* Toggle and burger lines (two-line burger morphs into an X) */
.glass-nav__toggle, .glass-nav__close {
  display: grid; place-items: center; flex: none; width: 2.75rem; height: 2.75rem; padding: 0;
  border: 0; border-radius: 0.875rem; background: transparent; color: inherit; cursor: pointer;
  transition: background-color var(--dur-2);
}
.glass-nav__toggle { color: var(--text-main); }
.glass-nav__toggle[hidden] { display: none; }
.glass-nav__toggle:hover { background: color-mix(in srgb, var(--text-main) 6%, transparent); }
.glass-nav__burger { position: relative; display: block; width: 1.125rem; height: 0.625rem; }
.glass-nav__burger::before, .glass-nav__burger::after {
  content: ""; position: absolute; left: 0; right: 0; height: 2px; border-radius: 2px; background: currentColor;
  transition: top var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring);
}
.glass-nav__burger::before { top: 0; }
.glass-nav__burger::after { top: calc(100% - 2px); }
.glass-nav__menu[data-state="open"] .glass-nav__burger--x::before { top: calc(50% - 1px); transform: rotate(45deg); transition-delay: 120ms; }
.glass-nav__menu[data-state="open"] .glass-nav__burger--x::after { top: calc(50% - 1px); transform: rotate(-45deg); transition-delay: 120ms; }

/* Focus */
.glass-nav a:focus-visible, .glass-nav button:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.glass-nav__menu a:focus-visible, .glass-nav__menu button:focus-visible { box-shadow: none; outline: 2px solid var(--text-inverse); outline-offset: 2px; }

/* Full-screen menu: circular reveal from the toggle */
.glass-nav__menu {
  pointer-events: auto;
  position: fixed; inset: 0; width: 100%; max-width: none; height: 100%; max-height: none; margin: 0;
  padding: calc(env(safe-area-inset-top, 0px) + 0.75rem) var(--gutter) calc(env(safe-area-inset-bottom, 0px) + 2rem);
  border: 0; color: var(--text-inverse);
  background:
    radial-gradient(60% 40% at 100% 0%, color-mix(in srgb, var(--primary) 35%, transparent), transparent 70%),
    radial-gradient(55% 35% at 0% 100%, color-mix(in srgb, var(--primary-2) 28%, transparent), transparent 70%),
    var(--surface-deep);
  clip-path: circle(0 at var(--glass-nav-x, 100%) var(--glass-nav-y, 0));
  transition: clip-path var(--dur-4) var(--ease-in-out);
}
.glass-nav__menu[open] { display: flex; flex-direction: column; gap: 2rem; }
.glass-nav__menu[data-state="open"] { clip-path: circle(150vmax at var(--glass-nav-x, 100%) var(--glass-nav-y, 0)); transition: clip-path var(--dur-5) var(--ease-out); }
.glass-nav__menu::backdrop { background: transparent; }
html:has(.glass-nav__menu[open]) { overflow: hidden; }

.glass-nav__menu-top {
  display: flex; align-items: center; justify-content: space-between;
  width: 100%; max-width: 72rem; height: 3.75rem; margin-inline: auto; padding: 0 0.5rem 0 1rem;
}
.glass-nav__menu .glass-nav__brand { color: var(--text-inverse); }
.glass-nav__close:hover { background: var(--glass-inverse); }

/* Menu links rise in sequence */
.glass-nav__menu-links { display: grid; margin: 0; padding: 0 0.25rem; list-style: none; }
.glass-nav__menu-links li, .glass-nav__menu-foot {
  opacity: 0; transform: translateY(1.25rem); filter: blur(6px);
  transition: opacity var(--dur-4) var(--ease-out), transform var(--dur-5) var(--ease-out), filter var(--dur-4) var(--ease-out);
}
.glass-nav__menu[data-state="open"] :is(.glass-nav__menu-links li, .glass-nav__menu-foot) {
  opacity: 1; transform: none; filter: none;
  transition-delay: calc(var(--i) * var(--stagger) + 160ms);
}
.glass-nav__menu-links a {
  display: flex; align-items: center; justify-content: space-between; gap: 1rem;
  padding-block: 0.875rem; border-bottom: 1px solid var(--border-inverse);
  color: var(--text-inverse); text-decoration: none;
  font: 600 clamp(1.875rem, 9vw, 2.75rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight);
}
.glass-nav__menu-links a span { font-size: 0.6em; opacity: 0.4; transition: transform var(--dur-3) var(--ease-spring), opacity var(--dur-2); }
.glass-nav__menu-links a:hover span, .glass-nav__menu-links a:focus-visible span { transform: translateX(6px); opacity: 1; }
.glass-nav__menu-links [aria-current="page"] {
  background: linear-gradient(100deg, var(--text-inverse), color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.glass-nav__menu-foot { display: grid; gap: 1rem; margin-top: auto; padding-inline: 0.25rem; }
.glass-nav__menu-foot p { margin: 0; color: var(--text-inverse-muted); font-size: 0.9375rem; }
.glass-nav__menu-cta {
  display: flex; align-items: center; justify-content: center; height: 3.25rem; border-radius: 999px;
  background: var(--surface-light); color: var(--text-main); font-weight: 600; text-decoration: none;
  box-shadow: 0 12px 32px -12px color-mix(in srgb, var(--primary) 80%, transparent);
}

/* Without JS on small screens: links wrap under the brand instead of hiding */
.glass-nav:not(.glass-nav--js) .glass-nav__bar { flex-wrap: wrap; height: auto; padding-block: 0.5rem; }
.glass-nav:not(.glass-nav--js) .glass-nav__track { overflow-x: auto; }
.glass-nav--js .glass-nav__track { display: none; }

@media (min-width: 480px) {
  .glass-nav__cta { display: inline-flex; }
}
@media (min-width: 768px) {
  .glass-nav__bar, .glass-nav:not(.glass-nav--js) .glass-nav__bar {
    display: grid; grid-template-columns: 1fr auto 1fr; flex-wrap: nowrap; height: 3.75rem; padding-block: 0;
  }
  .glass-nav--js .glass-nav__track { display: block; }
  .glass-nav__toggle, .glass-nav__toggle:not([hidden]) { display: none; }
}
```

## JS

```js
document.querySelectorAll('[data-glass-nav]').forEach((nav) => {
  nav.classList.add('glass-nav--js');

  // Compact the bar once the page scrolls
  let queued = false;
  const onScroll = () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => { nav.toggleAttribute('data-scrolled', scrollY > 8); queued = false; });
  };
  addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Hover pill: glides to the hovered or focused link, rests on the current page
  const track = nav.querySelector('.glass-nav__track');
  const pill = nav.querySelector('.glass-nav__pill');
  const current = track.querySelector('[aria-current="page"]');
  let target = current;
  const place = (link, instant) => {
    target = link;
    const jump = instant || pill.style.opacity !== '1'; // appear in place rather than slide in from 0
    if (jump) pill.style.transition = 'none';
    pill.style.opacity = link ? '1' : '0';
    if (link) {
      pill.style.setProperty('--x', `${link.offsetLeft}px`);
      pill.style.setProperty('--w', `${link.offsetWidth}px`);
    }
    if (jump) { void pill.offsetWidth; pill.style.transition = ''; }
  };
  track.addEventListener('pointerover', (e) => { const a = e.target.closest('a'); if (a) place(a); });
  track.addEventListener('pointerleave', () => place(current));
  track.addEventListener('focusin', (e) => place(e.target.closest('a')));
  track.addEventListener('focusout', (e) => { if (!track.contains(e.relatedTarget)) place(current); });
  new ResizeObserver(() => place(target, true)).observe(track);

  // Mobile menu: circle reveal from the toggle, links stagger in, animated close
  const toggle = nav.querySelector('.glass-nav__toggle');
  const menu = nav.querySelector('.glass-nav__menu');
  toggle.hidden = false;
  toggle.addEventListener('click', () => {
    const r = toggle.getBoundingClientRect();
    menu.style.setProperty('--glass-nav-x', `${r.left + r.width / 2}px`);
    menu.style.setProperty('--glass-nav-y', `${r.top + r.height / 2}px`);
    menu.showModal();
    requestAnimationFrame(() => requestAnimationFrame(() => { menu.dataset.state = 'open'; }));
  });
  const close = () => {
    if (menu.dataset.state !== 'open') return;
    delete menu.dataset.state;
    const finish = () => {
      clearTimeout(timer);
      menu.removeEventListener('transitionend', onEnd);
      if (menu.open) menu.close();
      toggle.focus();
    };
    const onEnd = (e) => { if (e.target === menu) finish(); };
    const timer = setTimeout(finish, 1200);
    menu.addEventListener('transitionend', onEnd);
  };
  menu.addEventListener('cancel', (e) => { e.preventDefault(); close(); });
  menu.addEventListener('click', (e) => { if (e.target.closest('a, .glass-nav__close')) close(); });
  matchMedia('(min-width: 768px)').addEventListener('change', (e) => {
    if (e.matches && menu.open) { delete menu.dataset.state; menu.close(); }
  });
});
```

## Notes

- The mobile menu is a modal `<dialog>`, so focus is trapped, the page behind is inert, and Escape closes it (with the reverse animation). Focus returns to the toggle.
- The toggle ships `hidden` and the script reveals it. Without JS the links wrap under the brand on small screens, so navigation never disappears.
- The glass needs something behind it to read as glass: it's designed to float over a hero or colourful content. Browsers without `backdrop-filter` get a solid bar.
- Keep it to 4–5 links. For dropdowns, use `morphing-dropdown.md` inside the track.
- **React:** keep the same markup; run the script body in a `useEffect` keyed on the header ref and return a cleanup that removes the scroll listener.
