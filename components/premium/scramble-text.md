# Scramble Text

A deep diagnostics panel where type decodes out of noise. Characters cycle through a Geist Mono glyph set, then lock into the display face left to right, with a gradient read-head under the character being decoded and a soft phosphor flash as each one settles. The headline decodes when it scrolls into view, the readout values follow in a cascade, nav-style links re-scramble on hover or focus, and a Replay button runs it again. On phones the bar stacks, the viewfinder frame tightens and the readout becomes a list. Depends on `tokens/variables.css`.

**Motion:** glyph cycling (55ms ticks) with a left-to-right lock wave and gradient read-head · per-character lock flash (`--dur-4`, `--ease-out`) · readout cascade (staggered delays) · link hover scramble · replay icon turn (`--dur-4`, `--ease-spring`) and spin (`--dur-5`, `--ease-out`).

## HTML

```html
<section class="scramble-text" aria-labelledby="scramble-text-title" data-scramble-text>
  <div class="scramble-text__inner">
    <header class="scramble-text__bar">
      <p class="scramble-text__brand">
        <span class="scramble-text__logo" aria-hidden="true">
          <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M3 10.5 12 3l9 7.5M5 9.5V20h14V9.5M10 20v-5h4v5" /></svg>
        </span>
        Brand <span class="scramble-text__brand-sub">Diagnostics</span>
      </p>
      <nav class="scramble-text__nav" aria-label="Diagnostics">
        <ul class="scramble-text__links" role="list">
          <li><a class="scramble-text__link" href="#services"><span class="scramble-text__index" aria-hidden="true">01</span><span data-scramble="hover">Services</span></a></li>
          <li><a class="scramble-text__link" href="#pricing"><span class="scramble-text__index" aria-hidden="true">02</span><span data-scramble="hover">Pricing</span></a></li>
          <li><a class="scramble-text__link" href="#contact"><span class="scramble-text__index" aria-hidden="true">03</span><span data-scramble="hover">Contact</span></a></li>
        </ul>
      </nav>
    </header>

    <div class="scramble-text__stage">
      <p class="scramble-text__status" aria-hidden="true">
        <span class="scramble-text__dot"></span>
        <span class="scramble-text__busy">Diagnosing</span><span class="scramble-text__done">Fault found</span>
      </p>
      <h2 id="scramble-text-title" class="scramble-text__title" data-scramble="view">
        <span class="scramble-text__line">No guesswork.</span>
        <span class="scramble-text__line scramble-text__line--lit">Just the fix.</span>
      </h2>
      <button class="scramble-text__replay" type="button" hidden>
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M3 12a9 9 0 1 0 2.6-6.4L3 8" /><path d="M3 3v5h5" /></svg>
        Replay
      </button>
    </div>

    <div class="scramble-text__foot">
      <p class="scramble-text__lead">Every visit starts with a full diagnostic. You see the fault, the fix and a fixed price before we touch a tool.</p>
      <dl class="scramble-text__readout">
        <div class="scramble-text__cell"><dt>Fault</dt><dd data-scramble="view" data-scramble-delay="300">Worn valve seat</dd></div>
        <div class="scramble-text__cell"><dt>On site</dt><dd data-scramble="view" data-scramble-delay="450">38 min</dd></div>
        <div class="scramble-text__cell"><dt>Fixed price</dt><dd data-scramble="view" data-scramble-delay="600">$149</dd></div>
      </dl>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: deep surface lit from two corners */
.scramble-text {
  --scramble-text-noise: color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse));
  --scramble-text-hot: color-mix(in srgb, var(--primary-2) 30%, var(--text-inverse));
  --scramble-text-mark: color-mix(in srgb, var(--text-inverse) 34%, transparent);
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(60% 55% at 10% 0%, color-mix(in srgb, var(--primary) 26%, transparent), transparent 70%),
    radial-gradient(50% 60% at 96% 100%, color-mix(in srgb, var(--primary-2) 18%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.scramble-text__inner {
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(1rem, 3vw, 1.75rem) var(--gutter) clamp(3.5rem, 8vw, 6rem);
}
.scramble-text :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Top bar: brand and nav-style links */
.scramble-text__bar {
  display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.5rem 1.5rem;
  padding-bottom: 0.75rem; border-bottom: 1px solid var(--border-inverse);
}
.scramble-text__brand { display: inline-flex; align-items: center; gap: 0.625rem; margin: 0; font: 600 1rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.scramble-text__brand-sub { color: var(--text-inverse-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.scramble-text__logo {
  display: grid; place-items: center; width: 1.75rem; height: 1.75rem; border-radius: 0.5rem; background: var(--gradient-brand);
  box-shadow: var(--highlight-inverse), 0 6px 16px -6px color-mix(in srgb, var(--primary) 80%, transparent);
}
.scramble-text__logo svg { fill: none; stroke: var(--text-inverse); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.scramble-text__links { display: flex; flex-wrap: wrap; margin: 0 0 0 -0.625rem; padding: 0; list-style: none; }
.scramble-text__link {
  display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem; padding: 0 0.625rem; border-radius: 999px;
  color: var(--text-inverse-muted); text-decoration: none; font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase;
  transition: color var(--dur-2), background-color var(--dur-2);
}
.scramble-text__link:hover, .scramble-text__link:focus-visible { color: var(--text-inverse); background: var(--glass-inverse); }
.scramble-text__index { color: var(--scramble-text-noise); font-size: 0.6875rem; }

/* Stage: a viewfinder frame with corner marks and faint scanlines */
.scramble-text__stage {
  position: relative; margin-top: clamp(1.75rem, 5vw, 3.5rem);
  padding: 3rem clamp(1rem, 4vw, 3rem) var(--scramble-text-room, 2.75rem);
  background:
    linear-gradient(var(--scramble-text-mark) 0 0) top left / 1rem 1px no-repeat,
    linear-gradient(var(--scramble-text-mark) 0 0) top left / 1px 1rem no-repeat,
    linear-gradient(var(--scramble-text-mark) 0 0) top right / 1rem 1px no-repeat,
    linear-gradient(var(--scramble-text-mark) 0 0) top right / 1px 1rem no-repeat,
    linear-gradient(var(--scramble-text-mark) 0 0) bottom left / 1rem 1px no-repeat,
    linear-gradient(var(--scramble-text-mark) 0 0) bottom left / 1px 1rem no-repeat,
    linear-gradient(var(--scramble-text-mark) 0 0) bottom right / 1rem 1px no-repeat,
    linear-gradient(var(--scramble-text-mark) 0 0) bottom right / 1px 1rem no-repeat;
}
.scramble-text__stage::before {
  content: ""; position: absolute; inset: 1px; z-index: -1; pointer-events: none;
  background: repeating-linear-gradient(to bottom, color-mix(in srgb, var(--text-inverse) 5%, transparent) 0 1px, transparent 1px 4px);
  -webkit-mask-image: radial-gradient(ellipse 75% 85% at 28% 50%, black, transparent 75%);
  mask-image: radial-gradient(ellipse 75% 85% at 28% 50%, black, transparent 75%);
}

/* Status chip: "Diagnosing" until every glyph has locked, pulsing only while glyphs cycle (CSS :has) */
.scramble-text__status {
  position: absolute; top: 1rem; left: clamp(1rem, 4vw, 3rem); display: inline-flex; align-items: center; gap: 0.5rem; margin: 0;
  color: var(--text-inverse-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase;
}
.scramble-text__dot { width: 0.4375rem; height: 0.4375rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 28%, transparent); }
.scramble-text__busy { display: none; }
.scramble-text__stage:has([data-g]) .scramble-text__busy { display: inline; }
.scramble-text__stage:has([data-g]) .scramble-text__done { display: none; }
.scramble-text__stage:has([data-g]) .scramble-text__dot { background: var(--accent); box-shadow: 0 0 0 3px color-mix(in srgb, var(--accent) 28%, transparent); }
.scramble-text__stage:has([data-g]:not([data-g=""])) .scramble-text__dot { animation: scramble-text-pulse 0.8s var(--ease-in-out) infinite; }

/* Headline: muted setup line, bright payoff line */
.scramble-text__title { margin: 0; font: 600 clamp(2.5rem, 1rem + 7vw, 6.75rem)/0.95 var(--font-display); letter-spacing: var(--tracking-display); }
.scramble-text__line { display: block; color: var(--text-inverse-muted); }
.scramble-text__line--lit { color: var(--text-inverse); }

/* Replay */
.scramble-text__replay {
  position: absolute; right: clamp(1rem, 4vw, 3rem); bottom: 1rem; display: inline-flex; align-items: center; gap: 0.5rem;
  height: 2.75rem; padding: 0 1.125rem 0 0.875rem; border: 0; border-radius: 999px; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.scramble-text__replay[hidden] { display: none; }
.scramble-text__replay:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.scramble-text__replay:active { transform: scale(0.96); }
.scramble-text__replay svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: rotate var(--dur-4) var(--ease-spring); }
.scramble-text__replay:hover svg { rotate: -40deg; }
.scramble-text__replay.is-spun svg { animation: scramble-text-spin var(--dur-5) var(--ease-out); }

/* Foot: lead and a readout that decodes after the headline */
.scramble-text__foot { display: grid; gap: 1.75rem; margin-top: clamp(1.75rem, 5vw, 3rem); }
.scramble-text__lead { max-width: 30rem; margin: 0; color: var(--text-inverse-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }
.scramble-text__readout {
  display: grid; margin: 0; border-radius: var(--radius-xl); background: var(--glass-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.scramble-text__cell { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; padding: 0.875rem 1.125rem; }
.scramble-text__cell + .scramble-text__cell { border-top: 1px solid var(--border-inverse); }
.scramble-text__cell dt { flex: none; color: var(--text-inverse-muted); font: 500 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.scramble-text__cell dd { margin: 0; font: 600 1.0625rem/1.2 var(--font-display); letter-spacing: -0.01em; text-align: right; }

/* Split text: a visually hidden copy for AT, glyph spans for the eye */
.scramble-text__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; }
.scramble-text__glyphs { font-variant-ligatures: none; }
.scramble-text__char { position: relative; }
.scramble-text__char[data-g] { color: transparent; }
.scramble-text__char[data-g]::before {
  content: attr(data-g); position: absolute; top: 0; left: 50%; translate: -50% 0;
  color: var(--scramble-text-noise); font-family: var(--font-mono); font-weight: 400; line-height: normal; letter-spacing: 0;
}
.scramble-text__char.is-front::before { color: var(--text-inverse); }
.scramble-text__char.is-front::after {
  content: ""; position: absolute; left: 0; right: 0; bottom: 0.02em; height: max(2px, 0.045em); border-radius: 999px;
  background: var(--gradient-brand); box-shadow: 0 0 12px color-mix(in srgb, var(--primary-2) 70%, transparent);
}
.scramble-text__char.is-locked { animation: scramble-text-lock var(--dur-4) var(--ease-out); }

/* Before the script runs: reserve room for Replay and hide only what will decode (2.5s CSS failsafe) */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .scramble-text { --scramble-text-room: 4.75rem; }
  .scramble-text:not(.scramble-text--ready) [data-scramble="view"] { opacity: 0; animation: scramble-text-failsafe 0s 2.5s forwards; }
}

@media (min-width: 768px) {
  .scramble-text__links { gap: 0.25rem; margin: 0 -0.875rem 0 0; }
  .scramble-text__link { gap: 0.5rem; padding: 0 0.875rem; letter-spacing: 0.08em; }
  .scramble-text__stage { padding-top: 3.5rem; }
  .scramble-text__status { top: 1.25rem; }
  .scramble-text__replay { bottom: 1.25rem; }
  .scramble-text__readout { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .scramble-text__cell { display: grid; align-content: start; justify-content: stretch; gap: 0.625rem; padding: 1.125rem 1.25rem; }
  .scramble-text__cell + .scramble-text__cell { border-top: 0; border-left: 1px solid var(--border-inverse); }
  .scramble-text__cell dd { font-size: 1.25rem; text-align: left; }
}
@media (min-width: 1024px) {
  .scramble-text__foot { grid-template-columns: minmax(0, 1fr) minmax(0, 1.3fr); align-items: end; gap: 3rem; }
}

@media (prefers-reduced-motion: reduce) {
  .scramble-text *, .scramble-text *::before, .scramble-text *::after { animation: none !important; }
}

@keyframes scramble-text-lock { from { color: var(--scramble-text-hot); text-shadow: 0 0 0.4em color-mix(in srgb, var(--primary-2) 75%, transparent); } }
@keyframes scramble-text-pulse { 50% { opacity: 0.35; } }
@keyframes scramble-text-spin { from { rotate: 0deg; } to { rotate: -360deg; } }
@keyframes scramble-text-failsafe { to { opacity: 1; } }
```

## JS

```js
const GLYPHS = 'ABCDEFGHJKLMNPQRSTUVWXYZ0123456789#%&*+=/<>';
const pick = () => GLYPHS[(Math.random() * GLYPHS.length) | 0];
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const span = (className, textContent = '') => Object.assign(document.createElement('span'), { className, textContent });

// Keep the real text for assistive tech; draw the effect in one aria-hidden layer of character spans
const split = (el) => {
  const copy = span('scramble-text__sr', el.textContent.replace(/\s+/g, ' ').trim());
  const layer = span('scramble-text__glyphs');
  layer.setAttribute('aria-hidden', 'true');
  layer.append(...el.childNodes);
  const walker = document.createTreeWalker(layer, NodeFilter.SHOW_TEXT);
  const texts = [];
  while (walker.nextNode()) texts.push(walker.currentNode);
  const chars = [];
  texts.forEach((node) => node.replaceWith(...node.data.split(/(\s+)/).flatMap((part) => {
    if (!part.trim()) return part ? [part] : []; // spaces stay text, so lines wrap between words only
    return [...part].map((ch) => { const c = span('scramble-text__char', ch); chars.push(c); return c; });
  })));
  el.append(copy, layer);
  return chars;
};

document.querySelectorAll('[data-scramble-text]').forEach((root) => {
  if (reduce.matches) return; // the final text stays as authored
  const targets = [...root.querySelectorAll('[data-scramble]')].map((el) => ({
    el, chars: split(el), hover: el.dataset.scramble === 'hover', delay: Number(el.dataset.scrambleDelay) || 0, token: 0,
  }));

  // Glyphs re-roll every ~55ms; each character locks at its own time, left to right
  const play = (t) => {
    const id = ++t.token;
    const start = performance.now() + (t.hover ? 0 : t.delay);
    const plan = t.chars.map((c, i) => ({
      c, show: t.hover ? 0 : i * 22,
      lock: t.hover ? 60 + i * 32 + Math.random() * 60 : 380 + i * 46 + Math.random() * 160,
    }));
    t.chars.forEach((c) => { c.dataset.g = t.hover ? pick() : ''; c.classList.remove('is-locked', 'is-front'); });
    t.busy = true;
    let last = 0;
    const tick = (now) => {
      if (id !== t.token) return;
      const time = now - start;
      const reroll = now - last > 55;
      if (reroll) last = now;
      let front = null;
      plan.forEach((p) => {
        if (p.done) return;
        if (time >= p.lock || reduce.matches) { p.done = true; delete p.c.dataset.g; p.c.classList.add('is-locked'); return; }
        if (time >= p.show && (reroll || !p.c.dataset.g)) p.c.dataset.g = pick();
        if (!front && time >= p.show) front = p.c;
      });
      if (front !== t.front) { t.front?.classList.remove('is-front'); front?.classList.add('is-front'); t.front = front; }
      t.busy = plan.some((p) => !p.done);
      if (t.busy) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  // Headline and readout start blank and decode once each scrolls into view
  const views = targets.filter((t) => !t.hover);
  views.forEach((t) => t.chars.forEach((c) => { c.dataset.g = ''; }));
  const io = new IntersectionObserver((entries) => entries.forEach((e) => {
    if (!e.isIntersecting) return;
    io.unobserve(e.target);
    play(views.find((t) => t.el === e.target));
  }), { threshold: 0.6 });
  views.forEach((t) => io.observe(t.el));
  root.classList.add('scramble-text--ready');

  // Nav-style links re-scramble on hover or keyboard focus (never mid-run)
  targets.filter((t) => t.hover).forEach((t) => {
    const trigger = t.el.closest('a, button') || t.el;
    const go = () => { if (!t.busy) play(t); };
    trigger.addEventListener('pointerenter', go);
    trigger.addEventListener('focus', go);
  });

  const replay = root.querySelector('.scramble-text__replay');
  if (!replay) return;
  replay.hidden = false;
  replay.addEventListener('click', () => {
    views.forEach((t) => { io.unobserve(t.el); play(t); });
    replay.classList.remove('is-spun');
    void replay.offsetWidth; // restart the icon spin
    replay.classList.add('is-spun');
  });
});
```

## Notes

- Accessibility: every scrambled element keeps a visually hidden copy of its text, and the glyph spans sit in one `aria-hidden` layer, so screen readers hear "No guesswork. Just the fix." once and never letter by letter. Link names stay "Services", "Pricing" and "Contact"; the `01–03` indices and the status chip are decorative.
- No layout shift: the final characters always hold their boxes (transparent while scrambling), and the noise is a `::before` overlay set in `--font-mono`, so proportional display type never reflows mid-decode.
- Without JS, or under reduced motion, the final text renders immediately and Replay stays hidden. With JS, `@media (scripting: enabled)` hides only the decoding targets until the script starts, with a 2.5s CSS failsafe, so nothing flashes from final to noise. The only loop is the status dot pulse, which runs only while glyphs are decoding (under 2s).
- Contrast on `--surface-deep`: noise glyphs 9.6:1, the muted line 7.7:1, white type 18.8:1.
- Adapt: put `data-scramble="view"` (optional `data-scramble-delay` in ms) or `data-scramble="hover"` on any text element inside the root, and swap `GLYPHS` for a different alphabet. The status chip relies on `:has()` and shows its final state where that isn't supported.
