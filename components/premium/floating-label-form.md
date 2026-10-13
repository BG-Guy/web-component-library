# Floating Label Form

A lead form that feels alive. Labels rest inside the fields and glide up as you type. Focus blooms a soft ring, and valid fields earn a springy check. Errors slide open beneath the field, and a failed submit gives each invalid field a short shake. Service type is a row of chips that pop when chosen, the details box grows with its content, and the submit button morphs through a spinner to "Request sent". Depends on `tokens/variables.css`.

**Motion:** floating label (scale + lift) · focus ring bloom · valid check pop (spring) · error slide-open (grid rows) · invalid shake · chip pop · submit morph (label → spinner → success).

## HTML

```html
<div class="float-form-demo">
  <form class="float-form" action="/contact" method="post" aria-labelledby="float-form-title" data-float-form>
    <header class="float-form__head">
      <p class="float-form__eyebrow">Free estimate</p>
      <h2 id="float-form-title" class="float-form__title">Tell us what needs fixing</h2>
      <p class="float-form__lead">We reply within one business day, usually within the hour.</p>
    </header>

    <div class="float-form__grid">
      <div class="float-form__field">
        <input class="float-form__input" id="float-form-name" name="name" type="text" autocomplete="name" placeholder=" " required
               aria-describedby="float-form-name-error" data-error="Please enter your name.">
        <label class="float-form__label" for="float-form-name">Full name</label>
        <span class="float-form__valid" aria-hidden="true"></span>
        <p class="float-form__error" id="float-form-name-error"><span></span></p>
      </div>
      <div class="float-form__field">
        <input class="float-form__input" id="float-form-phone" name="phone" type="tel" autocomplete="tel" placeholder=" " required
               pattern="[0-9\s\(\)\+\-\.]{7,20}" aria-describedby="float-form-phone-error" data-error="Enter a phone number we can reach you on.">
        <label class="float-form__label" for="float-form-phone">Phone</label>
        <span class="float-form__valid" aria-hidden="true"></span>
        <p class="float-form__error" id="float-form-phone-error"><span></span></p>
      </div>
      <div class="float-form__field float-form__field--full">
        <input class="float-form__input" id="float-form-email" name="email" type="email" autocomplete="email" placeholder=" " required
               aria-describedby="float-form-email-error" data-error="Enter an email like name@example.com.">
        <label class="float-form__label" for="float-form-email">Email</label>
        <span class="float-form__valid" aria-hidden="true"></span>
        <p class="float-form__error" id="float-form-email-error"><span></span></p>
      </div>

      <fieldset class="float-form__field float-form__field--full float-form__choices">
        <legend class="float-form__legend">What do you need?</legend>
        <div class="float-form__chips">
          <label class="float-form__chip"><input type="radio" name="service" value="repair" required aria-describedby="float-form-service-error" data-error="Choose the closest match.">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z" /></svg>Repair</label>
          <label class="float-form__chip"><input type="radio" name="service" value="install">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M21 8l-9-5-9 5v8l9 5 9-5V8zM3 8l9 5 9-5M12 13v8" /></svg>Installation</label>
          <label class="float-form__chip"><input type="radio" name="service" value="maintenance">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /></svg>Maintenance</label>
          <label class="float-form__chip"><input type="radio" name="service" value="other">
            <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM8 12h.01M12 12h.01M16 12h.01" /></svg>Something else</label>
        </div>
        <p class="float-form__error" id="float-form-service-error"><span></span></p>
      </fieldset>

      <div class="float-form__field float-form__field--full">
        <textarea class="float-form__input float-form__input--area" id="float-form-details" name="details" rows="3" placeholder=" "></textarea>
        <label class="float-form__label" for="float-form-details">Details (optional)</label>
      </div>
    </div>

    <button class="float-form__submit" type="submit">
      <span class="float-form__submit-label">Request my estimate</span>
      <span class="float-form__spinner" aria-hidden="true"></span>
      <span class="float-form__done" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg>Request sent</span>
    </button>
    <p class="float-form__status" role="status"></p>
  </form>
</div>
```

## CSS

```css
/* Demo backdrop and card */
.float-form-demo {
  padding: clamp(3rem, 8vw, 6rem) var(--gutter);
  background:
    radial-gradient(60% 50% at 10% 0%, color-mix(in srgb, var(--primary) 12%, transparent), transparent 70%),
    radial-gradient(50% 50% at 100% 100%, color-mix(in srgb, var(--primary-2) 12%, transparent), transparent 70%),
    var(--surface-muted);
}
.float-form {
  max-width: 40rem; margin-inline: auto; padding: clamp(1.5rem, 4vw, 2.5rem); border-radius: var(--radius-2xl);
  background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
  box-shadow: var(--shadow-xl), inset 0 0 0 1px var(--border-subtle);
}
.float-form__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.float-form__title { margin: 0.5rem 0 0; font: 600 clamp(1.5rem, 1.2rem + 1.4vw, 2rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.float-form__lead { margin: 0.5rem 0 0; color: var(--text-muted); }
.float-form__grid { display: grid; gap: 1rem; margin-top: 2rem; }
@media (min-width: 640px) {
  .float-form__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .float-form__field--full { grid-column: 1 / -1; }
}

/* Field with a floating label (label sits after the input so :placeholder-shown can drive it) */
.float-form__field { position: relative; min-width: 0; margin: 0; padding: 0; border: 0; }
.float-form__input {
  box-sizing: border-box; width: 100%; height: 3.5rem; padding: 1.5rem 2.75rem 0.5rem 1rem;
  border: 1px solid color-mix(in srgb, var(--text-main) 55%, var(--surface-light)); border-radius: 0.875rem;
  background: var(--surface-light); color: var(--text-main); font: 500 1rem/1.4 var(--font-sans);
  transition: border-color var(--dur-2), box-shadow var(--dur-3) var(--ease-out);
}
.float-form__input::placeholder { color: transparent; }
.float-form__input:hover { border-color: var(--text-muted); }
.float-form__input:focus { outline: 2px solid transparent; border-color: var(--primary); box-shadow: 0 0 0 4px color-mix(in srgb, var(--primary) 16%, transparent); }
.float-form__input--area { height: auto; min-height: 7.5rem; padding-top: 1.75rem; resize: vertical; field-sizing: content; }
.float-form__label {
  position: absolute; left: 1rem; top: 1.0625rem; color: var(--text-muted); font-size: 1rem; line-height: 1.4;
  pointer-events: none; transform-origin: 0 0; transition: transform var(--dur-3) var(--ease-out), color var(--dur-2);
}
.float-form__input:focus + .float-form__label, .float-form__input:not(:placeholder-shown) + .float-form__label { transform: translateY(-0.625rem) scale(0.75); }
.float-form__input:focus + .float-form__label { color: var(--primary); }

/* Valid: a check springs in at the right edge */
.float-form__valid {
  position: absolute; right: 0.875rem; top: 1rem; width: 1.5rem; height: 1.5rem; border-radius: 50%;
  background: var(--success); transform: scale(0); transition: transform var(--dur-4) var(--ease-spring);
}
.float-form__valid::after { content: ""; position: absolute; left: 0.5625rem; top: 0.375rem; width: 0.3125rem; height: 0.5625rem; border: solid var(--surface-light); border-width: 0 2px 2px 0; transform: rotate(45deg); }
.float-form__field[data-valid] .float-form__valid { transform: scale(1); }

/* Error: message slides open beneath; border and label turn red */
.float-form__error { display: grid; grid-template-rows: 0fr; margin: 0; transition: grid-template-rows var(--dur-3) var(--ease-out); }
.float-form__error > span { overflow: hidden; padding-left: 0.25rem; color: var(--danger); font-size: 0.8125rem; font-weight: 500; }
.float-form__field:has([aria-invalid="true"]) .float-form__error { grid-template-rows: 1fr; }
.float-form__field:has([aria-invalid="true"]) .float-form__error > span { padding-top: 0.375rem; }
.float-form__input[aria-invalid="true"] { border-color: var(--danger); }
.float-form__input[aria-invalid="true"]:focus { box-shadow: 0 0 0 4px color-mix(in srgb, var(--danger) 16%, transparent); }
.float-form__input[aria-invalid="true"] + .float-form__label { color: var(--danger); }
.float-form__field[data-shake] { animation: float-form-shake 420ms var(--ease-out); }

/* Service chips */
.float-form__legend { margin-bottom: 0.625rem; padding: 0; font-size: 0.875rem; font-weight: 600; }
.float-form__chips { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.float-form__chip {
  position: relative; display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1rem 0 0.875rem;
  border-radius: 999px; cursor: pointer; font-size: 0.9375rem; font-weight: 500;
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-main) 55%, var(--surface-light));
  transition: background-color var(--dur-2), box-shadow var(--dur-2), color var(--dur-2), transform var(--dur-4) var(--ease-spring);
}
.float-form__chip input { position: absolute; opacity: 0; pointer-events: none; }
.float-form__chip svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; color: var(--text-muted); transition: color var(--dur-2); }
.float-form__chip:hover { background: var(--surface-muted); }
.float-form__chip:active { transform: scale(0.95); }
.float-form__chip:has(:focus-visible) { outline: 2px solid var(--primary); outline-offset: 2px; }
.float-form__chip:has(:checked) {
  background: color-mix(in srgb, var(--primary) 9%, var(--surface-light)); color: var(--primary-hover);
  box-shadow: inset 0 0 0 1.5px var(--primary); animation: float-form-pop var(--dur-4) var(--ease-spring);
}
.float-form__chip:has(:checked) svg { color: var(--primary); }
.float-form__choices:has([aria-invalid="true"]) .float-form__chip { box-shadow: inset 0 0 0 1px var(--danger); }

/* Submit: label → spinner → success, stacked in one cell */
.float-form__submit {
  position: relative; display: grid; place-items: center; width: 100%; height: 3.25rem; margin-top: 1.75rem; overflow: hidden;
  border: 0; border-radius: 999px; cursor: pointer; color: var(--text-inverse); font: 600 1rem var(--font-sans);
  background: linear-gradient(180deg, var(--primary), var(--primary-hover));
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 14px 30px -12px var(--primary);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3);
}
.float-form__submit:hover { box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 18px 36px -12px var(--primary); }
.float-form__submit:active { transform: scale(0.98); }
.float-form__submit:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.float-form__submit::before { content: ""; position: absolute; inset: 0; background: var(--success); opacity: 0; transition: opacity var(--dur-3); }
.float-form__submit > * { position: relative; grid-area: 1 / 1; transition: opacity var(--dur-3), transform var(--dur-4) var(--ease-out); }
.float-form__spinner { width: 1.25rem; height: 1.25rem; border-radius: 50%; border: 2px solid color-mix(in srgb, var(--text-inverse) 35%, transparent); border-top-color: var(--text-inverse); opacity: 0; }
.float-form__done { display: inline-flex; align-items: center; gap: 0.5rem; opacity: 0; transform: translateY(10px); }
.float-form__done svg { fill: none; stroke: currentColor; stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
.float-form__done path { stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset var(--dur-4) var(--ease-out) var(--dur-2); }
.float-form__submit[data-state] .float-form__submit-label { opacity: 0; transform: translateY(-10px); }
.float-form__submit[data-state="loading"] .float-form__spinner { opacity: 1; animation: float-form-spin 0.7s linear infinite; }
.float-form__submit[data-state="success"]::before { opacity: 1; }
.float-form__submit[data-state="success"] .float-form__done { opacity: 1; transform: none; }
.float-form__submit[data-state="success"] .float-form__done path { stroke-dashoffset: 0; }
.float-form__status { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

@media (prefers-reduced-motion: reduce) {
  .float-form__field[data-shake], .float-form__chip:has(:checked) { animation: none; }
  .float-form__submit[data-state] .float-form__spinner { animation: none; }
}
@keyframes float-form-shake { 0%, 100% { transform: none; } 20% { transform: translateX(-6px); } 40% { transform: translateX(6px); } 60% { transform: translateX(-4px); } 80% { transform: translateX(3px); } }
@keyframes float-form-pop { 40% { transform: scale(0.94); } 100% { transform: scale(1); } }
@keyframes float-form-spin { to { rotate: 360deg; } }
```

## JS

```js
document.querySelectorAll('[data-float-form]').forEach((form) => {
  form.noValidate = true; // set by JS so no-JS visitors still get native validation
  const fields = [...form.querySelectorAll('[data-error]')];
  const submit = form.querySelector('.float-form__submit');
  const status = form.querySelector('.float-form__status');

  // Validate one field: ARIA state, message, valid tick
  const check = (field) => {
    const valid = field.checkValidity();
    field.setAttribute('aria-invalid', String(!valid));
    document.getElementById(field.getAttribute('aria-describedby')).firstElementChild.textContent = valid ? '' : field.dataset.error;
    field.closest('.float-form__field').toggleAttribute('data-valid', valid && field.type !== 'radio' && field.value !== '');
    return valid;
  };
  const shake = (field) => {
    const box = field.closest('.float-form__field');
    box.removeAttribute('data-shake');
    void box.offsetWidth; // restart the animation
    box.setAttribute('data-shake', '');
  };

  // Check on leaving a filled field, live while fixing an error, and when a chip is chosen
  form.addEventListener('focusout', (e) => { if (fields.includes(e.target) && e.target.value && e.target.type !== 'radio') check(e.target); });
  form.addEventListener('input', (e) => {
    const field = fields.includes(e.target) ? e.target : null;
    if (field && field.getAttribute('aria-invalid') === 'true') check(field);
  });
  form.addEventListener('change', (e) => { if (e.target.type === 'radio') check(fields.find((f) => f.name === e.target.name)); });
  form.addEventListener('animationend', (e) => e.target.removeAttribute('data-shake'));

  form.addEventListener('submit', (e) => {
    e.preventDefault(); // demo: post with fetch(form.action, { method: 'POST', body: new FormData(form) }) in production
    if (submit.dataset.state) return;
    const invalid = fields.filter((f) => !check(f));
    if (invalid.length) {
      invalid.forEach(shake);
      invalid[0].focus();
      return;
    }
    submit.dataset.state = 'loading';
    submit.setAttribute('aria-disabled', 'true');
    status.textContent = 'Sending your request…';
    setTimeout(() => {
      submit.dataset.state = 'success';
      status.textContent = 'Request sent. We’ll reply within one business day.';
    }, 1400);
  });
});
```

## Notes

- Real `<label for>` on every control. The label sits after its input only so `:placeholder-shown` can float it; reading order and names are unaffected. `placeholder=" "` (a space) is required for the effect.
- Errors are tied with `aria-describedby` and `aria-invalid`; on a failed submit, focus jumps to the first invalid field and the message is read with it. Empty fields aren't flagged on blur, only on submit.
- Field borders are 55% `--text-main` (3.6:1 on white), so the inputs are still identifiable for low-vision users (WCAG 1.4.11).
- `field-sizing: content` grows the details box as you type (Chromium); elsewhere it's a normal resizable textarea.
- Replace the demo `setTimeout` with your real request; keep the `role="status"` updates so screen readers hear "sending" and "sent".
