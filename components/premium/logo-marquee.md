# Logo Marquee

Two rows of partner logos gliding in opposite directions, fading out at the edges. Hovering a row eases it down to a crawl rather than stopping dead, and the pause button glides everything to a halt. Under reduced motion, or without JS, the logos sit in a still, centred grid. Depends on `tokens/variables.css`.

**Motion:** Web Animations API loops at a constant pixel speed · playback rate eased on hover (no jump) · edge fade masks · logo colour lift on hover.

## HTML

```html
<section class="logo-marquee" aria-labelledby="logo-marquee-title" data-logo-marquee data-speed="40">
  <div class="logo-marquee__inner">
    <p id="logo-marquee-title" class="logo-marquee__title">Trusted by <strong>2,000+</strong> homeowners, landlords and local businesses</p>

    <div class="logo-marquee__row">
      <ul class="logo-marquee__list" role="list">
        <li class="logo-marquee__logo"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15H5zM5 19l7-7" /></svg>Northwind</li>
        <li class="logo-marquee__logo logo-marquee__logo--caps"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 20 9 10l4 6 2-3 6 7z" /></svg>Summit Supply</li>
        <li class="logo-marquee__logo logo-marquee__logo--italic"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg>Brightline</li>
        <li class="logo-marquee__logo logo-marquee__logo--serif"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M2 12c3-3 5-3 8 0s5 3 8 0 4-2 4-2M2 17c3-3 5-3 8 0s5 3 8 0 4-2 4-2" /></svg>Harbor &amp; Co</li>
        <li class="logo-marquee__logo"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 2 5 8h-3l4 6h-5v6h-2v-6H6l4-6H7z" /></svg>Evergreen</li>
        <li class="logo-marquee__logo logo-marquee__logo--light"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 2 9 10-9 10-9-10zM12 7l4.5 5-4.5 5-4.5-5z" /></svg>Keystone</li>
        <li class="logo-marquee__logo logo-marquee__logo--caps"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM12 2v2M12 20v2M2 12h2M20 12h2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5" /></svg>Solstice</li>
      </ul>
    </div>

    <div class="logo-marquee__row logo-marquee__row--reverse">
      <ul class="logo-marquee__list" role="list">
        <li class="logo-marquee__logo logo-marquee__logo--serif"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 21v-6M12 3a6 6 0 0 0-6 6c0 3 2.5 5 6 5s6-2 6-5a6 6 0 0 0-6-6z" /></svg>Oakridge Homes</li>
        <li class="logo-marquee__logo"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 15c0-4 4-8 9-8s7 3 7 6-3 5-8 5-8-1-8-3z" /></svg>Riverstone</li>
        <li class="logo-marquee__logo logo-marquee__logo--caps"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m12 2 8 5v10l-8 5-8-5V7z" /></svg>Ironwood</li>
        <li class="logo-marquee__logo logo-marquee__logo--italic"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M3 12c4 0 6-4 10-4 3 0 5 2 8 2-2 2-4 3-6 3l-3 5-2-4c-3 0-5-1-7-2z" /></svg>Bluebird Realty</li>
        <li class="logo-marquee__logo logo-marquee__logo--light"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m3 11 9-7 9 7v9H3zM9 20v-5h6v5" /></svg>Fieldhouse</li>
        <li class="logo-marquee__logo"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3 21 19H3z" /></svg>Cobalt Labs</li>
        <li class="logo-marquee__logo logo-marquee__logo--serif"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3c3 3 3 15 0 18" /></svg>Meridian</li>
      </ul>
    </div>

    <button class="logo-marquee__pause" type="button" aria-pressed="false" hidden>
      <svg class="logo-marquee__icon-pause" viewBox="0 0 24 24" width="12" height="12" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
      <svg class="logo-marquee__icon-play" viewBox="0 0 24 24" width="12" height="12" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
      <span>Pause logos</span>
    </button>
  </div>
</section>
```

## CSS

```css
/* Section */
.logo-marquee { background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.logo-marquee__inner { position: relative; max-width: var(--container-max); margin-inline: auto; padding-block: clamp(3rem, 6vw, 4.5rem); }
.logo-marquee__title { margin: 0 0 2.25rem; padding-inline: var(--gutter); text-align: center; color: var(--text-muted); font-size: 0.9375rem; }
.logo-marquee__title strong { color: var(--text-main); }

/* Rows fade out at both edges */
.logo-marquee__row {
  overflow: hidden;
  -webkit-mask-image: linear-gradient(90deg, transparent, black 12%, black 88%, transparent);
  mask-image: linear-gradient(90deg, transparent, black 12%, black 88%, transparent);
}
.logo-marquee__row + .logo-marquee__row { margin-top: 1.5rem; }

/* Static layout: a centred, wrapping grid (no JS, or reduced motion) */
.logo-marquee__list { display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem 3rem; margin: 0; padding: 0 var(--gutter); list-style: none; }

/* Moving layout: the list and its copy side by side, spaced so the loop is seamless */
.logo-marquee__mover { display: flex; width: max-content; will-change: transform; }
.logo-marquee--js .logo-marquee__list { flex-wrap: nowrap; gap: 3rem; padding: 0 1.5rem; }

/* Wordmarks: each set in its own voice, muted until hovered */
.logo-marquee__logo {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 2.5rem;
  color: var(--text-muted); font: 650 1.1875rem/1 var(--font-display); letter-spacing: -0.03em; white-space: nowrap;
  transition: color var(--dur-2);
}
.logo-marquee__logo:hover { color: var(--text-main); }
.logo-marquee__logo svg { width: 1.5rem; height: 1.5rem; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.logo-marquee__logo--caps { font-size: 0.9375rem; font-weight: 700; letter-spacing: 0.16em; text-transform: uppercase; }
.logo-marquee__logo--italic { font-style: italic; font-weight: 800; letter-spacing: -0.04em; }
.logo-marquee__logo--serif { font-family: Georgia, "Times New Roman", serif; font-weight: 600; letter-spacing: 0; }
.logo-marquee__logo--light { font-weight: 400; letter-spacing: 0; }

/* Pause control (WCAG 2.2.2) */
.logo-marquee__pause {
  position: absolute; right: var(--gutter); bottom: 0.75rem; display: inline-flex; align-items: center; gap: 0.375rem;
  height: 1.75rem; padding: 0 0.625rem; border: 0; border-radius: 999px; cursor: pointer;
  background: color-mix(in srgb, var(--text-main) 5%, transparent); color: var(--text-muted);
  font: 500 0.75rem var(--font-sans); transition: color var(--dur-2), background-color var(--dur-2);
}
.logo-marquee__pause:hover { color: var(--text-main); background: color-mix(in srgb, var(--text-main) 9%, transparent); }
.logo-marquee__pause:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.logo-marquee__pause[hidden] { display: none; }
.logo-marquee__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.logo-marquee__icon-play, .logo-marquee__pause[aria-pressed="true"] .logo-marquee__icon-pause { display: none; }
.logo-marquee__pause[aria-pressed="true"] .logo-marquee__icon-play { display: block; }
```

## JS

```js
document.querySelectorAll('[data-logo-marquee]').forEach((root) => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return; // stays a still grid
  const speed = Number(root.dataset.speed) || 40; // px per second
  const pause = root.querySelector('.logo-marquee__pause');
  let paused = false;

  // Ease the playback rate towards a target instead of snapping (no visual jump)
  const glide = (anim, target) => {
    cancelAnimationFrame(anim.glideFrame);
    const step = () => {
      const next = anim.playbackRate + (target - anim.playbackRate) * 0.12;
      anim.playbackRate = Math.abs(target - next) < 0.01 ? target : next;
      if (anim.playbackRate !== target) anim.glideFrame = requestAnimationFrame(step);
    };
    step();
  };

  // Build after fonts load so the measured width (and loop speed) is exact
  document.fonts.ready.then(() => {
    root.classList.add('logo-marquee--js');
    const anims = [...root.querySelectorAll('.logo-marquee__row')].map((row) => {
      const list = row.querySelector('.logo-marquee__list');
      const copy = list.cloneNode(true);
      copy.setAttribute('aria-hidden', 'true');
      const mover = document.createElement('div');
      mover.className = 'logo-marquee__mover';
      list.replaceWith(mover);
      mover.append(list, copy);
      const anim = mover.animate([{ transform: 'translateX(0)' }, { transform: 'translateX(-50%)' }], {
        duration: (list.offsetWidth / speed) * 1000,
        iterations: Infinity,
        direction: row.classList.contains('logo-marquee__row--reverse') ? 'reverse' : 'normal',
      });
      row.addEventListener('pointerenter', () => { if (!paused) glide(anim, 0.15); });
      row.addEventListener('pointerleave', () => { if (!paused) glide(anim, 1); });
      return anim;
    });

    pause.hidden = false;
    pause.addEventListener('click', () => {
      paused = !paused;
      pause.setAttribute('aria-pressed', String(paused));
      anims.forEach((anim) => glide(anim, paused ? 0 : 1));
    });
  });
});
```

## Notes

- The visible list is the real content; the copy that makes the loop seamless is `aria-hidden`. Screen readers hear each logo once.
- Speed is set in pixels per second (`data-speed`), so short and long rows move at the same pace.
- Logos are generic placeholders. Swap in real marks as inline SVG (keep `aria-hidden` on the icon and the company name as text) or `<img alt="Company">`.
- Hover slows rather than stops, so the row never freezes mid-glance. The pause button meets WCAG 2.2.2 (motion running longer than 5s).
- On a dark section, set `.logo-marquee { background: var(--surface-deep) }` and change the logo colours to `--text-inverse-muted` / `--text-inverse`.
