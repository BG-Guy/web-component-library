# Scroll Timeline

A "how it works" timeline tied to scrolling. A gradient line fills from the first step to the last, with a glowing head at the reading position. Each step's dot lights up and pops as the line reaches it, and cards slide in from alternating sides on desktop. Single column with the line on the left on mobile. Depends on `tokens/variables.css`.

**Motion:** scroll-mapped line fill (1:1 with scroll, rAF-throttled) · glowing line head · dot activation with a spring and halo · card slide-in from the side.

## HTML

```html
<section class="progress-timeline" aria-labelledby="progress-timeline-title" data-progress-timeline>
  <div class="progress-timeline__inner">
    <header class="progress-timeline__head">
      <p class="progress-timeline__eyebrow">How it works</p>
      <h2 id="progress-timeline-title" class="progress-timeline__title">From first call to finished job.</h2>
      <p class="progress-timeline__lead">No mystery windows, no surprise invoices. Here's what happens, and when.</p>
    </header>

    <div class="progress-timeline__track">
      <span class="progress-timeline__rail" aria-hidden="true"><span class="progress-timeline__fill"></span></span>
      <ol class="progress-timeline__steps" role="list">
        <li class="progress-timeline__step">
          <span class="progress-timeline__dot" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg></span>
          <div class="progress-timeline__card">
            <p class="progress-timeline__when">Minute 0</p>
            <h3>You tell us what's wrong</h3>
            <p>Book online or call. Add a photo if you can; it helps us bring the right parts the first time.</p>
          </div>
        </li>
        <li class="progress-timeline__step">
          <span class="progress-timeline__dot" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9zM14 3v6h6M8 13h8M8 17h5" /></svg></span>
          <div class="progress-timeline__card">
            <p class="progress-timeline__when">Within 15 minutes</p>
            <h3>You get a written, flat-rate quote</h3>
            <p>One price for the whole job, before anyone picks up a tool. Approve it with a tap.</p>
          </div>
        </li>
        <li class="progress-timeline__step">
          <span class="progress-timeline__dot" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" /></svg></span>
          <div class="progress-timeline__card">
            <p class="progress-timeline__when">Same or next day</p>
            <h3>A licensed technician arrives on time</h3>
            <p>Track them live on the map. You'll get a text when they're five minutes away.</p>
          </div>
        </li>
        <li class="progress-timeline__step">
          <span class="progress-timeline__dot" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z" /></svg></span>
          <div class="progress-timeline__card">
            <p class="progress-timeline__when">Usually under 2 hours</p>
            <h3>Fixed, tested and cleaned up</h3>
            <p>We show you what we did, test it with you, and leave the space cleaner than we found it.</p>
          </div>
        </li>
        <li class="progress-timeline__step">
          <span class="progress-timeline__dot" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M12 3 20 6v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM9 12l2 2 4-4" /></svg></span>
          <div class="progress-timeline__card">
            <p class="progress-timeline__when">For the next 5 years</p>
            <h3>Covered by our guarantee</h3>
            <p>If anything we fixed fails, we come back and make it right. Free.</p>
          </div>
        </li>
      </ol>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section and heading */
.progress-timeline { background: var(--surface-muted); color: var(--text-main); font-family: var(--font-sans); }
.progress-timeline__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.progress-timeline__head { max-width: 40rem; margin: 0 auto 3.5rem; text-align: center; }
.progress-timeline__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.progress-timeline__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.progress-timeline__lead { margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Rail and the gradient fill with its glowing head */
.progress-timeline__track { position: relative; max-width: 62rem; margin-inline: auto; }
.progress-timeline__rail { position: absolute; top: 1.25rem; bottom: var(--rail-end, 1.25rem); left: 1.25rem; width: 2px; margin-left: -1px; border-radius: 2px; background: var(--border-subtle); }
.progress-timeline__fill { position: absolute; top: 0; left: 0; width: 100%; height: calc(var(--progress, 0) * 100%); border-radius: inherit; background: linear-gradient(var(--primary), var(--primary-2)); }
.progress-timeline:not(.progress-timeline--js) .progress-timeline__fill { height: 100%; }
.progress-timeline__fill::after {
  content: ""; position: absolute; left: 50%; bottom: -5px; width: 10px; height: 10px; margin-left: -5px; border-radius: 50%;
  background: var(--primary-2); opacity: var(--head, 0); transition: opacity var(--dur-3);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--primary-2) 25%, transparent), 0 0 18px 2px color-mix(in srgb, var(--primary-2) 70%, transparent);
}

/* Steps: line on the left (mobile) */
.progress-timeline__steps { display: grid; gap: 2rem; margin: 0; padding: 0; list-style: none; }
.progress-timeline__step { position: relative; padding-left: 4rem; }
.progress-timeline__dot {
  position: absolute; left: 0; top: 0; z-index: 1; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: var(--surface-light); color: var(--text-muted);
  box-shadow: inset 0 0 0 1px var(--border-subtle), 0 0 0 6px var(--surface-muted);
  transition: background-color var(--dur-4), color var(--dur-4), box-shadow var(--dur-4) var(--ease-out), transform var(--dur-4) var(--ease-spring);
}
.progress-timeline__dot svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.progress-timeline__card {
  padding: 1.25rem 1.5rem; border-radius: var(--radius-xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle);
  transition: box-shadow var(--dur-4) var(--ease-out), opacity var(--dur-5) var(--ease-out), transform var(--dur-5) var(--ease-out);
}
.progress-timeline__when { margin: 0; color: var(--primary); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.04em; text-transform: uppercase; }
.progress-timeline__card h3 { margin: 0.625rem 0 0; font: 600 1.1875rem/1.3 var(--font-display); letter-spacing: -0.015em; }
.progress-timeline__card p:last-child { margin: 0.5rem 0 0; color: var(--text-muted); line-height: 1.6; }

/* Reached: the dot lights up, the card picks up a tinted edge */
.progress-timeline__step.is-reached .progress-timeline__dot {
  background: var(--primary); color: var(--text-inverse); transform: scale(1.08);
  box-shadow: 0 0 0 6px var(--surface-muted), 0 0 0 10px color-mix(in srgb, var(--primary) 18%, transparent), 0 10px 24px -8px var(--primary);
}
.progress-timeline__step.is-reached .progress-timeline__card {
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 28%, var(--border-subtle)), 0 20px 40px -24px color-mix(in srgb, var(--primary) 45%, transparent);
}

/* Entrance: cards rise in the first time they come close (JS only) */
.progress-timeline--js .progress-timeline__step:not(.is-seen) .progress-timeline__card { opacity: 0; transform: translateY(24px); }

/* Desktop: centred line, cards alternate sides and slide in from them */
@media (min-width: 1024px) {
  .progress-timeline__rail { left: 50%; }
  .progress-timeline__steps { gap: 1.5rem; }
  .progress-timeline__step { display: grid; grid-template-columns: 1fr 2.5rem 1fr; column-gap: 2.5rem; align-items: start; padding-left: 0; }
  .progress-timeline__dot { position: relative; grid-column: 2; grid-row: 1; }
  .progress-timeline__card { grid-column: 3; grid-row: 1; }
  .progress-timeline__step:nth-child(even) .progress-timeline__card { grid-column: 1; text-align: right; }
  .progress-timeline--js .progress-timeline__step:not(.is-seen) .progress-timeline__card { transform: translateX(32px); }
  .progress-timeline--js .progress-timeline__step:nth-child(even):not(.is-seen) .progress-timeline__card { transform: translateX(-32px); }
}
```

## JS

```js
document.querySelectorAll('[data-progress-timeline]').forEach((root) => {
  const track = root.querySelector('.progress-timeline__track');
  const rail = root.querySelector('.progress-timeline__rail');
  const steps = [...root.querySelectorAll('.progress-timeline__step')];
  const dots = steps.map((step) => step.querySelector('.progress-timeline__dot'));
  root.classList.add('progress-timeline--js');
  let queued = false;

  // End the rail at the last dot's centre rather than the bottom of the last card
  const fitRail = () => {
    const last = dots[dots.length - 1];
    const end = track.getBoundingClientRect().bottom - last.getBoundingClientRect().top - last.offsetHeight / 2;
    track.style.setProperty('--rail-end', `${end}px`);
  };

  // Map scroll position to fill height; light each dot as the "reading line" passes it
  const update = () => {
    queued = false;
    const line = innerHeight * 0.55;
    const r = rail.getBoundingClientRect();
    const p = Math.min(Math.max((line - r.top) / r.height, 0), 1);
    track.style.setProperty('--progress', p.toFixed(4));
    track.style.setProperty('--head', p > 0 && p < 1 ? '1' : '0');
    steps.forEach((step, i) => {
      const dot = dots[i].getBoundingClientRect();
      step.classList.toggle('is-reached', dot.top + dot.height / 2 <= line);
      if (dot.top < innerHeight * 0.9) step.classList.add('is-seen');
    });
  };
  const request = () => { if (!queued) { queued = true; requestAnimationFrame(update); } };
  addEventListener('scroll', request, { passive: true });
  addEventListener('resize', () => { fitRail(); request(); });
  fitRail();
  update();
});
```

## Notes

- The line fill tracks scroll position directly; it isn't a timed animation, so it stays in sync and respects the reader's pace. Under reduced motion the dot and card transitions become instant.
- Without JS the line is shown fully filled and every card is visible.
- The timeline is an ordered list (`<ol>`); dots and icons are decorative. The time labels ("Within 15 minutes") carry the sequence in text.
- The "reading line" sits at 55% of the viewport height; change `0.55` to move it.
- On a dark section, change the dot's outer ring colour (`0 0 0 6px …`) to the section background so it still masks the rail.
