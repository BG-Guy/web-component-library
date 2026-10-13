# Forms

Lead-generation / contact form with inline validation. Depends on `tokens/variables.css`.

- Fields: full name, phone, email, service (select), details (optional).
- Two columns from 768px. Message and submit run full width.
- Validates on submit, on leaving a filled field, and live while the user fixes an error. No libraries.

## HTML

Convention: each validated control has `data-error` (its message) and an error element with id `{control id}-error`, referenced by `aria-describedby`.

```html
<form class="lead-form" action="/contact" method="post" aria-labelledby="lf-title">
  <h2 id="lf-title" class="lead-form__title">Get a free estimate</h2>
  <p class="lead-form__intro">Tell us what you need. We reply within one business day.</p>

  <div class="lead-form__grid">
    <div class="lead-form__field">
      <label for="lf-name">Full name</label>
      <input id="lf-name" name="name" type="text" autocomplete="name" required
             placeholder="Jane Smith" aria-describedby="lf-name-error"
             data-error="Enter your full name.">
      <p id="lf-name-error" class="lead-form__error"></p>
    </div>

    <div class="lead-form__field">
      <label for="lf-phone">Phone</label>
      <input id="lf-phone" name="phone" type="tel" autocomplete="tel" required
             pattern="[0-9\s\(\)\+\-\.]{7,20}" placeholder="(555) 555-0123"
             aria-describedby="lf-phone-error" data-error="Enter a valid phone number.">
      <p id="lf-phone-error" class="lead-form__error"></p>
    </div>

    <div class="lead-form__field">
      <label for="lf-email">Email</label>
      <input id="lf-email" name="email" type="email" autocomplete="email" required
             placeholder="jane@example.com" aria-describedby="lf-email-error"
             data-error="Enter an email address like name@example.com.">
      <p id="lf-email-error" class="lead-form__error"></p>
    </div>

    <div class="lead-form__field">
      <label for="lf-service">Service</label>
      <div class="lead-form__select">
        <select id="lf-service" name="service" required aria-describedby="lf-service-error"
                data-error="Choose a service.">
          <option value="">Select a service…</option>
          <option>Repair</option>
          <option>Installation</option>
          <option>Maintenance</option>
          <option>Inspection / estimate</option>
          <option>Other</option>
        </select>
      </div>
      <p id="lf-service-error" class="lead-form__error"></p>
    </div>

    <div class="lead-form__field lead-form__field--full">
      <label for="lf-message">Project details <span class="lead-form__optional">(optional)</span></label>
      <textarea id="lf-message" name="message" rows="4"
                placeholder="What's going on, and when works for you?"></textarea>
    </div>
  </div>

  <button class="lead-form__submit" type="submit">Request my estimate</button>
  <p class="lead-form__note">No spam. We only use your details to reply to this request.</p>
</form>
```

## CSS

```css
.lead-form, .lead-form * { box-sizing: border-box; }
.lead-form {
  max-width: 40rem; padding: var(--space-lg);
  background: var(--surface-light); color: var(--text-main);
  border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  box-shadow: var(--shadow-md);
}
.lead-form__title { margin: 0; font-size: 1.5rem; line-height: 1.2; }
.lead-form__intro { margin: var(--space-xs) 0 var(--space-lg); color: var(--text-muted); }
.lead-form__grid { display: grid; gap: var(--space-md); }
.lead-form__field { display: grid; gap: var(--space-xs); align-content: start; }
.lead-form label { font-size: 0.9375rem; font-weight: 600; }
.lead-form__optional { font-weight: 400; color: var(--text-muted); }

/* Controls. Border uses --text-muted for 3:1 boundary contrast (WCAG 1.4.11). */
.lead-form__field :is(input, select, textarea) {
  width: 100%; min-height: 2.75rem;
  padding: var(--space-sm) var(--space-md);
  border: 1px solid var(--text-muted); border-radius: var(--radius-md);
  background: var(--surface-light); color: var(--text-main); font: inherit;
  transition: border-color var(--transition-fast), box-shadow var(--transition-fast);
}
.lead-form textarea { min-height: 7rem; resize: vertical; }
.lead-form :is(input, textarea)::placeholder { color: var(--text-muted); opacity: 1; }
.lead-form__field :is(input, select, textarea):hover { border-color: var(--text-main); }
.lead-form__field :is(input, select, textarea):focus {
  outline: 2px solid transparent; border-color: var(--primary); box-shadow: var(--focus-ring);
}

/* Select chevron */
.lead-form__select { position: relative; }
.lead-form__select select { appearance: none; padding-right: var(--space-2xl); cursor: pointer; }
.lead-form__select::after {
  content: ""; position: absolute; right: var(--space-md); top: 50%;
  width: 0.5rem; height: 0.5rem;
  border: solid var(--text-muted); border-width: 0 2px 2px 0;
  transform: translateY(-75%) rotate(45deg); pointer-events: none;
}

/* Error state */
.lead-form [aria-invalid="true"] { border-color: var(--danger); }
.lead-form [aria-invalid="true"]:focus {
  border-color: var(--danger);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--danger) 35%, transparent);
}
.lead-form__error { margin: 0; font-size: 0.875rem; color: var(--danger); }
.lead-form__error:empty { display: none; }

/* Submit */
.lead-form__submit {
  width: 100%; min-height: 3rem; margin-top: var(--space-lg);
  padding: var(--space-sm) var(--space-lg);
  border: 0; border-radius: var(--radius-md);
  background: var(--primary); color: var(--text-inverse);
  font: inherit; font-weight: 600; cursor: pointer;
  transition: background-color var(--transition-fast);
}
.lead-form__submit:hover { background: var(--primary-hover); }
.lead-form__submit:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.lead-form__note { margin: var(--space-sm) 0 0; font-size: 0.875rem; text-align: center; color: var(--text-muted); }

@media (min-width: 768px) {
  .lead-form { padding: var(--space-xl); }
  .lead-form__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .lead-form__field--full { grid-column: 1 / -1; }
}
```

## JS

```js
const form = document.querySelector('.lead-form');
form.noValidate = true; // set by JS so no-JS visitors still get native validation

function check(field) {
  const valid = field.checkValidity();
  field.setAttribute('aria-invalid', !valid);
  document.getElementById(`${field.id}-error`).textContent = valid ? '' : field.dataset.error;
  return valid;
}

form.addEventListener('submit', (e) => {
  const invalid = [...form.querySelectorAll('[data-error]')].filter((f) => !check(f));
  if (invalid.length) { e.preventDefault(); invalid[0].focus(); }
});
form.addEventListener('focusout', (e) => {
  if (e.target.matches('[data-error]') && e.target.value) check(e.target);
});
form.addEventListener('input', (e) => {
  if (e.target.getAttribute('aria-invalid') === 'true') check(e.target);
});
```

## Notes

- Every control has a `<label for>`. Placeholders show examples and never replace labels.
- Screen readers announce `aria-invalid` and the `aria-describedby` message when a field gets focus. On submit, focus moves to the first invalid field.
- Empty fields aren't flagged on blur, only on submit, so tabbing through doesn't trigger errors early.
- The phone `pattern` escapes every symbol so it compiles under the `v` regex flag that browsers now apply to `pattern`.
- Always validate on the server too. For spam, use a server-checked honeypot field before reaching for a CAPTCHA, which costs conversions.
- **fetch submit:** after the invalid check passes, call `e.preventDefault()` and post `new FormData(form)`.
- **React:** keep inputs uncontrolled, set `noValidate` on `<form>`, and attach the same three handlers as `onSubmit`, `onBlur` and `onInput`. React's `onBlur` bubbles like `focusout`.
- **Tailwind (v4):** `aria-[invalid=true]:border-(--danger) placeholder:text-(--text-muted) focus:border-(--primary) focus:shadow-(--focus-ring)`.
