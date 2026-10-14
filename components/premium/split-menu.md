# Split-Screen Menu

A full-screen menu that closes in like two halves of a stage set. Two deep panels slide in from opposite sides until they meet, a glowing edge marking the seam, and then huge numbered links rise out of their masks one after another. On desktop, a large vivid preview window sits on the right: gradient art, a caption and two mini stats. As you hover or focus each link, it swaps with a clip-path wipe that follows the direction you're moving through the list. On phones it becomes a single pane: the panels meet top and bottom, the active link reveals a short inline descriptor, and the preview shrinks to a slim strip at the bottom. Depends on `tokens/variables.css`.

**Motion:** panels slide in from opposite sides (`--dur-4` + `--ease-out`) with a seam glint · links rise from masks (`--dur-5` + `--ease-out`, `--stagger`) · preview wipe-in on open and a directional clip-path wipe between previews, with an art settle · descriptor clip wipe · two-line burger springs into an × (`--ease-spring`) · content drops before the panels retract on close (`--ease-in-out`).

## HTML

```html
<div class="split-menu-demo">
  <header class="split-menu" data-split-menu>
    <div class="split-menu__bar">
      <a class="split-menu__logo" href="#"><span class="split-menu__mark" aria-hidden="true"></span>Brand</a>
      <button class="split-menu__toggle" type="button" aria-expanded="false" aria-controls="split-menu-panel" aria-label="Menu">
        <span class="split-menu__burger" aria-hidden="true"></span>
      </button>
    </div>

    <nav class="split-menu__panel" id="split-menu-panel" aria-label="Main">
      <span class="split-menu__shutter split-menu__shutter--a" aria-hidden="true"></span>
      <span class="split-menu__shutter split-menu__shutter--b" aria-hidden="true"></span>

      <div class="split-menu__body">
        <ul class="split-menu__list" role="list">
          <li class="split-menu__item" style="--split-menu-i: 0">
            <a class="split-menu__link" href="#services" aria-current="page">
              <span class="split-menu__num" aria-hidden="true">01</span>
              <span class="split-menu__mask"><span class="split-menu__word">Services</span></span>
              <span class="split-menu__desc" aria-hidden="true">Repairs, installs and upgrades</span>
              <svg class="split-menu__arrow" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </li>
          <li class="split-menu__item" style="--split-menu-i: 1">
            <a class="split-menu__link" href="#projects">
              <span class="split-menu__num" aria-hidden="true">02</span>
              <span class="split-menu__mask"><span class="split-menu__word">Projects</span></span>
              <span class="split-menu__desc" aria-hidden="true">Kitchens, baths and heat pumps</span>
              <svg class="split-menu__arrow" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </li>
          <li class="split-menu__item" style="--split-menu-i: 2">
            <a class="split-menu__link" href="#about">
              <span class="split-menu__num" aria-hidden="true">03</span>
              <span class="split-menu__mask"><span class="split-menu__word">About</span></span>
              <span class="split-menu__desc" aria-hidden="true">Family-run in Springfield since 1998</span>
              <svg class="split-menu__arrow" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </li>
          <li class="split-menu__item" style="--split-menu-i: 3">
            <a class="split-menu__link" href="#reviews">
              <span class="split-menu__num" aria-hidden="true">04</span>
              <span class="split-menu__mask"><span class="split-menu__word">Reviews</span></span>
              <span class="split-menu__desc" aria-hidden="true">4.9 from 1,200+ homeowners</span>
              <svg class="split-menu__arrow" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </li>
          <li class="split-menu__item" style="--split-menu-i: 4">
            <a class="split-menu__link" href="#contact">
              <span class="split-menu__num" aria-hidden="true">05</span>
              <span class="split-menu__mask"><span class="split-menu__word">Contact</span></span>
              <span class="split-menu__desc" aria-hidden="true">Same-day callouts, 7 days</span>
              <svg class="split-menu__arrow" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </li>
        </ul>

        <!-- Decorative preview: one slide per link, in the same order -->
        <div class="split-menu__preview" aria-hidden="true">
          <div class="split-menu__slide">
            <div class="split-menu__art split-menu__art--1"><span>01</span></div>
            <div class="split-menu__caption"><p>Repairs, installs and upgrades across Springfield.</p><div class="split-menu__stats"><span><b>40+</b> services</span><span><b>2 hr</b> arrival window</span></div></div>
          </div>
          <div class="split-menu__slide">
            <div class="split-menu__art split-menu__art--2"><span>02</span></div>
            <div class="split-menu__caption"><p>Latest: a whole-home heat pump retrofit in Westlake.</p><div class="split-menu__stats"><span><b>320</b> projects in 2025</span><span><b>12 yr</b> warranty</span></div></div>
          </div>
          <div class="split-menu__slide">
            <div class="split-menu__art split-menu__art--3"><span>03</span></div>
            <div class="split-menu__caption"><p>Family-run since 1998, now 24 licensed pros.</p><div class="split-menu__stats"><span><b>1998</b> founded</span><span><b>24</b> technicians</span></div></div>
          </div>
          <div class="split-menu__slide">
            <div class="split-menu__art split-menu__art--4"><span>04</span></div>
            <div class="split-menu__caption"><p>"Quick, tidy and explained everything." Maria R., Northside</p><div class="split-menu__stats"><span><b>4.9</b> average</span><span><b>1,200+</b> reviews</span></div></div>
          </div>
          <div class="split-menu__slide">
            <div class="split-menu__art split-menu__art--5"><span>05</span></div>
            <div class="split-menu__caption"><p>Riverside, Northside, Westlake and all of Springfield.</p><div class="split-menu__stats"><span><b>15 min</b> reply time</span><span><b>7</b> days a week</span></div></div>
          </div>
        </div>

        <div class="split-menu__contact">
          <a href="tel:+15555550123">
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
            (555) 555-0123
          </a>
          <a class="split-menu__email" href="mailto:hello@example.com">
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM22 6l-10 7L2 6" /></svg>
            <span class="split-menu__email-text">hello@example.com</span>
          </a>
          <a class="split-menu__social" href="https://instagram.com/" aria-label="Brand on Instagram">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zM16 11.4A4 4 0 1 1 12.6 8a4 4 0 0 1 3.4 3.4zM17.5 6.5h.01" /></svg>
          </a>
          <a class="split-menu__social" href="https://facebook.com/" aria-label="Brand on Facebook">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" /></svg>
          </a>
        </div>
      </div>
    </nav>
  </header>

  <main class="split-menu-demo__page">
    <p class="split-menu-demo__eyebrow">Services</p>
    <h2 class="split-menu-demo__title">Everything your home needs, one call away.</h2>
    <p class="split-menu-demo__lead">Plumbing, heating and electrical work by licensed Springfield pros, with upfront prices and a two-hour arrival window.</p>
    <div class="split-menu-demo__art" aria-hidden="true">
      <span class="split-menu-demo__chip">Licensed &amp; insured</span>
      <span class="split-menu-demo__chip">Same-day slots</span>
    </div>
  </main>
</div>
```

## CSS

```css
/* Demo page behind the menu (light) */
.split-menu-demo { min-height: 100vh; min-height: 100svh; background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.split-menu-demo__page { max-width: var(--container-max); margin-inline: auto; padding: clamp(1.5rem, 5vw, 4rem) var(--gutter) var(--space-2xl); }
.split-menu-demo__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.split-menu-demo__title { max-width: 16ch; margin: 0.75rem 0 0; font: 600 clamp(2.25rem, 1.4rem + 3.8vw, 4rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.split-menu-demo__lead { max-width: 34rem; margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.split-menu-demo__art {
  display: flex; flex-wrap: wrap; align-items: flex-end; gap: var(--space-sm); min-height: 13rem; margin-top: var(--space-xl); padding: var(--space-md);
  border-radius: var(--radius-2xl); box-shadow: var(--shadow-xl);
  background:
    radial-gradient(70% 90% at 15% 20%, color-mix(in srgb, var(--primary) 85%, transparent), transparent 70%),
    radial-gradient(60% 80% at 90% 90%, color-mix(in srgb, var(--primary-2) 80%, transparent), transparent 70%),
    var(--surface-deep);
}
.split-menu-demo__chip { padding: 0.375rem 0.75rem; border-radius: var(--radius-full); background: var(--glass); box-shadow: var(--highlight); color: var(--text-main); font-size: 0.8125rem; font-weight: 600; }

/* Header: sticky with JS; the panel inside is fixed, so no transform or filter may sit on this element */
.split-menu { --split-menu-bar: 4.25rem; --split-menu-split: 56%; position: relative; z-index: var(--z-sticky); font-family: var(--font-sans); }
.split-menu--js { position: sticky; top: 0; }
.split-menu.is-open { z-index: var(--z-overlay); }
html:has(.split-menu.is-open) { overflow: hidden; }

/* Bar: glass over the page, transparent over the open menu (colours wait for the panels on close) */
.split-menu__bar {
  position: relative; z-index: 1; display: flex; align-items: center; justify-content: space-between; gap: var(--space-md);
  height: var(--split-menu-bar); padding-inline: max(var(--gutter), calc((100% - var(--container-max)) / 2 + var(--gutter)));
  color: var(--text-main); transition: color var(--dur-3) var(--ease-out) var(--dur-4);
}
.split-menu__bar::before {
  content: ""; position: absolute; inset: 0; z-index: -1; box-shadow: inset 0 -1px 0 var(--border-subtle);
  background: var(--glass); -webkit-backdrop-filter: blur(var(--blur-md)) saturate(1.6); backdrop-filter: blur(var(--blur-md)) saturate(1.6);
  transition: opacity var(--dur-3) var(--ease-out) var(--dur-4);
}
.split-menu.is-open .split-menu__bar { color: var(--text-inverse); transition-delay: 0s; }
.split-menu.is-open .split-menu__bar::before { opacity: 0; transition-delay: 0s; }
.split-menu__logo { display: inline-flex; align-items: center; gap: 0.625rem; min-height: 2.75rem; color: inherit; font: 600 1.125rem var(--font-display); letter-spacing: var(--tracking-tight); text-decoration: none; }
.split-menu__mark { width: 1.25rem; height: 1.25rem; border-radius: var(--radius-sm); background: linear-gradient(90deg, var(--primary) 50%, var(--primary-2) 50%); box-shadow: var(--highlight); }
.split-menu :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.split-menu.is-open .split-menu__bar :is(a, button):focus-visible, .split-menu__panel :is(a, button):focus-visible { outline-color: var(--text-inverse); }

/* Two-line burger: lines meet in the middle, then spring into an × */
.split-menu__toggle {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: transparent; color: inherit; box-shadow: inset 0 0 0 1px color-mix(in srgb, currentColor 20%, transparent);
  transition: background-color var(--dur-2), scale var(--dur-3) var(--ease-spring);
}
.split-menu__toggle:hover { background: color-mix(in srgb, currentColor 8%, transparent); }
.split-menu__toggle:active { scale: 0.92; }
.split-menu__burger { position: relative; width: 1.125rem; height: 0.5rem; }
.split-menu__burger::before, .split-menu__burger::after {
  content: ""; position: absolute; left: 0; width: 100%; height: 2px; border-radius: 2px; background: currentColor;
  transition: rotate var(--dur-3) var(--ease-out), translate var(--dur-3) var(--ease-spring) var(--dur-2);
}
.split-menu__burger::before { top: 0; }
.split-menu__burger::after { bottom: 0; }
.split-menu.is-open .split-menu__burger::before, .split-menu.is-open .split-menu__burger::after { transition: translate var(--dur-3) var(--ease-out), rotate var(--dur-4) var(--ease-spring) var(--dur-2); }
.split-menu.is-open .split-menu__burger::before { translate: 0 3px; rotate: 45deg; }
.split-menu.is-open .split-menu__burger::after { translate: 0 -3px; rotate: -45deg; }

/* Without JS: a deep band under the bar with numbered links and contact */
.split-menu__panel { position: relative; background: var(--surface-deep); color: var(--text-inverse); }
.split-menu__shutter, .split-menu__preview, .split-menu__arrow { display: none; }
.split-menu__body { max-width: var(--container-max); margin-inline: auto; padding: var(--space-lg) var(--gutter) var(--space-xl); }
.split-menu__list { display: grid; gap: var(--space-xs); margin: 0; padding: 0; list-style: none; }
.split-menu__link { display: flex; align-items: flex-start; gap: 0.75rem; padding-block: 0.125rem; border-radius: var(--radius-md); color: var(--text-inverse); text-decoration: none; }
.split-menu__num { flex: none; min-width: 1.5rem; padding-top: 0.5rem; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); transition: color var(--dur-2); }
.split-menu__mask { display: block; overflow: clip; padding-bottom: 0.06em; }
.split-menu__word { display: block; font: 600 clamp(2rem, 1.3rem + 4vw, 2.75rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); transition: color var(--dur-3) var(--ease-out); }
.split-menu__desc { align-self: center; max-width: 9.5rem; color: var(--text-inverse-muted); font-size: 0.8125rem; line-height: 1.35; }
.split-menu__contact { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-sm); margin-top: var(--space-lg); }
.split-menu__contact a {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; min-width: 2.75rem; min-height: 2.75rem; padding: 0 0.875rem;
  border-radius: var(--radius-full); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  color: var(--text-inverse); font: 500 0.8125rem var(--font-mono); text-decoration: none; transition: background-color var(--dur-2);
}
.split-menu__contact a:hover { background: color-mix(in srgb, var(--text-inverse) 12%, transparent); }
.split-menu__contact svg { flex: none; fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.split-menu__contact :is(.split-menu__social, .split-menu__email) { padding: 0; }
.split-menu__email-text { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

@media (scripting: none) { .split-menu__toggle { display: none; } }
/* Failsafe: if the script never runs, the plain band comes back after 3s */
@media (scripting: enabled) {
  .split-menu:not(.split-menu--js) .split-menu__panel { max-height: 0; overflow: hidden; visibility: hidden; animation: split-menu-failsafe 0s 3s forwards; }
  .split-menu:not(.split-menu--js) .split-menu__toggle { animation: split-menu-failsafe-out 0s 3s forwards; }
}

/* Enhanced: a fixed full-screen panel under the bar */
.split-menu--js .split-menu__panel {
  position: fixed; inset: 0; z-index: 0; overflow: hidden; background: none;
  visibility: hidden; transition: visibility 0s calc(var(--dur-4) + var(--dur-2));
}
.split-menu--js.is-open .split-menu__panel { visibility: visible; transition-delay: 0s; }

/* Two panels slide in from opposite sides (top/bottom on phones) and meet; content leaves first on close */
.split-menu--js .split-menu__shutter {
  position: absolute; left: 0; right: 0; display: block; height: calc(50% + 1px);
  background: radial-gradient(90% 70% at 0% 0%, color-mix(in srgb, var(--primary) 24%, transparent), transparent 70%), var(--surface-deep);
  transition: transform var(--dur-4) var(--ease-in-out) var(--dur-2);
}
.split-menu--js .split-menu__shutter--a { top: 0; transform: translateY(-100%); }
.split-menu--js .split-menu__shutter--b {
  bottom: 0; transform: translateY(100%);
  background: radial-gradient(90% 70% at 100% 100%, color-mix(in srgb, var(--primary-2) 20%, transparent), transparent 70%), var(--surface-deep);
}
.split-menu--js.is-open .split-menu__shutter { transform: none; transition: transform var(--dur-4) var(--ease-out); }
/* Glint on the leading edge of the second panel; it fades once the panels meet */
.split-menu--js .split-menu__shutter--b::before {
  content: ""; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)), transparent);
  box-shadow: 0 0 18px 2px color-mix(in srgb, var(--primary-2) 55%, transparent);
  transition: opacity var(--dur-5) var(--ease-out);
}
.split-menu--js.is-open .split-menu__shutter--b::before { opacity: 0; transition-delay: var(--dur-4); }

.split-menu--js .split-menu__body {
  position: relative; display: flex; flex-direction: column; gap: var(--space-lg); height: 100%; max-width: none;
  padding: calc(var(--split-menu-bar) + var(--space-sm)) var(--gutter) max(var(--space-lg), env(safe-area-inset-bottom));
  overflow-y: auto; overscroll-behavior: contain;
}
.split-menu--js .split-menu__list { flex: 1 0 auto; align-content: center; }

/* Links rise from their masks; the active one is bright, the rest step back */
.split-menu--js .split-menu__word { translate: 0 110%; color: var(--text-inverse-muted); transition: translate var(--dur-2) var(--ease-in-out), color var(--dur-3) var(--ease-out); }
.split-menu--js.is-open .split-menu__word { translate: 0 0; transition: translate var(--dur-5) var(--ease-out) calc(var(--dur-3) + var(--split-menu-i) * var(--stagger)), color var(--dur-3) var(--ease-out); }
.split-menu--js .split-menu__num { opacity: 0; transition: opacity var(--dur-2) var(--ease-out), color var(--dur-2); }
.split-menu--js.is-open .split-menu__num { opacity: 1; transition: opacity var(--dur-4) var(--ease-out) calc(var(--dur-4) + var(--split-menu-i) * var(--stagger)), color var(--dur-2); }
.split-menu--js .split-menu__item.is-active .split-menu__word { color: var(--text-inverse); }
.split-menu--js .split-menu__item.is-active .split-menu__num { color: color-mix(in srgb, var(--primary-2) 65%, var(--text-inverse)); }
/* Phones: the active link wipes in its descriptor */
.split-menu--js .split-menu__desc { clip-path: inset(0 100% 0 0); opacity: 0; transition: clip-path var(--dur-4) var(--ease-out) var(--dur-3), opacity var(--dur-3) var(--ease-out) var(--dur-3); }
.split-menu--js.is-open .split-menu__item.is-active .split-menu__desc { clip-path: inset(0); opacity: 1; }

/* Preview: a slim strip at the bottom on phones */
.split-menu--js .split-menu__preview {
  position: relative; display: grid; flex: none; order: 2; height: 4.75rem; overflow: hidden; border-radius: var(--radius-xl);
  clip-path: inset(0 100% 0 0 round var(--radius-xl)); transition: clip-path var(--dur-3) var(--ease-in-out);
}
.split-menu--js.is-open .split-menu__preview { clip-path: inset(0 0 0 0 round var(--radius-xl)); transition: clip-path var(--dur-5) var(--ease-out) calc(var(--dur-3) + 3 * var(--stagger)); }
.split-menu--js .split-menu__preview::after { content: ""; position: absolute; inset: 0; z-index: 3; border-radius: inherit; box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse); pointer-events: none; }
.split-menu__slide { grid-area: 1 / 1; display: grid; grid-template-columns: 4.75rem minmax(0, 1fr); background: color-mix(in srgb, var(--surface-deep) 90%, var(--primary)); }
.split-menu__caption { display: grid; align-content: center; gap: 0.25rem; min-width: 0; padding: 0.625rem 0.875rem; }
.split-menu__caption p { margin: 0; overflow: hidden; color: var(--text-inverse); font-size: 0.8125rem; font-weight: 500; line-height: 1.35; white-space: nowrap; text-overflow: ellipsis; }
.split-menu__stats { display: flex; flex-wrap: wrap; gap: 0.125rem 0.875rem; color: var(--text-inverse-muted); font: 500 0.6875rem var(--font-mono); }
.split-menu__stats b { color: var(--text-inverse); font-weight: 600; }

/* Preview art: vivid gradient light, a fading grid, orbit rings and an outlined numeral */
.split-menu__art {
  --split-menu-c1: var(--primary); --split-menu-c2: var(--primary-2); --split-menu-at: 20% 20%;
  position: relative; overflow: hidden; container-type: size;
  background:
    radial-gradient(65% 75% at var(--split-menu-at), var(--split-menu-c1), transparent 70%),
    radial-gradient(70% 60% at 85% 90%, color-mix(in srgb, var(--split-menu-c2) 90%, transparent), transparent 70%),
    linear-gradient(160deg, color-mix(in srgb, var(--split-menu-c1) 40%, var(--surface-deep)), var(--surface-deep));
}
.split-menu__art--2 { --split-menu-c1: var(--accent); --split-menu-c2: var(--primary); --split-menu-at: 80% 15%; }
.split-menu__art--3 { --split-menu-c1: var(--primary-2); --split-menu-c2: var(--accent); --split-menu-at: 25% 75%; }
.split-menu__art--4 { --split-menu-c1: color-mix(in srgb, var(--primary) 55%, var(--accent)); --split-menu-c2: var(--primary-2); --split-menu-at: 60% 35%; }
.split-menu__art--5 { --split-menu-c1: var(--primary); --split-menu-c2: var(--accent); --split-menu-at: 15% 85%; }
.split-menu__art::before {
  content: ""; position: absolute; inset: 0;
  background-image: linear-gradient(var(--border-inverse) 1px, transparent 1px), linear-gradient(90deg, var(--border-inverse) 1px, transparent 1px);
  background-size: 1.5rem 1.5rem;
  -webkit-mask-image: linear-gradient(to top, black, transparent 85%); mask-image: linear-gradient(to top, black, transparent 85%);
}
.split-menu__art::after {
  content: ""; position: absolute; top: -20%; right: -15%; width: 75%; aspect-ratio: 1; border-radius: 50%;
  border: 1px solid color-mix(in srgb, var(--text-inverse) 35%, transparent);
  box-shadow: 0 0 0 1.75rem color-mix(in srgb, var(--text-inverse) 6%, transparent), 0 0 0 3.5rem color-mix(in srgb, var(--text-inverse) 3%, transparent);
}
.split-menu__art span {
  position: absolute; left: 0.5rem; left: 6cqw; bottom: -0.14em; color: transparent;
  font: 600 3rem/1 var(--font-display); font-size: min(80cqh, 48cqw); letter-spacing: var(--tracking-display);
  -webkit-text-stroke: 1px color-mix(in srgb, var(--text-inverse) 65%, transparent);
}

/* Contact row follows the links in */
.split-menu--js .split-menu__contact { flex: none; order: 1; margin-top: 0; opacity: 0; translate: 0 0.75rem; transition: opacity var(--dur-2) var(--ease-out), translate var(--dur-2) var(--ease-out); }
.split-menu--js.is-open .split-menu__contact { opacity: 1; translate: 0 0; transition-duration: var(--dur-4); transition-delay: calc(var(--dur-3) + 5 * var(--stagger)); }

/* Desktop: links left, a large preview window right, contact row along the bottom */
@media (min-width: 768px) {
  .split-menu { --split-menu-bar: 4.75rem; }
  .split-menu--js .split-menu__shutter { top: 0; bottom: 0; height: auto; }
  .split-menu--js .split-menu__shutter--a { right: auto; width: calc(var(--split-menu-split) + 1px); transform: translateX(-100%); }
  .split-menu--js .split-menu__shutter--b {
    left: auto; width: calc(100% - var(--split-menu-split)); transform: translateX(100%);
    background:
      radial-gradient(80% 60% at 70% 30%, color-mix(in srgb, var(--primary) 30%, transparent), transparent 70%),
      radial-gradient(60% 50% at 20% 100%, color-mix(in srgb, var(--primary-2) 22%, transparent), transparent 70%),
      color-mix(in srgb, var(--surface-deep) 90%, var(--primary));
  }
  .split-menu--js .split-menu__shutter--b::before { right: auto; bottom: 0; width: 1px; height: auto; background: linear-gradient(180deg, transparent, color-mix(in srgb, var(--primary-2) 70%, var(--text-inverse)), transparent); }

  .split-menu--js .split-menu__body { display: grid; grid-template-columns: var(--split-menu-split) minmax(0, 1fr); grid-template-rows: minmax(0, 1fr) auto; gap: 0; padding: var(--split-menu-bar) 0 0; }
  .split-menu--js .split-menu__list { grid-area: 1 / 1; padding: var(--space-xl) var(--space-xl) var(--space-xl) max(var(--gutter), calc((100vw - var(--container-max)) / 2 + var(--gutter))); }
  .split-menu--js .split-menu__link { gap: 1rem; }
  .split-menu--js .split-menu__num { padding-top: 0.875rem; }
  .split-menu--js .split-menu__word { font-size: clamp(3rem, min(5vw, 9vh), 5.5rem); }
  .split-menu--js .split-menu__desc { display: none; }
  .split-menu--js .split-menu__arrow {
    display: block; flex: none; align-self: center; width: 2rem; height: 2rem; fill: none; stroke: currentColor; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round;
    opacity: 0; translate: -0.75rem 0; transition: opacity var(--dur-2) var(--ease-out), translate var(--dur-3) var(--ease-spring);
  }
  .split-menu--js.is-open .split-menu__item.is-active .split-menu__arrow { opacity: 1; translate: 0 0; }

  .split-menu--js .split-menu__preview {
    grid-area: 1 / 2; align-self: center; order: 0; height: min(62vh, 34rem); border-radius: var(--radius-2xl);
    margin: var(--space-xl) max(var(--gutter), calc((100vw - var(--container-max)) / 2 + var(--gutter))) var(--space-xl) clamp(var(--space-xl), 4vw, 4rem);
    clip-path: inset(0 0 0 100% round var(--radius-2xl));
  }
  .split-menu--js.is-open .split-menu__preview { clip-path: inset(0 0 0 0 round var(--radius-2xl)); }
  .split-menu__slide { grid-template-columns: none; grid-template-rows: minmax(0, 1fr) auto; }
  .split-menu__caption { gap: 0.875rem; padding: 1.25rem 1.5rem 1.5rem; }
  .split-menu__caption p { font: 600 1.25rem/1.3 var(--font-display); letter-spacing: var(--tracking-tight); white-space: normal; text-wrap: balance; }
  .split-menu__stats { gap: 2rem; font-size: 0.75rem; }
  .split-menu__stats b { display: block; font: 600 1.5rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }

  .split-menu--js .split-menu__contact { grid-area: 2 / 1 / 3 / 3; padding: var(--space-md) max(var(--gutter), calc((100vw - var(--container-max)) / 2 + var(--gutter))); border-top: 1px solid var(--border-inverse); }
  .split-menu__email + .split-menu__social { margin-left: auto; }
  .split-menu__email-text { position: static; width: auto; height: auto; overflow: visible; clip-path: none; }
  .split-menu__contact .split-menu__email { padding: 0 0.875rem; }
}

/* The failsafes are 0s steps, not motion, so they stay on under prefers-reduced-motion */
@keyframes split-menu-failsafe { to { max-height: none; visibility: visible; } }
@keyframes split-menu-failsafe-out { to { visibility: hidden; } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const ease = 'cubic-bezier(0.16, 1, 0.3, 1)';

// While open, everything outside the header is inert (only what we changed is restored)
const inertOutside = (keep, on, store) => {
  if (!on) { store.forEach((el) => { el.inert = false; }); store.clear(); return; }
  for (let node = keep; node.parentElement && node !== document.body; node = node.parentElement) {
    for (const sib of node.parentElement.children) {
      if (sib !== node && !sib.inert) { sib.inert = true; store.add(sib); }
    }
  }
};

document.querySelectorAll('[data-split-menu]').forEach((root, n) => {
  const toggle = root.querySelector('.split-menu__toggle');
  const panel = root.querySelector('.split-menu__panel');
  const items = [...panel.querySelectorAll('.split-menu__item')];
  const links = items.map((item) => item.querySelector('a'));
  const slides = [...panel.querySelectorAll('.split-menu__slide')];
  const inerted = new Set();
  let shown = -1;
  root.classList.add('split-menu--js');
  if (n) panel.id = `${panel.id}-${n + 1}`; // unique ids for repeated instances
  toggle.setAttribute('aria-controls', panel.id);

  // Activate a link: brighten it, reveal its descriptor and wipe its preview in over the last one,
  // from below when moving down the list and from above when moving up
  const activate = (i) => {
    if (i < 0 || i === shown) return;
    items.forEach((item, k) => item.classList.toggle('is-active', k === i));
    slides.forEach((slide, k) => { slide.style.zIndex = k === i ? '2' : k === shown ? '1' : '0'; });
    if (shown >= 0 && !reduce.matches) {
      const from = i > shown ? 'inset(100% 0 0 0)' : 'inset(0 0 100% 0)';
      slides[i].animate({ clipPath: [from, 'inset(0 0 0 0)'] }, { duration: 640, easing: ease });
      slides[i].firstElementChild.animate({ transform: ['scale(1.12)', 'none'] }, { duration: 900, easing: ease });
    }
    shown = i;
  };

  const onKey = (e) => { if (e.key === 'Escape') { e.preventDefault(); setOpen(false); } };
  const setOpen = (open) => {
    if (open === root.classList.contains('is-open')) return;
    root.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    inertOutside(root, open, inerted);
    document[open ? 'addEventListener' : 'removeEventListener']('keydown', onKey);
    if (open) links[0].focus({ preventScroll: true }); // focusin makes it the active link
    else { shown = -1; toggle.focus({ preventScroll: true }); } // reopen without a wipe
  };

  toggle.addEventListener('click', () => setOpen(!root.classList.contains('is-open')));
  panel.addEventListener('focusin', (e) => activate(links.indexOf(e.target.closest('a'))));
  items.forEach((item, i) => item.addEventListener('pointerenter', (e) => { if (e.pointerType === 'mouse') activate(i); }));
  panel.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
  activate(0);
});
```

## Notes

- Disclosure model with a modal state: the burger has `aria-expanded` and `aria-controls` and opens a labelled `<nav>`. Opening focuses 01, makes everything outside the header `inert` and locks scrolling through `html:has()`. The bar (logo and toggle) stays above the panels, so the toggle remains the close control. Escape, the toggle or following a link closes the menu and returns focus to the toggle. Numbers, descriptors and the preview are `aria-hidden`, so each link is announced by its name alone.
- The panel is `position: fixed` inside a sticky header. Keep `transform`, `filter` and `backdrop-filter` off `.split-menu` itself, because they would trap it. The bar's glass lives on its own `::before` for that reason.
- No JS (`@media (scripting: none)`): the toggle is hidden and the nav renders as a deep band of numbered links with descriptors and contact links under the bar. With scripting on, the overlay starts closed from first paint, and a 3s CSS failsafe restores the band if the module never runs.
- Reduced motion: the panels, links, preview and contact row appear instantly (the motion tokens collapse), and the preview swaps without a wipe.
- Contrast on the deep panels: active links and captions use `--text-inverse` (19:1 on `--surface-deep`). The other links, numbers and stats use `--text-inverse-muted` (7:1), and the active number's teal tint is above 8:1. Preview text sits on its own deep caption area, never on the art.
- Adapting: keep one `.split-menu__slide` per link, in the same order. Swap `.split-menu__art` for an `<img>` with `width`/`height` and `object-fit: cover` to show photos. Move the split with `--split-menu-split`, and recolour the art through `--split-menu-c1`, `--split-menu-c2` and `--split-menu-at`.
