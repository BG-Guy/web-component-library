# Stacking Cards

"Why homeowners choose us" as a deck of four large cards. Each card is `position: sticky` with a stepped `top`, so as you scroll they pile up and leave a peeking edge per card. As the next card slides over, the one beneath recedes, shrinking from its top edge and dimming under a deep overlay, so the layered edges read like a real stack. Each card pairs copy and a checklist with a CSS-built illustration: a live ETA map, a warranty seal, a price-locked receipt and a review cluster. On phones the illustration sits above the text and the offsets tighten. Depends on `tokens/variables.css`.

**Motion:** sticky stacking (pure CSS) · covered cards scale down from the top edge (−4% per card above) and dim (up to 40%), both scrubbed by scroll through a per-card `--stack-cards-depth`.

## HTML

```html
<div class="stack-cards-demo">
  <div class="stack-cards-demo__note">
    <p>Four promises that stack into a deck as you scroll.</p>
    <span class="stack-cards-demo__hint">Scroll <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg></span>
  </div>

  <section class="stack-cards" aria-labelledby="stack-cards-title" data-stack-cards>
    <div class="stack-cards__inner">
      <header class="stack-cards__head">
        <p class="stack-cards__eyebrow">Why Brand</p>
        <h2 id="stack-cards-title" class="stack-cards__title">Why homeowners choose us</h2>
        <p class="stack-cards__lead">Four promises we put in writing on every job in Springfield, from the first call to the final walkthrough.</p>
      </header>

      <ol class="stack-cards__list" role="list">
        <li class="stack-cards__item" style="--stack-cards-i: 0">
          <div class="stack-cards__card stack-cards__card--primary">
            <div class="stack-cards__text">
              <span class="stack-cards__num" aria-hidden="true">01</span>
              <h3 class="stack-cards__name">On time, or the call-out is free</h3>
              <p class="stack-cards__copy">You get a two-hour arrival window and live tracking by text. If we're late, the call-out fee comes off automatically.</p>
              <ul class="stack-cards__checks" role="list">
                <li>Two-hour arrival windows</li>
                <li>Live ETA from the van</li>
                <li>Late? Call-out fee waived</li>
              </ul>
            </div>
            <div class="stack-cards__art stack-cards__art--eta" aria-hidden="true">
              <div class="stack-cards__map">
                <svg class="stack-cards__route" viewBox="0 0 240 120" focusable="false">
                  <path d="M20 96C70 96 80 40 130 46S190 84 214 30" />
                  <path d="M20 96C70 96 80 40 130 46S190 84 214 30" pathLength="1" />
                </svg>
                <span class="stack-cards__start"></span>
                <span class="stack-cards__van"><svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M2 7h12v9H2zM14 10h4.5L21 13v3h-7" /><circle cx="6.5" cy="17.5" r="1.8" /><circle cx="17" cy="17.5" r="1.8" /></svg></span>
                <span class="stack-cards__home"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z" /></svg></span>
                <span class="stack-cards__eta"><strong>12 min</strong><small>Sam · on the way</small></span>
              </div>
            </div>
          </div>
        </li>

        <li class="stack-cards__item" style="--stack-cards-i: 1">
          <div class="stack-cards__card stack-cards__card--secondary">
            <div class="stack-cards__text">
              <span class="stack-cards__num" aria-hidden="true">02</span>
              <h3 class="stack-cards__name">Every job guaranteed for five years</h3>
              <p class="stack-cards__copy">Repairs and installs are covered in writing, parts and labour. If something we fixed fails, we come back and make it right.</p>
              <ul class="stack-cards__checks" role="list">
                <li>Five-year written warranty</li>
                <li>Parts and labour included</li>
                <li>Transfers if you sell</li>
              </ul>
            </div>
            <div class="stack-cards__art stack-cards__art--seal" aria-hidden="true">
              <span class="stack-cards__glint"></span>
              <span class="stack-cards__seal">
                <span class="stack-cards__ribbon"></span>
                <span class="stack-cards__burst"></span>
                <span class="stack-cards__core"><b>5</b><small>Year<br>warranty</small></span>
              </span>
              <span class="stack-cards__glint"></span>
            </div>
          </div>
        </li>

        <li class="stack-cards__item" style="--stack-cards-i: 2">
          <div class="stack-cards__card stack-cards__card--accent">
            <div class="stack-cards__text">
              <span class="stack-cards__num" aria-hidden="true">03</span>
              <h3 class="stack-cards__name">The price we quote is the price you pay</h3>
              <p class="stack-cards__copy">You approve a fixed, itemised price before any work starts. No hourly meter, no surprise extras on the invoice.</p>
              <ul class="stack-cards__checks" role="list">
                <li>Fixed, itemised quotes</li>
                <li>Approved before we start</li>
                <li>No fuel or overtime surcharges</li>
              </ul>
            </div>
            <div class="stack-cards__art stack-cards__art--receipt" aria-hidden="true">
              <div class="stack-cards__paper">
                <div class="stack-cards__receipt">
                  <p class="stack-cards__receipt-head"><strong>Quote #2048</strong><span>Leak repair</span></p>
                  <p class="stack-cards__line"><span>Labour</span><span>$120.00</span></p>
                  <p class="stack-cards__line"><span>Parts</span><span>$29.00</span></p>
                  <p class="stack-cards__line stack-cards__line--total"><span>Total</span><span>$149.00</span></p>
                </div>
                <span class="stack-cards__lock"><svg viewBox="0 0 24 24" width="14" height="14" focusable="false"><path d="M6 11h12v9H6zM8.5 11V8a3.5 3.5 0 0 1 7 0v3" /></svg>Price locked</span>
              </div>
            </div>
          </div>
        </li>

        <li class="stack-cards__item" style="--stack-cards-i: 3">
          <div class="stack-cards__card stack-cards__card--deep">
            <div class="stack-cards__text">
              <span class="stack-cards__num" aria-hidden="true">04</span>
              <h3 class="stack-cards__name">Rated 4.9 by 1,200+ neighbours</h3>
              <p class="stack-cards__copy">Every review is verified and published unedited, and every technician is rated after every single visit.</p>
              <ul class="stack-cards__checks" role="list">
                <li>Verified reviews only</li>
                <li>Rated after every visit</li>
                <li>Issues answered within a day</li>
              </ul>
            </div>
            <div class="stack-cards__art stack-cards__art--reviews" aria-hidden="true">
              <div class="stack-cards__score"><strong>4.9</strong><span class="stack-cards__stars"></span><small>1,200+ reviews</small></div>
              <p class="stack-cards__bubble"><b>JM</b><span>Spotless work.</span></p>
              <p class="stack-cards__bubble"><b>AK</b><span>Fixed on the first visit.</span></p>
              <p class="stack-cards__bubble"><b>RS</b><span>No surprises.</span></p>
            </div>
          </div>
        </li>
      </ol>

      <p class="stack-cards__foot">Questions first? Call <a href="tel:+15555550123">(555) 555-0123</a> or email <a href="mailto:hello@example.com">hello@example.com</a>.</p>
    </div>
  </section>

  <div class="stack-cards-demo__note">
    <p>The finished deck scrolls away together.</p>
  </div>
</div>
```

## CSS

```css
/* Section: light page with a soft wash of brand light */
.stack-cards {
  --stack-cards-top: clamp(1rem, 5vh, 3rem);
  --stack-cards-step: 0.75rem;
  --stack-cards-seal: 6.25rem;
  --stack-cards-receipt: 9.5rem;
  position: relative; isolation: isolate; overflow-x: clip;
  background: radial-gradient(70% 32rem at 50% 0%, color-mix(in srgb, var(--primary) 7%, transparent), transparent 70%), var(--surface-light);
  color: var(--text-main); font-family: var(--font-sans);
}
.stack-cards :where(h2, h3, p, ul, ol) { margin: 0; }
.stack-cards__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.stack-cards__head { display: grid; justify-items: center; gap: 1rem; max-width: 40rem; margin: 0 auto clamp(2.5rem, 6vw, 4rem); text-align: center; }
.stack-cards__eyebrow { color: var(--primary); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.stack-cards__title { font: 600 clamp(2rem, 1.2rem + 3vw, 3.5rem)/1.02 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.stack-cards__lead { max-width: 32rem; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Deck: items are the sticky elements, the list is their runway */
.stack-cards__list { position: relative; display: grid; gap: var(--space-xl); padding: 0; list-style: none; }
.stack-cards__item { position: relative; }

/* Card: tint per modifier; --stack-cards-depth (JS) recedes it from the top edge */
.stack-cards__card {
  --stack-cards-tone: var(--primary);
  --stack-cards-ink: var(--text-main);
  --stack-cards-muted: color-mix(in srgb, var(--text-main) 80%, var(--surface-light));
  --stack-cards-line: color-mix(in srgb, var(--stack-cards-tone) 22%, var(--border-subtle));
  position: relative; isolation: isolate; display: grid; gap: 1.25rem; overflow: hidden;
  padding: clamp(1.25rem, 3.5vw, 3rem); border-radius: var(--radius-2xl);
  background: var(--stack-cards-bg); color: var(--stack-cards-ink);
  box-shadow:
    inset 0 0 0 1px var(--stack-cards-line), var(--highlight),
    0 -18px 40px -28px color-mix(in srgb, var(--surface-deep) 45%, transparent), var(--shadow-xl);
  transform-origin: 50% 0; transform: scale(calc(1 - var(--stack-cards-depth, 0) * 0.04));
}
.stack-cards__card::after {
  content: ""; position: absolute; inset: 0; z-index: 3; border-radius: inherit; pointer-events: none;
  background: var(--surface-deep); opacity: min(0.4, calc(var(--stack-cards-depth, 0) * 0.14));
}
.stack-cards__card--primary {
  --stack-cards-tone: var(--primary);
  --stack-cards-bg: radial-gradient(70% 80% at 100% 0%, color-mix(in srgb, var(--primary) 18%, transparent), transparent 70%), linear-gradient(160deg, color-mix(in srgb, var(--primary) 9%, var(--surface-light)), var(--surface-light) 75%);
}
.stack-cards__card--secondary {
  --stack-cards-tone: var(--primary-2);
  --stack-cards-bg: radial-gradient(70% 80% at 100% 0%, color-mix(in srgb, var(--primary-2) 18%, transparent), transparent 70%), linear-gradient(160deg, color-mix(in srgb, var(--primary-2) 10%, var(--surface-light)), var(--surface-light) 75%);
}
.stack-cards__card--accent {
  --stack-cards-tone: var(--warning);
  --stack-cards-bg: radial-gradient(70% 80% at 100% 0%, color-mix(in srgb, var(--accent) 24%, transparent), transparent 70%), linear-gradient(160deg, color-mix(in srgb, var(--accent) 12%, var(--surface-light)), var(--surface-light) 75%);
}
.stack-cards__card--deep {
  --stack-cards-tone: color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse));
  --stack-cards-ink: var(--text-inverse);
  --stack-cards-muted: var(--text-inverse-muted);
  --stack-cards-line: var(--border-inverse);
  --stack-cards-bg: radial-gradient(70% 80% at 100% 0%, color-mix(in srgb, var(--primary) 35%, transparent), transparent 70%), radial-gradient(60% 70% at 0% 100%, color-mix(in srgb, var(--primary-2) 22%, transparent), transparent 70%), var(--surface-deep);
  box-shadow: inset 0 0 0 1px var(--stack-cards-line), var(--highlight-inverse), 0 -18px 40px -28px color-mix(in srgb, var(--surface-deep) 60%, transparent), var(--shadow-xl);
}

/* Text column */
.stack-cards__text { display: grid; gap: 0.875rem; align-content: start; }
.stack-cards__num {
  justify-self: start; font: 500 clamp(2.25rem, 1.6rem + 2.6vw, 4.25rem)/0.9 var(--font-mono); letter-spacing: -0.06em;
  background: linear-gradient(180deg, var(--stack-cards-tone), color-mix(in srgb, var(--stack-cards-tone) 25%, transparent));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.stack-cards__name { font: 600 clamp(1.5rem, 1.1rem + 1.6vw, 2.5rem)/1.08 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.stack-cards__copy { max-width: 34rem; color: var(--stack-cards-muted); font-size: clamp(0.9375rem, 0.9rem + 0.2vw, 1.0625rem); line-height: 1.6; }
.stack-cards__checks { display: grid; gap: 0.5rem; margin-top: 0.25rem; padding: 0; list-style: none; }
.stack-cards__checks li { position: relative; padding-left: 1.75rem; font-size: 0.9375rem; font-weight: 500; }
.stack-cards__checks li::before { content: ""; position: absolute; left: 0; top: 0.125rem; width: 1.125rem; height: 1.125rem; border-radius: 50%; background: color-mix(in srgb, var(--stack-cards-tone) 16%, transparent); }
.stack-cards__checks li::after { content: ""; position: absolute; left: 0.4375rem; top: 0.3125rem; width: 0.25rem; height: 0.5rem; border: solid var(--stack-cards-tone); border-width: 0 2px 2px 0; transform: rotate(45deg); }

/* Illustration tray (above the text on phones) */
.stack-cards__art {
  position: relative; order: -1; height: 8.5rem; overflow: hidden; border-radius: var(--radius-xl);
  background: color-mix(in srgb, var(--surface-light) 55%, transparent);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--stack-cards-tone) 16%, transparent), var(--highlight);
}
.stack-cards__art svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }

/* 1 · Live ETA map */
.stack-cards__art--eta {
  background-image:
    linear-gradient(color-mix(in srgb, var(--primary) 7%, transparent) 1px, transparent 1px),
    linear-gradient(90deg, color-mix(in srgb, var(--primary) 7%, transparent) 1px, transparent 1px);
  background-size: 1.25rem 1.25rem;
}
.stack-cards__map { position: absolute; left: 50%; top: 50%; width: min(92%, 15rem); aspect-ratio: 2 / 1; translate: -50% -50%; }
.stack-cards__route { position: absolute; inset: 0; width: 100%; height: 100%; overflow: visible; }
.stack-cards__route path { stroke-width: 2.5; }
.stack-cards__route path:first-child { stroke: color-mix(in srgb, var(--primary) 30%, transparent); stroke-dasharray: 1 8; }
.stack-cards__route path:last-child { stroke: var(--primary); stroke-dasharray: 0.57 1; }
.stack-cards__start, .stack-cards__van, .stack-cards__home { position: absolute; translate: -50% -50%; display: grid; place-items: center; border-radius: 50%; }
.stack-cards__start { left: 8.3%; top: 80%; width: 0.75rem; height: 0.75rem; background: var(--primary); box-shadow: 0 0 0 3px var(--surface-light); }
.stack-cards__van {
  left: 54.2%; top: 38.3%; width: 2.25rem; height: 2.25rem; background: var(--primary); color: var(--text-inverse);
  box-shadow: 0 0 0 6px color-mix(in srgb, var(--primary) 16%, transparent), 0 8px 20px -6px var(--primary);
}
.stack-cards__home { left: 89.2%; top: 25%; width: 2rem; height: 2rem; background: var(--surface-light); color: var(--primary); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-md); }
.stack-cards__eta {
  position: absolute; left: 0; top: 0; display: grid; gap: 0.125rem; padding: 0.375rem 0.625rem; border-radius: var(--radius-md);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-lg);
}
.stack-cards__eta strong { font: 600 0.875rem/1 var(--font-display); }
.stack-cards__eta small { color: var(--text-muted); font-size: 0.6875rem; }

/* 2 · Warranty seal */
.stack-cards__art--seal { display: grid; place-items: center; }
.stack-cards__seal { position: relative; isolation: isolate; width: var(--stack-cards-seal); aspect-ratio: 1; margin-top: -0.75rem; }
.stack-cards__burst {
  position: absolute; inset: 0;
  clip-path: polygon(50% 0%, 55.9% 4.9%, 62.9% 1.7%, 67.4% 8%, 75% 6.7%, 77.7% 13.9%, 85.4% 14.6%, 86.1% 22.3%, 93.3% 25%, 92% 32.6%, 98.3% 37.1%, 95.1% 44.1%, 100% 50%, 95.1% 55.9%, 98.3% 62.9%, 92% 67.4%, 93.3% 75%, 86.1% 77.7%, 85.4% 85.4%, 77.7% 86.1%, 75% 93.3%, 67.4% 92%, 62.9% 98.3%, 55.9% 95.1%, 50% 100%, 44.1% 95.1%, 37.1% 98.3%, 32.6% 92%, 25% 93.3%, 22.3% 86.1%, 14.6% 85.4%, 13.9% 77.7%, 6.7% 75%, 8% 67.4%, 1.7% 62.9%, 4.9% 55.9%, 0% 50%, 4.9% 44.1%, 1.7% 37.1%, 8% 32.6%, 6.7% 25%, 13.9% 22.3%, 14.6% 14.6%, 22.3% 13.9%, 25% 6.7%, 32.6% 8%, 37.1% 1.7%, 44.1% 4.9%);
  background:
    radial-gradient(circle at 32% 26%, color-mix(in srgb, var(--surface-light) 35%, transparent), transparent 55%),
    linear-gradient(145deg, color-mix(in srgb, var(--primary-2) 80%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
}
.stack-cards__core {
  position: absolute; inset: 13%; display: grid; place-content: center; justify-items: center; border-radius: 50%; text-align: center;
  border: 1.5px dashed color-mix(in srgb, var(--surface-light) 55%, transparent);
  background: color-mix(in srgb, var(--primary-2) 75%, var(--surface-deep)); color: var(--text-inverse);
  box-shadow: inset 0 2px 8px color-mix(in srgb, var(--surface-deep) 35%, transparent);
}
.stack-cards__core b { font: 600 calc(var(--stack-cards-seal) * 0.34)/0.85 var(--font-display); letter-spacing: var(--tracking-tight); }
.stack-cards__core small { font: 600 max(0.5rem, calc(var(--stack-cards-seal) * 0.068))/1.25 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.stack-cards__ribbon { position: absolute; z-index: -1; left: 50%; top: 62%; width: 26%; height: 52%; translate: -50% 0; }
.stack-cards__ribbon::before, .stack-cards__ribbon::after {
  content: ""; position: absolute; top: 0; width: 100%; height: 100%; transform-origin: 50% 0;
  background: linear-gradient(180deg, color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)), color-mix(in srgb, var(--primary-2) 50%, var(--surface-deep)));
  clip-path: polygon(0 0, 100% 0, 100% 100%, 50% 80%, 0 100%);
}
.stack-cards__ribbon::before { left: -31%; transform: rotate(20deg); }
.stack-cards__ribbon::after { left: 31%; transform: rotate(-20deg); }
.stack-cards__glint { position: absolute; width: 0.625rem; height: 0.625rem; rotate: 45deg; border-radius: 2px; background: linear-gradient(135deg, var(--primary-2), color-mix(in srgb, var(--primary-2) 20%, transparent)); }
.stack-cards__glint:first-child { left: 22%; top: 24%; }
.stack-cards__glint:last-child { right: 20%; bottom: 26%; width: 0.4375rem; height: 0.4375rem; }

/* 3 · Price-locked receipt */
.stack-cards__art--receipt {
  display: grid; place-items: center;
  background-image: radial-gradient(color-mix(in srgb, var(--warning) 16%, transparent) 1px, transparent 1.5px); background-size: 0.875rem 0.875rem;
}
.stack-cards__paper { position: relative; rotate: -3deg; filter: drop-shadow(0 14px 16px color-mix(in srgb, var(--surface-deep) 18%, transparent)); }
.stack-cards__receipt {
  display: grid; gap: 0.3125rem; width: var(--stack-cards-receipt); padding: 0.625rem 0.75rem 1rem; border-radius: var(--radius-md) var(--radius-md) 0 0;
  background: var(--surface-light); color: var(--text-main); font: 500 0.625rem/1.3 var(--font-mono);
  -webkit-mask: linear-gradient(black 0 0) top / 100% calc(100% - 7px) no-repeat, conic-gradient(from -45deg at 50% 100%, black 90deg, transparent 0) bottom / 10px 7px repeat-x;
  mask: linear-gradient(black 0 0) top / 100% calc(100% - 7px) no-repeat, conic-gradient(from -45deg at 50% 100%, black 90deg, transparent 0) bottom / 10px 7px repeat-x;
}
.stack-cards__receipt p { display: flex; justify-content: space-between; gap: 0.5rem; }
.stack-cards__receipt-head { padding-bottom: 0.3125rem; border-bottom: 1px solid var(--border-subtle); }
.stack-cards__receipt-head span, .stack-cards__line span:first-child { color: var(--text-muted); }
.stack-cards__line--total { padding-top: 0.3125rem; border-top: 1px dashed var(--border-subtle); font-weight: 700; }
.stack-cards__line--total span:first-child { color: var(--text-main); }
.stack-cards__lock {
  position: absolute; right: -1.5rem; top: -0.875rem; display: inline-flex; align-items: center; gap: 0.3125rem; padding: 0.3125rem 0.625rem 0.3125rem 0.5rem;
  border-radius: var(--radius-full); rotate: 9deg; white-space: nowrap;
  background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 70%, var(--warning))); color: var(--text-main);
  font: 600 0.6875rem/1 var(--font-sans); box-shadow: var(--highlight), 0 8px 18px -8px var(--warning);
}

/* 4 · Review cluster on the deep card */
.stack-cards__art--reviews {
  background: radial-gradient(60% 80% at 20% 50%, color-mix(in srgb, var(--primary) 22%, transparent), transparent 70%), var(--glass-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.stack-cards__score { position: absolute; left: 6%; top: 50%; translate: 0 -50%; display: grid; gap: 0.375rem; }
.stack-cards__score strong { font: 600 clamp(2.25rem, 1.8rem + 2vw, 4rem)/0.9 var(--font-display); letter-spacing: var(--tracking-tight); }
.stack-cards__score small { color: var(--text-inverse-muted); font: 500 0.6875rem var(--font-mono); }
.stack-cards__stars {
  position: relative; display: block; width: 5.5em; height: 1.1em; font-size: 0.875rem; background: var(--border-inverse);
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='m12 2.5 2.9 6 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.2 1.3-6.6-4.9-4.6 6.6-.8z' fill='black'/%3E%3C/svg%3E") 0 0 / 1.1em 1.1em repeat-x;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='m12 2.5 2.9 6 6.6.8-4.9 4.6 1.3 6.6L12 17.3l-5.9 3.2 1.3-6.6-4.9-4.6 6.6-.8z' fill='black'/%3E%3C/svg%3E") 0 0 / 1.1em 1.1em repeat-x;
}
.stack-cards__stars::before { content: ""; position: absolute; inset: 0; width: 98%; background: var(--accent); }
.stack-cards__bubble {
  position: absolute; right: 5%; display: flex; align-items: center; gap: 0.5rem; padding: 0.3125rem 0.75rem 0.3125rem 0.3125rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 55%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), var(--shadow-lg);
  color: var(--text-inverse); font-size: 0.6875rem; white-space: nowrap;
}
.stack-cards__bubble b { display: grid; place-items: center; width: 1.5rem; height: 1.5rem; border-radius: 50%; background: var(--gradient-brand); font-size: 0.5625rem; }
.stack-cards__bubble:nth-of-type(1) { top: 12%; rotate: 2deg; }
.stack-cards__bubble:nth-of-type(2) { display: none; }
.stack-cards__bubble:nth-of-type(3) { bottom: 14%; right: 12%; rotate: -2deg; }
.stack-cards__bubble:nth-of-type(3) b { background: linear-gradient(135deg, var(--accent), var(--primary-2)); color: var(--text-main); }

/* Footer line */
.stack-cards__foot { margin-top: clamp(2rem, 5vw, 3rem); color: var(--text-muted); text-align: center; }
.stack-cards__foot a { display: inline-block; padding-block: 0.125rem; color: var(--primary); font-weight: 600; text-underline-offset: 3px; }
.stack-cards__foot a:focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; border-radius: var(--radius-sm); }

@media (min-width: 768px) {
  .stack-cards { --stack-cards-step: 1.25rem; --stack-cards-seal: 10.5rem; --stack-cards-receipt: 13rem; }
  .stack-cards__card { grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr); gap: clamp(2rem, 4vw, 4rem); align-items: center; min-height: 24rem; }
  .stack-cards__art { order: 0; align-self: stretch; height: auto; min-height: 19rem; }
  .stack-cards__map { width: min(90%, 28rem); }
  .stack-cards__eta { padding: 0.625rem 0.875rem; }
  .stack-cards__eta strong { font-size: 1.125rem; }
  .stack-cards__eta small { font-size: 0.75rem; }
  .stack-cards__receipt { gap: 0.5rem; padding: 1rem 1.125rem 1.5rem; font-size: 0.75rem; }
  .stack-cards__bubble { font-size: 0.8125rem; }
  .stack-cards__bubble:nth-of-type(1) { top: 16%; }
  .stack-cards__bubble:nth-of-type(2) { display: flex; top: 50%; right: 18%; translate: 0 -50%; }
  .stack-cards__bubble:nth-of-type(3) { bottom: 16%; right: 7%; }
}

/* Sticky stacking only when a card fits under its offset (JS double-checks and adds .stack-cards--flow) */
@media (min-height: 40rem), (min-width: 768px) and (min-height: 36rem) {
  .stack-cards__list { padding-bottom: clamp(2rem, 10vh, 6rem); }
  .stack-cards__item { position: sticky; top: calc(var(--stack-cards-top) + var(--stack-cards-i, 0) * var(--stack-cards-step)); }
}
.stack-cards--flow .stack-cards__item { position: relative; top: auto; }

/* Demo scroll room */
.stack-cards-demo { background: var(--surface-light); color: var(--text-muted); font-family: var(--font-sans); }
.stack-cards-demo__note { display: grid; place-content: center; justify-items: center; gap: 1rem; min-height: 70vh; padding: 2rem var(--gutter); text-align: center; }
.stack-cards-demo__note p { margin: 0; max-width: 30rem; font-size: 1.0625rem; line-height: 1.6; }
.stack-cards-demo__hint { display: inline-flex; align-items: center; gap: 0.5rem; color: var(--text-main); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.stack-cards-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const clamp = (v, min = 0, max = 1) => Math.min(max, Math.max(min, v));

document.querySelectorAll('[data-stack-cards]').forEach((root) => {
  const items = [...root.querySelectorAll('.stack-cards__item')];
  let near = false, frame = 0, tops = [];

  // Depth = how many cards (fractionally) now lie over this one; CSS turns it into scale + dim
  const render = () => {
    frame = 0;
    const rects = items.map((el) => el.getBoundingClientRect());
    let depth = 0;
    for (let i = items.length - 1; i >= 0; i--) {
      const next = rects[i + 1];
      const step = next ? tops[i + 1] - tops[i] : 0;
      depth += next ? clamp((rects[i].bottom - next.top) / Math.max(1, rects[i].height - step)) : 0;
      items[i].style.setProperty('--stack-cards-depth', reduce.matches ? 0 : depth.toFixed(3));
    }
  };
  const queue = () => { if (!frame) frame = requestAnimationFrame(render); };

  // Sticky offsets, plus a guard: if a card is taller than the room under its offset, let the deck flow
  const measure = () => {
    tops = items.map((el) => parseFloat(getComputedStyle(el).top) || 0);
    root.classList.toggle('stack-cards--flow', items.some((el, i) => el.offsetHeight > innerHeight - tops[i] - 8));
    render();
  };

  new IntersectionObserver((entries) => { near = entries.at(-1).isIntersecting; if (near) queue(); }, { rootMargin: '25% 0px' }).observe(root);
  addEventListener('scroll', () => { if (near) queue(); }, { passive: true });
  addEventListener('resize', measure, { passive: true });
  new ResizeObserver(measure).observe(root);
  reduce.addEventListener('change', queue);
  measure();
});
```

## Notes

- Structure: the cards are an ordered list, and each has an `<h3>`, copy and a real checklist. The big numbers and illustrations are decorative (`aria-hidden`). There's nothing focusable inside the cards, so a covering card never hides keyboard focus.
- Baseline without JS and under reduced motion: plain CSS sticky stacking with stepped `top` and no scaling or dimming. The distinct tints and top-edge sheens still show the layered edges. Sticky only switches on when there's height for it (≥ 640px, or ≥ 576px from 768px wide). JS also checks that every card fits below its offset and adds `.stack-cards--flow` otherwise, so no card content is ever stuck below the fold.
- Recede: each frame JS reads the item rects once and writes `--stack-cards-depth` on each item (the sum of how far every later card has slid over it). CSS turns that into `scale(1 − 0.04 × depth)` from the top edge and a deep overlay of up to 40%.
- Contrast: titles are `--text-main` on the tinted cards (≥ 11:1). Copy is `--text-main` mixed 80% with white, ≥ 5.7:1 even at the strongest tint, because `--text-muted` drops below 4.5:1 on tints. The deep card uses `--text-inverse` and `--text-inverse-muted` (≥ 5.4:1 at the brightest point of its glow). Check marks clear 3:1, using `--warning` on the amber card.
- Retheme each card with `--stack-cards-tone` and `--stack-cards-bg`, and add cards with `style="--stack-cards-i: n"`. If the page has a sticky header, add its height to `--stack-cards-top`.
