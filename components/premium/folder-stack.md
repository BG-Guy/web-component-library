# Folder Tab Stack

Case studies filed as a stack of coloured paper folders with staggered tabs along the top, like a drawer of project files. Choosing a tab pulls that folder up out of the stack, then springs it to the front while the others shuffle back a step and darken with depth. Each folder holds a clipped project print, the job's numbers and the owner's words, on grainy paper with soft inner shadows. On phones the tabs become a scrolling row of chips above the stack. Depends on `tokens/variables.css`.

**Motion:** folder lift (`--dur-3`, `--ease-out`) then spring to the front (`--dur-5`, `--ease-spring`) · the rest shuffle back with a stagger (`--stagger`) · depth shading via a registered `--folder-stack-shade` (`--dur-4`, `--ease-out`) · chip row glides to the active chip on phones.

## HTML

```html
<section class="folder-stack" aria-labelledby="folder-stack-title" data-folder-stack>
  <div class="folder-stack__inner">
    <header class="folder-stack__head">
      <p class="folder-stack__eyebrow">Case files</p>
      <h2 id="folder-stack-title" class="folder-stack__title">Four homes, start to finish.</h2>
      <p class="folder-stack__lead">Pull a folder from the stack for the photos, the numbers and what the owners said once we'd packed up.</p>
    </header>

    <div class="folder-stack__desk">
      <div class="folder-stack__tabs" role="tablist" aria-label="Case studies">
        <button class="folder-stack__tab folder-stack__tab--manila" role="tab" type="button" id="folder-stack-tab-kitchen" aria-selected="true" aria-controls="folder-stack-kitchen"><span class="folder-stack__tab-num">01</span>Kitchen</button>
        <button class="folder-stack__tab folder-stack__tab--sage" role="tab" type="button" id="folder-stack-tab-bath" aria-selected="false" aria-controls="folder-stack-bath" tabindex="-1"><span class="folder-stack__tab-num">02</span>Wet room</button>
        <button class="folder-stack__tab folder-stack__tab--blue" role="tab" type="button" id="folder-stack-tab-heat" aria-selected="false" aria-controls="folder-stack-heat" tabindex="-1"><span class="folder-stack__tab-num">03</span>Heat pump</button>
        <button class="folder-stack__tab folder-stack__tab--kraft" role="tab" type="button" id="folder-stack-tab-roof" aria-selected="false" aria-controls="folder-stack-roof" tabindex="-1"><span class="folder-stack__tab-num">04</span>Slate roof</button>
      </div>

      <div class="folder-stack__stack">
        <article class="folder-stack__folder folder-stack__folder--manila" role="tabpanel" id="folder-stack-kitchen" aria-labelledby="folder-stack-tab-kitchen" tabindex="0">
          <figure class="folder-stack__photo">
            <img src="case-kitchen.jpg" width="640" height="480" alt="Walnut kitchen with a white quartz island and brass pendant lights" loading="lazy" decoding="async">
            <svg class="folder-stack__clip" viewBox="0 0 24 24" width="36" height="36" aria-hidden="true" focusable="false"><path d="M15 7v9.5a3 3 0 0 1-6 0V5.5a2 2 0 0 1 4 0v10a1 1 0 0 1-2 0V7" /></svg>
            <span class="folder-stack__sticker" aria-hidden="true">Case 01</span>
          </figure>
          <div class="folder-stack__body">
            <p class="folder-stack__meta">Kitchen refit · Westlake · 2026</p>
            <h3 class="folder-stack__name">A walnut kitchen in nine working days.</h3>
            <dl class="folder-stack__stats">
              <div><dt>On site</dt><dd>9 days</dd></div>
              <div><dt>Fixed price</dt><dd>$18.4k</dd></div>
              <div><dt>Change orders</dt><dd>0</dd></div>
            </dl>
            <figure class="folder-stack__quote">
              <blockquote><p>“They kept the house cleaner than we do. Nine days, exactly as promised.”</p></blockquote>
              <figcaption>Amy &amp; Tom R., Westlake</figcaption>
            </figure>
            <a class="folder-stack__link" href="#case-kitchen">Read the case study <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </article>

        <article class="folder-stack__folder folder-stack__folder--sage" role="tabpanel" id="folder-stack-bath" aria-labelledby="folder-stack-tab-bath" tabindex="0">
          <figure class="folder-stack__photo">
            <img src="case-wet-room.jpg" width="640" height="480" alt="Level-access wet room with a fold-down seat and large grey tiles" loading="lazy" decoding="async">
            <svg class="folder-stack__clip" viewBox="0 0 24 24" width="36" height="36" aria-hidden="true" focusable="false"><path d="M15 7v9.5a3 3 0 0 1-6 0V5.5a2 2 0 0 1 4 0v10a1 1 0 0 1-2 0V7" /></svg>
            <span class="folder-stack__sticker" aria-hidden="true">Case 02</span>
          </figure>
          <div class="folder-stack__body">
            <p class="folder-stack__meta">Bathroom · Northside · 2026</p>
            <h3 class="folder-stack__name">A level-access wet room for a family of five.</h3>
            <dl class="folder-stack__stats">
              <div><dt>On site</dt><dd>6 days</dd></div>
              <div><dt>Fixed price</dt><dd>$11.3k</dd></div>
              <div><dt>Door threshold</dt><dd>0 mm</dd></div>
            </dl>
            <figure class="folder-stack__quote">
              <blockquote><p>“Mum can shower on her own again. That's the whole review.”</p></blockquote>
              <figcaption>Priya M., Northside</figcaption>
            </figure>
            <a class="folder-stack__link" href="#case-wet-room">Read the case study <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </article>

        <article class="folder-stack__folder folder-stack__folder--blue" role="tabpanel" id="folder-stack-heat" aria-labelledby="folder-stack-tab-heat" tabindex="0">
          <figure class="folder-stack__photo">
            <img src="case-heat-pump.jpg" width="640" height="480" alt="Heat pump unit on a concrete pad beside a brick wall" loading="lazy" decoding="async">
            <svg class="folder-stack__clip" viewBox="0 0 24 24" width="36" height="36" aria-hidden="true" focusable="false"><path d="M15 7v9.5a3 3 0 0 1-6 0V5.5a2 2 0 0 1 4 0v10a1 1 0 0 1-2 0V7" /></svg>
            <span class="folder-stack__sticker" aria-hidden="true">Case 03</span>
          </figure>
          <div class="folder-stack__body">
            <p class="folder-stack__meta">Heating · Riverside · 2025</p>
            <h3 class="folder-stack__name">From oil furnace to heat pump before the first frost.</h3>
            <dl class="folder-stack__stats">
              <div><dt>On site</dt><dd>3 days</dd></div>
              <div><dt>Energy bills</dt><dd>−41%</dd></div>
              <div><dt>Rebate claimed</dt><dd>$2,400</dd></div>
            </dl>
            <figure class="folder-stack__quote">
              <blockquote><p>“The house is warmer and the bills are lower. I didn't think I'd get both.”</p></blockquote>
              <figcaption>Glen O., Riverside</figcaption>
            </figure>
            <a class="folder-stack__link" href="#case-heat-pump">Read the case study <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </article>

        <article class="folder-stack__folder folder-stack__folder--kraft" role="tabpanel" id="folder-stack-roof" aria-labelledby="folder-stack-tab-roof" tabindex="0">
          <figure class="folder-stack__photo">
            <img src="case-slate-roof.jpg" width="640" height="480" alt="Grey slate roof with copper gutters under a clear sky" loading="lazy" decoding="async">
            <svg class="folder-stack__clip" viewBox="0 0 24 24" width="36" height="36" aria-hidden="true" focusable="false"><path d="M15 7v9.5a3 3 0 0 1-6 0V5.5a2 2 0 0 1 4 0v10a1 1 0 0 1-2 0V7" /></svg>
            <span class="folder-stack__sticker" aria-hidden="true">Case 04</span>
          </figure>
          <div class="folder-stack__body">
            <p class="folder-stack__meta">Roofing · Springfield · 2025</p>
            <h3 class="folder-stack__name">A reclaimed slate roof, matched slate for slate.</h3>
            <dl class="folder-stack__stats">
              <div><dt>On site</dt><dd>11 days</dd></div>
              <div><dt>Slates matched</dt><dd>1,850</dd></div>
              <div><dt>Warranty</dt><dd>25 yrs</dd></div>
            </dl>
            <figure class="folder-stack__quote">
              <blockquote><p>“You honestly can't tell which slates are new.”</p></blockquote>
              <figcaption>Dana K., Springfield</figcaption>
            </figure>
            <a class="folder-stack__link" href="#case-slate-roof">Read the case study <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
          </div>
        </article>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
@property --folder-stack-shade { syntax: "<percentage>"; inherits: true; initial-value: 0%; }

/* Section: warm paper with a fine grain */
.folder-stack {
  --folder-stack-step: 1.125rem;  /* how much higher each folder behind sits */
  --folder-stack-tab-h: 2.75rem;
  --folder-stack-depth-max: 3;    /* folders − 1; JS keeps it in sync */
  --folder-stack-grain: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='220' height='220'%3E%3Cfilter id='p'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2.6 -1.25'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23p)'/%3E%3C/svg%3E");
  position: relative; isolation: isolate; overflow: clip;
  background: color-mix(in srgb, var(--accent) 6%, var(--surface-light));
  color: var(--text-main); font-family: var(--font-sans);
}
.folder-stack::before {
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none; opacity: 0.45;
  background: color-mix(in srgb, var(--warning) 30%, transparent);
  -webkit-mask: var(--folder-stack-grain) 0 0 / 220px 220px;
  mask: var(--folder-stack-grain) 0 0 / 220px 220px;
}
.folder-stack svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.folder-stack__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.folder-stack__head { max-width: 40rem; margin-bottom: 2.5rem; }
.folder-stack__eyebrow { margin: 0; color: var(--warning); font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.1em; text-transform: uppercase; }
.folder-stack__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.folder-stack__lead { margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }

/* Paper colours, shaded by depth (--folder-stack-d is set by JS) */
.folder-stack__folder, .folder-stack__tab {
  --folder-stack-paper: color-mix(in srgb, var(--accent) 30%, var(--surface-light));
  --folder-stack-shade: calc(var(--folder-stack-d, 0) * 7%);
  --folder-stack-tone: color-mix(in srgb, var(--text-main) var(--folder-stack-shade), var(--folder-stack-paper));
  --folder-stack-ink-soft: color-mix(in srgb, var(--text-main) 78%, var(--folder-stack-paper));
}
.folder-stack__folder--sage, .folder-stack__tab--sage { --folder-stack-paper: color-mix(in srgb, var(--primary-2) 20%, var(--surface-light)); }
.folder-stack__folder--blue, .folder-stack__tab--blue { --folder-stack-paper: color-mix(in srgb, var(--primary) 16%, var(--surface-light)); }
.folder-stack__folder--kraft, .folder-stack__tab--kraft { --folder-stack-paper: color-mix(in srgb, var(--warning) 30%, var(--surface-light)); }

/* Folders: stacked articles without JS */
.folder-stack__stack { display: grid; gap: 3rem; }
.folder-stack__folder {
  position: relative; isolation: isolate; display: grid; gap: 1.75rem;
  padding: 1.75rem 1.25rem 1.5rem; border-radius: 0.375rem var(--radius-xl) var(--radius-xl) var(--radius-xl);
  background-color: var(--folder-stack-tone);
  background-image:
    linear-gradient(180deg, transparent 0.75rem, color-mix(in srgb, var(--text-main) 8%, transparent) 0.75rem calc(0.75rem + 1px), transparent calc(0.75rem + 1px)),
    linear-gradient(180deg, color-mix(in srgb, var(--surface-light) 40%, transparent), transparent 5rem);
  box-shadow:
    inset 0 0 0 1px color-mix(in srgb, var(--text-main) 9%, transparent),
    inset 0 1px 0 color-mix(in srgb, var(--surface-light) 70%, transparent),
    inset 0 -2.5rem 3rem -3rem color-mix(in srgb, var(--text-main) 25%, transparent),
    0 -6px 14px -10px color-mix(in srgb, var(--text-main) 28%, transparent),
    0 22px 44px -26px color-mix(in srgb, var(--text-main) 45%, transparent);
  transition: --folder-stack-shade var(--dur-4) var(--ease-out);
}
.folder-stack__folder::after { /* paper grain, under the content */
  content: ""; position: absolute; inset: 0; z-index: -1; border-radius: inherit; pointer-events: none; opacity: 0.5;
  background: color-mix(in srgb, var(--warning) 26%, transparent);
  -webkit-mask: var(--folder-stack-grain) 0 0 / 220px 220px;
  mask: var(--folder-stack-grain) 0 0 / 220px 220px;
}
.folder-stack__folder::before { /* printed tab for the no-JS stack */
  content: ""; position: absolute; left: 1.25rem; bottom: 100%; width: 7.5rem; height: 1.5rem;
  border-radius: 0.75rem 0.75rem 0 0; background: var(--folder-stack-tone);
}

/* Folder contents: a clipped print, the numbers and the owner's words */
.folder-stack__photo {
  position: relative; justify-self: start; width: 100%; max-width: 30rem; margin: 0.75rem 0 0; padding: 0.5rem;
  border-radius: 0.25rem; background: var(--surface-light); rotate: -1.25deg;
  box-shadow: 0 1px 2px color-mix(in srgb, var(--text-main) 16%, transparent), 0 16px 30px -18px color-mix(in srgb, var(--text-main) 55%, transparent);
}
.folder-stack__photo img {
  display: block; width: 100%; height: auto; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 2px;
  background: color-mix(in srgb, var(--folder-stack-paper) 60%, var(--surface-muted));
}
.folder-stack .folder-stack__clip {
  position: absolute; top: -1.25rem; left: 1.25rem; width: 2.25rem; height: 2.25rem; rotate: 6deg; stroke-width: 1.75;
  color: color-mix(in srgb, var(--text-muted) 80%, var(--text-main));
  filter: drop-shadow(0 2px 1px color-mix(in srgb, var(--text-main) 22%, transparent));
}
.folder-stack__sticker {
  position: absolute; top: -0.625rem; right: -0.5rem; padding: 0.3125rem 0.5rem; border-radius: 0.25rem; rotate: 3deg;
  background: var(--surface-light); box-shadow: var(--shadow-sm), inset 0 0 0 1px var(--border-subtle);
  font: 600 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase;
}
.folder-stack__body { display: grid; align-content: start; gap: 1rem; }
.folder-stack__meta { margin: 0; color: var(--folder-stack-ink-soft); font: 500 0.75rem/1.3 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.folder-stack__name { margin: 0; font: 600 clamp(1.5rem, 1.15rem + 1.4vw, 2.125rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.folder-stack__stats {
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 0.75rem; margin: 0.25rem 0 0; padding: 0.875rem 0;
  border-block: 1px dashed color-mix(in srgb, var(--text-main) 22%, transparent);
}
.folder-stack__stats div { display: flex; flex-direction: column-reverse; justify-content: flex-end; gap: 0.375rem; }
.folder-stack__stats dt { color: var(--folder-stack-ink-soft); font: 500 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.folder-stack__stats dd { margin: 0; font: 600 clamp(1.25rem, 1rem + 1vw, 1.625rem)/1 var(--font-display); letter-spacing: var(--tracking-tight); font-variant-numeric: tabular-nums; }
.folder-stack__quote { margin: 0; padding-left: 1rem; border-left: 3px solid color-mix(in srgb, var(--text-main) 24%, var(--folder-stack-paper)); }
.folder-stack__quote blockquote { margin: 0; }
.folder-stack__quote p { margin: 0; font: 500 1.0625rem/1.5 var(--font-display); letter-spacing: -0.01em; }
.folder-stack__quote figcaption { margin-top: 0.5rem; color: var(--folder-stack-ink-soft); font-size: 0.8125rem; }
.folder-stack__link {
  justify-self: start; display: inline-flex; align-items: center; gap: 0.375rem; min-height: 2.75rem;
  color: var(--text-main); font-size: 0.9375rem; font-weight: 600; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 0.25em;
}
.folder-stack__link svg { transition: transform var(--dur-3) var(--ease-spring); }
.folder-stack__link:hover svg { transform: translateX(3px); }
.folder-stack :is(.folder-stack__link, .folder-stack__folder):focus-visible { outline: 2px solid var(--primary); outline-offset: 3px; }

/* Tabs: a scrolling row of chips on phones (hidden without JS) */
.folder-stack:not(.folder-stack--js) .folder-stack__tabs { display: none; }
.folder-stack__tabs {
  position: relative; display: flex; gap: 0.5rem; margin: 0 calc(var(--gutter) * -1) 1rem; padding: 0.25rem var(--gutter);
  overflow-x: auto; scrollbar-width: none;
  -webkit-mask: linear-gradient(90deg, transparent, black var(--gutter), black calc(100% - var(--gutter)), transparent);
  mask: linear-gradient(90deg, transparent, black var(--gutter), black calc(100% - var(--gutter)), transparent);
}
.folder-stack__tabs::-webkit-scrollbar { display: none; }
.folder-stack__tab {
  position: relative; flex: none; display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1rem 0 0.375rem;
  border: 0; border-radius: var(--radius-full); cursor: pointer; white-space: nowrap;
  background-color: var(--folder-stack-paper); color: var(--text-main); font: 600 0.875rem/1 var(--font-sans);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-main) 10%, transparent), var(--highlight);
  transition: background-color var(--dur-2), color var(--dur-2);
}
.folder-stack__tab-num {
  display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: 50%;
  background: color-mix(in srgb, var(--surface-light) 65%, transparent); font: 600 0.75rem/1 var(--font-mono);
  transition: background-color var(--dur-2), color var(--dur-2);
}
.folder-stack__tab[aria-selected="true"] { background-color: var(--text-main); color: var(--surface-light); }
.folder-stack__tab[aria-selected="true"] .folder-stack__tab-num { background: var(--folder-stack-paper); color: var(--text-main); }
.folder-stack__tab:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

/* Deck (JS): every folder shares one cell; depth sets offset, z-order and shade */
.folder-stack--js .folder-stack__desk { position: relative; isolation: isolate; }
.folder-stack--js .folder-stack__stack { gap: 0; padding-top: calc(var(--folder-stack-depth-max) * var(--folder-stack-step)); }
.folder-stack--js .folder-stack__folder {
  grid-area: 1 / 1; z-index: calc(10 - var(--folder-stack-d, 0));
  transform: translateY(calc(var(--folder-stack-d, 0) * var(--folder-stack-step) * -1));
  transition: transform var(--dur-5) var(--ease-spring) calc(var(--folder-stack-d, 0) * var(--stagger)), --folder-stack-shade var(--dur-4) var(--ease-out);
}
.folder-stack--js .folder-stack__folder::before { display: none; }
/* The chosen folder first lifts clear of the stack, then springs into the front slot */
.folder-stack--js .folder-stack__folder.is-lifting {
  z-index: 20; transform: translateY(calc(var(--folder-stack-from, 1) * var(--folder-stack-step) * -1 - 2.25rem));
  transition: transform var(--dur-3) var(--ease-out), --folder-stack-shade var(--dur-4) var(--ease-out);
}

@media (min-width: 768px) {
  .folder-stack__folder { grid-template-columns: minmax(0, 1fr) minmax(0, 1.1fr); align-items: start; gap: 2.5rem; padding: 2.25rem 2.25rem 2rem; min-height: 26rem; }
  /* Real folder tabs: staggered along the top, each riding on its folder */
  .folder-stack--js .folder-stack__desk { padding-top: var(--folder-stack-tab-h); }
  .folder-stack--js .folder-stack__tabs {
    position: absolute; top: calc(var(--folder-stack-depth-max) * var(--folder-stack-step)); left: 1.5rem; right: 1.5rem;
    height: var(--folder-stack-tab-h); margin: 0; padding: 0; gap: 0.75rem; overflow: visible; -webkit-mask: none; mask: none;
  }
  .folder-stack--js .folder-stack__tab {
    z-index: calc(10 - var(--folder-stack-d, 0)); flex: 0 1 11.5rem; height: calc(100% + 1px); padding: 0 1rem 0 0.5rem;
    border-radius: 0.875rem 0.875rem 0 0; background-color: var(--folder-stack-tone); color: var(--text-main);
    box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 70%, transparent), 0 -5px 12px -9px color-mix(in srgb, var(--text-main) 40%, transparent);
    transform: translateY(calc(var(--folder-stack-d, 0) * var(--folder-stack-step) * -1));
    transition: transform var(--dur-5) var(--ease-spring) calc(var(--folder-stack-d, 0) * var(--stagger)), --folder-stack-shade var(--dur-4) var(--ease-out);
  }
  .folder-stack--js .folder-stack__tab::before, .folder-stack--js .folder-stack__tab::after { /* concave fillets into the folder edge */
    content: ""; position: absolute; bottom: 0; width: 0.75rem; height: 0.75rem; pointer-events: none;
  }
  .folder-stack--js .folder-stack__tab::before { right: 100%; background: radial-gradient(circle at 0 0, transparent 0.75rem, var(--folder-stack-tone) calc(0.75rem + 0.5px)); }
  .folder-stack--js .folder-stack__tab::after { left: 100%; background: radial-gradient(circle at 100% 0, transparent 0.75rem, var(--folder-stack-tone) calc(0.75rem + 0.5px)); }
  .folder-stack--js .folder-stack__tab[aria-selected="true"] { background-color: var(--folder-stack-tone); color: var(--text-main); }
  .folder-stack--js .folder-stack__tab[aria-selected="true"] .folder-stack__tab-num { background: var(--text-main); color: var(--surface-light); }
  .folder-stack--js .folder-stack__tab.is-lifting {
    z-index: 20; transform: translateY(calc(var(--folder-stack-from, 1) * var(--folder-stack-step) * -1 - 2.25rem));
    transition: transform var(--dur-3) var(--ease-out), --folder-stack-shade var(--dur-4) var(--ease-out);
  }
  .folder-stack--js .folder-stack__tab:focus-visible { outline-offset: -4px; }
}
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-folder-stack]').forEach((root) => {
  const list = root.querySelector('[role="tablist"]');
  const tabs = [...list.querySelectorAll('[role="tab"]')];
  const folders = tabs.map((tab) => document.getElementById(tab.getAttribute('aria-controls')));
  let order = tabs.map((_, i) => i); // folder indices, front to back
  let current = Math.max(0, tabs.findIndex((tab) => tab.getAttribute('aria-selected') === 'true'));
  let settle = 0;
  root.classList.add('folder-stack--js');
  root.style.setProperty('--folder-stack-depth-max', tabs.length - 1);

  // Choose a folder: ARIA state, roving tabindex and inert back folders, then restack.
  // The chosen folder lifts out of the pile before springing to the front; the rest shuffle back a step.
  const select = (index, { focus = false, instant = false } = {}) => {
    index = (index + tabs.length) % tabs.length;
    const from = order.indexOf(index);
    current = index;
    order = [index, ...order.filter((i) => i !== index)];
    tabs.forEach((tab, n) => {
      tab.setAttribute('aria-selected', String(n === index));
      tab.tabIndex = n === index ? 0 : -1;
      folders[n].inert = n !== index;
    });
    order.forEach((i, depth) => [tabs[i], folders[i]].forEach((el) => el.style.setProperty('--folder-stack-d', depth)));
    clearTimeout(settle);
    root.querySelectorAll('.is-lifting').forEach((el) => el.classList.remove('is-lifting'));
    if (from > 0 && !instant && !reduce.matches) {
      const pair = [tabs[index], folders[index]];
      pair.forEach((el) => { el.style.setProperty('--folder-stack-from', from); el.classList.add('is-lifting'); });
      settle = setTimeout(() => pair.forEach((el) => el.classList.remove('is-lifting')), 240);
    }
    if (focus) tabs[index].focus();
    // Phones: keep the active chip centred in its row (scrolls the row, never the page)
    const tab = tabs[index];
    list.scrollTo({ left: tab.offsetLeft - (list.clientWidth - tab.offsetWidth) / 2, behavior: instant || reduce.matches ? 'auto' : 'smooth' });
  };

  // APG tabs with automatic activation: arrows move and select (wrapping), Home/End jump
  tabs.forEach((tab, i) => tab.addEventListener('click', () => select(i)));
  list.addEventListener('keydown', (e) => {
    const keys = { ArrowRight: current + 1, ArrowLeft: current - 1, Home: 0, End: tabs.length - 1 };
    if (!(e.key in keys)) return;
    e.preventDefault();
    select(keys[e.key], { focus: true });
  });
  select(current, { instant: true });
});
```

## Notes

- APG tabs with automatic activation. ←/→ move and select (wrapping), Home/End jump to either end, and roving tabindex keeps the row to one tab stop. Tab then moves into the front folder, a `tabpanel` labelled by its tab. Folders behind it are `inert`, so they leave the tab order and the accessibility tree while only their edges show.
- Without JS, the tab row stays hidden and every folder renders as its own article, with its heading, photo, stats and quote, stacked down the page under a printed tab shape. JS adds `folder-stack--js`, which turns the column into the deck. Content stays visible throughout, so nothing flashes.
- Depth is one custom property per folder and tab (`--folder-stack-d`, set by JS). It drives the offset, the z-order, the stagger and the paper shade. The shade is a registered `@property` (`--folder-stack-shade`), so it darkens smoothly where registered properties are supported and switches instantly elsewhere.
- Reduced motion: no lift, spring or stagger; folders swap instantly because the duration tokens collapse and JS skips the lift.
- Contrast: copy is `--text-main` on every paper tone (9.5:1 or better). `--text-muted` drops to 3.1–3.8:1 on these papers, so secondary text uses `--folder-stack-ink-soft` (`--text-main` at 78% over the paper) at 5.4:1 or better. Tab labels on the deepest folder stay at 6.5:1 or better.
- To adapt it, add or remove folders freely; JS sets `--folder-stack-depth-max` from the tab count. Paper colours are `--folder-stack-paper` on the `--manila`, `--sage`, `--blue` and `--kraft` modifiers, all mixed from tokens, and `--folder-stack-step` sets how far each folder behind rises.
