# Drill-Down Menu

An iOS-Settings-style multi-level menu in a light panel, built from grouped inset lists with coloured icon tiles, live meta (prices, travel times) and chevrons. Choosing a category pushes the new level in from the right while the current one slides about 30% left and dims, the panel's height glides to fit, the header crossfades from the brand to a back button carrying the parent's title, and a pip slides along three depth dots. On phones the panel fills the width with 48px rows; on desktop it stays a compact 24rem menu. Depends on `tokens/variables.css`.

**Motion:** level push with parallax and dim (`--dur-4`, `--ease-out`) · panel height glide (`--dur-4`, `--ease-out`) · back-label and brand crossfade with blur (`--dur-3`) · depth pip slide (`--dur-4`, `--ease-spring`) · row press tint.

## HTML

```html
<div class="drill-menu-demo">
  <div class="drill-menu-demo__page">
    <p class="drill-menu-demo__eyebrow">Brand · Springfield</p>
    <h2 class="drill-menu-demo__title">Everything we do, two taps away.</h2>

    <nav class="drill-menu" aria-label="Site menu" data-drill-menu data-drill-menu-demo>
      <div class="drill-menu__bar">
        <div class="drill-menu__lead">
          <span class="drill-menu__brand" aria-hidden="true"><span class="drill-menu__mark"></span>Brand</span>
          <button class="drill-menu__back" type="button" hidden>
            <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m15 5-7 7 7 7" /></svg>
            <span class="drill-menu__back-labels" aria-hidden="true"><span class="drill-menu__back-label is-current">Menu</span><span class="drill-menu__back-label"></span></span>
          </button>
        </div>
        <span class="drill-menu__dots" aria-hidden="true"><span class="drill-menu__dot"></span><span class="drill-menu__dot"></span><span class="drill-menu__dot"></span><span class="drill-menu__pip"></span></span>
      </div>

      <div class="drill-menu__viewport">
        <div class="drill-menu__level">
          <h2 class="drill-menu__title" tabindex="-1">Menu</h2>
          <ul class="drill-menu__group" role="list">
            <li>
              <a class="drill-menu__item drill-menu__item--branch" href="#drill-menu-services">
                <span class="drill-menu__icon drill-menu__icon--services"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z" /></svg></span>
                <span class="drill-menu__label">Services</span><span class="drill-menu__meta">6</span>
                <svg class="drill-menu__chev" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m9 5 7 7-7 7" /></svg>
              </a>
              <div class="drill-menu__level" id="drill-menu-services">
                <h3 class="drill-menu__title" tabindex="-1">Services</h3>
                <ul class="drill-menu__group" role="list">
                  <li><a class="drill-menu__item" href="/services"><span class="drill-menu__label">All services</span></a></li>
                  <li><a class="drill-menu__item" href="/services/plumbing"><span class="drill-menu__label">Plumbing</span><span class="drill-menu__meta">from $89</span></a></li>
                  <li>
                    <a class="drill-menu__item drill-menu__item--branch" href="#drill-menu-heating">
                      <span class="drill-menu__label">Heating</span><span class="drill-menu__meta">4</span>
                      <svg class="drill-menu__chev" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m9 5 7 7-7 7" /></svg>
                    </a>
                    <div class="drill-menu__level" id="drill-menu-heating">
                      <h4 class="drill-menu__title" tabindex="-1">Heating</h4>
                      <ul class="drill-menu__group" role="list">
                        <li><a class="drill-menu__item" href="/services/heating"><span class="drill-menu__label">All heating</span></a></li>
                        <li><a class="drill-menu__item" href="/services/heating/boiler-repair"><span class="drill-menu__label">Boiler repair</span><span class="drill-menu__meta">from $119</span></a></li>
                        <li><a class="drill-menu__item" href="/services/heating/boiler-service"><span class="drill-menu__label">Boiler service</span><span class="drill-menu__tag">$79 offer</span></a></li>
                        <li><a class="drill-menu__item" href="/services/heating/heat-pumps"><span class="drill-menu__label">Heat pumps</span><span class="drill-menu__meta">quote</span></a></li>
                        <li><a class="drill-menu__item" href="/services/heating/radiators"><span class="drill-menu__label">Radiators and valves</span><span class="drill-menu__meta">from $65</span></a></li>
                      </ul>
                    </div>
                  </li>
                  <li><a class="drill-menu__item" href="/services/electrical"><span class="drill-menu__label">Electrical</span><span class="drill-menu__meta">from $95</span></a></li>
                  <li><a class="drill-menu__item" href="/services/roofing"><span class="drill-menu__label">Roofing</span><span class="drill-menu__meta">from $140</span></a></li>
                  <li><a class="drill-menu__item" href="/services/emergency"><span class="drill-menu__label">Emergency call-out</span><span class="drill-menu__tag drill-menu__tag--alert">24/7</span></a></li>
                </ul>
              </div>
            </li>
            <li>
              <a class="drill-menu__item drill-menu__item--branch" href="#drill-menu-areas">
                <span class="drill-menu__icon drill-menu__icon--areas"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z" /><circle cx="12" cy="10" r="2.5" /></svg></span>
                <span class="drill-menu__label">Areas</span><span class="drill-menu__meta">5</span>
                <svg class="drill-menu__chev" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m9 5 7 7-7 7" /></svg>
              </a>
              <div class="drill-menu__level" id="drill-menu-areas">
                <h3 class="drill-menu__title" tabindex="-1">Areas</h3>
                <ul class="drill-menu__group" role="list">
                  <li><a class="drill-menu__item" href="/areas/westlake"><span class="drill-menu__label">Westlake</span><span class="drill-menu__meta">12 min away</span></a></li>
                  <li><a class="drill-menu__item" href="/areas/northside"><span class="drill-menu__label">Northside</span><span class="drill-menu__meta">18 min away</span></a></li>
                  <li><a class="drill-menu__item" href="/areas/riverside"><span class="drill-menu__label">Riverside</span><span class="drill-menu__meta">20 min away</span></a></li>
                  <li><a class="drill-menu__item" href="/areas/eastfield"><span class="drill-menu__label">Eastfield</span><span class="drill-menu__meta">25 min away</span></a></li>
                  <li><a class="drill-menu__item" href="/areas/old-town"><span class="drill-menu__label">Old Town</span><span class="drill-menu__meta">30 min away</span></a></li>
                </ul>
              </div>
            </li>
            <li>
              <a class="drill-menu__item drill-menu__item--branch" href="#drill-menu-about">
                <span class="drill-menu__icon drill-menu__icon--about"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9" /><path d="M12 11v5M12 8h.01" /></svg></span>
                <span class="drill-menu__label">About</span>
                <svg class="drill-menu__chev" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m9 5 7 7-7 7" /></svg>
              </a>
              <div class="drill-menu__level" id="drill-menu-about">
                <h3 class="drill-menu__title" tabindex="-1">About</h3>
                <ul class="drill-menu__group" role="list">
                  <li><a class="drill-menu__item" href="/about"><span class="drill-menu__label">Our story</span></a></li>
                  <li><a class="drill-menu__item" href="/about/team"><span class="drill-menu__label">Team</span><span class="drill-menu__meta">14 people</span></a></li>
                  <li><a class="drill-menu__item" href="/reviews"><span class="drill-menu__label">Reviews</span><span class="drill-menu__meta">4.9 / 5</span></a></li>
                  <li><a class="drill-menu__item" href="/about/guarantee"><span class="drill-menu__label">12-month guarantee</span></a></li>
                  <li><a class="drill-menu__item" href="/careers"><span class="drill-menu__label">Careers</span><span class="drill-menu__tag">3 open</span></a></li>
                </ul>
              </div>
            </li>
            <li>
              <a class="drill-menu__item" href="/contact">
                <span class="drill-menu__icon drill-menu__icon--contact"><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><rect x="3" y="5" width="18" height="14" rx="2" /><path d="m3 7 9 6 9-6" /></svg></span>
                <span class="drill-menu__label">Contact</span><span class="drill-menu__meta">hello@example.com</span>
              </a>
            </li>
          </ul>

          <div class="drill-menu__cta">
            <p class="drill-menu__status"><span class="drill-menu__led" aria-hidden="true"></span>Open now · tech nearby, 12 min</p>
            <a class="drill-menu__book" href="/book">
              Book a visit
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
          </div>
        </div>
      </div>
    </nav>
  </div>
</div>
```

## CSS

```css
/* Demo page */
.drill-menu-demo {
  min-height: 100vh; min-height: 100svh; color: var(--text-main); font-family: var(--font-sans);
  background:
    radial-gradient(30rem 20rem at 0% 0%, color-mix(in srgb, var(--primary-2) 12%, transparent), transparent 70%),
    radial-gradient(30rem 20rem at 100% 100%, color-mix(in srgb, var(--primary) 10%, transparent), transparent 70%),
    var(--surface-light);
}
.drill-menu-demo__page { max-width: min(var(--container-max), 40rem); margin-inline: auto; padding: var(--space-xl) var(--gutter) var(--space-2xl); }
.drill-menu-demo__eyebrow { margin: 0; color: var(--primary); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.drill-menu-demo__title { margin: 0.625rem 0 var(--space-lg); font: 600 clamp(1.75rem, 1.3rem + 2vw, 2.5rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }

/* Panel */
.drill-menu {
  width: min(100%, 24rem); margin-inline: auto; overflow: clip; border-radius: var(--radius-2xl);
  background: var(--surface-muted); box-shadow: 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}

/* Header: the brand crossfades into a back button carrying the parent's title; a pip slides along the depth dots */
.drill-menu__bar {
  display: flex; align-items: center; gap: var(--space-sm); height: 3.25rem; padding: 0 0.875rem 0 0.375rem;
  background: color-mix(in srgb, var(--surface-light) 60%, var(--surface-muted)); box-shadow: inset 0 -1px 0 var(--border-subtle);
}
.drill-menu__lead { display: grid; align-items: center; min-width: 0; }
.drill-menu__brand, .drill-menu__back { grid-area: 1 / 1; }
.drill-menu__brand {
  display: inline-flex; align-items: center; gap: 0.5rem; padding-left: 0.5rem; font: 600 1rem/1 var(--font-display); letter-spacing: var(--tracking-tight);
  transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-out), filter var(--dur-3) var(--ease-out);
}
.drill-menu__mark { width: 1.375rem; height: 1.375rem; border-radius: 0.4375rem; background: var(--gradient-brand); box-shadow: var(--highlight), 0 6px 12px -6px var(--primary); }
.drill-menu__back {
  display: inline-flex; align-items: center; gap: 0.125rem; min-width: 0; height: 2.75rem; padding: 0 0.75rem 0 0.25rem; border: 0; border-radius: var(--radius-full);
  background: transparent; color: var(--primary); font: 600 0.9375rem/1 var(--font-sans); cursor: pointer; -webkit-tap-highlight-color: transparent;
  transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-spring), visibility 0s linear var(--dur-3), background-color var(--dur-2);
}
.drill-menu__back[hidden] { display: none; }
.drill-menu__back:hover { background: color-mix(in srgb, var(--primary) 8%, transparent); }
.drill-menu__back svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2.25; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.drill-menu__back:hover svg { translate: -2px 0; }
.drill-menu__back-labels { display: grid; min-width: 0; }
.drill-menu__back-label {
  grid-area: 1 / 1; overflow: hidden; white-space: nowrap; text-overflow: ellipsis;
  opacity: 0; translate: 0.5rem 0; filter: blur(4px);
  transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-out), filter var(--dur-3) var(--ease-out);
}
.drill-menu__back-label.is-current { opacity: 1; translate: 0 0; filter: none; }
.drill-menu--js .drill-menu__back { opacity: 0; translate: 0.75rem 0; visibility: hidden; }
.drill-menu--js:not([data-depth="0"]) .drill-menu__back { opacity: 1; translate: 0 0; visibility: visible; transition-delay: 0s; }
.drill-menu--js:not([data-depth="0"]) .drill-menu__brand { opacity: 0; translate: -0.5rem 0; filter: blur(4px); }

.drill-menu__dots { position: relative; display: flex; gap: 0.5rem; margin-left: auto; padding-left: 0.25rem; }
.drill-menu__dot { width: 0.375rem; height: 0.375rem; border-radius: 50%; background: color-mix(in srgb, var(--text-main) 16%, transparent); transition: background-color var(--dur-3) var(--ease-out); }
.drill-menu__dot.is-past { background: color-mix(in srgb, var(--primary) 45%, var(--surface-light)); }
.drill-menu__pip {
  position: absolute; left: 0; top: 50%; width: 0.875rem; height: 0.375rem; margin-top: -0.1875rem; border-radius: var(--radius-full);
  background: var(--gradient-brand); box-shadow: 0 0 10px color-mix(in srgb, var(--primary) 55%, transparent);
  translate: calc(var(--drill-menu-at, 0) * 0.875rem) 0; transition: translate var(--dur-4) var(--ease-spring);
}

/* Levels. Without JS they nest in place, fully expanded. */
.drill-menu__viewport { position: relative; }
.drill-menu__level { padding: 0.5rem 1rem 1rem; }
.drill-menu__title { margin: 0.5rem 0.25rem 0.875rem; border-radius: var(--radius-sm); font: 600 1.75rem/1.1 var(--font-display); letter-spacing: var(--tracking-display); }
.drill-menu__title:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.drill-menu__level .drill-menu__level { padding: 0; }
.drill-menu__level .drill-menu__level .drill-menu__title { margin: 0.875rem 0.875rem 0.5rem; color: var(--text-muted); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.drill-menu__level .drill-menu__level .drill-menu__group { margin: 0 0.75rem 0.75rem; background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }

/* Grouped inset list rows */
.drill-menu__group { margin: 0; padding: 0; overflow: clip; list-style: none; border-radius: var(--radius-xl); background: var(--surface-light); box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-sm); }
.drill-menu__item {
  position: relative; display: flex; align-items: center; gap: 0.75rem; min-height: 3rem; padding: 0.5rem 0.875rem;
  color: var(--text-main); font-size: 0.9375rem; font-weight: 500; text-decoration: none; -webkit-tap-highlight-color: transparent;
  transition: background-color var(--dur-2) var(--ease-out);
}
.drill-menu__item--branch { display: none; } /* no scripting: the expanded sections stand in for these rows */
.drill-menu__group > li + li > .drill-menu__item::before { content: ""; position: absolute; top: 0; right: 0; left: 0.875rem; height: 1px; background: var(--border-subtle); }
.drill-menu__group > li + li > .drill-menu__item:has(.drill-menu__icon)::before { left: 3.5rem; }
.drill-menu__item:hover { background: color-mix(in srgb, var(--surface-muted) 70%, var(--surface-light)); }
.drill-menu__item:active { background: var(--surface-muted); }
.drill-menu__item:focus-visible { outline: 2px solid var(--primary); outline-offset: -3px; } /* inset: the group clips its corners */
.drill-menu__icon { flex: none; display: grid; place-items: center; width: 1.875rem; height: 1.875rem; border-radius: 0.5rem; color: var(--text-inverse); box-shadow: var(--highlight), 0 4px 10px -6px color-mix(in srgb, var(--text-main) 60%, transparent); }
.drill-menu__icon svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.drill-menu__icon--services { background: var(--gradient-brand); }
.drill-menu__icon--areas { background: linear-gradient(150deg, color-mix(in srgb, var(--primary-2) 80%, var(--surface-light)), var(--primary-2)); }
.drill-menu__icon--about { background: linear-gradient(150deg, color-mix(in srgb, var(--accent) 70%, var(--surface-light)), var(--accent)); color: var(--text-main); }
.drill-menu__icon--contact { background: linear-gradient(150deg, color-mix(in srgb, var(--success) 80%, var(--surface-light)), var(--success)); }
.drill-menu__label { flex: 1; min-width: 0; overflow: hidden; white-space: nowrap; text-overflow: ellipsis; }
.drill-menu__meta { flex: none; max-width: 48%; overflow: hidden; color: var(--text-muted); font: 500 0.8125rem/1.2 var(--font-mono); white-space: nowrap; text-overflow: ellipsis; }
.drill-menu__tag { flex: none; padding: 0.25rem 0.5rem; border-radius: var(--radius-full); background: color-mix(in srgb, var(--primary) 10%, var(--surface-light)); color: var(--primary-hover); font: 600 0.75rem/1 var(--font-mono); }
.drill-menu__tag--alert { background: color-mix(in srgb, var(--danger) 10%, var(--surface-light)); color: color-mix(in srgb, var(--danger) 80%, var(--text-main)); }
.drill-menu__chev { flex: none; margin-right: -0.25rem; fill: none; stroke: var(--text-muted); stroke-width: 2.25; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.drill-menu__item--branch:hover .drill-menu__chev { translate: 2px 0; }
.drill-menu__item[aria-current="page"] { color: var(--primary); font-weight: 600; }
.drill-menu__item[aria-current="page"]::after { content: ""; flex: none; width: 0.375rem; height: 0.75rem; margin: -0.25rem 0.25rem 0 0.125rem; border: solid currentColor; border-width: 0 2px 2px 0; rotate: 45deg; }

/* Root call to action */
.drill-menu__cta {
  display: grid; gap: 0.75rem; margin-top: var(--space-md); padding: var(--space-md); border-radius: var(--radius-xl); color: var(--text-inverse);
  background:
    radial-gradient(90% 120% at 100% 0%, color-mix(in srgb, var(--primary-2) 55%, transparent), transparent 70%),
    radial-gradient(80% 120% at 0% 100%, color-mix(in srgb, var(--primary) 65%, transparent), transparent 70%),
    var(--surface-deep);
  box-shadow: var(--highlight-inverse), var(--shadow-lg);
}
.drill-menu__status { display: flex; align-items: center; gap: 0.5rem; margin: 0; font: 500 0.8125rem/1.3 var(--font-mono); }
.drill-menu__led { flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 30%, transparent), 0 0 10px var(--success); }
.drill-menu__book {
  display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; height: 3rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  transition: scale var(--dur-3) var(--ease-spring);
}
.drill-menu__book svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.drill-menu__book:hover svg { translate: 3px 0; }
.drill-menu__book:active { scale: 0.97; }
.drill-menu__book:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.drill-menu__back:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

/* Enhanced: levels stack in one viewport; the current one sits on top, its ancestors wait at -30%, dimmed */
.drill-menu--js .drill-menu__item--branch { display: flex; }
.drill-menu--js .drill-menu__viewport { overflow: hidden; transition: height var(--dur-4) var(--ease-out); }
.drill-menu--js .drill-menu__level {
  position: absolute; inset: 0 0 auto; z-index: var(--drill-menu-depth, 0); background: var(--surface-muted);
  translate: 100% 0; visibility: hidden;
  transition: translate var(--dur-4) var(--ease-out), filter var(--dur-4) var(--ease-out), box-shadow var(--dur-4) var(--ease-out), visibility 0s linear var(--dur-4);
}
.drill-menu--js .drill-menu__level[data-pos="current"] {
  translate: 0 0; visibility: visible; transition-delay: 0s;
  box-shadow: -1.5rem 0 2rem -1.5rem color-mix(in srgb, var(--surface-deep) 35%, transparent);
}
.drill-menu--js .drill-menu__level[data-pos="before"] { translate: -30% 0; filter: brightness(0.9) saturate(0.9); }

/* Scripting on: paint the top level only, from the first frame (no flash of the expanded tree).
   Failsafe: if the script never runs, the nested sections open after 2s and the rows still work as jump links. */
@media (scripting: enabled) {
  .drill-menu__item--branch { display: flex; }
  .drill-menu:not(.drill-menu--js) .drill-menu__level .drill-menu__level { height: 0; overflow: hidden; visibility: hidden; animation: drill-menu-failsafe 0.01ms 2s both; }
  .drill-menu:not(.drill-menu--js) .drill-menu__dots { animation: drill-menu-failsafe-hide 0.01ms 2s both; }
}
@media (scripting: none) {
  .drill-menu__dots { display: none; }
}

/* The failsafes are instant steps, not motion, so they stay on under prefers-reduced-motion */
@keyframes drill-menu-failsafe { to { height: auto; visibility: visible; } }
@keyframes drill-menu-failsafe-hide { to { visibility: hidden; } }
```

## JS

```js
document.querySelectorAll('[data-drill-menu]').forEach((menu) => {
  const viewport = menu.querySelector('.drill-menu__viewport');
  const back = menu.querySelector('.drill-menu__back');
  const labels = [...back.querySelectorAll('.drill-menu__back-label')];
  const dots = [...menu.querySelectorAll('.drill-menu__dot')];
  const levels = [...menu.querySelectorAll('.drill-menu__level')];
  const info = new Map();
  let current = levels[0];

  // Read the nesting first: each level's parent, depth, heading and the row that opens it
  levels.forEach((level) => {
    const parent = level.parentElement.closest('.drill-menu__level');
    info.set(level, {
      parent,
      depth: parent ? info.get(parent).depth + 1 : 0,
      opener: parent ? parent.querySelector(`a[href="#${level.id}"]`) : null,
      title: level.querySelector('.drill-menu__title'),
    });
  });

  // Show one level: its ancestors wait at -30% (dimmed), everything else waits off to the right
  const show = (level, focusTarget) => {
    current = level;
    const chain = new Set();
    for (let l = level; l; l = info.get(l).parent) chain.add(l);
    levels.forEach((l) => {
      l.dataset.pos = l === level ? 'current' : chain.has(l) ? 'before' : 'after';
      l.inert = l !== level;
    });
    const { parent, depth } = info.get(level);
    menu.dataset.depth = depth;
    menu.style.setProperty('--drill-menu-at', depth);
    dots.forEach((dot, i) => dot.classList.toggle('is-past', i < depth));
    back.inert = !parent;
    if (parent) {
      // Crossfade the back label to the parent's title
      const text = info.get(parent).title.textContent.trim();
      const [shown, spare] = labels[0].classList.contains('is-current') ? labels : [labels[1], labels[0]];
      if (shown.textContent !== text) {
        spare.textContent = text;
        spare.classList.add('is-current');
        shown.classList.remove('is-current');
      }
      back.setAttribute('aria-label', `Back to ${text}`);
    }
    viewport.style.height = `${level.offsetHeight}px`;
    focusTarget?.focus({ preventScroll: true });
  };
  // Going up returns focus to the row you came from, so you keep your place
  const up = () => {
    const { parent, opener } = info.get(current);
    if (parent) show(parent, opener);
  };

  // Enhance: lift every level into the viewport so each can slide on its own
  levels.forEach((level) => {
    const { depth, opener, title } = info.get(level);
    level.style.setProperty('--drill-menu-depth', depth);
    viewport.append(level);
    opener?.addEventListener('click', (e) => {
      e.preventDefault();
      show(level, title);
    });
  });
  back.hidden = false;
  menu.classList.add('drill-menu--js');
  show(levels[0]);

  back.addEventListener('click', up);
  menu.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && info.get(current).parent) {
      e.preventDefault();
      up();
    }
  });
  // Keep the panel height right as fonts load, text wraps or the viewport resizes
  const resize = new ResizeObserver(() => { viewport.style.height = `${current.offsetHeight}px`; });
  levels.forEach((level) => resize.observe(level));

  // Demo only (data-drill-menu-demo): leaf links mark the current page instead of navigating
  if (menu.hasAttribute('data-drill-menu-demo')) {
    const leaves = [...menu.querySelectorAll('.drill-menu__item[href^="/"]')];
    leaves.forEach((link) => link.addEventListener('click', (e) => {
      e.preventDefault();
      leaves.forEach((other) => (other === link ? other.setAttribute('aria-current', 'page') : other.removeAttribute('aria-current')));
    }));
  }
});
```

## Notes

- **Accessibility:** one labelled `<nav>` of plain links. Category rows are in-page links (`href="#drill-menu-…"`): with JS, Enter or a tap drills in; without it they jump to the open section. Drilling in moves focus to the new level's heading (`tabindex="-1"`). Back or Escape goes up and returns focus to the row you drilled from rather than the parent's heading, so keyboard and screen-reader users keep their place. Hidden levels are `inert` and `visibility: hidden`. The back button is named "Back to Services" and so on, while its crossfading visible labels are `aria-hidden`. The depth dots are decorative.
- **No JS:** with scripting off, the nested lists render fully expanded as indented sections with their own headings (h2 → h3 → h4), and every link works. With scripting on, `@media (scripting: enabled)` paints just the top level from the first frame, so nothing flashes. If the script fails, a zero-length CSS failsafe opens the sections after 2s.
- **Motion:** all CSS transitions on the tokens. Levels move on `translate` and `filter`; only the viewport's height animates as layout, measured by JS and kept current by a `ResizeObserver`. Under reduced motion everything is instant.
- **Contrast:** row text is `--text-main` on white (14.6:1), meta is `--text-muted` (4.8:1), the back label is `--primary` on the bar (about 5:1), tags are 6.9:1 and 5.4:1, and the call-to-action copy is `--text-inverse` on `--surface-deep` (at least 8:1 at the brightest glow).
- **Adapting:** to add a level, nest `li > a.drill-menu__item--branch[href="#id"]` followed by `div.drill-menu__level#id` with a heading and a `.drill-menu__group`. Add a `.drill-menu__dot` for each extra depth and keep ids unique per page. Drop `data-drill-menu-demo` so links navigate, and set `aria-current="page"` server-side.
