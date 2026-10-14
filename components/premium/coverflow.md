# 3D Coverflow

Cover Flow, rebuilt for featured projects on a deep stage with a glossy floor: the centre cover faces you, lit and glowing, while the covers either side turn 45° towards it, recede into a fanned stack and are mirrored in the floor. Drag or swipe the stage, scroll sideways on a trackpad, use the arrow keys or click a side cover, and the whole row springs to its new centre while the title and caption below cross-fade. On phones the covers shrink and the fan bleeds off both edges; without JS it's a horizontal scroll-snap row. Depends on `tokens/variables.css`.

**Motion:** cover positions from a per-card `--coverflow-offset` (translate, `translateZ`, `rotateY ±45°`) on a spring (`--dur-5` `--ease-spring`) · drag follows 1:1, then snaps with velocity · side-cover dimming (`filter`, `--ease-out`) · caption cross-fade with blur (`--dur-4`) · button press scale.

## HTML

```html
<section class="coverflow" aria-labelledby="coverflow-title" data-coverflow>
  <div class="coverflow__inner">
    <header class="coverflow__head">
      <p class="coverflow__eyebrow">Featured projects</p>
      <h2 id="coverflow-title" class="coverflow__title">Work we'd happily show the neighbours.</h2>
    </header>

    <div class="coverflow__carousel" role="region" aria-roledescription="carousel" aria-label="Featured projects">
      <div class="coverflow__stage">
        <ul class="coverflow__track" id="coverflow-track" role="list" tabindex="0" aria-label="Projects">
          <li class="coverflow__slide" role="group" aria-roledescription="slide" aria-label="1 of 7">
            <figure class="coverflow__figure">
              <a class="coverflow__card" href="#walnut-kitchen" aria-label="The Walnut Kitchen"><img src="walnut-kitchen.jpg" width="800" height="800" loading="lazy" decoding="async" alt=""></a>
              <figcaption class="coverflow__info"><span class="coverflow__name">The Walnut Kitchen</span><span class="coverflow__meta">Kitchen · Westlake · 2026</span></figcaption>
            </figure>
          </li>
          <li class="coverflow__slide" role="group" aria-roledescription="slide" aria-label="2 of 7">
            <figure class="coverflow__figure">
              <a class="coverflow__card" href="#slate-roof" aria-label="Copper and Slate Roof"><img src="slate-roof.jpg" width="800" height="800" loading="lazy" decoding="async" alt=""></a>
              <figcaption class="coverflow__info"><span class="coverflow__name">Copper &amp; Slate Roof</span><span class="coverflow__meta">Roofing · Northside · 2026</span></figcaption>
            </figure>
          </li>
          <li class="coverflow__slide" role="group" aria-roledescription="slide" aria-label="3 of 7">
            <figure class="coverflow__figure">
              <a class="coverflow__card" href="#garden-room" aria-label="Garden Room Studio"><img src="garden-room.jpg" width="800" height="800" loading="lazy" decoding="async" alt=""></a>
              <figcaption class="coverflow__info"><span class="coverflow__name">Garden Room Studio</span><span class="coverflow__meta">Extension · Riverside · 2025</span></figcaption>
            </figure>
          </li>
          <li class="coverflow__slide" role="group" aria-roledescription="slide" aria-label="4 of 7">
            <figure class="coverflow__figure">
              <a class="coverflow__card" href="#terrazzo-bath" aria-label="Terrazzo Bathroom"><img src="terrazzo-bath.jpg" width="800" height="800" loading="lazy" decoding="async" alt=""></a>
              <figcaption class="coverflow__info"><span class="coverflow__name">Terrazzo Bathroom</span><span class="coverflow__meta">Bathroom · Westlake · 2025</span></figcaption>
            </figure>
          </li>
          <li class="coverflow__slide" role="group" aria-roledescription="slide" aria-label="5 of 7">
            <figure class="coverflow__figure">
              <a class="coverflow__card" href="#cedar-deck" aria-label="Cedar Deck and Lights"><img src="cedar-deck.jpg" width="800" height="800" loading="lazy" decoding="async" alt=""></a>
              <figcaption class="coverflow__info"><span class="coverflow__name">Cedar Deck &amp; Lights</span><span class="coverflow__meta">Outdoor · Riverside · 2025</span></figcaption>
            </figure>
          </li>
          <li class="coverflow__slide" role="group" aria-roledescription="slide" aria-label="6 of 7">
            <figure class="coverflow__figure">
              <a class="coverflow__card" href="#basement-den" aria-label="The Basement Den"><img src="basement-den.jpg" width="800" height="800" loading="lazy" decoding="async" alt=""></a>
              <figcaption class="coverflow__info"><span class="coverflow__name">The Basement Den</span><span class="coverflow__meta">Basement · Northside · 2024</span></figcaption>
            </figure>
          </li>
          <li class="coverflow__slide" role="group" aria-roledescription="slide" aria-label="7 of 7">
            <figure class="coverflow__figure">
              <a class="coverflow__card" href="#sash-windows" aria-label="Heritage Sash Windows"><img src="sash-windows.jpg" width="800" height="800" loading="lazy" decoding="async" alt=""></a>
              <figcaption class="coverflow__info"><span class="coverflow__name">Heritage Sash Windows</span><span class="coverflow__meta">Windows · Springfield · 2024</span></figcaption>
            </figure>
          </li>
        </ul>
      </div>

      <div class="coverflow__captions" aria-hidden="true"></div>

      <div class="coverflow__controls" hidden>
        <button class="coverflow__btn" type="button" data-coverflow-prev aria-label="Previous project" aria-controls="coverflow-track">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M15 6l-6 6 6 6" /></svg>
        </button>
        <p class="coverflow__counter" aria-hidden="true"><span class="coverflow__current">4</span> / <span class="coverflow__total">7</span></p>
        <button class="coverflow__btn" type="button" data-coverflow-next aria-label="Next project" aria-controls="coverflow-track">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M9 6l6 6-6 6" /></svg>
        </button>
      </div>
      <p class="coverflow__sr" aria-live="polite" data-coverflow-status></p>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: a deep stage. Cover size and the two spacing steps drive the whole layout */
.coverflow {
  --coverflow-card: clamp(11rem, 7rem + 16vw, 17.5rem);
  --coverflow-step-near: calc(var(--coverflow-card) * 0.66); /* centre to first side cover */
  --coverflow-step-far: calc(var(--coverflow-card) * 0.22);  /* between stacked side covers */
  position: relative; overflow: clip;
  background:
    radial-gradient(60rem 30rem at 50% 32%, color-mix(in srgb, var(--primary) 20%, transparent), transparent 70%),
    radial-gradient(40rem 20rem at 50% 100%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.coverflow svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.coverflow__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.coverflow__head { max-width: 40rem; margin: 0 auto clamp(1.5rem, 4vw, 2.5rem); text-align: center; }
.coverflow__eyebrow { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; }
.coverflow__title { margin: 1rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }

/* Without JS: a scroll-snap row with a caption under each cover */
.coverflow__track {
  display: flex; gap: var(--space-lg); margin: 0; padding: var(--space-sm) var(--space-xs) var(--space-lg);
  list-style: none; overflow-x: auto; scroll-snap-type: x mandatory; overscroll-behavior-x: contain; scrollbar-width: thin;
}
.coverflow__slide { flex: 0 0 min(72%, 16rem); scroll-snap-align: center; }
.coverflow__figure { margin: 0; }
.coverflow__card {
  position: relative; display: block; aspect-ratio: 1; border-radius: var(--radius-xl); color: inherit;
  background: linear-gradient(145deg, color-mix(in srgb, var(--primary) 50%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 40%, var(--surface-deep)));
  box-shadow: 0 24px 50px -24px color-mix(in srgb, var(--surface-deep) 90%, transparent);
}
.coverflow__card img { display: block; width: 100%; height: 100%; object-fit: cover; border-radius: inherit; }
.coverflow__card::before { /* gloss and hairline */
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(155deg, color-mix(in srgb, var(--text-inverse) 16%, transparent), transparent 38%);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.coverflow__info { display: grid; gap: 0.375rem; margin-top: var(--space-md); }
.coverflow__name { font: 600 clamp(1.125rem, 1rem + 0.8vw, 1.625rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.coverflow__meta { color: var(--text-inverse-muted); font: 500 0.8125rem/1.3 var(--font-mono); letter-spacing: 0.04em; }

/* With JS: covers stand on a glossy floor inside a perspective stage */
.coverflow--js .coverflow__stage {
  position: relative; height: calc(var(--coverflow-card) * 1.45 + 2.5rem); perspective: 1100px;
  touch-action: pan-y; cursor: grab; -webkit-user-select: none; user-select: none;
}
.coverflow.is-dragging .coverflow__stage { cursor: grabbing; }
.coverflow--js .coverflow__stage::before {
  content: ""; position: absolute; top: calc(1.5rem + var(--coverflow-card) + 0.25rem); bottom: 0; left: 50%; width: min(100vw, 72rem); translate: -50% 0; pointer-events: none;
  border-top: 1px solid var(--border-inverse);
  background:
    radial-gradient(50% 80% at 50% 0%, color-mix(in srgb, var(--text-inverse) 10%, transparent), transparent 70%),
    linear-gradient(to bottom, color-mix(in srgb, var(--primary) 12%, transparent), transparent 85%);
  -webkit-mask-image: linear-gradient(90deg, transparent, black 22%, black 78%, transparent);
  mask-image: linear-gradient(90deg, transparent, black 22%, black 78%, transparent);
}
.coverflow--js .coverflow__track { display: block; height: 100%; padding: 0; overflow: visible; }

/* Each cover is placed from --coverflow-offset (its distance from the centre, fractional while dragging):
   up to ±1 it slides out by the near step and turns to ±45°; beyond that it stacks by the far step */
.coverflow--js .coverflow__slide {
  --coverflow-near: clamp(-1, var(--coverflow-offset, 0), 1);
  --coverflow-far: calc(var(--coverflow-offset, 0) - var(--coverflow-near));
  --coverflow-dist: max(var(--coverflow-offset, 0), -1 * var(--coverflow-offset, 0));
  position: absolute; top: 1.5rem; left: 50%; width: var(--coverflow-card); margin-left: calc(var(--coverflow-card) / -2);
  transform:
    translateX(calc(var(--coverflow-near) * var(--coverflow-step-near) + var(--coverflow-far) * var(--coverflow-step-far)))
    translateZ(calc(min(var(--coverflow-dist), 1) * -11rem - max(var(--coverflow-dist) - 1, 0) * 1.5rem))
    rotateY(calc(var(--coverflow-near) * -45deg));
  opacity: clamp(0, 4 - var(--coverflow-dist), 1);
  transition: transform var(--dur-5) var(--ease-spring), opacity var(--dur-4) var(--ease-out);
}
.coverflow--js .coverflow__slide.is-far { pointer-events: none; }
.coverflow--js .coverflow__card {
  filter: brightness(calc(1 - min(var(--coverflow-dist), 1) * 0.42));
  -webkit-box-reflect: below 0.375rem linear-gradient(transparent 58%, color-mix(in srgb, black 30%, transparent));
  transition: filter var(--dur-5) var(--ease-out), box-shadow var(--dur-4) var(--ease-out);
}
.coverflow--js .coverflow__slide.is-current .coverflow__card {
  box-shadow: 0 28px 70px -24px color-mix(in srgb, var(--primary) 65%, transparent), 0 0 0 1px color-mix(in srgb, var(--text-inverse) 14%, transparent);
}
.coverflow.is-dragging .coverflow__slide, .coverflow.is-dragging .coverflow__card { transition: none; }
/* Browsers without box-reflect (Firefox): a mirrored, masked copy of the photo */
@supports not (-webkit-box-reflect: below) {
  .coverflow--js .coverflow__card::after {
    content: ""; position: absolute; top: calc(100% + 0.375rem); left: 0; width: 100%; height: 100%; border-radius: inherit; pointer-events: none; opacity: 0.3;
    background: var(--coverflow-img, none) center / cover, linear-gradient(145deg, color-mix(in srgb, var(--primary) 50%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 40%, var(--surface-deep)));
    transform: scaleY(-1);
    -webkit-mask-image: linear-gradient(to top, black, transparent 42%);
    mask-image: linear-gradient(to top, black, transparent 42%);
  }
}

/* Captions: the slide's own figcaption stays for AT; a visual copy cross-fades under the stage */
.coverflow--js .coverflow__info { position: absolute; width: 1px; height: 1px; margin: 0; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.coverflow__captions { display: grid; justify-items: center; text-align: center; }
.coverflow__caption {
  grid-area: 1 / 1; display: grid; gap: 0.375rem; opacity: 0; transform: translateY(0.5rem); filter: blur(6px);
  transition: opacity var(--dur-4) var(--ease-out), transform var(--dur-4) var(--ease-out), filter var(--dur-4) var(--ease-out);
}
.coverflow__caption.is-current { opacity: 1; transform: none; filter: none; }

/* Controls */
.coverflow__controls { display: flex; align-items: center; justify-content: center; gap: var(--space-md); margin-top: var(--space-lg); }
.coverflow__controls[hidden] { display: none; }
.coverflow__btn {
  display: grid; place-items: center; width: 3rem; height: 3rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: background-color var(--dur-2) var(--ease-out), transform var(--dur-3) var(--ease-spring), opacity var(--dur-2) var(--ease-out);
}
.coverflow__btn:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.coverflow__btn:active { transform: scale(0.92); }
.coverflow__btn[aria-disabled="true"] { opacity: 0.4; cursor: default; transform: none; }
.coverflow :is(a, button, .coverflow__track):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.coverflow__counter { min-width: 4.5rem; margin: 0; color: var(--text-inverse-muted); font: 500 0.875rem/1 var(--font-mono); text-align: center; font-variant-numeric: tabular-nums; }
.coverflow__current { color: var(--text-inverse); font-weight: 600; }
.coverflow__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
```

## JS

```js
let instances = 0;

document.querySelectorAll('[data-coverflow]').forEach((root) => {
  const stage = root.querySelector('.coverflow__stage');
  const track = root.querySelector('.coverflow__track');
  const slides = [...track.querySelectorAll('.coverflow__slide')];
  const cards = slides.map((slide) => slide.querySelector('.coverflow__card'));
  const status = root.querySelector('[data-coverflow-status]');
  const counter = root.querySelector('.coverflow__current');
  const prev = root.querySelector('[data-coverflow-prev]');
  const next = root.querySelector('[data-coverflow-next]');
  const last = slides.length - 1;
  let index = Math.floor(slides.length / 2);
  let pos = index;
  let drag = null;
  let moved = false;
  let frame = 0;
  let wheel = 0;
  let wheelTimer = 0;

  root.classList.add('coverflow--js');
  root.querySelector('.coverflow__controls').hidden = false;
  root.querySelector('.coverflow__total').textContent = slides.length;
  track.removeAttribute('tabindex');
  track.id = `coverflow-track-${++instances}`;
  [prev, next].forEach((btn) => btn.setAttribute('aria-controls', track.id));

  // Visual captions: aria-hidden copies of each figcaption that cross-fade under the stage
  const lines = slides.map((slide) => {
    const line = document.createElement('div');
    line.className = 'coverflow__caption';
    line.innerHTML = slide.querySelector('.coverflow__info').innerHTML;
    root.querySelector('.coverflow__captions').append(line);
    return line;
  });
  // Without -webkit-box-reflect, the mirrored ::after fallback needs each photo as a variable
  if (!CSS.supports('-webkit-box-reflect', 'below')) {
    cards.forEach((card) => card.style.setProperty('--coverflow-img', `url("${card.querySelector('img').src}")`));
  }

  // Every cover is placed from its offset to the (possibly fractional) centre position
  const render = () => {
    frame = 0;
    slides.forEach((slide, i) => {
      const off = i - pos;
      slide.style.setProperty('--coverflow-offset', off.toFixed(3));
      slide.style.zIndex = String(100 - Math.round(Math.abs(off) * 10));
      slide.classList.toggle('is-far', Math.abs(off) > 3.5);
    });
  };

  // Settle on a cover: slide visibility for AT, roving tabindex, caption, counter, announcement
  const go = (i, focus = false) => {
    const target = Math.max(0, Math.min(last, i));
    const changed = target !== index;
    index = target;
    pos = target;
    render();
    slides.forEach((slide, n) => {
      const on = n === index;
      slide.classList.toggle('is-current', on);
      if (on) slide.removeAttribute('aria-hidden');
      else slide.setAttribute('aria-hidden', 'true');
      cards[n].tabIndex = on ? 0 : -1;
      lines[n].classList.toggle('is-current', on);
    });
    counter.textContent = index + 1;
    prev.setAttribute('aria-disabled', String(index === 0));
    next.setAttribute('aria-disabled', String(index === last));
    if (changed) status.textContent = `${slides[index].getAttribute('aria-label')}: ${cards[index].getAttribute('aria-label')}`;
    if (focus) cards[index].focus({ preventScroll: true });
  };

  prev.addEventListener('click', () => go(index - 1));
  next.addEventListener('click', () => go(index + 1));
  root.querySelector('.coverflow__carousel').addEventListener('keydown', (e) => {
    const keys = { ArrowLeft: index - 1, ArrowRight: index + 1, Home: 0, End: last };
    if (!(e.key in keys)) return;
    e.preventDefault();
    go(keys[e.key], track.contains(document.activeElement));
  });

  // A side cover's click brings it to the centre; only the centre cover follows its link. A drag is never a click
  stage.addEventListener('click', (e) => {
    const card = e.target.closest('.coverflow__card');
    const side = card && card !== cards[index];
    if (moved || side) e.preventDefault();
    if (!moved && side) go(cards.indexOf(card));
    moved = false;
  });

  // Drag or swipe: the row follows the pointer 1:1, then springs to the nearest cover, carried by the fling
  stage.addEventListener('pointerdown', (e) => {
    if (e.button > 0) return;
    drag = { x: e.clientX, from: pos, step: cards[0].offsetWidth * 0.56, prevX: e.clientX, t: e.timeStamp, v: 0 };
    moved = false;
  });
  stage.addEventListener('pointermove', (e) => {
    if (!drag) return;
    const dx = e.clientX - drag.x;
    if (!moved && Math.abs(dx) < 6) return;
    if (!moved) {
      moved = true;
      stage.setPointerCapture(e.pointerId);
      root.classList.add('is-dragging');
    }
    drag.v = 0.7 * ((e.clientX - drag.prevX) / Math.max(e.timeStamp - drag.t, 1)) + 0.3 * drag.v;
    drag.prevX = e.clientX;
    drag.t = e.timeStamp;
    pos = Math.max(-0.4, Math.min(last + 0.4, drag.from - dx / drag.step));
    frame ||= requestAnimationFrame(render);
  }, { passive: true });
  const drop = (e) => {
    if (!drag) return;
    const v = e.timeStamp - drag.t < 80 ? drag.v : 0;
    const { step } = drag;
    drag = null;
    if (!moved) return;
    root.classList.remove('is-dragging');
    go(Math.round(pos - (v * 220) / step));
  };
  stage.addEventListener('pointerup', drop);
  stage.addEventListener('pointercancel', drop);
  stage.addEventListener('dragstart', (e) => e.preventDefault()); // links and photos never start a native drag

  // Sideways trackpad scrolling (or Shift + wheel) steps through covers; vertical scrolling is left to the page
  stage.addEventListener('wheel', (e) => {
    if (Math.abs(e.deltaX) <= Math.abs(e.deltaY)) return;
    e.preventDefault();
    wheel += e.deltaX;
    clearTimeout(wheelTimer);
    wheelTimer = setTimeout(() => { wheel = 0; }, 180);
    if (Math.abs(wheel) < 60) return;
    go(index + Math.sign(wheel));
    wheel = 0;
  }, { passive: false });

  go(index);
});
```

## Notes

- This follows the APG carousel pattern: a `region` with `aria-roledescription="carousel"`, slides as `group`s labelled "3 of 7", and Prev/Next buttons that set `aria-disabled` at either end. Only the centre slide is exposed to AT (the side covers are `aria-hidden` previews) and only its link is tabbable. ←/→/Home/End work anywhere in the carousel, and focus follows the centre cover when it was on a cover. A polite live region announces "4 of 7: Terrazzo Bathroom", while the visible counter and the cross-fading captions are `aria-hidden`.
- Without JS it's a horizontal scroll-snap row (focusable for keyboard scrolling) with each project's caption under its cover. With JS the covers fan out from the centre on load.
- Positions come only from `--coverflow-offset`, through `clamp()`/`max()` in CSS, so a fractional offset while dragging and a whole-number offset at rest share one formula. `--coverflow-card` and the two step variables re-proportion the whole fan. Under reduced motion every move is instant (token durations), while a drag still tracks the pointer.
- Reflections use `-webkit-box-reflect` with a gradient mask (Chrome, Edge, Safari). Elsewhere a masked, mirrored `::after` copy of the photo stands in. Horizontal wheel input calls `preventDefault()`, so that listener is non-passive; vertical wheel input is never touched. The stage uses `touch-action: pan-y`, so phones can still scroll the page past it.
- Contrast on `--surface-deep` and its glows: titles and the counter 18.8:1, meta text `--text-inverse-muted` 6.3:1 or better. Side covers dim to 58% brightness as a depth cue; the photos carry no text.
