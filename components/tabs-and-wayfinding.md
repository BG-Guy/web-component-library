# Tabs & Wayfinding

Tabs, breadcrumbs, pagination, form progress, an in-page table of contents and a back-to-top button. Depends on `tokens/variables.css`.

| #  | Pattern                                                                                              | JS         |
| -- | ---------------------------------------------------------------------------------------------------- | ---------- |
| 1  | **Tabs**: horizontal APG tabs with a scrolling tablist on phones; stacked sections without JS         | ~24 lines  |
| 2  | **Vertical tabs**: sidebar tablist beside the panel from 768px, scrolling row above it on phones      | ~25 lines  |
| 3  | **Breadcrumbs**: ordered trail with CSS chevrons; collapses to Home › … › parent › current on phones  | none       |
| 4  | **Pagination**: page links with an ellipsis from 768px; "Page 3 of 10" with prev/next on phones       | none       |
| 5  | **Multi-step stepper**: form progress with connectors from 768px; "Step 2 of 4" and a bar on phones   | none       |
| 6  | **Table of contents with scrollspy**: `<details>` on small screens, sticky sidebar from 1024px        | ~20 lines  |
| 7  | **Back-to-top button**: floats in after one viewport; scrolls up, then moves focus to `#main`         | ~16 lines  |

## 1. Tabs

Horizontal tabs with automatic activation: arrow keys move focus and selection together, and the tablist scrolls sideways when the tabs don't fit.
**Approach:** the tablist ships pre-rendered with `hidden`, so without JS every panel is a stacked section with its heading. JS reveals the tablist, turns each section into a `tabpanel` named by its tab, and hides the rest. Place inside your page container.

### HTML

```html
<div class="tabs">
  <!-- Pre-rendered tablist: stays hidden until the script wires it up -->
  <div class="tabs__list" role="tablist" aria-label="Our services" hidden>
    <button class="tabs__tab" id="svc-tab-repairs" type="button" role="tab" aria-selected="true" aria-controls="svc-repairs">Repairs</button>
    <button class="tabs__tab" id="svc-tab-installs" type="button" role="tab" aria-selected="false" aria-controls="svc-installs" tabindex="-1">Installations</button>
    <button class="tabs__tab" id="svc-tab-plans" type="button" role="tab" aria-selected="false" aria-controls="svc-plans" tabindex="-1">Maintenance plans</button>
  </div>

  <!-- Plain sections without JS; the script turns them into tab panels -->
  <section class="tabs__panel" id="svc-repairs">
    <h3 class="tabs__heading">Repairs</h3>
    <p>Same-day fixes for leaks, tripped breakers and broken fixtures anywhere in Springfield.</p>
  </section>
  <section class="tabs__panel" id="svc-installs">
    <h3 class="tabs__heading">Installations</h3>
    <p>Water heaters, ceiling fans and smart thermostats, fitted, tested and cleaned up after.</p>
  </section>
  <section class="tabs__panel" id="svc-plans">
    <h3 class="tabs__heading">Maintenance plans</h3>
    <p>Two check-ups a year, priority booking and 10% off every repair.</p>
  </section>
</div>
```

### CSS

```css
/* Shell: tablist above the panel; the gap also spaces the stacked panels without JS */
.tabs { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--space-lg); }

/* Tablist: one row that scrolls sideways; padding keeps focus rings from being clipped */
.tabs__list {
  display: flex; gap: var(--space-xs); overflow-x: auto; scrollbar-width: thin;
  padding: var(--space-xs); border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-muted);
}
.tabs__list[hidden] { display: none; }

/* Tabs: muted pills; the selected one is filled */
.tabs__tab {
  flex: none; min-height: 2.75rem; padding: var(--space-sm) var(--space-md);
  border: 0; border-radius: var(--radius-md); background: transparent; cursor: pointer;
  color: var(--text-muted); font: inherit; font-weight: 600; white-space: nowrap;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}
.tabs__tab:hover { color: var(--text-main); }
.tabs__tab[aria-selected="true"] { background: var(--primary); color: var(--text-inverse); }
.tabs__tab:focus-visible,
.tabs__panel:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.tabs__panel { border-radius: var(--radius-sm); }
.tabs__heading { margin: 0 0 var(--space-sm); font-size: 1.25rem; }

/* With JS the tab names the panel, so the heading stays for screen readers only */
.tabs__panel[role="tabpanel"] > .tabs__heading {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
```

### JS

```js
// Tabs: reveal the pre-rendered tablist; ←/→ wrap, Home/End jump; selection follows focus
document.querySelectorAll('.tabs').forEach((root) => {
  const list = root.querySelector('.tabs__list');
  const tabs = [...list.querySelectorAll('.tabs__tab')];
  const panels = tabs.map((t) => document.getElementById(t.getAttribute('aria-controls')));
  const select = (tab) => tabs.forEach((t, i) => {
    t.setAttribute('aria-selected', t === tab);
    t.tabIndex = t === tab ? 0 : -1;
    panels[i].hidden = t !== tab;
  });
  tabs.forEach((t, i) => {
    // Each stacked section becomes a focusable panel named by its tab
    panels[i].setAttribute('role', 'tabpanel');
    panels[i].setAttribute('aria-labelledby', t.id);
    panels[i].tabIndex = 0;
    ['click', 'focus'].forEach((type) => t.addEventListener(type, () => select(t)));
    t.addEventListener('keydown', (e) => {
      const to = { ArrowLeft: i - 1, ArrowRight: i + 1, Home: 0, End: -1 }[e.key];
      if (to === undefined) return;
      e.preventDefault();
      tabs.at(to % tabs.length).focus(); // negative index wraps to the end
    });
  });
  list.hidden = false;
  select(tabs.find((t) => t.getAttribute('aria-selected') === 'true') ?? tabs[0]);
});
```

### Notes

- Selection follows focus (the `focus` listener), which is APG automatic activation. Keep `click` too: Safari doesn't focus buttons on click. If a panel fetches content, switch to manual activation (select on Enter/Space only).
- Panels get `tabindex="0"` so text-only panels are reachable with Tab. Headings stay in the panels (visually hidden with JS), so heading navigation still works; pick the level that fits your outline.
- Module scripts run after parsing, so the panels show stacked for a moment before JS hides them. Keep tabs below the fold, or reserve the panel height with `min-height`.
- **React:** derive `aria-selected`, `tabIndex` and `hidden` from one `selected` index. Render the tablist without `hidden` if you don't need the no-JS fallback.

## 2. Vertical tabs

Standalone: same model as the horizontal tabs, with the tablist as a sidebar beside the panel from 768px (↑/↓, Home/End) and a scrolling row above it on phones (←/→). `aria-orientation` follows the layout. Without JS, panels stack with their headings. Place inside your page container.

### HTML

```html
<div class="tabs-vertical">
  <!-- Pre-rendered tablist: stays hidden until the script wires it up -->
  <div class="tabs-vertical__list" role="tablist" aria-label="Before you book" hidden>
    <button class="tabs-vertical__tab" id="info-tab-quotes" type="button" role="tab" aria-selected="true" aria-controls="info-quotes">Free quotes</button>
    <button class="tabs-vertical__tab" id="info-tab-warranty" type="button" role="tab" aria-selected="false" aria-controls="info-warranty" tabindex="-1">Warranty</button>
    <button class="tabs-vertical__tab" id="info-tab-payment" type="button" role="tab" aria-selected="false" aria-controls="info-payment" tabindex="-1">Payment options</button>
    <button class="tabs-vertical__tab" id="info-tab-area" type="button" role="tab" aria-selected="false" aria-controls="info-area" tabindex="-1">Service area</button>
  </div>

  <section class="tabs-vertical__panel" id="info-quotes">
    <h3 class="tabs-vertical__heading">Free quotes</h3>
    <p>We visit, measure and email a fixed written quote within two working days. No obligation.</p>
  </section>
  <section class="tabs-vertical__panel" id="info-warranty">
    <h3 class="tabs-vertical__heading">Warranty</h3>
    <p>Every job carries a two-year labor warranty on top of the manufacturer's parts warranty.</p>
  </section>
  <section class="tabs-vertical__panel" id="info-payment">
    <h3 class="tabs-vertical__heading">Payment options</h3>
    <p>Pay by card or bank transfer, or in three interest-free installments on jobs over $1,000.</p>
  </section>
  <section class="tabs-vertical__panel" id="info-area">
    <h3 class="tabs-vertical__heading">Service area</h3>
    <p>Springfield and every town within 25 miles. Not sure? Call <a href="tel:+15555550123">(555) 555-0123</a>.</p>
  </section>
</div>
```

### CSS

```css
/* Shell: tablist above the panel on phones; the gap also spaces the stacked panels without JS */
.tabs-vertical { display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--space-lg); }

/* Phones: one row of tabs that scrolls sideways; padding keeps focus rings from being clipped */
.tabs-vertical__list { display: flex; overflow-x: auto; scrollbar-width: thin; padding: var(--space-xs); }
.tabs-vertical__list[hidden] { display: none; }
.tabs-vertical__tab {
  flex: none; min-height: 2.75rem; padding: var(--space-sm) var(--space-md);
  border: 0; border-bottom: 2px solid var(--border-subtle); background: transparent; cursor: pointer;
  color: var(--text-muted); font: inherit; font-weight: 600; text-align: start; white-space: nowrap;
  transition: background-color var(--transition-fast), color var(--transition-fast), border-color var(--transition-fast);
}
.tabs-vertical__tab:hover { background: var(--surface-muted); color: var(--text-main); }
.tabs-vertical__tab[aria-selected="true"] { border-color: var(--primary); color: var(--primary); }
.tabs-vertical__tab:focus-visible,
.tabs-vertical__panel:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.tabs-vertical__panel { border-radius: var(--radius-sm); }
.tabs-vertical__heading { margin: 0 0 var(--space-sm); font-size: 1.25rem; }

/* With JS the tab names the panel, so the heading stays for screen readers only */
.tabs-vertical__panel[role="tabpanel"] > .tabs-vertical__heading {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* 768px+: sidebar column. Panels are pinned to column 2; without JS column 1 is empty and collapses to 0 */
@media (min-width: 768px) {
  .tabs-vertical { grid-template-columns: auto minmax(0, 1fr); column-gap: 0; align-items: start; }
  .tabs-vertical__list { flex-direction: column; width: 14rem; margin-inline-end: var(--space-xl); overflow: visible; }
  .tabs-vertical__tab {
    white-space: normal; border-bottom: 0; border-inline-start: 2px solid var(--border-subtle);
    border-start-end-radius: var(--radius-md); border-end-end-radius: var(--radius-md);
  }
  .tabs-vertical__panel { grid-column: 2; }
}
```

### JS

```js
// Vertical tabs: ↑/↓ while the list is a sidebar (768px+), ←/→ while it is a row; selection follows focus
document.querySelectorAll('.tabs-vertical').forEach((root) => {
  const wide = matchMedia('(min-width: 768px)');
  const list = root.querySelector('.tabs-vertical__list');
  const tabs = [...list.querySelectorAll('.tabs-vertical__tab')];
  const panels = tabs.map((t) => document.getElementById(t.getAttribute('aria-controls')));
  // Reveal the tablist and keep aria-orientation in step with the layout
  const orient = () => Object.assign(list, { hidden: false, ariaOrientation: wide.matches ? 'vertical' : 'horizontal' });
  const select = (tab) => tabs.forEach((t, i) => {
    Object.assign(t, { ariaSelected: t === tab, tabIndex: t === tab ? 0 : -1 });
    panels[i].hidden = t !== tab;
  });
  tabs.forEach((t, i) => {
    Object.assign(panels[i], { role: 'tabpanel', tabIndex: 0 }).setAttribute('aria-labelledby', t.id);
    ['click', 'focus'].forEach((type) => t.addEventListener(type, () => select(t)));
    t.addEventListener('keydown', (e) => {
      const [prev, next] = wide.matches ? ['ArrowUp', 'ArrowDown'] : ['ArrowLeft', 'ArrowRight'];
      const to = { [prev]: i - 1, [next]: i + 1, Home: 0, End: -1 }[e.key];
      if (to === undefined) return;
      e.preventDefault();
      tabs.at(to % tabs.length).focus();
    });
  });
  wide.addEventListener('change', orient);
  orient();
  select(tabs.find((t) => t.ariaSelected === 'true') ?? tabs[0]);
});
```

### Notes

- Arrow keys always match what's on screen: the same `matchMedia` drives the key map and `aria-orientation`, so a resize or rotation switches both.
- No `:has()` needed for the no-JS layout: panels sit in grid column 2, and with the tablist hidden, column 1 is empty and collapses to zero width.
- Uses ARIA reflection (`el.ariaSelected`, `el.ariaOrientation`, `el.role`): Chrome 81+, Safari 12.1+, Firefox 119+. Swap in `setAttribute` for older browsers.
- Long labels wrap in the sidebar and stay on one line in the phone row. Keep labels short (1–3 words) so the row stays scannable.

## 3. Breadcrumbs

A `nav` landmark with an ordered trail. The last crumb is plain text with `aria-current="page"`. Chevrons are CSS masks on empty pseudo-elements, so they're never read aloud. On phones the middle collapses to Home › … › parent › current. Place inside your page container.

### HTML

```html
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol class="breadcrumbs__list" role="list">
    <li class="breadcrumbs__item"><a class="breadcrumbs__link" href="/">Home</a></li>
    <li class="breadcrumbs__item"><a class="breadcrumbs__link" href="/services/">Services</a></li>
    <li class="breadcrumbs__item"><a class="breadcrumbs__link" href="/services/plumbing/">Plumbing</a></li>
    <li class="breadcrumbs__item"><span class="breadcrumbs__current" aria-current="page">Water heater repair</span></li>
  </ol>
</nav>
```

### CSS

```css
/* Shape-only masks; color comes from the pseudo-element's background */
.breadcrumbs {
  --breadcrumbs-chevron: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='m9 6 6 6-6 6' fill='none' stroke='black' stroke-width='2'/></svg>");
  --breadcrumbs-dots: url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M6 12h.01M12 12h.01M18 12h.01' stroke='black' stroke-width='3' stroke-linecap='round'/></svg>");
  font-size: 0.875rem;
}
.breadcrumbs__list { display: flex; flex-wrap: wrap; align-items: center; margin: 0; padding: 0; list-style: none; }
.breadcrumbs__item { display: flex; align-items: center; }

/* Separator: an empty, masked pseudo-element, so screen readers skip it */
.breadcrumbs__item + .breadcrumbs__item::before {
  content: ""; flex: none; width: 1rem; height: 1rem; margin-inline: var(--space-xs);
  background: var(--text-muted);
  mask: var(--breadcrumbs-chevron) center / contain no-repeat;
}
.breadcrumbs__link {
  display: inline-flex; align-items: center; min-height: 1.5rem;
  border-radius: var(--radius-sm); color: var(--primary); text-underline-offset: 0.2em;
  transition: color var(--transition-fast);
}
.breadcrumbs__link:hover { color: var(--primary-hover); }
.breadcrumbs__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.breadcrumbs__current { color: var(--text-main); font-weight: 600; }

/* Phones: keep Home and the last two crumbs; the separator before the parent becomes "› … ›" */
.breadcrumbs__item:not(:first-child, :nth-last-child(-n + 2)) { display: none; }
.breadcrumbs__item:nth-last-child(2):nth-child(n + 3)::before {
  width: 3rem;
  mask: var(--breadcrumbs-chevron) left / 1rem no-repeat,
    var(--breadcrumbs-dots) center / 1rem no-repeat,
    var(--breadcrumbs-chevron) right / 1rem no-repeat;
}

/* 768px+: full trail */
@media (min-width: 768px) {
  .breadcrumbs__item:not(:first-child, :nth-last-child(-n + 2)) { display: flex; }
  .breadcrumbs__item:nth-last-child(2):nth-child(n + 3)::before {
    width: 1rem; mask: var(--breadcrumbs-chevron) center / contain no-repeat;
  }
}
```

### Notes

- The current page is text, not a link to itself. `aria-current="page"` tells screen readers it's where they are.
- Collapsed crumbs use `display: none`, so phone screen-reader users get the short trail too. The parent link, the most useful one, always stays.
- Unprefixed `mask` needs Chrome 120+, Safari 15.4+ or Firefox 53+. Duplicate the two `mask` declarations as `-webkit-mask` for older Chromium.
- Add `BreadcrumbList` JSON-LD: one `ListItem` per crumb with `position`, `name` and an absolute `item` URL (e.g. `https://example.com/services/`). The current page may omit `item`. Keep the names identical to the visible crumbs.

## 4. Pagination

Real links for every page, with `aria-current="page"` and an ellipsis for skipped ranges from 768px. Below 768px it shows a compact "Page 3 of 10" between icon-only prev/next links. Every target is 44px. Place inside your page container.

### HTML

```html
<nav class="pagination" aria-label="Pagination">
  <a class="pagination__step" href="?page=2" rel="prev" aria-label="Previous page">
    <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m15 18-6-6 6-6" /></svg>
    <span class="pagination__label">Previous</span>
  </a>

  <!-- Phones only -->
  <p class="pagination__status">Page 3 of 10</p>

  <!-- 768px+ only -->
  <ol class="pagination__list" role="list">
    <li><a class="pagination__link" href="?page=1" aria-label="Page 1">1</a></li>
    <li><a class="pagination__link" href="?page=2" aria-label="Page 2">2</a></li>
    <li><a class="pagination__link" href="?page=3" aria-label="Page 3" aria-current="page">3</a></li>
    <li><a class="pagination__link" href="?page=4" aria-label="Page 4">4</a></li>
    <li class="pagination__gap" aria-hidden="true">…</li>
    <li><a class="pagination__link" href="?page=10" aria-label="Page 10">10</a></li>
  </ol>

  <a class="pagination__step" href="?page=4" rel="next" aria-label="Next page">
    <span class="pagination__label">Next</span>
    <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m9 18 6-6-6-6" /></svg>
  </a>
</nav>
```

### CSS

```css
/* Phones: [‹]  Page 3 of 10  [›] */
.pagination { display: flex; align-items: center; justify-content: space-between; gap: var(--space-sm); }
.pagination__step,
.pagination__link {
  display: inline-flex; align-items: center; justify-content: center; gap: var(--space-xs);
  min-width: 2.75rem; min-height: 2.75rem; padding-inline: var(--space-sm);
  border-radius: var(--radius-md); color: var(--primary); font-weight: 600; text-decoration: none;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}
.pagination__step { border: 1px solid var(--border-subtle); }
.pagination__step svg {
  flex: none; width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.pagination__step:hover,
.pagination__link:hover { background: var(--surface-muted); }
.pagination__link[aria-current="page"] { background: var(--primary); color: var(--text-inverse); }
.pagination__step:focus-visible,
.pagination__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Placeholder that keeps the layout on the first or last page */
.pagination__step--disabled { color: var(--text-muted); opacity: 0.5; pointer-events: none; }
.pagination__status { margin: 0; color: var(--text-muted); font-size: 0.875rem; }
.pagination__label,
.pagination__list { display: none; }
.pagination__gap { display: grid; place-items: center; min-width: 2rem; color: var(--text-muted); }

/* 768px+: full page list; the status line hides (aria-current marks the page instead) */
@media (min-width: 768px) {
  .pagination { justify-content: center; }
  .pagination__step { padding-inline: var(--space-md); }
  .pagination__label { display: inline; }
  .pagination__list { display: flex; gap: var(--space-xs); margin: 0; padding: 0; list-style: none; }
  .pagination__status { display: none; }
}
```

### Notes

- Prev/next carry `aria-label` because their text is hidden on phones. The visible "Previous"/"Next" stays inside the name (2.5.3 Label in Name).
- On page 1 (or the last page), swap the missing link for `<span class="pagination__step pagination__step--disabled" aria-hidden="true">` plus the icon, so the layout doesn't jump.
- Show the first and last pages and the current page ±1, with an `aria-hidden` ellipsis `li` for each gap.
- Use real `href`s (`?page=4`) so paging works without JS and can be crawled. Each page should get its own `<title>` ("Projects, page 3 – Brand").

## 5. Multi-step stepper

Progress for a multi-page form as an `<ol>`: completed, current (`aria-current="step"`) and upcoming steps, each with visually hidden state text. Horizontal with connectors from 768px. Phones get "Step 2 of 4: Details" and a mini progress bar instead. Place inside your page container.

### HTML

```html
<div class="stepper">
  <!-- Phones: compact summary (the list below is hidden) -->
  <div class="stepper__compact">
    <p class="stepper__summary">Step 2 of 4: <strong class="stepper__name">Details</strong></p>
    <span class="stepper__bar" style="--stepper-progress: 50%" aria-hidden="true"></span>
  </div>

  <!-- 768px+: full list (the summary above is hidden) -->
  <ol class="stepper__list" role="list" aria-label="Booking progress">
    <li class="stepper__step stepper__step--done">
      <span class="stepper__marker" aria-hidden="true">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M20 6 9 17l-5-5" /></svg>
      </span>
      <span class="stepper__label"><span class="stepper__sr">Completed: </span>Contact</span>
    </li>
    <li class="stepper__step" aria-current="step">
      <span class="stepper__marker" aria-hidden="true">2</span>
      <span class="stepper__label"><span class="stepper__sr">Current: </span>Details</span>
    </li>
    <li class="stepper__step">
      <span class="stepper__marker" aria-hidden="true">3</span>
      <span class="stepper__label">Schedule</span>
    </li>
    <li class="stepper__step">
      <span class="stepper__marker" aria-hidden="true">4</span>
      <span class="stepper__label">Confirm</span>
    </li>
  </ol>
</div>
```

### CSS

```css
/* Shared marker size */
.stepper { --stepper-size: 2rem; }

/* Phones: text summary plus a thin bar (decorative: the text carries the information) */
.stepper__summary { margin: 0 0 var(--space-sm); color: var(--text-muted); font-size: 0.875rem; }
.stepper__name { color: var(--text-main); }
.stepper__bar {
  display: block; height: 0.5rem; overflow: hidden; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--primary) 15%, var(--surface-light));
}
.stepper__bar::before {
  content: ""; display: block; width: var(--stepper-progress, 0%); height: 100%;
  border-radius: inherit; background: var(--primary);
}
.stepper__list { display: none; }

/* Markers: upcoming = muted outline, current = primary outline, completed = filled check */
.stepper__marker {
  display: grid; place-items: center; width: var(--stepper-size); height: var(--stepper-size);
  border: 2px solid var(--text-muted); border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-muted); font-size: 0.875rem; font-weight: 700;
}
.stepper__marker svg {
  width: 1rem; height: 1rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.stepper__label { color: var(--text-muted); font-size: 0.875rem; }
.stepper__step--done .stepper__marker { border-color: var(--primary); background: var(--primary); color: var(--text-inverse); }
.stepper__step[aria-current="step"] .stepper__marker { border-color: var(--primary); color: var(--primary); }
.stepper__step--done .stepper__label { color: var(--text-main); }
.stepper__step[aria-current="step"] .stepper__label { color: var(--text-main); font-weight: 600; }
.stepper__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* 768px+: horizontal list; each connector runs from the previous marker to this one */
@media (min-width: 768px) {
  .stepper__compact { display: none; }
  .stepper__list { display: flex; margin: 0; padding: 0; list-style: none; }
  .stepper__step {
    position: relative; flex: 1 1 0; min-width: 0;
    display: flex; flex-direction: column; align-items: center; gap: var(--space-sm); text-align: center;
  }
  .stepper__step + .stepper__step::before {
    content: ""; position: absolute; top: calc(var(--stepper-size) / 2 - 1px); height: 2px;
    left: calc(-50% + var(--stepper-size) / 2 + var(--space-xs));
    right: calc(50% + var(--stepper-size) / 2 + var(--space-xs));
    background: var(--border-subtle);
  }
  .stepper__step--done + .stepper__step::before { background: var(--primary); }
}
```

### Notes

- Each breakpoint shows one version (the other is `display: none`), so screen readers never hear progress twice.
- The hidden "Completed"/"Current" text covers screen readers that skip `aria-current`. The marker numbers are `aria-hidden` because the `<ol>` already announces "2 of 4".
- It reports progress and isn't interactive. To let people revisit finished steps, link their labels and wrap the list in `<nav aria-label="Booking progress">`.
- Set `--stepper-progress` server-side (current step ÷ total), and put the step in each page's `<title>` ("Details, step 2 of 4 – Brand") so it's announced on load.

## 6. Table of contents with scrollspy

An "On this page" list in a `<details>` above the content, which becomes a sticky sidebar from 1024px. An IntersectionObserver sets `aria-current="true"` on the link for the section in view. `.toc__layout` is an example two-column wrapper. Place inside your page container.

### HTML

```html
<div class="toc__layout">
  <nav class="toc" aria-label="On this page">
    <!-- Ships open, so the list shows without JS; JS collapses it below 1024px -->
    <details class="toc__details" open>
      <summary class="toc__summary">
        On this page
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m6 9 6 6 6-6" /></svg>
      </summary>
      <ol class="toc__list" role="list">
        <li><a class="toc__link" href="#signs">Signs you need a new roof</a></li>
        <li><a class="toc__link" href="#materials">Choosing materials</a></li>
        <li><a class="toc__link" href="#cost">What it costs</a></li>
        <li><a class="toc__link" href="#timeline">Project timeline</a></li>
      </ol>
    </details>
  </nav>

  <div class="toc__content">
    <section class="toc__section" id="signs">
      <h2>Signs you need a new roof</h2>
      <p>Curling shingles, granules in the gutters and daylight in the attic are the big three.</p>
    </section>
    <section class="toc__section" id="materials">
      <h2>Choosing materials</h2>
      <p>Asphalt is the budget pick, metal lasts longest, and tile suits Springfield's older homes.</p>
    </section>
    <section class="toc__section" id="cost">
      <h2>What it costs</h2>
      <p>Most homes land between $9,000 and $16,000, depending on size, pitch and material.</p>
    </section>
    <section class="toc__section" id="timeline">
      <h2>Project timeline</h2>
      <p>Two to four days on site, plus a final walkthrough and cleanup.</p>
    </section>
  </div>
</div>
```

### CSS

```css
/* Example layout: one column, TOC first; --toc-offset = sticky header height + breathing room */
.toc__layout {
  --toc-offset: var(--space-lg);
  display: grid; grid-template-columns: minmax(0, 1fr); gap: var(--space-xl);
}
.toc__section { scroll-margin-top: var(--toc-offset); }

/* Small screens: a collapsible box above the content */
.toc__details { border: 1px solid var(--border-subtle); border-radius: var(--radius-md); background: var(--surface-muted); }
.toc__summary {
  display: flex; align-items: center; justify-content: space-between; gap: var(--space-sm);
  min-height: 2.75rem; padding: var(--space-sm) var(--space-md); border-radius: var(--radius-md);
  color: var(--text-main); font-weight: 600; cursor: pointer; list-style: none;
}
.toc__summary::-webkit-details-marker { display: none; }
.toc__summary svg {
  flex: none; width: 1.25rem; height: 1.25rem; transition: rotate var(--transition-smooth);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.toc__details[open] .toc__summary svg { rotate: 180deg; }
.toc__list { display: grid; gap: var(--space-xs); margin: 0; padding: 0 var(--space-md) var(--space-md); list-style: none; }

/* Links: a start-edge rule marks the section in view */
.toc__link {
  display: block; padding: var(--space-xs) var(--space-sm);
  border-inline-start: 2px solid var(--border-subtle);
  color: var(--text-muted); font-size: 0.875rem; text-decoration: none;
  transition: color var(--transition-fast), border-color var(--transition-fast);
}
.toc__link:hover { color: var(--text-main); }
.toc__link[aria-current="true"] { border-color: var(--primary); color: var(--primary); font-weight: 600; }
.toc__summary:focus-visible,
.toc__link:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* 1024px+: sticky sidebar; the summary hides because the list is always open */
@media (min-width: 1024px) {
  .toc__layout { grid-template-columns: 15rem minmax(0, 1fr); gap: var(--space-2xl); align-items: start; }
  .toc { position: sticky; top: var(--toc-offset); max-height: calc(100vh - 2 * var(--toc-offset)); overflow-y: auto; }
  .toc__details { border: 0; background: none; }
  .toc__summary { display: none; }
  .toc__list { padding: var(--space-xs); }
}
```

### JS

```js
// TOC: open sidebar from 1024px, collapsed <details> below; aria-current marks the section in view
document.querySelectorAll('.toc').forEach((toc) => {
  const details = toc.querySelector('.toc__details');
  const links = [...toc.querySelectorAll('.toc__link')];
  const wide = matchMedia('(min-width: 1024px)');
  const sync = () => { details.open = wide.matches; };
  wide.addEventListener('change', sync);
  sync();
  // The section crossing a thin band 25% down the viewport is "current"
  const spy = new IntersectionObserver((entries) => entries.forEach((entry) => {
    if (!entry.isIntersecting) return;
    links.forEach((a) => {
      if (a.getAttribute('href') === `#${entry.target.id}`) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
  }), { rootMargin: '-25% 0px -74% 0px' });
  links.forEach((a) => {
    const section = document.getElementById(a.getAttribute('href').slice(1));
    if (section) spy.observe(section);
    // Below 1024px, collapse the list after a jump so it doesn't push the section down
    a.addEventListener('click', () => { if (!wide.matches) details.open = false; });
  });
});
```

### Notes

- Without JS the `<details>` stays open at every width and the links still jump. With JS it opens and closes with the 1024px breakpoint.
- It observes whole sections, not headings, so the section you're reading stays current until the next one reaches the band. A very short last section may never reach it; that's a known limit of band-based scrollspy.
- With a sticky site header, set `--toc-offset` to its height plus a gap. It drives both the sidebar's `top` and each section's `scroll-margin-top`.
- `aria-current="true"` only marks the link; it never moves focus, so reading isn't interrupted.

## 7. Back-to-top button

A fixed button (z-index 5, clear of safe areas) that appears once you've scrolled about one viewport, using an IntersectionObserver on a top sentinel. It scrolls up smoothly (instantly under reduced motion), then moves focus to `#main`. While not shown it's hidden from assistive tech. Without JS it's an ordinary in-flow link.

### HTML

```html
<body>
  <!-- First thing in <body>: an invisible marker, one viewport tall -->
  <div class="to-top__sentinel"></div>
  …
  <main id="main" tabindex="-1">
    …
    <!-- Last thing in <main>: a text link without JS, a floating icon button with it -->
    <a class="to-top" href="#main">
      <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m18 15-6-6-6 6" /></svg>
      <span class="to-top__label">Back to top</span>
    </a>
  </main>
</body>
```

### CSS

```css
/* Sentinel: covers the first viewport of the page; the button shows once it has scrolled away */
.to-top__sentinel { position: absolute; top: 0; left: 0; width: 1px; height: 100vh; pointer-events: none; }

/* Without JS: an ordinary in-flow link */
.to-top {
  display: inline-flex; align-items: center; justify-content: center; gap: var(--space-sm);
  min-height: 2.75rem; padding: var(--space-sm) var(--space-md); border-radius: var(--radius-full);
  color: var(--primary); font-weight: 600; text-decoration: none;
}
.to-top svg {
  flex: none; width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.to-top:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* With JS: a floating icon button, hidden (and out of the accessibility tree) until --shown */
.to-top--js {
  position: fixed; z-index: 5;
  right: calc(var(--space-md) + env(safe-area-inset-right, 0px));
  bottom: calc(var(--space-md) + env(safe-area-inset-bottom, 0px));
  width: 2.75rem; height: 2.75rem; padding: 0;
  background: var(--primary); color: var(--text-inverse); box-shadow: var(--shadow-lg);
  opacity: 0; visibility: hidden; translate: 0 var(--space-sm);
  transition: opacity var(--transition-smooth), translate var(--transition-smooth),
    visibility var(--transition-smooth), background-color var(--transition-fast);
}
.to-top--shown { opacity: 1; visibility: visible; translate: 0; }
.to-top--js:hover { background: var(--primary-hover); }

/* Floats over light and dark sections: a --primary outline with offset reads on both */
.to-top--js:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; box-shadow: var(--shadow-lg); }
.to-top--js .to-top__label {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
```

### JS

```js
// Back to top: float in once the sentinel scrolls away; on click, scroll up and move focus to the target
document.querySelectorAll('.to-top').forEach((link) => {
  const sentinel = document.querySelector('.to-top__sentinel');
  const target = document.getElementById(link.hash.slice(1));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  if (!sentinel || !target) return;
  link.classList.add('to-top--js');
  new IntersectionObserver(([entry]) => {
    link.classList.toggle('to-top--shown', !entry.isIntersecting);
  }).observe(sentinel);
  link.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({ top: 0, behavior: reduce.matches ? 'instant' : 'smooth' });
    if (!target.hasAttribute('tabindex')) target.tabIndex = -1;
    target.focus({ preventScroll: true });
  });
});
```

### Notes

- Moving focus to `#main` means the next Tab starts at the top of the content, not back in the footer. `tabindex="-1"` is added if `#main` lacks it, and a skip link can share the same target.
- The hidden state uses `visibility: hidden`, so the button leaves the tab order and the accessibility tree, not just the screen.
- Starting as an in-flow link avoids a flash at load: it sits at the end of `<main>` until the script turns it into the floating button.
- `env(safe-area-inset-*)` needs `viewport-fit=cover` in the viewport meta. Raise `bottom` if the page also has the sticky mobile call bar from `components/cta-sections.md`.
- Its focus style differs from the light-surface ring on purpose: the `--primary` outline keeps 3:1 against both `--surface-light` and `--surface-dark`.
