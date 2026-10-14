# Holographic Membership Card

A "Brand Care Club" membership card at true credit-card proportions, floating in a deep section beside the benefits copy. Its brushed-silver surface carries a holographic foil: iridescent bands, a fine diffraction grating and sparkles that shift as the card tilts towards the pointer on a real spring, with a glare that follows the light. A button flips the card to show the perks on its back. On touch the card tilts as you drag it, a single shimmer sweeps across it when it enters view, and the layout stacks heading, card, then benefits. Depends on `tokens/variables.css`.

**Motion:** pointer tilt on a JS spring (stiffness 170, damping 16, rAF) driving foil `background-position`, glare and sparkle mask · glare fade (`--dur-4` `--ease-out`) · flip `rotateY(180deg)` (`--dur-5` `--ease-spring`) · one-shot shimmer sweep on entering view · CTA arrow nudge (`--ease-spring`).

## HTML

```html
<section class="holo-card" aria-labelledby="holo-card-title" data-holo-card>
  <div class="holo-card__inner">
    <header class="holo-card__head">
      <p class="holo-card__eyebrow"><span class="holo-card__gem" aria-hidden="true"></span>Brand Care Club</p>
      <h2 id="holo-card-title" class="holo-card__title">Your home, at the front of the queue.</h2>
      <p class="holo-card__lead">One membership covers every trade we offer, from a dripping tap in Westlake to a new roof in Riverside.</p>
    </header>

    <div class="holo-card__stage">
      <div class="holo-card__scene" role="group" aria-label="Brand Care Club membership card">
        <span class="holo-card__aura" aria-hidden="true"></span>
        <div class="holo-card__tilt">
          <div class="holo-card__flipper">
            <div class="holo-card__face holo-card__face--front">
              <span class="holo-card__foil" aria-hidden="true"></span>
              <span class="holo-card__sparkle" aria-hidden="true"></span>
              <span class="holo-card__glare" aria-hidden="true"></span>
              <span class="holo-card__sheen" aria-hidden="true"></span>
              <div class="holo-card__row">
                <p class="holo-card__brand">
                  <svg viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M3 10.5 12 3l9 7.5" /><path d="M5 9v11h14V9" /><path d="M9.5 20v-5.5h5V20" /></svg>
                  Brand <span>Care Club</span>
                </p>
                <p class="holo-card__tier"><span class="holo-card__sr">Tier: </span>Premier</p>
              </div>
              <div class="holo-card__row holo-card__row--mid" aria-hidden="true">
                <span class="holo-card__chip"></span>
                <svg class="holo-card__wave" viewBox="0 0 24 24" width="24" height="24" focusable="false"><path d="M7 8.5a5 5 0 0 1 0 7" /><path d="M10.5 6a8.5 8.5 0 0 1 0 12" /><path d="M14 3.5a12 12 0 0 1 0 17" /></svg>
              </div>
              <p class="holo-card__number"><span class="holo-card__sr">Member number </span>0427 1185 3092</p>
              <div class="holo-card__row holo-card__row--end">
                <p class="holo-card__field"><span class="holo-card__label">Member</span> Jordan Rivera</p>
                <p class="holo-card__field holo-card__field--end"><span class="holo-card__label">Since</span> 03/21</p>
              </div>
            </div>

            <div class="holo-card__face holo-card__face--back">
              <span class="holo-card__foil" aria-hidden="true"></span>
              <span class="holo-card__glare" aria-hidden="true"></span>
              <div class="holo-card__row">
                <h3 class="holo-card__perks-title">Member perks</h3>
                <svg class="holo-card__mark" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false"><path d="M3 10.5 12 3l9 7.5" /><path d="M5 9v11h14V9" /><path d="M9.5 20v-5.5h5V20" /></svg>
              </div>
              <ul class="holo-card__perks" role="list">
                <li>Priority same-day booking</li>
                <li>15% off parts and labour</li>
                <li>Free yearly safety check</li>
                <li>No call-out fees, ever</li>
              </ul>
              <div class="holo-card__row holo-card__row--end">
                <p class="holo-card__phone"><span class="holo-card__label">Members line</span> (555) 555-0123</p>
                <span class="holo-card__barcode" aria-hidden="true"></span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="holo-card__controls">
        <button class="holo-card__flip" type="button" hidden>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8" /><path d="M21 3v5h-5" /><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16" /><path d="M3 21v-5h5" /></svg>
          <span class="holo-card__flip-label">Show perks</span>
        </button>
        <p class="holo-card__hint" aria-hidden="true" hidden>
          <span class="holo-card__hint-mouse">Move across the card to catch the light</span>
          <span class="holo-card__hint-touch">Drag the card to tilt it</span>
        </p>
      </div>
    </div>

    <div class="holo-card__body">
      <ul class="holo-card__benefits" role="list">
        <li>
          <span class="holo-card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg></span>
          <div><h3>Priority booking</h3><p>First pick of same-day slots across Springfield, every day of the week.</p></div>
        </li>
        <li>
          <span class="holo-card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M20.6 13.4 13.4 20.6a2 2 0 0 1-2.8 0L3 13V3h10l7.6 7.6a2 2 0 0 1 0 2.8z" /><path d="M7.5 7.5h.01" /></svg></span>
          <div><h3>Member pricing</h3><p>15% off parts and labour on every job, in every trade.</p></div>
        </li>
        <li>
          <span class="holo-card__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="20" height="20" focusable="false"><path d="M12 22s8-3.5 8-10V5l-8-3-8 3v7c0 6.5 8 10 8 10z" /><path d="m9 12 2 2 4-4" /></svg></span>
          <div><h3>A yearly check, on us</h3><p>Plumbing, electrics and roof inspected once a year, with a written report.</p></div>
        </li>
      </ul>

      <div class="holo-card__offer">
        <p class="holo-card__price"><strong>$12</strong> / month</p>
        <p class="holo-card__terms">Cancel anytime. Members save $340 a year on average.</p>
      </div>
      <div class="holo-card__actions">
        <a class="holo-card__cta" href="#join">
          Join the club
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
        <a class="holo-card__link" href="#tiers">Compare tiers</a>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
/* Local foil palette: the only colour literals in this file */
.holo-card {
  --holo-card-rose: #ff6fb5;
  --holo-card-amber: #ffc857;
  --holo-card-mint: #4ff0c1;
  --holo-card-sky: #5cc8ff;
  --holo-card-violet: #a07cff;
  --holo-card-spectrum: var(--holo-card-rose), var(--holo-card-amber), var(--holo-card-mint), var(--holo-card-sky), var(--holo-card-violet), var(--holo-card-rose);
  --holo-card-chip-line: color-mix(in srgb, var(--warning) 55%, transparent);
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(42rem 30rem at 22% 58%, color-mix(in srgb, var(--holo-card-violet) 16%, transparent), transparent 70%),
    radial-gradient(34rem 22rem at 88% 6%, color-mix(in srgb, var(--primary-2) 18%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.holo-card svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* Layout: heading, card, benefits on phones; card beside the copy from 768px */
.holo-card__inner {
  display: grid; gap: var(--space-2xl); grid-template-areas: "head" "stage" "body";
  max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter);
}
.holo-card__head { grid-area: head; max-width: 34rem; }
.holo-card__stage { grid-area: stage; display: grid; justify-items: center; gap: var(--space-xl); padding-block: var(--space-md); }
.holo-card__body { grid-area: body; max-width: 34rem; }

.holo-card__eyebrow { display: inline-flex; align-items: center; gap: 0.625rem; margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; }
.holo-card__gem { width: 0.625rem; height: 0.625rem; border-radius: var(--radius-sm); rotate: 45deg; background: conic-gradient(var(--holo-card-spectrum)); box-shadow: 0 0 14px color-mix(in srgb, var(--holo-card-sky) 60%, transparent); }
.holo-card__title { margin: 1rem 0 0; font: 600 clamp(2rem, 1.2rem + 3.2vw, 3.5rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.holo-card__lead { margin: 1.25rem 0 0; max-width: 32rem; color: var(--text-inverse-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }

/* Scene. Without JS both faces sit flat, one above the other */
.holo-card__scene { position: relative; isolation: isolate; width: min(100%, 24rem); container-type: inline-size; }
.holo-card__flipper { display: grid; gap: var(--space-lg); }
.holo-card__aura {
  position: absolute; inset: -22% -14%; z-index: -1; pointer-events: none; opacity: 0.32;
  background: conic-gradient(from 200deg, var(--holo-card-spectrum));
  -webkit-mask-image: radial-gradient(closest-side, black, transparent);
  mask-image: radial-gradient(closest-side, black, transparent);
  rotate: calc(var(--holo-card-x, 0) * 50deg);
}

/* With JS: one card in 3D. The tilt wrapper reads the spring values, the flipper turns */
.holo-card--js .holo-card__scene { aspect-ratio: 1.586; perspective: 1000px; touch-action: pan-y; -webkit-user-select: none; user-select: none; }
.holo-card--js .holo-card__tilt, .holo-card--js .holo-card__flipper { position: absolute; inset: 0; transform-style: preserve-3d; }
.holo-card--js .holo-card__tilt { will-change: transform; transform: rotateX(calc(var(--holo-card-y, 0) * -12deg)) rotateY(calc(var(--holo-card-x, 0) * 16deg)); }
.holo-card--js .holo-card__flipper { transition: transform var(--dur-5) var(--ease-spring); }
.holo-card--js.is-flipped .holo-card__flipper { transform: rotateY(180deg); }
.holo-card--js .holo-card__face { position: absolute; inset: 0; -webkit-backface-visibility: hidden; backface-visibility: hidden; transition: visibility 0s linear; }
.holo-card--js .holo-card__face--back { transform: rotateY(180deg); }
/* The face turned away is inert (JS) and hidden once it has rotated past edge-on */
.holo-card--js .holo-card__face[inert] { visibility: hidden; transition-delay: var(--dur-3); }

/* Card faces: brushed-silver base (dark enough for overlay to show colour), ink above the foil layers */
.holo-card__face {
  position: relative; display: grid; grid-template-rows: auto 1fr auto auto; align-content: space-between; aspect-ratio: 1.586;
  overflow: hidden; isolation: isolate; padding: 6.5cqi 7cqi; border-radius: var(--radius-xl); color: var(--text-main);
  background: linear-gradient(125deg,
    color-mix(in srgb, var(--text-inverse-muted) 30%, var(--surface-light)) 0%, color-mix(in srgb, var(--text-inverse-muted) 60%, var(--surface-light)) 30%,
    var(--border-subtle) 52%, color-mix(in srgb, var(--text-inverse-muted) 70%, var(--surface-light)) 78%, color-mix(in srgb, var(--text-inverse-muted) 45%, var(--surface-light)) 100%);
  box-shadow:
    inset 0 0 0 1px color-mix(in srgb, var(--surface-light) 65%, transparent), var(--highlight),
    0 30px 60px -24px color-mix(in srgb, var(--holo-card-violet) 55%, transparent);
}
.holo-card__face > * { position: relative; z-index: 1; margin: 0; }
.holo-card__face--back { grid-template-rows: auto 1fr auto; gap: 2.4cqi; }

/* Foil: iridescent bands plus a fine grating, shifted against the tilt */
.holo-card__foil, .holo-card__sparkle, .holo-card__glare, .holo-card__sheen { position: absolute; inset: 0; z-index: 0; pointer-events: none; }
.holo-card__foil {
  background:
    repeating-linear-gradient(-55deg, color-mix(in srgb, var(--surface-light) 38%, transparent) 0 1px, transparent 1px 4px),
    repeating-linear-gradient(115deg, var(--holo-card-rose) 0%, var(--holo-card-amber) 6%, var(--holo-card-mint) 12%, var(--holo-card-sky) 18%, var(--holo-card-violet) 24%, var(--holo-card-rose) 30%);
  background-size: auto, 300% 300%;
  background-position: 0 0, calc(50% - var(--holo-card-x, 0) * 45%) calc(50% - var(--holo-card-y, 0) * 45%);
  mix-blend-mode: overlay; opacity: 0.9;
}
.holo-card__face--back .holo-card__foil { opacity: 0.5; }
/* Sparkles glint only near the light */
.holo-card__sparkle {
  background:
    radial-gradient(circle, var(--surface-light) 0 0.75px, transparent 1.5px) 0 0 / 11px 13px,
    radial-gradient(circle, var(--surface-light) 0 0.6px, transparent 1.25px) 5px 7px / 17px 19px,
    radial-gradient(circle, var(--holo-card-sky) 0 1px, transparent 1.75px) 9px 3px / 29px 23px;
  mix-blend-mode: color-dodge;
  translate: calc(var(--holo-card-x, 0) * -4px) calc(var(--holo-card-y, 0) * -4px);
  -webkit-mask-image: radial-gradient(circle at calc(50% + var(--holo-card-x, 0) * 50%) calc(50% + var(--holo-card-y, 0) * 50%), black, transparent 60%);
  mask-image: radial-gradient(circle at calc(50% + var(--holo-card-x, 0) * 50%) calc(50% + var(--holo-card-y, 0) * 50%), black, transparent 60%);
}
/* Glare follows the pointer; it only ever lightens, so the ink keeps its contrast */
.holo-card__glare {
  background: radial-gradient(circle at calc(50% + var(--holo-card-x, 0) * 50%) calc(50% + var(--holo-card-y, 0) * 50%),
    color-mix(in srgb, var(--surface-light) 90%, transparent), color-mix(in srgb, var(--surface-light) 30%, transparent) 22%, transparent 55%);
  mix-blend-mode: overlay; opacity: 0; transition: opacity var(--dur-4) var(--ease-out);
}
.holo-card__scene.is-lit .holo-card__glare { opacity: 1; }
/* One shimmer sweep when the card first comes into view */
.holo-card__sheen {
  background: linear-gradient(105deg, transparent 32%, color-mix(in srgb, var(--surface-light) 75%, transparent) 46%, color-mix(in srgb, var(--holo-card-sky) 55%, transparent) 50%, color-mix(in srgb, var(--holo-card-rose) 50%, transparent) 54%, transparent 68%);
  mix-blend-mode: overlay; transform: translateX(-130%);
}
.holo-card.is-swept .holo-card__sheen { animation: holo-card-sweep 1.6s var(--ease-in-out) 0.2s both; }

/* Front details */
.holo-card__row { display: flex; align-items: center; justify-content: space-between; gap: 3cqi; }
.holo-card__row--mid { justify-content: flex-start; gap: 3.5cqi; }
.holo-card__row--end { align-items: flex-end; }
.holo-card__brand { display: inline-flex; align-items: center; gap: 1.8cqi; font: 700 clamp(0.8125rem, 4.4cqi, 1.0625rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.holo-card__brand span { font-weight: 500; }
.holo-card__brand svg, .holo-card__mark { width: max(1rem, 6.5cqi); height: max(1rem, 6.5cqi); }
.holo-card__tier {
  padding: 1.4cqi 2.8cqi; border-radius: var(--radius-full); background: var(--text-main); color: var(--surface-light);
  font: 600 clamp(0.6875rem, 2.8cqi, 0.75rem)/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; box-shadow: var(--highlight-inverse);
}
.holo-card__chip {
  width: 12.5cqi; aspect-ratio: 1.32; border-radius: 1.8cqi;
  background:
    linear-gradient(90deg, transparent 31%, var(--holo-card-chip-line) 31% 34%, transparent 34% 66%, var(--holo-card-chip-line) 66% 69%, transparent 69%),
    linear-gradient(transparent 46%, var(--holo-card-chip-line) 46% 54%, transparent 54%),
    linear-gradient(135deg, color-mix(in srgb, var(--accent) 40%, var(--surface-light)), var(--accent) 50%, color-mix(in srgb, var(--accent) 65%, var(--warning)));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--warning) 50%, transparent), var(--highlight);
}
.holo-card__wave { width: max(1rem, 6.5cqi); height: max(1rem, 6.5cqi); }
.holo-card__number {
  font: 500 clamp(1rem, 6.4cqi, 1.5rem)/1 var(--font-mono); letter-spacing: 0.06em; word-spacing: 0.18em; white-space: nowrap; font-variant-numeric: tabular-nums;
  text-shadow: 0 1px 0 color-mix(in srgb, var(--surface-light) 85%, transparent), 0 -1px 0 color-mix(in srgb, var(--text-main) 25%, transparent);
}
.holo-card__field, .holo-card__phone { display: grid; gap: 1.2cqi; font: 600 clamp(0.8125rem, 4.2cqi, 1rem)/1.1 var(--font-sans); }
.holo-card__field--end { text-align: end; }
.holo-card__label { font: 500 clamp(0.6875rem, 2.6cqi, 0.75rem)/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }

/* Back details */
.holo-card__perks-title { font: 600 clamp(0.6875rem, 3cqi, 0.8125rem)/1 var(--font-mono); letter-spacing: 0.16em; text-transform: uppercase; }
.holo-card__perks { display: grid; align-content: center; gap: 1.3cqi; padding: 0; list-style: none; font: 500 clamp(0.6875rem, 3.6cqi, 0.875rem)/1.25 var(--font-sans); }
.holo-card__perks li { display: flex; align-items: center; gap: 2.2cqi; }
.holo-card__perks li::before { content: ""; flex: none; width: max(0.5rem, 2.6cqi); height: max(0.25rem, 1.3cqi); border: solid currentColor; border-width: 0 0 2px 2px; rotate: -45deg; translate: 0 -25%; }
.holo-card__phone { font-variant-numeric: tabular-nums; }
.holo-card__barcode {
  width: 30cqi; height: 8cqi; border-radius: var(--radius-sm); opacity: 0.85;
  background: repeating-linear-gradient(90deg, var(--text-main) 0 1px, transparent 1px 3px, var(--text-main) 3px 5px, transparent 5px 6px, var(--text-main) 6px 7px, transparent 7px 10px, var(--text-main) 10px 12px, transparent 12px 13px);
}

/* Flip button and hint */
.holo-card__controls { display: grid; justify-items: center; gap: var(--space-sm); }
.holo-card__flip {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.25rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse); font: 600 0.875rem var(--font-sans);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.holo-card__flip:hover { background: color-mix(in srgb, var(--text-inverse) 10%, transparent); }
.holo-card__flip:active { transform: scale(0.96); }
.holo-card__flip svg { transition: transform var(--dur-5) var(--ease-spring); }
.holo-card.is-flipped .holo-card__flip svg { transform: rotate(180deg); }
.holo-card__flip[hidden], .holo-card__hint[hidden] { display: none; }
.holo-card__hint { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1.4 var(--font-mono); letter-spacing: 0.04em; text-align: center; }
.holo-card__hint-touch { display: none; }
@media (hover: none) {
  .holo-card__hint-mouse { display: none; }
  .holo-card__hint-touch { display: inline; }
}

/* Benefits, price and CTA */
.holo-card__benefits { display: grid; gap: var(--space-lg); margin: 0; padding: 0; list-style: none; }
.holo-card__benefits li { display: grid; grid-template-columns: auto 1fr; gap: var(--space-md); align-items: start; }
.holo-card__icon {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border: 1px solid transparent; border-radius: var(--radius-lg); color: var(--text-inverse);
  background: linear-gradient(var(--surface-deep), var(--surface-deep)) padding-box, conic-gradient(from 200deg, var(--holo-card-spectrum)) border-box;
  box-shadow: var(--highlight-inverse), 0 8px 24px -12px color-mix(in srgb, var(--holo-card-sky) 70%, transparent);
}
.holo-card__benefits h3 { margin: 0.125rem 0 0; font: 600 1.0625rem/1.3 var(--font-display); letter-spacing: -0.01em; }
.holo-card__benefits p { margin: 0.25rem 0 0; color: var(--text-inverse-muted); font-size: 0.9375rem; line-height: 1.55; }
.holo-card__offer { display: flex; flex-wrap: wrap; align-items: baseline; gap: 0.25rem var(--space-md); margin-top: var(--space-xl); padding-top: var(--space-lg); border-top: 1px solid var(--border-inverse); }
.holo-card__price { margin: 0; color: var(--text-inverse-muted); font-size: 0.9375rem; }
.holo-card__price strong { color: var(--text-inverse); font: 600 2.25rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.holo-card__terms { margin: 0; color: var(--text-inverse-muted); font-size: 0.875rem; }
.holo-card__actions { display: flex; flex-wrap: wrap; align-items: center; gap: var(--space-sm) var(--space-lg); margin-top: var(--space-lg); }
.holo-card__cta {
  position: relative; display: inline-flex; align-items: center; gap: 0.5rem; height: 3rem; padding: 0 1.375rem; overflow: hidden; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: 0 12px 40px -12px color-mix(in srgb, var(--holo-card-violet) 80%, transparent);
  transition: transform var(--dur-2) var(--ease-out), box-shadow var(--dur-3);
}
.holo-card__cta::after {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(110deg, transparent 35%, color-mix(in srgb, var(--holo-card-sky) 30%, transparent) 48%, color-mix(in srgb, var(--holo-card-rose) 25%, transparent) 54%, transparent 66%);
  transform: translateX(-110%); transition: transform var(--dur-5) var(--ease-out);
}
.holo-card__cta:hover { transform: translateY(-1px); box-shadow: 0 16px 48px -10px color-mix(in srgb, var(--holo-card-sky) 70%, transparent); }
.holo-card__cta:hover::after { transform: translateX(110%); }
.holo-card__cta:active { transform: scale(0.97); }
.holo-card__cta svg { transition: transform var(--dur-3) var(--ease-spring); }
.holo-card__cta:hover svg { transform: translateX(3px); }
.holo-card__link {
  padding-block: 0.75rem; color: var(--text-inverse); font-size: 0.9375rem; font-weight: 600;
  text-decoration: underline; text-decoration-color: color-mix(in srgb, var(--text-inverse) 35%, transparent); text-underline-offset: 0.25em;
  transition: text-decoration-color var(--dur-2);
}
.holo-card__link:hover { text-decoration-color: currentColor; }
.holo-card :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.holo-card__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

@media (min-width: 768px) {
  .holo-card__inner { grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr); grid-template-areas: "stage head" "stage body"; column-gap: clamp(2.5rem, 6vw, 5.5rem); row-gap: var(--space-xl); }
  .holo-card__head { align-self: end; }
  .holo-card__body { align-self: start; }
}
@media (prefers-reduced-motion: reduce) {
  .holo-card *, .holo-card *::before, .holo-card *::after { animation: none !important; }
  .holo-card__glare { display: none; }
}

@keyframes holo-card-sweep { to { transform: translateX(130%); } }
```

## JS

```js
document.querySelectorAll('[data-holo-card]').forEach((root) => {
  const scene = root.querySelector('.holo-card__scene');
  const [front, back] = root.querySelectorAll('.holo-card__face');
  const flip = root.querySelector('.holo-card__flip');
  const label = root.querySelector('.holo-card__flip-label');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const clamp = (v) => Math.max(-1, Math.min(1, v));
  const s = { x: 0, y: 0, vx: 0, vy: 0, tx: 0, ty: 0 };
  let frame = 0;
  let last = 0;
  let pointer = null; // { x, y } for a hovering mouse; plus { sx, sy } for a touch or pen drag

  root.classList.add('holo-card--js');
  back.inert = true;
  flip.hidden = false;
  root.querySelector('.holo-card__hint').hidden = reduce.matches;

  // Flip: CSS turns the card; the face turned away is inert, so Tab and AT only reach the visible side
  flip.addEventListener('click', () => {
    const flipped = root.classList.toggle('is-flipped');
    front.inert = flipped;
    back.inert = !flipped;
    label.textContent = flipped ? 'Show front' : 'Show perks';
  });

  // One damped spring per axis (k 170, c 16): slight lag while following, a small overshoot on release
  const tick = (now) => {
    const dt = last ? Math.min((now - last) / 1000, 0.032) : 1 / 60;
    last = now;
    if (pointer) {
      const r = scene.getBoundingClientRect();
      s.tx = clamp(pointer.sx === undefined ? ((pointer.x - r.left) / r.width) * 2 - 1 : ((pointer.x - pointer.sx) / r.width) * 2.4);
      s.ty = clamp(pointer.sy === undefined ? ((pointer.y - r.top) / r.height) * 2 - 1 : ((pointer.y - pointer.sy) / r.height) * 2.4);
    }
    s.vx += (170 * (s.tx - s.x) - 16 * s.vx) * dt;
    s.vy += (170 * (s.ty - s.y) - 16 * s.vy) * dt;
    s.x += s.vx * dt;
    s.y += s.vy * dt;
    const done = Math.abs(s.tx - s.x) + Math.abs(s.ty - s.y) + Math.abs(s.vx) + Math.abs(s.vy) < 0.002;
    if (done) Object.assign(s, { x: s.tx, y: s.ty, vx: 0, vy: 0 });
    scene.style.setProperty('--holo-card-x', s.x.toFixed(4));
    scene.style.setProperty('--holo-card-y', s.y.toFixed(4));
    frame = done ? 0 : requestAnimationFrame(tick);
  };
  const wake = () => {
    if (frame) return;
    last = 0;
    frame = requestAnimationFrame(tick);
  };

  // Mouse: the card follows the cursor. Touch and pen: drag to tilt (vertical swipes still scroll the page)
  scene.addEventListener('pointermove', (e) => {
    if (reduce.matches || (e.pointerType !== 'mouse' && !pointer)) return;
    pointer = { ...pointer, x: e.clientX, y: e.clientY };
    scene.classList.add('is-lit');
    wake();
  }, { passive: true });
  scene.addEventListener('pointerdown', (e) => {
    if (reduce.matches || e.pointerType === 'mouse') return;
    pointer = { x: e.clientX, y: e.clientY, sx: e.clientX, sy: e.clientY };
    scene.setPointerCapture(e.pointerId);
    scene.classList.add('is-lit');
  });
  const release = (e) => {
    if (e.pointerType === 'mouse' && e.type !== 'pointerleave') return;
    pointer = null;
    s.tx = 0;
    s.ty = 0;
    scene.classList.remove('is-lit');
    wake();
  };
  ['pointerup', 'pointercancel', 'pointerleave'].forEach((type) => scene.addEventListener(type, release));

  // A single shimmer sweep the first time the card is mostly in view
  new IntersectionObserver(([entry], io) => {
    if (!entry.isIntersecting) return;
    root.classList.add('is-swept');
    io.disconnect();
  }, { threshold: 0.6 }).observe(scene);
});
```

## Notes

- The card is a labelled group. Foil layers, chip, contactless mark and barcode are `aria-hidden`, and the number carries a visually hidden "Member number" prefix. The flip button's label switches between "Show perks" and "Show front". The face turned away is `inert`, so it's out of the Tab order and the accessibility tree, and it becomes `visibility: hidden` once it has turned past edge-on.
- Without JS both faces lie flat, front above back, with no tilt or flip button, so every perk can still be read.
- On touch, `touch-action: pan-y` lets vertical swipes scroll the page while a sideways drag tilts the card; it springs back on release or when the browser takes over the scroll. Under reduced motion the spring never starts, so there's no tilt or glare: the foil stays at rest, the flip is instant (token durations) and the shimmer sweep is off.
- Contrast: card ink is `--text-main` on the silver base with its overlay foil, at least 8.1:1 at the darkest computed point (the glare and sparkles only lighten). The tier pill is 14.6:1. Section copy is `--text-inverse` at 18.8:1 and `--text-inverse-muted` at 6.3:1 or better over the coloured glows.
- To retheme, swap the five `--holo-card-*` hues (golds and ambers make a "Gold tier" foil) and keep the silver base dark enough for `overlay` to show colour. Card text scales with container units (`cqi`: Chrome 105+, Safari 16+, Firefox 110+), and the 3D uses `preserve-3d` with `backface-visibility`, which every evergreen browser supports.
