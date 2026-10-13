# Smooth Accordion

FAQ accordion on native `<details>`, with height animated by the Web Animations API, so it's smooth in every browser and interruptible: click mid-animation and it reverses from where it is. The open item lifts onto a white card, its number lights up, the plus springs into a minus, and the answer fades up. Optional one-open-at-a-time mode. The heading sticks beside the list on desktop. Depends on `tokens/variables.css`.

**Motion:** height 0 ↔ auto via WAAPI (ease-out, ~460ms) · answer fade-up · card lift · icon rotate with spring · colour shifts.

## HTML

```html
<section class="smooth-accordion" aria-labelledby="smooth-accordion-title">
  <div class="smooth-accordion__inner">
    <header class="smooth-accordion__head">
      <p class="smooth-accordion__eyebrow">FAQ</p>
      <h2 id="smooth-accordion-title" class="smooth-accordion__title">Questions, answered straight.</h2>
      <p class="smooth-accordion__lead">Can't find what you need? Call <a href="tel:+15555550123">(555) 555-0123</a>. A person picks up, day or night.</p>
    </header>

    <div class="smooth-accordion__list" data-smooth-accordion data-exclusive>
      <details class="smooth-accordion__item" open>
        <summary class="smooth-accordion__summary">
          <span class="smooth-accordion__num" aria-hidden="true">01</span>
          <span class="smooth-accordion__q">Do you charge for estimates?</span>
          <span class="smooth-accordion__icon" aria-hidden="true"></span>
        </summary>
        <div class="smooth-accordion__content"><div class="smooth-accordion__body">
          <p>Never. You get a written, flat-rate price before any work starts. If you decide not to go ahead, you owe nothing.</p>
        </div></div>
      </details>
      <details class="smooth-accordion__item">
        <summary class="smooth-accordion__summary">
          <span class="smooth-accordion__num" aria-hidden="true">02</span>
          <span class="smooth-accordion__q">How quickly can someone come out?</span>
          <span class="smooth-accordion__icon" aria-hidden="true"></span>
        </summary>
        <div class="smooth-accordion__content"><div class="smooth-accordion__body">
          <p>Most bookings get a same-day or next-day slot. Emergencies are answered 24/7, with a technician typically at your door within two hours.</p>
        </div></div>
      </details>
      <details class="smooth-accordion__item">
        <summary class="smooth-accordion__summary">
          <span class="smooth-accordion__num" aria-hidden="true">03</span>
          <span class="smooth-accordion__q">Are your technicians licensed and insured?</span>
          <span class="smooth-accordion__icon" aria-hidden="true"></span>
        </summary>
        <div class="smooth-accordion__content"><div class="smooth-accordion__body">
          <p>Yes. Every technician is state-licensed, background-checked and covered by our $2M liability policy. We're happy to send certificates.</p>
        </div></div>
      </details>
      <details class="smooth-accordion__item">
        <summary class="smooth-accordion__summary">
          <span class="smooth-accordion__num" aria-hidden="true">04</span>
          <span class="smooth-accordion__q">What does the 5-year guarantee cover?</span>
          <span class="smooth-accordion__icon" aria-hidden="true"></span>
        </summary>
        <div class="smooth-accordion__content"><div class="smooth-accordion__body">
          <p>All of our workmanship. If something we fixed or installed fails because of how we did it, we come back and make it right at no cost.</p>
        </div></div>
      </details>
      <details class="smooth-accordion__item">
        <summary class="smooth-accordion__summary">
          <span class="smooth-accordion__num" aria-hidden="true">05</span>
          <span class="smooth-accordion__q">Which areas do you serve?</span>
          <span class="smooth-accordion__icon" aria-hidden="true"></span>
        </summary>
        <div class="smooth-accordion__content"><div class="smooth-accordion__body">
          <p>Springfield and 14 surrounding towns, including Westlake, Northside and Riverside. Not sure? Enter your ZIP code when you book.</p>
        </div></div>
      </details>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: heading sticks beside the list on wide screens */
.smooth-accordion { background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.smooth-accordion__inner { display: grid; gap: 2.5rem; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
@media (min-width: 1024px) {
  .smooth-accordion__inner { grid-template-columns: 0.8fr 1.2fr; gap: 4rem; }
  .smooth-accordion__head { position: sticky; top: 6rem; align-self: start; }
}
.smooth-accordion__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.smooth-accordion__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.smooth-accordion__lead { margin: 1rem 0 0; max-width: 26rem; color: var(--text-muted); line-height: 1.6; }
.smooth-accordion__lead a { color: var(--text-main); font-weight: 600; text-decoration-color: color-mix(in srgb, var(--primary) 50%, transparent); text-underline-offset: 3px; }

/* Items: soft grey at rest, a lifted white card when open */
.smooth-accordion__list { display: grid; gap: 0.75rem; }
.smooth-accordion__item {
  border-radius: var(--radius-xl); background: var(--surface-muted); box-shadow: inset 0 0 0 1px transparent;
  transition: background-color var(--dur-3), box-shadow var(--dur-4) var(--ease-out);
}
.smooth-accordion__item:hover { box-shadow: inset 0 0 0 1px var(--border-subtle); }
.smooth-accordion__item:is([data-state="open"], [open]:not([data-state])) {
  background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), 0 20px 44px -24px color-mix(in srgb, var(--text-main) 30%, transparent);
}

/* Question row */
.smooth-accordion__summary {
  display: grid; grid-template-columns: auto 1fr auto; align-items: center; gap: 1rem;
  padding: 1.125rem 1.125rem 1.125rem 1.25rem; border-radius: inherit; cursor: pointer; list-style: none;
  font: 600 1.0625rem/1.4 var(--font-display); letter-spacing: -0.01em;
}
.smooth-accordion__summary::-webkit-details-marker { display: none; }
.smooth-accordion__summary:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.smooth-accordion__num { color: var(--text-muted); font: 500 0.8125rem/1 var(--font-mono); font-variant-numeric: tabular-nums; transition: color var(--dur-3); }

/* Plus that springs into a minus */
.smooth-accordion__icon {
  position: relative; width: 2rem; height: 2rem; border-radius: 50%;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle);
  transition: background-color var(--dur-3), box-shadow var(--dur-3), transform var(--dur-4) var(--ease-spring);
}
.smooth-accordion__icon::before, .smooth-accordion__icon::after {
  content: ""; position: absolute; left: 50%; top: 50%; width: 0.75rem; height: 2px; margin: -1px 0 0 -0.375rem;
  border-radius: 2px; background: var(--text-main); transition: transform var(--dur-4) var(--ease-spring), background-color var(--dur-3);
}
.smooth-accordion__icon::after { transform: rotate(90deg); }

/* Open state */
.smooth-accordion__item:is([data-state="open"], [open]:not([data-state])) .smooth-accordion__num { color: var(--primary); }
.smooth-accordion__item:is([data-state="open"], [open]:not([data-state])) .smooth-accordion__icon { background: var(--text-main); box-shadow: none; transform: rotate(180deg); }
.smooth-accordion__item:is([data-state="open"], [open]:not([data-state])) .smooth-accordion__icon::before,
.smooth-accordion__item:is([data-state="open"], [open]:not([data-state])) .smooth-accordion__icon::after { background: var(--surface-light); }
.smooth-accordion__item:is([data-state="open"], [open]:not([data-state])) .smooth-accordion__icon::after { transform: rotate(0deg); }

/* Answer: clipped container (height animated by JS), content fades up */
.smooth-accordion__content { overflow: hidden; }
.smooth-accordion__body {
  padding: 0 1.25rem 1.5rem calc(1.25rem + 1.25rem + 1rem); color: var(--text-muted); line-height: 1.65;
  opacity: 0; transform: translateY(-6px);
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-out);
}
.smooth-accordion__body p { margin: 0; max-width: 60ch; }
.smooth-accordion__item:is([data-state="open"], [open]:not([data-state])) .smooth-accordion__body { opacity: 1; transform: none; transition-delay: 80ms; }
@media (max-width: 479.98px) {
  .smooth-accordion__summary { gap: 0.75rem; }
  .smooth-accordion__body { padding-left: 1.25rem; }
}
```

## JS

```js
document.querySelectorAll('[data-smooth-accordion]').forEach((group) => {
  const exclusive = group.hasAttribute('data-exclusive');
  const items = [...group.querySelectorAll('.smooth-accordion__item')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  items.forEach((item) => { item.dataset.state = item.open ? 'open' : 'closed'; });

  // Animate between the current height and the target; reversible mid-flight
  const animate = (item, open) => {
    const content = item.querySelector('.smooth-accordion__content');
    const from = item.open ? content.offsetHeight : 0; // read before cancelling a running animation
    item.heightAnim?.cancel();
    item.dataset.state = open ? 'open' : 'closing';
    if (open) item.open = true;
    if (reduce.matches) {
      if (!open) { item.open = false; item.dataset.state = 'closed'; }
      return;
    }
    const to = open ? content.scrollHeight : 0;
    const anim = content.animate({ height: [`${from}px`, `${to}px`] }, { duration: 460, easing: 'cubic-bezier(0.16, 1, 0.3, 1)' });
    item.heightAnim = anim;
    anim.onfinish = () => {
      item.heightAnim = null;
      if (!open) { item.open = false; item.dataset.state = 'closed'; }
    };
  };

  items.forEach((item) => {
    item.querySelector('summary').addEventListener('click', (e) => {
      e.preventDefault(); // we drive open/close ourselves
      const opening = item.dataset.state !== 'open';
      if (opening && exclusive) {
        items.forEach((other) => { if (other !== item && other.dataset.state === 'open') animate(other, false); });
      }
      animate(item, opening);
    });
    // Find-in-page (or other code) can open an item natively: keep our state in sync
    item.addEventListener('toggle', () => { if (!item.heightAnim) item.dataset.state = item.open ? 'open' : 'closed'; });
  });
});
```

## Notes

- Built on `<details>`/`<summary>`: keyboard (Enter/Space), expanded/collapsed announcements and find-in-page all work natively, with or without the script. JS only adds the animation.
- Remove `data-exclusive` to allow several answers open at once.
- The answer container keeps `overflow: hidden`; avoid focus rings or shadows that need to overflow it.
- Answers stay in the page, so Ctrl+F finds them, and Chromium opens the matching item. The `toggle` listener keeps the styling in sync.
- Numbers are decorative (`aria-hidden`). Drop them and the body indent if you don't want them.
