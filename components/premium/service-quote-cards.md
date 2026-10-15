# Quote-Builder Service Cards

A light quote builder in one native form. Each service card is a fieldset: the whole card is the label for its "Add to quote" checkbox, and an S / M / L size switch rolls the card's price like an odometer. Ticking a card wraps it in a gradient ring and sends a small gradient dot arcing into a sticky tray, which slides up with removable chips, a count badge that pops as the dot lands, a rolling price range and "Get my quote". On phones the tray stacks into two rows and its chips scroll sideways. Depends on `tokens/variables.css`.

**Motion:** dot flight along a curved path (WAAPI, `--dur-5`, `--ease-in-out`) · tray slide-up (`--dur-4`, `--ease-spring`) · badge pop · odometer digit rolls (`--dur-5`, `--ease-out`, staggered by `--stagger`) · size pill glide and check pop (`--ease-spring`).

## HTML

```html
<section class="svc-quote" aria-labelledby="svc-quote-title" data-svc-quote>
  <div class="svc-quote__inner">
    <header class="svc-quote__head">
      <p class="svc-quote__eyebrow">Instant estimate</p>
      <h2 id="svc-quote-title" class="svc-quote__title">Build your quote <span class="svc-quote__glow">in a few taps.</span></h2>
      <p class="svc-quote__intro">Tick the jobs you need, pick a size and see your price range straight away. No call, no obligation.</p>
    </header>

    <form class="svc-quote__form" action="/quote" method="post" data-svc-quote-demo>
      <div class="svc-quote__grid">
        <fieldset class="svc-quote__card" style="--svc-quote-hue: var(--primary)">
          <legend class="svc-quote__legend"><h3 class="svc-quote__name">Plumbing</h3></legend>
          <span class="svc-quote__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M12 3s6 6.2 6 10.5a6 6 0 0 1-12 0C6 9.2 12 3 12 3zM9.5 14a2.5 2.5 0 0 0 2.5 2.5" /></svg></span>
          <label class="svc-quote__pick"><input class="svc-quote__check" type="checkbox" name="services" value="plumbing"><span>Add to quote<span class="svc-quote__sr">: plumbing</span></span></label>
          <p class="svc-quote__benefit">Leaks, clogs, fixtures and water heaters.</p>
          <fieldset class="svc-quote__sizes">
            <legend class="svc-quote__sizes-label">Job size<span class="svc-quote__sr"> (small, medium or large)</span></legend>
            <div class="svc-quote__seg">
              <label class="svc-quote__size"><input type="radio" name="size-plumbing" value="s" data-lo="95" data-hi="140" checked><span>S</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-plumbing" value="m" data-lo="160" data-hi="240"><span>M</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-plumbing" value="l" data-lo="280" data-hi="420"><span>L</span></label>
            </div>
          </fieldset>
          <p class="svc-quote__price"><small>from</small><span class="svc-quote__odo">$95</span></p>
          <a class="svc-quote__more" href="#plumbing">What's included<span class="svc-quote__sr"> in plumbing</span> <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </fieldset>

        <fieldset class="svc-quote__card" style="--svc-quote-hue: color-mix(in srgb, var(--accent) 70%, var(--warning))">
          <legend class="svc-quote__legend"><h3 class="svc-quote__name">Electrical</h3></legend>
          <span class="svc-quote__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M13 2.5 5.5 13.5H11l-1 8 7.5-11H12l1-8z" /></svg></span>
          <label class="svc-quote__pick"><input class="svc-quote__check" type="checkbox" name="services" value="electrical"><span>Add to quote<span class="svc-quote__sr">: electrical</span></span></label>
          <p class="svc-quote__benefit">Outlets, lighting, panels and EV chargers.</p>
          <fieldset class="svc-quote__sizes">
            <legend class="svc-quote__sizes-label">Job size<span class="svc-quote__sr"> (small, medium or large)</span></legend>
            <div class="svc-quote__seg">
              <label class="svc-quote__size"><input type="radio" name="size-electrical" value="s" data-lo="110" data-hi="160" checked><span>S</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-electrical" value="m" data-lo="180" data-hi="260"><span>M</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-electrical" value="l" data-lo="320" data-hi="480"><span>L</span></label>
            </div>
          </fieldset>
          <p class="svc-quote__price"><small>from</small><span class="svc-quote__odo">$110</span></p>
          <a class="svc-quote__more" href="#electrical">What's included<span class="svc-quote__sr"> in electrical</span> <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </fieldset>

        <fieldset class="svc-quote__card" style="--svc-quote-hue: var(--primary-2)">
          <legend class="svc-quote__legend"><h3 class="svc-quote__name">Heating &amp; cooling</h3></legend>
          <span class="svc-quote__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M10 13.5V5a2 2 0 1 1 4 0v8.5a4 4 0 1 1-4 0zM12 9.5v6M17.5 5h3M17.5 9h2" /></svg></span>
          <label class="svc-quote__pick"><input class="svc-quote__check" type="checkbox" name="services" value="hvac"><span>Add to quote<span class="svc-quote__sr">: heating and cooling</span></span></label>
          <p class="svc-quote__benefit">Tune-ups, repairs and new systems.</p>
          <fieldset class="svc-quote__sizes">
            <legend class="svc-quote__sizes-label">Job size<span class="svc-quote__sr"> (small, medium or large)</span></legend>
            <div class="svc-quote__seg">
              <label class="svc-quote__size"><input type="radio" name="size-hvac" value="s" data-lo="129" data-hi="189" checked><span>S</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-hvac" value="m" data-lo="220" data-hi="330"><span>M</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-hvac" value="l" data-lo="390" data-hi="580"><span>L</span></label>
            </div>
          </fieldset>
          <p class="svc-quote__price"><small>from</small><span class="svc-quote__odo">$129</span></p>
          <a class="svc-quote__more" href="#hvac">What's included<span class="svc-quote__sr"> in heating and cooling</span> <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </fieldset>

        <fieldset class="svc-quote__card" style="--svc-quote-hue: color-mix(in srgb, var(--danger) 70%, var(--accent))">
          <legend class="svc-quote__legend"><h3 class="svc-quote__name">Interior painting</h3></legend>
          <span class="svc-quote__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><rect x="3" y="3" width="15" height="6" rx="2" /><path d="M18 6h2.5v5H11v3.5M9.5 14.5h3v7h-3z" /></svg></span>
          <label class="svc-quote__pick"><input class="svc-quote__check" type="checkbox" name="services" value="painting"><span>Add to quote<span class="svc-quote__sr">: interior painting</span></span></label>
          <p class="svc-quote__benefit">Walls, trim and ceilings, tidied up after.</p>
          <fieldset class="svc-quote__sizes">
            <legend class="svc-quote__sizes-label">Job size<span class="svc-quote__sr"> (small, medium or large)</span></legend>
            <div class="svc-quote__seg">
              <label class="svc-quote__size"><input type="radio" name="size-painting" value="s" data-lo="180" data-hi="260" checked><span>S</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-painting" value="m" data-lo="420" data-hi="640"><span>M</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-painting" value="l" data-lo="890" data-hi="1280"><span>L</span></label>
            </div>
          </fieldset>
          <p class="svc-quote__price"><small>from</small><span class="svc-quote__odo">$180</span></p>
          <a class="svc-quote__more" href="#painting">What's included<span class="svc-quote__sr"> in interior painting</span> <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </fieldset>

        <fieldset class="svc-quote__card" style="--svc-quote-hue: color-mix(in srgb, var(--primary) 55%, var(--text-main))">
          <legend class="svc-quote__legend"><h3 class="svc-quote__name">Appliance repair</h3></legend>
          <span class="svc-quote__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><rect x="4" y="2.5" width="16" height="19" rx="2.5" /><circle cx="12" cy="13.5" r="4.5" /><path d="M7.5 6h.01M10.5 6h3" /></svg></span>
          <label class="svc-quote__pick"><input class="svc-quote__check" type="checkbox" name="services" value="appliance"><span>Add to quote<span class="svc-quote__sr">: appliance repair</span></span></label>
          <p class="svc-quote__benefit">Washers, dryers, ovens and fridges.</p>
          <fieldset class="svc-quote__sizes">
            <legend class="svc-quote__sizes-label">Job size<span class="svc-quote__sr"> (small, medium or large)</span></legend>
            <div class="svc-quote__seg">
              <label class="svc-quote__size"><input type="radio" name="size-appliance" value="s" data-lo="89" data-hi="129" checked><span>S</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-appliance" value="m" data-lo="140" data-hi="210"><span>M</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-appliance" value="l" data-lo="220" data-hi="340"><span>L</span></label>
            </div>
          </fieldset>
          <p class="svc-quote__price"><small>from</small><span class="svc-quote__odo">$89</span></p>
          <a class="svc-quote__more" href="#appliance">What's included<span class="svc-quote__sr"> in appliance repair</span> <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </fieldset>

        <fieldset class="svc-quote__card" style="--svc-quote-hue: color-mix(in srgb, var(--primary-2) 60%, var(--primary))">
          <legend class="svc-quote__legend"><h3 class="svc-quote__name">Gutter cleaning</h3></legend>
          <span class="svc-quote__icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M4 8.5 7 4h10l3 4.5M2.5 8.5h19v.8a2.2 2.2 0 0 1-2.2 2.2H4.7a2.2 2.2 0 0 1-2.2-2.2zM5 11.5v9h9.5v-9M18 11.5v7a2 2 0 0 0 2 2h1.5" /></svg></span>
          <label class="svc-quote__pick"><input class="svc-quote__check" type="checkbox" name="services" value="gutters"><span>Add to quote<span class="svc-quote__sr">: gutter cleaning</span></span></label>
          <p class="svc-quote__benefit">Cleared, flushed and checked for leaks.</p>
          <fieldset class="svc-quote__sizes">
            <legend class="svc-quote__sizes-label">Job size<span class="svc-quote__sr"> (small, medium or large)</span></legend>
            <div class="svc-quote__seg">
              <label class="svc-quote__size"><input type="radio" name="size-gutters" value="s" data-lo="99" data-hi="149" checked><span>S</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-gutters" value="m" data-lo="149" data-hi="219"><span>M</span></label>
              <label class="svc-quote__size"><input type="radio" name="size-gutters" value="l" data-lo="239" data-hi="339"><span>L</span></label>
            </div>
          </fieldset>
          <p class="svc-quote__price"><small>from</small><span class="svc-quote__odo">$99</span></p>
          <a class="svc-quote__more" href="#gutters">What's included<span class="svc-quote__sr"> in gutter cleaning</span> <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
        </fieldset>
      </div>

      <div class="svc-quote__dock">
        <p class="svc-quote__hint"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 8v8M8 12h8M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18z" /></svg>Tick a service to start your estimate</p>
        <div class="svc-quote__tray">
          <div class="svc-quote__summary">
            <span class="svc-quote__count" aria-hidden="true">0</span>
            <ul class="svc-quote__chips" role="list" aria-label="Selected services"></ul>
            <p class="svc-quote__total"><small>Estimate</small><span class="svc-quote__range"><span class="svc-quote__odo">$0</span><span class="svc-quote__dash" aria-hidden="true">–</span><span class="svc-quote__sr"> to </span><span class="svc-quote__odo">$0</span></span></p>
          </div>
          <p class="svc-quote__plain">Tick the services you need and we'll email a written quote, usually within the hour.</p>
          <button class="svc-quote__submit" type="submit"><span class="svc-quote__submit-label">Get my quote</span><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></button>
        </div>
        <p class="svc-quote__sr" aria-live="polite" data-svc-quote-live></p>
      </div>
    </form>
  </div>
</section>
```

## CSS

```css
/* Section: clean white with a soft brand glow behind the grid. overflow: clip keeps the parked tray
   from spilling out without creating a scroll container, so the dock can stay sticky. */
.svc-quote {
  position: relative; isolation: isolate; overflow: clip;
  background: radial-gradient(52rem 28rem at 50% 0%, color-mix(in srgb, var(--primary) 7%, transparent), transparent 70%), var(--surface-light);
  color: var(--text-main); font-family: var(--font-sans);
}
.svc-quote__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter) clamp(2.5rem, 5vw, 4rem); }

/* Heading */
.svc-quote__head { max-width: 38rem; margin: 0 auto clamp(2rem, 5vw, 3rem); text-align: center; }
.svc-quote__eyebrow { display: inline-flex; margin: 0; padding: 0.375rem 0.75rem; border-radius: var(--radius-full); background: color-mix(in srgb, var(--primary) 8%, var(--surface-light)); color: var(--primary); font: 600 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.svc-quote__title { margin: 1rem 0 0; font: 600 clamp(2rem, 1.25rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.svc-quote__glow { background: linear-gradient(100deg, var(--primary), var(--primary-2)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.svc-quote__intro { max-width: 32rem; margin: 1rem auto 0; color: var(--text-muted); font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); line-height: 1.6; }

/* Grid */
.svc-quote__form { margin: 0; }
.svc-quote__grid { display: grid; gap: var(--space-md); }
@media (min-width: 600px) { .svc-quote__grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (min-width: 1024px) { .svc-quote__grid { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: var(--space-lg); } }

/* Card: a fieldset laid out as a grid; muted until picked, then white with a gradient ring */
.svc-quote__card {
  --svc-quote-ink: color-mix(in srgb, var(--svc-quote-hue) 70%, var(--text-main));
  position: relative; display: grid; grid-template-columns: minmax(0, 1fr) auto;
  grid-template-areas: "icon pick" "name name" "benefit benefit" "sizes price" "more more";
  align-items: center; gap: var(--space-sm) var(--space-md);
  min-width: 0; margin: 0; padding: 1.25rem; border: 0; border-radius: var(--radius-2xl);
  background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
  transition: background-color var(--dur-3) var(--ease-out), box-shadow var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring);
}
.svc-quote__card::before {
  content: ""; position: absolute; inset: 0; padding: 2px; border-radius: inherit; pointer-events: none; opacity: 0;
  background: linear-gradient(135deg, var(--primary), var(--primary-2));
  -webkit-mask: linear-gradient(black 0 0) content-box, linear-gradient(black 0 0);
  -webkit-mask-composite: xor;
  mask: linear-gradient(black 0 0) content-box exclude, linear-gradient(black 0 0);
  transition: opacity var(--dur-3) var(--ease-out);
}
.svc-quote__card:has(.svc-quote__check:checked) {
  background: var(--surface-light);
  box-shadow: 0 0 0 5px color-mix(in srgb, var(--primary) 9%, transparent), 0 22px 44px -24px color-mix(in srgb, var(--primary) 60%, transparent);
}
.svc-quote__card:has(.svc-quote__check:checked)::before { opacity: 1; }
@media (hover: hover) { .svc-quote__card:hover { transform: translateY(-2px); } }

.svc-quote__legend { float: left; grid-area: name; width: 100%; margin: var(--space-xs) 0 0; padding: 0; }
.svc-quote__name { margin: 0; font: 600 1.1875rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.svc-quote__icon {
  grid-area: icon; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: var(--radius-lg);
  background: var(--surface-light); color: var(--svc-quote-ink);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--svc-quote-hue) 22%, var(--border-subtle)), 0 6px 14px -8px color-mix(in srgb, var(--svc-quote-hue) 60%, transparent);
  transition: background-color var(--dur-3) var(--ease-out);
}
.svc-quote__icon svg { fill: none; stroke: currentColor; stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.svc-quote__card:has(.svc-quote__check:checked) .svc-quote__icon { background: color-mix(in srgb, var(--svc-quote-hue) 12%, var(--surface-light)); }
.svc-quote__benefit { grid-area: benefit; margin: 0 0 var(--space-sm); color: var(--text-muted); font-size: 0.9375rem; line-height: 1.5; }

/* "Add to quote": the label's ::after stretches over the card, so the whole card toggles the checkbox */
.svc-quote__pick {
  grid-area: pick; display: inline-flex; align-items: center; gap: var(--space-sm); min-height: 2.5rem; padding: 0.25rem 0.875rem 0.25rem 0.375rem;
  border-radius: var(--radius-full); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle);
  color: var(--text-main); font-size: 0.8125rem; font-weight: 600; cursor: pointer; user-select: none;
  transition: background-color var(--dur-3) var(--ease-out), color var(--dur-3) var(--ease-out);
}
.svc-quote__pick::after { content: ""; position: absolute; inset: 0; border-radius: var(--radius-2xl); cursor: pointer; }
.svc-quote__card:has(.svc-quote__check:checked) .svc-quote__pick { background: var(--text-main); color: var(--surface-light); }
.svc-quote__check {
  appearance: none; flex: none; display: grid; place-content: center; width: 1.75rem; height: 1.75rem; margin: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-light); box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--text-muted) 60%, transparent);
  transition: box-shadow var(--dur-2) var(--ease-out), transform var(--dur-3) var(--ease-spring);
}
.svc-quote__check::before {
  content: ""; width: 1rem; height: 1rem; background: var(--text-inverse); transform: scale(0);
  -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='m5 12.5 4.5 4.5L19 7.5' fill='none' stroke='black' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / contain no-repeat;
  mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='m5 12.5 4.5 4.5L19 7.5' fill='none' stroke='black' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / contain no-repeat;
  transition: transform var(--dur-3) var(--ease-spring);
}
.svc-quote__check:checked { background: linear-gradient(135deg, var(--primary), var(--primary-2)); box-shadow: none; }
.svc-quote__check:checked::before { transform: none; }
.svc-quote__check:active { transform: scale(0.9); }

/* S / M / L: native radios over each segment; a dark pill glides to the checked one */
.svc-quote__sizes { grid-area: sizes; position: relative; z-index: 1; display: grid; justify-items: start; gap: 0.375rem; min-width: 0; margin: 0; padding: 0; border: 0; }
.svc-quote__sizes-label { float: left; padding: 0; }
.svc-quote__sizes-label, .svc-quote__price small { color: var(--text-muted); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }
.svc-quote__seg { position: relative; display: inline-grid; grid-template-columns: repeat(3, 2.75rem); padding: 0.1875rem; border-radius: var(--radius-full); background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.svc-quote__size { position: relative; height: 2.25rem; cursor: pointer; }
.svc-quote__size input { position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%; margin: 0; opacity: 0; cursor: pointer; }
.svc-quote__size span {
  position: relative; display: grid; place-items: center; height: 100%; border-radius: var(--radius-full);
  color: var(--text-muted); font-size: 0.875rem; font-weight: 700; transition: color var(--dur-3) var(--ease-out);
}
.svc-quote__size:hover input:not(:checked) + span { color: var(--text-main); }
.svc-quote__size input:checked + span { background: var(--text-main); color: var(--surface-light); }
.svc-quote__size input:focus-visible + span { outline: 2px solid var(--primary); outline-offset: 2px; }
@supports selector(:has(*)) {
  .svc-quote__seg::before {
    content: ""; position: absolute; top: 0.1875rem; left: 0.1875rem; width: 2.75rem; height: 2.25rem; border-radius: var(--radius-full);
    background: var(--text-main); box-shadow: 0 6px 14px -6px color-mix(in srgb, var(--text-main) 60%, transparent);
    transition: transform var(--dur-4) var(--ease-spring);
  }
  .svc-quote__seg:has(.svc-quote__size:nth-child(2) input:checked)::before { transform: translateX(100%); }
  .svc-quote__seg:has(.svc-quote__size:nth-child(3) input:checked)::before { transform: translateX(200%); }
  .svc-quote__size input:checked + span { background: transparent; }
}

/* Price and link */
.svc-quote__price { grid-area: price; display: grid; justify-items: end; align-self: end; gap: 0.375rem; margin: 0; }
.svc-quote__price .svc-quote__odo { font: 600 1.625rem/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.svc-quote__more {
  grid-area: more; position: relative; z-index: 1; justify-self: start; display: inline-flex; align-items: center; gap: 0.375rem;
  margin-top: var(--space-xs); padding-block: 0.25rem; color: var(--text-main); font-size: 0.875rem; font-weight: 600;
  text-decoration: underline; text-decoration-color: color-mix(in srgb, var(--svc-quote-hue) 45%, transparent); text-underline-offset: 3px;
}
.svc-quote__more svg { color: var(--svc-quote-ink); fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.svc-quote__more:hover svg { transform: translateX(3px); }
.svc-quote :is(.svc-quote__check, .svc-quote__more):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Odometer: each digit is a 0–9 strip in a one-line window */
.svc-quote__odo { display: inline-flex; font-variant-numeric: tabular-nums; }
.svc-quote__digit, .svc-quote__glyph { display: block; height: 1.15em; overflow: hidden; line-height: 1.15; }
.svc-quote__strip {
  display: block; white-space: pre; transform: translateY(calc(var(--svc-quote-d, 0) * -1.15em));
  transition: transform var(--dur-5) var(--ease-out) calc(var(--svc-quote-k, 0) * var(--stagger));
}

/* Dock: sticky to the bottom of the section; the hint and the tray share one cell */
.svc-quote__dock { position: sticky; bottom: var(--space-md); z-index: var(--z-sticky); display: grid; margin-top: var(--space-xl); }
.svc-quote__hint, .svc-quote__tray { grid-area: 1 / 1; }
.svc-quote__hint { display: none; }
.svc-quote--js .svc-quote__hint {
  display: inline-flex; align-items: center; gap: var(--space-sm); justify-self: center; align-self: end; margin: 0; padding: 0.625rem var(--space-md);
  border-radius: var(--radius-full); background: var(--surface-light); color: var(--text-muted); font-size: 0.875rem; font-weight: 500;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-lg);
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-3) var(--ease-out), visibility 0s linear 0s;
}
.svc-quote__hint svg { flex: none; color: var(--primary); fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }
.svc-quote__dock.is-active .svc-quote__hint {
  opacity: 0; transform: translateY(8px); visibility: hidden;
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-3) var(--ease-out), visibility 0s linear var(--dur-3);
}

/* Tray. Without JS: a plain line and the submit button */
.svc-quote__tray {
  display: grid; grid-template-columns: minmax(0, 1fr); grid-template-areas: "plain" "submit"; align-items: center; gap: 0.75rem var(--space-md);
  padding: var(--space-md); border-radius: var(--radius-2xl); background: var(--surface-deep); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 24px 60px -24px color-mix(in srgb, var(--surface-deep) 70%, transparent);
}
@media (min-width: 600px) { .svc-quote__tray { grid-template-columns: minmax(0, 1fr) auto; grid-template-areas: "plain submit"; padding: 0.75rem 0.75rem 0.75rem 1.25rem; } }
.svc-quote__plain { grid-area: plain; margin: 0; color: var(--text-inverse-muted); font-size: 0.9375rem; line-height: 1.5; }
.svc-quote__summary { display: none; }

/* With JS: the tray waits below the fold of the dock and slides up once something is picked */
.svc-quote--js .svc-quote__plain { display: none; }
.svc-quote--js .svc-quote__summary { display: contents; }
.svc-quote--js .svc-quote__tray {
  grid-template-columns: auto minmax(0, 1fr) auto; grid-template-areas: "count chips chips" "total total submit";
  opacity: 0; visibility: hidden; transform: translateY(calc(100% + var(--space-xl)));
  transition: transform var(--dur-4) var(--ease-out), opacity var(--dur-3) var(--ease-out), visibility 0s linear var(--dur-4);
}
@media (min-width: 768px) {
  .svc-quote--js .svc-quote__tray { grid-template-columns: auto minmax(0, 1fr) auto auto; grid-template-areas: "count chips total submit"; }
}
.svc-quote__dock.is-active .svc-quote__tray {
  opacity: 1; visibility: visible; transform: none;
  transition: transform var(--dur-4) var(--ease-spring), opacity var(--dur-3) var(--ease-out), visibility 0s linear 0s;
}
.svc-quote__count {
  grid-area: count; display: grid; place-items: center; width: 2.75rem; height: 2.75rem; border-radius: 50%;
  background: var(--primary); color: var(--text-inverse); font: 700 1.0625rem/1 var(--font-display); font-variant-numeric: tabular-nums;
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--primary-2) 35%, transparent), 0 8px 20px -6px color-mix(in srgb, var(--primary) 80%, transparent);
}
.svc-quote__chips { grid-area: chips; display: flex; gap: 0.375rem; min-width: 0; margin: 0; padding: 0.125rem; overflow-x: auto; list-style: none; scrollbar-width: none; }
.svc-quote__chips::-webkit-scrollbar { display: none; }
.svc-quote__chip {
  flex: none; display: inline-flex; align-items: center; gap: var(--space-xs); padding: 0.25rem 0.25rem 0.25rem 0.75rem; border-radius: var(--radius-full);
  background: var(--glass-inverse); box-shadow: inset 0 0 0 1px var(--border-inverse); font-size: 0.8125rem; font-weight: 600; white-space: nowrap;
  animation: svc-quote-chip var(--dur-4) var(--ease-spring) both;
}
.svc-quote__chip b { color: var(--text-inverse-muted); font: 600 0.6875rem/1 var(--font-mono); }
.svc-quote__remove {
  display: grid; place-items: center; width: 1.75rem; height: 1.75rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: transparent; color: var(--text-inverse-muted); transition: background-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out);
}
.svc-quote__remove:hover { background: color-mix(in srgb, var(--text-inverse) 12%, transparent); color: var(--text-inverse); }
.svc-quote__remove svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; }
.svc-quote__total { grid-area: total; display: grid; gap: 0.3125rem; margin: 0; }
.svc-quote__total small { color: var(--text-inverse-muted); font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.12em; text-transform: uppercase; }
.svc-quote__range { display: flex; align-items: flex-start; font: 600 1.375rem/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.svc-quote__dash { padding-inline: 0.3em; color: var(--text-inverse-muted); }
.svc-quote__submit {
  grid-area: submit; display: inline-flex; align-items: center; justify-content: center; gap: var(--space-sm); min-height: 3rem; padding: 0 1.375rem;
  border: 0; border-radius: var(--radius-full); cursor: pointer; white-space: nowrap;
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem var(--font-sans);
  box-shadow: 0 12px 32px -12px color-mix(in srgb, var(--primary) 90%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2) var(--ease-out), color var(--dur-2) var(--ease-out);
}
.svc-quote__submit svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.svc-quote__submit:hover svg { transform: translateX(3px); }
.svc-quote__submit:active { transform: scale(0.97); }
.svc-quote__submit.is-sent { background: var(--success); color: var(--text-inverse); }
.svc-quote :is(.svc-quote__submit, .svc-quote__remove):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* The flying dot (created per flight by JS) */
.svc-quote__flyer {
  position: fixed; top: 0; left: 0; z-index: var(--z-overlay); width: 0.875rem; height: 0.875rem; margin: -0.4375rem 0 0 -0.4375rem;
  border-radius: 50%; pointer-events: none; background: linear-gradient(135deg, var(--primary), var(--primary-2));
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--primary) 18%, transparent), 0 6px 16px -4px color-mix(in srgb, var(--primary) 70%, transparent);
}

.svc-quote__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

@media (prefers-reduced-motion: reduce) {
  .svc-quote *, .svc-quote *::before, .svc-quote *::after { animation: none !important; }
}
@keyframes svc-quote-chip { from { opacity: 0; transform: scale(0.85); } }
```

## JS

```js
// Quote-Builder Service Cards: odometer prices, a dot that flies to the tray, chips, totals and a polite summary.
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const DIGITS = '0\n1\n2\n3\n4\n5\n6\n7\n8\n9';
const money = (n) => `$${n.toLocaleString('en-US')}`;
const span = (className, text = '') => Object.assign(document.createElement('span'), { className, textContent: text });

// Odometer: one sliding 0–9 strip per digit. The rolling copy is aria-hidden; a twin span carries the text.
const odometer = (el) => {
  const twin = span('svc-quote__sr');
  el.after(twin);
  el.setAttribute('aria-hidden', 'true');
  let shape = '';
  return (value, instant = false) => {
    const text = money(value);
    twin.textContent = text;
    if (shape !== text.replace(/\d/g, '0')) {
      shape = text.replace(/\d/g, '0');
      el.replaceChildren(...[...text].map((ch, i) => {
        const digit = /\d/.test(ch);
        const slot = span(digit ? 'svc-quote__digit' : 'svc-quote__glyph', digit ? '' : ch);
        if (digit) slot.append(span('svc-quote__strip', DIGITS));
        slot.style.setProperty('--svc-quote-k', text.length - 1 - i);
        return slot;
      }));
      if (!instant) void el.offsetWidth; // new strips start at 0, so they roll in
    }
    [...text].forEach((ch, i) => /\d/.test(ch) && el.children[i].style.setProperty('--svc-quote-d', ch));
  };
};

document.querySelectorAll('[data-svc-quote]').forEach((root) => {
  const $ = (selector) => root.querySelector(selector);
  const [form, dock, tray, count, chips, live, submit] = ['form', '.svc-quote__dock', '.svc-quote__tray', '.svc-quote__count',
    '.svc-quote__chips', '[data-svc-quote-live]', '.svc-quote__submit'].map($);
  const label = $('.svc-quote__submit-label');
  const [lo, hi] = [...root.querySelectorAll('.svc-quote__range .svc-quote__odo')].map(odometer);
  const css = getComputedStyle(root);
  const token = (name, fallback) => css.getPropertyValue(name).trim() || fallback;
  root.classList.add('svc-quote--js');

  const cards = [...form.querySelectorAll('.svc-quote__card')].map((el) => ({
    el,
    check: el.querySelector('.svc-quote__check'),
    name: el.querySelector('.svc-quote__name').textContent.trim(),
    price: odometer(el.querySelector('.svc-quote__price .svc-quote__odo')),
    size: () => el.querySelector('.svc-quote__size input:checked'),
  }));
  const keyOf = (li) => li.dataset.svcQuoteKey;

  const chipFor = (card) => {
    const li = document.createElement('li');
    li.className = 'svc-quote__chip';
    li.dataset.svcQuoteKey = card.check.value;
    li.innerHTML = '<span></span><b></b><button class="svc-quote__remove" type="button"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>';
    li.firstChild.textContent = card.name;
    li.lastChild.setAttribute('aria-label', `Remove ${card.name}`);
    return li;
  };

  // Rebuild the tray from the form: chips in pick order, count, rolling range, debounced announcement
  let timer = 0;
  const sync = (announce = true) => {
    const picked = cards.filter((card) => card.check.checked);
    const sum = (key) => picked.reduce((total, card) => total + Number(card.size().dataset[key]), 0);
    const [from, to] = [sum('lo'), sum('hi')];
    [...chips.children].forEach((li) => picked.some((card) => card.check.value === keyOf(li)) || li.remove());
    picked.forEach((card) => {
      const li = [...chips.children].find((chip) => keyOf(chip) === card.check.value) || chips.appendChild(chipFor(card));
      li.querySelector('b').textContent = card.size().value.toUpperCase();
    });
    count.textContent = picked.length;
    dock.classList.toggle('is-active', picked.length > 0);
    lo(from);
    hi(to);
    submit.classList.remove('is-sent');
    label.textContent = 'Get my quote';
    clearTimeout(timer);
    if (!announce) return;
    timer = setTimeout(() => {
      live.textContent = picked.length ? `${picked.length} service${picked.length > 1 ? 's' : ''}, ${money(from)} to ${money(to)}` : 'No services selected';
    }, 700);
  };

  const pop = () => count.animate([{ transform: 'none' }, { transform: 'scale(1.35)' }, { transform: 'none' }],
    { duration: parseFloat(token('--dur-4', '0')), easing: token('--ease-out', 'ease-out') });

  // A gradient dot arcs from the checkbox to the badge along a sampled quadratic curve
  const fly = (from) => {
    if (reduce.matches) return;
    const a = from.getBoundingClientRect();
    const b = count.getBoundingClientRect();
    const lift = new DOMMatrix(getComputedStyle(tray).transform).m42; // the tray may still be sliding up
    const [x0, y0, x1, y1] = [a.left + a.width / 2, a.top + a.height / 2, b.left + b.width / 2, b.top + b.height / 2 - lift];
    const [cx, cy] = [(x0 + x1) / 2, Math.min(y0, y1) - 140];
    const frames = Array.from({ length: 17 }, (_, i) => {
      const [t, u] = [i / 16, 1 - i / 16];
      const [x, y] = [u * u * x0 + 2 * u * t * cx + t * t * x1, u * u * y0 + 2 * u * t * cy + t * t * y1];
      return { transform: `translate(${x}px, ${y}px) scale(${1 - 0.4 * t})` };
    });
    const dot = span('svc-quote__flyer');
    dot.setAttribute('aria-hidden', 'true');
    root.append(dot);
    dot.animate(frames, { duration: parseFloat(token('--dur-5', '0')) * 0.8, easing: token('--ease-in-out', 'ease-in-out') })
      .finished.then(pop, () => {}).finally(() => dot.remove());
  };

  form.addEventListener('change', (e) => {
    const card = cards.find((c) => c.el.contains(e.target));
    if (!card) return;
    if (e.target !== card.check) card.price(Number(card.size().dataset.lo));
    sync();
    if (e.target === card.check && card.check.checked) fly(card.check);
  });

  // Removing a chip unticks its card; focus moves to a neighbouring chip, or back to the card
  chips.addEventListener('click', (e) => {
    const li = e.target.closest('.svc-quote__remove')?.closest('li');
    if (!li) return;
    const card = cards.find((c) => c.check.value === keyOf(li));
    const next = li.nextElementSibling || li.previousElementSibling;
    card.check.checked = false;
    sync();
    (next ? next.lastChild : card.check).focus();
  });

  // Demo only: confirm in place. Remove data-svc-quote-demo and the form posts normally.
  form.addEventListener('submit', (e) => {
    if (!('svcQuoteDemo' in form.dataset)) return;
    e.preventDefault();
    submit.classList.add('is-sent');
    label.textContent = 'Quote requested';
    live.textContent = 'Thanks! Your written quote is on its way by email.';
  });

  // Build the odometers without rolling, and reflect any state the browser restored
  cards.forEach((card) => card.price(Number(card.size().dataset.lo), true));
  lo(0, true);
  hi(0, true);
  sync(false);
});
```

## Notes

- One native `<form>` that posts without JS. Each card is a `fieldset` whose legend is the service heading. "Add to quote" is a real checkbox (named "Add to quote: plumbing"), and the label's `::after` stretches over the card so the whole card is its hit area; the size radios and "What's included" link sit above it. Sizes are a native radio group in their own fieldset, so arrow keys work.
- The tray is a `position: sticky` dock at the end of the form, so it rides the bottom of the screen while the cards are in view and parks below the grid afterwards. Chip remove buttons are labelled ("Remove Plumbing") and move focus to a neighbouring chip, or back to the card's checkbox. A polite live region announces "3 services, $424 to $619" 700ms after changes settle; the rolling digits are `aria-hidden`, with text twins.
- Without JS the tray shows a plain line and "Get my quote", and the form posts every tick and size. With JS, `data-svc-quote-demo` confirms in place; delete it to post for real. Under reduced motion there is no flight, chip pop or badge pop, and digits swap instantly because `--dur-5` collapses.
- Odometer digits are `0–9` strips in a one-line window (`1.15em`), moved by `--svc-quote-d` and staggered right to left by `--stagger`. The size pill glides with `:has()` inside `@supports selector(:has(*))`, and older engines fall back to a static dark segment. The selected ring also uses `:has()`; without it the checkbox still shows the state.
- Contrast: muted copy on `--surface-muted` is at least 4.6:1, badge digits (`--text-inverse` on `--primary`) about 5:1, and tray text on `--surface-deep` at least 7:1. Prices live on each size radio as `data-lo`/`data-hi`; change them per market.
