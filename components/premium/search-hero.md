# Ask-Anything Hero

A light, airy hero built around one giant question: "What needs fixing?". Inside the field, a decorative overlay types and deletes real problems ("AC blowing warm air…") with a caret, three times, then rests on the last; focus wraps the field in a conic-gradient border that draws itself around it. Typing opens an APG combobox of matched services with price ranges and "Earliest" slot chips, and popular-service chips fill the field on tap. On phones the submit collapses to an arrow, options wrap their slot chip under the name, and the floating side cards drop away. Depends on `tokens/variables.css`.

**Motion:** blobs bloom in, copy and field rise in sequence (`--dur-5`, `--ease-out`, `--stagger`) · typed suggestions with a blinking caret (JS, about 9s, then rests) · focus border wraps and turns once (`@property` sweep + angle, `--ease-out`) · listbox enters via `@starting-style` (`--dur-3`) · chips press with `--ease-spring`. A pause button stops the typing; it freezes off-screen too.

## HTML

```html
<section class="ask-hero" aria-labelledby="ask-hero-title" data-ask-hero>
  <div class="ask-hero__bg" aria-hidden="true">
    <span class="ask-hero__blob ask-hero__blob--1"></span>
    <span class="ask-hero__blob ask-hero__blob--2"></span>
    <span class="ask-hero__blob ask-hero__blob--3"></span>
  </div>

  <div class="ask-hero__inner">
    <p class="ask-hero__eyebrow" style="--ask-hero-i: 0"><span class="ask-hero__dot" aria-hidden="true"></span>14 pros available today in Springfield</p>
    <h1 id="ask-hero-title" class="ask-hero__title" style="--ask-hero-i: 1">
      <label for="ask-hero-q">What needs <span class="ask-hero__grad">fixing?</span></label>
    </h1>
    <p class="ask-hero__lead" style="--ask-hero-i: 2">Describe it in your own words. We'll match a licensed pro, show an upfront price range and the earliest slot, usually today.</p>

    <form class="ask-hero__form" action="/search" method="get" role="search" aria-label="Find a service" style="--ask-hero-i: 3">
      <div class="ask-hero__field">
        <svg class="ask-hero__glass" viewBox="0 0 24 24" width="22" height="22" aria-hidden="true" focusable="false"><path d="M11 18a7 7 0 1 0 0-14 7 7 0 0 0 0 14zM20 20l-4-4" /></svg>
        <div class="ask-hero__control">
          <input class="ask-hero__input" id="ask-hero-q" name="q" type="text" list="ask-hero-services"
            role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="ask-hero-list"
            autocomplete="off" enterkeyhint="search" spellcheck="false">
          <span class="ask-hero__ghost" aria-hidden="true" data-ask-hero-lines="AC blowing warm air…|Water heater leaking…|Breaker keeps tripping…"><span class="ask-hero__ghost-text"></span><span class="ask-hero__caret"></span></span>
        </div>
        <button class="ask-hero__pause" type="button" aria-pressed="false" aria-label="Pause typing animation" hidden>
          <svg class="ask-hero__icon-pause" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M8 5v14M16 5v14" /></svg>
          <svg class="ask-hero__icon-play" viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="M7 5l12 7-12 7z" /></svg>
        </button>
        <button class="ask-hero__submit" type="submit">
          <span class="ask-hero__submit-label">Find a pro</span>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </button>
        <ul class="ask-hero__list" id="ask-hero-list" role="listbox" aria-label="Matching services" hidden></ul>
      </div>
      <p class="ask-hero__status" role="status"></p>

      <div class="ask-hero__chips">
        <span class="ask-hero__chips-label">Popular</span>
        <button class="ask-hero__chip" type="submit" name="service" value="AC repair" style="--ask-hero-c: 0"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 2v20M3.3 7l17.4 10M3.3 17 20.7 7M9 4l3 2 3-2M9 20l3-2 3 2" /></svg>AC repair</button>
        <button class="ask-hero__chip" type="submit" name="service" value="Water heater repair" style="--ask-hero-c: 1"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 3s6 6.2 6 11a6 6 0 0 1-12 0c0-4.8 6-11 6-11z" /></svg>Water heater</button>
        <button class="ask-hero__chip" type="submit" name="service" value="Drain cleaning" style="--ask-hero-c: 2"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z" /></svg>Drain cleaning</button>
        <button class="ask-hero__chip" type="submit" name="service" value="Electrical troubleshooting" style="--ask-hero-c: 3"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg>Electrical</button>
        <button class="ask-hero__chip" type="submit" name="service" value="Roof leak repair" style="--ask-hero-c: 4"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M3 11 12 4l9 7M5 10v10h14V10M10 20v-6h4v6" /></svg>Roof leak</button>
      </div>
    </form>

    <div class="ask-hero__foot" style="--ask-hero-i: 5">
      <a class="ask-hero__call" href="tel:+15555550123">
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" /></svg>
        Rather talk? (555) 555-0123
      </a>
      <p class="ask-hero__proof">
        <span class="ask-hero__faces" aria-hidden="true"><span>JM</span><span>AK</span><span>RS</span></span>
        <span><strong>4.9/5</strong> from 2,300 Springfield reviews</span>
      </p>
    </div>

    <div class="ask-hero__float ask-hero__float--left" aria-hidden="true">
      <span class="ask-hero__float-avatar">SK</span>
      <span><strong>Sam K. is on the way</strong><small>Licensed plumber · 12 min</small></span>
    </div>
    <div class="ask-hero__float ask-hero__float--right" aria-hidden="true">
      <small>Upfront quote</small>
      <strong>Water heater repair</strong>
      <span class="ask-hero__float-price">$149–$389</span>
      <span class="ask-hero__slot">Earliest: Today 4–6pm</span>
    </div>
  </div>

  <datalist id="ask-hero-services">
    <option value="AC repair" data-icon="snow" data-price="$89–$249" data-slot="Today 2–4pm" data-keys="ac air conditioner conditioning cooling warm blowing hot"></option>
    <option value="Water heater repair" data-icon="drop" data-price="$149–$389" data-slot="Today 4–6pm" data-keys="water heater leaking leak tank hot cold"></option>
    <option value="Electrical troubleshooting" data-icon="bolt" data-price="$99–$229" data-slot="Today 2–4pm" data-keys="breaker keeps tripping trips outlet power sparks lights flicker electric"></option>
    <option value="Panel upgrade" data-icon="bolt" data-price="$1,200–$2,800" data-slot="Thu 9–11am" data-keys="panel breaker box fuse amp upgrade electric"></option>
    <option value="Drain cleaning" data-icon="wrench" data-price="$119–$279" data-slot="Today 4–6pm" data-keys="drain clog clogged blocked sink shower toilet slow"></option>
    <option value="Roof leak repair" data-icon="home" data-price="$249–$690" data-slot="Tomorrow 8–10am" data-keys="roof leak leaking ceiling stain shingles water"></option>
    <option value="Furnace repair" data-icon="flame" data-price="$129–$349" data-slot="Today 6–8pm" data-keys="furnace heating heat cold no pilot boiler"></option>
    <option value="Lock change" data-icon="key" data-price="$79–$189" data-slot="Today 2–4pm" data-keys="lock locked out key door rekey deadbolt"></option>
  </datalist>

  <template class="ask-hero__tpl">
    <li class="ask-hero__option" role="option" aria-selected="false">
      <span class="ask-hero__opt-icon"></span>
      <span class="ask-hero__opt-main"><span class="ask-hero__opt-name"></span><span class="ask-hero__opt-price"></span></span>
      <span class="ask-hero__slot"></span>
    </li>
    <svg data-icon="snow" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 2v20M3.3 7l17.4 10M3.3 17 20.7 7M9 4l3 2 3-2M9 20l3-2 3 2" /></svg>
    <svg data-icon="drop" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 3s6 6.2 6 11a6 6 0 0 1-12 0c0-4.8 6-11 6-11z" /></svg>
    <svg data-icon="bolt" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M13 2 4 14h7l-1 8 9-12h-7z" /></svg>
    <svg data-icon="wrench" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z" /></svg>
    <svg data-icon="home" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M3 11 12 4l9 7M5 10v10h14V10M10 20v-6h4v6" /></svg>
    <svg data-icon="flame" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 22a7 7 0 0 0 7-7c0-4-3-6-4-10-2 2-3 4-3 6-1-1-2-2-2-4-3 3-5 5-5 8a7 7 0 0 0 7 7z" /></svg>
    <svg data-icon="key" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M7.5 20a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9zM10.7 12.3 20 3M16 7l3 3M14 9l2 2" /></svg>
    <svg data-icon="chat" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z" /></svg>
  </template>
</section>
```

## CSS

```css
@property --ask-hero-sweep { syntax: "<percentage>"; inherits: true; initial-value: 100%; }
@property --ask-hero-angle { syntax: "<angle>"; inherits: true; initial-value: 0deg; }

/* Section: white paper with a dot pattern and soft colour blooms */
.ask-hero {
  --ask-hero-muted: color-mix(in srgb, var(--text-muted) 70%, var(--text-main)); /* holds 4.5:1 on the tinted blooms */
  --ask-hero-ok: color-mix(in srgb, var(--success) 80%, var(--text-main));
  --ask-hero-in: 120ms;
  position: relative; isolation: isolate; overflow: clip;
  background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
}
.ask-hero__bg { position: absolute; inset: 0; z-index: -1; pointer-events: none; }
.ask-hero__bg::before {
  content: ""; position: absolute; inset: 0;
  background-image: radial-gradient(color-mix(in srgb, var(--text-main) 16%, transparent) 1px, transparent 1.6px);
  background-size: 22px 22px;
  -webkit-mask-image: radial-gradient(ellipse 75% 70% at 50% 40%, black 30%, transparent 85%);
  mask-image: radial-gradient(ellipse 75% 70% at 50% 40%, black 30%, transparent 85%);
}
.ask-hero__blob { position: absolute; width: 46rem; aspect-ratio: 1; border-radius: 50%; animation: ask-hero-bloom calc(var(--dur-5) * 2) var(--ease-out) backwards; }
.ask-hero__blob--1 { top: -24rem; left: -18rem; background: radial-gradient(closest-side, color-mix(in srgb, var(--primary) 22%, transparent), transparent); }
.ask-hero__blob--2 { top: -22rem; right: -20rem; background: radial-gradient(closest-side, color-mix(in srgb, var(--primary-2) 22%, transparent), transparent); animation-delay: 120ms; }
.ask-hero__blob--3 { bottom: -34rem; left: 50%; width: 64rem; translate: -50% 0; background: radial-gradient(closest-side, color-mix(in srgb, var(--accent) 18%, transparent), transparent); animation-delay: 240ms; }

/* Layout and entrance (backwards fill: no lingering transforms, so the listbox can overlap what follows) */
.ask-hero__inner {
  position: relative; display: flex; flex-direction: column; align-items: center; text-align: center;
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4rem, 12vw, 8rem) var(--gutter) clamp(4rem, 10vw, 6.5rem);
}
.ask-hero__eyebrow, .ask-hero__title, .ask-hero__lead, .ask-hero__form, .ask-hero__foot {
  animation: ask-hero-rise var(--dur-5) var(--ease-out) calc(var(--ask-hero-in) + var(--ask-hero-i) * var(--stagger) * 2) backwards;
}
.ask-hero__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.875rem 0.375rem 0.75rem; border-radius: var(--radius-full);
  background: var(--glass); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
  color: var(--ask-hero-muted); font-size: 0.8125rem; font-weight: 500;
}
.ask-hero__dot { flex: none; width: 0.5rem; height: 0.5rem; border-radius: 50%; background: var(--success); box-shadow: 0 0 0 3px color-mix(in srgb, var(--success) 22%, transparent); }
.ask-hero__title {
  max-width: 11ch; margin: 1.5rem 0 0; font: 600 clamp(2.75rem, 1.3rem + 6vw, 5.75rem)/0.98 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.ask-hero__title label { cursor: text; }
.ask-hero__grad {
  display: inline-block; padding-bottom: 0.06em;
  background: linear-gradient(100deg, var(--primary) 10%, color-mix(in srgb, var(--primary) 45%, var(--primary-2)) 60%, var(--primary-2));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.ask-hero__lead { max-width: 34rem; margin: 1.25rem 0 0; color: var(--ask-hero-muted); font-size: clamp(1.0625rem, 1rem + 0.35vw, 1.25rem); line-height: 1.6; text-wrap: pretty; }

/* The giant field. Focus wraps it in a conic gradient that draws itself around, then rests */
.ask-hero__form { position: relative; z-index: 2; width: 100%; max-width: 44rem; margin-top: 2.25rem; }
.ask-hero__field {
  position: relative; display: flex; align-items: center; gap: 0.375rem;
  min-height: 4rem; padding: 0.375rem; padding-inline-start: 1rem;
  border: 2px solid transparent; border-radius: var(--radius-2xl);
  background: linear-gradient(var(--surface-light), var(--surface-light)) padding-box, linear-gradient(var(--border-subtle), var(--border-subtle)) border-box;
  box-shadow: var(--highlight), var(--shadow-xl);
  transition: box-shadow var(--dur-3) var(--ease-out);
}
.ask-hero__field::before { /* soft aura behind the field, visible on focus */
  content: ""; position: absolute; inset: -2px; z-index: -1; border-radius: inherit; pointer-events: none;
  background: conic-gradient(from var(--ask-hero-angle), var(--primary), var(--primary-2), var(--primary));
  filter: blur(20px); opacity: 0; transition: opacity var(--dur-4) var(--ease-out);
}
.ask-hero__field:has(.ask-hero__input:focus) {
  background:
    linear-gradient(var(--surface-light), var(--surface-light)) padding-box,
    conic-gradient(from var(--ask-hero-angle), var(--primary), var(--primary-2) calc(var(--ask-hero-sweep) * 0.5), var(--primary) var(--ask-hero-sweep), var(--border-subtle) 0) border-box;
  box-shadow: 0 0 0 5px color-mix(in srgb, var(--primary) 10%, transparent), var(--shadow-xl);
  animation: ask-hero-wrap calc(var(--dur-5) * 1.8) var(--ease-out);
}
.ask-hero__field:has(.ask-hero__input:focus)::before { opacity: 0.3; }
.ask-hero__glass { flex: none; display: none; fill: none; stroke: var(--text-muted); stroke-width: 2; stroke-linecap: round; }
.ask-hero__control { position: relative; display: flex; flex: 1; min-width: 0; align-self: stretch; }
.ask-hero__input {
  flex: 1; min-width: 0; padding: 0 0.25rem; border: 0; background: transparent;
  color: var(--text-main); font: 500 1.0625rem/1.4 var(--font-sans);
}
.ask-hero__input:focus-visible { outline: 2px solid var(--primary); outline-offset: 0.5rem; }
@supports selector(:has(*)) { .ask-hero__input:focus-visible { outline: none; } }

/* Typed suggestions: aria-hidden overlay, end-aligned once it overflows so the caret stays in view */
.ask-hero__ghost {
  position: absolute; inset: 0 0.25rem; display: flex; align-items: center; justify-content: flex-end; overflow: hidden; pointer-events: none;
  color: var(--text-muted); font: 500 1.0625rem/1.4 var(--font-sans); white-space: nowrap;
  transition: opacity var(--dur-2) var(--ease-out);
}
.ask-hero__ghost::after { content: ""; flex: 1 0 0; }
.ask-hero__ghost-text { flex: none; }
.ask-hero__ghost:not(.is-typing) .ask-hero__ghost-text { flex: 0 1 auto; min-width: 0; overflow: hidden; text-overflow: ellipsis; } /* at rest: start-aligned, truncated */
.ask-hero__caret { display: none; flex: none; width: 2px; height: 1.3em; margin-left: 1px; border-radius: 1px; background: var(--primary); }
.ask-hero__ghost.is-typing .ask-hero__caret { display: block; animation: ask-hero-blink 1s steps(1) infinite; }
.ask-hero__ghost.is-paused .ask-hero__caret, .ask-hero[data-offscreen] .ask-hero__caret { animation-play-state: paused; }
.ask-hero:not(.ask-hero--js) .ask-hero__ghost { display: none; }
.ask-hero__control:focus-within .ask-hero__ghost, .ask-hero__control.is-filled .ask-hero__ghost { opacity: 0; }

/* Pause (only while typing) and submit */
.ask-hero__pause {
  flex: none; display: grid; place-items: center; width: 2rem; height: 2rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-muted); color: var(--text-muted); box-shadow: inset 0 0 0 1px var(--border-subtle);
  transition: color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.ask-hero__pause:hover { color: var(--text-main); }
.ask-hero__pause:active { transform: scale(0.9); }
.ask-hero__pause[hidden] { display: none; }
.ask-hero__pause svg { fill: currentColor; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.ask-hero__icon-play, .ask-hero__pause[aria-pressed="true"] .ask-hero__icon-pause { display: none; }
.ask-hero__pause[aria-pressed="true"] .ask-hero__icon-play { display: block; }
.ask-hero__submit {
  flex: none; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
  min-width: 2.75rem; height: 2.75rem; padding: 0 0.75rem; border: 0; border-radius: calc(var(--radius-2xl) - 0.375rem); cursor: pointer;
  background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font: 600 0.9375rem/1 var(--font-sans);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 28%, transparent), 0 10px 22px -10px var(--primary);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.ask-hero__submit svg { fill: none; stroke: currentColor; stroke-width: 2.25; stroke-linecap: round; stroke-linejoin: round; transition: transform var(--dur-3) var(--ease-spring); }
.ask-hero__submit:hover { box-shadow: inset 0 1px 0 color-mix(in srgb, var(--text-inverse) 28%, transparent), 0 14px 28px -10px var(--primary); }
.ask-hero__submit:hover svg { transform: translateX(3px); }
.ask-hero__submit:active { transform: scale(0.96); }
.ask-hero__submit-label, .ask-hero__status { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
.ask-hero :is(a, button):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Listbox: matched services with a price range and the earliest slot */
.ask-hero__list {
  position: absolute; left: -2px; right: -2px; top: calc(100% + 0.625rem); z-index: var(--z-popover);
  display: grid; gap: 0.125rem; max-height: min(22rem, 60vh); margin: 0; padding: 0.375rem; overflow-y: auto; overscroll-behavior: contain;
  list-style: none; text-align: left; border-radius: var(--radius-xl); background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-xl);
  transform-origin: 50% 0;
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-3) var(--ease-out);
}
@starting-style { .ask-hero__list { opacity: 0; transform: translateY(-8px) scale(0.98); } }
.ask-hero__list[hidden] { display: none; }
.ask-hero__option {
  display: grid; grid-template-columns: auto 1fr; align-items: center; gap: 0.25rem 0.75rem;
  padding: 0.625rem; border-radius: var(--radius-lg); color: var(--text-main); cursor: pointer;
  transition: background-color var(--dur-1);
}
.ask-hero__option:hover { background: var(--surface-muted); }
.ask-hero__option[aria-selected="true"] { background: color-mix(in srgb, var(--primary) 7%, var(--surface-light)); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 35%, transparent); }
.ask-hero__opt-icon {
  grid-row: span 2; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: var(--radius-lg); color: var(--primary);
  background: linear-gradient(135deg, color-mix(in srgb, var(--primary) 12%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 14%, var(--surface-light)));
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 16%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}
.ask-hero__option[aria-selected="true"] .ask-hero__opt-icon { transform: scale(1.08) rotate(-4deg); }
.ask-hero__opt-icon svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.ask-hero__opt-main { display: grid; min-width: 0; }
.ask-hero__opt-name { overflow: hidden; font-size: 0.9375rem; font-weight: 600; white-space: nowrap; text-overflow: ellipsis; }
.ask-hero__opt-name mark { padding: 0 0.0625rem; border-radius: 0.25rem; background: color-mix(in srgb, var(--primary) 14%, transparent); color: inherit; }
.ask-hero__opt-price { color: var(--ask-hero-muted); font: 500 0.75rem/1.5 var(--font-mono); }
.ask-hero__option .ask-hero__slot { grid-column: 2; }
.ask-hero__slot {
  justify-self: start; display: inline-flex; align-items: center; gap: 0.375rem; padding: 0.25rem 0.5rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--success) 10%, var(--surface-light)); color: var(--ask-hero-ok);
  font: 600 0.6875rem/1.2 var(--font-mono); white-space: nowrap;
}
.ask-hero__slot::before { content: ""; width: 0.375rem; height: 0.375rem; border-radius: 50%; background: currentColor; }

/* Popular chips: fill the field on tap (plain submit buttons without JS) */
.ask-hero__chips { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.5rem; margin-top: 1.25rem; }
.ask-hero__chips-label { width: 100%; color: var(--ask-hero-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.ask-hero__chip {
  display: inline-flex; align-items: center; gap: 0.4375rem; min-height: 2.5rem; padding: 0 0.875rem 0 0.75rem; border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--glass); color: var(--text-main); font: 500 0.875rem/1 var(--font-sans);
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
  -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
  animation: ask-hero-pop var(--dur-4) var(--ease-spring) calc(var(--ask-hero-in) + (8 + var(--ask-hero-c)) * var(--stagger)) backwards;
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2) var(--ease-out);
}
.ask-hero__chip svg { flex: none; fill: none; stroke: var(--primary); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.ask-hero__chip:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 35%, var(--border-subtle)), var(--highlight), var(--shadow-md); }
.ask-hero__chip:active { transform: scale(0.95); }

/* Secondary CTA and proof */
.ask-hero__foot { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 1rem 1.75rem; margin-top: 2.5rem; }
.ask-hero__call {
  display: inline-flex; align-items: center; gap: 0.5rem; min-height: 2.75rem; padding: 0 1.125rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-sm);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-2) var(--ease-out);
}
.ask-hero__call svg { fill: none; stroke: var(--primary); stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.ask-hero__call:hover { transform: translateY(-2px); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-md); }
.ask-hero__proof { display: inline-flex; align-items: center; gap: 0.625rem; margin: 0; color: var(--ask-hero-muted); font-size: 0.875rem; }
.ask-hero__proof strong { color: var(--text-main); }
.ask-hero__faces { display: flex; }
.ask-hero__faces span {
  display: grid; place-items: center; width: 2rem; height: 2rem; margin-left: -0.5rem; border: 2px solid var(--surface-light); border-radius: 50%;
  background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font-size: 0.6875rem; font-weight: 700;
}
.ask-hero__faces span:first-child { margin-left: 0; }
.ask-hero__faces span:nth-child(2) { background: linear-gradient(135deg, var(--primary-2), color-mix(in srgb, var(--primary-2) 60%, var(--text-main))); }
.ask-hero__faces span:nth-child(3) { background: linear-gradient(135deg, var(--accent), color-mix(in srgb, var(--accent) 60%, var(--primary))); color: var(--text-main); }

/* Floating glass cards: wide screens only, beside the headline */
.ask-hero__float { display: none; }
.ask-hero__float-avatar { display: grid; place-items: center; width: 2.25rem; height: 2.25rem; border-radius: 50%; background: var(--gradient-brand); color: var(--text-inverse); font-size: 0.75rem; font-weight: 700; }
.ask-hero__float strong { display: block; font-size: 0.875rem; font-weight: 600; }
.ask-hero__float small { color: var(--ask-hero-muted); font-size: 0.75rem; }
.ask-hero__float-price { font: 600 1.375rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }

@media (min-width: 768px) {
  .ask-hero__field { min-height: 4.75rem; gap: 0.625rem; padding: 0.5rem; padding-inline-start: 1.25rem; }
  .ask-hero__glass { display: block; }
  .ask-hero__input, .ask-hero__ghost { font-size: 1.25rem; }
  .ask-hero__submit { height: 3.25rem; padding: 0 1.375rem; border-radius: calc(var(--radius-2xl) - 0.5rem); }
  .ask-hero__submit-label { position: static; width: auto; height: auto; overflow: visible; clip: auto; }
  .ask-hero__chips-label { width: auto; margin-right: 0.25rem; }
  .ask-hero__option { grid-template-columns: auto 1fr auto; }
  .ask-hero__opt-icon { grid-row: auto; }
  .ask-hero__option .ask-hero__slot { grid-column: auto; }
}
@media (min-width: 1024px) {
  .ask-hero__float {
    position: absolute; z-index: 1; display: grid; gap: 0.25rem; width: 12.5rem; padding: 0.875rem; border-radius: var(--radius-xl);
    background: var(--glass); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight), var(--shadow-xl);
    -webkit-backdrop-filter: blur(var(--blur-md)); backdrop-filter: blur(var(--blur-md));
    text-align: left; animation: ask-hero-float-in var(--dur-5) var(--ease-out) calc(var(--ask-hero-in) + 900ms) backwards;
  }
  .ask-hero__float--left { top: 10rem; left: var(--gutter); grid-template-columns: auto 1fr; align-items: center; gap: 0.75rem; rotate: -4deg; }
  .ask-hero__float--right { top: 19rem; right: var(--gutter); rotate: 3deg; animation-delay: calc(var(--ask-hero-in) + 1050ms); }
}
@media (prefers-reduced-motion: reduce) {
  .ask-hero *, .ask-hero *::before, .ask-hero *::after { animation: none !important; }
}

@keyframes ask-hero-rise { from { opacity: 0; transform: translateY(16px); filter: blur(8px); } }
@keyframes ask-hero-bloom { from { opacity: 0; transform: scale(0.6); } }
@keyframes ask-hero-pop { from { opacity: 0; transform: translateY(8px) scale(0.9); } }
@keyframes ask-hero-float-in { from { opacity: 0; transform: translateY(24px) scale(0.94); filter: blur(6px); } }
@keyframes ask-hero-wrap { from { --ask-hero-sweep: 0%; --ask-hero-angle: -90deg; } }
@keyframes ask-hero-blink { 50% { opacity: 0; } }
```

## JS

```js
const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

document.querySelectorAll('[data-ask-hero]').forEach((hero, instance) => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const input = hero.querySelector('.ask-hero__input');
  const control = hero.querySelector('.ask-hero__control');
  const ghost = hero.querySelector('.ask-hero__ghost');
  const ghostText = hero.querySelector('.ask-hero__ghost-text');
  const pause = hero.querySelector('.ask-hero__pause');
  const list = hero.querySelector('.ask-hero__list');
  const status = hero.querySelector('.ask-hero__status');
  const tpl = hero.querySelector('.ask-hero__tpl').content;
  const lines = ghost.dataset.askHeroLines.split('|');
  const services = [...hero.querySelectorAll('datalist option')].map((o) => ({
    name: o.value, price: o.dataset.price, slot: o.dataset.slot, icon: o.dataset.icon,
    words: `${o.value} ${o.dataset.keys}`.toLowerCase().split(/\s+/),
  }));
  let options = [], active = -1, done = false, paused = false, offscreen = false;

  hero.classList.add('ask-hero--js');
  input.removeAttribute('list'); // the custom listbox replaces the native datalist popup

  // Typed suggestions: type and delete each problem, rest on the last. Pause and off-screen hold the clock.
  const wait = async (ms) => {
    await sleep(ms);
    while ((paused || offscreen) && !done) await sleep(150);
  };
  const end = () => {
    if (done) return;
    done = true;
    ghost.classList.remove('is-typing');
    ghostText.textContent = lines[lines.length - 1];
    if (document.activeElement === pause) input.focus(); // don't strand focus on a vanishing button
    pause.hidden = true;
  };
  const show = async (text, ms) => {
    if (done) return;
    ghostText.textContent = text;
    await wait(ms);
  };
  const type = async () => {
    ghost.classList.add('is-typing');
    pause.hidden = false;
    await wait(1400); // let the entrance land first
    for (const [i, line] of lines.entries()) {
      for (let n = 1; n <= line.length; n += 1) await show(line.slice(0, n), 45 + Math.random() * 60);
      if (i === lines.length - 1 || done) break;
      await wait(1500);
      for (let n = line.length - 1; n >= 0; n -= 1) await show(line.slice(0, n), 22);
      await wait(380);
    }
    end();
  };
  pause.addEventListener('click', () => {
    paused = !paused;
    pause.setAttribute('aria-pressed', String(paused));
    ghost.classList.toggle('is-paused', paused);
  });
  new IntersectionObserver(([entry]) => {
    offscreen = !entry.isIntersecting;
    hero.toggleAttribute('data-offscreen', offscreen);
  }).observe(hero);

  // Combobox (APG, list autocomplete): DOM focus stays in the input, aria-activedescendant moves
  const setActive = (i) => {
    active = i;
    options.forEach((opt, n) => opt.setAttribute('aria-selected', String(n === i)));
    if (i < 0) return input.removeAttribute('aria-activedescendant');
    input.setAttribute('aria-activedescendant', options[i].id);
    options[i].scrollIntoView({ block: 'nearest' });
  };
  const open = (on) => {
    list.hidden = !on;
    input.setAttribute('aria-expanded', String(on));
    if (!on) setActive(-1);
  };
  const score = (s, words) => words.filter((w) => s.words.some((k) => k.startsWith(w) || (k.length > 3 && w.startsWith(k)))).length;
  const highlight = (el, text, words) => {
    const lower = text.toLowerCase();
    const word = words.find((w) => lower.includes(w));
    if (!word) { el.textContent = text; return; }
    const at = lower.indexOf(word);
    const mark = document.createElement('mark');
    mark.textContent = text.slice(at, at + word.length);
    el.replaceChildren(text.slice(0, at), mark, text.slice(at + word.length));
  };
  const render = () => {
    const query = input.value.trim();
    const words = query.toLowerCase().split(/\s+/).filter((w) => w.length > 1);
    let hits = words.length
      ? services.map((s) => [s, score(s, words)]).filter(([, n]) => n).sort((a, b) => b[1] - a[1]).map(([s]) => s).slice(0, 5)
      : services.slice(0, 4);
    if (!hits.length) hits = [{ name: `Ask a pro: “${query}”`, value: query, price: 'Free 10-min diagnosis call', slot: 'Today 2–4pm', icon: 'chat' }];
    options = hits.map((s, n) => {
      const opt = tpl.querySelector('.ask-hero__option').cloneNode(true);
      opt.id = `ask-hero-${instance}-opt-${n}`; // unique per instance
      opt.dataset.value = s.value ?? s.name;
      highlight(opt.querySelector('.ask-hero__opt-name'), s.name, words);
      opt.querySelector('.ask-hero__opt-price').textContent = s.price;
      opt.querySelector('.ask-hero__slot').textContent = `Earliest: ${s.slot}`;
      opt.querySelector('.ask-hero__opt-icon').append((tpl.querySelector(`[data-icon="${s.icon}"]`) || tpl.querySelector('[data-icon="chat"]')).cloneNode(true));
      return opt;
    });
    list.replaceChildren(...options);
    setActive(-1);
    status.textContent = `${hits.length} ${hits.length === 1 ? 'suggestion' : 'suggestions'} available`;
  };
  const fill = (value) => {
    input.value = value;
    control.classList.toggle('is-filled', value !== '');
    input.focus();
  };
  const choose = (opt) => { fill(opt.dataset.value); open(false); };

  input.addEventListener('focus', end);
  input.addEventListener('blur', () => open(false));
  input.addEventListener('input', () => {
    end();
    control.classList.toggle('is-filled', input.value !== '');
    render();
    open(input.value.trim() !== '');
  });
  input.addEventListener('keydown', (e) => {
    const down = e.key === 'ArrowDown';
    if (down || e.key === 'ArrowUp') {
      e.preventDefault();
      if (list.hidden) { render(); open(true); }
      const n = options.length;
      setActive(active < 0 ? (down ? 0 : n - 1) : (active + (down ? 1 : -1) + n) % n);
    } else if (e.key === 'Enter' && !list.hidden && active >= 0) {
      e.preventDefault();
      choose(options[active]);
    } else if (e.key === 'Escape') {
      if (!list.hidden) open(false);
      else fill('');
    }
  });
  list.addEventListener('pointerdown', (e) => e.preventDefault()); // keep focus in the input
  list.addEventListener('click', (e) => {
    const opt = e.target.closest('[role="option"]');
    if (opt) choose(opt);
  });
  hero.querySelectorAll('.ask-hero__chip').forEach((chip) => chip.addEventListener('click', (e) => {
    e.preventDefault(); // with JS a chip fills the field instead of submitting
    fill(chip.value);
    render();
    open(true);
  }));

  if (input.value) { control.classList.add('is-filled'); end(); } // restored form state
  else if (reduce) end();
  else type();
});
```

## Notes

- The `<h1>` holds the field's `<label>`, so the question is both the headline and the input's accessible name. The input follows the APG combobox (list autocomplete): ↓/↑ open the list and move `aria-activedescendant` (wrapping), Enter takes the active option, Escape closes the list or, if it's already closed, clears the field. A polite status line announces how many suggestions there are.
- The typed text is an `aria-hidden` overlay, not a placeholder. It stops for good the moment the input is focused or filled, and afterwards rests as static text while the field is empty and blurred. Its pause button (`aria-pressed`) appears only while it types (about 9s); off-screen it waits too. If the pause button has focus when typing ends, focus moves to the input.
- Without JS it's a plain GET form (`role="search"`): `q` is the text, and the chips are submit buttons that send `service`. The `<datalist>` gives native suggestions and is also where the JS listbox gets its services, prices and slots (`data-price`, `data-slot`, `data-keys`). Point `action` at your search page.
- Reduced motion: no typing or caret blink and no entrance; the overlay shows the last suggestion statically, and the focus border appears fully drawn with no sweep. Without `@property` the border appears at once, and without `:has()` the input gets a plain outline.
- Contrast on white: body copy uses `--ask-hero-muted` (6.3:1, and 4.9:1 or better on the strongest bloom); the overlay uses `--text-muted` on the solid field (4.8:1); slot chips use `--ask-hero-ok` (5.4:1 on their tint); the gradient word `fixing?` stays at 3.7:1 or better (large text). The focus border and halo run from `--primary` to `--primary-2`, both 3:1 or better against white.
