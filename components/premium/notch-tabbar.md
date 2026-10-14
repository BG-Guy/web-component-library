# Liquid Notch Tab Bar

A bottom tab bar with five tabs where the active icon lifts out of the bar into a glossy brand-gradient bubble that floats in a curved notch. Switching tabs slides the notch and the bubble together on one spring, and the bubble squishes like liquid as it travels. The old icon drops back into the bar, the new one rises into the bubble, and its label fades in beneath. Full-bleed above the home indicator on phones; it becomes a floating rounded bar from 768px. Depends on `tokens/variables.css`.

**Motion:** notch and bubble glide on one registered index (`--dur-4`, `--ease-spring`) · bubble squash-and-stretch (`--dur-4`, `--ease-out`) · icon drop and delayed rise (`--dur-4`, `--ease-spring`) · label fade-up (`--dur-3`) · press squash (`--ease-spring`).

## HTML

```html
<div class="notch-tabs-demo">
  <div class="notch-tabs-demo__screen">
    <header class="notch-tabs-demo__head">
      <div>
        <p class="notch-tabs-demo__hello">Hi Alex · Westlake</p>
        <h2 class="notch-tabs-demo__title">What needs fixing today?</h2>
      </div>
      <span class="notch-tabs-demo__avatar" aria-hidden="true">AK</span>
    </header>

    <article class="notch-tabs-demo__eta">
      <div class="notch-tabs-demo__eta-row">
        <span class="notch-tabs-demo__tech" aria-hidden="true">SK</span>
        <p><strong>Sam is on the way</strong><span>Leak repair · Northside crew</span></p>
        <span class="notch-tabs-demo__mins">12 min</span>
      </div>
      <div class="notch-tabs-demo__route" aria-hidden="true"><span></span></div>
    </article>

    <ul class="notch-tabs-demo__grid" role="list">
      <li class="notch-tabs-demo__card"><strong>Plumbing</strong><span>Leaks, boilers, drains</span><small>from $89</small></li>
      <li class="notch-tabs-demo__card"><strong>Heating</strong><span>Service and repair</span><small>from $119</small></li>
      <li class="notch-tabs-demo__card"><strong>Electrical</strong><span>Sockets to rewires</span><small>from $95</small></li>
      <li class="notch-tabs-demo__card"><strong>Roofing</strong><span>Tiles, gutters, flashing</span><small>from $140</small></li>
    </ul>
    <p class="notch-tabs-demo__note">Licensed and insured across Springfield · (555) 555-0123</p>
  </div>

  <nav class="notch-tabs" aria-label="Main" data-notch-tabs data-notch-tabs-demo>
    <div class="notch-tabs__bg" aria-hidden="true"></div>
    <div class="notch-tabs__track" aria-hidden="true">
      <span class="notch-tabs__slot"><span class="notch-tabs__bubble"></span></span>
    </div>
    <ul class="notch-tabs__list" role="list">
      <li class="notch-tabs__item">
        <a class="notch-tabs__link" href="/" aria-current="page">
          <span class="notch-tabs__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M3 10.5 12 3l9 7.5" /><path d="M5.5 9v11a1 1 0 0 0 1 1H10v-6h4v6h3.5a1 1 0 0 0 1-1V9" /></svg></span>
          <span class="notch-tabs__label">Home</span>
        </a>
      </li>
      <li class="notch-tabs__item">
        <a class="notch-tabs__link" href="/services">
          <span class="notch-tabs__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z" /></svg></span>
          <span class="notch-tabs__label">Services</span>
        </a>
      </li>
      <li class="notch-tabs__item">
        <a class="notch-tabs__link" href="/book">
          <span class="notch-tabs__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /><path d="M8.5 14.5 11 17l4.5-4.5" /></svg></span>
          <span class="notch-tabs__label">Book</span>
        </a>
      </li>
      <li class="notch-tabs__item">
        <a class="notch-tabs__link" href="/messages">
          <span class="notch-tabs__icon">
            <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20.5l1.4-4.9A8 8 0 1 1 21 12z" /></svg>
            <span class="notch-tabs__badge" aria-hidden="true">2</span>
          </span>
          <span class="notch-tabs__label">Messages</span><span class="notch-tabs__sr">, 2 unread</span>
        </a>
      </li>
      <li class="notch-tabs__item">
        <a class="notch-tabs__link" href="/account">
          <span class="notch-tabs__icon"><svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><circle cx="12" cy="8" r="4" /><path d="M4 21a8 8 0 0 1 16 0" /></svg></span>
          <span class="notch-tabs__label">Account</span>
        </a>
      </li>
    </ul>
  </nav>
</div>
```

## CSS

```css
@property --notch-tabs-i { syntax: "<number>"; inherits: true; initial-value: 0; }

/* Demo screen: a light app home with the bar pinned to the bottom edge */
.notch-tabs-demo {
  display: flex; flex-direction: column; min-height: 100vh; min-height: 100svh;
  background: radial-gradient(30rem 18rem at 100% 0%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 70%), var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.notch-tabs-demo__screen { flex: 1; width: 100%; max-width: min(var(--container-max), 40rem); margin-inline: auto; padding: var(--space-lg) var(--gutter) 3.5rem; }
.notch-tabs-demo__head { display: flex; align-items: flex-start; justify-content: space-between; gap: var(--space-md); }
.notch-tabs-demo__hello { margin: 0; color: var(--text-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.04em; }
.notch-tabs-demo__title { margin: 0.625rem 0 0; font: 600 clamp(1.75rem, 1.3rem + 2vw, 2.5rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.notch-tabs-demo__avatar { flex: none; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%; background: var(--gradient-brand); color: var(--text-inverse); font-size: 0.8125rem; font-weight: 700; box-shadow: 0 0 0 3px var(--surface-light), var(--shadow-md); }

.notch-tabs-demo__eta {
  margin-top: var(--space-lg); padding: var(--space-md); border-radius: var(--radius-2xl); color: var(--text-inverse);
  background: radial-gradient(80% 120% at 100% 0%, color-mix(in srgb, var(--primary) 55%, transparent), transparent 70%), var(--surface-deep);
  box-shadow: var(--highlight-inverse), var(--shadow-xl);
}
.notch-tabs-demo__eta-row { display: flex; align-items: center; gap: 0.75rem; }
.notch-tabs-demo__eta-row p { flex: 1; min-width: 0; margin: 0; }
.notch-tabs-demo__eta-row strong { display: block; font-size: 0.9375rem; }
.notch-tabs-demo__eta-row p span { color: var(--text-inverse-muted); font-size: 0.8125rem; }
.notch-tabs-demo__tech { flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: var(--radius-lg); background: var(--gradient-brand); font-size: 0.75rem; font-weight: 700; }
.notch-tabs-demo__mins { flex: none; padding: 0.3125rem 0.5rem; border-radius: var(--radius-full); background: color-mix(in srgb, var(--success) 30%, transparent); font: 600 0.75rem/1 var(--font-mono); }
.notch-tabs-demo__route { height: 0.375rem; margin-top: var(--space-md); overflow: hidden; border-radius: var(--radius-full); background: var(--glass-inverse); }
.notch-tabs-demo__route span { display: block; width: 64%; height: 100%; border-radius: inherit; background: var(--gradient-brand); box-shadow: 0 0 12px color-mix(in srgb, var(--primary-2) 70%, transparent); }

.notch-tabs-demo__grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.625rem; margin: var(--space-md) 0 0; padding: 0; list-style: none; }
.notch-tabs-demo__card { display: grid; gap: 0.25rem; padding: var(--space-md); border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-sm); }
.notch-tabs-demo__card::before {
  content: ""; width: 2rem; height: 2rem; margin-bottom: 0.5rem; border-radius: var(--radius-md); box-shadow: var(--highlight);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 22%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 30%, var(--surface-light)));
}
.notch-tabs-demo__card:nth-child(2)::before { background: linear-gradient(135deg, color-mix(in srgb, var(--accent) 35%, var(--surface-light)), color-mix(in srgb, var(--danger) 22%, var(--surface-light))); }
.notch-tabs-demo__card:nth-child(3)::before { background: linear-gradient(135deg, color-mix(in srgb, var(--accent) 45%, var(--surface-light)), color-mix(in srgb, var(--primary) 18%, var(--surface-light))); }
.notch-tabs-demo__card:nth-child(4)::before { background: linear-gradient(135deg, color-mix(in srgb, var(--primary-2) 30%, var(--surface-light)), color-mix(in srgb, var(--success) 22%, var(--surface-light))); }
.notch-tabs-demo__card strong { font: 600 1rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.notch-tabs-demo__card span { color: var(--text-muted); font-size: 0.8125rem; line-height: 1.35; }
.notch-tabs-demo__card small { margin-top: 0.375rem; color: var(--primary); font: 600 0.75rem/1 var(--font-mono); }
.notch-tabs-demo__note { margin: var(--space-lg) 0 0; color: var(--text-muted); font-size: 0.8125rem; text-align: center; }

/* Bar: one animated index drives the notch, the bubble and nothing else */
.notch-tabs {
  --notch-tabs-n: 5;
  --notch-tabs-cup: 2.25rem;        /* R: notch radius */
  --notch-tabs-fillet: 0.75rem;     /* r: shoulder radius */
  --notch-tabs-span: 2.905rem;      /* √(R² + 2Rr): where each shoulder leaves the flat edge */
  --notch-tabs-tangent: 0.5625rem;  /* R·r ÷ (R + r): depth where the shoulder meets the cup */
  --notch-tabs-rise: 2.125rem;      /* how far the active icon climbs into the bubble */
  --notch-tabs-pad-l: max(var(--space-sm), env(safe-area-inset-left, 0px));
  --notch-tabs-pad-r: max(var(--space-sm), env(safe-area-inset-right, 0px));
  --notch-tabs-x: calc(var(--notch-tabs-pad-l) + (100% - var(--notch-tabs-pad-l) - var(--notch-tabs-pad-r)) * (var(--notch-tabs-i) + 0.5) / var(--notch-tabs-n));
  position: sticky; bottom: 0; z-index: var(--z-sticky);
  padding-bottom: env(safe-area-inset-bottom, 0px);
  font-family: var(--font-sans);
  transition: --notch-tabs-i var(--dur-4) var(--ease-spring);
}
/* No-JS: the index comes straight from aria-current in the markup (JS sets it inline when present) */
.notch-tabs:has(.notch-tabs__item:nth-child(2) > [aria-current="page"]) { --notch-tabs-i: 1; }
.notch-tabs:has(.notch-tabs__item:nth-child(3) > [aria-current="page"]) { --notch-tabs-i: 2; }
.notch-tabs:has(.notch-tabs__item:nth-child(4) > [aria-current="page"]) { --notch-tabs-i: 3; }
.notch-tabs:has(.notch-tabs__item:nth-child(5) > [aria-current="page"]) { --notch-tabs-i: 4; }

/* The light plate, notched by a mask. Union of: the bar outside the notch, two shoulder discs,
   and everything outside the cup below the shoulder tangent. The parent's drop-shadows trace the curve. */
.notch-tabs__bg {
  position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  filter: drop-shadow(0 -1px 0 color-mix(in srgb, var(--text-main) 10%, transparent)) drop-shadow(0 -10px 22px color-mix(in srgb, var(--text-main) 9%, transparent));
}
.notch-tabs__bg::before {
  --notch-tabs-mask:
    linear-gradient(to right, black calc(var(--notch-tabs-x) - var(--notch-tabs-span)), transparent 0 calc(var(--notch-tabs-x) + var(--notch-tabs-span)), black 0) no-repeat,
    radial-gradient(circle at calc(var(--notch-tabs-x) - var(--notch-tabs-span)) var(--notch-tabs-fillet), black calc(var(--notch-tabs-fillet) - 0.5px), transparent var(--notch-tabs-fillet)) no-repeat,
    radial-gradient(circle at calc(var(--notch-tabs-x) + var(--notch-tabs-span)) var(--notch-tabs-fillet), black calc(var(--notch-tabs-fillet) - 0.5px), transparent var(--notch-tabs-fillet)) no-repeat,
    radial-gradient(circle at var(--notch-tabs-x) calc(-1 * var(--notch-tabs-tangent)), transparent calc(var(--notch-tabs-cup) - 0.5px), black var(--notch-tabs-cup)) 0 var(--notch-tabs-tangent) / 100% 100% no-repeat;
  content: ""; position: absolute; inset: 0; border-radius: inherit;
  background: linear-gradient(180deg, var(--surface-light) 55%, color-mix(in srgb, var(--surface-light) 70%, var(--surface-muted)));
  box-shadow: var(--highlight);
  -webkit-mask: var(--notch-tabs-mask); mask: var(--notch-tabs-mask);
}

/* Bubble: a cell-wide slot slides by whole cells; the gradient drop floats in the cup */
.notch-tabs__track { position: absolute; top: 0; left: var(--notch-tabs-pad-l); right: var(--notch-tabs-pad-r); z-index: 1; pointer-events: none; }
.notch-tabs__slot { position: absolute; top: 0; left: 0; width: calc(100% / var(--notch-tabs-n)); translate: calc(var(--notch-tabs-i) * 100%) 0; }
.notch-tabs__bubble {
  position: absolute; left: 50%; top: -0.125rem; width: 3.5rem; height: 3.5rem; margin: -1.75rem 0 0 -1.75rem; border-radius: 50%;
  background: radial-gradient(110% 110% at 30% 18%, color-mix(in srgb, var(--primary) 65%, var(--surface-light)), var(--primary) 42%, var(--primary-2));
  box-shadow:
    var(--highlight), inset 0 -0.375rem 0.75rem -0.25rem color-mix(in srgb, var(--surface-deep) 35%, transparent),
    0 0.75rem 1.5rem -0.5rem color-mix(in srgb, var(--primary) 75%, transparent), 0 0.25rem 0.5rem -0.25rem color-mix(in srgb, var(--primary-2) 60%, transparent);
}
.notch-tabs__bubble::before { /* specular glint */
  content: ""; position: absolute; left: 20%; top: 12%; width: 36%; height: 22%; border-radius: 50%; rotate: -24deg;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--surface-light) 70%, transparent), transparent);
}
.notch-tabs__bubble.is-moving { animation: notch-tabs-squish var(--dur-4) var(--ease-out); }

/* Tabs */
.notch-tabs__list { display: grid; grid-template-columns: repeat(var(--notch-tabs-n), minmax(0, 1fr)); margin: 0; padding: 0 var(--notch-tabs-pad-r) 0 var(--notch-tabs-pad-l); list-style: none; }
.notch-tabs__link {
  position: relative; display: block; height: 4rem; border-radius: var(--radius-xl);
  color: var(--text-muted); text-decoration: none; -webkit-tap-highlight-color: transparent;
}
.notch-tabs__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.notch-tabs__link[aria-current="page"] { color: var(--primary); }
.notch-tabs__icon {
  position: absolute; left: 50%; top: 50%; z-index: 0; display: grid; place-items: center; width: 1.5rem; height: 1.5rem;
  translate: -50% -50%;
  transition: translate var(--dur-4) var(--ease-spring), color var(--dur-3) var(--ease-out), scale var(--dur-3) var(--ease-spring);
}
.notch-tabs__icon svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
/* The new icon rises a beat after the bubble sets off; the old one drops straight back */
.notch-tabs__link[aria-current="page"] .notch-tabs__icon {
  z-index: 2; color: var(--text-inverse); translate: -50% calc(-50% - var(--notch-tabs-rise));
  transition-delay: var(--stagger), var(--stagger), 0s;
}
.notch-tabs__link:active .notch-tabs__icon { scale: 0.86; }
@media (hover: hover) {
  .notch-tabs__link:not([aria-current]):hover { color: var(--text-main); }
  .notch-tabs__link:not([aria-current]):hover .notch-tabs__icon { translate: -50% calc(-50% - 0.125rem); }
}
.notch-tabs__label {
  position: absolute; left: 50%; bottom: 0.5rem; max-width: 100%;
  font: 600 0.6875rem/1 var(--font-sans); letter-spacing: 0.01em; white-space: nowrap;
  opacity: 0; translate: -50% 0.375rem;
  transition: opacity var(--dur-2) var(--ease-out), translate var(--dur-4) var(--ease-spring);
}
.notch-tabs__link[aria-current="page"] .notch-tabs__label { opacity: 1; translate: -50% 0; transition-duration: var(--dur-3), var(--dur-4); transition-delay: calc(var(--stagger) * 2); }
.notch-tabs__badge {
  position: absolute; top: -0.375rem; right: -0.5rem; min-width: 1rem; height: 1rem; padding: 0 0.25rem; border-radius: var(--radius-full);
  background: var(--danger); color: var(--text-inverse); font: 700 0.625rem/1rem var(--font-mono); text-align: center;
  box-shadow: 0 0 0 2px var(--surface-light);
}
.notch-tabs__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* From 768px: a floating rounded bar */
@media (min-width: 768px) {
  .notch-tabs {
    --notch-tabs-pad-l: 1.25rem; --notch-tabs-pad-r: 1.25rem;
    width: min(100% - 2rem, 30rem); margin: 0 auto var(--space-lg); bottom: var(--space-lg); padding-bottom: 0; border-radius: var(--radius-xl);
  }
  .notch-tabs__bg { filter: drop-shadow(0 0 1px color-mix(in srgb, var(--text-main) 16%, transparent)) drop-shadow(0 16px 32px color-mix(in srgb, var(--text-main) 14%, transparent)); }
}

@media (prefers-reduced-motion: reduce) {
  .notch-tabs *, .notch-tabs *::before, .notch-tabs *::after { animation: none !important; }
}

@keyframes notch-tabs-squish {
  0% { scale: 1; }
  30% { scale: 1.22 0.84; }
  62% { scale: 0.95 1.05; }
  100% { scale: 1; }
}
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-notch-tabs]').forEach((nav) => {
  const links = [...nav.querySelectorAll('.notch-tabs__link')];
  const bubble = nav.querySelector('.notch-tabs__bubble');
  nav.style.setProperty('--notch-tabs-n', links.length);

  // One source of truth: aria-current on the link, plus the index the notch and bubble follow
  const select = (index) => {
    links.forEach((link, i) => (i === index ? link.setAttribute('aria-current', 'page') : link.removeAttribute('aria-current')));
    nav.style.setProperty('--notch-tabs-i', index);
  };
  select(Math.max(0, links.findIndex((link) => link.getAttribute('aria-current') === 'page')));

  // The demo (data-notch-tabs-demo) switches tabs in place; a real site lets the links navigate
  links.forEach((link, i) => link.addEventListener('click', (e) => {
    if (!nav.hasAttribute('data-notch-tabs-demo')) return;
    e.preventDefault();
    if (link.getAttribute('aria-current') === 'page') return;
    select(i);
    if (reduce.matches) return;
    bubble.classList.remove('is-moving');
    void bubble.offsetWidth; // restart the squish
    bubble.classList.add('is-moving');
  }));
  bubble.addEventListener('animationend', () => bubble.classList.remove('is-moving'));
});
```

## Notes

- **Accessibility:** a labelled `<nav>` with real links in a `role="list"`; the active link has `aria-current="page"` and the notch is pure decoration (`aria-hidden`). Labels of inactive tabs are only faded out visually. They stay in the accessibility tree as each link's name, and Messages reads "Messages, 2 unread". Each cell is a full 64px-tall target with a `--focus-ring` on keyboard focus.
- **Geometry:** the notch is four mask layers on the plate: the bar outside the notch band, two shoulder discs of radius r, and the area outside the cup of radius R below the shoulders' tangent depth. If you change `--notch-tabs-cup` or `--notch-tabs-fillet`, recompute `--notch-tabs-span` (√(R² + 2Rr)) and `--notch-tabs-tangent` (R·r ÷ (R + r)). Keep the bubble radius 6–10px smaller than R.
- **Motion model:** the only animated value is the registered `--notch-tabs-i`. The mask position and the bubble's slot both derive from it, so they can never drift apart. Without `@property` support the notch jumps instead of gliding. Reduced motion makes everything instant and drops the squish.
- **No JS:** `:has()` reads `aria-current` from the markup, so the static bar shows the right notch and lifted icon (supports up to five tabs; JS sets the index inline for any count).
- **Contrast:** inactive icons use `--text-muted` (4.8:1), the active label is `--primary` (5.2:1), and the white icon on the bubble stays above 3.7:1 across the gradient. The badge is `--text-inverse` on `--danger` (4.8:1).
- **Wiring:** keep the nav as the last child of the page wrapper (sticky, so it reserves its own height) and add `viewport-fit=cover` for the safe-area padding. Leave room for the bubble, which rises 30px above the bar. Drop `data-notch-tabs-demo` so links navigate, and render `aria-current` per page.
