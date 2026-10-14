# Split-Flap Board

A Solari-style departures board announcing availability: rows such as "NEXT SLOT | TUE 09:00 | NORTHSIDE | ON TIME", where every character is a flap tile with top and bottom halves, mounted in a riveted housing on a dark station wall. The signature moment is the update: flaps cascade through a few intermediate characters, each top leaf folding down in 3D (rotateX) while a soft shadow falls across the lower half, the final leaf landing with a spring bounce, staggered left to right across the columns. The board rolls through upcoming slots every ~4s with a pause button, and "Check your area" sets the top row on demand. On phones each row folds into a 2×2 block of fields so the tiles stay legible at 320px. Depends on `tokens/variables.css`.

**Motion:** flap fold (top leaf `rotateX` 0 → -90°, ease-in, darkening) then land (bottom leaf 90° → 0°, `--ease-spring` on the final character) · cast shadow on the lower half · 30ms per-column and 80ms per-row stagger · board update every ~4s (2.6s dwell after the flaps settle), pausable and frozen off-screen · button lift and press (`--dur-2`, `--dur-1`).

## HTML

```html
<section class="split-flap" aria-labelledby="split-flap-title" data-split-flap
  data-split-flap-queue="PLUMBING|TUE 11:30|WESTLAKE|2 LEFT;HEATING|WED 08:00|RIVERSIDE|BOOKING;ELECTRIC|WED 14:00|NORTHSIDE|OPEN;AC REPAIR|THU 10:30|WESTLAKE|1 LEFT;DRAINS|THU 16:00|HILLCREST|OPEN;ROOFING|FRI 09:00|RIVERSIDE|ON TIME"
  data-split-flap-areas="WESTLAKE|THU 10:00|ON TIME;NORTHSIDE|TUE 09:00|ON TIME;RIVERSIDE|WED 15:30|2 LEFT;HILLCREST|FRI 08:00|1 LEFT;DOWNTOWN|TUE 13:00|OPEN">
  <div class="split-flap__inner">
    <header class="split-flap__head">
      <p class="split-flap__eyebrow">Live availability</p>
      <h2 id="split-flap-title" class="split-flap__title">Your next slot is on the board</h2>
      <p class="split-flap__lead">Real openings from our dispatch desk, updated through the day. Type your neighbourhood to see when we can be there.</p>
    </header>

    <div class="split-flap__stage">
      <div class="split-flap__board">
        <div class="split-flap__board-head">
          <p class="split-flap__board-title"><span class="split-flap__lamp" aria-hidden="true"></span>Departures · Springfield dispatch</p>
          <button class="split-flap__pause" type="button" aria-label="Pause board updates" aria-pressed="false" hidden>
            <svg class="split-flap__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
            <svg class="split-flap__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
          </button>
        </div>

        <div class="split-flap__table" role="table" aria-label="Next available slots">
          <div class="split-flap__row split-flap__row--head" role="row">
            <span class="split-flap__colhead" role="columnheader" style="--split-flap-n: 9"><span>Service</span></span>
            <span class="split-flap__colhead" role="columnheader" style="--split-flap-n: 9"><span>Time</span></span>
            <span class="split-flap__colhead" role="columnheader" style="--split-flap-n: 9"><span>Area</span></span>
            <span class="split-flap__colhead" role="columnheader" style="--split-flap-n: 8"><span>Status</span></span>
          </div>
          <div class="split-flap__row split-flap__row--pinned" role="row" data-split-flap-row>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">NEXT SLOT</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">TUE 09:00</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">NORTHSIDE</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 8">ON TIME</span>
          </div>
          <div class="split-flap__row" role="row" data-split-flap-row>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">PLUMBING</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">TUE 11:30</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">WESTLAKE</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 8">2 LEFT</span>
          </div>
          <div class="split-flap__row" role="row" data-split-flap-row>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">HEATING</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">WED 08:00</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">RIVERSIDE</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 8">BOOKING</span>
          </div>
          <div class="split-flap__row" role="row" data-split-flap-row>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">ELECTRIC</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">WED 14:00</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 9">NORTHSIDE</span>
            <span class="split-flap__cell" role="cell" style="--split-flap-n: 8">OPEN</span>
          </div>
        </div>
      </div>

      <form class="split-flap__check" action="#" method="get">
        <label class="split-flap__label">
          <span class="split-flap__label-text">Check your area</span>
          <input class="split-flap__input" name="area" list="split-flap-areas" placeholder="e.g. Westlake" autocomplete="off" required>
        </label>
        <button class="split-flap__btn" type="submit">Show my slot</button>
        <datalist id="split-flap-areas"><option value="Westlake"></option><option value="Northside"></option><option value="Riverside"></option><option value="Hillcrest"></option><option value="Downtown"></option></datalist>
        <p class="split-flap__sr split-flap__live" role="status"></p>
      </form>
    </div>
  </div>
</section>
```

## CSS

```css
/* Palette and tile geometry. Widths use ch, so the no-JS text and the JS tiles line up exactly */
.split-flap {
  --split-flap-board: #0d0d0f;
  --split-flap-flap: #1f1f23;
  --split-flap-ink: #f2efe6;
  --split-flap-amber: #ffb627;
  --split-flap-muted: color-mix(in srgb, var(--split-flap-ink) 62%, var(--split-flap-board));
  --split-flap-size: min(4.6vw, 1.125rem);
  --split-flap-w: calc(1ch + 0.22em);   /* tile width */
  --split-flap-gap: 0.08em;             /* gap between tiles */
  --split-flap-cell: calc(var(--split-flap-w) + var(--split-flap-gap));
  --split-flap-h: 1.36em;               /* tile height */
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(60% 45% at 50% 62%, color-mix(in srgb, var(--split-flap-amber) 9%, transparent), transparent 70%),
    linear-gradient(color-mix(in srgb, var(--split-flap-board) 70%, var(--split-flap-flap)), var(--split-flap-board));
  color: var(--split-flap-ink); font-family: var(--font-sans);
}
.split-flap__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.split-flap__head { max-width: 40rem; margin: 0 auto 2.75rem; text-align: center; }
.split-flap__eyebrow { margin: 0; color: var(--split-flap-amber); font: 600 0.8125rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }
.split-flap__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.split-flap__lead { max-width: 34rem; margin: 1rem auto 0; color: var(--split-flap-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Housing: framed, riveted, lit from above */
.split-flap__stage { width: fit-content; max-width: 100%; margin-inline: auto; }
.split-flap__board {
  position: relative; padding: 0.75rem 0.75rem 1rem; border-radius: var(--radius-lg);
  background: linear-gradient(color-mix(in srgb, var(--split-flap-board) 92%, var(--split-flap-ink)), var(--split-flap-board));
  box-shadow:
    var(--highlight-inverse),
    0 0 0 1px color-mix(in srgb, var(--split-flap-ink) 10%, transparent),
    0 0 0 0.375rem color-mix(in srgb, var(--split-flap-flap) 75%, var(--split-flap-board)),
    0 0 0 calc(0.375rem + 1px) color-mix(in srgb, var(--split-flap-ink) 14%, transparent),
    0 2.5rem 5rem -1.5rem var(--split-flap-board);
  font: 600 var(--split-flap-size)/1 var(--font-mono);
}
.split-flap__board::before {
  content: ""; position: absolute; inset: 0; pointer-events: none; border-radius: inherit;
  background:
    radial-gradient(circle at left 0.3rem top 0.3rem, var(--split-flap-muted) 0 0.09rem, transparent 0.13rem),
    radial-gradient(circle at right 0.3rem top 0.3rem, var(--split-flap-muted) 0 0.09rem, transparent 0.13rem),
    radial-gradient(circle at left 0.3rem bottom 0.3rem, var(--split-flap-muted) 0 0.09rem, transparent 0.13rem),
    radial-gradient(circle at right 0.3rem bottom 0.3rem, var(--split-flap-muted) 0 0.09rem, transparent 0.13rem);
}
.split-flap__board-head {
  display: flex; align-items: center; justify-content: space-between; gap: 1rem;
  margin-bottom: 0.75rem; padding-bottom: 0.625rem; border-bottom: 1px solid color-mix(in srgb, var(--split-flap-ink) 10%, transparent);
}
.split-flap__board-title { display: flex; align-items: center; gap: 0.5rem; margin: 0; color: var(--split-flap-amber); font: 600 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.split-flap__lamp { flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--split-flap-amber); box-shadow: 0 0 0.5rem var(--split-flap-amber); }
.split-flap__pause {
  flex: none; display: grid; place-items: center; width: 2.25rem; height: 2.25rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--split-flap-flap); color: var(--split-flap-ink);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--split-flap-ink) 12%, transparent), var(--highlight-inverse);
  transition: background-color var(--dur-2) var(--ease-out), scale var(--dur-1) var(--ease-out);
}
.split-flap__pause:hover { background: color-mix(in srgb, var(--split-flap-flap) 82%, var(--split-flap-ink)); }
.split-flap__pause:active { scale: 0.94; }
.split-flap__pause[hidden] { display: none; }
.split-flap__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.split-flap__icon-play, .split-flap__pause[aria-pressed="true"] .split-flap__icon-pause { display: none; }
.split-flap__pause[aria-pressed="true"] .split-flap__icon-play { display: block; }

/* Rows: 2 × 2 fields on phones, one line of four from 768px */
.split-flap__table { display: grid; grid-template-columns: max-content; justify-content: center; gap: 0.55em; }
.split-flap__row { position: relative; display: grid; grid-template-columns: repeat(2, max-content); gap: 0.3em 0.6em; }
.split-flap__row[data-split-flap-row] { padding-top: 0.55em; border-top: 1px solid color-mix(in srgb, var(--split-flap-ink) 8%, transparent); }
.split-flap__row--pinned::before {
  content: ""; position: absolute; left: -0.55em; top: calc(0.55em + var(--split-flap-h) / 2 - 0.15em); width: 0.3em; height: 0.3em; border-radius: 50%;
  background: var(--split-flap-flap); transition: background-color var(--dur-3) var(--ease-out);
}
.split-flap__row--pinned.is-yours::before { background: var(--split-flap-amber); box-shadow: 0 0 0.4em var(--split-flap-amber); }
.split-flap__colhead { display: block; width: calc(var(--split-flap-n) * var(--split-flap-cell) - var(--split-flap-gap)); color: var(--split-flap-muted); }
.split-flap__colhead > span { font: 600 0.6875rem/1 var(--font-sans); letter-spacing: 0.14em; text-transform: uppercase; }

/* No-JS cell: the text itself, spaced to the tile pitch over painted tiles and a hinge line */
.split-flap__cell {
  display: block; box-sizing: border-box; width: calc(var(--split-flap-n) * var(--split-flap-cell) - var(--split-flap-gap)); height: var(--split-flap-h);
  overflow: hidden; padding-left: calc((var(--split-flap-w) - 1ch) / 2); border-radius: 0.1em;
  color: var(--split-flap-ink); line-height: var(--split-flap-h); letter-spacing: calc(var(--split-flap-cell) - 1ch); white-space: pre;
  background:
    linear-gradient(transparent calc(50% - 0.5px), var(--split-flap-board) 0 calc(50% + 0.5px), transparent 0),
    repeating-linear-gradient(90deg, var(--split-flap-flap) 0 var(--split-flap-w), transparent 0 var(--split-flap-cell));
}
.split-flap--js .split-flap__cell { padding-left: 0; letter-spacing: 0; background: none; }
.split-flap__row.is-yours .split-flap__cell { color: var(--split-flap-amber); }

/* Flap tile: static top and bottom halves, plus two leaves that do the 3D flip */
.split-flap__tiles { display: flex; gap: var(--split-flap-gap); }
.split-flap__tile { position: relative; flex: none; width: var(--split-flap-w); height: var(--split-flap-h); perspective: 5em; }
.split-flap__tile::before { /* axle nubs */
  content: ""; position: absolute; z-index: 2; inset-inline: 0; top: calc(50% - 0.12em); height: 0.24em;
  background: linear-gradient(90deg, var(--split-flap-board) 0 0.05em, transparent 0 calc(100% - 0.05em), var(--split-flap-board) 0);
}
.split-flap__tile::after { /* hinge line */
  content: ""; position: absolute; z-index: 2; inset-inline: 0; top: calc(50% - 0.5px); height: 1px; background: var(--split-flap-board);
}
.split-flap__half, .split-flap__leaf { position: absolute; inset-inline: 0; height: 50%; overflow: hidden; text-align: center; backface-visibility: hidden; }
.split-flap__half--top, .split-flap__leaf--top {
  top: 0; line-height: var(--split-flap-h); border-radius: 0.1em 0.1em 0 0; transform-origin: 50% 100%;
  background: linear-gradient(color-mix(in srgb, var(--split-flap-flap) 86%, var(--split-flap-ink)), var(--split-flap-flap));
}
.split-flap__half--bottom, .split-flap__leaf--bottom {
  bottom: 0; line-height: 0; border-radius: 0 0 0.1em 0.1em; transform-origin: 50% 0;
  background: linear-gradient(var(--split-flap-flap), color-mix(in srgb, var(--split-flap-flap) 75%, var(--split-flap-board)));
}
.split-flap__half--bottom::after { /* shadow cast by the falling leaf (animated from JS) */
  content: ""; position: absolute; inset: 0; opacity: 0;
  background: linear-gradient(color-mix(in srgb, var(--split-flap-board) 80%, transparent), transparent 75%);
}

/* Check your area */
.split-flap__check { display: flex; flex-wrap: wrap; align-items: flex-end; gap: 0.75rem; margin-top: 2rem; }
.split-flap__label { display: grid; gap: 0.5rem; flex: 1 1 14rem; }
.split-flap__label-text { font-size: 0.9375rem; font-weight: 600; }
.split-flap__input {
  box-sizing: border-box; width: 100%; min-height: 3rem; margin: 0; padding: 0 1rem; border: 0; border-radius: var(--radius-md);
  background: var(--split-flap-flap); color: var(--split-flap-ink); font: 600 1rem var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--split-flap-ink) 14%, transparent), inset 0 2px 6px color-mix(in srgb, var(--split-flap-board) 60%, transparent);
}
.split-flap__input::placeholder { color: color-mix(in srgb, var(--split-flap-ink) 55%, var(--split-flap-flap)); letter-spacing: 0; text-transform: none; opacity: 1; }
.split-flap__btn {
  flex: none; min-height: 3rem; padding: 0 1.375rem; border: 0; border-radius: var(--radius-md); cursor: pointer;
  background: var(--split-flap-amber); color: var(--split-flap-board); font: 700 0.9375rem var(--font-sans);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--split-flap-ink) 45%, transparent), 0 10px 24px -12px var(--split-flap-amber);
  transition: translate var(--dur-2) var(--ease-spring), scale var(--dur-1) var(--ease-out);
}
.split-flap__btn:hover { translate: 0 -1px; }
.split-flap__btn:active { scale: 0.97; }
.split-flap :is(a, button, input):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.split-flap__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }

@media (min-width: 768px) {
  .split-flap { --split-flap-size: clamp(1.0625rem, 0.4rem + 1.6vw, 1.75rem); }
  .split-flap__board { padding: 1.25rem 1.5rem 1.5rem; }
  .split-flap__table { gap: 0.45em; }
  .split-flap__row { grid-template-columns: repeat(4, max-content); row-gap: 0; }
  .split-flap__row[data-split-flap-row] { padding-top: 0; border-top: 0; }
  .split-flap__row--pinned::before { top: calc(var(--split-flap-h) / 2 - 0.15em); }
}
```

## JS

```js
const CHARS = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:-.+/';
const MAX_STEPS = 4; // characters a flap shows on its way to the target, the target included
const DWELL = 2600; // rest after the flaps settle, for a ~4s cadence
const DAYS = { MON: 'Monday', TUE: 'Tuesday', WED: 'Wednesday', THU: 'Thursday', FRI: 'Friday', SAT: 'Saturday', SUN: 'Sunday' };
const LEAVES = '<span class="split-flap__half split-flap__half--top"></span><span class="split-flap__half split-flap__half--bottom"></span>'
  + '<span class="split-flap__leaf split-flap__leaf--top"></span><span class="split-flap__leaf split-flap__leaf--bottom"></span>';
const parse = (s = '') => s.split(';').filter(Boolean).map((row) => row.split('|'));
const clean = (s) => [...s.toUpperCase()].map((c) => (CHARS.includes(c) ? c : ' ')).join('');
const wait = (ms) => new Promise((done) => { setTimeout(done, ms); });

document.querySelectorAll('[data-split-flap]').forEach((root, n) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const spring = getComputedStyle(root).getPropertyValue('--ease-spring').trim() || 'ease-out';
  const queue = parse(root.dataset.splitFlapQueue);
  const areas = new Map(parse(root.dataset.splitFlapAreas).map(([area, ...slot]) => [area, slot]));
  const pause = root.querySelector('.split-flap__pause');
  const form = root.querySelector('.split-flap__check');
  const live = root.querySelector('.split-flap__live');
  const list = root.querySelector('datalist');
  const pinnedRow = root.querySelector('.split-flap__row--pinned');
  let cursor = 0;
  let timer = 0;
  let offscreen = true;

  list.id = `split-flap-areas-${n}`;
  form.elements.area.setAttribute('list', list.id);

  // Build the tiles. Each cell keeps a visually hidden copy of its text; the tiles are aria-hidden.
  const show = (t, ch) => {
    t.char = ch;
    t.top.textContent = t.bottom.textContent = t.leafTop.textContent = t.leafBottom.textContent = ch;
  };
  root.classList.add('split-flap--js');
  const [pinned, ...rolling] = [...root.querySelectorAll('[data-split-flap-row]')].map((row) => {
    let offset = 0;
    return [...row.querySelectorAll('.split-flap__cell')].map((cell) => {
      const width = Number(cell.style.getPropertyValue('--split-flap-n'));
      const text = clean(cell.textContent.trim());
      const sr = Object.assign(document.createElement('span'), { className: 'split-flap__sr', textContent: text.trim() });
      const strip = Object.assign(document.createElement('span'), { className: 'split-flap__tiles' });
      strip.setAttribute('aria-hidden', 'true');
      const tiles = Array.from({ length: width }, (_, i) => {
        const tile = strip.appendChild(Object.assign(document.createElement('span'), { className: 'split-flap__tile', innerHTML: LEAVES }));
        const [top, bottom, leafTop, leafBottom] = tile.children;
        const t = { top, bottom, leafTop, leafBottom, char: ' ', job: 0, run: Promise.resolve() };
        show(t, text[i] || ' ');
        return t;
      });
      cell.replaceChildren(sr, strip);
      offset += width;
      return { sr, tiles, offset: offset - width };
    });
  });

  // One flip: the top leaf folds down over the new top half, then the bottom leaf lands (springy on the last one)
  const step = async (t, ch, last) => {
    const fall = last ? 150 : 70;
    const land = last ? 280 : 90;
    t.top.textContent = ch;
    t.leafTop.textContent = t.char;
    t.leafBottom.textContent = ch;
    const fold = t.leafTop.animate(
      [{ transform: 'rotateX(0deg)', filter: 'brightness(1)' }, { transform: 'rotateX(-90deg)', filter: 'brightness(0.55)' }],
      { duration: fall, easing: 'ease-in', fill: 'forwards' },
    );
    if (last) t.bottom.animate([{ opacity: 0 }, { opacity: 1, offset: 0.4 }, { opacity: 0 }], { duration: fall + land, pseudoElement: '::after' });
    await t.leafBottom.animate(
      [{ transform: 'rotateX(90deg)', filter: 'brightness(1.5)' }, { transform: 'rotateX(0deg)', filter: 'brightness(1)' }],
      { duration: land, delay: fall, easing: last ? spring : 'ease-out', fill: 'backwards' },
    ).finished;
    t.bottom.textContent = t.leafTop.textContent = ch;
    fold.cancel();
    t.char = ch;
  };

  // Cascade through the characters before the target (MAX_STEPS at most); a newer job supersedes an older one
  const flip = (t, target, delay) => {
    const job = ++t.job;
    t.run = t.run.then(async () => {
      if (job !== t.job || target === t.char) return;
      await wait(delay);
      const path = [];
      for (let i = CHARS.indexOf(t.char); CHARS[i] !== target;) { i = (i + 1) % CHARS.length; path.push(CHARS[i]); }
      for (const ch of path.slice(-MAX_STEPS)) {
        if (job !== t.job) return;
        await step(t, ch, ch === target);
      }
    }).catch(() => {});
    return t.run;
  };

  // Write a row: pad each field to its tiles, refresh its hidden text, flip left to right
  const write = (fields, values, rowIndex) => Promise.all(fields.flatMap((field, f) => {
    const text = clean(values[f] || '').padEnd(field.tiles.length).slice(0, field.tiles.length);
    field.sr.textContent = text.trim();
    return field.tiles.map((t, i) => (reduce ? show(t, text[i]) : flip(t, text[i], (field.offset + i) * 30 + rowIndex * 80)));
  }));

  // Auto cycle: the rolling rows shift up one slot every ~4s. Never under reduced motion, paused or off-screen.
  const schedule = () => {
    clearTimeout(timer);
    if (!reduce && !offscreen && !root.hasAttribute('data-paused') && queue.length > rolling.length) timer = setTimeout(cycle, DWELL);
  };
  const cycle = async () => {
    cursor = (cursor + 1) % queue.length;
    await Promise.all(rolling.map((fields, i) => write(fields, queue[(cursor + i) % queue.length], i + 1)));
    schedule();
  };
  pause.hidden = reduce;
  pause.addEventListener('click', () => {
    pause.setAttribute('aria-pressed', String(root.toggleAttribute('data-paused')));
    schedule();
  });
  new IntersectionObserver(([entry]) => { offscreen = !entry.isIntersecting; schedule(); }).observe(root);

  // Check your area: set the pinned row on demand, and only then speak through the live region
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const typed = form.elements.area.value.trim();
    const key = clean(typed).trim();
    if (!key) return;
    const slot = areas.get(key);
    write(pinned, ['NEXT SLOT', slot ? slot[0] : '--- --:--', key, slot ? slot[1] : 'CALL US'], 0);
    pinnedRow.classList.add('is-yours');
    const [day, time] = slot ? slot[0].split(' ') : [];
    const message = slot
      ? `Next slot in ${typed}: ${DAYS[day] || day} at ${time}, ${slot[1].toLowerCase()}.`
      : `No online slots for ${typed} yet. Call (555) 555-0123.`;
    live.textContent = '';
    setTimeout(() => { live.textContent = message; }, 60);
  });
});
```

## Notes

- Semantics: a `role="table"` with column headers. Each cell keeps its current text in a visually hidden span while the tiles are `aria-hidden`, so the board reads as an ordinary table at any moment. The polite `role="status"` region speaks only after "Check your area" ("Next slot in Westlake: Thursday at 10:00, on time."), never on the auto cycle.
- Auto cycle: the three rolling rows shift up one slot every ~4s (2.6s after the flaps settle). The `aria-pressed` pause button stops it, it freezes while off-screen, and it never runs under reduced motion, where text also swaps instantly and the pause button stays hidden.
- No JS: the same rows render as text spaced to the tile pitch over painted tiles. Widths are in `ch`, so the swap to real tiles doesn't shift anything. The form submits normally, so point `action` at a real availability page.
- Data lives on the root: `data-split-flap-queue` (`SERVICE|TIME|AREA|STATUS;…`) and `data-split-flap-areas` (`AREA|TIME|STATUS;…`). Unknown areas show "CALL US", and characters outside `A–Z 0–9 : - . + /` become blanks.
- Contrast: flap ink on charcoal 14.3:1, amber on charcoal 9.4:1, muted ink (62%) on the board 6.8:1, board black on the amber button 11.1:1.
- Flips are WAAPI (transform, filter, and opacity on a pseudo-element shadow), at most four characters per tile per update, so a full board update stays light. Spring easing on the final landing reads `--ease-spring` from the tokens.
