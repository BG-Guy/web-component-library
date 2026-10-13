# Pricing Plans

Three-tier pricing with a billing switch. The thumb springs across, prices roll vertically to their new values like a counter, and "billed yearly" fades in. The featured plan is a dark card with an inner glow and a conic border that traces while you hover. No JavaScript: state comes from a radio group via `:has()`. Depends on `tokens/variables.css`.

**Motion:** spring thumb · vertical price roll with fade · plan lift on hover (spring) · conic border trace on the featured plan (hover only) · CTA shine.

## HTML

```html
<section class="pricing-pro" aria-labelledby="pricing-pro-title">
  <div class="pricing-pro__inner">
    <header class="pricing-pro__head">
      <p class="pricing-pro__eyebrow">Maintenance plans</p>
      <h2 id="pricing-pro-title" class="pricing-pro__title">Simple plans. No surprise bills.</h2>
      <p class="pricing-pro__lead">Priority scheduling, yearly checks and member pricing on every repair. Cancel any time.</p>
      <fieldset class="pricing-pro__toggle">
        <legend class="pricing-pro__sr">Billing period</legend>
        <span class="pricing-pro__thumb" aria-hidden="true"></span>
        <label class="pricing-pro__option"><input type="radio" name="pricing-pro-period" value="monthly" checked> Monthly</label>
        <label class="pricing-pro__option"><input type="radio" name="pricing-pro-period" value="yearly"> Yearly <span class="pricing-pro__save">−20%</span></label>
      </fieldset>
    </header>

    <ul class="pricing-pro__plans" role="list">
      <li class="pricing-pro__plan">
        <h3 class="pricing-pro__name">Essential</h3>
        <p class="pricing-pro__desc">A yearly check-up and member pricing for one home.</p>
        <p class="pricing-pro__price">
          <span class="pricing-pro__currency">$</span>
          <span class="pricing-pro__amount"><span class="pricing-pro__roll"><span class="pricing-pro__value pricing-pro__value--monthly">19</span><span class="pricing-pro__value pricing-pro__value--yearly">15</span></span></span>
          <span class="pricing-pro__per">per month<span class="pricing-pro__billed">, billed yearly</span></span>
        </p>
        <a class="pricing-pro__cta" href="#essential">Choose Essential</a>
        <ul class="pricing-pro__features" role="list">
          <li>Annual system inspection</li>
          <li>10% off all repairs</li>
          <li>Next-day scheduling</li>
        </ul>
      </li>

      <li class="pricing-pro__plan pricing-pro__plan--featured">
        <p class="pricing-pro__badge">Most popular</p>
        <h3 class="pricing-pro__name">Plus</h3>
        <p class="pricing-pro__desc">Twice-yearly service and same-day priority.</p>
        <p class="pricing-pro__price">
          <span class="pricing-pro__currency">$</span>
          <span class="pricing-pro__amount"><span class="pricing-pro__roll"><span class="pricing-pro__value pricing-pro__value--monthly">49</span><span class="pricing-pro__value pricing-pro__value--yearly">39</span></span></span>
          <span class="pricing-pro__per">per month<span class="pricing-pro__billed">, billed yearly</span></span>
        </p>
        <a class="pricing-pro__cta" href="#plus">Choose Plus</a>
        <p class="pricing-pro__includes">Everything in Essential, plus:</p>
        <ul class="pricing-pro__features" role="list">
          <li>Two inspections a year</li>
          <li>20% off all repairs</li>
          <li>Same-day priority line</li>
          <li>No callout fees, ever</li>
        </ul>
      </li>

      <li class="pricing-pro__plan">
        <h3 class="pricing-pro__name">Premium</h3>
        <p class="pricing-pro__desc">Full coverage for landlords and larger homes.</p>
        <p class="pricing-pro__price">
          <span class="pricing-pro__currency">$</span>
          <span class="pricing-pro__amount"><span class="pricing-pro__roll"><span class="pricing-pro__value pricing-pro__value--monthly">99</span><span class="pricing-pro__value pricing-pro__value--yearly">79</span></span></span>
          <span class="pricing-pro__per">per month<span class="pricing-pro__billed">, billed yearly</span></span>
        </p>
        <a class="pricing-pro__cta" href="#premium">Choose Premium</a>
        <p class="pricing-pro__includes">Everything in Plus, plus:</p>
        <ul class="pricing-pro__features" role="list">
          <li>Up to 3 properties</li>
          <li>Parts covered up to $500 a year</li>
          <li>Dedicated technician</li>
        </ul>
      </li>
    </ul>
    <p class="pricing-pro__note">Every plan includes our 5-year workmanship guarantee. Prices in USD, excluding parts unless stated.</p>
  </div>
</section>
```

## CSS

```css
@property --pricing-pro-angle { syntax: "<angle>"; inherits: false; initial-value: 0deg; }

/* Section and heading */
.pricing-pro { background: var(--surface-muted); color: var(--text-main); font-family: var(--font-sans); }
.pricing-pro__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.pricing-pro__head { max-width: 40rem; margin: 0 auto 3.5rem; text-align: center; }
.pricing-pro__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.pricing-pro__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.pricing-pro__lead { margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.pricing-pro__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Billing switch: equal halves, a thumb that springs between them */
.pricing-pro__toggle {
  position: relative; display: inline-grid; grid-template-columns: 1fr 1fr; min-inline-size: 0;
  margin: 2.25rem 0 0; padding: 0.25rem; border: 0; border-radius: 999px;
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
}
.pricing-pro__thumb {
  position: absolute; top: 0.25rem; bottom: 0.25rem; left: 0.25rem; width: calc(50% - 0.25rem);
  border-radius: 999px; background: var(--text-main); box-shadow: var(--highlight-inverse), 0 6px 16px -8px color-mix(in srgb, var(--text-main) 80%, transparent);
  transition: transform var(--dur-4) var(--ease-spring);
}
.pricing-pro__option {
  position: relative; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
  height: 2.5rem; padding: 0 1.25rem; border-radius: 999px; cursor: pointer; white-space: nowrap;
  color: var(--text-muted); font-size: 0.9375rem; font-weight: 600; transition: color var(--dur-3);
}
.pricing-pro__option input { position: absolute; opacity: 0; pointer-events: none; }
.pricing-pro__option:has(:checked) { color: var(--surface-light); }
.pricing-pro__option:has(:focus-visible) { box-shadow: var(--focus-ring); }
.pricing-pro__save { padding: 0.125rem 0.4375rem; border-radius: 999px; background: color-mix(in srgb, var(--success) 14%, transparent); color: var(--success); font-size: 0.75rem; transition: background-color var(--dur-3), color var(--dur-3); }
.pricing-pro__option:has(:checked) .pricing-pro__save { background: var(--success); color: var(--surface-light); }

/* Plans */
.pricing-pro__plans { display: grid; gap: 1.25rem; align-items: start; margin: 0; padding: 0; list-style: none; }
@media (min-width: 960px) { .pricing-pro__plans { grid-template-columns: repeat(3, minmax(0, 1fr)); align-items: stretch; } }
.pricing-pro__plan {
  position: relative; isolation: isolate; display: flex; flex-direction: column;
  padding: 2rem; border-radius: var(--radius-2xl);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  transition: transform var(--dur-4) var(--ease-spring), box-shadow var(--dur-4) var(--ease-out);
}
.pricing-pro__plan:hover { transform: translateY(-6px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl); }

/* Featured: dark, inner glow, conic border that traces while hovered */
.pricing-pro__plan--featured {
  border: 1.5px solid transparent; color: var(--text-inverse);
  background:
    linear-gradient(var(--surface-deep), var(--surface-deep)) padding-box,
    conic-gradient(from var(--pricing-pro-angle), var(--border-inverse) 0 25%, var(--primary-2) 45%, var(--primary) 55%, var(--border-inverse) 75%) border-box;
  box-shadow: 0 30px 60px -24px color-mix(in srgb, var(--primary) 60%, transparent);
  animation: pricing-pro-trace 4s linear infinite paused;
}
.pricing-pro__plan--featured:is(:hover, :focus-within) { animation-play-state: running; box-shadow: 0 36px 72px -24px color-mix(in srgb, var(--primary) 75%, transparent); }
.pricing-pro__plan--featured::before {
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none;
  background: radial-gradient(90% 55% at 50% 0%, color-mix(in srgb, var(--primary) 32%, transparent), transparent 70%);
}
.pricing-pro__badge {
  position: absolute; top: 0; left: 50%; margin: 0; padding: 0.3125rem 0.75rem; border-radius: 999px; transform: translate(-50%, -50%);
  background: var(--primary); color: var(--text-inverse); font-size: 0.75rem; font-weight: 600; white-space: nowrap;
  box-shadow: 0 8px 20px -6px color-mix(in srgb, var(--primary) 80%, transparent);
}

.pricing-pro__name { margin: 0; font: 600 1.25rem/1.2 var(--font-display); letter-spacing: -0.02em; }
.pricing-pro__desc { margin: 0.5rem 0 0; color: var(--text-muted); font-size: 0.9375rem; line-height: 1.5; }
.pricing-pro__plan--featured .pricing-pro__desc { color: var(--text-inverse-muted); }

/* Price: values stacked in a 1em window; the stack rolls to the active period */
.pricing-pro__price { display: flex; align-items: flex-start; gap: 0.125rem; margin: 1.75rem 0 0; }
.pricing-pro__currency { margin-top: 0.375rem; color: var(--text-muted); font: 600 1.375rem/1 var(--font-display); }
.pricing-pro__plan--featured .pricing-pro__currency { color: var(--text-inverse-muted); }
.pricing-pro__amount { display: block; height: 1em; overflow: hidden; font: 600 3.75rem/1 var(--font-display); letter-spacing: var(--tracking-display); font-variant-numeric: tabular-nums; }
.pricing-pro__roll { display: flex; flex-direction: column; transition: transform var(--dur-4) var(--ease-spring); }
.pricing-pro__value { display: block; height: 1em; transition: opacity var(--dur-3), filter var(--dur-3), visibility 0s linear var(--dur-4); }
.pricing-pro__per { align-self: flex-end; margin: 0 0 0.375rem 0.5rem; color: var(--text-muted); font-size: 0.875rem; }
.pricing-pro__plan--featured .pricing-pro__per { color: var(--text-inverse-muted); }
.pricing-pro__billed { opacity: 0; transition: opacity var(--dur-3); }

/* Period state */
.pricing-pro__value--yearly { opacity: 0; filter: blur(4px); visibility: hidden; }
.pricing-pro:has([value="yearly"]:checked) .pricing-pro__thumb { transform: translateX(100%); }
.pricing-pro:has([value="yearly"]:checked) .pricing-pro__roll { transform: translateY(-1em); }
.pricing-pro:has([value="yearly"]:checked) .pricing-pro__value--monthly { opacity: 0; filter: blur(4px); visibility: hidden; }
.pricing-pro:has([value="yearly"]:checked) .pricing-pro__value--yearly { opacity: 1; filter: none; visibility: visible; transition-delay: 0s; }
.pricing-pro:has([value="monthly"]:checked) .pricing-pro__value--monthly { transition-delay: 0s; }
.pricing-pro:has([value="yearly"]:checked) .pricing-pro__billed { opacity: 1; }

/* CTA: outline pill; the featured plan gets a light pill with a shine */
.pricing-pro__cta {
  position: relative; overflow: hidden; display: flex; align-items: center; justify-content: center;
  height: 3rem; margin-top: 1.75rem; border-radius: 999px;
  color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-subtle);
  transition: background-color var(--dur-2), box-shadow var(--dur-3), transform var(--dur-3) var(--ease-spring);
}
.pricing-pro__cta:hover { background: color-mix(in srgb, var(--text-main) 5%, transparent); box-shadow: inset 0 0 0 1px var(--text-muted); }
.pricing-pro__cta:active { transform: scale(0.97); }
.pricing-pro__cta:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }
.pricing-pro__plan--featured .pricing-pro__cta { background: var(--surface-light); box-shadow: 0 12px 30px -12px color-mix(in srgb, var(--primary-2) 90%, transparent); }
.pricing-pro__plan--featured .pricing-pro__cta:focus-visible { outline-color: var(--text-inverse); }
.pricing-pro__plan--featured .pricing-pro__cta::after {
  content: ""; position: absolute; inset: 0;
  background: linear-gradient(110deg, transparent 35%, color-mix(in srgb, var(--primary) 18%, transparent) 50%, transparent 65%);
  transform: translateX(-110%); transition: transform var(--dur-5) var(--ease-out);
}
.pricing-pro__plan--featured .pricing-pro__cta:hover::after { transform: translateX(110%); }

/* Feature list with drawn checks */
.pricing-pro__includes { margin: 1.75rem 0 0; font-size: 0.8125rem; font-weight: 600; }
.pricing-pro__features { display: grid; gap: 0.75rem; margin: 1.25rem 0 0; padding: 1.25rem 0 0; border-top: 1px solid var(--border-subtle); list-style: none; font-size: 0.9375rem; }
.pricing-pro__includes + .pricing-pro__features { margin-top: 0.75rem; }
.pricing-pro__plan--featured .pricing-pro__features { border-top-color: var(--border-inverse); }
.pricing-pro__features li { position: relative; padding-left: 1.875rem; line-height: 1.45; }
.pricing-pro__features li::before { content: ""; position: absolute; left: 0; top: 0.0625rem; width: 1.25rem; height: 1.25rem; border-radius: 50%; background: color-mix(in srgb, var(--primary) 12%, transparent); }
.pricing-pro__features li::after { content: ""; position: absolute; left: 0.4375rem; top: 0.3125rem; width: 0.3125rem; height: 0.5625rem; border: solid var(--primary); border-width: 0 2px 2px 0; transform: rotate(45deg); }
.pricing-pro__plan--featured .pricing-pro__features li::before { background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); }
.pricing-pro__plan--featured .pricing-pro__features li::after { border-color: var(--primary-2); }
.pricing-pro__note { margin: 2.5rem 0 0; text-align: center; color: var(--text-muted); font-size: 0.875rem; }

@media (prefers-reduced-motion: reduce) { .pricing-pro__plan--featured { animation: none; } }
@keyframes pricing-pro-trace { to { --pricing-pro-angle: 360deg; } }
```

## Notes

- Billing is a real radio group in a `fieldset` with a hidden `legend`. Arrow keys switch periods, and the focus ring shows on the visible option.
- The inactive price is `visibility: hidden` once the roll finishes, so screen readers read only the current price (e.g. "$ 39 per month, billed yearly").
- Keep both prices the same digit count (19/15, 49/39, 99/79) so the roll never changes width.
- Without `:has()` support (very old browsers) the switch still changes the radio but prices stay monthly. Add a 3-line script that toggles a class if you need to support them.
- On the featured plan, `--primary-2` checks sit on `--surface-deep` (5:1), and all body text is `--text-inverse` / `--text-inverse-muted`.
