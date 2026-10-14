# Theme Switch

A sun/moon switch that flips the whole page between light and dark. The icon morphs (the rays retract and a masked circle slides in to carve the crescent), while the new theme spreads across the page as a circle growing out of the switch, revealing a starlit sky in the demo hero. The choice persists, defaults to the OS setting, and is applied before first paint. On phones the switch sits alone in the header, at a full 44px. Depends on `tokens/variables.css`.

**Motion:** circular View Transition reveal from the switch (`--dur-5`, `--ease-out`) · rays retract with a spin, core swells and the crescent mask slides in (`--dur-4`, `--ease-spring` / `--ease-out`) · stars pop in staggered (`--stagger`) · hover tilt and press squash (`--ease-spring`).

## HTML

```html
<div class="theme-switch-demo">
  <div class="theme-switch-demo__bar">
    <div class="theme-switch-demo__inner theme-switch-demo__bar-inner">
      <a class="theme-switch-demo__logo" href="#">
        <span class="theme-switch-demo__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z" /></svg></span>
        Brand
      </a>
      <nav class="theme-switch-demo__nav" aria-label="Main">
        <a href="#">Services</a><a href="#">Reviews</a><a href="#">Contact</a>
      </nav>
      <button class="theme-switch" type="button" role="switch" aria-checked="false" aria-label="Dark mode">
        <svg class="theme-switch__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
          <mask id="theme-switch-mask" maskUnits="userSpaceOnUse" x="0" y="0" width="24" height="24">
            <rect width="24" height="24" fill="white" />
            <circle class="theme-switch__bite" cx="17" cy="8" r="7.5" fill="black" />
          </mask>
          <g mask="url(#theme-switch-mask)"><circle class="theme-switch__core" cx="12" cy="12" r="4.5" /></g>
          <path class="theme-switch__rays" d="M12 1.75v2.5M12 19.75v2.5M1.75 12h2.5M19.75 12h2.5M4.75 4.75l1.77 1.77M17.48 17.48l1.77 1.77M4.75 19.25l1.77-1.77M17.48 6.52l1.77-1.77" />
          <path class="theme-switch__star" d="m19.5 1.25.55 1.45 1.45.55-1.45.55-.55 1.45-.55-1.45-1.45-.55 1.45-.55z" />
          <path class="theme-switch__star theme-switch__star--late" d="m22.25 9.25.35.9.9.35-.9.35-.35.9-.35-.9-.9-.35.9-.35z" />
        </svg>
      </button>
    </div>
  </div>

  <div class="theme-switch-demo__hero">
    <div class="theme-switch-demo__sky" aria-hidden="true"></div>
    <div class="theme-switch-demo__inner">
      <p class="theme-switch-demo__eyebrow">Heating &amp; cooling · Springfield</p>
      <h2 class="theme-switch-demo__title">Comfort at home, day or night.</h2>
      <p class="theme-switch-demo__lead">Boilers serviced, AC tuned and leaks fixed by licensed local engineers. The night line stays open until 11pm.</p>
      <div class="theme-switch-demo__actions">
        <a class="theme-switch-demo__btn" href="#book">
          Book a visit
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="theme-switch-demo__link" href="tel:+15555550123">(555) 555-0123</a>
      </div>

      <ul class="theme-switch-demo__cards" role="list">
        <li class="theme-switch-demo__card">
          <span class="theme-switch-demo__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.4-.5-2-1-3-1.1-2.1-.2-4.1 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.2.4-2.3 1-3a2.5 2.5 0 0 0 2.5 2.5z" /></svg></span>
          <h3>Heating</h3>
          <p>Boiler services and repairs, booked the same week.</p>
          <span class="theme-switch-demo__meta">from $119</span>
        </li>
        <li class="theme-switch-demo__card">
          <span class="theme-switch-demo__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M12 2v20M4.5 6.5l15 11M19.5 6.5l-15 11M9 3.5l3 2.5 3-2.5M9 20.5l3-2.5 3 2.5" /></svg></span>
          <h3>Cooling</h3>
          <p>AC tune-ups for Westlake and Riverside before the summer rush.</p>
          <span class="theme-switch-demo__meta">from $99</span>
        </li>
        <li class="theme-switch-demo__card">
          <span class="theme-switch-demo__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11z" /></svg></span>
          <h3>Night line</h3>
          <p>Burst pipe after dinner? A real engineer answers until 11pm.</p>
          <span class="theme-switch-demo__meta">(555) 555-0123</span>
        </li>
      </ul>
    </div>
  </div>
</div>
```

## CSS

```css
/* Dark theme: surface and text tokens flip, built only from existing tokens; everything that uses them follows */
:root[data-theme="dark"] {
  color-scheme: dark;
  --surface-light: color-mix(in srgb, var(--surface-deep) 70%, var(--surface-dark));
  --surface-muted: color-mix(in srgb, var(--surface-dark) 94%, var(--text-inverse-muted));
  --text-main: var(--text-inverse);
  --text-muted: var(--text-inverse-muted);
  --border-subtle: color-mix(in srgb, var(--surface-dark) 78%, var(--text-inverse-muted));
  --highlight: var(--highlight-inverse);
  --shadow-sm: 0 1px 2px color-mix(in srgb, var(--surface-deep) 60%, transparent);
  --shadow-md: 0 4px 12px -2px color-mix(in srgb, var(--surface-deep) 70%, transparent);
  --shadow-lg: 0 12px 28px -6px color-mix(in srgb, var(--surface-deep) 80%, transparent);
  --shadow-xl:
    0 1px 2px color-mix(in srgb, var(--surface-deep) 50%, transparent),
    0 16px 40px -8px color-mix(in srgb, var(--surface-deep) 80%, transparent),
    0 40px 80px -20px color-mix(in srgb, var(--surface-deep) 90%, transparent);
  --focus-ring: 0 0 0 3px color-mix(in srgb, var(--primary) 65%, var(--text-inverse));
  --theme-switch-night: 1; /* 0 in light: lets decorative art swap with the theme */
}

/* The new theme grows as a circle out of the switch (centre and radius set by JS) */
::view-transition-old(theme-switch) { animation: none; mix-blend-mode: normal; }
::view-transition-new(theme-switch) { animation: theme-switch-reveal var(--dur-5) var(--ease-out) both; mix-blend-mode: normal; }

/* Focus colour that adapts: darker blue on light, lighter blue on dark (≥ 6:1 either way) */
.theme-switch, .theme-switch-demo { --theme-switch-ring: color-mix(in srgb, var(--primary) 70%, var(--text-main)); }

/* Switch: a sunlit (or moonlit) glass button */
.theme-switch {
  --theme-switch-glow: color-mix(in srgb, var(--accent) 50%, transparent);
  position: relative; flex: none; display: inline-grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: radial-gradient(circle at 32% 28%, color-mix(in srgb, var(--accent) 20%, var(--surface-light)), var(--surface-light) 72%);
  color: color-mix(in srgb, var(--accent) 40%, var(--warning));
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm), 0 8px 24px -10px var(--theme-switch-glow);
  transition: color var(--dur-3), box-shadow var(--dur-4) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
:root[data-theme="dark"] .theme-switch {
  --theme-switch-glow: color-mix(in srgb, var(--primary) 60%, transparent);
  background: radial-gradient(circle at 32% 28%, color-mix(in srgb, var(--primary) 28%, var(--surface-light)), var(--surface-light) 72%);
  color: color-mix(in srgb, var(--text-main) 85%, var(--primary));
}
.theme-switch:hover { box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md), 0 10px 30px -8px var(--theme-switch-glow); }
.theme-switch:active { transform: scale(0.92); }
.theme-switch:focus-visible { outline: 2px solid var(--theme-switch-ring); outline-offset: 3px; }

/* Icon morph: rays retract and spin away, the core swells, a mask circle slides in to carve the crescent.
   Keyed to :root[data-theme] (set before paint), so the icon is already right on first render. */
.theme-switch__icon { fill: none; stroke: none; overflow: visible; transition: rotate var(--dur-4) var(--ease-spring); }
@media (hover: hover) { .theme-switch:hover .theme-switch__icon { rotate: 20deg; } }
.theme-switch__core { fill: currentColor; transform-box: fill-box; transform-origin: center; transition: transform var(--dur-4) var(--ease-spring); }
.theme-switch__bite { transform: translate(7px, -7px); transition: transform var(--dur-4) var(--ease-out); }
.theme-switch__rays {
  stroke: currentColor; stroke-width: 2; stroke-linecap: round; transform-box: view-box; transform-origin: 12px 12px;
  transition: transform var(--dur-4) var(--ease-spring) calc(var(--stagger) * 2), opacity var(--dur-3) var(--ease-out) calc(var(--stagger) * 2);
}
.theme-switch__star { fill: currentColor; opacity: 0; transform: scale(0); transform-box: fill-box; transform-origin: center; transition: transform var(--dur-3) var(--ease-out), opacity var(--dur-2); }
:root[data-theme="dark"] .theme-switch .theme-switch__core { transform: scale(2); }
:root[data-theme="dark"] .theme-switch .theme-switch__bite { transform: none; }
:root[data-theme="dark"] .theme-switch .theme-switch__rays { opacity: 0; transform: rotate(-90deg) scale(0.4); transition-delay: 0s; }
:root[data-theme="dark"] .theme-switch .theme-switch__star {
  opacity: 1; transform: none;
  transition: transform var(--dur-4) var(--ease-spring) calc(var(--stagger) * 3), opacity var(--dur-3) var(--ease-out) calc(var(--stagger) * 3);
}
:root[data-theme="dark"] .theme-switch .theme-switch__star--late { transition-delay: calc(var(--stagger) * 5); }

/* Demo mini page: every colour comes from the flipped tokens */
.theme-switch-demo {
  --theme-switch-ink: color-mix(in srgb, var(--primary) 65%, var(--text-main));
  --theme-switch-muted: color-mix(in srgb, var(--text-muted) 70%, var(--text-main));
  overflow: clip; background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
}
.theme-switch-demo__mark svg, .theme-switch-demo__icon svg, .theme-switch-demo__btn svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.theme-switch-demo__inner { max-width: var(--container-max); margin-inline: auto; padding-inline: var(--gutter); }
.theme-switch-demo__bar { position: relative; z-index: 1; border-bottom: 1px solid var(--border-subtle); }
.theme-switch-demo__bar-inner { display: flex; align-items: center; gap: 1.75rem; height: 4.25rem; }
.theme-switch-demo__logo {
  display: inline-flex; align-items: center; gap: 0.625rem; margin-right: auto; border-radius: var(--radius-md);
  color: var(--text-main); font: 600 1.125rem var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none;
}
.theme-switch-demo__mark { display: grid; place-items: center; width: 2.125rem; height: 2.125rem; border-radius: 0.75rem; background: var(--gradient-brand); color: var(--text-inverse); box-shadow: var(--highlight), var(--shadow-glow); }
.theme-switch-demo__nav { display: none; gap: 1.75rem; }
.theme-switch-demo__nav a { border-radius: var(--radius-sm); color: var(--theme-switch-muted); font-size: 0.9375rem; font-weight: 500; text-decoration: none; transition: color var(--dur-2); }
.theme-switch-demo__nav a:hover { color: var(--text-main); }
.theme-switch-demo a:focus-visible { outline: 2px solid var(--theme-switch-ring); outline-offset: 3px; }

/* Hero sky: warm sun glow by day, moon glow and stars by night */
.theme-switch-demo__hero { position: relative; isolation: isolate; padding-block: clamp(3rem, 8vw, 5.5rem) clamp(3rem, 7vw, 5rem); }
.theme-switch-demo__sky { position: absolute; inset: 0; z-index: -1; pointer-events: none; }
.theme-switch-demo__sky::before, .theme-switch-demo__sky::after { content: ""; position: absolute; inset: 0; }
.theme-switch-demo__sky::before {
  opacity: calc(1 - var(--theme-switch-night, 0));
  background:
    radial-gradient(28rem circle at 88% -10%, color-mix(in srgb, var(--accent) 26%, transparent), transparent 60%),
    radial-gradient(40rem circle at 5% 115%, color-mix(in srgb, var(--primary-2) 10%, transparent), transparent 60%);
}
.theme-switch-demo__sky::after {
  opacity: var(--theme-switch-night, 0);
  background:
    radial-gradient(1.5px 1.5px at 12% 18%, var(--text-inverse), transparent),
    radial-gradient(1px 1px at 28% 8%, var(--text-inverse), transparent),
    radial-gradient(1.5px 1.5px at 46% 24%, color-mix(in srgb, var(--text-inverse) 70%, transparent), transparent),
    radial-gradient(1px 1px at 63% 10%, var(--text-inverse), transparent),
    radial-gradient(2px 2px at 76% 30%, var(--text-inverse), transparent),
    radial-gradient(1px 1px at 93% 14%, color-mix(in srgb, var(--text-inverse) 70%, transparent), transparent),
    radial-gradient(1.5px 1.5px at 68% 50%, color-mix(in srgb, var(--text-inverse) 60%, transparent), transparent),
    radial-gradient(28rem circle at 88% -10%, color-mix(in srgb, var(--primary) 32%, transparent), transparent 60%);
  -webkit-mask-image: linear-gradient(black 40%, transparent);
  mask-image: linear-gradient(black 40%, transparent);
}
.theme-switch-demo__eyebrow { margin: 0; color: var(--theme-switch-ink); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.theme-switch-demo__title { max-width: 14ch; margin: 0.875rem 0 0; font: 600 clamp(2.25rem, 1.3rem + 4.2vw, 4.25rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.theme-switch-demo__lead { max-width: 34rem; margin: 1.25rem 0 0; color: var(--theme-switch-muted); font-size: 1.0625rem; line-height: 1.6; }
.theme-switch-demo__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem 1.5rem; margin-top: 2rem; }
.theme-switch-demo__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; border-radius: 999px;
  background: var(--primary); color: var(--text-inverse); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 25%, transparent), var(--shadow-glow);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2);
}
.theme-switch-demo__btn:hover { background: var(--primary-hover); transform: translateY(-1px); }
.theme-switch-demo__btn:active { transform: scale(0.97); }
.theme-switch-demo__link {
  border-radius: var(--radius-sm); color: var(--text-main); font-weight: 600;
  text-decoration: underline; text-decoration-color: color-mix(in srgb, var(--text-main) 30%, transparent); text-underline-offset: 0.25em;
}
.theme-switch-demo__cards { display: grid; gap: 1rem; margin: 3rem 0 0; padding: 0; list-style: none; }
.theme-switch-demo__card { padding: 1.375rem; border-radius: var(--radius-xl); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm); }
.theme-switch-demo__icon {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 0.75rem;
  background: color-mix(in srgb, var(--primary) 14%, var(--surface-light)); color: var(--theme-switch-ink);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 20%, transparent);
}
.theme-switch-demo__card h3 { margin: 1rem 0 0; font: 600 1.0625rem/1.3 var(--font-display); letter-spacing: var(--tracking-tight); }
.theme-switch-demo__card p { margin: 0.375rem 0 0; color: var(--theme-switch-muted); font-size: 0.9375rem; line-height: 1.55; }
.theme-switch-demo__meta { display: inline-block; margin-top: 1rem; font: 500 0.8125rem var(--font-mono); }

@media (min-width: 768px) {
  .theme-switch-demo__nav { display: flex; }
  .theme-switch-demo__cards { grid-template-columns: repeat(3, 1fr); }
}
/* No JS, no switch: the page keeps the default theme */
@media (scripting: none) { .theme-switch { display: none; } }
@media (prefers-reduced-motion: reduce) { ::view-transition-new(theme-switch) { animation: none; } }

@keyframes theme-switch-reveal {
  from { clip-path: circle(0 at var(--theme-switch-x, 50%) var(--theme-switch-y, 0)); }
  to { clip-path: circle(var(--theme-switch-r, 150vmax) at var(--theme-switch-x, 50%) var(--theme-switch-y, 0)); }
}
```

## JS

```js
const KEY = 'theme';
const root = document.documentElement;
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const osDark = matchMedia('(prefers-color-scheme: dark)');
const switches = [...document.querySelectorAll('.theme-switch')];
const valid = (t) => (t === 'dark' || t === 'light' ? t : null);
const stored = () => { try { return valid(localStorage.getItem(KEY)); } catch { return null; } };

// Apply a theme and reflect it on every switch on the page
const apply = (theme) => {
  root.dataset.theme = theme;
  switches.forEach((s) => s.setAttribute('aria-checked', String(theme === 'dark')));
};

// The new theme grows as a circle out of the switch; without View Transitions (or with reduced motion) it swaps instantly
const toggle = (btn) => {
  const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
  try { localStorage.setItem(KEY, next); } catch { /* storage blocked: the theme still applies for this visit */ }
  if (!document.startViewTransition || reduce.matches) return apply(next);
  const r = btn.getBoundingClientRect();
  const x = r.left + r.width / 2;
  const y = r.top + r.height / 2;
  root.style.setProperty('--theme-switch-x', `${x}px`);
  root.style.setProperty('--theme-switch-y', `${y}px`);
  root.style.setProperty('--theme-switch-r', `${Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y))}px`);
  root.style.viewTransitionName = 'theme-switch';
  document.startViewTransition(() => apply(next)).finished.finally(() => { root.style.viewTransitionName = ''; });
};

switches.forEach((s, i) => {
  const mask = s.querySelector('mask');
  mask.id = `theme-switch-mask-${i}`; // unique per instance
  s.querySelector('[mask]').setAttribute('mask', `url(#${mask.id})`);
  s.addEventListener('click', () => toggle(s));
});

// The <head> snippet normally set data-theme before paint; this also covers pages without it
apply(valid(root.dataset.theme) || stored() || (osDark.matches ? 'dark' : 'light'));
osDark.addEventListener('change', (e) => { if (!stored()) apply(e.matches ? 'dark' : 'light'); });
addEventListener('storage', (e) => { if (e.key === KEY && valid(e.newValue)) apply(e.newValue); });
```

## Notes

- **Install:** paste this into `<head>` before your stylesheets so the right theme is set before first paint: `<script>(function () { var t; try { t = localStorage.getItem('theme'); } catch (e) {} document.documentElement.dataset.theme = t === 'dark' || t === 'light' ? t : (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'); })();</script>`. Give your page background `var(--surface-light)` and text `var(--text-main)` so the page itself follows the tokens. Put the button anywhere. Several switches stay in sync, and so do other open tabs.
- **Tokens:** `:root[data-theme="dark"]` overrides `--surface-light`, `--surface-muted`, `--text-main`, `--text-muted`, `--border-subtle`, `--highlight`, `--shadow-sm/md/lg/xl`, `--focus-ring` and `color-scheme`. Everything is mixed from existing tokens, and `--glass` follows automatically. To extend, add more overrides to the same block. `--primary` is kept so white-on-primary buttons stay at 5.2:1. For small brand-coloured text, use `color-mix(in srgb, var(--primary) 65%, var(--text-main))`, which is the demo's `--theme-switch-ink` (7.5:1 light, 6.7:1 dark). `--theme-switch-night` (0 or 1) lets artwork such as the demo sky swap with the theme.
- **Contrast in dark:** `--text-main` 18:1, `--text-muted` 7.4:1 on the page and 6.4:1 on `--surface-muted`, and the demo's muted text 8.6:1. The focus outline is ≥ 6:1. The sun icon is 3.5:1 against the light button.
- **Accessibility:** a `<button role="switch">` named "Dark mode", with `aria-checked` kept in sync. The icon keys off `:root[data-theme]`, so it's right on first paint and never morphs on load. Space and Enter toggle it, and the focus outline is recoloured per theme.
- **Support:** the circular reveal uses View Transitions (Chromium 111+, Safari 18+, Firefox 144+). Elsewhere, and under reduced motion, the swap is instant and the icon morph collapses with the motion tokens. Without JS the switch is hidden by `@media (scripting: none)` and the page keeps the default theme. To follow the OS without JS, repeat the token block inside `@media (prefers-color-scheme: dark) { :root:not([data-theme]) { … } }`.
