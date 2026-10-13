# Morphing Dropdown

Stripe-style navigation dropdowns. One shared panel background morphs its size and position as you move between menus, a caret tracks the active trigger, and content slides in from the direction you're moving. Below 768px the same markup becomes a stacked accordion. Depends on `tokens/variables.css`.

**Motion:** background morphs width/height/position (`--dur-4`, ease-out) · directional content slide + fade · chevron flips with a spring · icon tiles tilt on hover.

## HTML

```html
<nav class="morph-nav" aria-label="Main" data-morph-nav>
  <ul class="morph-nav__list" role="list">
    <li>
      <button class="morph-nav__trigger" type="button" aria-expanded="false" aria-controls="morph-services">
        Services
        <svg class="morph-nav__chevron" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
      </button>
      <div class="morph-nav__panel" id="morph-services" style="--morph-panel-w: 40rem">
        <div class="morph-nav__split">
          <ul class="morph-nav__tiles" role="list">
            <li><a class="morph-nav__tile" href="#repairs">
              <span class="morph-nav__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z" /></svg></span>
              <span><strong>Repairs</strong><small>Fast fixes at a flat, upfront price</small></span>
            </a></li>
            <li><a class="morph-nav__tile" href="#installs">
              <span class="morph-nav__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M21 8l-9-5-9 5v8l9 5 9-5V8zM3 8l9 5 9-5M12 13v8" /></svg></span>
              <span><strong>Installations</strong><small>New systems, fitted and tested</small></span>
            </a></li>
            <li><a class="morph-nav__tile" href="#maintenance">
              <span class="morph-nav__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM9 15l2 2 4-4" /></svg></span>
              <span><strong>Maintenance plans</strong><small>Yearly checks that prevent breakdowns</small></span>
            </a></li>
            <li><a class="morph-nav__tile" href="#inspections">
              <span class="morph-nav__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM21 21l-5-5" /></svg></span>
              <span><strong>Inspections</strong><small>Written reports for buyers and sellers</small></span>
            </a></li>
          </ul>
          <a class="morph-nav__feature" href="#emergency">
            <span class="morph-nav__eyebrow">24/7</span>
            <strong>Emergency callouts</strong>
            <small>A licensed technician at your door in under two hours.</small>
            <span class="morph-nav__more">See coverage <span aria-hidden="true">→</span></span>
          </a>
        </div>
      </div>
    </li>
    <li>
      <button class="morph-nav__trigger" type="button" aria-expanded="false" aria-controls="morph-company">
        Company
        <svg class="morph-nav__chevron" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
      </button>
      <div class="morph-nav__panel" id="morph-company" style="--morph-panel-w: 19rem">
        <ul class="morph-nav__menu-list" role="list">
          <li><a href="#about">About us <small>Family-owned since 2009</small></a></li>
          <li><a href="#team">Our team <small>42 licensed technicians</small></a></li>
          <li><a href="#careers">Careers <small>We're hiring apprentices</small></a></li>
          <li><a href="#contact">Contact <small>(555) 555-0123</small></a></li>
        </ul>
      </div>
    </li>
    <li>
      <button class="morph-nav__trigger" type="button" aria-expanded="false" aria-controls="morph-resources">
        Resources
        <svg class="morph-nav__chevron" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
      </button>
      <div class="morph-nav__panel" id="morph-resources" style="--morph-panel-w: 31rem">
        <div class="morph-nav__split morph-nav__split--even">
          <ul class="morph-nav__menu-list" role="list">
            <li><a href="#guides">Homeowner guides <small>Fix small things yourself</small></a></li>
            <li><a href="#faq">FAQ <small>Pricing, warranties, scheduling</small></a></li>
            <li><a href="#areas">Service areas <small>Springfield and 14 towns</small></a></li>
          </ul>
          <a class="morph-nav__guide" href="#winter-guide">
            <span class="morph-nav__guide-art" aria-hidden="true"></span>
            <small>New guide</small>
            <strong>Winter-proof your pipes in 20 minutes</strong>
          </a>
        </div>
      </div>
    </li>
    <li><a class="morph-nav__link" href="#pricing">Pricing</a></li>
  </ul>
  <div class="morph-nav__bg" aria-hidden="true"><span class="morph-nav__caret"></span></div>
</nav>
```

## CSS

```css
/* Mobile first: a stacked accordion */
.morph-nav { position: relative; font-family: var(--font-sans); color: var(--text-main); }
.morph-nav__list { display: grid; gap: 0.125rem; margin: 0; padding: 0; list-style: none; }
.morph-nav__trigger, .morph-nav__link {
  display: flex; align-items: center; justify-content: space-between; gap: 0.375rem;
  width: 100%; height: 2.75rem; padding: 0 0.875rem;
  border: 0; border-radius: 999px; background: transparent; color: var(--text-muted);
  font: 500 0.9375rem/1 var(--font-sans); text-decoration: none; cursor: pointer;
  transition: color var(--dur-2), background-color var(--dur-2);
}
.morph-nav__trigger:hover, .morph-nav__link:hover, .morph-nav__trigger[aria-expanded="true"] {
  color: var(--text-main); background: color-mix(in srgb, var(--text-main) 5%, transparent);
}
.morph-nav__chevron { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-4) var(--ease-spring); }
.morph-nav__trigger[aria-expanded="true"] .morph-nav__chevron { transform: rotate(180deg); }
.morph-nav :is(a, button):focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.morph-nav__panel { display: none; padding: 0.25rem 0 0.75rem; }
.morph-nav__panel[data-active] { display: block; }
.morph-nav__bg { display: none; }

/* Panel content: icon tiles */
.morph-nav__split { display: grid; gap: 0.5rem; }
.morph-nav__tiles { display: grid; gap: 0.125rem; margin: 0; padding: 0; list-style: none; }
.morph-nav__tile {
  display: flex; align-items: flex-start; gap: 0.875rem; padding: 0.75rem; border-radius: 0.875rem;
  color: var(--text-main); text-decoration: none; transition: background-color var(--dur-2);
}
.morph-nav__tile:hover { background: color-mix(in srgb, var(--text-main) 4%, transparent); }
.morph-nav__icon {
  flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 0.75rem;
  background: color-mix(in srgb, var(--primary) 9%, var(--surface-light)); color: var(--primary);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 16%, transparent);
  transition: transform var(--dur-4) var(--ease-spring), background-color var(--dur-2), color var(--dur-2);
}
.morph-nav__icon svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.morph-nav__tile:hover .morph-nav__icon { transform: scale(1.06) rotate(-6deg); background: var(--primary); color: var(--surface-light); }
.morph-nav__tile strong, .morph-nav__menu-list a { display: block; font-size: 0.9375rem; font-weight: 600; }
.morph-nav__tile small, .morph-nav__menu-list small { display: block; margin-top: 0.125rem; color: var(--text-muted); font-size: 0.8125rem; font-weight: 400; line-height: 1.4; }

/* Feature card */
.morph-nav__feature {
  display: flex; flex-direction: column; gap: 0.375rem; padding: 1.25rem; border-radius: 0.875rem;
  color: var(--text-inverse); text-decoration: none;
  background:
    radial-gradient(120% 90% at 100% 0%, color-mix(in srgb, var(--primary-2) 65%, transparent), transparent 60%),
    radial-gradient(90% 80% at 0% 100%, color-mix(in srgb, var(--primary) 55%, transparent), transparent 60%),
    var(--surface-deep);
  box-shadow: var(--highlight-inverse);
}
.morph-nav__feature strong { font: 600 1.125rem/1.2 var(--font-display); letter-spacing: -0.01em; }
.morph-nav__feature small { color: var(--text-inverse-muted); font-size: 0.8125rem; line-height: 1.45; }
.morph-nav__eyebrow {
  align-self: flex-start; padding: 0.125rem 0.5rem; border-radius: 999px;
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse);
  font-size: 0.75rem; font-weight: 600;
}
.morph-nav__more { margin-top: auto; padding-top: 1rem; font-size: 0.875rem; font-weight: 600; }
.morph-nav__more span { display: inline-block; transition: transform var(--dur-3) var(--ease-spring); }
.morph-nav__feature:hover .morph-nav__more span { transform: translateX(4px); }
.morph-nav__feature:focus-visible { box-shadow: var(--focus-ring); }

/* Simple link list */
.morph-nav__menu-list { display: grid; gap: 0.125rem; margin: 0; padding: 0; list-style: none; }
.morph-nav__menu-list a { padding: 0.625rem 0.75rem; border-radius: 0.75rem; color: var(--text-main); text-decoration: none; transition: background-color var(--dur-2); }
.morph-nav__menu-list a:hover { background: color-mix(in srgb, var(--text-main) 4%, transparent); }

/* Guide card */
.morph-nav__guide { display: grid; gap: 0.25rem; padding: 0.5rem; border-radius: 0.875rem; color: var(--text-main); text-decoration: none; transition: background-color var(--dur-2); }
.morph-nav__guide:hover { background: color-mix(in srgb, var(--text-main) 4%, transparent); }
.morph-nav__guide-art {
  height: 6rem; margin-bottom: 0.375rem; border-radius: 0.625rem;
  background:
    radial-gradient(70% 90% at 20% 20%, color-mix(in srgb, var(--primary-2) 75%, transparent), transparent 60%),
    radial-gradient(80% 80% at 90% 80%, color-mix(in srgb, var(--primary) 80%, transparent), transparent 60%),
    var(--surface-deep);
  transition: transform var(--dur-4) var(--ease-out);
}
.morph-nav__guide:hover .morph-nav__guide-art { transform: scale(1.02); }
.morph-nav__guide small { color: var(--primary); font-size: 0.75rem; font-weight: 600; }
.morph-nav__guide strong { font-size: 0.9375rem; font-weight: 600; line-height: 1.35; }

/* Desktop: inline triggers, floating panels over one morphing background */
@media (min-width: 768px) {
  .morph-nav { display: inline-block; }
  .morph-nav__list { display: flex; }
  .morph-nav__trigger, .morph-nav__link { width: auto; height: 2.5rem; justify-content: center; }
  .morph-nav__split { grid-template-columns: 1.55fr 1fr; }
  .morph-nav__split--even { grid-template-columns: 1fr 1fr; }
  .morph-nav__tiles { grid-template-columns: 1fr 1fr; }

  .morph-nav__panel {
    display: block; position: absolute; top: calc(100% + 0.75rem); left: 0; z-index: calc(var(--z-popover) + 1);
    width: min(var(--morph-panel-w, 24rem), calc(100vw - 2rem)); padding: 0.75rem;
    transform: translateX(var(--morph-px, 0)) translateX(calc(var(--from, 0) * 2.5rem));
    translate: 0 0.375rem; opacity: 0; visibility: hidden;
    transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-out),
                translate var(--dur-4) var(--ease-out), visibility 0s linear var(--dur-3);
  }
  .morph-nav__panel[data-active] { translate: 0 0; opacity: 1; visibility: visible; transition-delay: 0s; }

  .morph-nav__bg {
    display: block; position: absolute; top: calc(100% + 0.75rem); left: 0; z-index: var(--z-popover);
    width: var(--morph-w, 0); height: var(--morph-h, 0);
    transform: translateX(var(--morph-x, 0)); transform-origin: var(--morph-caret, 50%) 0;
    border: 1px solid var(--border-subtle); border-radius: var(--radius-xl);
    background: var(--surface-light); box-shadow: var(--shadow-xl);
    opacity: 0; scale: 0.96; visibility: hidden;
    transition: transform var(--dur-4) var(--ease-out), width var(--dur-4) var(--ease-out), height var(--dur-4) var(--ease-out),
                opacity var(--dur-2), scale var(--dur-3) var(--ease-out), visibility 0s linear var(--dur-2);
  }
  .morph-nav[data-open] .morph-nav__bg { opacity: 1; scale: 1; visibility: visible; transition-delay: 0s; }
  .morph-nav__caret {
    position: absolute; top: -7px; left: var(--morph-caret, 50%); width: 12px; height: 12px; margin-left: -6px;
    rotate: 45deg; border-top-left-radius: 3px; background: var(--surface-light);
    box-shadow: -1px -1px 0 0 var(--border-subtle);
    transition: left var(--dur-4) var(--ease-out);
  }
  /* First open: appear in place instead of morphing from the last menu's size */
  .morph-nav[data-instant] .morph-nav__bg { transition-property: opacity, scale, visibility; }
  .morph-nav[data-instant] .morph-nav__caret { transition: none; }
}
```

## JS

```js
document.querySelectorAll('[data-morph-nav]').forEach((nav) => {
  const triggers = [...nav.querySelectorAll('.morph-nav__trigger')];
  const desktop = matchMedia('(min-width: 768px)');
  const panelOf = (t) => document.getElementById(t.getAttribute('aria-controls'));
  let active = null;
  let openedAt = 0;
  let closeTimer = 0;

  // Fit the shared background to the panel, centred under its trigger and kept on screen
  const place = (t, panel) => {
    if (!desktop.matches) return;
    const nr = nav.getBoundingClientRect();
    const tr = t.getBoundingClientRect();
    const w = panel.offsetWidth;
    const centre = tr.left + tr.width / 2 - nr.left;
    const x = Math.min(Math.max(centre - w / 2, 16 - nr.left), innerWidth - 16 - w - nr.left);
    panel.style.setProperty('--morph-px', `${x}px`);
    nav.style.setProperty('--morph-x', `${x}px`);
    nav.style.setProperty('--morph-w', `${w}px`);
    nav.style.setProperty('--morph-h', `${panel.offsetHeight}px`);
    nav.style.setProperty('--morph-caret', `${centre - x}px`);
  };

  // Open a menu; content slides in from the direction of travel
  const open = (t) => {
    clearTimeout(closeTimer);
    if (active === t) return;
    const panel = panelOf(t);
    const dir = active ? Math.sign(triggers.indexOf(t) - triggers.indexOf(active)) : 0;
    if (active) {
      const old = panelOf(active);
      old.style.setProperty('--from', -dir);
      old.removeAttribute('data-active');
      active.setAttribute('aria-expanded', 'false');
    } else {
      nav.setAttribute('data-instant', '');
    }
    panel.style.transition = 'none';
    panel.style.setProperty('--from', dir);
    place(t, panel);
    void panel.offsetWidth; // commit the start position before animating
    panel.style.transition = '';
    panel.style.setProperty('--from', 0);
    panel.setAttribute('data-active', '');
    t.setAttribute('aria-expanded', 'true');
    nav.setAttribute('data-open', '');
    active = t;
    openedAt = performance.now();
    requestAnimationFrame(() => requestAnimationFrame(() => nav.removeAttribute('data-instant')));
  };

  const close = (refocus) => {
    if (!active) return;
    const panel = panelOf(active);
    panel.style.setProperty('--from', 0);
    panel.removeAttribute('data-active');
    active.setAttribute('aria-expanded', 'false');
    if (refocus === true) active.focus();
    nav.removeAttribute('data-open');
    active = null;
  };
  const closeSoon = () => { clearTimeout(closeTimer); closeTimer = setTimeout(close, 200); };
  const mouse = (e) => e.pointerType === 'mouse' && desktop.matches;

  // Hover opens on desktop; click toggles everywhere (a click right after hover-open keeps it open)
  triggers.forEach((t) => {
    t.addEventListener('click', () => (active === t && performance.now() - openedAt > 400 ? close() : open(t)));
    t.addEventListener('pointerenter', (e) => { if (mouse(e)) open(t); });
  });
  nav.querySelectorAll('.morph-nav__link').forEach((link) => link.addEventListener('pointerenter', (e) => { if (mouse(e)) closeSoon(); }));
  nav.addEventListener('pointerleave', (e) => { if (mouse(e)) closeSoon(); });
  nav.addEventListener('pointerenter', () => clearTimeout(closeTimer));
  nav.addEventListener('keydown', (e) => { if (e.key === 'Escape' && active) close(true); });
  nav.addEventListener('focusout', (e) => { if (!nav.contains(e.relatedTarget)) close(); });
  document.addEventListener('click', (e) => { if (!nav.contains(e.target)) close(); });
  addEventListener('resize', () => { if (active) place(active, panelOf(active)); });
});
```

## Notes

- Disclosure pattern, not `role="menu"`: each trigger is a button with `aria-expanded`, and its panel sits right after it in the DOM, so Tab flows from a trigger into its open panel. Inactive panels use `visibility: hidden`, so they leave the tab order.
- Hover opens with a 200ms grace period for crossing the gap, so menus don't flicker shut. Touch and keyboard use click/Enter; Escape closes and returns focus to the trigger.
- Set each panel's width with `--morph-panel-w`. Heights are measured, so content can change freely.
- Drop it into the track of `floating-navbar.md` in place of the plain link list. On mobile, put it inside that component's menu dialog, where it becomes an accordion.
- The background morph animates `width`/`height` on one absolutely positioned element; that's cheap. Don't animate the panels' own size.
