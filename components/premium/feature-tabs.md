# Feature Tabs

Product-tour tabs. A white pill springs between tabs; panels cross-fade with a soft blur; each panel's product mock assembles itself piece by piece. Optional autoplay (`data-autoplay="6000"`) shows a progress line in the active tab, pauses while hovered or focused, stops for good as soon as someone picks a tab, and has its own pause button. Full APG keyboard support. Depends on `tokens/variables.css`.

**Motion:** spring indicator glide · panel cross-fade (opacity + lift + blur) · staggered mock assembly · route fill · "Paid" stamp slam · star sweep · autoplay progress line.

## HTML

```html
<section class="feature-tabs" aria-labelledby="feature-tabs-title" data-feature-tabs data-autoplay="6000">
  <div class="feature-tabs__inner">
    <header class="feature-tabs__head">
      <p class="feature-tabs__eyebrow">The Brand app</p>
      <h2 id="feature-tabs-title" class="feature-tabs__title">Every job, from booking to five stars.</h2>
    </header>

    <div class="feature-tabs__bar">
      <div class="feature-tabs__list" role="tablist" aria-label="App features">
        <span class="feature-tabs__indicator" aria-hidden="true"></span>
        <button class="feature-tabs__tab" role="tab" id="ft-tab-book" aria-selected="true" aria-controls="ft-panel-book" type="button">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /></svg>
          Book<span class="feature-tabs__progress" aria-hidden="true"></span>
        </button>
        <button class="feature-tabs__tab" role="tab" id="ft-tab-track" aria-selected="false" aria-controls="ft-panel-track" type="button" tabindex="-1">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12zM12 12.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5z" /></svg>
          Track<span class="feature-tabs__progress" aria-hidden="true"></span>
        </button>
        <button class="feature-tabs__tab" role="tab" id="ft-tab-pay" aria-selected="false" aria-controls="ft-panel-pay" type="button" tabindex="-1">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M3 7a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 10h18M7 15h3" /></svg>
          Pay<span class="feature-tabs__progress" aria-hidden="true"></span>
        </button>
        <button class="feature-tabs__tab" role="tab" id="ft-tab-review" aria-selected="false" aria-controls="ft-panel-review" type="button" tabindex="-1">
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z" /></svg>
          Review<span class="feature-tabs__progress" aria-hidden="true"></span>
        </button>
      </div>
      <button class="feature-tabs__play" type="button" aria-label="Pause autoplay" aria-pressed="false" hidden>
        <svg class="feature-tabs__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
        <svg class="feature-tabs__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
      </button>
    </div>

    <div class="feature-tabs__panels">
      <div class="feature-tabs__panel is-active" role="tabpanel" id="ft-panel-book" aria-labelledby="ft-tab-book" tabindex="0">
        <div class="feature-tabs__copy">
          <h3>Book in under a minute</h3>
          <p>Pick a day and a two-hour window that suits you. Confirmation and a reminder arrive by text.</p>
          <ul role="list"><li>Same-day slots shown first</li><li>Free rescheduling up to 2 hours before</li></ul>
        </div>
        <div class="feature-tabs__visual" aria-hidden="true">
          <div class="feature-tabs__mock">
            <div class="feature-tabs__mock-head" style="--i: 0"><strong>October</strong><span>Pick a day</span></div>
            <div class="feature-tabs__days" style="--i: 1"><span>Mo<b>13</b></span><span>Tu<b>14</b></span><span class="is-picked">We<b>15</b></span><span>Th<b>16</b></span><span>Fr<b>17</b></span></div>
            <div class="feature-tabs__slots" style="--i: 2"><span>8–10</span><span class="is-picked">10–12</span><span>12–2</span><span>2–4</span></div>
            <div class="feature-tabs__mock-cta" style="--i: 3">Confirm · Wed 15, 10–12</div>
          </div>
        </div>
      </div>

      <div class="feature-tabs__panel" role="tabpanel" id="ft-panel-track" aria-labelledby="ft-tab-track" tabindex="0">
        <div class="feature-tabs__copy">
          <h3>Know exactly when we'll arrive</h3>
          <p>Watch your technician's live ETA, see who's coming and get a text when they're five minutes out.</p>
          <ul role="list"><li>Photo and licence of your technician</li><li>Live map from dispatch to your door</li></ul>
        </div>
        <div class="feature-tabs__visual feature-tabs__visual--alt" aria-hidden="true">
          <div class="feature-tabs__mock">
            <div class="feature-tabs__tech" style="--i: 0"><span class="feature-tabs__avatar">SK</span><span><strong>Sam K.</strong><small>Licensed plumber · 4.9 ★</small></span><span class="feature-tabs__eta">12 min</span></div>
            <div class="feature-tabs__route" style="--i: 1"><span></span></div>
            <ol class="feature-tabs__steps" style="--i: 2"><li class="is-done">Booked</li><li class="is-done">On the way</li><li>Arrived</li></ol>
          </div>
        </div>
      </div>

      <div class="feature-tabs__panel" role="tabpanel" id="ft-panel-pay" aria-labelledby="ft-tab-pay" tabindex="0">
        <div class="feature-tabs__copy">
          <h3>Pay the price you were quoted</h3>
          <p>An itemised invoice lands the moment the job's done. Pay by card or Apple Pay in one tap.</p>
          <ul role="list"><li>Matches your written quote, line by line</li><li>Receipts saved for warranty claims</li></ul>
        </div>
        <div class="feature-tabs__visual" aria-hidden="true">
          <div class="feature-tabs__mock">
            <div class="feature-tabs__mock-head" style="--i: 0"><strong>Invoice #1042</strong><span>Leak repair</span></div>
            <dl class="feature-tabs__lines" style="--i: 1"><div><dt>Labour</dt><dd>$120</dd></div><div><dt>Parts</dt><dd>$29</dd></div><div class="is-total"><dt>Total</dt><dd>$149</dd></div></dl>
            <div class="feature-tabs__mock-cta" style="--i: 2">Pay $149</div>
            <span class="feature-tabs__stamp">Paid</span>
          </div>
        </div>
      </div>

      <div class="feature-tabs__panel" role="tabpanel" id="ft-panel-review" aria-labelledby="ft-tab-review" tabindex="0">
        <div class="feature-tabs__copy">
          <h3>Tell us how we did</h3>
          <p>Rate the visit in two taps. Every review is read by a real person, and every issue gets a call back.</p>
          <ul role="list"><li>Reviews published unedited</li><li>Problems fixed under guarantee</li></ul>
        </div>
        <div class="feature-tabs__visual feature-tabs__visual--alt" aria-hidden="true">
          <div class="feature-tabs__mock">
            <div class="feature-tabs__mock-head" style="--i: 0"><strong>How did Sam do?</strong><span>Leak repair · Today</span></div>
            <div class="feature-tabs__rate" style="--i: 1"><span>★★★★★</span>★★★★★</div>
            <p class="feature-tabs__quote" style="--i: 2">"Quick, tidy and explained everything."</p>
            <div class="feature-tabs__mock-cta" style="--i: 3">Post review</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section and heading */
.feature-tabs { background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans); }
.feature-tabs__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.feature-tabs__head { max-width: 40rem; margin: 0 auto 2.5rem; text-align: center; }
.feature-tabs__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.feature-tabs__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }

/* Tab bar: pill track, a white indicator springs between tabs */
.feature-tabs__bar { display: flex; justify-content: center; align-items: center; gap: 0.75rem; margin-bottom: 3rem; }
.feature-tabs:not(.feature-tabs--js) .feature-tabs__bar { display: none; }
.feature-tabs__list {
  position: relative; display: flex; gap: 0.25rem; max-width: 100%; padding: 0.3125rem; overflow-x: auto; scrollbar-width: none;
  border-radius: 999px; background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
}
.feature-tabs__list::-webkit-scrollbar { display: none; }
.feature-tabs__indicator {
  position: absolute; top: 0.3125rem; bottom: 0.3125rem; left: 0; width: var(--w, 0); transform: translateX(var(--x, 0));
  border-radius: 999px; background: var(--surface-light); box-shadow: var(--shadow-md), inset 0 0 0 1px var(--border-subtle);
  transition: transform var(--dur-4) var(--ease-spring), width var(--dur-4) var(--ease-spring);
}
.feature-tabs__tab {
  position: relative; z-index: 1; flex: none; display: inline-flex; align-items: center; gap: 0.5rem;
  height: 2.75rem; padding: 0 1.125rem; border: 0; border-radius: 999px; background: transparent; cursor: pointer;
  color: var(--text-muted); font: 600 0.9375rem/1 var(--font-sans); white-space: nowrap; transition: color var(--dur-3);
}
.feature-tabs__tab svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: color var(--dur-3), transform var(--dur-4) var(--ease-spring); }
.feature-tabs__tab:hover { color: var(--text-main); }
.feature-tabs__tab[aria-selected="true"] { color: var(--text-main); }
.feature-tabs__tab[aria-selected="true"] svg { color: var(--primary); transform: scale(1.1); }
.feature-tabs__tab:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }

/* Autoplay progress line inside the active tab */
.feature-tabs__progress { position: absolute; left: 1.125rem; right: 1.125rem; bottom: 0.375rem; height: 2px; overflow: hidden; border-radius: 2px; }
.feature-tabs__progress::after { content: ""; position: absolute; inset: 0; background: var(--gradient-brand); transform: scaleX(0); transform-origin: left; }
.feature-tabs--playing .feature-tabs__tab[aria-selected="true"] .feature-tabs__progress { background: color-mix(in srgb, var(--text-main) 10%, transparent); }
.feature-tabs--playing .feature-tabs__tab[aria-selected="true"] .feature-tabs__progress::after { animation: feature-tabs-progress var(--feature-tabs-duration, 6s) linear forwards; }
.feature-tabs--playing:is(:hover, :focus-within) .feature-tabs__tab[aria-selected="true"] .feature-tabs__progress::after { animation-play-state: paused; }
.feature-tabs__play {
  flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-muted); color: var(--text-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); transition: color var(--dur-2);
}
.feature-tabs__play:hover { color: var(--text-main); }
.feature-tabs__play:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.feature-tabs__play[hidden] { display: none; }
.feature-tabs__play svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.feature-tabs__icon-play, .feature-tabs__play[aria-pressed="true"] .feature-tabs__icon-pause { display: none; }
.feature-tabs__play[aria-pressed="true"] .feature-tabs__icon-play { display: block; }

/* Panels: stacked sections without JS; one grid cell cross-fading with JS */
.feature-tabs__panels { display: grid; gap: 4rem; }
.feature-tabs__panel { display: grid; gap: 2.5rem; align-items: center; border-radius: var(--radius-2xl); }
.feature-tabs__panel:focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
@media (min-width: 900px) { .feature-tabs__panel { grid-template-columns: 0.85fr 1.15fr; gap: 4rem; } }
.feature-tabs--js .feature-tabs__panel {
  grid-area: 1 / 1; opacity: 0; transform: translateY(16px) scale(0.985); filter: blur(6px); visibility: hidden;
  transition: opacity var(--dur-4) var(--ease-out), transform var(--dur-4) var(--ease-out), filter var(--dur-4) var(--ease-out), visibility 0s linear var(--dur-4);
}
.feature-tabs--js .feature-tabs__panel.is-active { opacity: 1; transform: none; filter: none; visibility: visible; transition-delay: 0s; }

/* Copy column */
.feature-tabs__copy h3 { margin: 0; font: 600 clamp(1.5rem, 1.2rem + 1.2vw, 2rem)/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.feature-tabs__copy p { margin: 1rem 0 0; max-width: 30rem; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.feature-tabs__copy ul { display: grid; gap: 0.625rem; margin: 1.5rem 0 0; padding: 0; list-style: none; }
.feature-tabs__copy li { position: relative; padding-left: 1.75rem; font-weight: 500; }
.feature-tabs__copy li::before { content: ""; position: absolute; left: 0; top: 0.125rem; width: 1.125rem; height: 1.125rem; border-radius: 50%; background: color-mix(in srgb, var(--primary) 12%, transparent); }
.feature-tabs__copy li::after { content: ""; position: absolute; left: 0.4375rem; top: 0.3125rem; width: 0.25rem; height: 0.5rem; border: solid var(--primary); border-width: 0 2px 2px 0; transform: rotate(45deg); }

/* Visual: dark art board with a white product mock */
.feature-tabs__visual {
  display: grid; place-items: center; min-height: 22rem; padding: 2rem 1.25rem; border-radius: var(--radius-2xl); overflow: hidden;
  background:
    radial-gradient(70% 60% at 85% 10%, color-mix(in srgb, var(--primary-2) 55%, transparent), transparent 65%),
    radial-gradient(70% 70% at 10% 90%, color-mix(in srgb, var(--primary) 60%, transparent), transparent 65%),
    var(--surface-deep);
}
.feature-tabs__visual--alt {
  background:
    radial-gradient(70% 60% at 15% 10%, color-mix(in srgb, var(--primary) 55%, transparent), transparent 65%),
    radial-gradient(70% 70% at 90% 90%, color-mix(in srgb, var(--primary-2) 55%, transparent), transparent 65%),
    var(--surface-deep);
}
.feature-tabs__mock {
  position: relative; display: grid; gap: 1rem; width: min(100%, 22rem); padding: 1.25rem; border-radius: 1.25rem;
  background: var(--surface-light); color: var(--text-main);
  box-shadow: 0 30px 60px -20px color-mix(in srgb, var(--surface-deep) 90%, transparent), var(--highlight);
}
.feature-tabs__panel.is-active .feature-tabs__mock > * { animation: feature-tabs-in var(--dur-4) var(--ease-out) calc(var(--i, 0) * 80ms + 120ms) both; }
.feature-tabs__mock-head { display: flex; justify-content: space-between; align-items: baseline; gap: 1rem; }
.feature-tabs__mock-head strong { font: 600 1rem var(--font-display); }
.feature-tabs__mock-head span { color: var(--text-muted); font-size: 0.75rem; }
.feature-tabs__mock-cta { display: grid; place-items: center; height: 2.75rem; border-radius: 0.875rem; background: var(--text-main); color: var(--surface-light); font-size: 0.875rem; font-weight: 600; }

/* Mock: calendar */
.feature-tabs__days { display: grid; grid-template-columns: repeat(5, 1fr); gap: 0.375rem; }
.feature-tabs__days span { display: grid; justify-items: center; gap: 0.125rem; padding: 0.5rem 0; border-radius: 0.75rem; background: var(--surface-muted); color: var(--text-muted); font-size: 0.6875rem; }
.feature-tabs__days b { color: var(--text-main); font: 600 1rem var(--font-display); }
.feature-tabs__slots { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0.375rem; }
.feature-tabs__slots span { padding: 0.5rem 0; border-radius: 0.625rem; box-shadow: inset 0 0 0 1px var(--border-subtle); text-align: center; font-size: 0.75rem; font-weight: 600; }
.feature-tabs__days .is-picked, .feature-tabs__slots .is-picked { background: var(--primary); color: var(--text-inverse); box-shadow: 0 8px 18px -8px var(--primary); }
.feature-tabs__days .is-picked b { color: var(--text-inverse); }
.feature-tabs__panel.is-active .is-picked { animation: feature-tabs-pick var(--dur-4) var(--ease-spring) 700ms both; }

/* Mock: tracking */
.feature-tabs__tech { display: flex; align-items: center; gap: 0.75rem; }
.feature-tabs__tech strong { display: block; font-size: 0.875rem; }
.feature-tabs__tech small { color: var(--text-muted); font-size: 0.75rem; }
.feature-tabs__avatar { display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 0.875rem; background: var(--gradient-brand); color: var(--text-inverse); font-size: 0.75rem; font-weight: 700; }
.feature-tabs__eta { margin-left: auto; padding: 0.25rem 0.5rem; border-radius: 999px; background: color-mix(in srgb, var(--success) 14%, transparent); color: var(--success); font-size: 0.75rem; font-weight: 700; }
.feature-tabs__route { height: 0.5rem; border-radius: 999px; background: var(--surface-muted); overflow: hidden; }
.feature-tabs__route span { display: block; width: 68%; height: 100%; border-radius: inherit; background: var(--gradient-brand); transform-origin: left; }
.feature-tabs__panel.is-active .feature-tabs__route span { animation: feature-tabs-grow calc(var(--dur-5) * 1.6) var(--ease-out) 400ms both; }
.feature-tabs__steps { display: flex; justify-content: space-between; margin: 0; padding: 0; list-style: none; color: var(--text-muted); font-size: 0.75rem; }
.feature-tabs__steps .is-done { color: var(--text-main); font-weight: 600; }

/* Mock: invoice with a stamp */
.feature-tabs__lines { display: grid; gap: 0.5rem; margin: 0; }
.feature-tabs__lines div { display: flex; justify-content: space-between; font-size: 0.875rem; }
.feature-tabs__lines dt { color: var(--text-muted); }
.feature-tabs__lines dd { margin: 0; font-weight: 600; font-variant-numeric: tabular-nums; }
.feature-tabs__lines .is-total { padding-top: 0.5rem; border-top: 1px dashed var(--border-subtle); font-size: 1rem; }
.feature-tabs__lines .is-total dt { color: var(--text-main); font-weight: 600; }
.feature-tabs__stamp {
  position: absolute; right: 1.25rem; top: 3.5rem; padding: 0.25rem 0.75rem; border: 2px solid var(--success); border-radius: 0.5rem;
  color: var(--success); font: 700 1.25rem/1 var(--font-display); letter-spacing: 0.08em; text-transform: uppercase; transform: rotate(-12deg);
}
.feature-tabs__panel.is-active .feature-tabs__stamp { animation: feature-tabs-stamp var(--dur-4) var(--ease-spring) 900ms both; }

/* Mock: review */
.feature-tabs__rate { position: relative; justify-self: start; color: var(--border-subtle); font-size: 1.75rem; letter-spacing: 0.12em; }
.feature-tabs__rate span { position: absolute; inset: 0 auto 0 0; width: 100%; overflow: hidden; color: var(--accent); white-space: nowrap; }
.feature-tabs__panel.is-active .feature-tabs__rate span { animation: feature-tabs-grow var(--dur-5) var(--ease-out) 450ms both; transform-origin: left; }
.feature-tabs__quote { margin: 0; padding: 0.75rem; border-radius: 0.75rem; background: var(--surface-muted); color: var(--text-muted); font-size: 0.875rem; }

@media (prefers-reduced-motion: reduce) {
  .feature-tabs__panel *, .feature-tabs__panel *::before, .feature-tabs__panel *::after { animation: none !important; }
}
@keyframes feature-tabs-progress { to { transform: scaleX(1); } }
@keyframes feature-tabs-in { from { opacity: 0; transform: translateY(10px); filter: blur(4px); } }
@keyframes feature-tabs-pick { 0% { transform: scale(1); } 40% { transform: scale(0.9); } 100% { transform: scale(1); } }
@keyframes feature-tabs-grow { from { transform: scaleX(0); } }
@keyframes feature-tabs-stamp { from { opacity: 0; transform: rotate(-12deg) scale(1.8); } }
```

## JS

```js
document.querySelectorAll('[data-feature-tabs]').forEach((root) => {
  const list = root.querySelector('[role="tablist"]');
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const panels = tabs.map((tab) => document.getElementById(tab.getAttribute('aria-controls')));
  const indicator = root.querySelector('.feature-tabs__indicator');
  const play = root.querySelector('.feature-tabs__play');
  const delay = Number(root.dataset.autoplay) || 0;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let current = Math.max(0, tabs.findIndex((tab) => tab.getAttribute('aria-selected') === 'true'));
  root.classList.add('feature-tabs--js');
  root.style.setProperty('--feature-tabs-duration', `${delay}ms`);

  // Glide the indicator to the active tab; keep that tab scrolled into the bar (never the page)
  const moveIndicator = (instant) => {
    const tab = tabs[current];
    if (instant) indicator.style.transition = 'none';
    indicator.style.setProperty('--x', `${tab.offsetLeft}px`);
    indicator.style.setProperty('--w', `${tab.offsetWidth}px`);
    if (instant) { void indicator.offsetWidth; indicator.style.transition = ''; }
    list.scrollTo({ left: tab.offsetLeft - (list.clientWidth - tab.offsetWidth) / 2, behavior: reduce || instant ? 'auto' : 'smooth' });
  };

  // Activate a tab: ARIA state, roving tabindex, panel swap (inactive panels are inert)
  const select = (index, focus) => {
    current = (index + tabs.length) % tabs.length;
    tabs.forEach((tab, n) => {
      const on = n === current;
      tab.setAttribute('aria-selected', String(on));
      tab.tabIndex = on ? 0 : -1;
      panels[n].classList.toggle('is-active', on);
      panels[n].inert = !on;
    });
    if (focus) tabs[current].focus();
    moveIndicator();
  };

  // Autoplay: the progress line's animationend advances; hover/focus pause it in CSS
  const setPlaying = (on) => {
    root.classList.toggle('feature-tabs--playing', on);
    play.setAttribute('aria-pressed', String(!on));
  };
  if (delay && !reduce) { play.hidden = false; setPlaying(true); }
  root.addEventListener('animationend', (e) => {
    if (e.animationName === 'feature-tabs-progress' && root.classList.contains('feature-tabs--playing')) select(current + 1);
  });
  play.addEventListener('click', () => setPlaying(!root.classList.contains('feature-tabs--playing')));

  // Choosing a tab stops autoplay for good; arrows/Home/End move with automatic activation
  tabs.forEach((tab, i) => tab.addEventListener('click', () => { setPlaying(false); select(i); }));
  list.addEventListener('keydown', (e) => {
    const keys = { ArrowRight: current + 1, ArrowLeft: current - 1, Home: 0, End: tabs.length - 1 };
    if (!(e.key in keys)) return;
    e.preventDefault();
    setPlaying(false);
    select(keys[e.key], true);
  });
  new ResizeObserver(() => moveIndicator(true)).observe(list);
  select(current);
});
```

## Notes

- APG tabs with automatic activation: ←/→ move and select, Home/End jump, and Tab moves into the panel. Inactive panels are `inert`, so they're out of the tab order and the accessibility tree while hidden.
- Without JS, the tab bar is hidden and every panel shows as a stacked section with its own heading. Nothing is lost.
- Autoplay meets WCAG 2.2.2: a visible pause button, a pause on hover or focus, and it stops permanently once someone chooses a tab. It never runs under reduced motion.
- The mocks are decorative HTML/CSS (`aria-hidden`); replace `.feature-tabs__visual` contents with screenshots if you have them.
- The indicator measures the tabs, so labels can be any length; on narrow screens the bar scrolls sideways and keeps the active tab centred.
