# Hover-Preview Project List

An editorial index of projects on a light surface: big hairline-separated rows with an index number, a display-font title, category, location, year and an arrow. On desktop, hovering a row summons a floating photo that trails the cursor on a spring and leans into the direction of travel; moving to another row wipes the next photo up over the last one, while the row's title slides right and its arrow turns. Keyboard focus shows the same preview, anchored to the row's right edge. On touch screens and narrow layouts each row carries an inline thumbnail instead. Depends on `tokens/variables.css`.

**Motion:** preview follow on a JS spring (stiffness 110, damping 15, rAF) with velocity-based `rotate` · preview pop-in (`--dur-4` `--ease-spring`) · photo clip-wipe and settle (`clip-path` + `scale`, `--dur-4`/`--dur-5` `--ease-out`) · title slide and arrow turn (`--dur-4` `--ease-spring`).

## HTML

```html
<section class="preview-list" aria-labelledby="preview-list-title" data-preview-list>
  <div class="preview-list__inner">
    <header class="preview-list__head">
      <h2 id="preview-list-title" class="preview-list__heading">Selected work <span class="preview-list__count" aria-hidden="true">(06)</span></h2>
      <p class="preview-list__lead">Recent favourites from Westlake, Northside and Riverside. Every one of them started with a free home visit.</p>
    </header>

    <div class="preview-list__board">
      <ul class="preview-list__rows" role="list">
        <li class="preview-list__item">
          <a class="preview-list__link" href="#walnut-kitchen">
            <span class="preview-list__index" aria-hidden="true">01</span>
            <img class="preview-list__thumb" src="walnut-kitchen.jpg" width="800" height="600" loading="lazy" decoding="async" alt="">
            <span class="preview-list__name">The Walnut Kitchen</span>
            <span class="preview-list__meta">
              <span class="preview-list__cat">Kitchen</span>
              <span class="preview-list__loc">Westlake</span>
              <span class="preview-list__year">2026</span>
            </span>
            <span class="preview-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
          </a>
        </li>
        <li class="preview-list__item">
          <a class="preview-list__link" href="#slate-roof">
            <span class="preview-list__index" aria-hidden="true">02</span>
            <img class="preview-list__thumb" src="slate-roof.jpg" width="800" height="600" loading="lazy" decoding="async" alt="">
            <span class="preview-list__name">Copper &amp; Slate Roof</span>
            <span class="preview-list__meta">
              <span class="preview-list__cat">Roofing</span>
              <span class="preview-list__loc">Northside</span>
              <span class="preview-list__year">2026</span>
            </span>
            <span class="preview-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
          </a>
        </li>
        <li class="preview-list__item">
          <a class="preview-list__link" href="#garden-room">
            <span class="preview-list__index" aria-hidden="true">03</span>
            <img class="preview-list__thumb" src="garden-room.jpg" width="800" height="600" loading="lazy" decoding="async" alt="">
            <span class="preview-list__name">Garden Room Studio</span>
            <span class="preview-list__meta">
              <span class="preview-list__cat">Extension</span>
              <span class="preview-list__loc">Riverside</span>
              <span class="preview-list__year">2025</span>
            </span>
            <span class="preview-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
          </a>
        </li>
        <li class="preview-list__item">
          <a class="preview-list__link" href="#terrazzo-bath">
            <span class="preview-list__index" aria-hidden="true">04</span>
            <img class="preview-list__thumb" src="terrazzo-bath.jpg" width="800" height="600" loading="lazy" decoding="async" alt="">
            <span class="preview-list__name">Terrazzo Bathroom</span>
            <span class="preview-list__meta">
              <span class="preview-list__cat">Bathroom</span>
              <span class="preview-list__loc">Westlake</span>
              <span class="preview-list__year">2025</span>
            </span>
            <span class="preview-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
          </a>
        </li>
        <li class="preview-list__item">
          <a class="preview-list__link" href="#cedar-deck">
            <span class="preview-list__index" aria-hidden="true">05</span>
            <img class="preview-list__thumb" src="cedar-deck.jpg" width="800" height="600" loading="lazy" decoding="async" alt="">
            <span class="preview-list__name">Cedar Deck &amp; Lights</span>
            <span class="preview-list__meta">
              <span class="preview-list__cat">Outdoor</span>
              <span class="preview-list__loc">Riverside</span>
              <span class="preview-list__year">2024</span>
            </span>
            <span class="preview-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
          </a>
        </li>
        <li class="preview-list__item">
          <a class="preview-list__link" href="#basement-den">
            <span class="preview-list__index" aria-hidden="true">06</span>
            <img class="preview-list__thumb" src="basement-den.jpg" width="800" height="600" loading="lazy" decoding="async" alt="">
            <span class="preview-list__name">The Basement Den</span>
            <span class="preview-list__meta">
              <span class="preview-list__cat">Basement</span>
              <span class="preview-list__loc">Northside</span>
              <span class="preview-list__year">2024</span>
            </span>
            <span class="preview-list__arrow" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M7 17 17 7M8 7h9v9" /></svg></span>
          </a>
        </li>
      </ul>
    </div>

    <a class="preview-list__all" href="#work">
      View all 240 projects
      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
    </a>
  </div>
</section>
```

## CSS

```css
/* Section: light and editorial, with type and hairlines doing the work */
.preview-list { overflow: clip; background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.preview-list svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.preview-list__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.preview-list__head { display: grid; gap: var(--space-md); margin-bottom: clamp(2rem, 5vw, 3.5rem); }
.preview-list__heading { margin: 0; font: 600 clamp(2.5rem, 1.2rem + 5.5vw, 5.5rem)/0.95 var(--font-display); letter-spacing: var(--tracking-display); }
.preview-list__count { display: inline-block; margin: 0.3em 0 0 0.2em; vertical-align: top; color: var(--primary); font: 500 max(0.875rem, 0.22em)/1 var(--font-mono); letter-spacing: 0; }
.preview-list__lead { max-width: 26rem; margin: 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Rows: phones stack thumbnail, index, title and meta */
.preview-list__board { position: relative; }
.preview-list__rows { margin: 0; padding: 0; list-style: none; border-bottom: 1px solid var(--border-subtle); }
.preview-list__item { border-top: 1px solid var(--border-subtle); }
.preview-list__link {
  display: grid; grid-template-columns: auto minmax(0, 1fr) auto; grid-template-areas: "thumb index arrow" "thumb name arrow" "thumb meta arrow";
  align-items: center; column-gap: 1rem; row-gap: 0.25rem; padding-block: 1.25rem;
  color: var(--text-main); text-decoration: none; transition: color var(--dur-3) var(--ease-out);
}
.preview-list__index { grid-area: index; color: var(--text-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; transition: color var(--dur-3) var(--ease-out); }
.preview-list__thumb {
  grid-area: thumb; display: block; width: 5.5rem; height: auto; aspect-ratio: 4 / 3; object-fit: cover;
  border-radius: var(--radius-md); background: var(--surface-muted); box-shadow: 0 0 0 1px var(--border-subtle);
}
.preview-list__name { grid-area: name; font: 600 clamp(1.375rem, 0.9rem + 2.6vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; transition: transform var(--dur-4) var(--ease-spring); }
.preview-list__meta { grid-area: meta; display: flex; flex-wrap: wrap; align-items: center; gap: 0.25rem 0.625rem; color: var(--text-muted); font-size: 0.875rem; }
.preview-list__meta > span + span::before { content: ""; display: inline-block; width: 3px; height: 3px; margin-right: 0.625rem; border-radius: 50%; background: currentColor; vertical-align: middle; }
.preview-list__year { font-family: var(--font-mono); font-variant-numeric: tabular-nums; }
.preview-list__arrow {
  grid-area: arrow; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%; box-shadow: inset 0 0 0 1px var(--border-subtle);
  transition: background-color var(--dur-3) var(--ease-out), color var(--dur-3) var(--ease-out), box-shadow var(--dur-3) var(--ease-out);
}
.preview-list__arrow svg { transition: transform var(--dur-4) var(--ease-spring); }

/* Row states: the title slides, the arrow turns, the other rows step back */
.preview-list__link:is(:hover, :focus-visible) .preview-list__name { transform: translateX(0.75rem); }
.preview-list__link:is(:hover, :focus-visible) .preview-list__index { color: var(--primary); }
.preview-list__link:is(:hover, :focus-visible) .preview-list__arrow { background: var(--text-main); color: var(--surface-light); box-shadow: none; }
.preview-list__link:is(:hover, :focus-visible) .preview-list__arrow svg { transform: rotate(45deg); }
.preview-list__link:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; border-radius: var(--radius-md); }
@media (hover: hover) {
  .preview-list__rows:hover .preview-list__link:not(:hover) { color: var(--text-muted); }
}

/* Floating preview (built by JS): position and lean come from the spring */
.preview-list__preview {
  position: absolute; top: 0; left: 0; z-index: 2; width: clamp(14rem, 22vw, 19rem); aspect-ratio: 4 / 3; pointer-events: none;
  translate: -50% -50%; will-change: transform;
  transform: translate3d(var(--preview-list-x, 0px), var(--preview-list-y, 0px), 0) rotate(var(--preview-list-r, 0deg));
}
.preview-list__card {
  position: relative; width: 100%; height: 100%; overflow: hidden; border-radius: var(--radius-xl); background: var(--surface-muted);
  box-shadow: var(--shadow-xl), 0 0 0 1px color-mix(in srgb, var(--text-main) 8%, transparent);
  opacity: 0; transform: scale(0.6); transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring);
}
.preview-list__preview.is-visible .preview-list__card { opacity: 1; transform: none; }
/* The incoming photo wipes up over the last one, which only clears once it's covered */
.preview-list__shot { position: absolute; inset: 0; clip-path: inset(100% 0 0 0); transition: clip-path var(--dur-4) var(--ease-out) var(--dur-4); }
.preview-list__shot.is-active { clip-path: inset(0); transition-delay: 0s; }
.preview-list__shot img { display: block; width: 100%; height: 100%; object-fit: cover; transform: scale(1.15); transition: transform var(--dur-5) var(--ease-out) var(--dur-4); }
.preview-list__shot.is-active img { transform: none; transition-delay: 0s; }

.preview-list__all {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; margin-top: var(--space-xl); color: var(--text-main); font-weight: 600;
  text-decoration: underline 2px; text-decoration-color: var(--border-subtle); text-underline-offset: 0.35em; transition: text-decoration-color var(--dur-2) var(--ease-out);
}
.preview-list__all:hover { text-decoration-color: currentColor; }
.preview-list__all svg { transition: transform var(--dur-3) var(--ease-spring); }
.preview-list__all:hover svg { transform: translateX(3px); }
.preview-list__all:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

@media (min-width: 768px) {
  .preview-list__head { grid-template-columns: 1fr auto; align-items: end; column-gap: var(--space-2xl); }
  .preview-list__link {
    grid-template-columns: 3.5rem auto minmax(0, 1fr) minmax(0, 0.3fr) minmax(0, 0.25fr) 3.75rem 2.75rem;
    grid-template-areas: "index thumb name cat loc year arrow"; column-gap: 0; row-gap: 0; padding-block: clamp(1.25rem, 2.6vw, 2rem);
  }
  .preview-list__thumb { width: 6.5rem; margin-right: 1.5rem; }
  .preview-list__meta { display: contents; }
  .preview-list__meta > span + span::before { display: none; }
  .preview-list__cat { grid-area: cat; }
  .preview-list__loc { grid-area: loc; }
  .preview-list__year { grid-area: year; }
  .preview-list__cat, .preview-list__loc, .preview-list__year { padding-left: var(--space-md); font-size: 0.9375rem; }
}
/* Desktop with a fine pointer: the floating preview replaces the inline thumbnails */
@media (hover: hover) and (pointer: fine) and (min-width: 768px) {
  .preview-list--js .preview-list__thumb { display: none; }
}
```

## JS

```js
document.querySelectorAll('[data-preview-list]').forEach((root) => {
  const board = root.querySelector('.preview-list__board');
  const links = [...board.querySelectorAll('.preview-list__link')];
  const canHover = matchMedia('(hover: hover) and (pointer: fine) and (min-width: 768px)');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));
  root.classList.add('preview-list--js');

  // One floating card, built from each row's thumbnail (decorative: the rows carry the content)
  const preview = document.createElement('div');
  const card = document.createElement('div');
  preview.className = 'preview-list__preview';
  preview.setAttribute('aria-hidden', 'true');
  card.className = 'preview-list__card';
  const shots = links.map((link) => {
    const shot = document.createElement('div');
    const img = link.querySelector('.preview-list__thumb').cloneNode();
    img.removeAttribute('class');
    shot.className = 'preview-list__shot';
    shot.append(img);
    card.append(shot);
    return shot;
  });
  preview.append(card);
  board.append(preview);

  const s = { x: 0, y: 0, vx: 0, vy: 0, tx: 0, ty: 0 };
  let mode = ''; // 'follow' the cursor, or 'anchor' to the row's right side (keyboard, or reduced motion)
  let active = -1;
  let layer = 0;
  let frame = 0;
  let last = 0;
  let snap = false;
  let px = 0;
  let py = 0;

  // Spring (k 110, c 15) toward the target; the lean comes from its velocity. Reduced motion jumps, with no lean
  const tick = (now) => {
    const dt = last ? Math.min((now - last) / 1000, 0.032) : 1 / 60;
    last = now;
    const box = board.getBoundingClientRect();
    const w = preview.offsetWidth;
    if (mode === 'follow') {
      s.tx = clamp(px - box.left + w * 0.5 + 24, w / 2, box.width - w / 2);
      s.ty = py - box.top;
    } else if (active >= 0) {
      const r = links[active].getBoundingClientRect();
      s.tx = box.width - w / 2 - 56;
      s.ty = r.top - box.top + r.height / 2;
    }
    if (snap || reduce.matches) Object.assign(s, { x: s.tx, y: s.ty, vx: 0, vy: 0 });
    s.vx += (110 * (s.tx - s.x) - 15 * s.vx) * dt;
    s.vy += (110 * (s.ty - s.y) - 15 * s.vy) * dt;
    s.x += s.vx * dt;
    s.y += s.vy * dt;
    snap = false;
    preview.style.setProperty('--preview-list-x', `${s.x.toFixed(1)}px`);
    preview.style.setProperty('--preview-list-y', `${s.y.toFixed(1)}px`);
    preview.style.setProperty('--preview-list-r', `${clamp(s.vx * 0.012, -12, 12).toFixed(2)}deg`);
    const moving = Math.abs(s.tx - s.x) + Math.abs(s.ty - s.y) + Math.abs(s.vx) + Math.abs(s.vy) > 0.5;
    frame = moving ? requestAnimationFrame(tick) : 0;
  };
  const wake = () => {
    if (frame) return;
    last = 0;
    frame = requestAnimationFrame(tick);
  };

  // Show row i's photo: the new layer goes on top and wipes up over the previous one
  const show = (i, how) => {
    if (!preview.classList.contains('is-visible')) snap = true;
    mode = reduce.matches ? 'anchor' : how;
    if (i !== active) {
      active = i;
      shots[i].style.zIndex = ++layer;
      shots.forEach((shot, n) => shot.classList.toggle('is-active', n === i));
    }
    preview.classList.add('is-visible');
    wake();
  };
  const hide = () => {
    preview.classList.remove('is-visible');
    shots.forEach((shot) => shot.classList.remove('is-active'));
    active = -1;
    mode = '';
  };

  // Mouse: the row under the cursor picks the photo, and the card trails the cursor
  board.addEventListener('pointermove', (e) => {
    if (e.pointerType !== 'mouse' || !canHover.matches) return;
    px = e.clientX;
    py = e.clientY;
    const link = e.target.closest('.preview-list__link');
    if (link) show(links.indexOf(link), 'follow');
    else if (active >= 0) wake();
  }, { passive: true });
  board.addEventListener('pointerleave', () => {
    const i = links.indexOf(document.activeElement);
    if (i >= 0 && links[i].matches(':focus-visible')) show(i, 'anchor');
    else hide();
  });

  // Keyboard: the preview anchors to the focused row's right side
  board.addEventListener('focusin', (e) => {
    const i = links.indexOf(e.target);
    if (i >= 0 && canHover.matches && e.target.matches(':focus-visible')) show(i, 'anchor');
  });
  board.addEventListener('focusout', (e) => {
    if (!board.contains(e.relatedTarget) && !board.matches(':hover')) hide();
  });
  window.addEventListener('scroll', () => { if (active >= 0) wake(); }, { passive: true });
  canHover.addEventListener('change', hide);
});
```

## Notes

- Every row is a real link, with its title, category, location and year as its accessible name. Index numbers, arrows and the floating preview are `aria-hidden`, and the inline thumbnails have empty `alt` because the title already names the project. Hover and keyboard focus share the same row states: the title slides, the arrow turns, and the other rows fall back to `--text-muted` (still 4.8:1).
- The floating preview only exists with JS, on devices with a fine pointer, hover and at least 768px of width. Everywhere else, including touch screens, narrow layouts and no-JS pages, each row shows its inline thumbnail. The preview clones those thumbnails, so each photo is in the markup only once and lazy-loads.
- Keyboard focus anchors the preview to the right of the focused row, clear of the arrow, and it hides when focus leaves the list. Under reduced motion every hover anchors the same way, with no lag or lean, and the photo wipe is instant (token durations).
- The card follows a damped spring in rAF. It leans by up to 12° in proportion to its own horizontal velocity, stops ticking once it settles, and is clamped inside the list so it never causes overflow. It has `pointer-events: none`, so it never steals hover from the rows.
- Contrast on `--surface-light`: titles 14.6:1, meta and index 4.8:1, the `--primary` count and hover index 5.2:1. To retheme, change the tokens; the row grid is set in one `grid-template-columns` line per breakpoint.
