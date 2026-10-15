# Expanding Service Grid

A dark pricing grid of six service cards. "Details" opens a card in place: on desktop it grows across two columns (leftwards when it sits in the last column), its outline turns into a gradient, and its three price tiers, "What's included" checklist and booking button rise in. The other cards glide to their new places with a transform-only FLIP, and closing folds the card back into its summary first, so nothing pops. One card is open at a time; on phones it simply grows downwards in the single column. Depends on `tokens/variables.css`.

**Motion:** FLIP glide for the other cards (WAAPI, `--dur-4`, `--ease-out`) · the opening card grows via clip-path and translate in the same beat · fold-back before closing (`--dur-3`, `--ease-in-out`) · staggered detail rise (`--stagger`) · plus-to-cross toggle (`--ease-spring`).

## HTML

```html
<section class="svc-expand" aria-labelledby="svc-expand-title" data-svc-expand>
  <div class="svc-expand__inner">
    <header class="svc-expand__head">
      <p class="svc-expand__eyebrow">Plans &amp; pricing</p>
      <h2 id="svc-expand-title" class="svc-expand__title">Pick a service. <span class="svc-expand__glow">See every price.</span></h2>
      <p class="svc-expand__intro">Six trades, three clear tiers each. Open any card to see what's included. No call-out fees, and no surprises on the invoice.</p>
    </header>

    <ul class="svc-expand__grid" role="list">
      <li class="svc-expand__card">
        <div class="svc-expand__summary">
          <div class="svc-expand__top">
            <span class="svc-expand__num" aria-hidden="true">01</span>
            <span class="svc-expand__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M12 3s6 6.2 6 10.5a6 6 0 0 1-12 0C6 9.2 12 3 12 3zM9.5 14a2.5 2.5 0 0 0 2.5 2.5" /></svg></span>
          </div>
          <h3 class="svc-expand__name">Plumbing</h3>
          <p class="svc-expand__benefit">Leaks, clogs and water heaters, fixed on the first visit.</p>
          <div class="svc-expand__row">
            <p class="svc-expand__price"><small>from</small> $89</p>
            <div class="svc-expand__actions">
              <a class="svc-expand__quick" href="#book-plumbing">Book<span class="svc-expand__sr"> plumbing</span></a>
              <button class="svc-expand__toggle" type="button" hidden>Details<span class="svc-expand__sr"> for plumbing</span><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg></button>
            </div>
          </div>
        </div>
        <div class="svc-expand__details">
          <div class="svc-expand__details-head">
            <h4 class="svc-expand__detail-title">Plumbing plans</h4>
            <button class="svc-expand__close" type="button" aria-label="Close plumbing details" hidden><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
          </div>
          <ul class="svc-expand__tiers" role="list">
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Basic</span><span class="svc-expand__tier-price"><small>from</small> $89</span><span class="svc-expand__tier-note">One fixture, one visit</span></li>
            <li class="svc-expand__tier svc-expand__tier--pick"><span class="svc-expand__tier-name">Plus <em class="svc-expand__badge">Popular</em></span><span class="svc-expand__tier-price"><small>from</small> $149</span><span class="svc-expand__tier-note">Up to three fixtures and a drain check</span></li>
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Pro</span><span class="svc-expand__tier-price"><small>from</small> $249</span><span class="svc-expand__tier-note">Whole-home inspection, priority slot</span></li>
          </ul>
          <div class="svc-expand__more">
            <div>
              <p class="svc-expand__inc-title">What's included</p>
              <ul class="svc-expand__checks" role="list">
                <li>Fixed quote before any work</li>
                <li>Parts at trade price</li>
                <li>12-month workmanship guarantee</li>
                <li>Clean-up and job photos</li>
              </ul>
            </div>
            <a class="svc-expand__book" href="#book-plumbing">Book this service<span class="svc-expand__sr">: plumbing</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>

      <li class="svc-expand__card">
        <div class="svc-expand__summary">
          <div class="svc-expand__top">
            <span class="svc-expand__num" aria-hidden="true">02</span>
            <span class="svc-expand__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M13 2.5 5.5 13.5H11l-1 8 7.5-11H12l1-8z" /></svg></span>
          </div>
          <h3 class="svc-expand__name">Electrical</h3>
          <p class="svc-expand__benefit">Outlets, panels and lighting, by licensed electricians.</p>
          <div class="svc-expand__row">
            <p class="svc-expand__price"><small>from</small> $99</p>
            <div class="svc-expand__actions">
              <a class="svc-expand__quick" href="#book-electrical">Book<span class="svc-expand__sr"> electrical</span></a>
              <button class="svc-expand__toggle" type="button" hidden>Details<span class="svc-expand__sr"> for electrical</span><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg></button>
            </div>
          </div>
        </div>
        <div class="svc-expand__details">
          <div class="svc-expand__details-head">
            <h4 class="svc-expand__detail-title">Electrical plans</h4>
            <button class="svc-expand__close" type="button" aria-label="Close electrical details" hidden><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
          </div>
          <ul class="svc-expand__tiers" role="list">
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Basic</span><span class="svc-expand__tier-price"><small>from</small> $99</span><span class="svc-expand__tier-note">One outlet, switch or fixture</span></li>
            <li class="svc-expand__tier svc-expand__tier--pick"><span class="svc-expand__tier-name">Plus <em class="svc-expand__badge">Popular</em></span><span class="svc-expand__tier-price"><small>from</small> $179</span><span class="svc-expand__tier-note">Up to three points and a safety test</span></li>
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Pro</span><span class="svc-expand__tier-price"><small>from</small> $329</span><span class="svc-expand__tier-note">Panel check and surge protection</span></li>
          </ul>
          <div class="svc-expand__more">
            <div>
              <p class="svc-expand__inc-title">What's included</p>
              <ul class="svc-expand__checks" role="list">
                <li>Licensed master electrician</li>
                <li>Permits handled for you</li>
                <li>Safety test certificate</li>
                <li>12-month guarantee</li>
              </ul>
            </div>
            <a class="svc-expand__book" href="#book-electrical">Book this service<span class="svc-expand__sr">: electrical</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>

      <li class="svc-expand__card">
        <div class="svc-expand__summary">
          <div class="svc-expand__top">
            <span class="svc-expand__num" aria-hidden="true">03</span>
            <span class="svc-expand__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M10 13.5V5a2 2 0 1 1 4 0v8.5a4 4 0 1 1-4 0zM12 9.5v6M17.5 5h3M17.5 9h2" /></svg></span>
          </div>
          <h3 class="svc-expand__name">Heating &amp; cooling</h3>
          <p class="svc-expand__benefit">Furnace and AC tune-ups, repairs and new installs.</p>
          <div class="svc-expand__row">
            <p class="svc-expand__price"><small>from</small> $129</p>
            <div class="svc-expand__actions">
              <a class="svc-expand__quick" href="#book-hvac">Book<span class="svc-expand__sr"> heating and cooling</span></a>
              <button class="svc-expand__toggle" type="button" hidden>Details<span class="svc-expand__sr"> for heating and cooling</span><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg></button>
            </div>
          </div>
        </div>
        <div class="svc-expand__details">
          <div class="svc-expand__details-head">
            <h4 class="svc-expand__detail-title">Heating &amp; cooling plans</h4>
            <button class="svc-expand__close" type="button" aria-label="Close heating and cooling details" hidden><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
          </div>
          <ul class="svc-expand__tiers" role="list">
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Basic</span><span class="svc-expand__tier-price"><small>from</small> $129</span><span class="svc-expand__tier-note">Tune-up for one system</span></li>
            <li class="svc-expand__tier svc-expand__tier--pick"><span class="svc-expand__tier-name">Plus <em class="svc-expand__badge">Popular</em></span><span class="svc-expand__tier-price"><small>from</small> $219</span><span class="svc-expand__tier-note">Furnace and AC, filters included</span></li>
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Pro</span><span class="svc-expand__tier-price"><small>from</small> $389</span><span class="svc-expand__tier-note">Twice-yearly plan, priority repairs</span></li>
          </ul>
          <div class="svc-expand__more">
            <div>
              <p class="svc-expand__inc-title">What's included</p>
              <ul class="svc-expand__checks" role="list">
                <li>21-point system check</li>
                <li>Filters and refrigerant top-up</li>
                <li>Carbon-monoxide test</li>
                <li>No overtime rates</li>
              </ul>
            </div>
            <a class="svc-expand__book" href="#book-hvac">Book this service<span class="svc-expand__sr">: heating and cooling</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>

      <li class="svc-expand__card">
        <div class="svc-expand__summary">
          <div class="svc-expand__top">
            <span class="svc-expand__num" aria-hidden="true">04</span>
            <span class="svc-expand__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M3 11.5 12 4l9 7.5M5.5 9.5v11h13v-11M10 20.5v-5h4v5" /></svg></span>
          </div>
          <h3 class="svc-expand__name">Roofing</h3>
          <p class="svc-expand__benefit">Leak patches, storm damage and full re-roofs.</p>
          <div class="svc-expand__row">
            <p class="svc-expand__price"><small>from</small> $249</p>
            <div class="svc-expand__actions">
              <a class="svc-expand__quick" href="#book-roofing">Book<span class="svc-expand__sr"> roofing</span></a>
              <button class="svc-expand__toggle" type="button" hidden>Details<span class="svc-expand__sr"> for roofing</span><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg></button>
            </div>
          </div>
        </div>
        <div class="svc-expand__details">
          <div class="svc-expand__details-head">
            <h4 class="svc-expand__detail-title">Roofing plans</h4>
            <button class="svc-expand__close" type="button" aria-label="Close roofing details" hidden><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
          </div>
          <ul class="svc-expand__tiers" role="list">
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Basic</span><span class="svc-expand__tier-price"><small>from</small> $249</span><span class="svc-expand__tier-note">Find and patch one leak</span></li>
            <li class="svc-expand__tier svc-expand__tier--pick"><span class="svc-expand__tier-name">Plus <em class="svc-expand__badge">Popular</em></span><span class="svc-expand__tier-price"><small>from</small> $590</span><span class="svc-expand__tier-note">Up to 50 shingles replaced</span></li>
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Pro</span><span class="svc-expand__tier-price"><small>from</small> $1,450</span><span class="svc-expand__tier-note">Section re-roof and new flashing</span></li>
          </ul>
          <div class="svc-expand__more">
            <div>
              <p class="svc-expand__inc-title">What's included</p>
              <ul class="svc-expand__checks" role="list">
                <li>Drone roof inspection</li>
                <li>Colour-matched shingles</li>
                <li>Debris hauled away</li>
                <li>10-year leak warranty</li>
              </ul>
            </div>
            <a class="svc-expand__book" href="#book-roofing">Book this service<span class="svc-expand__sr">: roofing</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>

      <li class="svc-expand__card">
        <div class="svc-expand__summary">
          <div class="svc-expand__top">
            <span class="svc-expand__num" aria-hidden="true">05</span>
            <span class="svc-expand__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><rect x="4" y="2.5" width="16" height="19" rx="2.5" /><circle cx="12" cy="13.5" r="4.5" /><path d="M7.5 6h.01M10.5 6h3" /></svg></span>
          </div>
          <h3 class="svc-expand__name">Appliance repair</h3>
          <p class="svc-expand__benefit">Washers, ovens and fridges, working again today.</p>
          <div class="svc-expand__row">
            <p class="svc-expand__price"><small>from</small> $89</p>
            <div class="svc-expand__actions">
              <a class="svc-expand__quick" href="#book-appliance">Book<span class="svc-expand__sr"> appliance repair</span></a>
              <button class="svc-expand__toggle" type="button" hidden>Details<span class="svc-expand__sr"> for appliance repair</span><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg></button>
            </div>
          </div>
        </div>
        <div class="svc-expand__details">
          <div class="svc-expand__details-head">
            <h4 class="svc-expand__detail-title">Appliance repair plans</h4>
            <button class="svc-expand__close" type="button" aria-label="Close appliance repair details" hidden><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
          </div>
          <ul class="svc-expand__tiers" role="list">
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Basic</span><span class="svc-expand__tier-price"><small>from</small> $89</span><span class="svc-expand__tier-note">Diagnosis and a quick fix</span></li>
            <li class="svc-expand__tier svc-expand__tier--pick"><span class="svc-expand__tier-name">Plus <em class="svc-expand__badge">Popular</em></span><span class="svc-expand__tier-price"><small>from</small> $159</span><span class="svc-expand__tier-note">Repair with common parts</span></li>
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Pro</span><span class="svc-expand__tier-price"><small>from</small> $259</span><span class="svc-expand__tier-note">Two appliances, one visit</span></li>
          </ul>
          <div class="svc-expand__more">
            <div>
              <p class="svc-expand__inc-title">What's included</p>
              <ul class="svc-expand__checks" role="list">
                <li>All major brands</li>
                <li>90-day parts warranty</li>
                <li>Same-day slots</li>
                <li>No fix, no fee</li>
              </ul>
            </div>
            <a class="svc-expand__book" href="#book-appliance">Book this service<span class="svc-expand__sr">: appliance repair</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>

      <li class="svc-expand__card">
        <div class="svc-expand__summary">
          <div class="svc-expand__top">
            <span class="svc-expand__num" aria-hidden="true">06</span>
            <span class="svc-expand__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M4 8.5 7 4h10l3 4.5M2.5 8.5h19v.8a2.2 2.2 0 0 1-2.2 2.2H4.7a2.2 2.2 0 0 1-2.2-2.2zM5 11.5v9h9.5v-9M18 11.5v7a2 2 0 0 0 2 2h1.5" /></svg></span>
          </div>
          <h3 class="svc-expand__name">Gutters</h3>
          <p class="svc-expand__benefit">Cleaning, guards and repairs, with every scrap hauled away.</p>
          <div class="svc-expand__row">
            <p class="svc-expand__price"><small>from</small> $119</p>
            <div class="svc-expand__actions">
              <a class="svc-expand__quick" href="#book-gutters">Book<span class="svc-expand__sr"> gutters</span></a>
              <button class="svc-expand__toggle" type="button" hidden>Details<span class="svc-expand__sr"> for gutters</span><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 5v14M5 12h14" /></svg></button>
            </div>
          </div>
        </div>
        <div class="svc-expand__details">
          <div class="svc-expand__details-head">
            <h4 class="svc-expand__detail-title">Gutter plans</h4>
            <button class="svc-expand__close" type="button" aria-label="Close gutter details" hidden><svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
          </div>
          <ul class="svc-expand__tiers" role="list">
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Basic</span><span class="svc-expand__tier-price"><small>from</small> $119</span><span class="svc-expand__tier-note">Clean and flush, one storey</span></li>
            <li class="svc-expand__tier svc-expand__tier--pick"><span class="svc-expand__tier-name">Plus <em class="svc-expand__badge">Popular</em></span><span class="svc-expand__tier-price"><small>from</small> $189</span><span class="svc-expand__tier-note">Two storeys plus downspouts</span></li>
            <li class="svc-expand__tier"><span class="svc-expand__tier-name">Pro</span><span class="svc-expand__tier-price"><small>from</small> $349</span><span class="svc-expand__tier-note">Full clean with guards fitted</span></li>
          </ul>
          <div class="svc-expand__more">
            <div>
              <p class="svc-expand__inc-title">What's included</p>
              <ul class="svc-expand__checks" role="list">
                <li>Downspouts flushed</li>
                <li>Before and after photos</li>
                <li>Debris bagged and hauled</li>
                <li>Minor re-sealing</li>
              </ul>
            </div>
            <a class="svc-expand__book" href="#book-gutters">Book this service<span class="svc-expand__sr">: gutters</span> <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </div>
      </li>
    </ul>

    <p class="svc-expand__foot">Need two trades? <a href="#bundle">Bundle any two services in one visit and save 10%</a></p>
  </div>
</section>
```

## CSS

```css
/* Section: deepest surface with a wash of brand light from above */
.svc-expand {
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(64rem 30rem at 50% -12rem, color-mix(in srgb, var(--primary) 24%, transparent), transparent 70%),
    radial-gradient(36rem 22rem at 100% 100%, color-mix(in srgb, var(--primary-2) 14%, transparent), transparent 70%),
    var(--surface-deep);
  color: var(--text-inverse); font-family: var(--font-sans);
}
.svc-expand__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }

/* Heading */
.svc-expand__head { max-width: 42rem; margin-bottom: clamp(2.25rem, 5vw, 3.5rem); }
.svc-expand__eyebrow { margin: 0; color: color-mix(in srgb, var(--primary-2) 55%, var(--text-inverse)); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.svc-expand__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.25rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.svc-expand__glow {
  background: linear-gradient(100deg, var(--text-inverse), color-mix(in srgb, var(--primary) 40%, var(--text-inverse)) 45%, color-mix(in srgb, var(--primary-2) 75%, var(--text-inverse)));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.svc-expand__intro { max-width: 36rem; margin: 1rem 0 0; color: var(--text-inverse-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }

/* Grid: cards keep their own height so a neighbour never stretches beside an open card */
.svc-expand__grid { display: grid; gap: var(--space-md); align-items: start; margin: 0; padding: 0; list-style: none; }
@media (min-width: 600px) { .svc-expand__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1024px) { .svc-expand__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.25rem; } }

/* Card: opaque face (padding-box) over a hairline (border-box); open turns the hairline into the brand gradient */
.svc-expand__card {
  --svc-expand-face: color-mix(in srgb, var(--text-inverse) 4%, var(--surface-deep));
  container: svc-expand-card / inline-size;
  position: relative; border: 1px solid transparent; border-radius: var(--radius-2xl);
  background:
    linear-gradient(180deg, color-mix(in srgb, var(--text-inverse) 7%, var(--surface-deep)), var(--svc-expand-face) 55%) padding-box,
    linear-gradient(180deg, color-mix(in srgb, var(--text-inverse) 18%, transparent), var(--border-inverse) 45%) border-box;
  box-shadow: var(--highlight-inverse), 0 28px 56px -36px color-mix(in srgb, var(--surface-deep) 95%, transparent);
}
.svc-expand__card.is-open {
  background:
    radial-gradient(36rem 14rem at 0% 0%, color-mix(in srgb, var(--primary) 20%, transparent), transparent 70%) padding-box,
    radial-gradient(30rem 16rem at 100% 100%, color-mix(in srgb, var(--primary-2) 12%, transparent), transparent 70%) padding-box,
    linear-gradient(180deg, color-mix(in srgb, var(--text-inverse) 7%, var(--surface-deep)), var(--svc-expand-face) 55%) padding-box,
    linear-gradient(135deg, var(--primary), var(--primary-2) 60%, color-mix(in srgb, var(--primary-2) 30%, transparent)) border-box;
  box-shadow: var(--highlight-inverse), var(--shadow-glow);
}

/* Summary: the open card's summary keeps the collapsed column width, so the grow never reflows it */
.svc-expand__summary { display: flex; flex-direction: column; gap: 0.625rem; padding: var(--space-lg); }
.svc-expand--js .svc-expand__card.is-open .svc-expand__summary { max-width: calc(var(--svc-expand-col, 100%) - 2px); }
.svc-expand__top { display: flex; align-items: center; justify-content: space-between; margin-bottom: var(--space-sm); }
.svc-expand__num { color: var(--text-inverse-muted); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; }
.svc-expand__icon {
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-lg); color: var(--text-inverse);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 60%, transparent), color-mix(in srgb, var(--primary-2) 45%, transparent));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-inverse) 14%, transparent), var(--highlight-inverse), 0 10px 28px -12px color-mix(in srgb, var(--primary) 80%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.svc-expand__icon svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
@media (hover: hover) { .svc-expand__card:hover .svc-expand__icon { transform: rotate(-6deg) scale(1.06); } }
.svc-expand__name { margin: 0; font: 600 1.375rem/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.svc-expand__benefit { min-height: 3.1em; margin: 0; color: var(--text-inverse-muted); font-size: 0.9375rem; line-height: 1.55; }
.svc-expand__row { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem; margin-top: var(--space-sm); padding-top: var(--space-md); border-top: 1px solid var(--border-inverse); }
.svc-expand__price { margin: 0; font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.svc-expand__price small, .svc-expand__tier-price small { margin-right: 0.125rem; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0; }

/* Actions: "Book" (collapsed only) and the Details disclosure button */
.svc-expand__actions { display: flex; gap: var(--space-sm); }
.svc-expand__quick, .svc-expand__toggle {
  display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.5rem; padding: 0 0.9375rem; border-radius: var(--radius-full);
  font: 600 0.875rem/1 var(--font-sans); text-decoration: none;
  transition: background-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
.svc-expand__quick { background: var(--text-inverse); color: var(--surface-deep); }
.svc-expand__quick:hover { background: color-mix(in srgb, var(--text-inverse) 85%, var(--primary-2)); }
.svc-expand:not(.svc-expand--js) .svc-expand__quick, .svc-expand__card.is-open .svc-expand__quick { display: none; }
.svc-expand__toggle { border: 0; cursor: pointer; background: var(--glass-inverse); color: var(--text-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); }
.svc-expand__toggle:hover { background: color-mix(in srgb, var(--text-inverse) 12%, transparent); }
.svc-expand__toggle[hidden], .svc-expand__close[hidden] { display: none; }
.svc-expand__toggle svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; transition: transform var(--dur-3) var(--ease-spring); }
.svc-expand__toggle[aria-expanded="true"] { background: var(--text-inverse); color: var(--surface-deep); }
.svc-expand__toggle[aria-expanded="true"] svg { transform: rotate(45deg); }
.svc-expand__quick:active, .svc-expand__toggle:active { transform: scale(0.96); }

/* Details: static under each card without JS; hidden until opened with JS */
.svc-expand__details { display: grid; gap: 1.25rem; padding: 0 var(--space-lg) var(--space-lg); }
.svc-expand__details[hidden] { display: none; }
.svc-expand__details-head { display: flex; align-items: center; justify-content: space-between; gap: var(--space-md); padding-top: 1.25rem; border-top: 1px solid var(--border-inverse); }
.svc-expand__detail-title { margin: 0; border-radius: var(--radius-sm); font: 600 1.0625rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.svc-expand__close {
  flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--glass-inverse); color: var(--text-inverse-muted); box-shadow: inset 0 0 0 1px var(--border-inverse);
  transition: background-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
.svc-expand__close:hover { background: color-mix(in srgb, var(--text-inverse) 12%, transparent); color: var(--text-inverse); transform: rotate(90deg); }
.svc-expand__close svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }

/* Tiers: compact rows in a narrow card, three columns once the card is wide (container query) */
.svc-expand__tiers { display: grid; gap: var(--space-sm); margin: 0; padding: 0; list-style: none; }
.svc-expand__tier {
  display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; column-gap: var(--space-md); row-gap: 0.3125rem;
  padding: 0.875rem var(--space-md); border-radius: var(--radius-xl); background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse);
}
.svc-expand__tier--pick {
  background: linear-gradient(150deg, color-mix(in srgb, var(--primary) 32%, transparent), color-mix(in srgb, var(--primary-2) 14%, transparent));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary-2) 55%, transparent), var(--highlight-inverse);
}
.svc-expand__tier-name { display: flex; align-items: center; gap: var(--space-sm); color: var(--text-inverse-muted); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.svc-expand__tier-price { grid-column: 2; grid-row: 1 / span 2; font: 600 1.375rem/1 var(--font-display); letter-spacing: var(--tracking-tight); white-space: nowrap; font-variant-numeric: tabular-nums; }
.svc-expand__tier-note { color: var(--text-inverse-muted); font-size: 0.8125rem; line-height: 1.4; }
.svc-expand__badge { padding: 0.1875rem 0.4375rem; border-radius: var(--radius-full); background: var(--text-inverse); color: var(--surface-deep); font: 700 0.625rem/1.2 var(--font-mono); font-style: normal; letter-spacing: 0.08em; }

/* What's included and the booking button */
.svc-expand__more { --svc-expand-i: 4; display: grid; gap: 1.25rem; }
.svc-expand__inc-title { margin: 0 0 0.75rem; color: var(--text-inverse-muted); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.svc-expand__checks { display: grid; gap: var(--space-sm); margin: 0; padding: 0; list-style: none; }
.svc-expand__checks li { position: relative; padding-left: 1.625rem; font-size: 0.9375rem; line-height: 1.4; }
.svc-expand__checks li::before { content: ""; position: absolute; left: 0; top: 0.0625rem; width: 1.125rem; height: 1.125rem; border-radius: 50%; background: color-mix(in srgb, var(--primary-2) 26%, transparent); }
.svc-expand__checks li::after {
  content: ""; position: absolute; left: 0.4375rem; top: 0.25rem; width: 0.25rem; height: 0.5rem;
  border: solid color-mix(in srgb, var(--primary-2) 45%, var(--text-inverse)); border-width: 0 2px 2px 0; transform: rotate(45deg);
}
.svc-expand__book {
  justify-self: start; display: inline-flex; align-items: center; gap: 0.5rem; min-height: 3rem; padding: 0 1.375rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none; white-space: nowrap;
  box-shadow: 0 12px 36px -12px color-mix(in srgb, var(--primary) 90%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.svc-expand__book svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.svc-expand__book:hover svg { transform: translateX(3px); }
.svc-expand__book:active { transform: scale(0.97); }

@container svc-expand-card (min-width: 34rem) {
  .svc-expand__tiers { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.75rem; }
  .svc-expand__tier { grid-template-columns: none; align-content: start; row-gap: 0.5rem; padding: 1.125rem; }
  .svc-expand__tier-price { grid-column: auto; grid-row: auto; font-size: 1.625rem; }
  .svc-expand__more { grid-template-columns: minmax(0, 1fr) auto; align-items: end; }
  .svc-expand__checks { grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: var(--space-lg); }
}

/* Opening: the details rise in, staggered, while the card grows */
.svc-expand__tier:nth-child(1) { --svc-expand-i: 1; }
.svc-expand__tier:nth-child(2) { --svc-expand-i: 2; }
.svc-expand__tier:nth-child(3) { --svc-expand-i: 3; }
.svc-expand__card.is-open :is(.svc-expand__details-head, .svc-expand__tier, .svc-expand__more) {
  animation: svc-expand-rise var(--dur-4) var(--ease-out) calc(var(--svc-expand-i, 0) * var(--stagger) + 140ms) both;
}

/* Footer line, focus and utilities */
.svc-expand__foot { margin: clamp(2rem, 4vw, 3rem) 0 0; color: var(--text-inverse-muted); text-align: center; }
.svc-expand__foot a { color: var(--text-inverse); font-weight: 600; text-decoration-color: color-mix(in srgb, var(--primary-2) 60%, transparent); text-underline-offset: 3px; }
.svc-expand :is(.svc-expand__quick, .svc-expand__toggle, .svc-expand__close, .svc-expand__book, .svc-expand__detail-title, .svc-expand__foot a):focus-visible {
  outline: 2px solid var(--text-inverse); outline-offset: 3px;
}
.svc-expand__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

@media (prefers-reduced-motion: reduce) {
  .svc-expand *, .svc-expand *::before, .svc-expand *::after { animation: none !important; }
}
@keyframes svc-expand-rise { from { opacity: 0; transform: translateY(12px); } }
```

## JS

```js
// Expanding Service Grid: one card open at a time. The opening card grows in place (clip-path + translate);
// every other card glides to its new spot with a transform-only FLIP (WAAPI).
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
let uid = 0;

document.querySelectorAll('[data-svc-expand]').forEach((root) => {
  const grid = root.querySelector('.svc-expand__grid');
  const cards = [...grid.children];
  const token = (name) => getComputedStyle(root).getPropertyValue(name).trim();
  const ms = (name) => parseFloat(token(name)) || 0;
  const id = `svc-expand-${++uid}`;
  const parts = (card) => ({
    toggle: card.querySelector('.svc-expand__toggle'),
    panel: card.querySelector('.svc-expand__details'),
    heading: card.querySelector('.svc-expand__detail-title'),
  });
  let open = null;
  let busy = false;
  let cols = 0;

  root.classList.add('svc-expand--js');
  cards.forEach((card, i) => {
    const { toggle, panel, heading } = parts(card);
    panel.id = `${id}-details-${i}`;
    panel.hidden = true;
    heading.tabIndex = -1;
    toggle.setAttribute('aria-controls', panel.id);
    toggle.setAttribute('aria-expanded', 'false');
    toggle.hidden = false;
    card.querySelector('.svc-expand__close').hidden = false;
    toggle.addEventListener('click', () => go(open === card ? null : card));
  });

  // Column count and width; the open card's summary keeps the collapsed width so it never reflows
  const measure = () => {
    const tracks = getComputedStyle(grid).gridTemplateColumns.split(' ');
    cols = tracks.length;
    grid.style.setProperty('--svc-expand-col', tracks[0]);
  };

  // Span two columns in place; a card in the last column grows leftwards and keeps its row
  const place = (card) => {
    const i = cards.indexOf(card);
    const last = cols > 1 && i % cols === cols - 1;
    card.style.gridColumn = cols < 2 ? '' : last ? `${cols - 1} / span 2` : 'span 2';
    card.style.gridRow = last ? String(Math.floor(i / cols) + 1) : '';
  };

  const set = (card, on) => {
    const { toggle, panel } = parts(card);
    card.classList.toggle('is-open', on);
    toggle.setAttribute('aria-expanded', String(on));
    panel.hidden = !on;
    if (on) place(card);
    else card.style.gridColumn = card.style.gridRow = '';
  };

  // FLIP: read every box, change the layout, read again, then play each card from old to new
  const flip = (change, grow) => {
    const first = cards.map((card) => card.getBoundingClientRect());
    cards.forEach((card) => card.getAnimations({ subtree: true }).forEach((a) => a.cancel()));
    change();
    const last = cards.map((card) => card.getBoundingClientRect());
    if (reduce.matches) return last[cards.indexOf(grow)];
    const timing = { duration: ms('--dur-4'), easing: token('--ease-out') || 'ease-out' };
    cards.forEach((card, i) => {
      const dx = first[i].left - last[i].left;
      const dy = first[i].top - last[i].top;
      if (card === grow) {
        const r = getComputedStyle(card).borderTopLeftRadius;
        const w = Math.max(0, last[i].width - first[i].width);
        const h = Math.max(0, last[i].height - first[i].height);
        card.animate([
          { transform: `translate(${dx}px, ${dy}px)`, clipPath: `inset(0 ${w}px ${h}px 0 round ${r})` },
          { transform: 'none', clipPath: `inset(0 0 0 0 round ${r})` },
        ], timing);
      } else if (Math.abs(dx) + Math.abs(dy) > 1) {
        card.animate([{ transform: `translate(${dx}px, ${dy}px)` }, { transform: 'none' }], timing);
      }
    });
    return last[cards.indexOf(grow)];
  };

  // Before the layout changes, fold the open card back to its summary so nothing pops
  const fold = (card) => {
    if (reduce.matches) return Promise.resolve();
    const box = card.getBoundingClientRect();
    const w = Math.max(0, box.width - parseFloat(getComputedStyle(grid).gridTemplateColumns));
    const h = Math.max(0, box.height - card.querySelector('.svc-expand__summary').offsetHeight - 2);
    const r = getComputedStyle(card).borderTopLeftRadius;
    const timing = { duration: ms('--dur-3'), easing: token('--ease-in-out') || 'ease-in-out', fill: 'forwards' };
    parts(card).panel.animate({ opacity: [1, 0] }, timing);
    return card.animate({ clipPath: [`inset(0 0 0 0 round ${r})`, `inset(0 ${w}px ${h}px 0 round ${r})`] }, timing).finished.catch(() => {});
  };

  const go = async (next) => {
    if (busy || next === open) return;
    busy = true;
    const prev = open;
    if (prev) await fold(prev);
    measure();
    const box = flip(() => {
      if (prev) set(prev, false);
      if (next) set(next, true);
      open = next;
    }, next);
    busy = false;
    if (next) {
      parts(next).heading.focus({ preventScroll: true });
      if (box.bottom > innerHeight || box.top < 0) {
        const top = box.top < 0 ? box.top - 24 : Math.min(box.top - 24, box.bottom - innerHeight + 24);
        scrollBy({ top, behavior: reduce.matches ? 'auto' : 'smooth' });
      }
    } else if (prev) {
      parts(prev).toggle.focus();
    }
  };

  root.addEventListener('click', (e) => {
    if (e.target.closest('.svc-expand__close')) go(null);
  });
  root.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && open) {
      e.preventDefault();
      go(null);
    }
  });

  // Re-place the open card when the column count changes
  new ResizeObserver(() => {
    const before = cols;
    measure();
    if (open && cols !== before) place(open);
  }).observe(grid);
});
```

## Notes

- Disclosure pattern: each Details button has `aria-expanded` and an `aria-controls` id generated per instance. Opening moves focus to the plans heading (`tabindex="-1"`). Escape anywhere in the section, the close button or Details again collapses the card and returns focus to its Details button. Only one card is open at a time.
- Motion: the other cards animate only `transform`, using WAAPI with the `--dur-4` / `--ease-out` token values read at run time. The opening card grows with clip-path plus translate; closing first folds it back to its summary (`--dur-3`). A second click mid-animation starts from wherever things currently are.
- Layout: the open card spans two columns in place. In the last column it grows leftwards and keeps its row, which drops its left neighbour into the next row. That is the only visual reorder; DOM and focus order never change. On phones it grows downwards. The detail layout uses a container query on the card, so tiers stack in a narrow card and sit in three columns in a wide one.
- Without JS each card shows its tiers, checklist and "Book this service" statically; the Details and close buttons stay hidden, and so does the quick "Book" link, leaving one booking link per card. Under reduced motion there is no FLIP, fold or rise, and cards open instantly.
- Contrast on `--surface-deep`: `--text-inverse-muted` copy on the card face is about 7:1, tier labels on the highlighted "Plus" tier at least 5:1, and the gradient headline at least 4.5:1 at every stop.
