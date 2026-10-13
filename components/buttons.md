# Buttons

A base button system plus icon, loading, toggle, segmented, grouped, split, floating and copy buttons. Depends on `tokens/variables.css`.

| #  | Pattern                                                                         | JS         |
| -- | ------------------------------------------------------------------------------- | ---------- |
| 1  | **Base button**: five variants, three sizes, full width, disabled states        | none       |
| 2  | **Icon-only buttons**: square or round, three sizes, `aria-label` required      | none       |
| 3  | **Buttons with icons**: leading or trailing icon; arrows nudge on hover/focus   | none       |
| 4  | **Loading button**: inline spinner, `aria-busy`, fixed width, demo request      | ~20 lines  |
| 5  | **Toggle button**: `aria-pressed` on/off with a filled-icon pressed state       | ~7 lines   |
| 6  | **Segmented control**: radio inputs drawn as a joined button row                | none       |
| 7  | **Button group**: attached buttons that stack full width on phones              | none       |
| 8  | **Split button**: main action plus a disclosure list of more actions            | ~25 lines  |
| 9  | **Floating action button**: fixed corner button with a speed dial of actions    | ~24 lines  |
| 10 | **Copy button**: copies text, announces "Copied", explains failures             | ~21 lines  |

## 1. Base button

Five variants, three sizes, full width and disabled states, on `<a>` or `<button>`. Default height is 2.75rem (44px). Variants only swap the `--btn-*` colors, so hover, focus and disabled behave the same everywhere.

### HTML

```html
<!-- Variants: identical on <button> and <a> -->
<button class="btn btn--primary" type="button">Get a free quote</button>
<a class="btn btn--secondary" href="https://example.com/services">Our services</a>
<button class="btn btn--outline" type="button">Compare plans</button>
<button class="btn btn--ghost" type="button">Not now</button>
<button class="btn btn--danger" type="button">Cancel booking</button>

<!-- Sizes and full width -->
<button class="btn btn--primary btn--sm" type="button">Add a note</button>
<a class="btn btn--primary btn--lg" href="tel:+15555550123">Call (555) 555-0123</a>
<button class="btn btn--primary btn--block" type="submit">Book my visit</button>

<!-- Disabled: native on <button>; on <a>, drop href and add role="link" -->
<button class="btn btn--primary" type="button" disabled>Booking closed</button>
<a class="btn btn--outline" role="link" aria-disabled="true">Fully booked</a>
```

### CSS

```css
/* Base box, type and states. Variants below only change the --btn-* colors. */
.btn {
  --btn-bg: var(--surface-light);
  --btn-bg-hover: var(--surface-muted);
  --btn-fg: var(--text-main);
  --btn-border: var(--border-subtle);
  display: inline-flex; align-items: center; justify-content: center; gap: var(--space-sm);
  box-sizing: border-box; min-height: 2.75rem; max-width: 100%;
  padding: var(--space-sm) var(--space-lg);
  border: 1px solid var(--btn-border); border-radius: var(--radius-md);
  background: var(--btn-bg); color: var(--btn-fg);
  font: 600 1rem/1.25 var(--font-sans); text-align: center; text-decoration: none;
  cursor: pointer; touch-action: manipulation;
  transition: background-color var(--transition-fast), border-color var(--transition-fast),
    color var(--transition-fast), box-shadow var(--transition-fast);
}
.btn[hidden] { display: none; }
.btn:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
@media (hover: hover) {
  .btn:hover { background: var(--btn-bg-hover); }
}

/* Inline SVG icons scale with the label and take its color */
.btn svg {
  flex: none; width: 1.25em; height: 1.25em;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}

/* Variants. Transparent borders keep sizes equal and show up in forced-colors mode. */
.btn--primary {
  --btn-bg: var(--primary); --btn-bg-hover: var(--primary-hover);
  --btn-border: transparent; --btn-fg: var(--text-inverse);
}
.btn--secondary {
  --btn-bg: color-mix(in srgb, var(--primary) 10%, var(--surface-light));
  --btn-bg-hover: color-mix(in srgb, var(--primary) 18%, var(--surface-light));
  --btn-border: transparent; --btn-fg: var(--primary-hover);
}
.btn--outline {
  --btn-bg: transparent; --btn-bg-hover: color-mix(in srgb, var(--primary) 6%, transparent);
  --btn-border: var(--primary); --btn-fg: var(--primary);
}
.btn--ghost {
  --btn-bg: transparent; --btn-bg-hover: color-mix(in srgb, var(--text-main) 6%, transparent);
  --btn-border: transparent;
}
.btn--danger {
  --btn-bg: var(--danger); --btn-bg-hover: color-mix(in srgb, var(--danger) 85%, var(--surface-dark));
  --btn-border: transparent; --btn-fg: var(--text-inverse);
}

/* Sizes and full width */
.btn--sm { min-height: 2rem; padding: var(--space-xs) var(--space-md); font-size: 0.875rem; }
.btn--lg { min-height: 3.25rem; padding: var(--space-sm) var(--space-xl); font-size: 1.125rem; }
.btn--block { display: flex; width: 100%; }

/* Disabled: flat and muted, still 4.5:1. Busy buttons (pattern 4) keep their variant colors. */
.btn:is(:disabled, [aria-disabled="true"]):not([aria-busy="true"]) {
  --btn-bg: var(--surface-muted); --btn-bg-hover: var(--surface-muted);
  --btn-border: var(--border-subtle); --btn-fg: var(--text-muted);
  cursor: not-allowed;
}
```

### Notes

- `<a href>` navigates, `<button>` acts. Always set `type`: a bare `<button>` inside a form submits it.
- `disabled` removes the button from the tab order. `aria-disabled="true"` keeps it focusable (pair it with `aria-describedby` to say why) but doesn't block clicks, so guard your handler.
- Text contrast on white: primary 5:1, secondary 5.8:1, outline 5.2:1, danger 4.6:1, disabled 4.5:1. `--sm` is 32px, above the 24px minimum; keep primary touch actions at the default.
- Variants assume a light surface. On `--surface-dark` or `--primary` sections, change the focus style to `outline: 2px solid var(--text-inverse); outline-offset: 2px`.
- Tints use `color-mix()` (Chrome 111, Safari 16.2, Firefox 113). Older browsers fall back to a transparent background, which keeps text contrast.

## 2. Icon-only buttons

Builds on 1. Base button. Square or round buttons that show only an icon. The `aria-label` is the accessible name and there's no tooltip, so use only icons people recognize.

### HTML

```html
<!-- Square (default radius) -->
<button class="btn btn--ghost btn-icon" type="button" aria-label="Close">
  <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6 6 18"/></svg>
</button>
<button class="btn btn--outline btn-icon btn-icon--sm" type="button" aria-label="Edit address">
  <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M4 20h4L19 9l-4-4L4 16v4Z"/></svg>
</button>

<!-- Round -->
<a class="btn btn--primary btn-icon btn-icon--round btn-icon--lg" href="tel:+15555550123" aria-label="Call (555) 555-0123">
  <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
</a>
```

### CSS

```css
/* Fixed square box; one custom property sets the size */
.btn-icon {
  --btn-icon-size: 2.75rem;
  flex: none; width: var(--btn-icon-size); height: var(--btn-icon-size);
  min-height: 0; padding: 0;
}
.btn-icon--sm { --btn-icon-size: 2rem; }
.btn-icon--lg { --btn-icon-size: 3.25rem; }
.btn-icon--lg svg { width: 1.5rem; height: 1.5rem; }
.btn-icon--round { border-radius: var(--radius-full); }
```

### Notes

- Name the action, not the picture: "Close" or "Edit address", not "X" or "Pencil". For links, include the destination ("Call (555) 555-0123").
- No tooltip by design. If an icon needs explaining, use pattern 3 with a visible label instead.
- Sizes are 2rem, 2.75rem and 3.25rem. The 2rem size passes the 24px target minimum but suits dense UI only.
- Dev-only check (keep out of production CSS): `.btn-icon:not([aria-label], [aria-labelledby]) { outline: 2px dashed var(--danger); }` flags icon buttons with no accessible name.

## 3. Buttons with icons

Builds on 1. Base button. A text label with a leading or trailing icon. Arrow icons nudge in the direction they point on hover and keyboard focus.

### HTML

```html
<!-- Leading icon -->
<a class="btn btn--primary btn-with-icon" href="tel:+15555550123">
  <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
  Call (555) 555-0123
</a>
<a class="btn btn--secondary btn-with-icon" href="price-list.pdf" download>
  <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>
  Price list (PDF, 120 KB)
</a>

<!-- Trailing arrow nudges forward; a leading back arrow nudges back -->
<a class="btn btn--outline btn-with-icon" href="https://example.com/services">
  See all services
  <svg class="btn-with-icon__arrow" aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>
</a>
<a class="btn btn--ghost btn-with-icon" href="https://example.com/projects">
  <svg class="btn-with-icon__arrow btn-with-icon__arrow--back" aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>
  Back to projects
</a>
```

### CSS

```css
/* Direction multiplier: arrows mirror and nudge the other way in RTL */
.btn-with-icon { --btn-with-icon-dir: 1; }
.btn-with-icon:dir(rtl) { --btn-with-icon-dir: -1; }

/* Arrow nudge. A transition, so the motion tokens make it instant under reduced motion. */
.btn-with-icon__arrow {
  --btn-with-icon-nudge: var(--space-xs);
  scale: var(--btn-with-icon-dir) 1;
  transition: translate var(--transition-fast);
}
.btn-with-icon__arrow--back { --btn-with-icon-nudge: calc(var(--space-xs) * -1); }
.btn-with-icon:focus-visible .btn-with-icon__arrow {
  translate: calc(var(--btn-with-icon-nudge) * var(--btn-with-icon-dir)) 0;
}
@media (hover: hover) {
  .btn-with-icon:hover .btn-with-icon__arrow {
    translate: calc(var(--btn-with-icon-nudge) * var(--btn-with-icon-dir)) 0;
  }
}
```

### Notes

- Icons are decorative (`aria-hidden`), so the text alone is the accessible name.
- For downloads, put the file type and size in the label.
- `:dir()` is in Chrome 120, Safari 16.4 and Firefox. Older browsers keep LTR arrows.
- Hover nudges only on devices that can hover, so the arrow doesn't stay shifted after a tap.

## 4. Loading button

Builds on 1. Base button. While a request runs, the label swaps to a spinner and "Sending…" at the same width. `aria-busy` and `aria-disabled` keep the button focusable but inert. A `role="status"` line reports progress and the result.

### HTML

```html
<button class="btn btn--primary btn-loading" type="button" data-status="quote-status">
  <span class="btn-loading__idle">Request a quote</span>
  <span class="btn-loading__busy">
    <span class="btn-loading__spinner" aria-hidden="true"></span>
    Sending…
  </span>
</button>
<p class="btn-loading__status" id="quote-status" role="status"></p>
```

### CSS

```css
/* Both labels share one grid cell, so the button always fits the wider one: no layout jump */
.btn-loading { display: inline-grid; }
.btn-loading__idle,
.btn-loading__busy {
  grid-area: 1 / 1;
  display: inline-flex; align-items: center; justify-content: center; gap: var(--space-sm);
}

/* visibility (not opacity) also hides the inactive label from screen readers */
.btn-loading__busy { visibility: hidden; }
.btn-loading[aria-busy="true"] { cursor: progress; }
.btn-loading[aria-busy="true"] .btn-loading__idle { visibility: hidden; }
.btn-loading[aria-busy="true"] .btn-loading__busy { visibility: visible; }

/* Spinner: a ring in the label color with one solid arc */
.btn-loading__spinner {
  flex: none; box-sizing: border-box; width: 1em; height: 1em;
  border: 2px solid color-mix(in srgb, currentColor 30%, transparent);
  border-top-color: currentColor; border-radius: var(--radius-full);
  animation: btn-loading-spin 0.8s linear infinite;
}
@keyframes btn-loading-spin { to { rotate: 1turn; } }
@media (prefers-reduced-motion: reduce) {
  .btn-loading__spinner { animation: none; } /* static ring; "Sending…" carries the state */
}

/* Status line reserves its height, so messages don't push content down */
.btn-loading__status {
  min-height: 1.5em; margin: var(--space-sm) 0 0;
  color: var(--text-main); font-size: 0.875rem; line-height: 1.5;
}
```

### JS

```js
// Demo: fakes a 2s request. Replace wait() with your fetch() call.
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

document.querySelectorAll('.btn-loading').forEach((btn) => {
  const status = document.getElementById(btn.dataset.status);
  const say = (text) => { if (status) status.textContent = text; };

  btn.addEventListener('click', async () => {
    if (btn.getAttribute('aria-busy') === 'true') return; // ignore repeat clicks
    // aria-disabled (not disabled) keeps keyboard focus on the button
    btn.setAttribute('aria-busy', 'true');
    btn.setAttribute('aria-disabled', 'true');
    say('Sending your request…');
    try {
      await wait(2000);
      say('Request sent. We’ll call you within one business day.');
    } catch {
      say('Something went wrong. Please try again.');
    } finally {
      btn.removeAttribute('aria-busy');
      btn.removeAttribute('aria-disabled');
    }
  });
});
```

### Notes

- `disabled` would drop focus to the page while the request runs; `aria-disabled` plus the busy guard keeps focus and blocks repeat clicks.
- In a form, run the same logic in the `submit` handler and return early while `aria-busy="true"`.
- Keep the `role="status"` element in the page from load, empty, so the first message is announced.
- Under reduced motion the spinner stops. If a request can take longer than about 5s, show progress text rather than an endless spinner.

## 5. Toggle button

Builds on 1. Base button. An on/off button using `aria-pressed`, such as "Save to favorites". Pressed adds a tint and fills the icon, so the state doesn't rely on color.

### HTML

```html
<button class="btn btn--outline btn-toggle" type="button" aria-pressed="false">
  <svg class="btn-toggle__icon" aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6 4 4 0 0 1 7 2.6c0 5.6-7 10-7 10Z"/></svg>
  Save to favorites
</button>
```

### CSS

```css
/* Pressed: tinted fill plus a solid icon (a shape change, not only a color change) */
.btn-toggle[aria-pressed="true"] {
  --btn-bg: color-mix(in srgb, var(--primary) 10%, var(--surface-light));
  --btn-bg-hover: color-mix(in srgb, var(--primary) 18%, var(--surface-light));
  --btn-border: var(--primary);
  --btn-fg: var(--primary-hover);
}
.btn-toggle__icon { transition: fill var(--transition-fast); }
.btn-toggle[aria-pressed="true"] .btn-toggle__icon { fill: currentColor; }
```

### JS

```js
// Flip aria-pressed. CSS styles from the attribute, so state and look can't drift apart.
document.addEventListener('click', (event) => {
  const btn = event.target.closest('.btn-toggle');
  if (!btn) return;
  const pressed = btn.getAttribute('aria-pressed') !== 'true';
  btn.setAttribute('aria-pressed', String(pressed));
  // Hook for saving: listen for this on the button or any ancestor
  btn.dispatchEvent(new CustomEvent('btn-toggle:change', { bubbles: true, detail: { pressed } }));
});
```

### Notes

- Keep the label the same in both states; screen readers announce "Save to favorites, toggle button, pressed". If you'd rather change the text to "Saved", drop `aria-pressed`.
- The outline-to-solid icon is the cue that doesn't depend on color. Keep an icon on every toggle.
- Persist the state from the `btn-toggle:change` event. If it must work without JS, render it as a submit button in a small `<form method="post">`.

## 6. Segmented control

Radio buttons in a `fieldset`, drawn as a joined row of buttons. No JS: Tab moves into the group and arrow keys choose. Equal-width segments fill the row on phones and size to their content from 768px. Place inside your page container.

### HTML

```html
<fieldset class="btn-segmented">
  <legend class="btn-segmented__legend">Visit frequency</legend>
  <div class="btn-segmented__options">
    <label class="btn-segmented__option">
      <input class="btn-segmented__input" type="radio" name="frequency" value="once" checked>
      <span class="btn-segmented__text">One-time</span>
    </label>
    <label class="btn-segmented__option">
      <input class="btn-segmented__input" type="radio" name="frequency" value="monthly">
      <span class="btn-segmented__text">Monthly</span>
    </label>
    <label class="btn-segmented__option">
      <input class="btn-segmented__input" type="radio" name="frequency" value="quarterly">
      <span class="btn-segmented__text">Quarterly</span>
    </label>
  </div>
</fieldset>
```

### CSS

```css
/* Fieldset reset. min-width: 0 stops the fieldset's min-content width overflowing at 320px. */
.btn-segmented {
  --btn-segmented-r: calc(var(--radius-md) - 1px); /* inner radius inside the 1px border */
  min-width: 0; margin: 0; padding: 0; border: 0;
}
.btn-segmented__legend { margin-bottom: var(--space-sm); padding: 0; color: var(--text-main); font-weight: 600; }

/* Joined row: one outer border, dividers between segments, equal-width columns */
.btn-segmented__options {
  display: grid; grid-auto-flow: column; grid-auto-columns: minmax(0, 1fr);
  border: 1px solid var(--text-muted); border-radius: var(--radius-md); background: var(--surface-light);
}
.btn-segmented__option { position: relative; display: flex; }
.btn-segmented__option + .btn-segmented__option { border-inline-start: 1px solid var(--text-muted); }

/* The real radio stays focusable and announced; it's only visually hidden */
.btn-segmented__input {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
.btn-segmented__text {
  flex: 1; display: flex; align-items: center; justify-content: center;
  min-height: 2.75rem; padding: var(--space-xs) var(--space-sm);
  color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-align: center;
  overflow-wrap: anywhere; cursor: pointer;
  transition: background-color var(--transition-fast), color var(--transition-fast);
}
.btn-segmented__option:first-child .btn-segmented__text {
  border-start-start-radius: var(--btn-segmented-r); border-end-start-radius: var(--btn-segmented-r);
}
.btn-segmented__option:last-child .btn-segmented__text {
  border-start-end-radius: var(--btn-segmented-r); border-end-end-radius: var(--btn-segmented-r);
}

/* States: solid fill when checked, focus ring raised above the dividers */
.btn-segmented__input:checked + .btn-segmented__text { background: var(--primary); color: var(--text-inverse); }
.btn-segmented__input:focus-visible + .btn-segmented__text {
  position: relative; z-index: 1; outline: 2px solid transparent; box-shadow: var(--focus-ring);
}
@media (hover: hover) {
  .btn-segmented__input:not(:checked) + .btn-segmented__text:hover { background: var(--surface-muted); }
}

/* From 768px: hug the content; 1fr columns still match the widest label */
@media (min-width: 768px) {
  .btn-segmented__options { display: inline-grid; }
}
```

### Notes

- Native radio keyboard support: Tab lands on the checked option, arrow keys move and select, and the `legend` names the group.
- The input is clipped, not `display: none`, so it stays focusable and announced. The whole label is the 2.75rem-tall click target.
- Use it for 2–4 short options. For more options use a `<select>`, and for switching content panels use tabs.
- Submit it like any radio group (`name="frequency"`). Read the value with `form.elements.frequency.value`.

## 7. Button group

Builds on 1. Base button. Related buttons attached into one control, sharing borders, with only the outer corners rounded. `--stack` makes a full-width column on phones and an attached row from 768px.

### HTML

```html
<!-- Full-width column on phones, attached row from 768px -->
<div class="btn-group btn-group--stack" role="group" aria-label="Contact us">
  <a class="btn btn--outline" href="tel:+15555550123">Call us</a>
  <a class="btn btn--outline" href="sms:+15555550123">Text us</a>
  <a class="btn btn--outline" href="mailto:hello@example.com">Email us</a>
</div>

<!-- Always a row: keep labels short -->
<div class="btn-group" role="group" aria-label="Review pages">
  <a class="btn btn--outline btn--sm" href="https://example.com/reviews?page=1">Previous</a>
  <a class="btn btn--outline btn--sm" href="https://example.com/reviews?page=3">Next</a>
</div>
```

### CSS

```css
/* Attached row: inner corners square, neighbours overlap so they share one 1px border */
.btn-group {
  --btn-group-r: var(--radius-md);
  --btn-group-row-r: var(--btn-group-r); /* corners rounded only in a row */
  --btn-group-col-r: 0;                  /* corners rounded only in a column */
  display: inline-flex; max-width: 100%; vertical-align: middle;
}
.btn-group > .btn { flex: 1 1 auto; border-radius: 0; }
.btn-group > .btn + .btn { margin-inline-start: -1px; }
.btn-group > .btn:first-child {
  border-start-start-radius: var(--btn-group-r);
  border-end-start-radius: var(--btn-group-row-r);
  border-start-end-radius: var(--btn-group-col-r);
}
.btn-group > .btn:last-child {
  border-end-end-radius: var(--btn-group-r);
  border-start-end-radius: var(--btn-group-row-r);
  border-end-start-radius: var(--btn-group-col-r);
}

/* Lift the hovered or focused button so its border and ring sit above its neighbours */
.btn-group > .btn:is(:hover, :focus-visible) { position: relative; z-index: 1; }

/* Stack: full-width column on phones, attached row from 768px */
.btn-group--stack {
  --btn-group-row-r: 0; --btn-group-col-r: var(--btn-group-r);
  display: flex; flex-direction: column;
}
.btn-group--stack > .btn + .btn { margin-inline-start: 0; margin-block-start: -1px; }
@media (min-width: 768px) {
  .btn-group--stack {
    --btn-group-row-r: var(--btn-group-r); --btn-group-col-r: 0;
    display: inline-flex; flex-direction: row;
  }
  .btn-group--stack > .btn + .btn { margin-inline-start: -1px; margin-block-start: 0; }
}
```

### Notes

- `role="group"` plus `aria-label` names the set; each button keeps its own label.
- Built for `--outline` buttons, whose borders overlap by 1px. Filled variants need a divider: `.btn-group > .btn + .btn { border-inline-start-color: var(--text-inverse); }`.
- For one-of-many choices use pattern 6. For independent on/off buttons, put pattern 5 toggles inside the group.
- A plain row doesn't wrap. Use `--stack` whenever the labels might not fit at 320px.

## 8. Split button

Builds on 1. Base button. A main action plus a chevron disclosure button (`aria-expanded`/`aria-controls`) that opens a list of more actions. The options are a plain list in Tab order, not `role="menu"`. Escape or an outside click closes the list and returns focus.

### HTML

```html
<div class="btn-split">
  <a class="btn btn--primary btn-split__main" href="https://example.com/book">Book a visit</a>
  <!-- Hidden until JS runs; without JS the list below shows as plain links -->
  <button class="btn btn--primary btn-split__toggle" type="button" aria-expanded="false"
          aria-controls="book-options" aria-label="More booking options" hidden>
    <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></svg>
  </button>
  <ul class="btn-split__list" id="book-options" role="list">
    <li><a class="btn-split__item" href="https://example.com/book?type=estimate">Free estimate</a></li>
    <li><a class="btn-split__item" href="https://example.com/book?type=emergency">Emergency repair (24/7)</a></li>
    <li><a class="btn-split__item" href="tel:+15555550123">Call (555) 555-0123</a></li>
  </ul>
</div>
```

### CSS

```css
/* Main action + chevron read as one control. Corners join only once JS shows the toggle. */
.btn-split { position: relative; display: inline-flex; flex-wrap: wrap; max-width: 100%; vertical-align: middle; }
.btn-split__main { flex: 1 1 auto; }
.btn-split--ready .btn-split__main { border-start-end-radius: 0; border-end-end-radius: 0; }
.btn-split__toggle {
  flex: none; min-width: 2.75rem; padding-inline: var(--space-sm); margin-inline-start: -1px;
  border-start-start-radius: 0; border-end-start-radius: 0;
  border-inline-start-color: color-mix(in srgb, currentColor 35%, transparent); /* divider */
}
.btn-split > .btn:focus-visible { position: relative; z-index: 1; }
.btn-split__toggle svg { transition: rotate var(--transition-smooth); }
.btn-split__toggle[aria-expanded="true"] svg { rotate: 180deg; }

/* No JS: a plain panel below the button. With JS: a dropdown on the popover layer (70). */
.btn-split__list {
  flex-basis: 100%; box-sizing: border-box; margin: var(--space-xs) 0 0; padding: var(--space-xs);
  list-style: none; background: var(--surface-light);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
}
.btn-split--ready .btn-split__list {
  position: absolute; z-index: 70; top: 100%; inset-inline-start: 0;
  width: max-content; min-width: 100%; max-width: min(20rem, 100vw - 2 * var(--gutter));
  box-shadow: var(--shadow-lg);
}

/* Options: full-width rows, 2.75rem tall; works for <a> and <button> */
.btn-split__item {
  display: flex; align-items: center; box-sizing: border-box; width: 100%; min-height: 2.75rem;
  padding: var(--space-sm) var(--space-md); border: 0; border-radius: var(--radius-sm);
  background: none; color: var(--text-main); font: inherit; text-align: start;
  text-decoration: none; cursor: pointer;
}
.btn-split__item:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
@media (hover: hover) {
  .btn-split__item:hover { background: var(--surface-muted); }
}
```

### JS

```js
// Disclosure: the toggle shows/hides the list; Escape or an outside click closes it
document.querySelectorAll('.btn-split').forEach((root) => {
  const toggle = root.querySelector('.btn-split__toggle');
  const list = root.querySelector('.btn-split__list');
  const setOpen = (open, refocus = false) => {
    toggle.setAttribute('aria-expanded', String(open));
    list.hidden = !open;
    if (refocus) toggle.focus();
  };
  // Enhance: show the toggle, collapse the list into a dropdown
  root.classList.add('btn-split--ready');
  toggle.hidden = false;
  setOpen(false);
  toggle.addEventListener('click', () => setOpen(list.hidden));
  list.addEventListener('click', () => setOpen(false, true));
  root.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !list.hidden) setOpen(false, true);
  });
  // Tabbing away closes quietly; an outside click refocuses the toggle unless focus moved elsewhere
  root.addEventListener('focusout', (event) => {
    if (event.relatedTarget && !root.contains(event.relatedTarget)) setOpen(false);
  });
  document.addEventListener('click', (event) => {
    if (list.hidden || root.contains(event.target)) return;
    const active = document.activeElement;
    setOpen(false, !active || active === document.body || root.contains(active));
  });
});
```

### Notes

- Disclosure, not `role="menu"`: options are ordinary links or buttons in Tab order, so screen readers don't expect menu arrow-key behavior.
- Focus stays on the toggle when the list opens. The toggle's `aria-label` says what it reveals, and the chevron is decorative.
- The list aligns to the button's start edge. If the split button sits at the right edge of the page, add `inset-inline: auto 0` to `.btn-split--ready .btn-split__list`.
- Without JS the toggle stays hidden and the options show as a list under the main action.

## 9. Floating action button

Builds on 1. Base button. A fixed bottom-right button (z-index 5) that opens a speed dial of labelled contact actions as a disclosure. `env(safe-area-inset-bottom)` keeps it clear of the iOS home indicator. Place it once, at the end of `<body>`.

### HTML

```html
<aside class="btn-fab" aria-label="Quick contact">
  <!-- Hidden until JS runs; without JS the actions stay visible -->
  <button class="btn btn--primary btn-fab__toggle" type="button" aria-expanded="false"
          aria-controls="fab-actions" aria-label="Contact options" hidden>
    <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg>
  </button>
  <ul class="btn-fab__actions" id="fab-actions" role="list">
    <li>
      <a class="btn btn-fab__action" href="tel:+15555550123">
        <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2Z"/></svg>
        Call (555) 555-0123
      </a>
    </li>
    <li>
      <a class="btn btn-fab__action" href="sms:+15555550123">
        <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4V5Z"/></svg>
        Text us
      </a>
    </li>
    <li>
      <a class="btn btn-fab__action" href="mailto:hello@example.com">
        <svg aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M3 6h18v12H3zM3 7l9 6 9-6"/></svg>
        Email us
      </a>
    </li>
  </ul>
</aside>
```

### CSS

```css
/* Fixed corner column, clear of the iOS home indicator. --btn-fab-offset lifts it above a bottom bar. */
.btn-fab {
  --btn-fab-offset: 0px;
  position: fixed; z-index: 5;
  right: calc(var(--gutter) + env(safe-area-inset-right, 0px));
  bottom: calc(var(--gutter) + var(--btn-fab-offset) + env(safe-area-inset-bottom, 0px));
  display: flex; flex-direction: column-reverse; align-items: flex-end; gap: var(--space-sm);
}
/* Keep focused content scrolled clear of the button (WCAG 2.4.11) */
html:has(.btn-fab) { scroll-padding-bottom: calc(3.5rem + var(--space-2xl)); }

/* Round toggle; the plus turns into an × when open */
.btn-fab__toggle {
  width: 3.5rem; height: 3.5rem; padding: 0;
  border-radius: var(--radius-full); box-shadow: var(--shadow-lg);
}
.btn-fab__toggle:focus-visible { box-shadow: var(--shadow-lg), var(--focus-ring); }
.btn-fab__toggle svg { width: 1.5rem; height: 1.5rem; transition: rotate var(--transition-smooth); }
.btn-fab__toggle[aria-expanded="true"] svg { rotate: 45deg; }

/* Labelled pills stacked above the toggle; DOM order keeps them after it for Tab */
.btn-fab__actions {
  display: flex; flex-direction: column-reverse; align-items: flex-end; gap: var(--space-sm);
  margin: 0; padding: 0; list-style: none;
}
.btn-fab__actions[hidden] { display: none; }
.btn-fab__action {
  border-radius: var(--radius-full); box-shadow: var(--shadow-md);
  transition: background-color var(--transition-fast), box-shadow var(--transition-fast),
    opacity var(--transition-smooth), translate var(--transition-smooth);
}
.btn-fab__action:focus-visible { box-shadow: var(--shadow-md), var(--focus-ring); }

/* Fade and rise in on open where @starting-style is supported */
@starting-style {
  .btn-fab__action { opacity: 0; translate: 0 var(--space-sm); }
}
```

### JS

```js
// Speed dial as a disclosure: the toggle shows the actions; Escape or an outside click closes them
document.querySelectorAll('.btn-fab').forEach((root) => {
  const toggle = root.querySelector('.btn-fab__toggle');
  const actions = root.querySelector('.btn-fab__actions');
  const setOpen = (open, refocus = false) => {
    toggle.setAttribute('aria-expanded', String(open));
    actions.hidden = !open;
    if (refocus) toggle.focus();
  };
  // Enhance: show the toggle and collapse the actions
  toggle.hidden = false;
  setOpen(false);
  toggle.addEventListener('click', () => setOpen(actions.hidden));
  actions.addEventListener('click', () => setOpen(false, true));
  root.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && !actions.hidden) setOpen(false, true);
  });
  // Tabbing away closes quietly; an outside click refocuses the toggle unless focus moved elsewhere
  root.addEventListener('focusout', (event) => {
    if (event.relatedTarget && !root.contains(event.relatedTarget)) setOpen(false);
  });
  document.addEventListener('click', (event) => {
    if (actions.hidden || root.contains(event.target)) return;
    const active = document.activeElement;
    setOpen(false, !active || active === document.body || root.contains(active));
  });
});
```

### Notes

- `env(safe-area-inset-*)` is 0 unless the viewport meta includes `viewport-fit=cover`.
- **Above a mobile bottom bar** (such as the sticky call bar in `components/cta-sections.md`), set the offset to the bar's height without its safe-area padding, e.g. `body:has(.action-bar) .btn-fab { --btn-fab-offset: 4rem; }`. Reset it from 768px if the bar hides there.
- Tab moves from the toggle into the actions, which are listed nearest-first. Without JS the toggle stays hidden and the actions show as a fixed stack, so the links still work.
- `@starting-style` (Chrome 117, Safari 17.5, Firefox 129) animates the actions in; other browsers show them instantly. The `:has()` scroll padding is an enhancement.
- z-index 5 keeps it under the sticky header, drawers and modals.

## 10. Copy button

Builds on 1. Base button. Copies a value with the Clipboard API. On success the icon becomes a check and a polite live region says "Copied to clipboard". On failure it explains why and selects the text for manual copying. Place inside your page container.

### HTML

```html
<div class="btn-copy">
  <code class="btn-copy__value">SPRING20</code>
  <!-- Hidden until JS runs; without JS the code is plain selectable text -->
  <button class="btn btn--outline btn-copy__button" type="button" hidden>
    <svg class="btn-copy__icon" aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="M9 9h11v11H9zM5 15H4V4h11v1"/></svg>
    <svg class="btn-copy__check" aria-hidden="true" focusable="false" width="24" height="24" viewBox="0 0 24 24"><path d="m5 12 5 5 9-10"/></svg>
    Copy code
  </button>
  <span class="btn-copy__status" role="status"></span>
</div>
```

### CSS

```css
/* Value and button on one line, wrapping on narrow screens */
.btn-copy { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-sm); }
.btn-copy__value {
  min-width: 0; padding: var(--space-sm) var(--space-md);
  border: 1px dashed var(--text-muted); border-radius: var(--radius-sm);
  background: var(--surface-muted); color: var(--text-main);
  font: 600 1rem/1.5 var(--font-sans); letter-spacing: 0.08em; overflow-wrap: anywhere;
}

/* Copied: check icon, success border and text, so the state isn't color alone */
.btn-copy__check { display: none; }
.btn-copy[data-state="copied"] .btn-copy__icon { display: none; }
.btn-copy[data-state="copied"] .btn-copy__check { display: block; }
.btn-copy[data-state="copied"] .btn-copy__button { --btn-fg: var(--success); --btn-border: var(--success); }

/* Live region text: green on success, red on its own line on failure */
.btn-copy__status { font-size: 0.875rem; font-weight: 600; }
.btn-copy[data-state="copied"] .btn-copy__status { color: var(--success); }
.btn-copy[data-state="error"] .btn-copy__status { flex-basis: 100%; color: var(--danger); }
```

### JS

```js
// Copy the value; show success for 2s, or explain the failure and pre-select the text
document.querySelectorAll('.btn-copy').forEach((root) => {
  const button = root.querySelector('.btn-copy__button');
  const value = root.querySelector('.btn-copy__value');
  const status = root.querySelector('.btn-copy__status');
  let timer;
  button.hidden = false; // the button needs JS; the value is selectable without it

  button.addEventListener('click', async () => {
    clearTimeout(timer);
    status.textContent = '';
    try {
      await navigator.clipboard.writeText(button.dataset.copy ?? value.textContent.trim());
      root.dataset.state = 'copied';
      status.textContent = 'Copied to clipboard';
      timer = setTimeout(() => { delete root.dataset.state; status.textContent = ''; }, 2000);
    } catch {
      // No Clipboard API (http, older browser) or permission denied
      root.dataset.state = 'error';
      status.textContent = 'Couldn’t copy. The text is selected so you can copy it yourself.';
      getSelection().selectAllChildren(value);
    }
  });
});
```

### Notes

- The Clipboard API needs a secure context (https or localhost), and inside an iframe it needs `allow="clipboard-write"`. Any failure lands in `catch`.
- Keep the `role="status"` element in the page from load, empty. The success message clears after 2s; the error stays until the next attempt, so there's no time limit to read it.
- To copy something other than the visible text (a full URL, say), add `data-copy="…"` to the button.
- With several copy buttons on a page, make each label specific: "Copy promo code", "Copy email address".
