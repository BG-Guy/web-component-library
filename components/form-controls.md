# Form Controls

Specialized inputs that share the lead form's look (2.75rem controls, `--text-muted` borders, `--primary` focus): switches, custom checkboxes and radios, option cards, input groups, search, password, file upload and quantity fields. Depends on `tokens/variables.css`. Place inside your page container.

| #  | Pattern                                                                          | JS        |
| -- | -------------------------------------------------------------------------------- | --------- |
| 1  | **Toggle switch**: on/off checkbox with `role="switch"` and a sliding thumb      | none      |
| 2  | **Custom checkbox & radio**: restyled native inputs with check, dot and dash     | ~1 line   |
| 3  | **Option cards**: radio group shown as selectable cards with icon and text       | none      |
| 4  | **Input group**: input with a leading icon or `$` / `/hr` / `https://` addons    | none      |
| 5  | **Search field**: `role="search"` form with a clear button and `/` shortcut      | ~22 lines |
| 6  | **Password field**: show/hide toggle (`aria-pressed`) and Caps Lock warning      | ~18 lines |
| 7  | **File dropzone**: styled native file input, drag highlight, announced file list | ~24 lines |
| 8  | **Quantity stepper**: − / + buttons around a clamped number input                | ~22 lines |

## 1. Toggle switch

A checkbox that reads as on/off. The whole label is a 44px-tall target, and the on state moves the thumb, so it never relies on color alone.

### HTML

```html
<label class="switch">
  <input class="switch__input" type="checkbox" role="switch" name="reminders" checked>
  <span class="switch__label">Text me appointment reminders</span>
</label>
<label class="switch">
  <input class="switch__input" type="checkbox" role="switch" name="newsletter" disabled>
  <span class="switch__label">Monthly newsletter (coming soon)</span>
</label>
```

### CSS

```css
/* Row: the whole label is a 44px-tall hit area; long text wraps beside the track */
.switch {
  display: flex; align-items: center; gap: var(--space-sm);
  width: fit-content; max-width: 100%; min-height: 2.75rem;
  color: var(--text-main); cursor: pointer;
}
.switch:has(.switch__input:disabled) { cursor: not-allowed; }
.switch__input:disabled + .switch__label { color: var(--text-muted); }

/* Track: the native checkbox, restyled */
.switch__input {
  --switch-w: 2.75rem; --switch-thumb: 1.125rem;
  appearance: none; position: relative; flex: none; box-sizing: border-box;
  width: var(--switch-w); height: 1.5rem; margin: 0;
  border: 1px solid var(--text-muted); border-radius: var(--radius-full);
  background: var(--surface-light); cursor: inherit;
  transition: background-color var(--transition-fast), border-color var(--transition-fast), box-shadow var(--transition-fast);
}

/* Thumb: drawn as a thick border (stays visible in forced-colors mode); slides right when on */
.switch__input::before {
  content: ""; position: absolute; top: 50%; left: 0.125rem;
  border: calc(var(--switch-thumb) / 2) solid var(--text-muted); border-radius: var(--radius-full);
  translate: 0 -50%;
  transition: translate var(--transition-smooth), border-color var(--transition-fast);
}
.switch__input:checked { border-color: var(--primary); background: var(--primary); }
.switch__input:checked::before {
  border-color: var(--surface-light);
  translate: calc(var(--switch-w) - var(--switch-thumb) - 0.25rem - 2px) -50%;
}

/* Hover, keyboard focus, disabled */
.switch:hover .switch__input:not(:checked, :disabled, :focus-visible) { border-color: var(--text-main); }
.switch__input:focus-visible { outline: 2px solid transparent; border-color: var(--primary); box-shadow: var(--focus-ring); }
.switch__input:disabled { border-color: var(--border-subtle); background: var(--border-subtle); }
.switch__input:disabled::before { border-color: var(--surface-light); }
```

### Notes

- `role="switch"` makes screen readers say "on/off" instead of "checked". The native `checked` state maps to it, so don't add `aria-checked`. Older screen readers fall back to "checkbox", which is still correct.
- A switch should apply right away, for example by saving on `change`. For a choice that's only sent when the form is submitted, use 2. Custom checkbox & radio.
- Pseudo-elements on `appearance: none` checkboxes work in all current engines. The `:has()` rule only sets the not-allowed cursor.
- RTL: flip the sign of the checked `translate` under `:dir(rtl)`.

## 2. Custom checkbox & radio

Native checkboxes and radios with `appearance: none` and CSS-drawn marks, grouped in a `fieldset`/`legend`. Covers focus, disabled and indeterminate states. Keyboard behavior is native.

### HTML

```html
<fieldset class="choice">
  <legend class="choice__legend">Services needed</legend>
  <label class="choice__item">
    <input class="choice__input" type="checkbox" data-choice-indeterminate> All exterior services
  </label>
  <div class="choice__nested">
    <label class="choice__item"><input class="choice__input" type="checkbox" name="services" value="gutters" checked> Gutter cleaning</label>
    <label class="choice__item"><input class="choice__input" type="checkbox" name="services" value="windows"> Window washing</label>
    <label class="choice__item"><input class="choice__input" type="checkbox" name="services" value="pressure" disabled> Pressure washing (booked until May)</label>
  </div>
</fieldset>

<fieldset class="choice">
  <legend class="choice__legend">Best time to call</legend>
  <label class="choice__item"><input class="choice__input" type="radio" name="call-time" value="morning" checked> Morning</label>
  <label class="choice__item"><input class="choice__input" type="radio" name="call-time" value="afternoon"> Afternoon</label>
  <label class="choice__item"><input class="choice__input" type="radio" name="call-time" value="evening" disabled> Evening (unavailable)</label>
</fieldset>
```

### CSS

```css
/* Group: fieldset reset; legend styled like a form label */
.choice { margin: 0; padding: 0; border: 0; min-width: 0; color: var(--text-main); }
.choice__legend { padding: 0; margin-bottom: var(--space-xs); font-size: 0.9375rem; font-weight: 600; }
.choice__nested { padding-inline-start: var(--space-xl); }

/* Row: the label is a 44px-tall hit area */
.choice__item {
  display: flex; align-items: center; gap: var(--space-sm);
  width: fit-content; max-width: 100%; min-height: 2.75rem; cursor: pointer;
}
.choice__item:has(:disabled) { color: var(--text-muted); cursor: not-allowed; }

/* Box: native input with appearance: none; the mark is a ::before drawn with borders */
.choice__input {
  appearance: none; flex: none; display: grid; place-content: center; box-sizing: border-box;
  width: 1.25rem; height: 1.25rem; margin: 0;
  border: 1px solid var(--text-muted); border-radius: var(--radius-sm);
  background: var(--surface-light); cursor: inherit;
  transition: background-color var(--transition-fast), border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.choice__input[type="radio"] { border-radius: var(--radius-full); }
.choice__input::before { content: ""; scale: 0; transition: scale var(--transition-fast); }
/* Checkmark: a rotated L. Radio dot: a zero-size circle with a thick border. */
.choice__input[type="checkbox"]::before {
  width: 0.3125rem; height: 0.625rem; margin-top: -0.125rem;
  border: solid var(--text-inverse); border-width: 0 2px 2px 0; rotate: 45deg;
}
.choice__input[type="radio"]::before { border: 0.3125rem solid var(--primary); border-radius: var(--radius-full); }

/* States. :where() keeps hover weaker than checked and disabled. */
.choice__item:hover :where(.choice__input) { border-color: var(--text-main); }
.choice__input:focus-visible { outline: 2px solid transparent; border-color: var(--primary); box-shadow: var(--focus-ring); }
.choice__input:checked::before,
.choice__input[type="checkbox"]:indeterminate::before { scale: 1; }
.choice__input[type="checkbox"]:is(:checked, :indeterminate) { border-color: var(--primary); background: var(--primary); }
.choice__input[type="radio"]:checked { border-color: var(--primary); }
/* Indeterminate: the L flattens into a dash (scoped to checkboxes: unselected radio groups match too) */
.choice__input[type="checkbox"]:indeterminate::before { width: 0.625rem; height: 0; margin: 0; border-width: 0 0 2px; rotate: none; }
.choice__input[type]:disabled { border-color: var(--border-subtle); background: var(--surface-muted); }
.choice__input[type]:disabled::before { border-color: var(--text-muted); }
```

### JS

```js
// Demo: indeterminate has no HTML attribute, so it can only be set from JS
document.querySelectorAll('[data-choice-indeterminate]').forEach((box) => { box.indeterminate = true; });
```

### Notes

- The `legend` names the group ("Services needed, group"). Space toggles checkboxes; arrow keys move between radios. Both are native.
- `indeterminate` is announced as "mixed" or "half checked". A click clears it, so a real "select all" must recompute `checked`/`indeterminate` from its children on every `change`.
- Marks are drawn with borders, not backgrounds, so they stay visible in Windows forced-colors mode.
- `:has()` only greys the label text of disabled items. Without it the text keeps full color.
- **React:** set `indeterminate` through a ref in an effect. React has no prop for it.

## 3. Option cards

A radio group shown as cards. The whole card is the label; the selected card gets a `--primary` border and a check. One Tab stop, with arrow keys to choose (native radios). Cards wrap from one column to as many as fit.

### HTML

```html
<fieldset class="option-card">
  <legend class="option-card__legend">Choose a cleaning plan</legend>
  <div class="option-card__grid">
    <label class="option-card__item">
      <input class="option-card__input" type="radio" name="plan" value="once"
             aria-labelledby="plan-once" aria-describedby="plan-once-desc">
      <svg class="option-card__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
        <rect x="3" y="5" width="18" height="16" rx="2" /><path d="M3 10h18M8 3v4M16 3v4" />
      </svg>
      <span class="option-card__title" id="plan-once">One-time visit</span>
      <span class="option-card__desc" id="plan-once-desc">A single deep clean, booked when you need it.</span>
      <span class="option-card__check" aria-hidden="true"></span>
    </label>
    <label class="option-card__item">
      <input class="option-card__input" type="radio" name="plan" value="monthly" checked
             aria-labelledby="plan-monthly" aria-describedby="plan-monthly-desc">
      <svg class="option-card__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
        <path d="m17 2 4 4-4 4M3 11V9a3 3 0 0 1 3-3h15M7 22l-4-4 4-4M21 13v2a3 3 0 0 1-3 3H3" />
      </svg>
      <span class="option-card__title" id="plan-monthly">Monthly plan</span>
      <span class="option-card__desc" id="plan-monthly-desc">Same crew every month, 10% off each visit.</span>
      <span class="option-card__check" aria-hidden="true"></span>
    </label>
    <label class="option-card__item">
      <input class="option-card__input" type="radio" name="plan" value="seasonal"
             aria-labelledby="plan-seasonal" aria-describedby="plan-seasonal-desc">
      <svg class="option-card__icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
        <circle cx="12" cy="12" r="4" /><path d="M12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5" />
      </svg>
      <span class="option-card__title" id="plan-seasonal">Seasonal</span>
      <span class="option-card__desc" id="plan-seasonal-desc">Four visits a year, timed to each season.</span>
      <span class="option-card__check" aria-hidden="true"></span>
    </label>
  </div>
</fieldset>
```

### CSS

```css
/* Group: fieldset reset; legend styled like a form label */
.option-card { margin: 0; padding: 0; border: 0; min-width: 0; color: var(--text-main); }
.option-card__legend { padding: 0; margin-bottom: var(--space-sm); font-size: 0.9375rem; font-weight: 600; }

/* Grid: one column on phones, then as many 14rem cards as fit */
.option-card__grid {
  display: grid; gap: var(--space-md);
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 14rem), 1fr));
}

/* Card: two local shadows so the selected edge and the focus ring can stack */
.option-card__item {
  --option-card-sel: 0 0 transparent; --option-card-focus: 0 0 transparent;
  position: relative; display: grid; gap: var(--space-xs); align-content: start;
  padding: var(--space-md); padding-inline-end: var(--space-2xl);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-light); cursor: pointer;
  box-shadow: var(--option-card-sel), var(--option-card-focus);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.option-card__item:hover { border-color: var(--text-muted); }

/* Native radio stretched invisibly over the card: click, touch and arrow keys stay native */
.option-card__input { position: absolute; inset: 0; width: 100%; height: 100%; margin: 0; opacity: 0; cursor: pointer; }
.option-card__icon {
  width: 1.5rem; height: 1.5rem; margin-bottom: var(--space-xs); color: var(--primary);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.option-card__title { font-weight: 600; }
.option-card__desc { font-size: 0.875rem; color: var(--text-muted); }

/* Check indicator: empty circle, filled with a border-drawn check when selected (no :has needed) */
.option-card__check {
  position: absolute; inset-block-start: var(--space-md); inset-inline-end: var(--space-md);
  display: grid; place-content: center; box-sizing: border-box; width: 1.25rem; height: 1.25rem;
  border: 1px solid var(--text-muted); border-radius: var(--radius-full);
  background: var(--surface-light); pointer-events: none;
  transition: background-color var(--transition-fast), border-color var(--transition-fast);
}
.option-card__check::before {
  content: ""; width: 0.25rem; height: 0.5rem; margin-top: -0.125rem;
  border: solid var(--text-inverse); border-width: 0 2px 2px 0; rotate: 45deg; scale: 0;
  transition: scale var(--transition-fast);
}
.option-card__input:checked ~ .option-card__check { border-color: var(--primary); background: var(--primary); }
.option-card__input:checked ~ .option-card__check::before { scale: 1; }

/* Selected border and card-level focus ring */
.option-card__item:has(.option-card__input:checked) { border-color: var(--primary); --option-card-sel: inset 0 0 0 1px var(--primary); }
.option-card__item:has(.option-card__input:focus-visible) { outline: 2px solid transparent; --option-card-focus: var(--focus-ring); }
@supports not selector(:has(*)) {
  .option-card__input:focus-visible ~ .option-card__check { box-shadow: var(--focus-ring); }
}
```

### Notes

- The radio's name comes from the title (`aria-labelledby`) and its details from the description (`aria-describedby`), so screen readers don't read the whole card as one long name. Keep the IDs unique on the page.
- The radio covers the card at `opacity: 0`, so touch screen-reader exploration finds it anywhere on the card.
- `:has()` (all current browsers) adds the selected border and the card-level focus ring. Without it, the check indicator still shows selection and focus.
- To let people pick several, change `type="radio"` to `checkbox`. The CSS stays the same; the keyboard becomes Tab and Space.

## 4. Input group

A text input with a leading icon or fixed prefix/suffix text. The wrapper draws the border, so the focus ring wraps the whole group. Addons are hidden from screen readers, so the label or hint must carry their meaning.

### HTML

```html
<!-- Leading icon -->
<div class="input-group">
  <label class="input-group__label" for="ig-email">Email</label>
  <div class="input-group__control">
    <svg class="input-group__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
      <rect x="3" y="5" width="18" height="14" rx="2" /><path d="m3 7 9 6 9-6" />
    </svg>
    <input class="input-group__input" id="ig-email" name="email" type="email" autocomplete="email" placeholder="you@example.com">
  </div>
</div>

<!-- Prefix + suffix: the visually hidden label text says what "$" and "/hr" mean -->
<div class="input-group">
  <label class="input-group__label" for="ig-rate">Hourly rate <span class="input-group__sr">in US dollars per hour</span></label>
  <div class="input-group__control">
    <span class="input-group__addon" aria-hidden="true">$</span>
    <input class="input-group__input" id="ig-rate" name="rate" type="text" inputmode="decimal">
    <span class="input-group__addon" aria-hidden="true">/hr</span>
  </div>
</div>

<!-- Prefix explained by a visible hint -->
<div class="input-group">
  <label class="input-group__label" for="ig-site">Website</label>
  <div class="input-group__control">
    <span class="input-group__addon" aria-hidden="true">https://</span>
    <input class="input-group__input" id="ig-site" name="website" type="text" inputmode="url"
           autocapitalize="none" spellcheck="false" aria-describedby="ig-site-hint">
  </div>
  <p class="input-group__hint" id="ig-site-hint">Domain only, like example.com. We add https:// for you.</p>
</div>
```

### CSS

```css
/* Field: label, box, optional hint */
.input-group { display: grid; gap: var(--space-xs); color: var(--text-main); }
.input-group__label { font-size: 0.9375rem; font-weight: 600; }
.input-group__hint { margin: 0; font-size: 0.875rem; color: var(--text-muted); }
.input-group__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}

/* Box: the wrapper owns border, hover and focus, so the ring wraps icon, addons and input */
.input-group__control {
  display: flex; box-sizing: border-box; min-height: 2.75rem; overflow: hidden;
  border: 1px solid var(--text-muted); border-radius: var(--radius-md); background: var(--surface-light);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.input-group__control:hover { border-color: var(--text-main); }
.input-group__control:focus-within { outline: 2px solid transparent; border-color: var(--primary); box-shadow: var(--focus-ring); }

/* Input: borderless inside the box; the wrapper shows its focus */
.input-group__input {
  flex: 1; min-width: 0; box-sizing: border-box; margin: 0;
  padding: var(--space-sm) var(--space-md); border: 0;
  background: transparent; color: inherit; font: inherit;
}
.input-group__input:focus { outline: none; }
.input-group__input::placeholder { color: var(--text-muted); opacity: 1; }

/* Leading icon sits inside the box; addons get a muted panel and a divider */
.input-group__icon {
  flex: none; align-self: center; width: 1.25rem; height: 1.25rem;
  margin-inline-start: var(--space-md); color: var(--text-muted);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.input-group__icon + .input-group__input { padding-inline-start: var(--space-sm); }
.input-group__addon {
  display: flex; align-items: center; flex: none; padding-inline: var(--space-md);
  background: var(--surface-muted); color: var(--text-muted); white-space: nowrap;
}
.input-group__addon:first-child { border-inline-end: 1px solid var(--border-subtle); }
.input-group__addon:last-child { border-inline-start: 1px solid var(--border-subtle); }

/* Error: set aria-invalid="true" on the input */
.input-group__control:has([aria-invalid="true"]) { border-color: var(--danger); }
.input-group__control:has([aria-invalid="true"]):focus-within {
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--danger) 35%, transparent);
}
```

### Notes

- Addons are `aria-hidden`, because "$" and "/hr" read badly ("slash h r"). Put their meaning in the label (visually hidden text) or in a hint linked with `aria-describedby`.
- Clicking an addon doesn't focus the input. That's harmless because the input fills the rest of the box.
- `:focus-within` keeps the ring on the group in every browser. The error rules use `:has()` and `color-mix()`; without them the error message text still shows the error.
- **Tailwind:** put `focus-within:` utilities on the wrapper and `outline-none` on the input.

## 5. Search field

A `role="search"` form with a clear button that appears only when there's text, and a `/` shortcut that jumps to the field. Without JS it's a plain search input with the browser's own clear button.

### HTML

```html
<form class="search-field" role="search" action="/search">
  <label class="search-field__sr" for="site-search">Search services</label>
  <div class="search-field__box">
    <svg class="search-field__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
      <circle cx="11" cy="11" r="7" /><path d="m20 20-3.5-3.5" />
    </svg>
    <input class="search-field__input" id="site-search" type="search" name="q"
           placeholder="Search services" aria-keyshortcuts="/" autocomplete="off">
    <button class="search-field__clear" type="button" aria-label="Clear search" hidden>
      <svg class="search-field__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
        <path d="M6 6l12 12M18 6 6 18" />
      </svg>
    </button>
    <kbd class="search-field__kbd" aria-hidden="true" hidden>/</kbd>
  </div>
</form>
```

### CSS

```css
/* Box: owns the border, so the ring wraps icon, input and buttons */
.search-field { max-width: 32rem; }
.search-field__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
.search-field__box {
  display: flex; align-items: center; gap: var(--space-xs); box-sizing: border-box;
  min-height: 2.75rem; padding-inline: var(--space-md) var(--space-xs);
  border: 1px solid var(--text-muted); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-muted);
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.search-field__box:hover { border-color: var(--text-main); }
.search-field__box:focus-within { outline: 2px solid transparent; border-color: var(--primary); box-shadow: var(--focus-ring); }
.search-field__icon {
  flex: none; width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round;
}

/* Input: borderless; the browser's own clear (x) is removed only once JS supplies one */
.search-field__input {
  flex: 1; min-width: 0; min-height: 2.5rem; margin: 0; padding: 0 var(--space-xs);
  border: 0; appearance: none; background: transparent; color: var(--text-main); font: inherit;
}
.search-field__input:focus { outline: none; }
.search-field__input::placeholder { color: var(--text-muted); opacity: 1; }
.search-field--js .search-field__input::-webkit-search-cancel-button { -webkit-appearance: none; display: none; }

/* Clear button: 40px target with its own focus ring */
.search-field__clear {
  display: grid; place-items: center; flex: none; width: 2.5rem; height: 2.5rem; padding: 0;
  border: 0; border-radius: var(--radius-sm); background: transparent; color: inherit; cursor: pointer;
  transition: color var(--transition-fast), background-color var(--transition-fast);
}
.search-field__clear[hidden] { display: none; }
.search-field__clear:hover { background: var(--surface-muted); color: var(--text-main); }
.search-field__clear:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* "/" hint: hidden while focused or filled, on touch-only devices, or when shortcuts are off */
.search-field__kbd {
  flex: none; min-width: 1.5rem; margin-inline-end: var(--space-sm); padding: 0 var(--space-xs);
  border: 1px solid var(--text-muted); border-radius: var(--radius-sm);
  font: 600 0.8125rem/1.5 var(--font-sans); text-align: center;
}
.search-field__input:focus ~ .search-field__kbd,
[data-search-shortcut="off"] .search-field__kbd { display: none; }
@media (hover: none) { .search-field__kbd { display: none; } }
```

### JS

```js
// Clear button and "/" hint for each search field
const searchFields = document.querySelectorAll('.search-field');
searchFields.forEach((form) => {
  const input = form.querySelector('.search-field__input');
  const clear = form.querySelector('.search-field__clear');
  const kbd = form.querySelector('.search-field__kbd');
  const sync = () => { clear.hidden = !input.value; kbd.hidden = Boolean(input.value); };
  input.addEventListener('input', sync);
  clear.addEventListener('click', () => {
    input.value = '';
    input.dispatchEvent(new Event('input', { bubbles: true })); // runs sync() and any live-search listener
    input.focus();
  });
  form.classList.add('search-field--js');
  sync();
});

// "/" focuses the first field, unless the user is typing or turned shortcuts off (WCAG 2.1.4)
document.addEventListener('keydown', (e) => {
  if (e.key !== '/' || e.ctrlKey || e.metaKey || e.altKey || e.isComposing || !searchFields.length) return;
  if (document.documentElement.dataset.searchShortcut === 'off') return;
  if (e.target.isContentEditable || e.target.closest?.('input, textarea, select')) return;
  e.preventDefault();
  searchFields[0].querySelector('.search-field__input').focus();
});
```

### Notes

- `role="search"` makes the form a landmark. The newer `<search>` element does the same, but keep the role for older screen readers.
- The shortcut is announced through `aria-keyshortcuts="/"`. The visible `<kbd>` is `aria-hidden`, so screen readers don't just read "slash".
- `/` is a single-character shortcut, so WCAG 2.1.4 requires a way to turn it off. Set `<html data-search-shortcut="off">`, for example from a settings switch (pattern 1). It's already ignored while typing in any field. With several search fields, `/` focuses the first.
- The label is visually hidden because the icon and placeholder show the field's purpose. In a long form, use a visible label instead. Enter submits the form; add a submit button if your users expect one.

## 6. Password field

A password input with a show/hide toggle (`aria-pressed`) and an optional Caps Lock warning in a polite live region. Shown for sign-in (`current-password`) and sign-up (`new-password`).

### HTML

```html
<!-- Sign in -->
<div class="password-field">
  <label class="password-field__label" for="pw-current">Password</label>
  <div class="password-field__box">
    <input class="password-field__input" id="pw-current" name="password" type="password" autocomplete="current-password" required>
    <button class="password-field__toggle" type="button" aria-label="Show password" aria-pressed="false" aria-controls="pw-current">
      <svg class="password-field__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
        <path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z" /><circle cx="12" cy="12" r="3" />
        <path class="password-field__slash" d="m3 3 18 18" />
      </svg>
    </button>
  </div>
  <p class="password-field__caps" role="status"></p>
</div>

<!-- Sign up: new-password lets password managers suggest a strong one -->
<div class="password-field">
  <label class="password-field__label" for="pw-new">Create a password</label>
  <p class="password-field__hint" id="pw-new-hint">At least 12 characters.</p>
  <div class="password-field__box">
    <input class="password-field__input" id="pw-new" name="new-password" type="password" autocomplete="new-password"
           minlength="12" aria-describedby="pw-new-hint" required>
    <button class="password-field__toggle" type="button" aria-label="Show password" aria-pressed="false" aria-controls="pw-new">
      <svg class="password-field__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false">
        <path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z" /><circle cx="12" cy="12" r="3" />
        <path class="password-field__slash" d="m3 3 18 18" />
      </svg>
    </button>
  </div>
  <p class="password-field__caps" role="status"></p>
</div>
```

### CSS

```css
/* Field: margins instead of gap, so the empty live region takes no space */
.password-field { display: grid; color: var(--text-main); }
.password-field__label { margin-bottom: var(--space-xs); font-size: 0.9375rem; font-weight: 600; }
.password-field__hint { margin: 0 0 var(--space-xs); font-size: 0.875rem; color: var(--text-muted); }

/* Input: same box as the lead form, with room on the right for the toggle */
.password-field__box { position: relative; }
.password-field__input {
  display: block; box-sizing: border-box; width: 100%; min-height: 2.75rem; margin: 0;
  padding: var(--space-sm) var(--space-2xl) var(--space-sm) var(--space-md);
  border: 1px solid var(--text-muted); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-main); font: inherit;
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.password-field__input:hover { border-color: var(--text-main); }
.password-field__input:focus { outline: 2px solid transparent; border-color: var(--primary); box-shadow: var(--focus-ring); }
.password-field__input[aria-invalid="true"] { border-color: var(--danger); }
.password-field__input[aria-invalid="true"]:focus { box-shadow: 0 0 0 3px color-mix(in srgb, var(--danger) 35%, transparent); }
/* JS draws its own toggle, so hide the browser's built-in reveal button */
.password-field--js .password-field__input::-ms-reveal { display: none; }

/* Toggle: 40px icon button inside the input's end edge; needs JS, so hidden until then */
.password-field__toggle {
  position: absolute; top: 50%; inset-inline-end: var(--space-xs); translate: 0 -50%;
  display: none; place-items: center; width: 2.5rem; height: 2.5rem; padding: 0;
  border: 0; border-radius: var(--radius-sm); background: transparent; color: var(--text-muted); cursor: pointer;
  transition: color var(--transition-fast), background-color var(--transition-fast);
}
.password-field--js .password-field__toggle { display: grid; }
.password-field__toggle:hover { color: var(--text-main); }
.password-field__toggle:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.password-field__icon {
  width: 1.25rem; height: 1.25rem;
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
/* Pressed = password visible: tinted button and a slashed eye (not color alone) */
.password-field__toggle[aria-pressed="true"] { background: color-mix(in srgb, var(--primary) 10%, var(--surface-light)); color: var(--primary); }
.password-field__toggle[aria-pressed="false"] .password-field__slash { display: none; }

/* Caps Lock warning */
.password-field__caps { margin: 0; font-size: 0.875rem; font-weight: 600; color: var(--warning); }
.password-field__caps:not(:empty) { margin-top: var(--space-xs); }
```

### JS

```js
// Show/hide toggle and Caps Lock warning for each password field
document.querySelectorAll('.password-field').forEach((field) => {
  const input = field.querySelector('.password-field__input');
  const toggle = field.querySelector('.password-field__toggle');
  const caps = field.querySelector('.password-field__caps');
  const reveal = (on) => {
    input.type = on ? 'text' : 'password';
    toggle.setAttribute('aria-pressed', String(on));
  };
  toggle.addEventListener('click', () => reveal(input.type === 'password'));
  input.form?.addEventListener('submit', () => reveal(false)); // never submit (or save) it as plain text
  field.classList.add('password-field--js'); // shows the toggle
  if (!caps) return;
  // Only touch the live region when the message changes, so it isn't re-announced per key
  const warn = (msg) => { if (caps.textContent !== msg) caps.textContent = msg; };
  ['keydown', 'keyup'].forEach((type) => input.addEventListener(type, (e) => {
    warn(e.getModifierState?.('CapsLock') ? 'Caps Lock is on.' : '');
  }));
  input.addEventListener('blur', () => warn(''));
});
```

### Notes

- The toggle is a toggle button: "Show password, toggle button, pressed / not pressed". The name never changes, so don't also swap it to "Hide password".
- Use `autocomplete="current-password"` for sign-in and `"new-password"` for sign-up or reset, so password managers fill or generate correctly. Never block paste (WCAG 3.3.8).
- The Caps Lock warning only knows the state after the first key press in the field, and most mobile keyboards don't report it. Leave out the `.password-field__caps` element to turn the warning off.
- Without JS the toggle stays hidden and the field is a plain password input. Edge's built-in reveal button is hidden only once JS adds its own.

## 7. File dropzone

A large drop target that's really a native file input inside a visible label, so click, keyboard and drag-and-drop all work. Selected files are listed and announced; files that are too large or the wrong type are flagged.

### HTML

```html
<div class="dropzone" data-max-mb="10">
  <label class="dropzone__area">
    <svg class="dropzone__icon" viewBox="0 0 24 24" width="32" height="32" aria-hidden="true" focusable="false">
      <path d="M12 15V4M7 9l5-5 5 5M4 15v4a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-4" />
    </svg>
    <span class="dropzone__title" id="dz-title">Upload project photos</span>
    <span>Drag files here or <span class="dropzone__browse">browse</span></span>
    <span class="dropzone__hint" id="dz-hint">JPG, PNG or PDF, up to 10 MB each</span>
    <input class="dropzone__input" type="file" name="photos" multiple accept=".jpg,.jpeg,.png,.pdf"
           aria-labelledby="dz-title" aria-describedby="dz-hint">
  </label>
  <!-- Polite live region: screen readers hear the file names after each change -->
  <ul class="dropzone__list" role="list" aria-live="polite"></ul>
</div>
```

### CSS

```css
/* Area: dashed target; hover and focus switch to --primary */
.dropzone { display: grid; gap: var(--space-sm); color: var(--text-main); }
.dropzone__area {
  position: relative; display: grid; justify-items: center; gap: var(--space-xs);
  padding: var(--space-xl) var(--space-md); text-align: center;
  border: 2px dashed var(--text-muted); border-radius: var(--radius-lg);
  background: var(--surface-muted); cursor: pointer;
  transition: border-color var(--transition-fast), background-color var(--transition-fast), box-shadow var(--transition-fast);
}
.dropzone__area:hover { border-color: var(--primary); }
.dropzone__area:focus-within { outline: 2px solid transparent; border-color: var(--primary); box-shadow: var(--focus-ring); }
/* Drag-over: solid border and a lighter surface, not just a color change */
.dropzone__area--over { border-style: solid; border-color: var(--primary); background: var(--surface-light); }

.dropzone__icon {
  width: 2rem; height: 2rem; color: var(--primary);
  fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
}
.dropzone__title { font-weight: 600; }
.dropzone__browse { color: var(--primary); font-weight: 600; text-decoration: underline; }
.dropzone__hint { font-size: 0.875rem; color: var(--text-muted); }

/* Without JS the native input shows its own file names. With JS it covers the area invisibly. */
.dropzone__input { max-width: 100%; margin-top: var(--space-sm); font: inherit; font-size: 0.875rem; }
.dropzone--js .dropzone__input {
  position: absolute; inset: 0; width: 100%; height: 100%; margin: 0; opacity: 0; cursor: pointer;
}

/* Selected files; errors say so in text as well as color */
.dropzone__list { display: grid; gap: var(--space-xs); margin: 0; padding: 0; list-style: none; }
.dropzone__file {
  padding: var(--space-sm) var(--space-md); font-size: 0.875rem; overflow-wrap: anywhere;
  border: 1px solid var(--border-subtle); border-radius: var(--radius-md);
}
.dropzone__file--error { border-color: var(--danger); color: var(--danger); }
```

### JS

```js
// Enhance each dropzone: invisible input over the area, drag highlight, checked file list
document.querySelectorAll('.dropzone').forEach((zone) => {
  const input = zone.querySelector('.dropzone__input');
  const area = zone.querySelector('.dropzone__area');
  const list = zone.querySelector('.dropzone__list');
  const maxBytes = Number(zone.dataset.maxMb || 10) * 1048576;
  const types = input.accept.split(',').map((t) => t.trim().toLowerCase()).filter(Boolean);
  // `accept` filters the picker but not drops, so re-check the extension or MIME type
  const typeOk = (file) => !types.length || types.some((t) => (t.startsWith('.')
    ? file.name.toLowerCase().endsWith(t) : file.type.startsWith(t.replace('*', ''))));
  const over = (on) => () => area.classList.toggle('dropzone__area--over', on);
  ['dragenter', 'dragover'].forEach((type) => input.addEventListener(type, over(true)));
  ['dragleave', 'drop'].forEach((type) => input.addEventListener(type, over(false)));

  // Rebuild the list on every change (picker or drop) and block submit while a file is invalid
  input.addEventListener('change', () => {
    list.replaceChildren(...[...input.files].map((file) => {
      const error = file.size > maxBytes ? 'too large' : typeOk(file) ? '' : 'wrong file type';
      const li = document.createElement('li');
      li.className = error ? 'dropzone__file dropzone__file--error' : 'dropzone__file';
      li.textContent = `${file.name}, ${Math.ceil(file.size / 104857.6) / 10} MB${error ? `: ${error}` : ''}`;
      return li;
    }));
    const hasError = list.querySelector('.dropzone__file--error');
    input.setCustomValidity(hasError ? 'Some files are too large or the wrong type.' : '');
  });
  zone.classList.add('dropzone--js');
});
```

### Notes

- It's a real `<input type="file">`: Tab focuses it, Enter or Space opens the picker, and browsers accept a drop straight onto it, so the script never reads `dataTransfer`. A drop replaces the selection, just like the picker.
- The list is a polite live region, so each change is read out ("deck.jpg, 2.4 MB"), including errors. Always validate type and size again on the server.
- Keep `accept`, `data-max-mb` and the hint text in sync. `accept` takes extensions or MIME types (`image/*` works).
- Use unique `dz-title`/`dz-hint` IDs per instance. Without JS, the native input is visible inside the area and lists its own files.

## 8. Quantity stepper

− / + buttons around a number input. Bounds and step come from `min`/`max`/`step`; the buttons go inactive at the bounds, and typed values are clamped on `change`. Without JS it's a native number input.

### HTML

```html
<div class="qty">
  <label class="qty__label" for="qty-rooms">Rooms to paint</label>
  <div class="qty__control">
    <button class="qty__btn" type="button" aria-label="Decrease rooms" aria-controls="qty-rooms">
      <svg class="qty__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M5 12h14" /></svg>
    </button>
    <input class="qty__input" id="qty-rooms" name="rooms" type="number" inputmode="numeric" min="1" max="10" step="1" value="1">
    <button class="qty__btn" type="button" aria-label="Increase rooms" aria-controls="qty-rooms">
      <svg class="qty__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg>
    </button>
  </div>
  <span class="qty__sr" role="status"></span>
</div>
```

### CSS

```css
/* Field: label above a row of [−] [input] [+] */
.qty { display: grid; gap: var(--space-xs); justify-items: start; color: var(--text-main); }
.qty__label { font-size: 0.9375rem; font-weight: 600; }
.qty__sr {
  position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; border: 0;
}
.qty__control { display: flex; gap: var(--space-xs); }

/* Shared box: 44px tall, same border, radius and focus as the lead form */
.qty__input, .qty__btn {
  box-sizing: border-box; height: 2.75rem; margin: 0;
  border: 1px solid var(--text-muted); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-main); font: inherit;
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast), background-color var(--transition-fast);
}
.qty__input { width: 4.5rem; padding: 0 var(--space-sm); text-align: center; font-variant-numeric: tabular-nums; }
.qty__btn { display: none; place-items: center; width: 2.75rem; padding: 0; cursor: pointer; }
.qty--js .qty__btn { display: grid; }
.qty__icon { width: 1.25rem; height: 1.25rem; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }
.qty__input:hover, .qty__btn:not([aria-disabled="true"]):hover { border-color: var(--text-main); }
.qty__input:focus, .qty__btn:focus-visible { outline: 2px solid transparent; border-color: var(--primary); box-shadow: var(--focus-ring); }

/* At a bound: still focusable, visibly inactive */
.qty__btn[aria-disabled="true"] { border-color: var(--border-subtle); background: var(--surface-muted); color: var(--text-muted); cursor: not-allowed; }

/* With JS, the buttons replace the native spinner; arrow keys still step */
.qty--js .qty__input { -moz-appearance: textfield; appearance: textfield; }
.qty--js .qty__input::-webkit-inner-spin-button,
.qty--js .qty__input::-webkit-outer-spin-button { -webkit-appearance: none; margin: 0; }
```

### JS

```js
// Wire − / + to the number input; bounds and step come from its attributes
document.querySelectorAll('.qty').forEach((qty) => {
  const input = qty.querySelector('.qty__input');
  const [dec, inc] = qty.querySelectorAll('.qty__btn');
  const status = qty.querySelector('[role="status"]');
  const min = Number(input.min || 0);
  const max = Number(input.max || Infinity);
  // aria-disabled (not disabled) keeps focus on a button that reaches a bound
  const sync = () => {
    dec.setAttribute('aria-disabled', String(Number(input.value) <= min));
    inc.setAttribute('aria-disabled', String(Number(input.value) >= max));
  };
  const clamp = () => { input.value = Math.min(max, Math.max(min, Number(input.value))); sync(); };
  [dec, inc].forEach((btn) => btn.addEventListener('click', () => {
    if (btn.getAttribute('aria-disabled') === 'true') return;
    if (btn === inc) input.stepUp(); else input.stepDown();
    input.dispatchEvent(new Event('change', { bubbles: true })); // clamps, syncs and informs listeners
    status.textContent = input.value;
  }));
  input.addEventListener('input', sync);
  input.addEventListener('change', clamp);
  qty.classList.add('qty--js');
  sync();
});
```

### Notes

- The buttons' `aria-label`s name the thing being counted ("Increase rooms"), and the hidden `role="status"` announces the new value after each click.
- At a bound a button gets `aria-disabled="true"` instead of `disabled`. A `disabled` button would drop keyboard focus mid-press; screen readers still report the button as unavailable.
- The input stays editable. ↑/↓ use the native step, and typed values (or an empty field) are clamped to `min`/`max` on `change`. `stepUp()`/`stepDown()` handle the step math, so don't use `step="any"` (they throw on it). `min` defaults to 0.
- Without JS the buttons are hidden and the native number spinner is kept.
