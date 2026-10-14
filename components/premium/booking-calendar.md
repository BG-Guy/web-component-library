# Booking Calendar

A two-panel appointment picker on a light card: an APG date grid with availability dots, whose months slide in from the direction you travel, beside the chosen day's arrival windows. Choosing a day springs a gradient circle behind it and staggers its windows in as a radio group; picking a window raises a dark summary whose "Confirm booking" button morphs into a drawn check. On phones the calendar sits on top, the windows become swipeable rows and the summary turns into a sticky bottom bar. Depends on `tokens/variables.css`.

**Motion:** month slide + fade with an outgoing ghost (WAAPI, `--ease-out`) · selected-day circle spring (`--ease-spring`, `--dur-4`) + ring ripple (`--dur-5`) · window chips stagger in (`--dur-4`, `--stagger`) · summary rises (`--ease-spring`) · confirm button clip-path morph (`--ease-out`) + check draw.

## HTML

```html
<section class="book-cal" aria-labelledby="book-cal-title" data-book-cal>
  <div class="book-cal__inner">
    <header class="book-cal__head">
      <p class="book-cal__eyebrow">Online booking · Springfield</p>
      <h2 id="book-cal-title" class="book-cal__title">Pick a day. We'll handle the rest.</h2>
      <p class="book-cal__lede">Two-hour arrival windows, confirmed on the spot. The dots show how much room each day has left.</p>
      <ul class="book-cal__perks" role="list">
        <li><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Free rescheduling up to 2 hours before</li>
        <li><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Text reminder the evening before</li>
        <li><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>Flat-rate pricing, agreed upfront</li>
      </ul>
    </header>

    <form class="book-cal__card" action="/book" method="post" aria-labelledby="book-cal-title">
      <!-- Without JS: a native date field and a window select -->
      <fieldset class="book-cal__fallback">
        <legend class="book-cal__fallback-title">Request a visit</legend>
        <label class="book-cal__field">
          <span>Day</span>
          <input type="date" name="date" required>
        </label>
        <label class="book-cal__field">
          <span>Arrival window</span>
          <select name="slot" required>
            <option value="">Choose a window</option>
            <optgroup label="Morning"><option>8–10am</option><option>9–11am</option><option>10am–12pm</option><option>11am–1pm</option></optgroup>
            <optgroup label="Afternoon"><option>12–2pm</option><option>1–3pm</option><option>2–4pm</option><option>3–5pm</option></optgroup>
          </select>
        </label>
        <button class="book-cal__submit" type="submit">Request booking</button>
        <p class="book-cal__note">We confirm by text within the hour. Prefer to talk? Call <a href="tel:+15555550123">(555) 555-0123</a>.</p>
      </fieldset>

      <!-- With JS: calendar, windows and summary -->
      <div class="book-cal__app" hidden>
        <input type="hidden" name="date">

        <div class="book-cal__cal">
          <div class="book-cal__nav">
            <h3 class="book-cal__month" id="book-cal-month" aria-live="polite">Calendar</h3>
            <button class="book-cal__step" type="button" data-step="-1" aria-label="Previous month">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m15 6-6 6 6 6" /></svg>
            </button>
            <button class="book-cal__step" type="button" data-step="1" aria-label="Next month">
              <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m9 6 6 6-6 6" /></svg>
            </button>
          </div>
          <div class="book-cal__grid" role="grid" aria-labelledby="book-cal-month">
            <div class="book-cal__week book-cal__week--head" role="row">
              <span role="columnheader" aria-label="Sunday">Su</span><span role="columnheader" aria-label="Monday">Mo</span>
              <span role="columnheader" aria-label="Tuesday">Tu</span><span role="columnheader" aria-label="Wednesday">We</span>
              <span role="columnheader" aria-label="Thursday">Th</span><span role="columnheader" aria-label="Friday">Fr</span>
              <span role="columnheader" aria-label="Saturday">Sa</span>
            </div>
            <div class="book-cal__body"><div class="book-cal__weeks" role="rowgroup"></div></div>
          </div>
          <ul class="book-cal__legend" role="list">
            <li><span class="book-cal__key book-cal__key--many" aria-hidden="true"></span>Plenty of times</li>
            <li><span class="book-cal__key book-cal__key--few" aria-hidden="true"></span>Filling up</li>
            <li><span class="book-cal__key book-cal__key--none" aria-hidden="true"></span>Booked out</li>
            <li><span class="book-cal__key book-cal__key--today" aria-hidden="true"></span>Today</li>
          </ul>
        </div>

        <fieldset class="book-cal__times">
          <legend class="book-cal__times-title">
            <span class="book-cal__kicker">Arrival windows</span>
            <span class="book-cal__sel">Choose a day</span>
          </legend>
          <p class="book-cal__count"></p>
          <fieldset class="book-cal__group">
            <legend>
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M17 18a5 5 0 0 0-10 0M12 2v7M4.2 10.2l1.4 1.4M1 18h2M21 18h2M18.4 11.6l1.4-1.4M23 22H1M8 6l4-4 4 4" /></svg>
              Morning
            </legend>
            <div class="book-cal__chips" data-group="morning"></div>
          </fieldset>
          <fieldset class="book-cal__group">
            <legend>
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="4" /><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" /></svg>
              Afternoon
            </legend>
            <div class="book-cal__chips" data-group="afternoon"></div>
          </fieldset>
        </fieldset>

        <div class="book-cal__summary" hidden>
          <span class="book-cal__summary-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /></svg>
          </span>
          <div class="book-cal__summary-text">
            <p class="book-cal__summary-label">Your visit</p>
            <p class="book-cal__when"></p>
            <p class="book-cal__meta">Plumbing visit · free estimate on arrival</p>
          </div>
          <button class="book-cal__confirm" type="submit">
            <span class="book-cal__confirm-label">Confirm<span class="book-cal__wide"> booking</span></span>
            <svg class="book-cal__tick" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" pathLength="1" /></svg>
          </button>
        </div>

        <p class="book-cal__live" aria-live="polite"></p>
      </div>
    </form>
  </div>
</section>
```

## CSS

```css
/* Section: a soft daylight wash behind a white card */
.book-cal {
  --book-cal-pad: 1rem;
  --book-cal-disc: 2.75rem;
  background:
    radial-gradient(55% 45% at 85% 0%, color-mix(in srgb, var(--primary-2) 12%, transparent), transparent 70%),
    radial-gradient(45% 40% at 5% 15%, color-mix(in srgb, var(--primary) 9%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
}
.book-cal__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(3.5rem, 8vw, 6rem) var(--gutter); }
.book-cal__head { max-width: 36rem; margin-bottom: clamp(1.75rem, 4vw, 2.75rem); }
.book-cal__eyebrow, .book-cal__kicker, .book-cal__summary-label { font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.book-cal__eyebrow { margin: 0; color: var(--primary); font-size: 0.75rem; }
.book-cal__title { margin: 0.875rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.6vw, 3rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.book-cal__lede { margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.book-cal__perks { display: flex; flex-wrap: wrap; gap: 0.625rem 1.5rem; margin: 1.5rem 0 0; padding: 0; list-style: none; font-size: 0.9375rem; font-weight: 500; }
.book-cal__perks li { display: flex; align-items: center; gap: 0.5rem; }
.book-cal__perks svg { flex: none; padding: 0.1875rem; border-radius: 50%; background: color-mix(in srgb, var(--primary) 12%, transparent); color: var(--primary); stroke-width: 2.5; }
:where(.book-cal) svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.book-cal :is(button, a):focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Card */
.book-cal__card {
  position: relative; margin: 0; padding: var(--book-cal-pad); border-radius: var(--radius-2xl);
  background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}

/* No-JS fields */
.book-cal__fallback { display: grid; gap: 1rem; min-width: 0; margin: 0; padding: 0.5rem; border: 0; }
.book-cal__fallback[hidden] { display: none; }
.book-cal__fallback-title { float: left; grid-column: 1 / -1; padding: 0; font: 600 1.375rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.book-cal__field { display: grid; gap: 0.375rem; font-size: 0.875rem; font-weight: 600; }
.book-cal__field :is(input, select) {
  min-width: 0; height: 3rem; padding: 0 0.875rem; border: 1px solid var(--border-subtle); border-radius: var(--radius-lg);
  background: var(--surface-muted); color: var(--text-main); font: 500 1rem var(--font-sans);
  transition: border-color var(--dur-2), background-color var(--dur-2), box-shadow var(--dur-2);
}
.book-cal__field :is(input, select):focus-visible { outline: 2px solid transparent; border-color: var(--primary); background: var(--surface-light); box-shadow: var(--focus-ring); }
.book-cal__submit {
  height: 3rem; padding: 0 1.5rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--text-main); color: var(--surface-light); font: 600 0.9375rem var(--font-sans);
  box-shadow: var(--highlight-inverse), 0 12px 28px -14px color-mix(in srgb, var(--text-main) 80%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.book-cal__submit:active { transform: scale(0.97); }
.book-cal__note { grid-column: 1 / -1; margin: 0; color: var(--text-muted); font-size: 0.8125rem; line-height: 1.5; }
.book-cal__note a { color: var(--primary); font-weight: 600; }

/* JS is on: keep the fallback invisible while the script boots; it reappears after 3s if the script never runs */
@media (scripting: enabled) {
  .book-cal:not(.book-cal--ready) .book-cal__fallback { animation: book-cal-failsafe 1ms 3s both; }
}

/* App: calendar, windows, summary */
.book-cal__app { display: grid; gap: 1.75rem; }
.book-cal__app[hidden] { display: none; }

.book-cal__nav { display: flex; align-items: center; gap: 0.375rem; margin-bottom: 0.5rem; }
.book-cal__month { flex: 1; margin: 0; font: 600 1.375rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.book-cal__month span { color: var(--text-muted); font: 500 0.875rem var(--font-mono); letter-spacing: 0; }
.book-cal__step {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: background-color var(--dur-2), color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.book-cal__step:hover { background: var(--surface-muted); }
.book-cal__step:active { transform: scale(0.9); }
.book-cal__step[aria-disabled="true"] { cursor: default; background: transparent; color: color-mix(in srgb, var(--text-muted) 55%, transparent); transform: none; }

/* Date grid */
.book-cal__week { display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); }
.book-cal__week--head { padding-block: 0.5rem; color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; text-align: center; }
.book-cal__body { position: relative; }
.book-cal__weeks { display: grid; gap: 0.125rem; }
.book-cal__weeks.is-ghost { position: absolute; inset: 0 0 auto; pointer-events: none; }
.book-cal__day { display: grid; place-items: center; padding: 0.125rem; cursor: pointer; -webkit-tap-highlight-color: transparent; }
.book-cal__day:focus-visible { outline: 2px solid transparent; }
.book-cal__disc {
  position: relative; isolation: isolate; display: grid; place-items: center; width: 100%; max-width: var(--book-cal-disc); aspect-ratio: 1; border-radius: 50%;
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.book-cal__disc::before { /* the selection circle */
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit;
  background: linear-gradient(135deg, var(--primary), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep))); box-shadow: var(--shadow-glow);
  opacity: 0; transform: scale(0.3);
  transition: transform var(--dur-4) var(--ease-spring), opacity var(--dur-2) var(--ease-out);
}
.book-cal__disc::after { /* ripple ring */
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; opacity: 0;
  box-shadow: 0 0 0 2px color-mix(in srgb, var(--primary) 70%, var(--primary-2));
}
.book-cal__num { font: 600 0.9375rem/1 var(--font-display); font-variant-numeric: tabular-nums; transition: color var(--dur-3); }
.book-cal__dots { position: absolute; bottom: 16%; display: flex; gap: 0.1875rem; }
.book-cal__dots i { width: 0.25rem; height: 0.25rem; border-radius: 50%; background: var(--primary); transition: background-color var(--dur-3); }
.book-cal__day[data-avail="few"] .book-cal__dots i { background: var(--warning); }
.book-cal__day:not([aria-disabled]):hover .book-cal__disc { background: var(--surface-muted); transform: translateY(-1px); }
.book-cal__day:not([aria-disabled]):active .book-cal__disc { transform: scale(0.9); }
.book-cal__day[aria-disabled] { cursor: default; }
.book-cal__day[data-avail="none"] .book-cal__num { color: var(--text-muted); text-decoration: line-through; text-decoration-color: color-mix(in srgb, var(--text-muted) 60%, transparent); }
.book-cal__day[data-avail="past"] .book-cal__num { color: color-mix(in srgb, var(--text-muted) 55%, var(--surface-light)); font-weight: 500; }
.book-cal__day[data-today] .book-cal__disc { box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--primary) 60%, transparent); }
.book-cal__day[data-today] .book-cal__num { color: var(--primary); }
.book-cal__day[aria-selected="true"] .book-cal__num { color: var(--text-inverse); }
.book-cal__day[aria-selected="true"] .book-cal__dots i { background: var(--text-inverse); }
.book-cal__day[aria-selected="true"] .book-cal__disc::before { opacity: 1; transform: scale(1); }
.book-cal__day[aria-selected="true"] .book-cal__disc::after { animation: book-cal-ring var(--dur-5) var(--ease-out); }
.book-cal__day:focus-visible .book-cal__disc { box-shadow: var(--focus-ring); }

/* Legend */
.book-cal__legend { display: flex; flex-wrap: wrap; gap: 0.5rem 1.125rem; margin: 1rem 0 0; padding: 1rem 0 0; border-top: 1px dashed var(--border-subtle); list-style: none; color: var(--text-muted); font-size: 0.75rem; }
.book-cal__legend li { display: inline-flex; align-items: center; gap: 0.5rem; }
.book-cal__key { width: 0.9375rem; height: 0.9375rem; }
.book-cal__key--many { background: radial-gradient(circle, var(--primary) 0.125rem, transparent 0.14rem) 0 50% / 0.3125rem 100% repeat-x; }
.book-cal__key--few { background: radial-gradient(circle, var(--warning) 0.125rem, transparent 0.14rem) 50% 50% / 0.3125rem 100% no-repeat; }
.book-cal__key--none { background: linear-gradient(var(--text-muted), var(--text-muted)) 50% 50% / 100% 1.5px no-repeat; }
.book-cal__key--today { border-radius: 50%; box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--primary) 60%, transparent); }

/* Arrival windows: one radio group in two sets */
.book-cal__times, .book-cal__group { min-width: 0; margin: 0; padding: 0; border: 0; }
.book-cal__times-title { display: grid; gap: 0.5rem; padding: 0; }
.book-cal__kicker { color: var(--text-muted); }
.book-cal__sel { font: 600 1.375rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.book-cal__count { margin: 0.375rem 0 0; color: var(--text-muted); font-size: 0.875rem; }
.book-cal__count strong { color: var(--text-main); font-weight: 600; }
.book-cal__group { margin-top: 1.25rem; }
.book-cal__group legend { display: flex; align-items: center; gap: 0.375rem; margin-bottom: 0.5rem; padding: 0; color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.book-cal__group legend svg { color: var(--primary); }
.book-cal__chips { /* phones: a swipeable row that bleeds to the card edge */
  display: flex; gap: 0.5rem; overflow-x: auto; overscroll-behavior-x: contain; scroll-snap-type: x mandatory; scrollbar-width: none;
  margin-inline: calc(var(--book-cal-pad) * -1); padding: 0.25rem var(--book-cal-pad) 0.75rem; scroll-padding-inline: var(--book-cal-pad);
}
.book-cal__chips::-webkit-scrollbar { display: none; }
.book-cal__chip {
  position: relative; flex: none; display: grid; align-content: center; justify-items: start; gap: 0.3125rem;
  min-width: 7.75rem; min-height: 3.75rem; padding: 0.625rem 2.25rem 0.625rem 0.875rem; border-radius: var(--radius-xl); cursor: pointer; scroll-snap-align: start;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: background-color var(--dur-3), color var(--dur-3), box-shadow var(--dur-3), transform var(--dur-4) var(--ease-spring);
  animation: book-cal-in var(--dur-4) var(--ease-out) calc(var(--book-cal-i, 0) * var(--stagger)) backwards;
}
.book-cal__chip input { position: absolute; opacity: 0; pointer-events: none; }
.book-cal__time { font-size: 0.9375rem; font-weight: 600; font-variant-numeric: tabular-nums; white-space: nowrap; }
.book-cal__chip small { color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.04em; text-transform: uppercase; white-space: nowrap; transition: opacity var(--dur-2); }
.book-cal__check { position: absolute; right: 0.75rem; top: 50%; translate: 0 -50%; scale: 0; transition: scale var(--dur-4) var(--ease-spring); }
.book-cal__chip:hover { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 45%, var(--border-subtle)), var(--shadow-md); }
.book-cal__chip:active { transform: scale(0.95); }
.book-cal__chip:has(:checked) { background: var(--text-main); color: var(--surface-light); box-shadow: var(--highlight-inverse), 0 8px 18px -10px color-mix(in srgb, var(--text-main) 90%, transparent); }
.book-cal__chip:has(:checked) small { opacity: 0; }
.book-cal__chip:has(:checked) .book-cal__check { scale: 1; }
.book-cal__chip:has(:focus-visible) { outline: 2px solid transparent; box-shadow: var(--focus-ring), inset 0 0 0 1px var(--primary); }
.book-cal__chip:has(:disabled) { cursor: not-allowed; background: var(--surface-muted); box-shadow: none; transform: none; }
.book-cal__chip:has(:disabled) .book-cal__time { color: var(--text-muted); font-weight: 500; text-decoration: line-through; }

/* Summary: a deep card that rises in; on phones it sticks to the bottom of the screen */
.book-cal__summary {
  position: sticky; bottom: max(0.75rem, env(safe-area-inset-bottom)); z-index: var(--z-sticky); container-type: inline-size;
  display: flex; align-items: center; gap: 0.875rem; padding: 0.625rem 0.625rem 0.625rem 1rem; border-radius: var(--radius-2xl);
  background:
    radial-gradient(120% 160% at 0% 0%, color-mix(in srgb, var(--primary) 34%, transparent), transparent 55%),
    radial-gradient(100% 140% at 100% 100%, color-mix(in srgb, var(--primary-2) 24%, transparent), transparent 60%),
    var(--surface-deep);
  color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 24px 48px -20px color-mix(in srgb, var(--surface-deep) 80%, transparent);
  animation: book-cal-rise var(--dur-4) var(--ease-spring) backwards;
}
.book-cal__summary[hidden] { display: none; }
.book-cal__summary.is-done { box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--success) 70%, transparent), var(--highlight-inverse), 0 24px 48px -20px color-mix(in srgb, var(--success) 45%, transparent); }
.book-cal__summary-icon { flex: none; display: none; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-xl); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); }
.book-cal__summary-text { flex: 1; min-width: 0; }
.book-cal__summary-label { margin: 0; color: var(--text-inverse-muted); }
.book-cal__when { margin: 0.375rem 0 0; font: 600 1rem/1.25 var(--font-display); letter-spacing: var(--tracking-tight); }
.book-cal__meta { display: none; margin: 0.25rem 0 0; color: var(--text-inverse-muted); font-size: 0.8125rem; }
.book-cal__wide { display: none; }
@container (min-width: 24rem) {
  .book-cal__wide { display: inline; }
  .book-cal__summary-icon { display: grid; }
  .book-cal__meta { display: block; }
}

/* Confirm: the white pill clips down to a green circle and a check draws in */
.book-cal__confirm {
  position: relative; isolation: isolate; flex: none; display: grid; place-items: center; height: 3rem; padding: 0 1.25rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: none; color: var(--text-main); font: 600 0.9375rem var(--font-sans);
  transition: transform var(--dur-3) var(--ease-spring);
}
.book-cal__confirm::before {
  content: ""; position: absolute; inset: 0; z-index: -1; background: var(--surface-light); clip-path: inset(0 round 1.5rem);
  transition: clip-path var(--dur-4) var(--ease-out), background-color var(--dur-3);
}
.book-cal__confirm:active { transform: scale(0.96); }
.book-cal .book-cal__confirm:focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; box-shadow: none; }
.book-cal__confirm-label { grid-area: 1 / 1; white-space: nowrap; transition: opacity var(--dur-2), filter var(--dur-3), scale var(--dur-3) var(--ease-out); }
.book-cal__tick { grid-area: 1 / 1; color: var(--text-inverse); stroke-width: 2.75; stroke-dasharray: 1; stroke-dashoffset: 1; transition: stroke-dashoffset var(--dur-4) var(--ease-out); }
.book-cal__summary.is-done .book-cal__confirm { cursor: default; transform: none; }
.book-cal__summary.is-done .book-cal__confirm::before { clip-path: inset(0 calc(50% - 1.5rem) round 1.5rem); background: var(--success); }
.book-cal__summary.is-done .book-cal__confirm-label { opacity: 0; filter: blur(4px); scale: 0.85; }
.book-cal__summary.is-done .book-cal__tick { stroke-dashoffset: 0; transition-delay: var(--dur-2); }

.book-cal__sr, .book-cal__live { position: absolute; width: 1px; height: 1px; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

/* Tablet and up: calendar left, windows right, summary docked under the windows */
@media (min-width: 768px) {
  .book-cal { --book-cal-pad: 1.75rem; }
  .book-cal__fallback { grid-template-columns: 1fr 1fr auto; align-items: end; padding: 0.75rem; }
  .book-cal__app { grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); grid-template-rows: auto 1fr; gap: 0; }
  .book-cal__cal { grid-row: span 2; padding-right: var(--book-cal-pad); border-right: 1px solid var(--border-subtle); }
  .book-cal__times, .book-cal__summary { margin-left: var(--book-cal-pad); }
  .book-cal__summary { position: relative; bottom: auto; align-self: end; display: grid; grid-template-columns: auto minmax(0, 1fr); gap: 1rem 0.875rem; margin-top: 1.5rem; padding: 1rem; }
  .book-cal__summary-icon { display: grid; }
  .book-cal__meta { display: block; }
  .book-cal__wide { display: inline; }
  .book-cal__confirm { grid-column: 1 / -1; }
  .book-cal__chips { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); margin: 0; padding: 0; overflow: visible; }
  .book-cal__chip { min-width: 0; }
}
@media (min-width: 1024px) {
  .book-cal__inner { display: grid; grid-template-columns: minmax(0, 0.8fr) minmax(0, 2fr); gap: 3.5rem; align-items: start; }
  .book-cal__head { position: sticky; top: 2rem; margin: 0; padding-top: 1rem; }
}

@media (prefers-reduced-motion: reduce) {
  .book-cal__chip, .book-cal__summary, .book-cal__disc::after { animation: none !important; }
}
@keyframes book-cal-in { from { opacity: 0; transform: translateY(0.5rem) scale(0.96); } }
@keyframes book-cal-rise { from { opacity: 0; transform: translateY(1rem) scale(0.97); } }
@keyframes book-cal-ring { from { opacity: 0.6; transform: scale(1); } to { opacity: 0; transform: scale(1.6); } }
@keyframes book-cal-failsafe { from { visibility: hidden; } to { visibility: visible; } }
```

## JS

```js
const SLOTS = { morning: ['8–10am', '9–11am', '10am–12pm', '11am–1pm'], afternoon: ['12–2pm', '1–3pm', '2–4pm', '3–5pm'] };
const ALL = [...SLOTS.morning, ...SLOTS.afternoon];
const SAY = { many: 'plenty of times', few: 'filling up', none: 'booked out', past: 'unavailable' };
const DOTS = { many: 3, few: 1 };
const CHECK = '<svg class="book-cal__check" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>';
const EASE = 'cubic-bezier(0.16, 1, 0.3, 1)';
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const fmt = (d, opts) => d.toLocaleDateString('en-US', opts);
const rand = (n) => { const x = Math.sin(n) * 43758.5453; return x - Math.floor(x); };
// Move by days, or by months keeping the day number (clamped to the month's length)
const shift = (d, days, months = 0) => {
  const first = new Date(d.getFullYear(), d.getMonth() + months, 1);
  const last = new Date(first.getFullYear(), first.getMonth() + 1, 0).getDate();
  return new Date(first.getFullYear(), first.getMonth(), Math.min(d.getDate(), last) + days);
};
let count = 0;

document.querySelectorAll('[data-book-cal]').forEach((root) => {
  const $ = (s) => root.querySelector(s);
  const app = $('.book-cal__app'), weeks = $('.book-cal__weeks'), month = $('.book-cal__month');
  const fallback = $('.book-cal__fallback'), summary = $('.book-cal__summary'), confirm = $('.book-cal__confirm');
  const [prev, next] = root.querySelectorAll('.book-cal__step');
  const now = new Date(), today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const min = new Date(today.getFullYear(), today.getMonth(), 1);
  const max = new Date(today.getFullYear(), today.getMonth() + 3, 0); // bookable: this month + 2
  let view = min, active = today, picked = null, ready = false;

  // Take over from the native fields (a disabled fieldset doesn't submit); unique ids per instance
  month.id = `book-cal-${++count}-month`;
  $('[role="grid"]').setAttribute('aria-labelledby', month.id);
  fallback.disabled = fallback.hidden = true;
  app.hidden = false;
  root.classList.add('book-cal--ready');
  const say = (text) => { if (ready) $('.book-cal__live').textContent = text; };
  // Seeded demo availability: stable per date, Sundays closed, nothing in the past
  const open = (d) => {
    if (d < today || d.getDay() === 0) return [];
    const k = d.getFullYear() * 400 + d.getMonth() * 32 + d.getDate(), r = rand(k);
    const n = r < 0.16 ? 0 : r < 0.42 ? 1 + Math.floor(rand(k + 0.3) * 3) : 4 + Math.floor(rand(k + 0.6) * 5);
    return ALL.map((s, i) => [rand(k * 8 + i), s]).sort((a, b) => a[0] - b[0]).slice(0, n).map((p) => p[1]);
  };
  const level = (d) => { const n = open(d).length; return d < today ? 'past' : n > 3 ? 'many' : n ? 'few' : 'none'; };
  const cell = (d) => weeks.querySelector(`[data-day="${d.getDate()}"]`);
  const rove = () => weeks.querySelectorAll('.book-cal__day').forEach((c) => { c.tabIndex = +c.dataset.day === active.getDate() ? 0 : -1; });
  // Build the month; on a month change the old grid leaves as a ghost while the new one slides in
  const render = (dir) => {
    const y = view.getFullYear(), m = view.getMonth(), name = fmt(view, { month: 'long' });
    const cells = Array(view.getDay()).fill('<div role="gridcell"></div>');
    for (let n = 1; n <= new Date(y, m + 1, 0).getDate(); n++) {
      const d = new Date(y, m, n), lvl = level(d), isToday = +d === +today;
      cells.push(`<div role="gridcell" class="book-cal__day" data-day="${n}" data-avail="${lvl}" tabindex="-1" aria-selected="${+d === +picked}"${DOTS[lvl] ? '' : ' aria-disabled="true"'}${isToday ? ' data-today' : ''}>`
        + `<span class="book-cal__disc"><span class="book-cal__num">${n}</span><span class="book-cal__dots" aria-hidden="true">${'<i></i>'.repeat(DOTS[lvl] || 0)}</span></span>`
        + `<span class="book-cal__sr"> ${name}${isToday ? ', today' : ''}, ${SAY[lvl]}</span></div>`);
    }
    while (cells.length % 7) cells.push('<div role="gridcell"></div>');
    if (dir && !reduce.matches) {
      const ghost = Object.assign(weeks.cloneNode(true), { inert: true, ariaHidden: 'true', className: 'book-cal__weeks is-ghost' });
      weeks.after(ghost);
      ghost.animate({ opacity: [1, 0], transform: ['none', `translateX(${-dir * 3}rem)`] }, { duration: 320, easing: EASE }).onfinish = () => ghost.remove();
      weeks.animate({ opacity: [0, 1], transform: [`translateX(${dir * 3}rem)`, 'none'] }, { duration: 560, easing: EASE });
      month.animate({ opacity: [0, 1], transform: [`translateY(${dir * 0.5}rem)`, 'none'] }, { duration: 420, easing: EASE });
    }
    let rows = '';
    for (let i = 0; i < cells.length; i += 7) rows += `<div class="book-cal__week" role="row">${cells.slice(i, i + 7).join('')}</div>`;
    weeks.innerHTML = rows;
    month.innerHTML = `${name} <span>${y}</span>`;
    prev.setAttribute('aria-disabled', String(+view <= +min));
    next.setAttribute('aria-disabled', String(+new Date(y, m + 1, 1) > +max));
    rove();
  };
  // Move the roving focus (clamped to the bookable range), re-rendering when the month changes
  const go = (d, focus) => {
    active = d < min ? min : d > max ? max : d;
    const dir = Math.sign((active.getFullYear() - view.getFullYear()) * 12 + active.getMonth() - view.getMonth());
    if (dir) { view = new Date(active.getFullYear(), active.getMonth(), 1); render(dir); } else rove();
    if (focus) cell(active).focus();
  };
  // Choose a day: the circle springs in, its windows stagger in as radios, the count is announced
  const pick = (d) => {
    const c = cell(d);
    if (!c || c.hasAttribute('aria-disabled')) return;
    weeks.querySelector('[aria-selected="true"]')?.setAttribute('aria-selected', 'false');
    c.setAttribute('aria-selected', 'true');
    picked = d;
    app.querySelector('[name="date"]').value = d.toLocaleDateString('en-CA'); // YYYY-MM-DD
    const free = new Set(open(d)), long = fmt(d, { weekday: 'long', month: 'long', day: 'numeric' });
    $('.book-cal__sel').textContent = long;
    $('.book-cal__count').innerHTML = `<strong>${free.size} of ${ALL.length}</strong> windows open · 2-hour arrival`;
    let i = 0;
    root.querySelectorAll('.book-cal__chips').forEach((list) => {
      list.innerHTML = SLOTS[list.dataset.group].map((s) => `<label class="book-cal__chip" style="--book-cal-i: ${i++}">`
        + `<input type="radio" name="slot" value="${s}" required${free.has(s) ? '' : ' disabled'}><span class="book-cal__time">${s}</span>`
        + `<small>${free.has(s) ? (free.size === 1 ? 'Last one' : 'Open') : 'Taken'}</small>${CHECK}</label>`).join('');
      list.scrollLeft = 0;
    });
    summary.hidden = true;
    say(`${long}: ${free.size} arrival windows open.`);
  };
  // Grid keyboard (APG date grid): arrows, Home/End within the week, PageUp/PageDown by month (+Shift: year)
  weeks.addEventListener('keydown', (e) => {
    const days = { ArrowLeft: -1, ArrowRight: 1, ArrowUp: -7, ArrowDown: 7, Home: -active.getDay(), End: 6 - active.getDay() }[e.key];
    const months = { PageUp: -1, PageDown: 1 }[e.key];
    if (days !== undefined) go(shift(active, days), true);
    else if (months) go(shift(active, 0, months * (e.shiftKey ? 12 : 1)), true);
    else if (e.key === 'Enter' || e.key === ' ') pick(active);
    else return;
    e.preventDefault();
  });
  weeks.addEventListener('click', (e) => {
    const c = e.target.closest('.book-cal__day');
    if (c) { go(new Date(view.getFullYear(), view.getMonth(), +c.dataset.day)); pick(active); }
  });
  [prev, next].forEach((b) => b.addEventListener('click', () => {
    if (b.getAttribute('aria-disabled') !== 'true') go(shift(active, 0, +b.dataset.step));
  }));
  // Choosing a window raises the summary; a confirmed booking morphs the button into a check
  const setDone = (on) => {
    summary.classList.toggle('is-done', on);
    $('.book-cal__summary-label').textContent = on ? "You're booked" : 'Your visit';
    confirm.setAttribute('aria-label', on ? 'Booking confirmed' : 'Confirm booking');
  };
  app.addEventListener('change', (e) => {
    if (e.target.name !== 'slot') return;
    $('.book-cal__when').textContent = `${fmt(picked, { weekday: 'short', month: 'short', day: 'numeric' })} · ${e.target.value}`;
    setDone(false);
    summary.hidden = false;
  });
  $('form').addEventListener('submit', (e) => {
    e.preventDefault(); // Demo only: POST new FormData(form) to form.action, then morph on success
    if (summary.classList.contains('is-done')) return;
    setDone(true);
    say(`Booking confirmed for ${$('.book-cal__when').textContent}. We'll text you a reminder.`);
  });
  // Start on the first day with room, so windows show straight away
  while (!open(active).length && active < max) active = shift(active, 1);
  view = new Date(active.getFullYear(), active.getMonth(), 1);
  render(0);
  pick(active);
  ready = true;
});
```

## Notes

- APG date grid: one roving `tabindex` stop; ←/→/↑/↓ move by day and week, Home/End jump to the week's ends, PageUp/PageDown change month (Shift for a year), Enter/Space choose. Fully booked and past days stay focusable with `aria-disabled`; each cell carries hidden text ("14 October, today, filling up"), the month heading is `aria-live`, and the windows are one native radio group inside `fieldset`/`legend`. A polite live region reports each day's open count and the confirmation.
- Without JS the form shows a native date input and a window `<select>`, and it submits to `/book`. With JS, a `scripting: enabled` rule hides the fallback while the module boots, and a 3s CSS failsafe brings it back if the script never runs. The fallback fieldset is then `disabled`, so only the calendar's hidden `date` and the `slot` radio submit.
- Reduced motion: the month ghost slide is skipped (the month swaps instantly), the ripple and the chip and summary entrances are off, and the token-driven springs and the morph become instant.
- Contrast: the summary text (`--text-inverse` on `--surface-deep` lit by ≤ 34% `--primary`) stays above 11:1, and its labels (`--text-inverse-muted`) above 6:1. The selected circle runs from `--primary` to a teal deepened with 30% `--surface-deep`, so its white numeral is ≥ 4.9:1 at every point. The availability dots (`--primary`, `--warning`) are ≥ 5:1, and only inactive past days drop below 4.5:1.
- The demo `submit` handler only plays the success state. Replace it with a `fetch(form.action, { method: 'post', body: new FormData(form) })` and morph on success. Availability comes from `open(date)`; swap the seeded function for your API's slots per day, keeping the same `SLOTS` labels.
- Uses `:has()`, container queries and the individual `scale`/`translate` properties. Older browsers lose the chips' check pop, and phones without container queries keep the compact summary bar.
