# Testimonial Wall

A wall of reviews whose columns drift in opposite directions, fading in and out at the top and bottom edges. Hovering a column eases it to a crawl so it can be read, and a pause button stops the whole wall. One column on phones, two on tablets, three on desktop. Without JS or under reduced motion it's a still, masked grid. Depends on `tokens/variables.css`.

**Motion:** vertical loops at constant pixel speed (Web Animations API) · eased hover slow-down · card lift with a hint of tilt · gradient-border featured review.

## HTML

```html
<section class="testimonial-wall" aria-labelledby="testimonial-wall-title" data-testimonial-wall>
  <div class="testimonial-wall__inner">
    <header class="testimonial-wall__head">
      <p class="testimonial-wall__eyebrow">Reviews</p>
      <h2 id="testimonial-wall-title" class="testimonial-wall__title">Springfield's most recommended crew</h2>
      <p class="testimonial-wall__summary"><span class="testimonial-wall__stars" aria-hidden="true">★★★★★</span><strong>4.9</strong> average from 1,248 verified reviews</p>
    </header>

    <div class="testimonial-wall__cols">
      <div class="testimonial-wall__col" data-speed="34">
        <ul class="testimonial-wall__list" role="list">
          <li><figure class="testimonial-wall__card testimonial-wall__card--featured">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>They quoted on the spot, showed up the next morning and were done by lunch. The price on the invoice was the price on the quote. That never happens.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">ML</span><span><strong>Maria Lopez</strong><small>Westlake · Water heater</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>Burst pipe at 11pm. A real person answered and Sam was here in 40 minutes.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">DK</span><span><strong>Daniel Kim</strong><small>Northside · Emergency</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>Shoe covers, drop cloths, and they vacuumed when they finished. Cleaner than before they came.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">AP</span><span><strong>Aisha Patel</strong><small>Riverside · Kitchen</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="4 out of 5 stars">★★★★☆</p>
            <blockquote><p>Had to reschedule once, but they called ahead and knocked 10% off. Great work.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">TB</span><span><strong>Tom Becker</strong><small>Downtown · Inspection</small></span></figcaption>
          </figure></li>
        </ul>
      </div>

      <div class="testimonial-wall__col testimonial-wall__col--reverse" data-speed="28">
        <ul class="testimonial-wall__list" role="list">
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>The live map is brilliant. I knew exactly when to leave work to meet them.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">JM</span><span><strong>Jess Morgan</strong><small>Northside · Leak repair</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>Third company we called and the only one that explained what was actually wrong. Fixed for half what the others quoted.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">RS</span><span><strong>Rafael Silva</strong><small>Westlake · Boiler</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card testimonial-wall__card--featured">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>We manage 40 rentals. Brand is the only contractor our tenants compliment. Booking, invoices, photos: all in one place.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">KO</span><span><strong>Kemi Okafor</strong><small>Property manager</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>Friendly, fast, fair. Booked them again for the bathroom.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">LT</span><span><strong>Lena Tran</strong><small>Riverside · Plumbing</small></span></figcaption>
          </figure></li>
        </ul>
      </div>

      <div class="testimonial-wall__col" data-speed="40">
        <ul class="testimonial-wall__list" role="list">
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>The 5-year guarantee sold me. A part failed after two years; they swapped it the same week, free.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">GH</span><span><strong>Grace Hall</strong><small>Downtown · Heating</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>Online booking took a minute. Confirmation, reminder, arrival text. Effortless.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">OB</span><span><strong>Omar Brooks</strong><small>Westlake · Maintenance</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>Honest advice: they told me I didn't need a new unit yet. Saved us thousands.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">SC</span><span><strong>Sofia Costa</strong><small>Northside · AC repair</small></span></figcaption>
          </figure></li>
          <li><figure class="testimonial-wall__card">
            <p class="testimonial-wall__rating" role="img" aria-label="5 out of 5 stars">★★★★★</p>
            <blockquote><p>Polite, on time, tidy. Exactly what you want in your home.</p></blockquote>
            <figcaption><span class="testimonial-wall__avatar">EW</span><span><strong>Ethan Wright</strong><small>Riverside · Inspection</small></span></figcaption>
          </figure></li>
        </ul>
      </div>
    </div>

    <button class="testimonial-wall__pause" type="button" aria-pressed="false" hidden>
      <svg class="testimonial-wall__icon-pause" viewBox="0 0 24 24" width="12" height="12" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
      <svg class="testimonial-wall__icon-play" viewBox="0 0 24 24" width="12" height="12" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
      <span>Pause reviews</span>
    </button>
  </div>
</section>
```

## CSS

```css
/* Section and heading */
.testimonial-wall { background: var(--surface-muted); color: var(--text-main); font-family: var(--font-sans); }
.testimonial-wall__inner { position: relative; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.testimonial-wall__head { max-width: 40rem; margin: 0 auto 3rem; text-align: center; }
.testimonial-wall__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.testimonial-wall__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.testimonial-wall__summary { display: inline-flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.5rem; margin: 1.25rem 0 0; color: var(--text-muted); font-size: 0.9375rem; }
.testimonial-wall__summary strong { color: var(--text-main); }
.testimonial-wall__stars { color: var(--accent); letter-spacing: 0.1em; }

/* The wall: fixed height, soft fade top and bottom */
.testimonial-wall__cols {
  display: grid; gap: 1rem; height: 40rem; overflow: hidden;
  -webkit-mask-image: linear-gradient(transparent, black 14%, black 86%, transparent);
  mask-image: linear-gradient(transparent, black 14%, black 86%, transparent);
}
.testimonial-wall__col:nth-child(n + 2) { display: none; }
@media (min-width: 640px) {
  .testimonial-wall__cols { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .testimonial-wall__col:nth-child(2) { display: block; }
}
@media (min-width: 1024px) {
  .testimonial-wall__cols { grid-template-columns: repeat(3, minmax(0, 1fr)); height: 44rem; }
  .testimonial-wall__col:nth-child(3) { display: block; }
}
.testimonial-wall__list { display: grid; gap: 1rem; margin: 0; padding: 0 0 1rem; list-style: none; }
.testimonial-wall__mover { will-change: transform; }

/* Review card */
.testimonial-wall__card {
  margin: 0; padding: 1.5rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: transform var(--dur-4) var(--ease-out), box-shadow var(--dur-4) var(--ease-out);
}
.testimonial-wall__card:hover { transform: translateY(-3px) rotate(-0.4deg); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl); }
.testimonial-wall__card--featured {
  border: 1.5px solid transparent;
  background: linear-gradient(var(--surface-light), var(--surface-light)) padding-box, var(--gradient-brand) border-box;
  box-shadow: 0 18px 40px -20px color-mix(in srgb, var(--primary) 55%, transparent);
}
.testimonial-wall__card--featured blockquote p { font: 500 1.0625rem/1.55 var(--font-display); letter-spacing: -0.01em; }
.testimonial-wall__rating { margin: 0; color: var(--accent); font-size: 0.875rem; letter-spacing: 0.12em; }
.testimonial-wall__card blockquote { margin: 0.75rem 0 0; }
.testimonial-wall__card blockquote p { margin: 0; font-size: 0.9375rem; line-height: 1.6; }
.testimonial-wall__card figcaption { display: flex; align-items: center; gap: 0.75rem; margin-top: 1.25rem; }
.testimonial-wall__card strong { display: block; font-size: 0.875rem; font-weight: 600; }
.testimonial-wall__card small { display: block; color: var(--text-muted); font-size: 0.8125rem; }
.testimonial-wall__avatar {
  flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: var(--gradient-brand); color: var(--text-inverse); font-size: 0.75rem; font-weight: 700;
}
.testimonial-wall__list > li:nth-child(3n + 2) .testimonial-wall__avatar { background: linear-gradient(135deg, var(--primary-2), var(--surface-deep)); }
.testimonial-wall__list > li:nth-child(3n) .testimonial-wall__avatar { background: linear-gradient(135deg, var(--accent), var(--primary-2)); color: var(--text-main); }

/* Pause control */
.testimonial-wall__pause {
  position: absolute; right: var(--gutter); bottom: 1.25rem; display: inline-flex; align-items: center; gap: 0.375rem;
  height: 1.75rem; padding: 0 0.625rem; border: 0; border-radius: 999px; cursor: pointer;
  background: color-mix(in srgb, var(--text-main) 6%, transparent); color: var(--text-muted);
  font: 500 0.75rem var(--font-sans); transition: color var(--dur-2), background-color var(--dur-2);
}
.testimonial-wall__pause:hover { color: var(--text-main); background: color-mix(in srgb, var(--text-main) 10%, transparent); }
.testimonial-wall__pause:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.testimonial-wall__pause[hidden] { display: none; }
.testimonial-wall__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.testimonial-wall__icon-play, .testimonial-wall__pause[aria-pressed="true"] .testimonial-wall__icon-pause { display: none; }
.testimonial-wall__pause[aria-pressed="true"] .testimonial-wall__icon-play { display: block; }
```

## JS

```js
document.querySelectorAll('[data-testimonial-wall]').forEach((wall) => {
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return; // stays a still grid
  const pause = wall.querySelector('.testimonial-wall__pause');
  let paused = false;

  // Ease the playback rate towards a target instead of snapping
  const glide = (anim, target) => {
    cancelAnimationFrame(anim.glideFrame);
    const step = () => {
      const next = anim.playbackRate + (target - anim.playbackRate) * 0.12;
      anim.playbackRate = Math.abs(target - next) < 0.01 ? target : next;
      if (anim.playbackRate !== target) anim.glideFrame = requestAnimationFrame(step);
    };
    step();
  };

  // Each column: list + hidden copy, looping vertically; speed in px/s, kept exact on resize
  const anims = [...wall.querySelectorAll('.testimonial-wall__col')].map((col) => {
    const list = col.querySelector('.testimonial-wall__list');
    const copy = list.cloneNode(true);
    copy.setAttribute('aria-hidden', 'true');
    copy.inert = true;
    const mover = document.createElement('div');
    mover.className = 'testimonial-wall__mover';
    list.replaceWith(mover);
    mover.append(list, copy);
    const speed = Number(col.dataset.speed) || 34;
    const anim = mover.animate([{ transform: 'translateY(0)' }, { transform: 'translateY(-50%)' }], {
      duration: 30000,
      iterations: Infinity,
      direction: col.classList.contains('testimonial-wall__col--reverse') ? 'reverse' : 'normal',
    });
    new ResizeObserver(() => {
      anim.effect.updateTiming({ duration: (Math.max(list.offsetHeight, 400) / speed) * 1000 });
    }).observe(list);
    col.addEventListener('pointerenter', () => { if (!paused) glide(anim, 0.12); });
    col.addEventListener('pointerleave', () => { if (!paused) glide(anim, 1); });
    return anim;
  });

  pause.hidden = false;
  pause.addEventListener('click', () => {
    paused = !paused;
    pause.setAttribute('aria-pressed', String(paused));
    anims.forEach((anim) => glide(anim, paused ? 0 : 1));
  });
});
```

## Notes

- Every review is in the DOM once for screen readers; the duplicate that makes the loop seamless is `aria-hidden` and `inert`. Ratings are `role="img"` with a text label.
- Columns hidden at small widths stay in the DOM but `display: none`. Put your strongest reviews in the first column, because phones only see that one.
- Speeds differ per column (`data-speed`, px/s) so the wall never moves in lockstep. Hover slows a column to 12% so it can be read; the pause button stops everything (WCAG 2.2.2).
- Publish only genuine, attributable reviews. Placeholder names and quotes here are examples.
