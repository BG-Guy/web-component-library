# Service-Area Checker

"Do we serve your area?" answered on a stylised map of six Springfield neighbourhoods, drawn as soft-cornered zones on a light surface. Enter a ZIP or pick a neighbourhood chip: the matching zone fills with the brand gradient, a pin drops in with a bounce and a ripple, and a result card slides in with the next opening and a booking CTA, or a friendly waitlist offer for an unknown ZIP. Hovering a zone previews its response time. On phones the map sits between the controls and the result. Depends on `tokens/variables.css`.

**Motion:** zone gradient bloom (opacity + scale, `--dur-4`, `--ease-spring`) · pin drop with squash and settle, then a ground ripple (WAAPI) · result card slide-in (`--ease-out`) · zone hover tooltip rise (`--dur-3`) · chip press and check springs · ZIP error shake.

## HTML

```html
<section class="coverage-check" aria-labelledby="coverage-check-title" data-coverage-check>
  <div class="coverage-check__inner">
    <header class="coverage-check__head">
      <p class="coverage-check__eyebrow">Service area</p>
      <h2 id="coverage-check-title" class="coverage-check__title">Do we serve your area?</h2>
      <p class="coverage-check__lede">Six Springfield neighbourhoods, with same-day windows in most of them.</p>
    </header>

    <form class="coverage-check__form" action="/coverage" method="get">
      <label class="coverage-check__label" for="coverage-check-zip">Your ZIP code</label>
      <div class="coverage-check__field">
        <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z" /><circle cx="12" cy="10" r="2.5" /></svg>
        <input class="coverage-check__input" id="coverage-check-zip" name="zip" inputmode="numeric" autocomplete="postal-code" pattern="\d{5}" maxlength="5" placeholder="e.g. 62702" required>
        <button class="coverage-check__go" type="submit">Check</button>
      </div>
      <p class="coverage-check__error"></p>

      <p class="coverage-check__or">Or pick your neighbourhood</p>
      <div class="coverage-check__chips" role="group" aria-label="Neighbourhoods">
        <button class="coverage-check__chip" type="submit" name="area" value="westlake" formnovalidate aria-pressed="false" data-zone="westlake" data-zips="62704 62711" data-next="Today 3–5pm" data-eta="35"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Westlake</button>
        <button class="coverage-check__chip" type="submit" name="area" value="northside" formnovalidate aria-pressed="false" data-zone="northside" data-zips="62702 62707" data-next="Today 3–5pm" data-eta="45"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Northside</button>
        <button class="coverage-check__chip" type="submit" name="area" value="riverside" formnovalidate aria-pressed="false" data-zone="riverside" data-zips="62703 62712" data-next="Today 5–7pm" data-eta="30"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Riverside</button>
        <button class="coverage-check__chip" type="submit" name="area" value="downtown" formnovalidate aria-pressed="false" data-zone="downtown" data-zips="62701" data-next="Tomorrow 8–10am" data-eta="25"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Downtown</button>
        <button class="coverage-check__chip" type="submit" name="area" value="eastgate" formnovalidate aria-pressed="false" data-zone="eastgate" data-zips="62705 62706" data-next="Tomorrow 10am–12pm" data-eta="50"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Eastgate</button>
        <button class="coverage-check__chip" type="submit" name="area" value="hillcrest" formnovalidate aria-pressed="false" data-zone="hillcrest" data-zips="62708 62709" data-next="Tomorrow 1–3pm" data-eta="60"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Hillcrest</button>
      </div>
    </form>

    <div class="coverage-check__map" aria-hidden="true">
      <p class="coverage-check__caption"><span>Springfield service map</span><span class="coverage-check__hint">Hover a zone for response times</span></p>
      <svg class="coverage-check__svg" viewBox="0 0 480 360" focusable="false">
        <defs>
          <linearGradient class="coverage-check__grad" id="coverage-check-grad" x1="0" y1="0" x2="1" y2="1">
            <stop class="coverage-check__stop-a" offset="0" /><stop class="coverage-check__stop-b" offset="1" />
          </linearGradient>
        </defs>
        <g class="coverage-check__zone" data-zone="northside" data-pin="178 62">
          <polygon class="coverage-check__shape" points="40,36 300,26 318,108 196,122 52,112" />
          <polygon class="coverage-check__glow" points="40,36 300,26 318,108 196,122 52,112" />
          <path class="coverage-check__decor coverage-check__decor--dots" d="M70 56h0M92 50h0M116 60h0M250 48h0M276 70h0M84 90h0M262 94h0" />
          <text class="coverage-check__name" x="178" y="84">Northside</text>
          <g class="coverage-check__tip" transform="translate(178 32)"><rect x="-58" y="-11" width="116" height="22" rx="11" /><text y="4">~45 min response</text></g>
        </g>
        <g class="coverage-check__zone" data-zone="eastgate" data-pin="398 110">
          <polygon class="coverage-check__shape" points="342,30 442,48 452,196 360,204 340,124" />
          <polygon class="coverage-check__glow" points="342,30 442,48 452,196 360,204 340,124" />
          <path class="coverage-check__decor" d="M372 160v-14a14 14 0 0 1 28 0v14M366 160h40" />
          <text class="coverage-check__name" x="398" y="132">Eastgate</text>
          <g class="coverage-check__tip" transform="translate(398 80)"><rect x="-58" y="-11" width="116" height="22" rx="11" /><text y="4">~50 min response</text></g>
        </g>
        <g class="coverage-check__zone" data-zone="westlake" data-pin="106 156">
          <polygon class="coverage-check__shape" points="38,138 174,146 166,246 44,252" />
          <polygon class="coverage-check__glow" points="38,138 174,146 166,246 44,252" />
          <ellipse class="coverage-check__water" cx="106" cy="216" rx="34" ry="15" />
          <text class="coverage-check__name" x="106" y="178">Westlake</text>
          <g class="coverage-check__tip" transform="translate(106 126)"><rect x="-58" y="-11" width="116" height="22" rx="11" /><text y="4">~35 min response</text></g>
        </g>
        <g class="coverage-check__zone" data-zone="downtown" data-pin="262 166">
          <polygon class="coverage-check__shape" points="198,146 320,132 334,206 262,232 194,222" />
          <polygon class="coverage-check__glow" points="198,146 320,132 334,206 262,232 194,222" />
          <path class="coverage-check__decor" d="M226 200v-16h10v16M240 200v-26h10v26M254 200v-20h10v20M268 200v-30h10v30M282 200v-14h10v14" />
          <text class="coverage-check__name" x="262" y="160">Downtown</text>
          <g class="coverage-check__tip" transform="translate(262 120)"><rect x="-58" y="-11" width="116" height="22" rx="11" /><text y="4">~25 min response</text></g>
        </g>
        <g class="coverage-check__zone" data-zone="riverside" data-pin="320 268">
          <polygon class="coverage-check__shape" points="190,248 262,256 350,226 452,220 444,322 306,334 196,318" />
          <polygon class="coverage-check__glow" points="190,248 262,256 350,226 452,220 444,322 306,334 196,318" />
          <path class="coverage-check__water-line" d="M214 306q20-9 40 0t40 0 40 0 40 0 40 0 30 0" />
          <text class="coverage-check__name" x="320" y="290">Riverside</text>
          <g class="coverage-check__tip" transform="translate(320 236)"><rect x="-58" y="-11" width="116" height="22" rx="11" /><text y="4">~30 min response</text></g>
        </g>
        <g class="coverage-check__zone" data-zone="hillcrest" data-pin="106 292">
          <polygon class="coverage-check__shape" points="40,276 166,270 172,330 48,334" />
          <polygon class="coverage-check__glow" points="40,276 166,270 172,330 48,334" />
          <path class="coverage-check__decor" d="M58 326q18-20 36 0M88 326q22-26 44 0M124 326q14-14 28 0" />
          <text class="coverage-check__name" x="106" y="306">Hillcrest</text>
          <g class="coverage-check__tip" transform="translate(106 258)"><rect x="-58" y="-11" width="116" height="22" rx="11" /><text y="4">~60 min response</text></g>
        </g>
        <g class="coverage-check__pin" transform="translate(178 62)">
          <ellipse class="coverage-check__ring" rx="12" ry="5" />
          <ellipse class="coverage-check__shadow" rx="6" ry="2.5" />
          <g class="coverage-check__drop">
            <path class="coverage-check__pin-body" d="M0 0C-1-7-11-11-11-20A11 11 0 0 1 11-20C11-11 1-7 0 0Z" />
            <circle class="coverage-check__pin-dot" cy="-20" r="4" />
          </g>
        </g>
      </svg>
    </div>

    <div class="coverage-check__result" aria-live="polite">
      <div class="coverage-check__state coverage-check__state--idle">
        <span class="coverage-check__badge" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z" /><circle cx="12" cy="10" r="2.5" /></svg></span>
        <div>
          <p class="coverage-check__result-title">Covering six Springfield neighbourhoods</p>
          <p class="coverage-check__result-text">Enter your ZIP or pick a neighbourhood to see your next opening.</p>
        </div>
      </div>
      <div class="coverage-check__state coverage-check__state--yes" hidden>
        <span class="coverage-check__badge coverage-check__badge--yes" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg></span>
        <div>
          <p class="coverage-check__result-title">Yes! <span data-slot="area">Northside</span> is covered.</p>
          <p class="coverage-check__result-text">Next available: <strong data-slot="next">Today 3–5pm</strong> · typical response about <span data-slot="eta">45</span> min.</p>
        </div>
        <a class="coverage-check__cta" href="#book">Book <span data-slot="next">Today 3–5pm</span><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </div>
      <div class="coverage-check__state coverage-check__state--no" hidden>
        <span class="coverage-check__badge coverage-check__badge--no" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M12 7v6M12 17h0" /><circle cx="12" cy="12" r="9" /></svg></span>
        <div>
          <p class="coverage-check__result-title">Not yet in <span data-slot="zip">90210</span>, but we're growing.</p>
          <p class="coverage-check__result-text">Join the waitlist and we'll email you the week we start serving your street.</p>
        </div>
        <a class="coverage-check__cta coverage-check__cta--ghost" href="#waitlist">Join the waitlist</a>
      </div>
    </div>

    <div class="coverage-check__list">
      <h3 class="coverage-check__list-title">Areas we cover</h3>
      <ul class="coverage-check__areas" role="list">
        <li><span>Westlake</span><span>62704 · 62711</span></li>
        <li><span>Northside</span><span>62702 · 62707</span></li>
        <li><span>Riverside</span><span>62703 · 62712</span></li>
        <li><span>Downtown</span><span>62701</span></li>
        <li><span>Eastgate</span><span>62705 · 62706</span></li>
        <li><span>Hillcrest</span><span>62708 · 62709</span></li>
      </ul>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: one grid; phones read head → form → map → result → list */
.coverage-check {
  --coverage-check-fill: url(#coverage-check-grad);
  --coverage-check-grad: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  background:
    radial-gradient(45% 50% at 100% 15%, color-mix(in srgb, var(--primary-2) 9%, transparent), transparent 70%),
    radial-gradient(40% 40% at 0% 100%, color-mix(in srgb, var(--primary) 6%, transparent), transparent 70%),
    var(--surface-light);
  color: var(--text-main); font-family: var(--font-sans);
}
.coverage-check__inner {
  display: grid; gap: 1.5rem; grid-template-areas: "head" "form" "map" "result" "list";
  max-width: var(--container-max); margin-inline: auto; padding: clamp(3.5rem, 8vw, 6rem) var(--gutter);
}
.coverage-check__head { grid-area: head; }
.coverage-check__form { grid-area: form; }
.coverage-check__map { grid-area: map; }
.coverage-check__result { grid-area: result; }
.coverage-check__list { grid-area: list; }
:where(.coverage-check) svg:not(.coverage-check__svg) { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.coverage-check :is(a, button):focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

.coverage-check__eyebrow { margin: 0; color: var(--primary); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.coverage-check__title { margin: 0.875rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.6vw, 3.25rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.coverage-check__lede { max-width: 30rem; margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }

/* ZIP field: icon, input and a Check button in one pill */
.coverage-check__label { display: block; margin-bottom: 0.5rem; font-size: 0.9375rem; font-weight: 600; }
.coverage-check__field {
  display: flex; align-items: center; gap: 0.5rem; height: 3.5rem; padding: 0.375rem 0.375rem 0.375rem 1rem; border-radius: var(--radius-full);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-md); transition: box-shadow var(--dur-2);
}
.coverage-check__field > svg { flex: none; color: var(--primary); }
.coverage-check__field:has(.coverage-check__input:focus-visible) { box-shadow: inset 0 0 0 1px var(--primary), var(--focus-ring); }
.coverage-check__field:has([aria-invalid="true"]) { box-shadow: inset 0 0 0 1.5px var(--danger), var(--shadow-md); }
.coverage-check__input { flex: 1; min-width: 0; height: 100%; padding: 0; border: 0; background: transparent; color: var(--text-main); font: 600 1.125rem var(--font-mono); letter-spacing: 0.08em; }
.coverage-check__input:focus-visible { outline: 2px solid transparent; }
.coverage-check__input::placeholder { color: var(--text-muted); font-weight: 500; letter-spacing: 0.02em; }
.coverage-check__go {
  flex: none; height: 100%; padding: 0 1.25rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--coverage-check-grad); color: var(--text-inverse); font: 600 0.9375rem var(--font-sans);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 8px 18px -8px color-mix(in srgb, var(--primary) 80%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.coverage-check__go:active { transform: scale(0.95); }
.coverage-check__error { margin: 0.5rem 0 0 1rem; color: var(--danger); font-size: 0.8125rem; font-weight: 500; }
.coverage-check__error:empty { display: none; }

/* Neighbourhood chips: toggle buttons; the dot springs into a check */
.coverage-check__or { margin: 1.5rem 0 0.75rem; color: var(--text-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.coverage-check__chips { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.coverage-check__chip {
  position: relative; display: inline-flex; align-items: center; height: 2.75rem; padding: 0 1rem 0 2.25rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--surface-muted); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle); font: 600 0.875rem var(--font-sans);
  transition: background-color var(--dur-2), color var(--dur-2), box-shadow var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.coverage-check__chip::before {
  content: ""; position: absolute; top: 50%; left: 1rem; width: 0.5rem; height: 0.5rem; margin-top: -0.25rem; border-radius: 50%;
  background: color-mix(in srgb, var(--primary) 45%, var(--surface-light)); transition: scale var(--dur-3) var(--ease-spring);
}
.coverage-check__chip svg { position: absolute; top: 50%; left: 0.75rem; margin-top: -0.5rem; scale: 0; transition: scale var(--dur-4) var(--ease-spring); }
.coverage-check__chip:hover { background: var(--surface-light); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 40%, var(--border-subtle)), var(--shadow-sm); }
.coverage-check__chip:active { transform: scale(0.95); }
.coverage-check__chip[aria-pressed="true"] { background: var(--text-main); color: var(--surface-light); box-shadow: 0 10px 22px -12px color-mix(in srgb, var(--text-main) 80%, transparent); }
.coverage-check__chip[aria-pressed="true"]::before { scale: 0; }
.coverage-check__chip[aria-pressed="true"] svg { scale: 1; }

/* Map card: dotted paper, soft-cornered zones (fill + same-colour round-joined stroke) */
.coverage-check__map {
  position: relative; overflow: hidden; padding: 0.75rem; border-radius: var(--radius-2xl);
  background: radial-gradient(circle at 1px 1px, color-mix(in srgb, var(--text-muted) 22%, transparent) 1px, transparent 1.5px) 0 0 / 18px 18px, var(--surface-muted);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.coverage-check__caption { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 0.25rem 1rem; margin: 0.25rem 0.5rem 0.5rem; color: var(--text-muted); font: 500 0.6875rem/1.4 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.coverage-check__svg { display: block; width: 100%; height: auto; }
.coverage-check__zone { cursor: pointer; }
.coverage-check__shape, .coverage-check__glow { stroke-width: 14; stroke-linejoin: round; }
.coverage-check__shape {
  fill: color-mix(in srgb, var(--primary) 5%, var(--surface-light)); stroke: color-mix(in srgb, var(--primary) 5%, var(--surface-light));
  filter: drop-shadow(0 2px 3px color-mix(in srgb, var(--text-main) 10%, transparent)); transition: fill var(--dur-3), stroke var(--dur-3);
}
.coverage-check__zone:hover .coverage-check__shape { fill: color-mix(in srgb, var(--primary) 13%, var(--surface-light)); stroke: color-mix(in srgb, var(--primary) 13%, var(--surface-light)); }
.coverage-check__glow {
  fill: var(--coverage-check-fill); stroke: var(--coverage-check-fill); opacity: 0; transform: scale(0.9); transform-box: fill-box; transform-origin: center;
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring);
}
.coverage-check__zone.is-active .coverage-check__glow { opacity: 1; transform: none; }
.coverage-check__stop-a { stop-color: var(--primary); }
.coverage-check__stop-b { stop-color: color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)); }
.coverage-check__decor, .coverage-check__water-line { fill: none; stroke-linecap: round; stroke-linejoin: round; pointer-events: none; transition: stroke var(--dur-3); }
.coverage-check__decor { stroke: color-mix(in srgb, var(--primary-2) 38%, var(--surface-light)); stroke-width: 2.5; }
.coverage-check__decor--dots { stroke-width: 9; }
.coverage-check__water { fill: color-mix(in srgb, var(--primary) 16%, var(--surface-light)); pointer-events: none; transition: fill var(--dur-3); }
.coverage-check__water-line { stroke: color-mix(in srgb, var(--primary) 30%, var(--surface-light)); stroke-width: 3; }
.coverage-check__zone.is-active .coverage-check__decor, .coverage-check__zone.is-active .coverage-check__water-line { stroke: color-mix(in srgb, var(--surface-light) 35%, transparent); }
.coverage-check__zone.is-active .coverage-check__water { fill: color-mix(in srgb, var(--surface-light) 22%, transparent); }
.coverage-check__name { fill: var(--text-main); font: 600 13px var(--font-display); letter-spacing: -0.01em; text-anchor: middle; pointer-events: none; transition: fill var(--dur-3); }
.coverage-check__zone.is-active .coverage-check__name { fill: var(--text-inverse); }

/* Hover tooltip: response time (mouse preview; the result card repeats it) */
.coverage-check__tip { opacity: 0; translate: 0 4px; pointer-events: none; transition: opacity var(--dur-2), translate var(--dur-3) var(--ease-out); }
.coverage-check__zone:hover .coverage-check__tip { opacity: 1; translate: 0 0; }
.coverage-check__tip rect { fill: var(--text-main); }
.coverage-check__tip text { fill: var(--surface-light); font: 600 10px var(--font-mono); text-anchor: middle; }

/* Pin: dropped by script; squashes on landing, then a ground ripple */
.coverage-check__pin { visibility: hidden; pointer-events: none; }
.coverage-check__pin.is-shown { visibility: visible; }
.coverage-check__drop { transform-box: fill-box; transform-origin: 50% 100%; }
.coverage-check__pin-body { fill: var(--text-main); stroke: var(--surface-light); stroke-width: 2.5; }
.coverage-check__pin-dot { fill: var(--surface-light); }
.coverage-check__shadow { fill: color-mix(in srgb, var(--surface-deep) 28%, transparent); }
.coverage-check__ring { fill: none; stroke: var(--surface-light); stroke-width: 2; opacity: 0; transform-box: fill-box; transform-origin: center; }

/* Result card (polite live region) */
.coverage-check__result { container-type: inline-size; border-radius: var(--radius-2xl); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-lg); }
.coverage-check__state { display: grid; grid-template-columns: auto minmax(0, 1fr); align-items: start; gap: 1rem; padding: 1.25rem; }
.coverage-check__state[hidden] { display: none; }
.coverage-check__badge { display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-lg); background: var(--surface-muted); color: var(--text-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.coverage-check__badge--yes { background: color-mix(in srgb, var(--success) 12%, var(--surface-light)); color: var(--success); box-shadow: none; }
.coverage-check__badge--no { background: color-mix(in srgb, var(--accent) 18%, var(--surface-light)); color: var(--warning); box-shadow: none; }
.coverage-check__badge--yes svg { stroke-width: 2.75; }
.coverage-check__result-title { margin: 0; font: 600 1.125rem/1.3 var(--font-display); letter-spacing: var(--tracking-tight); }
.coverage-check__result-text { margin: 0.375rem 0 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.5; }
.coverage-check__result-text strong { color: var(--text-main); font-weight: 600; }
.coverage-check__cta {
  grid-column: 1 / -1; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; height: 3rem; padding: 0 1.25rem; border-radius: var(--radius-full);
  background: var(--coverage-check-grad); color: var(--text-inverse); font: 600 0.9375rem var(--font-sans); white-space: nowrap; text-decoration: none;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 10px 24px -12px color-mix(in srgb, var(--primary) 80%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.coverage-check__cta svg { transition: transform var(--dur-3) var(--ease-spring); }
.coverage-check__cta:hover svg { transform: translateX(3px); }
.coverage-check__cta:active { transform: scale(0.97); }
.coverage-check__cta--ghost { background: var(--surface-muted); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle); }

/* Covered areas: always visible (the no-JS answer key) */
.coverage-check__list-title { margin: 0 0 0.5rem; color: var(--text-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.coverage-check__areas { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 12rem), 1fr)); column-gap: 1.5rem; margin: 0; padding: 0; list-style: none; }
.coverage-check__areas li { display: flex; justify-content: space-between; gap: 1rem; padding: 0.625rem 0; border-bottom: 1px dashed var(--border-subtle); font-size: 0.875rem; font-weight: 500; }
.coverage-check__areas span + span { color: var(--text-muted); font: 500 0.8125rem var(--font-mono); }

@container (min-width: 32rem) {
  .coverage-check__state { grid-template-columns: auto minmax(0, 1fr) auto; align-items: center; }
  .coverage-check__cta { grid-column: auto; }
}
@media (hover: none) {
  .coverage-check__hint, .coverage-check__tip { display: none; }
}
@media (min-width: 1024px) {
  .coverage-check__inner {
    grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr); grid-template-rows: auto auto 1fr auto;
    grid-template-areas: "head map" "form map" "result map" ". list"; gap: 1.75rem 3.5rem; align-items: start;
  }
}
```

## JS

```js
const EASE = 'cubic-bezier(0.16, 1, 0.3, 1)';
const SHAKE = { transform: ['translateX(0)', 'translateX(-6px)', 'translateX(5px)', 'translateX(-3px)', 'translateX(0)'] };
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
let uid = 0;

document.querySelectorAll('[data-coverage-check]').forEach((root) => {
  const $ = (s) => root.querySelector(s);
  const form = $('.coverage-check__form'), zip = form.elements.zip, error = $('.coverage-check__error');
  const result = $('.coverage-check__result'), pin = $('.coverage-check__pin');
  const chips = [...root.querySelectorAll('.coverage-check__chip')], zones = [...root.querySelectorAll('.coverage-check__zone')];
  const byZip = new Map(chips.flatMap((chip) => chip.dataset.zips.split(' ').map((code) => [code, chip])));
  const id = `coverage-check-${++uid}`;

  // Our own validation message, plus unique ids per instance for it and for this map's gradient
  form.noValidate = true;
  error.id = `${id}-error`;
  zip.setAttribute('aria-describedby', error.id);
  $('.coverage-check__grad').id = `${id}-grad`;
  root.style.setProperty('--coverage-check-fill', `url(#${id}-grad)`);

  // Result card: swap the state, fill its slots, slide it in (the card is the polite live region)
  const show = (state, slots) => {
    root.querySelectorAll('.coverage-check__state').forEach((el) => { el.hidden = !el.classList.contains(`coverage-check__state--${state}`); });
    Object.entries(slots).forEach(([key, value]) => root.querySelectorAll(`[data-slot="${key}"]`).forEach((el) => { el.textContent = value; }));
    if (!reduce.matches) result.animate({ opacity: [0, 1], transform: ['translateY(0.75rem)', 'none'] }, { duration: 480, easing: EASE });
  };

  // A neighbourhood: press its chip, bloom its zone, drop the pin on it
  const select = (chip) => {
    chips.forEach((c) => c.setAttribute('aria-pressed', String(c === chip)));
    zones.forEach((zone) => zone.classList.toggle('is-active', zone.dataset.zone === chip?.dataset.zone));
    pin.classList.toggle('is-shown', Boolean(chip));
    if (!chip) return;
    pin.setAttribute('transform', `translate(${zones.find((zone) => zone.dataset.zone === chip.dataset.zone).dataset.pin})`);
    if (!reduce.matches) {
      pin.querySelector('.coverage-check__drop').animate([
        { transform: 'translateY(-64px)', opacity: 0 },
        { transform: 'translateY(0) scale(1.1, 0.86)', opacity: 1, offset: 0.55 },
        { transform: 'translateY(-9px) scale(0.97, 1.04)', offset: 0.78 },
        { transform: 'none' },
      ], { duration: 760, easing: 'cubic-bezier(0.33, 0, 0.2, 1)' });
      pin.querySelector('.coverage-check__ring').animate({ transform: ['scale(0.3)', 'scale(2.8)'], opacity: [0.9, 0] }, { duration: 900, delay: 380, easing: EASE });
    }
    show('yes', { area: chip.textContent.trim(), next: chip.dataset.next, eta: chip.dataset.eta });
  };

  const setError = (message) => {
    error.textContent = message;
    if (message) zip.setAttribute('aria-invalid', 'true'); else zip.removeAttribute('aria-invalid');
  };

  // One submit handler: a chip (the submitter) or a ZIP lookup; an unknown ZIP gets the waitlist
  form.addEventListener('submit', (e) => {
    e.preventDefault(); // Demo: answered locally. Without JS, /coverage answers the same GET
    const chip = e.submitter?.closest('.coverage-check__chip');
    setError('');
    if (chip) { select(chip); return; }
    const code = zip.value.trim();
    if (!/^\d{5}$/.test(code)) {
      setError('Enter a 5-digit ZIP code, like 62702.');
      if (!reduce.matches) $('.coverage-check__field').animate(SHAKE, { duration: 400, easing: 'cubic-bezier(0.36, 0.07, 0.19, 0.97)' });
      zip.focus();
      return;
    }
    const match = byZip.get(code);
    select(match);
    if (!match) show('no', { zip: code });
  });
  zip.addEventListener('input', () => { if (zip.hasAttribute('aria-invalid')) setError(''); });

  // Mouse convenience: clicking a zone does what its chip does (the chips stay the accessible controls)
  $('.coverage-check__map').addEventListener('click', (e) => {
    const zone = e.target.closest('.coverage-check__zone');
    if (zone) select(chips.find((chip) => chip.dataset.zone === zone.dataset.zone));
  });
});
```

## Notes

- Accessibility model: the ZIP field has a visible label, a pattern check whose message is linked by `aria-describedby` (unique id per instance) with `aria-invalid`, and a shake. The neighbourhoods are toggle buttons (`aria-pressed`) in a labelled group, and they are the only controls for areas. The map, zones, pin and tooltips are `aria-hidden`; clicking a zone is a mouse shortcut for its chip. The result card is a polite live region, so "Yes! Northside is covered. Next available: Today 3–5pm…" is read once per answer.
- Without JS the form GETs `/coverage?zip=…`. Each chip is a submit button (`name="area"`, `formnovalidate`), so picking a neighbourhood also works without JS, and the "Areas we cover" list with every ZIP is always visible. Nothing is hidden at load, so nothing flashes.
- Reduced motion: no pin drop, ripple, card slide or shake; the zone fill, chip check and tooltip switch instantly through the motion tokens. The response time shown on hover is repeated in the result card, so touch and keyboard users get it too; tooltips are off where `hover: none`.
- Contrast: zone names on the gradient fill (`--primary` → teal deepened with 30% `--surface-deep`) are ≥ 4.9:1, tooltip text on `--text-main` is ≥ 13:1, and the results use `--text-main`/`--text-muted` on white (≥ 4.8:1).
- To adapt: zones are polygons in a 480×360 `viewBox`, softened by a round-joined stroke of the same colour, and each pairs with a chip through `data-zone`. ZIPs, next opening and response time live on the chips (`data-zips`, `data-next`, `data-eta`); swap them for your coverage API. The individual `translate`/`scale` properties and `:has()` style the tooltip and field focus, with plain fallbacks.
