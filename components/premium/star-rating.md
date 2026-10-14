# Expressive Star Rating

A "How did we do?" card built on a native radio group. A gold gradient sweeps across the stars up to the one you hover or pick. The chosen star pops on a spring with a burst of SVG sparkles. Above the stars a face reacts: its mouth and eyes morph from a frown to an open grin, its colour warms and a word rolls into place ("Terrible" … "Amazing!"). Once a rating is chosen, a comment box opens with a prompt that fits the score. CSS `:has()` drives the fill, face, word and panel, so all of it works without JS. On phones the stars stay 44px tall targets. Depends on `tokens/variables.css`.

**Motion:** star fill sweep (`clip-path`, `--dur-3`, `--ease-out`, staggered by half a `--stagger` per star) · chosen-star pop (`--dur-4`) and sparkle burst (`--dur-5`, `--ease-out`) · face morph via CSS `d` (`--dur-4`, `--ease-spring`) with tint, tilt and scale · rolling word crossfade (`--dur-3` / `--dur-4`, `--ease-spring`) · comment panel opens with `interpolate-size` (`--dur-4`, `--ease-out`) · sent state via a scoped view transition.

## HTML

```html
<div class="star-rate-demo">
  <form class="star-rate" action="/feedback" method="post" aria-labelledby="star-rate-title" data-star-rate>
    <p class="star-rate__who"><span class="star-rate__avatar" aria-hidden="true">SK</span><span><strong>Sam K.</strong> · Leak repair · Tue 14 Oct</span></p>
    <h2 id="star-rate-title" class="star-rate__title">How did we do?</h2>
    <p class="star-rate__lead">Your rating goes straight to Sam and helps us coach the whole team.</p>

    <div class="star-rate__mood" aria-hidden="true">
      <svg class="star-rate__face" viewBox="0 0 64 64" width="88" height="88" focusable="false">
        <circle class="star-rate__head" cx="32" cy="32" r="29" />
        <ellipse class="star-rate__shine" cx="22" cy="13.5" rx="9" ry="4" />
        <circle class="star-rate__cheek" cx="17" cy="38" r="4.5" />
        <circle class="star-rate__cheek" cx="47" cy="38" r="4.5" />
        <path class="star-rate__brow" d="M17 22 25 19M47 22 39 19" />
        <path class="star-rate__eye-l" d="M21.5 27 Q24 23.5 26.5 27 Q24 30.5 21.5 27 Z" />
        <path class="star-rate__eye-r" d="M37.5 27 Q40 23.5 42.5 27 Q40 30.5 37.5 27 Z" />
        <path class="star-rate__mouth" d="M24 42 Q32 45 40 42 Q32 45 24 42 Z" />
      </svg>
      <p class="star-rate__words">
        <span class="star-rate__word star-rate__word--idle" style="--star-rate-k: 0">Pick a star</span>
        <span class="star-rate__word" style="--star-rate-k: 1">Terrible</span>
        <span class="star-rate__word" style="--star-rate-k: 2">Not great</span>
        <span class="star-rate__word" style="--star-rate-k: 3">Okay</span>
        <span class="star-rate__word" style="--star-rate-k: 4">Good</span>
        <span class="star-rate__word" style="--star-rate-k: 5">Amazing!</span>
      </p>
    </div>

    <fieldset class="star-rate__stars">
      <legend class="star-rate__sr">Your rating</legend>
      <input class="star-rate__radio" type="radio" name="rating" value="1" id="star-rate-1" required>
      <label class="star-rate__star" for="star-rate-1" style="--star-rate-i: 0">
        <span class="star-rate__glyph" aria-hidden="true"><span class="star-rate__solid"></span><svg class="star-rate__line" viewBox="-3 -3 30 30" focusable="false"><path d="M12 2.5l2.94 5.96 6.58.96-4.76 4.64 1.12 6.55L12 17.52l-5.88 3.09 1.12-6.55L2.48 9.42l6.58-.96z" /></svg></span>
        <svg class="star-rate__burst" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M24 1.5Q24 5 27.5 5 24 5 24 8.5 24 5 20.5 5 24 5 24 1.5ZM43 21Q43 24 46 24 43 24 43 27 43 24 40 24 43 24 43 21ZM24 39.5Q24 43 27.5 43 24 43 24 46.5 24 43 20.5 43 24 43 24 39.5ZM5 21Q5 24 8 24 5 24 5 27 5 24 2 24 5 24 5 21ZM36 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM36 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0Z" /></svg>
        <span class="star-rate__sr">1 star, Terrible</span>
      </label>
      <input class="star-rate__radio" type="radio" name="rating" value="2" id="star-rate-2">
      <label class="star-rate__star" for="star-rate-2" style="--star-rate-i: 1">
        <span class="star-rate__glyph" aria-hidden="true"><span class="star-rate__solid"></span><svg class="star-rate__line" viewBox="-3 -3 30 30" focusable="false"><path d="M12 2.5l2.94 5.96 6.58.96-4.76 4.64 1.12 6.55L12 17.52l-5.88 3.09 1.12-6.55L2.48 9.42l6.58-.96z" /></svg></span>
        <svg class="star-rate__burst" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M24 1.5Q24 5 27.5 5 24 5 24 8.5 24 5 20.5 5 24 5 24 1.5ZM43 21Q43 24 46 24 43 24 43 27 43 24 40 24 43 24 43 21ZM24 39.5Q24 43 27.5 43 24 43 24 46.5 24 43 20.5 43 24 43 24 39.5ZM5 21Q5 24 8 24 5 24 5 27 5 24 2 24 5 24 5 21ZM36 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM36 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0Z" /></svg>
        <span class="star-rate__sr">2 stars, Not great</span>
      </label>
      <input class="star-rate__radio" type="radio" name="rating" value="3" id="star-rate-3">
      <label class="star-rate__star" for="star-rate-3" style="--star-rate-i: 2">
        <span class="star-rate__glyph" aria-hidden="true"><span class="star-rate__solid"></span><svg class="star-rate__line" viewBox="-3 -3 30 30" focusable="false"><path d="M12 2.5l2.94 5.96 6.58.96-4.76 4.64 1.12 6.55L12 17.52l-5.88 3.09 1.12-6.55L2.48 9.42l6.58-.96z" /></svg></span>
        <svg class="star-rate__burst" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M24 1.5Q24 5 27.5 5 24 5 24 8.5 24 5 20.5 5 24 5 24 1.5ZM43 21Q43 24 46 24 43 24 43 27 43 24 40 24 43 24 43 21ZM24 39.5Q24 43 27.5 43 24 43 24 46.5 24 43 20.5 43 24 43 24 39.5ZM5 21Q5 24 8 24 5 24 5 27 5 24 2 24 5 24 5 21ZM36 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM36 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0Z" /></svg>
        <span class="star-rate__sr">3 stars, Okay</span>
      </label>
      <input class="star-rate__radio" type="radio" name="rating" value="4" id="star-rate-4">
      <label class="star-rate__star" for="star-rate-4" style="--star-rate-i: 3">
        <span class="star-rate__glyph" aria-hidden="true"><span class="star-rate__solid"></span><svg class="star-rate__line" viewBox="-3 -3 30 30" focusable="false"><path d="M12 2.5l2.94 5.96 6.58.96-4.76 4.64 1.12 6.55L12 17.52l-5.88 3.09 1.12-6.55L2.48 9.42l6.58-.96z" /></svg></span>
        <svg class="star-rate__burst" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M24 1.5Q24 5 27.5 5 24 5 24 8.5 24 5 20.5 5 24 5 24 1.5ZM43 21Q43 24 46 24 43 24 43 27 43 24 40 24 43 24 43 21ZM24 39.5Q24 43 27.5 43 24 43 24 46.5 24 43 20.5 43 24 43 24 39.5ZM5 21Q5 24 8 24 5 24 5 27 5 24 2 24 5 24 5 21ZM36 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM36 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0Z" /></svg>
        <span class="star-rate__sr">4 stars, Good</span>
      </label>
      <input class="star-rate__radio" type="radio" name="rating" value="5" id="star-rate-5">
      <label class="star-rate__star" for="star-rate-5" style="--star-rate-i: 4">
        <span class="star-rate__glyph" aria-hidden="true"><span class="star-rate__solid"></span><svg class="star-rate__line" viewBox="-3 -3 30 30" focusable="false"><path d="M12 2.5l2.94 5.96 6.58.96-4.76 4.64 1.12 6.55L12 17.52l-5.88 3.09 1.12-6.55L2.48 9.42l6.58-.96z" /></svg></span>
        <svg class="star-rate__burst" viewBox="0 0 48 48" aria-hidden="true" focusable="false"><path d="M24 1.5Q24 5 27.5 5 24 5 24 8.5 24 5 20.5 5 24 5 24 1.5ZM43 21Q43 24 46 24 43 24 43 27 43 24 40 24 43 24 43 21ZM24 39.5Q24 43 27.5 43 24 43 24 46.5 24 43 20.5 43 24 43 24 39.5ZM5 21Q5 24 8 24 5 24 5 27 5 24 2 24 5 24 5 21ZM36 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM36 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 37.4a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0ZM9.2 10.6a1.4 1.4 0 1 0 2.8 0 1.4 1.4 0 1 0-2.8 0Z" /></svg>
        <span class="star-rate__sr">5 stars, Amazing</span>
      </label>
    </fieldset>

    <div class="star-rate__more">
      <div class="star-rate__compose">
        <label class="star-rate__ask" for="star-rate-comment">
          <span><span class="star-rate__ask-low">What could we have done better?</span><span class="star-rate__ask-high">What did Sam do well?</span></span>
          <span class="star-rate__optional">Optional</span>
        </label>
        <textarea class="star-rate__comment" id="star-rate-comment" name="comment" rows="3" maxlength="500" placeholder="A sentence or two is plenty."></textarea>
        <div class="star-rate__actions">
          <p class="star-rate__note">Shared with Sam and our quality team.</p>
          <button class="star-rate__submit" type="submit">Send feedback</button>
        </div>
      </div>
      <p class="star-rate__thanks" tabindex="-1" hidden>
        <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="10" /><path d="m8 12.5 3 3 5-6" /></svg>
        <span><strong>Thanks for the feedback.</strong> Sam will see it today.</span>
      </p>
    </div>
  </form>
</div>
```

## CSS

```css
/* Demo backdrop */
.star-rate-demo {
  display: grid; place-items: center; min-height: 40rem; padding: 3rem var(--gutter);
  background:
    radial-gradient(50% 45% at 50% 0%, color-mix(in srgb, var(--accent) 14%, transparent), transparent 70%),
    radial-gradient(45% 40% at 0% 100%, color-mix(in srgb, var(--primary) 8%, transparent), transparent 70%),
    var(--surface-muted);
}

/* Card. Mood defaults: no rating yet */
.star-rate {
  --star-rate-s: 2.75rem;
  --star-rate-gold: color-mix(in srgb, var(--accent) 50%, var(--warning));
  --star-rate-dim: color-mix(in srgb, var(--text-muted) 80%, var(--surface-light));
  --star-rate-shape: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='-3 -3 30 30'%3E%3Cpath d='M12 2.5l2.94 5.96 6.58.96-4.76 4.64 1.12 6.55L12 17.52l-5.88 3.09 1.12-6.55L2.48 9.42l6.58-.96z' fill='black' stroke='black' stroke-width='1.5' stroke-linejoin='round'/%3E%3C/svg%3E");
  --star-rate-m: 0;
  --star-rate-tint: var(--surface-muted);
  --star-rate-mouth: path("M24 42 Q32 45 40 42 Q32 45 24 42 Z");
  --star-rate-eye-l: path("M21.5 27 Q24 23.5 26.5 27 Q24 30.5 21.5 27 Z");
  --star-rate-eye-r: path("M37.5 27 Q40 23.5 42.5 27 Q40 30.5 37.5 27 Z");
  position: relative; isolation: isolate; width: min(100%, 27rem); padding: clamp(1.5rem, 1rem + 2.5vw, 2.25rem);
  border-radius: var(--radius-2xl); background: var(--surface-light); color: var(--text-main);
  font-family: var(--font-sans); text-align: center; interpolate-size: allow-keywords;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl);
}
.star-rate::before {
  content: ""; position: absolute; inset: 0 0 auto; z-index: -1; height: 12rem; border-radius: inherit; pointer-events: none;
  background: radial-gradient(70% 100% at 50% 0%, color-mix(in srgb, var(--accent) 10%, transparent), transparent 75%);
}

/* The chosen star sets the mood; hovering a star previews it (hover selectors are more specific) */
.star-rate:has(.star-rate__radio[value="1"]:checked),
.star-rate:has(.star-rate__stars:enabled .star-rate__star:nth-of-type(1):hover) {
  --star-rate-m: 1; --star-rate-tint: color-mix(in srgb, var(--danger) 16%, var(--surface-light));
  --star-rate-mouth: path("M22 46 Q32 35 42 46 Q32 35 22 46 Z");
  --star-rate-eye-l: path("M21 26.5 Q24 25.5 27 28 Q24 30.5 21 26.5 Z");
  --star-rate-eye-r: path("M37 28 Q40 25.5 43 26.5 Q40 30.5 37 28 Z");
}
.star-rate:has(.star-rate__radio[value="2"]:checked),
.star-rate:has(.star-rate__stars:enabled .star-rate__star:nth-of-type(2):hover) {
  --star-rate-m: 2; --star-rate-tint: color-mix(in srgb, var(--warning) 16%, var(--surface-light));
  --star-rate-mouth: path("M23 44.5 Q32 40 41 44.5 Q32 40 23 44.5 Z");
  --star-rate-eye-l: path("M21.5 27.5 Q24 26.5 26.5 27.5 Q24 30.5 21.5 27.5 Z");
  --star-rate-eye-r: path("M37.5 27.5 Q40 26.5 42.5 27.5 Q40 30.5 37.5 27.5 Z");
}
.star-rate:has(.star-rate__radio[value="3"]:checked),
.star-rate:has(.star-rate__stars:enabled .star-rate__star:nth-of-type(3):hover) {
  --star-rate-m: 3; --star-rate-tint: color-mix(in srgb, var(--text-muted) 14%, var(--surface-light));
  --star-rate-mouth: path("M23 43 Q32 43 41 43 Q32 43 23 43 Z");
}
.star-rate:has(.star-rate__radio[value="4"]:checked),
.star-rate:has(.star-rate__stars:enabled .star-rate__star:nth-of-type(4):hover) {
  --star-rate-m: 4; --star-rate-tint: color-mix(in srgb, var(--primary-2) 18%, var(--surface-light));
  --star-rate-mouth: path("M22 41 Q32 49 42 41 Q32 49 22 41 Z");
  --star-rate-eye-l: path("M21.5 26.5 Q24 22.5 26.5 26.5 Q24 30 21.5 26.5 Z");
  --star-rate-eye-r: path("M37.5 26.5 Q40 22.5 42.5 26.5 Q40 30 37.5 26.5 Z");
}
.star-rate:has(.star-rate__radio[value="5"]:checked),
.star-rate:has(.star-rate__stars:enabled .star-rate__star:nth-of-type(5):hover) {
  --star-rate-m: 5; --star-rate-tint: color-mix(in srgb, var(--accent) 38%, var(--surface-light));
  --star-rate-mouth: path("M20 39 Q32 41 44 39 Q32 57 20 39 Z");
  --star-rate-eye-l: path("M21 28 Q24 22 27 28 Q24 25.5 21 28 Z");
  --star-rate-eye-r: path("M37 28 Q40 22 43 28 Q40 25.5 37 28 Z");
}

/* Header */
.star-rate__who {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.25rem 0.75rem 0.25rem 0.25rem;
  border-radius: var(--radius-full); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
  color: var(--text-muted); font-size: 0.8125rem;
}
.star-rate__who strong { color: var(--text-main); font-weight: 600; }
.star-rate__avatar {
  display: grid; place-items: center; width: 1.75rem; height: 1.75rem; border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-size: 0.6875rem; font-weight: 700;
}
.star-rate__title { margin: 1.25rem 0 0; font: 600 clamp(1.625rem, 1.3rem + 1.2vw, 2rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.star-rate__lead { max-width: 21rem; margin: 0.5rem auto 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.55; text-wrap: pretty; }

/* Face: mouth and eyes morph through CSS `d`; tint, tilt, cheeks and brows follow the mood */
.star-rate__face {
  display: block; width: 5.5rem; height: 5.5rem; margin: 1.5rem auto 0; overflow: visible;
  filter: drop-shadow(0 10px 16px color-mix(in srgb, var(--surface-deep) 12%, transparent));
  scale: calc(0.96 + var(--star-rate-m) * 0.012);
  rotate: calc((var(--star-rate-m) - 3) * clamp(0, var(--star-rate-m), 1) * 2deg);
  transition: scale var(--dur-4) var(--ease-spring), rotate var(--dur-4) var(--ease-spring);
}
.star-rate__head { fill: var(--star-rate-tint); stroke: color-mix(in srgb, var(--text-main) 12%, transparent); stroke-width: 1; transition: fill var(--dur-4) var(--ease-out); }
.star-rate__shine { fill: color-mix(in srgb, var(--surface-light) 65%, transparent); }
.star-rate__cheek { fill: color-mix(in srgb, var(--danger) 28%, transparent); opacity: clamp(0, var(--star-rate-m) - 3.5, 1); transition: opacity var(--dur-3) var(--ease-out); }
.star-rate__brow { fill: none; stroke: var(--text-main); stroke-width: 2; stroke-linecap: round; opacity: clamp(0, (2 - var(--star-rate-m)) * var(--star-rate-m), 1); transition: opacity var(--dur-3) var(--ease-out); }
.star-rate__eye-l, .star-rate__eye-r, .star-rate__mouth {
  fill: var(--text-main); stroke: var(--text-main); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round;
  transition: d var(--dur-4) var(--ease-spring);
}
@supports (d: path("M0 0")) {
  .star-rate__mouth { d: var(--star-rate-mouth); }
  .star-rate__eye-l { d: var(--star-rate-eye-l); }
  .star-rate__eye-r { d: var(--star-rate-eye-r); }
}

/* Word: every label sits in one cell; the mood's word rolls in, the others roll away */
.star-rate__words { display: grid; height: 1.75rem; margin: 0.625rem 0 0; font: 600 1.25rem/1.4 var(--font-display); letter-spacing: var(--tracking-tight); }
.star-rate__word {
  grid-area: 1 / 1;
  opacity: clamp(0, 1 - (var(--star-rate-m) - var(--star-rate-k)) * (var(--star-rate-m) - var(--star-rate-k)), 1);
  translate: 0 clamp(-1em, (var(--star-rate-k) - var(--star-rate-m)) * 0.6em, 1em);
  transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-spring);
}
.star-rate__word--idle { color: var(--text-muted); font: 500 1rem/1.75 var(--font-sans); letter-spacing: 0; }

/* Stars: native radios, labels as stars */
.star-rate__stars { position: relative; isolation: isolate; display: flex; justify-content: center; min-width: 0; margin: 0.75rem 0 0; padding: 0; border: 0; }
.star-rate__radio, .star-rate__sr {
  position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0; border: 0;
  overflow: hidden; clip: rect(0 0 0 0); clip-path: inset(50%); white-space: nowrap;
}
.star-rate__star {
  --star-rate-on: 0; --star-rate-ink: var(--star-rate-dim); --star-rate-body: var(--surface-muted);
  --star-rate-wait: calc((var(--star-rate-on) * var(--star-rate-i) + (1 - var(--star-rate-on)) * (4 - var(--star-rate-i))) * var(--stagger) / 2);
  position: relative; width: var(--star-rate-s); height: var(--star-rate-s); border-radius: 0.875rem; cursor: pointer;
}
/* Filled up to the checked star... */
.star-rate__radio:checked + .star-rate__star,
.star-rate__star:has(~ .star-rate__radio:checked) { --star-rate-on: 1; --star-rate-ink: var(--star-rate-gold); --star-rate-body: transparent; }
/* ...unless a star is hovered: then up to that one */
.star-rate__stars:enabled:has(.star-rate__star:hover) .star-rate__star { --star-rate-on: 0; --star-rate-ink: var(--star-rate-dim); --star-rate-body: var(--surface-muted); }
.star-rate__stars:enabled:has(.star-rate__star:hover) .star-rate__star:hover,
.star-rate__stars:enabled:has(.star-rate__star:hover) .star-rate__star:has(~ .star-rate__star:hover) { --star-rate-on: 1; --star-rate-ink: var(--star-rate-gold); --star-rate-body: transparent; }
.star-rate__stars:disabled .star-rate__star { cursor: default; }
.star-rate__radio:focus-visible + .star-rate__star { outline: 2px solid var(--primary); outline-offset: 3px; }

.star-rate__glyph { position: absolute; inset: 0; transition: scale var(--dur-3) var(--ease-spring); }
.star-rate__stars:enabled .star-rate__star:hover .star-rate__glyph { scale: 1.08; }
/* One gradient spans the row: each star shows its own fifth of it */
.star-rate__solid {
  position: absolute; inset: 0;
  background: linear-gradient(90deg, color-mix(in srgb, var(--accent) 55%, var(--surface-light)), var(--accent) 45%, color-mix(in srgb, var(--accent) 55%, var(--warning))) calc(var(--star-rate-i) * 25%) 0 / 500% 100%;
  -webkit-mask: var(--star-rate-shape) center / 100% 100% no-repeat;
  mask: var(--star-rate-shape) center / 100% 100% no-repeat;
  clip-path: inset(0 calc((1 - var(--star-rate-on)) * 100%) 0 0);
  transition: clip-path var(--dur-3) var(--ease-out) var(--star-rate-wait);
}
.star-rate__line {
  position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible;
  fill: var(--star-rate-body); stroke: var(--star-rate-ink); stroke-width: 1.5; stroke-linejoin: round;
  transition: fill var(--dur-3) var(--ease-out) var(--star-rate-wait), stroke var(--dur-3) var(--ease-out) var(--star-rate-wait);
}
/* The chosen star pops and throws a sparkle burst */
.star-rate__burst { position: absolute; left: 50%; top: 50%; z-index: -1; width: 190%; height: 190%; translate: -50% -50%; overflow: visible; pointer-events: none; fill: var(--accent); opacity: 0; }
.star-rate__radio:checked + .star-rate__star .star-rate__glyph { animation: star-rate-pop var(--dur-4) var(--ease-out); }
.star-rate__radio:checked + .star-rate__star .star-rate__burst { animation: star-rate-burst var(--dur-5) var(--ease-out); }

/* Comment panel: opens once a rating is chosen (height: auto via interpolate-size) */
.star-rate__more {
  height: 0; overflow: clip; opacity: 0; visibility: hidden; text-align: left;
  transition: height var(--dur-4) var(--ease-out), opacity var(--dur-3) var(--ease-out), visibility 0s linear var(--dur-4);
}
.star-rate:has(.star-rate__radio:checked) .star-rate__more {
  height: auto; opacity: 1; visibility: visible;
  transition: height var(--dur-4) var(--ease-out), opacity var(--dur-4) var(--ease-out) var(--dur-1), visibility 0s;
}
.star-rate__compose { display: grid; gap: 0.625rem; padding: 1.5rem 0.25rem 0.25rem; }
.star-rate__compose[hidden] { display: none; }
.star-rate__ask { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; font-size: 0.9375rem; font-weight: 600; }
.star-rate__ask-high { display: none; }
.star-rate:has(.star-rate__radio[value="4"]:checked, .star-rate__radio[value="5"]:checked) .star-rate__ask-low { display: none; }
.star-rate:has(.star-rate__radio[value="4"]:checked, .star-rate__radio[value="5"]:checked) .star-rate__ask-high { display: inline; }
.star-rate__optional { color: var(--text-muted); font-size: 0.8125rem; font-weight: 500; }
.star-rate__comment {
  display: block; width: 100%; min-height: 5.5rem; max-height: 12rem; padding: 0.75rem 0.875rem; border: 0; border-radius: var(--radius-lg); resize: vertical;
  background: var(--surface-muted); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle);
  font: 400 0.9375rem/1.5 var(--font-sans); field-sizing: content;
  transition: background-color var(--dur-2) var(--ease-out), box-shadow var(--dur-2) var(--ease-out);
}
.star-rate__comment::placeholder { color: var(--text-muted); }
.star-rate__comment:focus-visible { outline: 2px solid transparent; background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--primary), var(--focus-ring); }
.star-rate__actions { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem 1rem; margin-top: 0.25rem; }
.star-rate__note { margin: 0; color: var(--text-muted); font-size: 0.8125rem; }
.star-rate__submit {
  height: 2.75rem; padding: 0 1.25rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font: 600 0.9375rem var(--font-sans);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 10px 24px -10px var(--primary);
  transition: transform var(--dur-3) var(--ease-spring), opacity var(--dur-2) var(--ease-out);
}
.star-rate__submit:active { transform: scale(0.97); }
.star-rate__submit:disabled { cursor: progress; opacity: 0.75; }
.star-rate__submit:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.star-rate__thanks {
  display: flex; align-items: center; gap: 0.75rem; margin: 1.5rem 0.25rem 0.25rem; padding: 0.875rem 1rem;
  border-radius: var(--radius-lg); background: color-mix(in srgb, var(--success) 10%, var(--surface-light)); font-size: 0.9375rem; line-height: 1.45;
}
.star-rate__thanks[hidden] { display: none; }
.star-rate__thanks:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.star-rate__thanks svg { flex: none; }
.star-rate__thanks circle { fill: var(--success); }
.star-rate__thanks path { fill: none; stroke: var(--text-inverse); stroke-width: 2.5; stroke-linecap: round; stroke-linejoin: round; }
::view-transition-group(star-rate-card) { animation-duration: var(--dur-4); animation-timing-function: var(--ease-out); }

@media (min-width: 768px) {
  .star-rate { --star-rate-s: 3.25rem; }
}
@media (prefers-reduced-motion: reduce) {
  .star-rate *, .star-rate *::before, .star-rate *::after { animation: none !important; }
}
@keyframes star-rate-pop {
  0% { scale: 1; rotate: 0deg; }
  30% { scale: 1.32; rotate: -10deg; }
  62% { scale: 0.94; rotate: 4deg; }
  100% { scale: 1; rotate: 0deg; }
}
@keyframes star-rate-burst {
  0% { opacity: 0; scale: 0.35; rotate: -25deg; }
  25% { opacity: 1; }
  100% { opacity: 0; scale: 1.15; rotate: 20deg; }
}
```

## JS

```js
const morphs = CSS.supports('d', 'path("M0 0")');

document.querySelectorAll('[data-star-rate]').forEach((form) => {
  const $ = (part) => form.querySelector(`.star-rate__${part}`);
  const [stars, compose, thanks, submit] = ['stars', 'compose', 'thanks', 'submit'].map($);
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');

  // No CSS `d` (Safari): copy the mood's path data onto the face, so it swaps instead of morphing
  if (!morphs) {
    const parts = ['mouth', 'eye-l', 'eye-r'].map((part) => [$(part), `--star-rate-${part}`]);
    let frame = 0;
    const swap = () => {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(() => {
        const style = getComputedStyle(form);
        parts.forEach(([path, prop]) => {
          const d = style.getPropertyValue(prop).match(/path\(\s*["']([^"']+)["']\s*\)/);
          if (d) path.setAttribute('d', d[1]);
        });
      });
    };
    ['change', 'pointerover', 'pointerout'].forEach((type) => stars.addEventListener(type, swap));
    swap(); // a rating restored by the browser on reload
  }

  // Demo send. Post it for real with fetch(form.action, { method: 'POST', body: new FormData(form) })
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    submit.disabled = true;
    submit.textContent = 'Sending…';
    setTimeout(() => {
      const done = () => {
        form.dataset.state = 'sent';
        stars.disabled = true;
        compose.hidden = true;
        thanks.hidden = false;
        thanks.focus();
      };
      if (reduce.matches || !document.startViewTransition) return done();
      // Name the card only for this transition, so several cards can share a page
      form.style.viewTransitionName = 'star-rate-card';
      document.startViewTransition(done).finished.finally(() => { form.style.viewTransitionName = ''; });
    }, 700);
  });
});
```

## Notes

- A real radio group inside a `fieldset` with a `legend`. Arrow keys move and select, Tab enters and leaves the group, and each label carries a hidden name ("4 stars, Good"). The face and the rolling word are `aria-hidden`, because the radio names already say it. The comment panel stays `visibility: hidden` until a rating is chosen, so its fields stay out of the tab order. After sending, focus moves to the thank-you note.
- CSS does all of it, JS or not. `:has()` fills the stars up to the checked or hovered one. One rule per rating sets the face's `path()` data, tint and a mood index in custom properties, which drive the CSS `d` morph, the word, the cheeks and the brows. The panel opens with `height: auto` through `interpolate-size`. Without JS the form posts normally. JS only adds the Safari path swap (no CSS `d` there) and the demo's sent state.
- Reduced motion: no pop, sparkle burst, `d` morph, face tilt bounce or word roll. Every change is instant (token durations and `--stagger` collapse), and nothing loops.
- Contrast: the star outlines are at least 3:1 against the card in both states (`--text-muted` at 80% is about 3.2:1, and the filled gold edge `--accent`/`--warning` is about 3.2:1). Text is `--text-main` or `--text-muted` on white, and the white submit label sits on `--primary` (5.2:1).
- `interpolate-size` and CSS `d` are Chromium/Firefox-era features. Elsewhere the panel opens without the height glide and the face swaps expressions. To retheme, change the gold mix in `.star-rate__solid` and the mood tints. For a different scale, add radios and matching mood rules.
