# One-Time Code Input

A six-digit verification card built on one real input. Decorative boxes sit underneath it: a caret ring glides between them, each digit springs up into its box, and a pasted or autofilled code ripples across all six. A complete code checks itself with a shimmer. A wrong code shakes and tints red. The right one pulls the boxes together into a single green pill and draws a check. On phones the boxes, gaps and digits scale with the card through container units, so six boxes and the split still fit at 320px. Depends on `tokens/variables.css`.

**Motion:** digit pop (`--dur-4`, `--ease-spring`) · paste/autofill ripple staggered by `--stagger` · caret glide (`--dur-4`, `--ease-spring`) with a four-beat cursor blink · checking shimmer (1.2s, four staggered passes) · error shake (`--dur-4`, `--ease-out`) · success merge: boxes close ranks (`--ease-out`), pill contracts (`--dur-5`, `--ease-spring`), check ring and tick draw.

## HTML

```html
<div class="otp-field-demo">
  <form class="otp-field" action="/verify" method="post" aria-labelledby="otp-field-title" data-otp-field data-demo-code="123456">
    <span class="otp-field__badge" aria-hidden="true">
      <svg viewBox="0 0 24 24" width="24" height="24" focusable="false"><rect x="6" y="2" width="12" height="20" rx="3" /><path d="M11 18.5h2M9 11h.01M12 11h.01M15 11h.01" /></svg>
    </span>
    <h2 id="otp-field-title" class="otp-field__title">Check your phone</h2>
    <p class="otp-field__lead">We texted a 6-digit code to <strong>(555) 555-0123</strong>. Enter it below and we'll check it as soon as it's complete.</p>

    <div class="otp-field__row">
      <label class="otp-field__label" for="otp-field-code">Verification code</label>
      <p class="otp-field__hint" id="otp-field-hint">Demo code <b>123456</b></p>
    </div>
    <div class="otp-field__slot">
      <input class="otp-field__input" id="otp-field-code" name="code" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" minlength="6" pattern="[0-9]{6}" required spellcheck="false" aria-describedby="otp-field-hint otp-field-status">
      <div class="otp-field__boxes" aria-hidden="true">
        <span class="otp-field__box" style="--otp-field-i: 0"></span>
        <span class="otp-field__box" style="--otp-field-i: 1"></span>
        <span class="otp-field__box" style="--otp-field-i: 2"></span>
        <span class="otp-field__box" style="--otp-field-i: 3"></span>
        <span class="otp-field__box" style="--otp-field-i: 4"></span>
        <span class="otp-field__box" style="--otp-field-i: 5"></span>
        <span class="otp-field__dash"></span>
        <span class="otp-field__caret"><span class="otp-field__bar"></span></span>
        <span class="otp-field__pill">
          <svg class="otp-field__check" viewBox="0 0 24 24" width="22" height="22" focusable="false"><circle cx="12" cy="12" r="9" pathLength="1" /><path d="m8.5 12.5 2.5 2.5 4.5-5" pathLength="1" /></svg>
          <span class="otp-field__pill-text">Verified</span>
        </span>
      </div>
    </div>
    <p class="otp-field__status" id="otp-field-status" role="status"></p>
    <button class="otp-field__submit" type="submit">Verify code</button>

    <p class="otp-field__foot">
      Didn't get it?
      <button class="otp-field__link otp-field__resend" type="submit" name="intent" value="resend" formnovalidate>
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M21 12a9 9 0 1 1-2.6-6.4L21 8M21 3v5h-5" /></svg>
        <span class="otp-field__resend-text">Resend code</span> <span class="otp-field__count" hidden></span>
      </button>
    </p>
    <button class="otp-field__link otp-field__again" type="button" hidden>Start over</button>
  </form>
</div>
```

## CSS

```css
/* Demo backdrop: soft brand light over a fading dot grid */
.otp-field-demo {
  position: relative; isolation: isolate; display: grid; place-items: center;
  min-height: 40rem; padding: 3rem var(--gutter);
  background:
    radial-gradient(55% 45% at 50% 0%, color-mix(in srgb, var(--primary) 12%, transparent), transparent 70%),
    radial-gradient(45% 40% at 90% 100%, color-mix(in srgb, var(--primary-2) 10%, transparent), transparent 70%),
    var(--surface-muted);
}
.otp-field-demo::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  background: radial-gradient(color-mix(in srgb, var(--text-main) 12%, transparent) 1px, transparent 1.5px) 0 0 / 1.25rem 1.25rem;
  -webkit-mask-image: radial-gradient(ellipse 60% 55% at 50% 45%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 60% 55% at 50% 45%, black, transparent 75%);
}

/* Card */
.otp-field {
  --otp-field-ring: var(--primary);
  position: relative; isolation: isolate; width: min(100%, 25rem);
  padding: clamp(1.5rem, 1rem + 2.5vw, 2.25rem);
  border-radius: var(--radius-2xl); background: var(--surface-light); color: var(--text-main);
  font-family: var(--font-sans); text-align: center;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl);
}
.otp-field::before {
  content: ""; position: absolute; inset: 0 0 auto; z-index: -1; height: 9rem; border-radius: inherit; pointer-events: none;
  background: radial-gradient(70% 100% at 50% 0%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 75%);
}
.otp-field[data-state="loading"] { --otp-field-ring: color-mix(in srgb, var(--primary) 45%, transparent); }
.otp-field[data-state="error"] { --otp-field-ring: var(--danger); }

/* Phone badge with two quiet signal rings */
.otp-field__badge {
  position: relative; display: grid; place-items: center; width: 3.5rem; height: 3.5rem; margin: 0.75rem auto 1.75rem;
  border-radius: 1.125rem; background: var(--gradient-brand); color: var(--text-inverse);
  box-shadow: var(--shadow-glow), inset 0 1px 0 color-mix(in srgb, var(--surface-light) 35%, transparent);
}
.otp-field__badge::before, .otp-field__badge::after {
  content: ""; position: absolute; inset: -0.625rem; z-index: -1; border-radius: 1.625rem;
  border: 1px solid color-mix(in srgb, var(--primary) 18%, transparent);
}
.otp-field__badge::after { inset: -1.375rem; border-radius: 2.25rem; border-color: color-mix(in srgb, var(--primary) 8%, transparent); }
.otp-field__badge svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

.otp-field__title { margin: 0; font: 600 clamp(1.5rem, 1.3rem + 0.8vw, 1.75rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.otp-field__lead { max-width: 20rem; margin: 0.625rem auto 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.55; text-wrap: pretty; }
.otp-field__lead strong { color: var(--text-main); font-weight: 600; white-space: nowrap; }

/* Label row */
.otp-field__row { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.5rem 0.75rem; margin-top: 1.75rem; text-align: left; }
.otp-field__label { font-size: 0.8125rem; font-weight: 600; }
.otp-field__hint {
  margin: 0; padding: 0.25rem 0.625rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--primary) 8%, var(--surface-light)); color: var(--primary-hover);
  font: 500 0.75rem/1.4 var(--font-mono);
}
.otp-field__hint b { font-weight: 700; letter-spacing: 0.06em; }

/* The real input. Without JS it is a roomy monospace field */
.otp-field__slot { position: relative; margin-top: 0.625rem; container-type: inline-size; }
.otp-field__input {
  display: block; width: 100%; height: 3.5rem; margin: 0; padding: 0 0 0 0.5em; border: 0;
  border-radius: var(--radius-lg); background: var(--surface-muted); color: var(--text-main);
  box-shadow: inset 0 0 0 1px var(--border-subtle);
  font: 600 1.5rem/1 var(--font-mono); font-variant-numeric: tabular-nums; letter-spacing: 0.5em; text-align: center;
  transition: box-shadow var(--dur-2) var(--ease-out);
}
.otp-field:not(.otp-field--js) .otp-field__input:focus-visible { outline: 2px solid transparent; box-shadow: inset 0 0 0 1px var(--primary), var(--focus-ring); }
.otp-field__boxes { display: none; }

/* Enhanced: the input lies invisibly over the boxes and keeps focus, autofill and AT */
.otp-field--js .otp-field__input {
  position: absolute; inset: 0; z-index: 3; height: 100%; padding: 0; border-radius: 0;
  background: transparent; box-shadow: none; outline: none; cursor: text;
  color: transparent; -webkit-text-fill-color: transparent; caret-color: transparent;
  font-size: 1rem; letter-spacing: 0;
}
.otp-field--js .otp-field__input::selection { background: transparent; color: transparent; }
.otp-field--js .otp-field__input:disabled { cursor: default; }
.otp-field--js .otp-field__input:autofill { opacity: 0; }
.otp-field--js .otp-field__input:-webkit-autofill { opacity: 0; }

.otp-field--js .otp-field__boxes {
  --otp-field-gap: 0.4rem; --otp-field-split: 0.75rem; --otp-field-h: 3.5rem; --otp-field-size: 1.5rem;
  position: relative; display: flex; gap: var(--otp-field-gap);
  transition: filter var(--dur-4) var(--ease-out);
}
@supports (width: 1cqi) {
  .otp-field--js .otp-field__boxes {
    --otp-field-gap: clamp(0.25rem, 2cqi, 0.5rem); --otp-field-split: clamp(0.5rem, 4cqi, 1rem);
    --otp-field-h: clamp(3rem, 17cqi, 4rem); --otp-field-size: clamp(1.25rem, 8cqi, 1.75rem);
  }
}

/* Boxes: a dot when empty, a lifted tile when filled */
.otp-field__box {
  --otp-field-s: clamp(-1, (2.5 - var(--otp-field-i)) * 4, 1);
  position: relative; display: grid; place-items: center; flex: 1 1 0; min-width: 0; height: var(--otp-field-h); overflow: hidden;
  border-radius: var(--radius-lg); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
  color: var(--text-main); font: 600 var(--otp-field-size)/1 var(--font-mono); font-variant-numeric: tabular-nums;
  transition: translate var(--dur-4) var(--ease-out), opacity var(--dur-3) var(--ease-out), background-color var(--dur-3) var(--ease-out), box-shadow var(--dur-3) var(--ease-out), color var(--dur-3) var(--ease-out);
}
.otp-field__box:nth-child(4) { margin-inline-start: var(--otp-field-split); }
.otp-field__box::before {
  content: ""; grid-area: 1 / 1; width: 0.375rem; height: 0.375rem; border-radius: 50%;
  background: color-mix(in srgb, var(--text-muted) 40%, transparent);
  transition: opacity var(--dur-2) var(--ease-out), scale var(--dur-3) var(--ease-spring);
}
.otp-field__box.is-filled { background: var(--surface-light); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-main) 16%, transparent), var(--shadow-sm); }
.otp-field__box.is-filled::before { opacity: 0; scale: 0; }
.otp-field__box.is-ripple { animation: otp-field-ripple var(--dur-4) var(--ease-out) calc(var(--otp-field-i) * var(--stagger)) both; }
.otp-field__digit { grid-area: 1 / 1; animation: otp-field-pop var(--dur-4) var(--ease-spring) calc(var(--otp-field-d, 0) * var(--stagger)) both; }

.otp-field__dash {
  position: absolute; left: 50%; top: 50%; width: 0.5rem; height: 2px; border-radius: 1px; translate: -50% -50%;
  background: color-mix(in srgb, var(--text-muted) 45%, transparent); transition: opacity var(--dur-2) var(--ease-out);
}

/* Caret ring: glides to the active box; a cursor blinks a few times in an empty one */
.otp-field__caret {
  position: absolute; top: 0; left: 0; z-index: 1; height: 100%; pointer-events: none;
  width: calc((100% - 5 * var(--otp-field-gap) - var(--otp-field-split)) / 6);
  border-radius: var(--radius-lg);
  box-shadow: 0 0 0 2px var(--otp-field-ring), 0 0 0 6px color-mix(in srgb, var(--otp-field-ring) 18%, transparent);
  translate: calc(var(--otp-field-at, 0) * (100% + var(--otp-field-gap)) + clamp(0, var(--otp-field-at, 0) - 2, 1) * var(--otp-field-split)) 0;
  opacity: 0; scale: 0.9;
  transition: translate var(--dur-4) var(--ease-spring), scale var(--dur-3) var(--ease-spring), opacity var(--dur-2) var(--ease-out), box-shadow var(--dur-3) var(--ease-out);
}
.otp-field__input:focus ~ .otp-field__boxes .otp-field__caret { opacity: 1; scale: 1; }
.otp-field__bar {
  position: absolute; left: 50%; top: 50%; width: 2px; height: 40%; border-radius: 1px; translate: -50% -50%;
  background: var(--otp-field-ring); opacity: 0;
}
.otp-field__caret.is-blank .otp-field__bar { opacity: 1; animation: otp-field-blink 1.1s var(--ease-in-out) 4; }

/* Checking: a staggered shimmer runs across the boxes */
.otp-field__box::after {
  content: ""; position: absolute; inset: 0; translate: -100% 0; opacity: 0; pointer-events: none;
  background: linear-gradient(100deg, transparent 15%, color-mix(in srgb, var(--primary) 22%, transparent) 50%, transparent 85%);
}
.otp-field[data-state="loading"] .otp-field__box { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 35%, transparent); }
.otp-field[data-state="loading"] .otp-field__box::after { opacity: 1; animation: otp-field-shimmer 1.2s var(--ease-in-out) calc(var(--otp-field-i) * 90ms) 4; }

/* Wrong code: shake and tint */
.otp-field__boxes.is-shaking { animation: otp-field-shake var(--dur-4) var(--ease-out); }
.otp-field[data-state="error"] .otp-field__box {
  background: color-mix(in srgb, var(--danger) 6%, var(--surface-light)); color: var(--danger);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--danger) 50%, transparent);
}
.otp-field[data-state="error"] .otp-field__box::before { background: color-mix(in srgb, var(--danger) 45%, transparent); }

/* Verified: boxes close ranks, a green pill covers them and contracts, the check draws */
.otp-field[data-state="success"] .otp-field__boxes { filter: drop-shadow(0 0.75rem 1rem color-mix(in srgb, var(--success) 35%, transparent)); }
.otp-field[data-state="success"] .otp-field__box {
  translate: calc((2.5 - var(--otp-field-i)) * var(--otp-field-gap) + var(--otp-field-s) * var(--otp-field-split) / 2) 0;
  opacity: 0; background: color-mix(in srgb, var(--success) 14%, var(--surface-light)); color: var(--success);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--success) 45%, transparent);
  transition-delay: 0s, calc(var(--stagger) * 5), 0s, 0s, 0s;
}
.otp-field[data-state="success"] .otp-field__dash { opacity: 0; }
.otp-field__pill {
  --otp-field-pack: calc((5 * var(--otp-field-gap) + var(--otp-field-split)) / 2);
  position: absolute; inset: 0; z-index: 2; display: flex; align-items: center; justify-content: center; gap: 0.5rem;
  background: linear-gradient(180deg, var(--success), color-mix(in srgb, var(--success) 78%, var(--surface-deep)));
  color: var(--text-inverse); font: 600 0.9375rem var(--font-sans);
  clip-path: inset(0 var(--otp-field-pack) round var(--radius-lg));
  opacity: 0; visibility: hidden;
  transition: opacity var(--dur-2) var(--ease-out), clip-path var(--dur-4) var(--ease-out), visibility 0s linear var(--dur-2);
}
.otp-field[data-state="success"] .otp-field__pill {
  opacity: 1; visibility: visible;
  clip-path: inset(max(0px, (var(--otp-field-h) - 3rem) / 2) max(0px, 50% - 5.25rem) round 1.5rem);
  transition: opacity var(--dur-2) var(--ease-out) calc(var(--stagger) * 4), clip-path var(--dur-5) var(--ease-spring) calc(var(--stagger) * 6), visibility 0s linear calc(var(--stagger) * 4);
}
.otp-field__check { flex: none; fill: none; stroke: currentColor; stroke-width: 2.25; stroke-linecap: round; stroke-linejoin: round; scale: 0.6; transition: scale var(--dur-4) var(--ease-spring); }
.otp-field__check circle { stroke: color-mix(in srgb, var(--text-inverse) 45%, transparent); }
.otp-field__check :is(circle, path) { stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset var(--dur-4) var(--ease-out); }
.otp-field__pill-text { opacity: 0; translate: 0.375rem 0; transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-spring); }
.otp-field[data-state="success"] .otp-field__check { scale: 1; transition-delay: calc(var(--stagger) * 8); }
.otp-field[data-state="success"] .otp-field__check circle { stroke-dashoffset: 0; transition-delay: calc(var(--stagger) * 8); }
.otp-field[data-state="success"] .otp-field__check path { stroke-dashoffset: 0; transition-delay: calc(var(--stagger) * 11); }
.otp-field[data-state="success"] .otp-field__pill-text { opacity: 1; translate: 0 0; transition-delay: calc(var(--stagger) * 10); }

/* Status, fallback submit, resend */
.otp-field__status { min-height: 1.375rem; margin: 0.875rem 0 0; color: var(--text-muted); font-size: 0.875rem; font-weight: 500; line-height: 1.5; }
.otp-field[data-state="error"] .otp-field__status { color: var(--danger); }
.otp-field[data-state="success"] .otp-field__status { color: var(--success); }
.otp-field__submit {
  width: 100%; height: 3rem; margin-top: 0.75rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--text-main); color: var(--surface-light); font: 600 0.9375rem var(--font-sans);
  box-shadow: var(--highlight-inverse), 0 10px 24px -12px color-mix(in srgb, var(--text-main) 70%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.otp-field__submit:active { transform: scale(0.97); }
.otp-field--js .otp-field__submit { display: none; }
.otp-field__foot {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 0.25rem 0.375rem;
  margin: 1.25rem 0 0; padding-top: 1.25rem; border-top: 1px solid var(--border-subtle); color: var(--text-muted); font-size: 0.875rem;
}
.otp-field__foot[hidden] { display: none; }
.otp-field__link {
  display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.5rem; padding: 0 0.75rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: transparent; color: var(--primary); font: 600 0.875rem var(--font-sans);
  transition: background-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out);
}
.otp-field__link[hidden] { display: none; }
.otp-field__link:hover { background: color-mix(in srgb, var(--primary) 8%, transparent); }
.otp-field__link[aria-disabled="true"] { background: transparent; color: var(--text-muted); cursor: not-allowed; }
.otp-field__link svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.otp-field__again { margin-top: 0.75rem; }
.otp-field__count { font-family: var(--font-mono); font-variant-numeric: tabular-nums; }
.otp-field :is(.otp-field__link, .otp-field__submit):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) {
  .otp-field *, .otp-field *::before, .otp-field *::after { animation: none !important; }
}
@keyframes otp-field-pop { from { opacity: 0; transform: translateY(0.7em) scale(0.5); filter: blur(4px); } }
@keyframes otp-field-ripple { 40% { transform: translateY(-0.375rem) scale(1.05); } }
@keyframes otp-field-blink { 50% { opacity: 0; } }
@keyframes otp-field-shimmer { from { translate: -100% 0; } to { translate: 100% 0; } }
@keyframes otp-field-shake {
  15% { transform: translateX(-0.5rem); } 30% { transform: translateX(0.4rem); } 45% { transform: translateX(-0.28rem); }
  60% { transform: translateX(0.16rem); } 75% { transform: translateX(-0.06rem); }
}
```

## JS

```js
document.querySelectorAll('[data-otp-field]').forEach((form) => {
  const $ = (part) => form.querySelector(`.otp-field__${part}`);
  const [input, row, caret, status, foot, resend, again] = ['input', 'boxes', 'caret', 'status', 'foot', 'resend', 'again'].map($);
  const boxes = [...row.querySelectorAll('.otp-field__box')];
  const [label, count] = resend.querySelectorAll('span');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const N = boxes.length;
  let prev = input.value;
  let timer = 0;
  let tick = 0;
  form.classList.add('otp-field--js');
  form.noValidate = true;
  resend.type = 'button';

  // Demo check. Swap for a request to your verify endpoint that resolves true/false
  const verify = (code) => new Promise((done) => setTimeout(() => done(code === form.dataset.demoCode), 1400));

  const setState = (state, message = '') => {
    form.dataset.state = state;
    status.textContent = message;
    input.readOnly = state === 'loading';
    input.disabled = state === 'success';
    input.setAttribute('aria-invalid', String(state === 'error'));
  };

  // Restart a one-shot CSS animation (shake, ripple) by re-adding its class
  const replay = (els, cls) => {
    els.forEach((el) => el.classList.remove(cls));
    void row.offsetWidth;
    els.forEach((el) => el.classList.add(cls));
  };

  // Caret: a filled box is selected (typing replaces it), otherwise the first empty box
  const setCaret = (i) => {
    const len = input.value.length;
    const at = Math.max(0, Math.min(i, len, N - 1));
    if (document.activeElement === input) input.setSelectionRange(at, at < len ? at + 1 : at);
    form.style.setProperty('--otp-field-at', at);
    caret.classList.toggle('is-blank', at === len);
    caret.firstElementChild.getAnimations().forEach((a) => { a.cancel(); a.play(); });
  };

  // Paint digits into the boxes; a fill (paste, autofill) ripples across them
  const render = (fill = false) => {
    const changed = boxes.filter((box, i) => box.textContent !== (input.value[i] || ''));
    changed.forEach((box) => {
      const i = boxes.indexOf(box);
      box.replaceChildren();
      box.classList.toggle('is-filled', i < input.value.length);
      if (i >= input.value.length) return;
      const digit = Object.assign(document.createElement('span'), { className: 'otp-field__digit', textContent: input.value[i] });
      digit.style.setProperty('--otp-field-d', fill ? i : 0);
      box.append(digit);
    });
    if (fill) replay(changed.filter((box) => box.textContent), 'is-ripple');
  };

  const reset = () => {
    input.value = prev = '';
    render();
    setCaret(0);
  };
  const showAgain = (on) => { again.hidden = !on; foot.hidden = on; };

  const commit = (fill) => {
    if (form.dataset.state === 'error') setState('idle');
    render(fill);
    prev = input.value;
    setCaret(fill ? N : input.selectionStart);
    clearTimeout(timer);
    if (prev.length === N) timer = setTimeout(() => input.value.length === N && form.requestSubmit(), fill && !reduce.matches ? 650 : 280);
  };

  const fail = (message) => {
    setState('error', message);
    replay([row], 'is-shaking');
    input.focus();
  };

  input.addEventListener('beforeinput', (e) => {
    if (e.inputType === 'insertText' && /\D/.test(e.data ?? '')) e.preventDefault();
  });
  input.addEventListener('input', (e) => {
    const clean = input.value.replace(/\D/g, '').slice(0, N);
    const fill = clean.length - prev.length > 1 || (!e.inputType && clean.length > 1);
    if (clean !== input.value) input.value = clean;
    commit(fill);
  });
  input.addEventListener('paste', (e) => {
    e.preventDefault();
    const code = e.clipboardData.getData('text').replace(/\D/g, '').slice(0, N);
    if (code && !input.readOnly) { input.value = code; commit(true); }
  });
  input.addEventListener('keydown', (e) => {
    const at = Math.min(input.selectionStart, N - 1);
    const to = { ArrowLeft: at - 1, ArrowRight: at + 1, Home: 0, End: N }[e.key];
    if (to === undefined || e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    e.preventDefault();
    setCaret(to);
  });
  input.addEventListener('click', (e) => {
    const r = input.getBoundingClientRect();
    setCaret(Math.floor(((e.clientX - r.left) / r.width) * N));
  });
  // Tabbing in selects everything; settle on the first empty box instead
  input.addEventListener('focus', () => requestAnimationFrame(() => {
    setCaret(input.selectionEnd - input.selectionStart > 1 ? N : input.selectionStart);
  }));

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (input.readOnly || input.disabled) return;
    clearTimeout(timer);
    if (input.value.length < N) return fail(`Enter all ${N} digits.`);
    setState('loading', 'Checking your code…');
    if (!(await verify(input.value))) {
      fail("That code didn't match. Try again.");
      // Clear the wrong code once the shake has played, unless they're already retyping
      return setTimeout(() => form.dataset.state === 'error' && reset(), reduce.matches ? 0 : 520);
    }
    setState('success', "Verified. You're all set.");
    showAgain(true);
    again.focus();
  });

  // Resend stays focusable (aria-disabled) while it counts down
  const countdown = (seconds) => {
    const until = Date.now() + seconds * 1000;
    const step = () => {
      const left = Math.max(0, Math.ceil((until - Date.now()) / 1000));
      resend.setAttribute('aria-disabled', String(left > 0));
      label.textContent = left ? 'Resend in' : 'Resend code';
      count.textContent = `${Math.floor(left / 60)}:${String(left % 60).padStart(2, '0')}`;
      count.hidden = !left;
      if (!left) clearInterval(tick);
    };
    clearInterval(tick);
    tick = setInterval(step, 1000);
    step();
  };
  resend.addEventListener('click', () => {
    if (resend.getAttribute('aria-disabled') === 'true') return;
    countdown(30);
    status.textContent = 'A new code is on its way.';
  });
  again.addEventListener('click', () => {
    setState('idle');
    showAgain(false);
    reset();
    input.focus();
  });

  setState('idle');
  render();
  setCaret(prev.length);
  countdown(24);
});
```

## Notes

- One native input holds the value, label and description. It has `autocomplete="one-time-code"`, `inputmode="numeric"` and `pattern`, so iOS/Android code suggestions, password managers and paste all fill it, and a fill ripples across the boxes. The boxes, caret ring and pill are `aria-hidden` paint over it. ←/→/Home/End move between boxes, and a filled box is selected so the next digit replaces it. Backspace steps back one box. Clicking a box puts the caret there.
- Checking, errors, success and "new code sent" all go through one polite `role="status"` region. Errors also set `aria-invalid`. The lead copy says the code is checked as soon as it's complete (WCAG 3.2.2). Resend uses `aria-disabled` while it counts down, so it stays discoverable, and on success focus moves to the next control.
- Without JS it's a plain, large monospace field with a "Verify code" button and a working resend submit. `required` and `pattern` validate it natively.
- Reduced motion: no pop, ripple, shake, shimmer or cursor blink. Every delay is a multiple of `--stagger`, so states switch instantly. The cursor blink and the checking shimmer both stop after four beats (under 5s), so nothing needs a pause control.
- Contrast: "Verified" is `--text-inverse` on a gradient that never gets lighter than `--success` (4.8:1). Error text uses `--danger` (4.8:1), and the demo hint uses `--primary-hover` on its 8% tint (about 6:1).
- To wire it up, replace `verify()` with a fetch to your endpoint and use unique ids per instance. The digit count follows the number of `.otp-field__box` elements, so keep `maxlength`/`pattern` in step. Chrome's WebOTP (`navigator.credentials.get({ otp })`) can call the same fill path. Uses container units, `:autofill` and the individual `translate`/`scale` properties. Older engines get fixed box sizes. "Start over" is for the demo.
