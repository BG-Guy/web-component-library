# Expanding Image Panels

Five tall photo panels, one per trade, on a deep surface. Hover or focus a panel and it springs wide on `flex-grow`, its photo brightens and settles, its label swings on a hinge from vertical to horizontal, and a project count, description and "View projects" link rise in, one after another. Collapsed panels stay dim, showing a number and a vertical label; hovering previews a panel, and a click or tap pins it open. On phones the row becomes a vertical stack of drawers that open in height on tap. Depends on `tokens/variables.css`.

**Motion:** `flex-grow` spring (`--dur-5` `--ease-spring`, inside a size- and layout-contained row) · label hinge `rotate(90deg → 0)` on the spring · photo brighten, saturate and settle from `scale(1.12)` (`--dur-5` `--ease-out`) · body rise with `--stagger` · number underline draw · plus-to-cross on mobile.

## HTML

```html
<section class="expand-panels" aria-labelledby="expand-panels-title" data-expand-panels>
  <div class="expand-panels__inner">
    <header class="expand-panels__head">
      <p class="expand-panels__eyebrow">Our work</p>
      <h2 id="expand-panels-title" class="expand-panels__title">Five trades. One crew you'll trust in every room.</h2>
      <p class="expand-panels__lead">Look inside recent projects from Westlake, Northside and Riverside. Hover to preview a trade, or click to keep it open.</p>
    </header>

    <ul class="expand-panels__list" role="list">
      <li class="expand-panels__panel is-open">
        <img class="expand-panels__img" src="kitchens.jpg" width="1600" height="1200" loading="lazy" decoding="async" alt="Walnut and white kitchen with a stone-topped island">
        <span class="expand-panels__num" aria-hidden="true">01</span>
        <h3 class="expand-panels__label">
          <button class="expand-panels__toggle" type="button" aria-expanded="true" aria-controls="expand-panels-body-1">
            Kitchens
            <svg class="expand-panels__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg>
          </button>
        </h3>
        <div class="expand-panels__body" id="expand-panels-body-1">
          <p class="expand-panels__meta">48 projects · since 2012</p>
          <p class="expand-panels__desc">Cabinetry, stone tops and lighting, planned around how you actually cook.</p>
          <a class="expand-panels__link" href="#kitchens">View projects <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </div>
      </li>
      <li class="expand-panels__panel">
        <img class="expand-panels__img" src="baths.jpg" width="1600" height="1200" loading="lazy" decoding="async" alt="Bright bathroom with a walk-in shower and a terrazzo floor">
        <span class="expand-panels__num" aria-hidden="true">02</span>
        <h3 class="expand-panels__label">
          <button class="expand-panels__toggle" type="button" aria-expanded="true" aria-controls="expand-panels-body-2">
            Baths
            <svg class="expand-panels__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg>
          </button>
        </h3>
        <div class="expand-panels__body" id="expand-panels-body-2">
          <p class="expand-panels__meta">36 projects · since 2014</p>
          <p class="expand-panels__desc">Walk-in showers, heated floors and storage that keeps the counter clear.</p>
          <a class="expand-panels__link" href="#baths">View projects <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </div>
      </li>
      <li class="expand-panels__panel">
        <img class="expand-panels__img" src="roofing.jpg" width="1600" height="1200" loading="lazy" decoding="async" alt="Slate roof with new copper gutters at dusk">
        <span class="expand-panels__num" aria-hidden="true">03</span>
        <h3 class="expand-panels__label">
          <button class="expand-panels__toggle" type="button" aria-expanded="true" aria-controls="expand-panels-body-3">
            Roofing
            <svg class="expand-panels__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg>
          </button>
        </h3>
        <div class="expand-panels__body" id="expand-panels-body-3">
          <p class="expand-panels__meta">112 projects · since 2009</p>
          <p class="expand-panels__desc">Re-roofs, repairs and gutters, backed by a ten-year workmanship guarantee.</p>
          <a class="expand-panels__link" href="#roofing">View projects <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </div>
      </li>
      <li class="expand-panels__panel">
        <img class="expand-panels__img" src="outdoor.jpg" width="1600" height="1200" loading="lazy" decoding="async" alt="Cedar deck with string lights and outdoor seating">
        <span class="expand-panels__num" aria-hidden="true">04</span>
        <h3 class="expand-panels__label">
          <button class="expand-panels__toggle" type="button" aria-expanded="true" aria-controls="expand-panels-body-4">
            Outdoor
            <svg class="expand-panels__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg>
          </button>
        </h3>
        <div class="expand-panels__body" id="expand-panels-body-4">
          <p class="expand-panels__meta">27 projects · since 2016</p>
          <p class="expand-panels__desc">Decks, patios and lighting that make the garden the best room in the house.</p>
          <a class="expand-panels__link" href="#outdoor">View projects <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </div>
      </li>
      <li class="expand-panels__panel">
        <img class="expand-panels__img" src="basements.jpg" width="1600" height="1200" loading="lazy" decoding="async" alt="Finished basement den with an oak floor and built-in shelving">
        <span class="expand-panels__num" aria-hidden="true">05</span>
        <h3 class="expand-panels__label">
          <button class="expand-panels__toggle" type="button" aria-expanded="true" aria-controls="expand-panels-body-5">
            Basements
            <svg class="expand-panels__icon" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg>
          </button>
        </h3>
        <div class="expand-panels__body" id="expand-panels-body-5">
          <p class="expand-panels__meta">19 projects · since 2018</p>
          <p class="expand-panels__desc">Damp-proofed, insulated and finished as a den, a gym or a guest suite.</p>
          <a class="expand-panels__link" href="#basements">View projects <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </div>
      </li>
    </ul>
  </div>
</section>
```

## CSS

```css
/* Section */
.expand-panels {
  position: relative; overflow: clip;
  background:
    radial-gradient(50rem 28rem at 8% 0%, color-mix(in srgb, var(--primary) 22%, transparent), transparent 70%),
    radial-gradient(40rem 26rem at 100% 100%, color-mix(in srgb, var(--primary-2) 18%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.expand-panels svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.expand-panels__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.expand-panels__head { max-width: 42rem; margin-bottom: clamp(2rem, 4vw, 3rem); }
.expand-panels__eyebrow { display: flex; align-items: center; gap: 0.75rem; margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; }
.expand-panels__eyebrow::before { content: ""; width: 1.5rem; height: 1px; background: var(--gradient-brand); }
.expand-panels__title { margin: 1rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.expand-panels__lead { max-width: 34rem; margin: 1rem 0 0; color: var(--text-inverse-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Without JS: a static grid of open cards. Panel state lives in two variables that every part reads */
.expand-panels__list { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 15rem), 1fr)); gap: var(--space-sm); margin: 0; padding: 0; list-style: none; }
.expand-panels__panel {
  --expand-panels-open: 1; --expand-panels-vis: visible; --expand-panels-tint: var(--primary);
  position: relative; isolation: isolate; display: flex; flex-direction: column; justify-content: flex-end; gap: var(--space-md);
  min-height: 24rem; padding: var(--space-lg); overflow: hidden; border-radius: var(--radius-2xl);
  background: linear-gradient(160deg, color-mix(in srgb, var(--expand-panels-tint) 55%, var(--surface-deep)), var(--surface-deep));
}
.expand-panels__panel:nth-child(2) { --expand-panels-tint: var(--primary-2); }
.expand-panels__panel:nth-child(3) { --expand-panels-tint: var(--accent); }
.expand-panels__panel:nth-child(4) { --expand-panels-tint: color-mix(in srgb, var(--primary-2) 60%, var(--accent)); }
.expand-panels__panel:nth-child(5) { --expand-panels-tint: color-mix(in srgb, var(--primary) 60%, var(--primary-2)); }

/* Photo: dim and desaturated when closed, it brightens and settles as the panel opens */
.expand-panels__img {
  position: absolute; inset: 0; z-index: -2; width: 100%; height: 100%; object-fit: cover;
  transform: scale(calc(1.12 - var(--expand-panels-open) * 0.12));
  filter: brightness(calc(0.45 + var(--expand-panels-open) * 0.55)) saturate(calc(0.6 + var(--expand-panels-open) * 0.4));
  transition: transform var(--dur-5) var(--ease-out), filter var(--dur-4) var(--ease-out);
}
.expand-panels__panel::before, .expand-panels__panel::after { content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none; }
.expand-panels__panel::before { /* bottom scrim under the copy, fades in as the panel opens */
  background: linear-gradient(to top, color-mix(in srgb, var(--surface-deep) 92%, transparent), color-mix(in srgb, var(--surface-deep) 78%, transparent) 11rem, transparent 18rem);
  opacity: var(--expand-panels-open); transition: opacity var(--dur-4) var(--ease-out);
}
.expand-panels__panel::after { /* top scrim under the number and label, plus the hairline */
  background: linear-gradient(to bottom, color-mix(in srgb, var(--surface-deep) 82%, transparent), color-mix(in srgb, var(--surface-deep) 60%, transparent) 7rem, transparent 14rem);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}

/* Number with an underline that draws in when open */
.expand-panels__num { position: absolute; top: var(--space-lg); left: var(--space-lg); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; }
.expand-panels__num::after {
  content: ""; display: block; width: 1.75rem; height: 2px; margin-top: 0.5rem; border-radius: var(--radius-full); background: var(--gradient-brand);
  transform: scaleX(var(--expand-panels-open)); transform-origin: left; transition: transform var(--dur-5) var(--ease-spring);
}

/* Label: the h3 holds the toggle button */
.expand-panels__label { margin: 0; font: 600 clamp(1.375rem, 1.1rem + 1vw, 2rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.expand-panels__toggle {
  display: flex; align-items: center; gap: 0.75rem; min-height: 2.75rem; padding: 0; border: 0; background: none; color: inherit;
  font: inherit; letter-spacing: inherit; text-align: start;
}
.expand-panels__icon { display: none; }

/* Body: hidden from AT while closed; its parts rise in one after another */
.expand-panels__body { display: grid; justify-items: start; gap: 0.75rem; visibility: var(--expand-panels-vis); transition: visibility 0s linear calc((1 - var(--expand-panels-open)) * var(--dur-3)); }
.expand-panels__body > * {
  margin: 0; opacity: var(--expand-panels-open); transform: translateY(calc((1 - var(--expand-panels-open)) * 1rem));
  transition: opacity var(--dur-4) var(--ease-out), transform var(--dur-5) var(--ease-out);
  transition-delay: calc(var(--expand-panels-open) * var(--stagger) * (var(--expand-panels-i, 0) + 3));
}
.expand-panels__body > :nth-child(2) { --expand-panels-i: 1; }
.expand-panels__body > :nth-child(3) { --expand-panels-i: 2; }
.expand-panels__meta { font: 500 0.75rem/1.2 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }
.expand-panels__desc { max-width: 20rem; font-size: 0.9375rem; line-height: 1.5; }
.expand-panels__link {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-size: 0.875rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight), 0 10px 30px -10px color-mix(in srgb, var(--expand-panels-tint) 80%, transparent);
}
.expand-panels__link svg { transition: transform var(--dur-3) var(--ease-spring); }
.expand-panels__link:hover svg { transform: translateX(3px); }
.expand-panels :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
@supports selector(:has(*)) {
  .expand-panels .expand-panels__toggle:focus-visible { outline-color: transparent; }
  .expand-panels__panel:has(.expand-panels__toggle:focus-visible) { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
}

/* With JS: one fixed-height, contained row (a column on phones). flex-grow springs inside it */
.expand-panels--js .expand-panels__list { display: flex; flex-direction: column; gap: var(--space-sm); height: 40rem; contain: size layout; }
.expand-panels--js .expand-panels__panel {
  --expand-panels-open: 0; --expand-panels-vis: hidden;
  flex-grow: calc(1 + var(--expand-panels-open) * 5); flex-shrink: 1; flex-basis: 0; min-width: 0; min-height: 0; padding: 0; cursor: pointer;
  transition: flex-grow var(--dur-5) var(--ease-spring);
}
.expand-panels--js .expand-panels__toggle { cursor: pointer; }
/* Open: the pinned panel or the one holding focus. A hovered panel wins over both */
.expand-panels--js .expand-panels__panel:is(.is-open, :focus-within) { --expand-panels-open: 1; --expand-panels-vis: visible; }
.expand-panels--js .expand-panels__list:focus-within .expand-panels__panel:not(:focus-within) { --expand-panels-open: 0; --expand-panels-vis: hidden; }
@media (hover: hover) {
  .expand-panels--js .expand-panels__list:hover .expand-panels__panel:not(:hover) { --expand-panels-open: 0; --expand-panels-vis: hidden; }
  .expand-panels--js .expand-panels__list:hover .expand-panels__panel:hover { --expand-panels-open: 1; --expand-panels-vis: visible; }
}
/* Phones: drawers. The label stays horizontal, and a plus turns into a cross */
.expand-panels--js .expand-panels__num { top: 1.5rem; left: 1.25rem; }
.expand-panels--js .expand-panels__label { position: absolute; top: 0.5rem; left: 3.5rem; right: 0.75rem; font-size: 1.375rem; }
.expand-panels--js .expand-panels__toggle { width: 100%; justify-content: space-between; }
.expand-panels--js .expand-panels__icon { display: block; transform: rotate(calc(var(--expand-panels-open) * 45deg)); transition: transform var(--dur-4) var(--ease-spring); }
.expand-panels--js .expand-panels__body { position: absolute; left: 1.25rem; right: 1.25rem; bottom: 1.25rem; }

@media (min-width: 768px) {
  .expand-panels--js .expand-panels__list { flex-direction: row; height: clamp(28rem, 72vh, 38rem); }
  .expand-panels--js .expand-panels__num { top: var(--space-lg); left: var(--space-lg); }
  /* Collapsed labels hang vertically from a hinge at their bottom-left corner and swing flat when the panel opens */
  .expand-panels--js .expand-panels__label {
    top: 3.75rem; left: var(--space-lg); right: auto; font-size: clamp(1.5rem, 1.1rem + 1vw, 2rem); white-space: nowrap;
    transform-origin: 0 100%; transform: rotate(calc((1 - var(--expand-panels-open)) * 90deg));
    transition: transform var(--dur-5) var(--ease-spring);
  }
  .expand-panels--js .expand-panels__toggle { width: auto; }
  .expand-panels--js .expand-panels__icon { display: none; }
  /* Fixed width, so the copy never reflows while the panel grows */
  .expand-panels--js .expand-panels__body { left: var(--space-lg); right: auto; bottom: var(--space-lg); width: 20rem; }
}
```

## JS

```js
let instances = 0;

document.querySelectorAll('[data-expand-panels]').forEach((root) => {
  const list = root.querySelector('.expand-panels__list');
  const panels = [...list.querySelectorAll('.expand-panels__panel')];
  const toggles = panels.map((panel) => panel.querySelector('.expand-panels__toggle'));
  const id = ++instances;
  let frame = 0;
  root.classList.add('expand-panels--js');

  // Unique ids per instance, so aria-controls stays valid when the section is repeated
  panels.forEach((panel, i) => {
    const body = panel.querySelector('.expand-panels__body');
    body.id = `expand-panels-${id}-${i + 1}`;
    toggles[i].setAttribute('aria-controls', body.id);
  });

  // aria-expanded mirrors whatever the CSS decided: hover, focus or the pinned panel
  const sync = () => {
    frame = 0;
    panels.forEach((panel, i) => {
      const open = getComputedStyle(panel).getPropertyValue('--expand-panels-open').trim() === '1';
      toggles[i].setAttribute('aria-expanded', String(open));
    });
  };
  const queue = () => {
    frame ||= requestAnimationFrame(sync);
  };

  // A click or tap pins a panel open (on touch screens it's the only way to open one)
  list.addEventListener('click', (e) => {
    const panel = e.target.closest('.expand-panels__panel');
    if (!panel) return;
    panels.forEach((p) => p.classList.toggle('is-open', p === panel));
    queue();
  });
  ['pointerover', 'pointerleave', 'focusin', 'focusout'].forEach((type) => list.addEventListener(type, queue, { passive: true }));
  sync();
});
```

## Notes

- Each trade is an `h3` holding a button that reports `aria-expanded` and controls its body. A closed body is `visibility: hidden`, so it's out of the Tab order and the accessibility tree. Focusing a button opens its panel (`:focus-within`), so the next Tab lands on that panel's link, and Enter or Space pins it open. JS adds the gate class, gives each instance unique ids, pins panels on click or tap, and copies the CSS state (`--expand-panels-open`) into `aria-expanded`. Where `:has()` is supported, the focus ring wraps the whole panel.
- Without JS the section is a static grid of five open cards, with every description and link visible.
- Hover rules apply only on `(hover: hover)` devices, so a tap never leaves a panel stuck open. Hovering previews a panel and wins over keyboard focus; when the pointer leaves, the pinned panel (or the focused one) opens again. Under reduced motion every change is a token transition, so panels snap open with no hinge, rise or settle.
- `flex-grow` is the only layout property that animates, and only inside the row, which has a fixed height and `contain: size layout`, so the reflow never leaves it. The photos are 4:3, so `object-fit: cover` scales them by height and they reveal more of themselves rather than zooming as a panel widens. The body has a fixed width, so its copy doesn't reflow mid-spring.
- Contrast: the label and number sit on a `--surface-deep` top scrim (82% fading to 60%), and the copy on a bottom scrim of 78–92%. That keeps white text at 5:1 or better even over a pure-white photo. Closed photos drop to 45% brightness, so the large vertical labels stay at 4.5:1 or better. Section copy uses `--text-inverse-muted` (6.3:1 or better on the glows). `--expand-panels-tint` colours the gradient shown behind each photo while it loads.
