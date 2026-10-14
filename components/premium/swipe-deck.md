# Swipeable Review Deck

A Tinder-style stack of customer reviews on a light surface. Grab the top card and it follows your finger, swinging from its base in proportion to how far you've pulled it, while the card beneath scales up from 0.94 and lifts into place. Let go past the threshold (or flick it) and the card flies off with your release velocity, then tucks in at the back of the deck; let go early and it springs home. Prev/Next buttons and the arrow keys deal the same fling and a counter tracks "3 / 8". On phones the deck sits full-width under the heading, and without JS it's a swipeable scroll-snap row. Depends on `tokens/variables.css`.

**Motion:** drag-follow with rotation ∝ x (rAF) · next card scale 0.94 → 1 and lift tied to drag distance · spring return (`--dur-5` `--ease-spring`) · velocity fling and fade (`--dur-4` `--ease-out`) · Prev card swings back in on the spring · button press scale (`--ease-spring`).

## HTML

```html
<section class="swipe-deck" aria-labelledby="swipe-deck-title" data-swipe-deck>
  <svg class="swipe-deck__defs" width="0" height="0" aria-hidden="true" focusable="false">
    <symbol id="swipe-deck-star" viewBox="0 0 24 24"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></symbol>
    <symbol id="swipe-deck-quote" viewBox="0 0 24 24"><path d="M10 7H6.5a1 1 0 0 0-1 1v3.5a1 1 0 0 0 1 1H9V13a3.5 3.5 0 0 1-3.5 3.5M18.5 7H15a1 1 0 0 0-1 1v3.5a1 1 0 0 0 1 1h2.5V13a3.5 3.5 0 0 1-3.5 3.5" /></symbol>
  </svg>

  <div class="swipe-deck__inner">
    <header class="swipe-deck__head">
      <p class="swipe-deck__eyebrow">Reviews</p>
      <h2 id="swipe-deck-title" class="swipe-deck__title">Springfield, in its own words.</h2>
      <p class="swipe-deck__lead">Swipe through recent reviews from verified jobs. Every one is published exactly as it was written.</p>
      <div class="swipe-deck__score">
        <p class="swipe-deck__avg"><strong>4.9</strong><span class="swipe-deck__sr"> out of 5</span></p>
        <div>
          <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" aria-hidden="true" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
          <p class="swipe-deck__count-total">from 1,284 verified reviews</p>
        </div>
      </div>
      <dl class="swipe-deck__bars">
        <div style="--swipe-deck-share: 92%"><dt>5 stars</dt><dd>92%</dd></div>
        <div style="--swipe-deck-share: 6%"><dt>4 stars</dt><dd>6%</dd></div>
        <div style="--swipe-deck-share: 2%"><dt>3 or fewer</dt><dd>2%</dd></div>
      </dl>
    </header>

    <div class="swipe-deck__deck">
      <ol class="swipe-deck__stack" role="list" aria-label="Customer reviews" tabindex="0">
        <li class="swipe-deck__card">
          <figure class="swipe-deck__figure">
            <div class="swipe-deck__top">
              <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" role="img" aria-label="Rated 5 out of 5" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
              <svg class="swipe-deck__mark" viewBox="0 0 24 24" width="40" height="40" aria-hidden="true" focusable="false"><use href="#swipe-deck-quote" /></svg>
            </div>
            <blockquote class="swipe-deck__quote"><p>“Called at eight, fixed by lunch. Sam explained every step and left the utility room cleaner than he found it.”</p></blockquote>
            <figcaption class="swipe-deck__who">
              <span class="swipe-deck__avatar" aria-hidden="true">MR</span>
              <span class="swipe-deck__name"><strong>Maria R.</strong><small>Water heater install · Westlake</small></span>
            </figcaption>
          </figure>
        </li>
        <li class="swipe-deck__card">
          <figure class="swipe-deck__figure">
            <div class="swipe-deck__top">
              <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" role="img" aria-label="Rated 5 out of 5" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
              <svg class="swipe-deck__mark" viewBox="0 0 24 24" width="40" height="40" aria-hidden="true" focusable="false"><use href="#swipe-deck-quote" /></svg>
            </div>
            <blockquote class="swipe-deck__quote"><p>“A storm took three tiles on a Sunday. They were up the ladder within two hours, and the quote didn't budge.”</p></blockquote>
            <figcaption class="swipe-deck__who">
              <span class="swipe-deck__avatar" aria-hidden="true">DP</span>
              <span class="swipe-deck__name"><strong>Dev P.</strong><small>Roof leak repair · Northside</small></span>
            </figcaption>
          </figure>
        </li>
        <li class="swipe-deck__card">
          <figure class="swipe-deck__figure">
            <div class="swipe-deck__top">
              <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" role="img" aria-label="Rated 5 out of 5" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
              <svg class="swipe-deck__mark" viewBox="0 0 24 24" width="40" height="40" aria-hidden="true" focusable="false"><use href="#swipe-deck-quote" /></svg>
            </div>
            <blockquote class="swipe-deck__quote"><p>“Tidy, punctual and properly certified. The new lighting has changed how we use the whole kitchen.”</p></blockquote>
            <figcaption class="swipe-deck__who">
              <span class="swipe-deck__avatar" aria-hidden="true">AK</span>
              <span class="swipe-deck__name"><strong>Alison K.</strong><small>Kitchen rewire · Riverside</small></span>
            </figcaption>
          </figure>
        </li>
        <li class="swipe-deck__card">
          <figure class="swipe-deck__figure">
            <div class="swipe-deck__top">
              <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" role="img" aria-label="Rated 5 out of 5" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
              <svg class="swipe-deck__mark" viewBox="0 0 24 24" width="40" height="40" aria-hidden="true" focusable="false"><use href="#swipe-deck-quote" /></svg>
            </div>
            <blockquote class="swipe-deck__quote"><p>“Ten days from start to finish, exactly as promised. The tiling is better than anything in the showroom.”</p></blockquote>
            <figcaption class="swipe-deck__who">
              <span class="swipe-deck__avatar" aria-hidden="true">JB</span>
              <span class="swipe-deck__name"><strong>Jess B.</strong><small>Bathroom refit · Westlake</small></span>
            </figcaption>
          </figure>
        </li>
        <li class="swipe-deck__card">
          <figure class="swipe-deck__figure">
            <div class="swipe-deck__top">
              <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" role="img" aria-label="Rated 5 out of 5" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
              <svg class="swipe-deck__mark" viewBox="0 0 24 24" width="40" height="40" aria-hidden="true" focusable="false"><use href="#swipe-deck-quote" /></svg>
            </div>
            <blockquote class="swipe-deck__quote"><p>“Booked in the app, watched the van arrive, paid in one tap. I wish everything worked like this.”</p></blockquote>
            <figcaption class="swipe-deck__who">
              <span class="swipe-deck__avatar" aria-hidden="true">HO</span>
              <span class="swipe-deck__name"><strong>Hannah O.</strong><small>Boiler service · Northside</small></span>
            </figcaption>
          </figure>
        </li>
        <li class="swipe-deck__card">
          <figure class="swipe-deck__figure">
            <div class="swipe-deck__top">
              <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" role="img" aria-label="Rated 5 out of 5" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
              <svg class="swipe-deck__mark" viewBox="0 0 24 24" width="40" height="40" aria-hidden="true" focusable="false"><use href="#swipe-deck-quote" /></svg>
            </div>
            <blockquote class="swipe-deck__quote"><p>“They talked me out of the expensive option and into the right one. That's how you earn a customer for life.”</p></blockquote>
            <figcaption class="swipe-deck__who">
              <span class="swipe-deck__avatar" aria-hidden="true">ML</span>
              <span class="swipe-deck__name"><strong>Marcus L.</strong><small>Deck rebuild · Riverside</small></span>
            </figcaption>
          </figure>
        </li>
        <li class="swipe-deck__card">
          <figure class="swipe-deck__figure">
            <div class="swipe-deck__top">
              <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" role="img" aria-label="Rated 5 out of 5" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
              <svg class="swipe-deck__mark" viewBox="0 0 24 24" width="40" height="40" aria-hidden="true" focusable="false"><use href="#swipe-deck-quote" /></svg>
            </div>
            <blockquote class="swipe-deck__quote"><p>“Burst pipe at eleven at night. A calm voice on the phone and a plumber at the door by midnight.”</p></blockquote>
            <figcaption class="swipe-deck__who">
              <span class="swipe-deck__avatar" aria-hidden="true">PS</span>
              <span class="swipe-deck__name"><strong>Priya S.</strong><small>Emergency plumbing · Westlake</small></span>
            </figcaption>
          </figure>
        </li>
        <li class="swipe-deck__card">
          <figure class="swipe-deck__figure">
            <div class="swipe-deck__top">
              <svg class="swipe-deck__rating" viewBox="0 0 116 20" width="116" height="20" role="img" aria-label="Rated 4 out of 5" focusable="false"><use href="#swipe-deck-star" width="20" height="20" /><use href="#swipe-deck-star" x="24" width="20" height="20" /><use href="#swipe-deck-star" x="48" width="20" height="20" /><use href="#swipe-deck-star" x="72" width="20" height="20" /><use class="swipe-deck__star--off" href="#swipe-deck-star" x="96" width="20" height="20" /></svg>
              <svg class="swipe-deck__mark" viewBox="0 0 24 24" width="40" height="40" aria-hidden="true" focusable="false"><use href="#swipe-deck-quote" /></svg>
            </div>
            <blockquote class="swipe-deck__quote"><p>“Fair price, no mess, and the house is noticeably quieter. The back windows are already booked in.”</p></blockquote>
            <figcaption class="swipe-deck__who">
              <span class="swipe-deck__avatar" aria-hidden="true">GW</span>
              <span class="swipe-deck__name"><strong>Greg W.</strong><small>Window replacement · Northside</small></span>
            </figcaption>
          </figure>
        </li>
      </ol>

      <div class="swipe-deck__controls" hidden>
        <button class="swipe-deck__btn" type="button" data-swipe-deck-prev aria-label="Previous review">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M19 12H5M11 18l-6-6 6-6" /></svg>
        </button>
        <p class="swipe-deck__counter" aria-hidden="true"><span class="swipe-deck__current">1</span> / <span class="swipe-deck__total">8</span></p>
        <button class="swipe-deck__btn" type="button" data-swipe-deck-next aria-label="Next review">
          <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </button>
      </div>
      <p class="swipe-deck__hint" aria-hidden="true" hidden>Drag the top card, or use the arrow keys</p>
      <p class="swipe-deck__sr" aria-live="polite" data-swipe-deck-status></p>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: light, with soft brand light pooled behind the deck */
.swipe-deck {
  position: relative; overflow: clip;
  background:
    radial-gradient(46rem 32rem at 80% 42%, color-mix(in srgb, var(--primary) 8%, transparent), transparent 70%),
    radial-gradient(34rem 24rem at 96% 96%, color-mix(in srgb, var(--primary-2) 8%, transparent), transparent 70%),
    var(--surface-muted);
  color: var(--text-main); font-family: var(--font-sans);
  --swipe-deck-muted: color-mix(in srgb, var(--text-muted) 75%, var(--text-main)); /* holds 4.9:1 even on the glows */
}
.swipe-deck svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.swipe-deck__defs { position: absolute; width: 0; height: 0; overflow: hidden; }
.swipe-deck__inner { display: grid; gap: var(--space-2xl); align-items: center; max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }

/* Heading column with the rating summary */
.swipe-deck__head { max-width: 30rem; }
.swipe-deck__eyebrow { margin: 0; color: var(--primary-hover); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; }
.swipe-deck__title { margin: 0.875rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.04 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.swipe-deck__lead { margin: 1rem 0 0; color: var(--swipe-deck-muted); font-size: 1.0625rem; line-height: 1.6; }
.swipe-deck__score { display: flex; align-items: center; gap: var(--space-md); margin-top: var(--space-xl); }
.swipe-deck__avg { margin: 0; }
.swipe-deck__avg strong { font: 600 3.25rem/1 var(--font-display); letter-spacing: var(--tracking-display); }
.swipe-deck__count-total { margin: 0.375rem 0 0; color: var(--swipe-deck-muted); font-size: 0.875rem; }
.swipe-deck__rating { display: block; color: var(--accent); }
.swipe-deck__rating use { fill: currentColor; stroke: currentColor; stroke-width: 1.5; }
.swipe-deck__star--off { color: var(--border-subtle); }
.swipe-deck__bars { display: grid; gap: 0.5rem; max-width: 20rem; margin: var(--space-lg) 0 0; }
.swipe-deck__bars div { display: grid; grid-template-columns: 5.5rem 1fr 2.5rem; align-items: center; gap: 0.75rem; font-size: 0.8125rem; }
.swipe-deck__bars div::before {
  content: ""; grid-area: 1 / 2; height: 0.375rem; border-radius: var(--radius-full);
  background: linear-gradient(90deg, var(--accent) var(--swipe-deck-share), var(--border-subtle) 0);
}
.swipe-deck__bars dt { grid-area: 1 / 1; color: var(--swipe-deck-muted); }
.swipe-deck__bars dd { grid-area: 1 / 3; margin: 0; text-align: end; font: 500 0.8125rem var(--font-mono); font-variant-numeric: tabular-nums; }

/* Deck column, on a faint dotted "table" */
.swipe-deck__deck { position: relative; isolation: isolate; display: grid; justify-items: center; gap: var(--space-lg); min-width: 0; }
.swipe-deck__deck::before {
  content: ""; position: absolute; inset: -2rem -1rem; z-index: -1; pointer-events: none;
  background: radial-gradient(color-mix(in srgb, var(--text-main) 14%, transparent) 1px, transparent 1.5px) 0 0 / 22px 22px;
  -webkit-mask-image: radial-gradient(closest-side, black, transparent);
  mask-image: radial-gradient(closest-side, black, transparent);
}

/* Without JS: a swipeable scroll-snap row */
.swipe-deck__stack {
  display: flex; gap: var(--space-md); width: 100%; margin: 0; padding: var(--space-sm) var(--space-sm) var(--space-lg);
  list-style: none; overflow-x: auto; scroll-snap-type: x mandatory; overscroll-behavior-x: contain; scrollbar-width: thin;
}
.swipe-deck__card { flex: 0 0 min(85%, 22rem); scroll-snap-align: center; }

/* Card */
.swipe-deck__card {
  --swipe-deck-tint: var(--primary);
  position: relative; display: grid; min-height: 18.5rem; border-radius: var(--radius-2xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
}
.swipe-deck__card:nth-child(3n + 2) { --swipe-deck-tint: var(--primary-2); }
.swipe-deck__card:nth-child(3n) { --swipe-deck-tint: var(--accent); }
.swipe-deck__figure {
  display: grid; grid-template-rows: auto 1fr auto; gap: var(--space-lg); margin: 0; padding: clamp(1.25rem, 1rem + 1vw, 1.75rem);
  border-radius: inherit; background: radial-gradient(110% 70% at 100% 0%, color-mix(in srgb, var(--swipe-deck-tint) 13%, transparent), transparent 60%);
}
.swipe-deck__top { display: flex; align-items: flex-start; justify-content: space-between; gap: var(--space-md); }
.swipe-deck__mark { width: 2.5rem; height: 2.5rem; margin: -0.375rem -0.375rem 0 0; color: color-mix(in srgb, var(--swipe-deck-tint) 70%, var(--text-main)); opacity: 0.45; }
.swipe-deck__quote { margin: 0; }
.swipe-deck__quote p { margin: 0; font: 500 clamp(1.125rem, 1.02rem + 0.5vw, 1.3125rem)/1.45 var(--font-display); letter-spacing: -0.012em; text-wrap: pretty; }
.swipe-deck__who { display: flex; align-items: center; gap: 0.75rem; padding-top: var(--space-md); border-top: 1px solid var(--border-subtle); }
.swipe-deck__avatar {
  display: grid; place-items: center; flex: none; width: 2.75rem; height: 2.75rem; border-radius: 50%;
  background: linear-gradient(135deg, color-mix(in srgb, var(--swipe-deck-tint) 60%, var(--surface-deep)), color-mix(in srgb, var(--swipe-deck-tint) 35%, var(--surface-deep)));
  color: var(--text-inverse); font: 600 0.875rem/1 var(--font-display); letter-spacing: 0.02em;
  box-shadow: var(--highlight-inverse), 0 6px 14px -6px color-mix(in srgb, var(--swipe-deck-tint) 70%, transparent);
}
.swipe-deck__name strong { display: block; font-size: 0.9375rem; font-weight: 600; }
.swipe-deck__name small { color: var(--text-muted); font-size: 0.8125rem; }

/* With JS: one stack. Depth (set by JS) and pull (drag distance) drive scale, lift, shade and order */
.swipe-deck--js .swipe-deck__stack { display: grid; width: min(100%, 25rem); padding: 0 0 1.75rem; overflow: visible; isolation: isolate; }
.swipe-deck--js .swipe-deck__card {
  --swipe-deck-d: max(0, var(--swipe-deck-depth, 0) - var(--swipe-deck-pull, 0));
  grid-area: 1 / 1; z-index: calc(20 - var(--swipe-deck-depth, 0)); transform-origin: 50% 100%;
  transform: translate3d(var(--swipe-deck-x, 0px), calc(var(--swipe-deck-y, 0px) + min(var(--swipe-deck-d), 2) * 0.875rem), 0) rotate(var(--swipe-deck-r, 0deg)) scale(calc(1 - min(var(--swipe-deck-d), 2) * 0.06));
  opacity: clamp(0, 3 - var(--swipe-deck-d), 1);
  cursor: grab; touch-action: pan-y; -webkit-user-select: none; user-select: none;
  transition: transform var(--dur-5) var(--ease-spring), opacity var(--dur-3) var(--ease-out), box-shadow var(--dur-3) var(--ease-out);
}
.swipe-deck--js .swipe-deck__card::after { /* cards further back sit in shade */
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; background: var(--border-subtle);
  opacity: calc(min(var(--swipe-deck-d), 2) * 0.35); transition: opacity var(--dur-3) var(--ease-out);
}
.swipe-deck.is-dragging .swipe-deck__card:not(.is-flung), .swipe-deck.is-dragging .swipe-deck__card:not(.is-flung)::after { transition: none; }
.swipe-deck--js .swipe-deck__card.is-held {
  cursor: grabbing;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), 0 2px 4px color-mix(in srgb, var(--text-main) 6%, transparent), 0 40px 80px -24px color-mix(in srgb, var(--text-main) 30%, transparent);
}
.swipe-deck--js .swipe-deck__card.is-flung { z-index: 30; opacity: 0; transition: transform var(--dur-4) var(--ease-out), opacity var(--dur-4) var(--ease-in-out); }

/* Controls */
.swipe-deck__controls { display: flex; align-items: center; gap: var(--space-md); }
.swipe-deck__controls[hidden], .swipe-deck__hint[hidden] { display: none; }
.swipe-deck__btn {
  display: grid; place-items: center; width: 3rem; height: 3rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-light); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2) var(--ease-out);
}
.swipe-deck__btn:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-lg); }
.swipe-deck__btn:active { transform: scale(0.92); }
.swipe-deck__btn svg { transition: transform var(--dur-3) var(--ease-spring); }
.swipe-deck__btn[data-swipe-deck-prev]:hover svg { transform: translateX(-2px); }
.swipe-deck__btn[data-swipe-deck-next]:hover svg { transform: translateX(2px); }
.swipe-deck :is(button, .swipe-deck__card, .swipe-deck__stack):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.swipe-deck__counter { min-width: 4.5rem; margin: 0; color: var(--swipe-deck-muted); font: 500 0.875rem/1 var(--font-mono); text-align: center; font-variant-numeric: tabular-nums; }
.swipe-deck__current { color: var(--text-main); font-weight: 600; }
.swipe-deck__hint { margin: 0; color: var(--swipe-deck-muted); font-size: 0.8125rem; text-align: center; }
.swipe-deck__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

@media (min-width: 768px) {
  .swipe-deck__inner { grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.05fr); column-gap: clamp(2.5rem, 6vw, 5rem); }
}
```

## JS

```js
document.querySelectorAll('[data-swipe-deck]').forEach((root) => {
  const stack = root.querySelector('.swipe-deck__stack');
  const cards = [...stack.children];
  const order = [...cards];
  const current = root.querySelector('.swipe-deck__current');
  const status = root.querySelector('[data-swipe-deck-status]');
  let drag = null;
  let frame = 0;

  root.classList.add('swipe-deck--js');
  stack.removeAttribute('tabindex');
  root.querySelector('.swipe-deck__controls').hidden = false;
  root.querySelector('.swipe-deck__hint').hidden = false;
  root.querySelector('.swipe-deck__total').textContent = cards.length;

  const place = (card, x = 0, y = 0, r = 0) => {
    card.style.setProperty('--swipe-deck-x', `${x}px`);
    card.style.setProperty('--swipe-deck-y', `${y}px`);
    card.style.setProperty('--swipe-deck-r', `${r}deg`);
  };
  const instantly = (card, change) => {
    card.style.transition = 'none';
    change();
    void card.offsetWidth;
    card.style.transition = '';
  };

  // Depth drives scale, lift, shade and stacking in CSS. Only the top card is reachable; the rest are inert
  const layout = (announce) => {
    const hadFocus = stack.contains(document.activeElement);
    order.forEach((card, depth) => {
      card.style.setProperty('--swipe-deck-depth', depth);
      card.inert = depth > 0;
      card.tabIndex = depth ? -1 : 0;
    });
    const n = cards.indexOf(order[0]) + 1;
    current.textContent = n;
    if (announce) status.textContent = `Review ${n} of ${cards.length}`;
    if (hadFocus) order[0].focus({ preventScroll: true });
  };

  // Throw the top card off with the release velocity, then park it, hidden, at the back of the deck
  const fling = (dir, vx = 0, vy = 0, y = 0) => {
    const card = order.shift();
    order.push(card);
    const w = stack.offsetWidth;
    card.classList.add('is-flung');
    place(card, dir * (w * 1.5 + Math.abs(vx) * 120), y + vy * 120, dir * Math.min(40, 18 + Math.abs(vx) * 10));
    root.style.setProperty('--swipe-deck-pull', 0);
    layout(true);
    const park = () => {
      clearTimeout(timer);
      card.removeEventListener('transitionend', onEnd);
      if (card.classList.contains('is-flung')) instantly(card, () => { card.classList.remove('is-flung'); place(card); });
    };
    const onEnd = (e) => { if (e.target === card && e.propertyName === 'transform') park(); };
    const timer = setTimeout(park, 900);
    card.addEventListener('transitionend', onEnd);
  };

  // Previous: the back card swings in from the left on the spring
  const prev = () => {
    const card = order.pop();
    order.unshift(card);
    instantly(card, () => {
      card.classList.remove('is-flung');
      card.style.setProperty('--swipe-deck-depth', 0);
      place(card, -stack.offsetWidth * 1.2, -24, -16);
    });
    layout(true);
    place(card);
  };
  const next = () => fling(-1);

  // Drag: the card follows the pointer (one write per frame); the pull also lifts the cards behind it
  stack.addEventListener('pointerdown', (e) => {
    const card = order[0];
    if (drag || e.button > 0 || !card.contains(e.target)) return;
    drag = { id: e.pointerId, x: e.clientX, y: e.clientY, dx: 0, dy: 0, vx: 0, vy: 0, t: e.timeStamp };
    card.setPointerCapture(e.pointerId);
    card.classList.add('is-held');
    root.classList.add('is-dragging');
  });
  stack.addEventListener('pointermove', (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    const dt = Math.max(e.timeStamp - drag.t, 1);
    const dx = e.clientX - drag.x;
    const dy = e.clientY - drag.y;
    drag.vx = 0.7 * ((dx - drag.dx) / dt) + 0.3 * drag.vx;
    drag.vy = 0.7 * ((dy - drag.dy) / dt) + 0.3 * drag.vy;
    Object.assign(drag, { dx, dy, t: e.timeStamp });
    frame ||= requestAnimationFrame(() => {
      frame = 0;
      if (!drag) return;
      const w = stack.offsetWidth;
      place(order[0], drag.dx, drag.dy, (drag.dx / w) * 18);
      root.style.setProperty('--swipe-deck-pull', Math.min(1, Math.abs(drag.dx) / (w * 0.4)).toFixed(3));
    });
  }, { passive: true });

  // Release: past the threshold (or flicked) it flies; otherwise it springs home
  const release = (e) => {
    if (!drag || e.pointerId !== drag.id) return;
    const { dx, dy } = drag;
    const fresh = e.timeStamp - drag.t < 80;
    const vx = fresh ? drag.vx : 0;
    const vy = fresh ? drag.vy : 0;
    const card = order[0];
    drag = null;
    card.classList.remove('is-held');
    root.classList.remove('is-dragging');
    const thrown = Math.abs(dx) > stack.offsetWidth * 0.35 || (Math.abs(vx) > 0.5 && Math.sign(vx) === Math.sign(dx));
    if (e.type === 'pointerup' && thrown) fling(Math.sign(dx), vx, vy, dy);
    else {
      root.style.setProperty('--swipe-deck-pull', 0);
      place(card);
    }
  };
  stack.addEventListener('pointerup', release);
  stack.addEventListener('pointercancel', release);

  // Buttons and arrow keys deal the same fling
  root.querySelector('[data-swipe-deck-next]').addEventListener('click', next);
  root.querySelector('[data-swipe-deck-prev]').addEventListener('click', prev);
  root.querySelector('.swipe-deck__deck').addEventListener('keydown', (e) => {
    if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
    e.preventDefault();
    if (e.key === 'ArrowRight') next();
    else prev();
  });
  layout(false);
});
```

## Notes

- Only the top card is exposed: the cards beneath are `inert`, so they're out of the Tab order and the accessibility tree. The top card is focusable, and focus follows it when it's flung from the keyboard. Prev/Next are labelled buttons, ← and → work anywhere in the deck, and a polite live region announces "Review 3 of 8" (the visible "3 / 8" counter is `aria-hidden`). Each rating is an SVG with `role="img"` and a label such as "Rated 4 out of 5".
- Without JS the list is a horizontal scroll-snap row of the same cards: focusable, swipeable and readable, with the controls left `hidden`.
- On touch, `touch-action: pan-y` keeps vertical page scrolling. A sideways drag moves the card, and a scroll that takes over cancels the drag and springs the card home. A drag counts as thrown past 35% of the card width, or on a flick faster than 0.5 px/ms in the drag direction.
- Every animation runs on token transitions. Under reduced motion they collapse, so flings and swaps are instant while the card still tracks your finger during a drag. Nothing loops.
- Contrast: body text is `--text-main` on white cards (14.6:1). Card meta is `--text-muted` on white (4.8:1). Section-level secondary text uses a darker `--swipe-deck-muted` (75% `--text-muted`, 25% `--text-main`), which holds 4.9:1 even where both 8% brand glows overlap. Avatar initials are `--text-inverse` on tints darkened with `--surface-deep`, at 4.9:1 or better. Card tints cycle through `--primary`, `--primary-2` and `--accent` via `:nth-child`, so retheming the tokens re-tints the deck. With several decks on one page, keep a single `<svg>` sprite for the star and quote symbols so their ids stay unique.
