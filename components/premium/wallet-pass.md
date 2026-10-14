# Appointment Wallet Pass

An appointment confirmation styled as a phone wallet pass, tucked into a dark leather card holder. When the holder scrolls into view (or someone presses "Show pass"), the pass springs up out of the pocket, and once it settles a foil shine sweeps across it. "Details" flips the pass over to notes, the cancellation policy, an .ics calendar file and directions. On phones the copy stacks above the holder, and the pass narrows with the column without losing its notches or QR code. Depends on `tokens/variables.css`.

**Motion:** pocket slide-out and tuck (`--dur-5`, `--ease-spring`) · one-shot foil shine sweep (`--ease-in-out`) · 3D card flip (`--dur-5`, `--ease-spring`) · chevron turn and button presses (`--dur-2`–`--dur-4`, `--ease-spring`).

## HTML

```html
<section class="wallet-pass" aria-labelledby="wallet-pass-title" data-wallet-pass>
  <div class="wallet-pass__inner">
    <div class="wallet-pass__copy">
      <p class="wallet-pass__eyebrow">
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>
        Booking confirmed
      </p>
      <h2 id="wallet-pass-title" class="wallet-pass__title">Your visit, ready in your pocket.</h2>
      <p class="wallet-pass__lead">Every booking comes with a wallet pass: who's coming, when to expect them and a check-in code for the door. If your window moves, the pass updates itself.</p>
      <ul class="wallet-pass__perks" role="list">
        <li>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M12 3v12m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" /></svg>
          Saved to your phone, works offline
        </li>
        <li>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M20.5 12a8.5 8.5 0 0 1-15 5.5L3 15M3.5 12a8.5 8.5 0 0 1 15-5.5L21 9M21 4v5h-5M3 20v-5h5" /></svg>
          Live updates if Sam is running early
        </li>
        <li>
          <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2z" /></svg>
          Calendar and directions in one tap
        </li>
      </ul>
    </div>

    <div class="wallet-pass__stage">
      <div class="wallet-pass__sleeve" aria-hidden="true"></div>

      <div class="wallet-pass__slot">
        <div class="wallet-pass__lift">
          <div class="wallet-pass__flipper">
            <!-- Front -->
            <article class="wallet-pass__face wallet-pass__face--front" aria-labelledby="wallet-pass-front-title">
              <div class="wallet-pass__part wallet-pass__part--main">
                <div class="wallet-pass__strip">
                  <div class="wallet-pass__bar">
                    <span class="wallet-pass__logo">
                      <span class="wallet-pass__mark" aria-hidden="true"><svg viewBox="0 0 24 24" width="18" height="18" focusable="false"><path d="M3.5 11 12 4l8.5 7M6 9.5V20h12V9.5M10 20v-5.5h4V20" /></svg></span>
                      Brand
                    </span>
                    <span class="wallet-pass__chip">
                      <svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true" focusable="false"><path d="m5 12.5 4.5 4.5L19 7.5" /></svg>
                      Confirmed
                    </span>
                  </div>
                  <h3 id="wallet-pass-front-title" class="wallet-pass__headline">
                    <span class="wallet-pass__service">Leak repair · Kitchen<span class="wallet-pass__sr">,</span></span>
                    <span class="wallet-pass__date">Thu 16 Oct</span>
                  </h3>
                </div>
                <dl class="wallet-pass__fields">
                  <div class="wallet-pass__field wallet-pass__field--wide">
                    <dt>Technician</dt>
                    <dd class="wallet-pass__tech">
                      <span class="wallet-pass__avatar" aria-hidden="true">SK</span>
                      <span><strong>Sam Kowalski</strong><small>Licensed plumber · 4.9 rating</small></span>
                    </dd>
                  </div>
                  <div class="wallet-pass__field"><dt>Arrival window</dt><dd><strong>10:00–12:00</strong></dd></div>
                  <div class="wallet-pass__field"><dt>Address</dt><dd><strong>42 Elm Street, Westlake</strong></dd></div>
                </dl>
              </div>

              <div class="wallet-pass__part wallet-pass__part--stub">
                <svg class="wallet-pass__qr" viewBox="-1.5 -1.5 24 24" width="96" height="96" role="img" aria-label="Check-in QR code" focusable="false">
                  <rect class="wallet-pass__eye" x="0.5" y="0.5" width="6" height="6" rx="1.4" /><rect x="2" y="2" width="3" height="3" rx="0.6" />
                  <rect class="wallet-pass__eye" x="14.5" y="0.5" width="6" height="6" rx="1.4" /><rect x="16" y="2" width="3" height="3" rx="0.6" />
                  <rect class="wallet-pass__eye" x="0.5" y="14.5" width="6" height="6" rx="1.4" /><rect x="2" y="16" width="3" height="3" rx="0.6" />
                  <rect x="8" y="0" width="2" height="1"/><rect x="11" y="0" width="2" height="1"/><rect x="8" y="1" width="2" height="1"/><rect x="8" y="2" width="1" height="1"/><rect x="12" y="2" width="1" height="1"/><rect x="9" y="3" width="2" height="1"/><rect x="8" y="4" width="1" height="1"/><rect x="11" y="4" width="2" height="1"/><rect x="11" y="5" width="1" height="1"/><rect x="8" y="6" width="1" height="1"/><rect x="10" y="6" width="1" height="1"/><rect x="12" y="6" width="1" height="1"/><rect x="11" y="7" width="1" height="1"/><rect x="0" y="8" width="3" height="1"/><rect x="5" y="8" width="5" height="1"/><rect x="11" y="8" width="1" height="1"/><rect x="13" y="8" width="2" height="1"/><rect x="19" y="8" width="2" height="1"/><rect x="1" y="9" width="2" height="1"/><rect x="9" y="9" width="1" height="1"/><rect x="11" y="9" width="3" height="1"/><rect x="16" y="9" width="5" height="1"/><rect x="1" y="10" width="2" height="1"/><rect x="4" y="10" width="4" height="1"/><rect x="9" y="10" width="1" height="1"/><rect x="11" y="10" width="1" height="1"/><rect x="1" y="11" width="1" height="1"/><rect x="3" y="11" width="2" height="1"/><rect x="9" y="11" width="1" height="1"/><rect x="12" y="11" width="1" height="1"/><rect x="16" y="11" width="1" height="1"/><rect x="19" y="11" width="2" height="1"/><rect x="3" y="12" width="1" height="1"/><rect x="5" y="12" width="2" height="1"/><rect x="12" y="12" width="5" height="1"/><rect x="8" y="13" width="1" height="1"/><rect x="10" y="13" width="1" height="1"/><rect x="14" y="13" width="3" height="1"/><rect x="18" y="13" width="1" height="1"/><rect x="8" y="14" width="1" height="1"/><rect x="10" y="14" width="1" height="1"/><rect x="8" y="15" width="1" height="1"/><rect x="11" y="15" width="1" height="1"/><rect x="14" y="15" width="1" height="1"/><rect x="16" y="15" width="1" height="1"/><rect x="19" y="15" width="2" height="1"/><rect x="8" y="16" width="2" height="1"/><rect x="12" y="16" width="1" height="1"/><rect x="17" y="16" width="3" height="1"/><rect x="8" y="17" width="3" height="1"/><rect x="14" y="17" width="2" height="1"/><rect x="17" y="17" width="4" height="1"/><rect x="8" y="18" width="1" height="1"/><rect x="10" y="18" width="1" height="1"/><rect x="12" y="18" width="3" height="1"/><rect x="17" y="18" width="1" height="1"/><rect x="9" y="19" width="1" height="1"/><rect x="11" y="19" width="1" height="1"/><rect x="13" y="19" width="8" height="1"/><rect x="8" y="20" width="1" height="1"/><rect x="10" y="20" width="2" height="1"/><rect x="14" y="20" width="1" height="1"/><rect x="16" y="20" width="1" height="1"/><rect x="19" y="20" width="1" height="1"/>
                </svg>
                <div class="wallet-pass__code">
                  <p class="wallet-pass__code-label">Check-in code</p>
                  <p class="wallet-pass__code-value">BR-4821</p>
                  <p class="wallet-pass__code-note">Show this to Sam at the door.</p>
                  <button class="wallet-pass__flip" type="button" hidden>
                    <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18zM12 16v-4.5M12 8h.01" /></svg>
                    Details
                  </button>
                </div>
              </div>
            </article>

            <!-- Back -->
            <article class="wallet-pass__face wallet-pass__face--back" aria-labelledby="wallet-pass-back-title">
              <div class="wallet-pass__part wallet-pass__part--main">
                <div class="wallet-pass__strip wallet-pass__strip--back">
                  <div class="wallet-pass__bar">
                    <h3 id="wallet-pass-back-title" class="wallet-pass__back-title" tabindex="-1">Visit details</h3>
                    <button class="wallet-pass__flip wallet-pass__flip--done" type="button" hidden>
                      <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M3.5 12a8.5 8.5 0 1 0 2.6-6.1L3.5 8.5M3.5 3.5v5h5" /></svg>
                      Done
                    </button>
                  </div>
                  <p class="wallet-pass__back-meta">Leak repair · Thu 16 Oct, 10:00–12:00<br>Booking BR-4821</p>
                </div>
                <dl class="wallet-pass__notes">
                  <div><dt>Notes for Sam</dt><dd>Please clear the cupboard under the kitchen sink. Park on the drive; the side gate is open.</dd></div>
                  <div><dt>Cancellation policy</dt><dd>Free to reschedule or cancel until 8:00 on the day. After that, a $35 call-out fee applies.</dd></div>
                </dl>
              </div>

              <div class="wallet-pass__part wallet-pass__part--stub wallet-pass__part--actions">
                <div class="wallet-pass__actions">
                  <a class="wallet-pass__action wallet-pass__action--primary" download="brand-visit-BR-4821.ics" href="data:text/calendar;charset=utf-8,BEGIN:VCALENDAR%0D%0AVERSION:2.0%0D%0APRODID:-//Brand//Wallet%20pass//EN%0D%0ABEGIN:VEVENT%0D%0AUID:BR-4821@example.com%0D%0ADTSTAMP:20261013T090000Z%0D%0ADTSTART:20261016T100000%0D%0ADTEND:20261016T120000%0D%0ASUMMARY:Brand%20leak%20repair%0D%0ALOCATION:42%20Elm%20Street%5C,%20Westlake%5C,%20Springfield%0D%0ADESCRIPTION:Technician%20Sam%20Kowalski.%20Questions:%20(555)%20555-0123%0D%0AEND:VEVENT%0D%0AEND:VCALENDAR">
                    <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M8 2v4M16 2v4M3 9h18M5 4h14a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2zM12 12.5v5M9.5 15h5" /></svg>
                    Add to calendar
                  </a>
                  <a class="wallet-pass__action" href="https://www.google.com/maps/dir/?api=1&amp;destination=42+Elm+Street+Westlake+Springfield">
                    <svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><path d="M3 11 21 3l-8 18-2-8z" /></svg>
                    Get directions
                  </a>
                </div>
                <p class="wallet-pass__help">Questions? Call <a href="tel:+15555550123">(555) 555-0123</a></p>
              </div>
            </article>
          </div>
        </div>
      </div>

      <div class="wallet-pass__pocket" aria-hidden="true">
        <span class="wallet-pass__emboss">
          <svg viewBox="0 0 24 24" width="22" height="22" focusable="false"><path d="M3.5 11 12 4l8.5 7M6 9.5V20h12V9.5M10 20v-5.5h4V20" /></svg>
          Brand
        </span>
      </div>
      <button class="wallet-pass__show" type="button" hidden>
        <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="m6 15 6-6 6 6" /></svg>
        <span>Show pass</span>
      </button>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section: light, with a local leather palette mixed from tokens */
.wallet-pass {
  --wallet-pass-leather: color-mix(in srgb, var(--warning) 22%, var(--surface-deep));
  --wallet-pass-leather-hi: color-mix(in srgb, var(--warning) 34%, var(--surface-deep));
  --wallet-pass-leather-lo: color-mix(in srgb, var(--warning) 11%, var(--surface-deep));
  --wallet-pass-thread: color-mix(in srgb, var(--accent) 62%, var(--surface-deep));
  --wallet-pass-strip: linear-gradient(135deg, var(--primary-hover), color-mix(in srgb, var(--primary-2) 70%, var(--surface-deep)));
  --wallet-pass-grain: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='g'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.8' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2.4 -1.1'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23g)'/%3E%3C/svg%3E");
  --wallet-pass-notch: 0.75rem;   /* tear-line notch radius */
  --wallet-pass-pocket: 9rem;     /* front pocket height */
  --wallet-pass-overlap: 1.5rem;  /* pass left inside the pocket when it's out */
  --wallet-pass-peek: 5.5rem;     /* pass showing above the pocket when tucked */
  --wallet-pass-tuck: calc(100% - var(--wallet-pass-peek) - var(--wallet-pass-overlap));
  position: relative; isolation: isolate; overflow: clip;
  background:
    radial-gradient(50rem 28rem at 88% 8%, color-mix(in srgb, var(--primary) 8%, transparent), transparent 70%),
    linear-gradient(180deg, var(--surface-muted), var(--surface-light));
  color: var(--text-main); font-family: var(--font-sans);
}
.wallet-pass svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.wallet-pass__inner {
  display: grid; gap: 3.5rem; align-items: center;
  max-width: var(--container-max); margin-inline: auto;
  padding: clamp(4rem, 9vw, 7rem) var(--gutter);
}

/* Copy column */
.wallet-pass__eyebrow {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0;
  padding: 0.25rem 0.875rem 0.25rem 0.25rem; border-radius: var(--radius-full);
  background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm);
  font-size: 0.8125rem; font-weight: 600;
}
.wallet-pass__eyebrow svg { width: 0.875rem; height: 0.875rem; padding: 0.25rem; border-radius: 50%; background: var(--success); color: var(--surface-light); stroke-width: 3; }
.wallet-pass__title {
  margin: 1.25rem 0 0; font: 600 clamp(2rem, 1.3rem + 2.8vw, 3.25rem)/1.04 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.wallet-pass__lead { max-width: 31rem; margin: 1.25rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.wallet-pass__perks { display: grid; gap: 0.875rem; margin: 2rem 0 0; padding: 0; list-style: none; font-size: 0.9375rem; font-weight: 500; }
.wallet-pass__perks li { display: flex; align-items: center; gap: 0.875rem; }
.wallet-pass__perks svg {
  width: 1.125rem; height: 1.125rem; padding: 0.5rem; border-radius: 0.75rem;
  background: color-mix(in srgb, var(--primary) 8%, var(--surface-light)); color: var(--primary);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--primary) 14%, transparent), var(--highlight);
}

/* Stage: sleeve, pass and pocket share one grid cell */
.wallet-pass__stage { position: relative; display: grid; grid-template-columns: minmax(0, 23rem); justify-content: center; padding-top: 1rem; }
.wallet-pass__stage > * { grid-area: 1 / 1; }
.wallet-pass__stage::before { /* light pooling behind the wallet */
  content: ""; position: absolute; inset: -12% -30% 8%; z-index: -1; pointer-events: none;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--primary-2) 13%, transparent), color-mix(in srgb, var(--primary) 5%, transparent) 60%, transparent);
}
.wallet-pass__stage::after { /* contact shadow */
  content: ""; position: absolute; left: 4%; right: 4%; bottom: -1.5rem; height: 3rem; z-index: -1; pointer-events: none;
  background: radial-gradient(closest-side, color-mix(in srgb, var(--surface-deep) 32%, transparent), transparent);
}

/* Leather: grain is a turbulence mask, stitching a dashed inset */
.wallet-pass__sleeve, .wallet-pass__pocket { position: relative; align-self: end; }
.wallet-pass__sleeve {
  height: calc(var(--wallet-pass-pocket) + 2.75rem); border-radius: var(--radius-2xl);
  background: linear-gradient(180deg, color-mix(in srgb, var(--surface-deep) 60%, transparent), transparent 3rem), var(--wallet-pass-leather-lo);
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--accent) 16%, transparent), var(--shadow-xl);
}
.wallet-pass__pocket {
  z-index: 2; height: var(--wallet-pass-pocket); display: grid; justify-items: center; align-content: start; padding-top: 1.75rem;
  border-radius: 0.5rem 0.5rem var(--radius-2xl) var(--radius-2xl);
  background:
    radial-gradient(2.5rem 1.7rem at 50% 0, transparent 94%, color-mix(in srgb, var(--accent) 24%, var(--wallet-pass-leather)) 100%, transparent 118%),
    radial-gradient(140% 100% at 50% 0%, var(--wallet-pass-leather-hi), var(--wallet-pass-leather) 55%, var(--wallet-pass-leather-lo));
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--accent) 34%, transparent), inset 0 -1rem 1.5rem -1rem color-mix(in srgb, var(--surface-deep) 80%, transparent);
  -webkit-mask: radial-gradient(2.4rem 1.6rem at 50% 0, transparent 97%, black); /* thumb cut */
  mask: radial-gradient(2.4rem 1.6rem at 50% 0, transparent 97%, black);
}
.wallet-pass__sleeve::before, .wallet-pass__pocket::before {
  content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none; opacity: 0.4;
  background: color-mix(in srgb, var(--accent) 45%, var(--wallet-pass-leather));
  -webkit-mask: var(--wallet-pass-grain) 0 0 / 180px 180px;
  mask: var(--wallet-pass-grain) 0 0 / 180px 180px;
}
.wallet-pass__sleeve::after, .wallet-pass__pocket::after {
  content: ""; position: absolute; inset: 0.5rem; pointer-events: none; opacity: 0.6;
  border: 1.5px dashed var(--wallet-pass-thread); border-radius: calc(var(--radius-2xl) - 0.5rem);
}
.wallet-pass__pocket::after { top: 1rem; border-top: 0; border-radius: 0 0 calc(var(--radius-2xl) - 0.5rem) calc(var(--radius-2xl) - 0.5rem); }
.wallet-pass__emboss {
  display: grid; justify-items: center; gap: 0.375rem;
  color: color-mix(in srgb, var(--wallet-pass-leather) 55%, var(--surface-deep));
  font: 700 0.75rem/1 var(--font-display); letter-spacing: 0.4em; text-indent: 0.4em; text-transform: uppercase;
  text-shadow: 0 1px 0 color-mix(in srgb, var(--accent) 20%, var(--wallet-pass-leather));
}
.wallet-pass__emboss svg { filter: drop-shadow(0 1px 0 color-mix(in srgb, var(--accent) 20%, var(--wallet-pass-leather))); }

/* Show / tuck button, stitched onto the pocket */
.wallet-pass__show {
  position: relative; z-index: 3; align-self: end; justify-self: center; margin-bottom: 1.25rem;
  display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1.25rem 0 1rem;
  border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: color-mix(in srgb, var(--text-inverse) 10%, transparent); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse), 0 8px 18px -8px color-mix(in srgb, var(--surface-deep) 90%, transparent);
  font: 600 0.875rem/1 var(--font-sans);
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.wallet-pass__show[hidden] { display: none; }
.wallet-pass__show:hover { background: color-mix(in srgb, var(--text-inverse) 16%, transparent); }
.wallet-pass__show:active { transform: scale(0.96); }
.wallet-pass__show svg { transition: rotate var(--dur-4) var(--ease-spring); }
.wallet-pass.is-out .wallet-pass__show svg { rotate: 180deg; }

/* The slot clips the pass at the pocket's bottom edge; the lift slides it */
.wallet-pass__slot {
  position: relative; z-index: 1;
  padding: 0 0.75rem calc(var(--wallet-pass-pocket) - var(--wallet-pass-overlap));
  clip-path: inset(-50% -50% 0 -50%);
}
.wallet-pass__lift {
  filter: drop-shadow(0 1px 1px color-mix(in srgb, var(--surface-deep) 18%, transparent)) drop-shadow(0 16px 24px color-mix(in srgb, var(--surface-deep) 26%, transparent));
}
@media (scripting: enabled) {
  .wallet-pass:not(.is-out) .wallet-pass__lift { translate: 0 var(--wallet-pass-tuck); }
  .wallet-pass:not(.wallet-pass--js) .wallet-pass__lift { animation: wallet-pass-failsafe 1ms 2.5s forwards; } /* script never ran */
}
.wallet-pass--js:not(.is-out) .wallet-pass__lift { translate: 0 var(--wallet-pass-tuck); }
.wallet-pass--js .wallet-pass__lift { transition: translate var(--dur-5) var(--ease-spring); }

/* Faces: two stacked cards without JS; one 3D flip card with JS (subgrid keeps the notches level) */
.wallet-pass__flipper { display: grid; gap: 1rem; }
.wallet-pass__face { display: grid; }
.wallet-pass--js .wallet-pass__flipper {
  grid-template-rows: auto auto; gap: 0; transform-style: preserve-3d;
  transform: perspective(1600px) rotateY(0deg); transition: transform var(--dur-5) var(--ease-spring);
}
.wallet-pass--js .wallet-pass__face {
  grid-area: 1 / 1 / 3 / 2; grid-template-rows: subgrid;
  -webkit-backface-visibility: hidden; backface-visibility: hidden; transition: visibility 0s;
}
.wallet-pass--js .wallet-pass__face--back { transform: rotateY(180deg); }
.wallet-pass--js .wallet-pass__face[inert] { visibility: hidden; transition-delay: var(--dur-3); }
.wallet-pass.is-flipped .wallet-pass__flipper { transform: perspective(1600px) rotateY(180deg); }

/* Halves of the pass: radial-gradient masks cut the tear-line notches */
.wallet-pass__part {
  --wallet-pass-y: 100%;
  position: relative; overflow: hidden; background: var(--surface-light);
  -webkit-mask:
    radial-gradient(circle at 0 var(--wallet-pass-y), transparent var(--wallet-pass-notch), black calc(var(--wallet-pass-notch) + 0.5px)) 0 0 / 51% 100% no-repeat,
    radial-gradient(circle at 100% var(--wallet-pass-y), transparent var(--wallet-pass-notch), black calc(var(--wallet-pass-notch) + 0.5px)) 100% 0 / 51% 100% no-repeat;
  mask:
    radial-gradient(circle at 0 var(--wallet-pass-y), transparent var(--wallet-pass-notch), black calc(var(--wallet-pass-notch) + 0.5px)) 0 0 / 51% 100% no-repeat,
    radial-gradient(circle at 100% var(--wallet-pass-y), transparent var(--wallet-pass-notch), black calc(var(--wallet-pass-notch) + 0.5px)) 100% 0 / 51% 100% no-repeat;
}
.wallet-pass__part--main { border-radius: var(--radius-xl) var(--radius-xl) 0 0; }
.wallet-pass__part--stub {
  --wallet-pass-y: 0%;
  display: flex; align-items: center; gap: 1rem;
  padding: 1.25rem 1.25rem calc(1.25rem + var(--wallet-pass-overlap));
  border-radius: 0 0 var(--radius-xl) var(--radius-xl);
  box-shadow: inset 0 12px 14px -14px color-mix(in srgb, var(--surface-deep) 22%, transparent);
}
.wallet-pass__part--stub::before { /* perforation */
  content: ""; position: absolute; top: 0; left: calc(var(--wallet-pass-notch) + 0.5rem); right: calc(var(--wallet-pass-notch) + 0.5rem); height: 2px;
  background: repeating-linear-gradient(90deg, color-mix(in srgb, var(--text-muted) 45%, transparent) 0 0.375rem, transparent 0.375rem 0.6875rem);
}

/* Front: gradient strip */
.wallet-pass__strip {
  display: grid; gap: 1.5rem; padding: 1rem 1.25rem 1.25rem; color: var(--text-inverse);
  background:
    repeating-radial-gradient(circle at 100% 0, transparent 0 0.75rem, color-mix(in srgb, var(--text-inverse) 7%, transparent) 0.75rem calc(0.75rem + 1px)),
    radial-gradient(90% 120% at 0% 0%, color-mix(in srgb, var(--primary) 40%, transparent), transparent 60%),
    var(--wallet-pass-strip);
}
.wallet-pass__bar { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 0.75rem; }
.wallet-pass__logo { display: inline-flex; align-items: center; gap: 0.5rem; font: 600 1.0625rem/1 var(--font-display); letter-spacing: var(--tracking-tight); }
.wallet-pass__mark {
  display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: 0.625rem;
  background: color-mix(in srgb, var(--surface-deep) 22%, transparent);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-inverse) 20%, transparent), var(--highlight-inverse);
}
.wallet-pass__chip {
  display: inline-flex; align-items: center; gap: 0.3125rem; padding: 0.3125rem 0.625rem 0.3125rem 0.5rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 28%, transparent); font-size: 0.75rem; font-weight: 600;
}
.wallet-pass__chip svg { color: color-mix(in srgb, var(--success) 45%, var(--text-inverse)); stroke-width: 3; }
.wallet-pass__headline { display: grid; gap: 0.5rem; margin: 0; font-weight: 400; }
.wallet-pass__service { font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.wallet-pass__date { font: 600 2.25rem/0.95 var(--font-display); letter-spacing: var(--tracking-display); }

/* Front: fields */
.wallet-pass__fields { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem 1.25rem; margin: 0; padding: 1.125rem 1.25rem 1.375rem; }
.wallet-pass__field--wide { grid-column: 1 / -1; }
.wallet-pass__fields dt, .wallet-pass__code-label { color: var(--text-muted); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.08em; text-transform: uppercase; }
.wallet-pass__fields dd { margin: 0.4375rem 0 0; font-size: 0.9375rem; line-height: 1.3; }
.wallet-pass__fields strong { font-weight: 600; font-variant-numeric: tabular-nums; }
.wallet-pass__tech { display: flex; align-items: center; gap: 0.75rem; }
.wallet-pass__tech strong, .wallet-pass__tech small { display: block; }
.wallet-pass__tech small { margin-top: 0.125rem; color: var(--text-muted); font-size: 0.8125rem; }
.wallet-pass__avatar {
  flex: none; display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 50%;
  background: var(--wallet-pass-strip); color: var(--text-inverse); font-size: 0.75rem; font-weight: 700;
  box-shadow: 0 0 0 2px var(--surface-light), 0 0 0 3px var(--border-subtle);
}

/* Front: QR stub */
.wallet-pass .wallet-pass__qr {
  width: 6rem; height: 6rem; border-radius: 0.875rem; background: var(--surface-light);
  box-shadow: inset 0 0 0 1px var(--border-subtle); color: var(--text-main); fill: currentColor; stroke: none;
}
.wallet-pass__qr rect { shape-rendering: crispEdges; }
.wallet-pass__qr [rx] { shape-rendering: geometricPrecision; }
.wallet-pass__qr .wallet-pass__eye { fill: none; stroke: currentColor; stroke-width: 1; }
.wallet-pass__code { min-width: 0; }
.wallet-pass__code p { margin: 0; }
.wallet-pass__code .wallet-pass__code-value { margin-top: 0.375rem; font: 600 1.25rem/1 var(--font-mono); letter-spacing: 0.04em; }
.wallet-pass__code .wallet-pass__code-note { margin-top: 0.375rem; color: var(--text-muted); font-size: 0.8125rem; line-height: 1.4; }

/* Flip buttons */
.wallet-pass__flip {
  display: inline-flex; align-items: center; gap: 0.375rem; height: 2.25rem; margin-top: 0.75rem; padding: 0 0.875rem 0 0.625rem;
  border: 0; border-radius: var(--radius-full); cursor: pointer;
  background: var(--surface-muted); color: var(--text-main); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight);
  font: 600 0.8125rem/1 var(--font-sans);
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.wallet-pass__flip[hidden] { display: none; }
.wallet-pass__flip:hover { background: var(--border-subtle); }
.wallet-pass__flip:active { transform: scale(0.95); }
.wallet-pass__flip--done {
  margin-top: 0; background: color-mix(in srgb, var(--text-inverse) 10%, transparent); color: var(--text-inverse);
  box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
}
.wallet-pass__flip--done:hover { background: color-mix(in srgb, var(--text-inverse) 16%, transparent); }

/* Back */
.wallet-pass__strip--back {
  gap: 1rem;
  background:
    repeating-radial-gradient(circle at 0 0, transparent 0 0.75rem, color-mix(in srgb, var(--text-inverse) 5%, transparent) 0.75rem calc(0.75rem + 1px)),
    linear-gradient(160deg, var(--surface-dark), var(--surface-deep));
}
.wallet-pass__back-title { margin: 0; border-radius: 0.375rem; font: 600 1.375rem/1.1 var(--font-display); letter-spacing: var(--tracking-tight); }
.wallet-pass__back-meta { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem/1.6 var(--font-mono); }
.wallet-pass__notes { display: grid; gap: 1rem; margin: 0; padding: 1.125rem 1.25rem 1.375rem; }
.wallet-pass__notes dt { font-size: 0.8125rem; font-weight: 600; }
.wallet-pass__notes dd { margin: 0.25rem 0 0; color: var(--text-muted); font-size: 0.875rem; line-height: 1.5; }
.wallet-pass__part--actions { flex-direction: column; align-items: stretch; justify-content: center; }
.wallet-pass__actions { display: flex; flex-wrap: wrap; gap: 0.5rem; }
.wallet-pass__action {
  flex: 1 1 auto; display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem; height: 2.75rem; padding: 0 1rem;
  border-radius: var(--radius-full); background: var(--surface-muted); color: var(--text-main); white-space: nowrap;
  box-shadow: inset 0 0 0 1px var(--border-subtle), var(--highlight);
  font-size: 0.875rem; font-weight: 600; text-decoration: none;
  transition: background-color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.wallet-pass__action:hover { background: var(--border-subtle); }
.wallet-pass__action:active { transform: scale(0.97); }
.wallet-pass__action--primary {
  background: var(--text-main); color: var(--surface-light);
  box-shadow: var(--highlight-inverse), 0 10px 20px -12px color-mix(in srgb, var(--text-main) 80%, transparent);
}
.wallet-pass__action--primary:hover { background: color-mix(in srgb, var(--text-main) 88%, var(--primary)); }
.wallet-pass__help { margin: 0; color: var(--text-muted); font-size: 0.8125rem; text-align: center; }
.wallet-pass__help a { border-radius: 0.25rem; color: var(--text-main); font-weight: 600; text-underline-offset: 0.2em; }
.wallet-pass__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Focus: ring on light surfaces, white outline on leather and the dark strip */
.wallet-pass :is(.wallet-pass__flip:not(.wallet-pass__flip--done), .wallet-pass__action, .wallet-pass__help a):focus-visible { outline: 2px solid transparent; box-shadow: var(--focus-ring); }
.wallet-pass :is(.wallet-pass__show, .wallet-pass__flip--done, .wallet-pass__back-title):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

/* Shine: one sweep per part, skewed about the tear line so the band lines up across it */
.wallet-pass__face--front .wallet-pass__part::after {
  content: ""; position: absolute; inset: 0; pointer-events: none;
  background: linear-gradient(90deg, transparent 30%, color-mix(in srgb, var(--primary-2) 16%, transparent) 42%, color-mix(in srgb, var(--surface-light) 50%, transparent) 50%, color-mix(in srgb, var(--primary) 16%, transparent) 58%, transparent 70%);
  transform: translateX(-130%) skewX(-24deg); transform-origin: 50% 100%;
}
.wallet-pass__face--front .wallet-pass__part--stub::after { transform-origin: 50% 0; }
.wallet-pass.is-shine .wallet-pass__face--front .wallet-pass__part::after { animation: wallet-pass-shine calc(var(--dur-5) * 1.25) var(--ease-in-out) both; }

@media (min-width: 400px) {
  .wallet-pass__slot { padding-inline: 1rem; }
}
@media (min-width: 768px) {
  .wallet-pass__inner { grid-template-columns: minmax(0, 1fr) minmax(0, 22rem); gap: 3rem; }
}
@media (min-width: 1024px) {
  .wallet-pass__inner { grid-template-columns: minmax(0, 1fr) minmax(0, 24rem); gap: 6rem; }
}
@media (prefers-reduced-motion: reduce) {
  .wallet-pass__part::after { animation: none !important; }
}
@keyframes wallet-pass-shine {
  from { transform: translateX(-130%) skewX(-24deg); }
  to { transform: translateX(130%) skewX(-24deg); }
}
@keyframes wallet-pass-failsafe { to { translate: 0 0; } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-wallet-pass]').forEach((root) => {
  const stage = root.querySelector('.wallet-pass__stage');
  const lift = root.querySelector('.wallet-pass__lift');
  const [front, back] = root.querySelectorAll('.wallet-pass__face');
  const [details, done] = root.querySelectorAll('.wallet-pass__flip');
  const show = root.querySelector('.wallet-pass__show');
  const label = show.querySelector('span');
  root.classList.add('wallet-pass--js');

  // Flip: the face turned away is inert, so it leaves the tab order and the accessibility tree
  const flip = (toBack, moveFocus) => {
    root.classList.toggle('is-flipped', toBack);
    front.inert = toBack;
    back.inert = !toBack;
    if (moveFocus) (toBack ? back.querySelector('h3') : details).focus();
  };

  // In or out of the pocket; nothing hidden by the pocket can take focus
  const setOut = (out) => {
    root.classList.toggle('is-out', out);
    lift.inert = !out;
    label.textContent = out ? 'Tuck away' : 'Show pass';
    if (!out) flip(false);
  };

  // Once the spring settles, sweep the shine across the front (never under reduced motion)
  lift.addEventListener('transitionend', (e) => {
    if (e.target === lift && e.propertyName === 'translate' && root.classList.contains('is-out') && !reduce.matches) {
      root.classList.add('is-shine');
    }
  });
  root.addEventListener('animationend', (e) => {
    if (e.animationName === 'wallet-pass-shine') root.classList.remove('is-shine');
  });

  details.addEventListener('click', () => flip(true, true));
  done.addEventListener('click', () => flip(false, true));
  back.addEventListener('keydown', (e) => { if (e.key === 'Escape') flip(false, true); });
  show.addEventListener('click', () => setOut(!root.classList.contains('is-out')));
  [details, done, show].forEach((button) => { button.hidden = false; });
  setOut(false);

  // Slide out the first time the holder is mostly in view
  const io = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    io.disconnect();
    setTimeout(() => setOut(true), 250);
  }, { threshold: 0.45 });
  io.observe(stage);
});
```

## Notes

- The two faces are `<article>`s with their own headings. The face that's turned away is `inert` (and `visibility: hidden` once the turn passes edge-on), so it leaves the tab order and the accessibility tree. "Details" moves focus to the back's heading; "Done" or Escape flips back and returns focus to "Details". While the pass is tucked the whole pass is `inert`, so nothing covered by the pocket can take focus. "Show pass" / "Tuck away" is a plain button whose label follows the state.
- Without JS, the pass sits out of the pocket and both faces show as two stacked cards, with the flip and show buttons left `hidden`. With scripting on, `@media (scripting: enabled)` tucks the pass from the first paint, so it never flashes out and back in. If the script fails, a 2.5s CSS failsafe brings the pass out anyway.
- Reduced motion: the slide and the flip become instant because the duration tokens collapse, and the shine never runs (JS skips it and CSS removes the keyframes).
- Contrast: white text on the pass strip is at least 5.2:1 everywhere across the blue-to-teal gradient, its rings and its bloom; "Confirmed" on its dark chip is 8.8:1; "Show pass" on the leather is 11.8:1; and the back-face meta (`--text-inverse-muted` on `--surface-dark`) is 7:1.
- The notches are `radial-gradient` masks on the two halves of the pass, and the shadow is a `filter: drop-shadow()` on the wrapper, so it follows the cut-outs. Subgrid keeps the notches at the same height on both faces (Chrome 117+, Safari 16+, Firefox 71+); in older browsers each face sizes on its own. The shine is skewed about the tear line in each half, so the band lines up across the perforation.
- To adapt it, retheme the leather (`--wallet-pass-leather*`, `--wallet-pass-thread`) or the strip (`--wallet-pass-strip`) on the root. The "Add to calendar" link is a self-contained .ics data URI; in production, point it at your calendar endpoint and replace the demo QR rects with the real code from your backend.
