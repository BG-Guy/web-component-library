# Blueprint Draw

A pinned blueprint sheet on grid paper. As you scroll, a section drawing of a house drafts itself stroke by stroke: footings, walls, roof trusses, stairs, windows, services, then dimension lines whose figures count up. When the plan is done, four amber "markup" callouts pop in with leader lines. On phones the sheet scales to fit the stage and the callouts become numbered pins with a legend underneath. Depends on `tokens/variables.css`.

**Motion:** scroll-scrubbed stroke draw (linear, per-path ranges from `--blueprint-draw-from`/`--blueprint-draw-to`) · poché and hatch fade · dimension count-up (cubic ease-out in JS) · callout leader draw (`--dur-4` `--ease-out`) · label and pin pop (`--ease-spring`, delayed by `--dur-3`) · drafting meter fill.

## HTML

```html
<div class="blueprint-draw-demo">
  <div class="blueprint-draw-demo__intro">
    <p class="blueprint-draw-demo__kicker">Pre-construction</p>
    <p class="blueprint-draw-demo__line">Scroll to watch the plan come together.</p>
    <span class="blueprint-draw-demo__hint" aria-hidden="true">Scroll
      <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
    </span>
  </div>

  <section class="blueprint-draw" aria-labelledby="blueprint-draw-title" data-blueprint-draw>
    <div class="blueprint-draw__stage">
      <div class="blueprint-draw__inner">
        <div class="blueprint-draw__copy">
          <p class="blueprint-draw__eyebrow">
            <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M4 20h4L19 9a2.1 2.1 0 0 0-3-3L5 17zM14 8l2 2" /></svg>
            Pre-construction · Sheet A-301
          </p>
          <h2 id="blueprint-draw-title" class="blueprint-draw__title">Every job starts with a plan.</h2>
          <div class="blueprint-draw__body">
            <p class="blueprint-draw__lead">Before a wall opens, we draw your home: structure, services and code notes on one sheet. The price you sign is the job we build.</p>
            <ul class="blueprint-draw__checks" role="list">
              <li>Measured site survey</li>
              <li>Load, code and permit review</li>
              <li>Fixed price from the drawing</li>
            </ul>
            <div class="blueprint-draw__actions">
              <a class="blueprint-draw__btn" href="#survey">
                Book a site survey
                <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
              </a>
            </div>
            <div class="blueprint-draw__meter" aria-hidden="true"><span>Drafting</span><span class="blueprint-draw__track"></span><span>A-301</span></div>
          </div>
        </div>

        <div class="blueprint-draw__figure">
          <div class="blueprint-draw__plate">
            <div class="blueprint-draw__sheet">
              <svg class="blueprint-draw__svg" viewBox="0 0 960 640" role="img" aria-labelledby="blueprint-draw-art-title" focusable="false">
                <title id="blueprint-draw-art-title">Section drawing of a two-storey house: roof trusses over attic insulation, a stair between floors, plumbing supply lines up to the bathroom, and an electrical panel and sump pump in the basement.</title>
                <defs>
                  <pattern id="blueprint-draw-hatch" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
                    <path class="blueprint-draw__hatch" d="M0 0V9" />
                  </pattern>
                  <mask id="blueprint-draw-fade" maskUnits="userSpaceOnUse" x="0" y="0" width="960" height="640">
                    <radialGradient id="blueprint-draw-fade-fill" gradientUnits="userSpaceOnUse" cx="392" cy="470" r="330" gradientTransform="matrix(1 0 0 .42 0 272.6)">
                      <stop offset=".55" stop-color="white" /><stop offset="1" stop-color="black" />
                    </radialGradient>
                    <rect width="960" height="640" fill="url(#blueprint-draw-fade-fill)" />
                  </mask>
                </defs>

                <g class="blueprint-draw__art">
                  <!-- Sheet border and drawing title -->
                  <g style="--blueprint-draw-from: 0; --blueprint-draw-to: .07">
                    <path class="blueprint-draw__l3" d="M12 12H948V628H12Z" pathLength="1" />
                    <path class="blueprint-draw__l2" d="M20 20H940V620H20Z" pathLength="1" />
                  </g>
                  <g style="--blueprint-draw-from: .03; --blueprint-draw-to: .1">
                    <path class="blueprint-draw__l2" d="M30 52a18 18 0 1 0 36 0a18 18 0 1 0-36 0" pathLength="1" />
                    <path class="blueprint-draw__l3" d="M30 52H66" pathLength="1" />
                    <path class="blueprint-draw__l1" d="M76 56H190" pathLength="1" />
                    <text class="blueprint-draw__strong" x="48" y="47" text-anchor="middle">A</text>
                    <text class="blueprint-draw__tiny" x="48" y="64" text-anchor="middle">A-301</text>
                    <text class="blueprint-draw__strong" x="76" y="50">SECTION A–A</text>
                    <text x="76" y="68">SCALE 1/4" = 1'-0"</text>
                  </g>

                  <!-- Ground: grade line and hatched earth -->
                  <g style="--blueprint-draw-from: .05; --blueprint-draw-to: .13">
                    <g mask="url(#blueprint-draw-fade)">
                      <path class="blueprint-draw__earth" d="M198 470V562H186V590H28V470Z" />
                      <path class="blueprint-draw__earth" d="M586 470V562H598V590H704V470Z" />
                    </g>
                    <path class="blueprint-draw__l1" d="M198 470H40" pathLength="1" />
                    <path class="blueprint-draw__l1" d="M586 470H700" pathLength="1" />
                  </g>

                  <!-- Footings, foundation walls, drain tile -->
                  <g class="blueprint-draw__l1" style="--blueprint-draw-from: .1; --blueprint-draw-to: .18">
                    <path class="blueprint-draw__cut" d="M186 562H222V578H186Z" pathLength="1" />
                    <path class="blueprint-draw__cut" d="M562 562H598V578H562Z" pathLength="1" />
                    <path class="blueprint-draw__cut" d="M198 562V458H210V562Z" pathLength="1" />
                    <path class="blueprint-draw__cut" d="M586 562V458H574V562Z" pathLength="1" />
                  </g>
                  <g class="blueprint-draw__l3" style="--blueprint-draw-from: .15; --blueprint-draw-to: .19">
                    <path d="M174 571a4 4 0 1 0 8 0a4 4 0 1 0-8 0" pathLength="1" />
                    <path d="M602 571a4 4 0 1 0 8 0a4 4 0 1 0-8 0" pathLength="1" />
                  </g>

                  <!-- Slab, floors, walls, ceiling -->
                  <g class="blueprint-draw__l1" style="--blueprint-draw-from: .16; --blueprint-draw-to: .24">
                    <path class="blueprint-draw__cut" d="M210 554H574V562H210Z" pathLength="1" />
                    <path class="blueprint-draw__cut" d="M208 458V446H576V458Z" pathLength="1" />
                  </g>
                  <g class="blueprint-draw__l1" style="--blueprint-draw-from: .21; --blueprint-draw-to: .3">
                    <path class="blueprint-draw__cut" d="M200 458V230H208V458Z" pathLength="1" />
                    <path class="blueprint-draw__cut" d="M584 458V230H576V458Z" pathLength="1" />
                  </g>
                  <g class="blueprint-draw__l1" style="--blueprint-draw-from: .27; --blueprint-draw-to: .34">
                    <path class="blueprint-draw__cut" d="M208 338V326H372V338Z" pathLength="1" />
                    <path class="blueprint-draw__cut" d="M576 338V326H486V338Z" pathLength="1" />
                    <path class="blueprint-draw__cut" d="M200 230V224H584V230Z" pathLength="1" />
                  </g>

                  <!-- Roof: rafters, sheathing, eaves, Fink truss webs, vent stack -->
                  <g class="blueprint-draw__l1" style="--blueprint-draw-from: .32; --blueprint-draw-to: .43">
                    <path d="M176 246L392 102L608 246" pathLength="1" />
                    <path d="M170 238L392 90L614 238" pathLength="1" />
                  </g>
                  <g class="blueprint-draw__l2" style="--blueprint-draw-from: .4; --blueprint-draw-to: .5">
                    <path d="M170 238V252H200" pathLength="1" style="--blueprint-draw-to: .45" />
                    <path d="M614 238V252H584" pathLength="1" style="--blueprint-draw-to: .45" />
                    <path d="M296 166L328 224L392 102L456 224L488 166" pathLength="1" style="--blueprint-draw-from: .42" />
                    <path d="M536 224V176H544V224" pathLength="1" style="--blueprint-draw-from: .47" />
                  </g>

                  <!-- Stair, stringer, handrail -->
                  <g class="blueprint-draw__l2" style="--blueprint-draw-from: .47; --blueprint-draw-to: .56">
                    <path d="M336 446v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5h10v-7.5" pathLength="1" />
                    <path d="M349 446L486 343.5V338" pathLength="1" style="--blueprint-draw-from: .5" />
                    <path d="M338 446V402L486 291V326" pathLength="1" style="--blueprint-draw-from: .52; --blueprint-draw-to: .58" />
                  </g>

                  <!-- Windows and door, seen beyond the cut -->
                  <g class="blueprint-draw__l2" style="--blueprint-draw-from: .52; --blueprint-draw-to: .6">
                    <path d="M226 362H302V420H226Z" pathLength="1" />
                    <path d="M264 362V420" pathLength="1" />
                    <path d="M226 391H302" pathLength="1" />
                    <path class="blueprint-draw__l1" d="M218 421.5H310" pathLength="1" />
                    <path d="M228 254H292V300H228Z" pathLength="1" />
                    <path d="M260 254V300" pathLength="1" />
                    <path d="M228 277H292" pathLength="1" />
                    <path class="blueprint-draw__l1" d="M222 301.5H298" pathLength="1" />
                  </g>
                  <g class="blueprint-draw__l2" style="--blueprint-draw-from: .55; --blueprint-draw-to: .62">
                    <path d="M500 446V366H540V446" pathLength="1" />
                    <path d="M507 373H533V400H507Z" pathLength="1" />
                    <path d="M507 408H533V438H507Z" pathLength="1" />
                    <path d="M533.4 404a1.6 1.6 0 1 0 3.2 0a1.6 1.6 0 1 0-3.2 0" pathLength="1" />
                  </g>

                  <!-- Bathroom: vanity, basin, faucet, mirror -->
                  <g class="blueprint-draw__l2" style="--blueprint-draw-from: .58; --blueprint-draw-to: .65">
                    <path d="M500 326V294H548V326" pathLength="1" />
                    <path class="blueprint-draw__l1" d="M494 294H554" pathLength="1" />
                    <path d="M512 294q12 11 24 0" pathLength="1" />
                    <path d="M522 294V285q0-5 6-5h3" pathLength="1" />
                    <path d="M506 252H542V280H506Z" pathLength="1" />
                  </g>

                  <!-- Services: water heater, PEX supply, panel, sump pump -->
                  <g class="blueprint-draw__l2" style="--blueprint-draw-from: .6; --blueprint-draw-to: .72">
                    <path d="M236 554V500a16 6 0 0 1 32 0V554" pathLength="1" style="--blueprint-draw-to: .65" />
                    <path d="M262 495V484Q262 478 268 478H556Q562 478 562 472V312Q562 306 556 306H548" pathLength="1" style="--blueprint-draw-from: .62" />
                    <path d="M222 554V478Q222 472 228 472H550Q556 472 556 466V318Q556 312 550 312H548" pathLength="1" style="--blueprint-draw-from: .62" />
                    <path d="M548 486H574V524H548Z" pathLength="1" style="--blueprint-draw-from: .64; --blueprint-draw-to: .69" />
                    <path class="blueprint-draw__l3" d="M553 492H569V496H553V500H569V504H553V508H569V512H553V516H569" pathLength="1" style="--blueprint-draw-from: .66; --blueprint-draw-to: .7" />
                    <path class="blueprint-draw__l1" d="M512 554V600H548V554" pathLength="1" style="--blueprint-draw-from: .64; --blueprint-draw-to: .69" />
                    <path d="M522 578H538V598H522Z" pathLength="1" style="--blueprint-draw-from: .66" />
                    <path d="M538 586H541a3 3 0 1 0 6 0a3 3 0 1 0-6 0" pathLength="1" style="--blueprint-draw-from: .67" />
                    <path d="M530 578V536Q530 530 536 530H586L668 537" pathLength="1" style="--blueprint-draw-from: .66" />
                    <path class="blueprint-draw__l3" d="M526 538H534V550H526Z" pathLength="1" style="--blueprint-draw-from: .68" />
                  </g>

                  <!-- Attic insulation, landscape -->
                  <g class="blueprint-draw__l2" style="--blueprint-draw-from: .66; --blueprint-draw-to: .76">
                    <path d="M236 216a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0a8 8 0 0 1 16 0a4 8 0 0 1-8 0" pathLength="1" />
                    <path d="M84 470V417" pathLength="1" style="--blueprint-draw-from: .68; --blueprint-draw-to: .71" />
                    <path d="M84 363A11 11 0 0 1 101.4 369.3A11 11 0 0 1 110.6 385.3A11 11 0 0 1 107.4 403.5A11 11 0 0 1 93.2 415.4A11 11 0 0 1 74.8 415.4A11 11 0 0 1 60.6 403.5A11 11 0 0 1 57.4 385.3A11 11 0 0 1 66.6 369.3A11 11 0 0 1 84 363" pathLength="1" style="--blueprint-draw-from: .69; --blueprint-draw-to: .75" />
                    <path d="M606 470a9 9 0 0 1 8-13a10 10 0 0 1 18-2a8 8 0 0 1 10 15" pathLength="1" style="--blueprint-draw-from: .69; --blueprint-draw-to: .74" />
                  </g>

                  <!-- Room names -->
                  <g style="--blueprint-draw-from: .7; --blueprint-draw-to: .76">
                    <text x="392" y="204" text-anchor="middle">ATTIC</text>
                    <text x="330" y="296" text-anchor="middle">BEDROOM</text>
                    <text x="524" y="244" text-anchor="middle">BATH</text>
                    <text x="264" y="438" text-anchor="middle">LIVING</text>
                    <text x="520" y="358" text-anchor="middle">ENTRY</text>
                    <text x="392" y="520" text-anchor="middle">BASEMENT</text>
                  </g>

                  <!-- Dimensions: extension lines, dimension lines, arrowheads, figures (inches) -->
                  <g class="blueprint-draw__l3" style="--blueprint-draw-from: .72; --blueprint-draw-to: .76">
                    <path d="M380 90H142" pathLength="1" />
                    <path d="M196 446H168" pathLength="1" />
                    <path d="M196 326H168" pathLength="1" />
                    <path d="M200 584V618" pathLength="1" />
                    <path d="M584 584V618" pathLength="1" />
                  </g>
                  <g class="blueprint-draw__l3" style="--blueprint-draw-from: .74; --blueprint-draw-to: .82">
                    <path d="M150 470V90" pathLength="1" />
                    <path d="M176 446V326" pathLength="1" />
                    <path d="M200 610H584" pathLength="1" />
                    <text class="blueprint-draw__fig" x="142" y="280" transform="rotate(-90 142 280)" text-anchor="middle" data-blueprint-draw-count="380">31'-8"</text>
                    <text class="blueprint-draw__fig" x="168" y="386" transform="rotate(-90 168 386)" text-anchor="middle" data-blueprint-draw-count="120">10'-0"</text>
                    <text class="blueprint-draw__fig" x="392" y="604" text-anchor="middle" data-blueprint-draw-count="384">32'-0"</text>
                  </g>
                  <g class="blueprint-draw__l3" style="--blueprint-draw-from: .8; --blueprint-draw-to: .84">
                    <path class="blueprint-draw__solid" d="M146.5 99L150 90L153.5 99Z" pathLength="1" />
                    <path class="blueprint-draw__solid" d="M146.5 461L150 470L153.5 461Z" pathLength="1" />
                    <path class="blueprint-draw__solid" d="M172.5 335L176 326L179.5 335Z" pathLength="1" />
                    <path class="blueprint-draw__solid" d="M172.5 437L176 446L179.5 437Z" pathLength="1" />
                    <path class="blueprint-draw__solid" d="M209 606.5L200 610L209 613.5Z" pathLength="1" />
                    <path class="blueprint-draw__solid" d="M575 606.5L584 610L575 613.5Z" pathLength="1" />
                  </g>

                  <!-- Roof pitch and north arrow -->
                  <g class="blueprint-draw__l3" style="--blueprint-draw-from: .8; --blueprint-draw-to: .86">
                    <path d="M262 130H298V106Z" pathLength="1" />
                    <text x="280" y="142" text-anchor="middle">12</text>
                    <text x="305" y="121">8</text>
                    <path d="M874 76a22 22 0 1 0 44 0a22 22 0 1 0-44 0" pathLength="1" />
                    <path class="blueprint-draw__l2" d="M896 52L905 94L896 87L887 94Z" pathLength="1" />
                    <path class="blueprint-draw__solid" d="M896 52L896 87L887 94Z" />
                    <path class="blueprint-draw__l2" d="M890 44V31L902 44V31" pathLength="1" />
                  </g>
                </g>

                <!-- Markup leaders (desktop) -->
                <g class="blueprint-draw__leaders">
                  <path d="M420 216L474 150H640" pathLength="1" style="--blueprint-draw-at: .87" />
                  <path d="M562 392L604 300H640" pathLength="1" style="--blueprint-draw-at: .9" />
                  <path d="M561 505L604 430H640" pathLength="1" style="--blueprint-draw-at: .93" />
                  <path d="M530 590L604 575H640" pathLength="1" style="--blueprint-draw-at: .96" />
                </g>
              </svg>

              <span class="blueprint-draw__pin" style="--blueprint-draw-x: 420; --blueprint-draw-y: 216; --blueprint-draw-at: .87" aria-hidden="true">1</span>
              <span class="blueprint-draw__pin" style="--blueprint-draw-x: 562; --blueprint-draw-y: 392; --blueprint-draw-at: .9" aria-hidden="true">2</span>
              <span class="blueprint-draw__pin" style="--blueprint-draw-x: 561; --blueprint-draw-y: 505; --blueprint-draw-at: .93" aria-hidden="true">3</span>
              <span class="blueprint-draw__pin" style="--blueprint-draw-x: 530; --blueprint-draw-y: 590; --blueprint-draw-at: .96" aria-hidden="true">4</span>
            </div>
          </div>

          <ol class="blueprint-draw__notes" role="list" aria-label="Plan notes">
            <li class="blueprint-draw__note" style="--blueprint-draw-x: 640; --blueprint-draw-y: 150; --blueprint-draw-at: .87">
              <span class="blueprint-draw__num" aria-hidden="true">1</span>
              <span><strong>R-49 attic insulation</strong><small>16 in blown cellulose</small></span>
            </li>
            <li class="blueprint-draw__note" style="--blueprint-draw-x: 640; --blueprint-draw-y: 300; --blueprint-draw-at: .9">
              <span class="blueprint-draw__num" aria-hidden="true">2</span>
              <span><strong>PEX supply lines</strong><small>Hot and cold home runs</small></span>
            </li>
            <li class="blueprint-draw__note" style="--blueprint-draw-x: 640; --blueprint-draw-y: 430; --blueprint-draw-at: .93">
              <span class="blueprint-draw__num" aria-hidden="true">3</span>
              <span><strong>200A panel</strong><small>40 spaces, whole-home surge</small></span>
            </li>
            <li class="blueprint-draw__note" style="--blueprint-draw-x: 640; --blueprint-draw-y: 575; --blueprint-draw-at: .96">
              <span class="blueprint-draw__num" aria-hidden="true">4</span>
              <span><strong>Sump pump</strong><small>1/3 hp with battery backup</small></span>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </section>

  <div class="blueprint-draw-demo__outro">
    <p class="blueprint-draw-demo__kicker">Plan approved</p>
    <p class="blueprint-draw-demo__line">Next up: the build.</p>
  </div>
</div>
```

## CSS

```css
@property --blueprint-draw-p { syntax: "<number>"; inherits: true; initial-value: 1; }

/* Paper: blueprint blue mixed from the brand; ink is --text-inverse at alpha; markups in amber */
.blueprint-draw {
  --blueprint-draw-paper: color-mix(in srgb, var(--primary) 50%, var(--surface-deep));
  --blueprint-draw-glow: color-mix(in srgb, var(--primary) 64%, var(--surface-deep));
  --blueprint-draw-glow-at: 50% 64%;
  --blueprint-draw-ink: color-mix(in srgb, var(--text-inverse) 92%, transparent);
  --blueprint-draw-ink-2: color-mix(in srgb, var(--text-inverse) 72%, transparent);
  --blueprint-draw-ink-3: color-mix(in srgb, var(--text-inverse) 50%, transparent);
  --blueprint-draw-copy: color-mix(in srgb, var(--text-inverse) 78%, var(--blueprint-draw-paper));
  --blueprint-draw-grid: color-mix(in srgb, var(--text-inverse) 5%, transparent);
  --blueprint-draw-grid-major: color-mix(in srgb, var(--text-inverse) 12%, transparent);
  --blueprint-draw-poche: color-mix(in srgb, var(--text-inverse) 16%, transparent);
  --blueprint-draw-markup: var(--accent);
  position: relative; height: 300vh;
  background: var(--blueprint-draw-paper); color: var(--text-inverse); font-family: var(--font-sans);
}

/* Pinned stage on grid paper: fine and major lines, a light-table glow and a soft vignette */
.blueprint-draw__stage {
  position: sticky; top: 0; height: 100vh; height: 100svh; overflow: hidden;
  background:
    radial-gradient(ellipse 85% 80% at 50% 50%, transparent 55%, color-mix(in srgb, var(--surface-deep) 40%, transparent)),
    linear-gradient(var(--blueprint-draw-grid-major) 1px, transparent 1px) 0 0 / 100px 100px,
    linear-gradient(90deg, var(--blueprint-draw-grid-major) 1px, transparent 1px) 0 0 / 100px 100px,
    linear-gradient(var(--blueprint-draw-grid) 1px, transparent 1px) 0 0 / 20px 20px,
    linear-gradient(90deg, var(--blueprint-draw-grid) 1px, transparent 1px) 0 0 / 20px 20px,
    radial-gradient(ellipse 60% 55% at var(--blueprint-draw-glow-at), var(--blueprint-draw-glow), transparent 72%),
    var(--blueprint-draw-paper);
}
.blueprint-draw__inner {
  box-sizing: border-box; display: flex; flex-direction: column; gap: 1rem; height: 100%;
  max-width: var(--container-max); margin-inline: auto; padding: clamp(1rem, 4vh, 2.5rem) var(--gutter);
}

/* Copy */
.blueprint-draw__copy { flex: none; }
.blueprint-draw__eyebrow {
  display: flex; align-items: center; gap: 0.5rem; margin: 0;
  color: var(--blueprint-draw-copy); font: 500 0.6875rem/1.2 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.blueprint-draw__eyebrow svg { flex: none; fill: none; stroke: var(--blueprint-draw-markup); stroke-width: 1.75; stroke-linecap: round; stroke-linejoin: round; }
.blueprint-draw__title {
  margin: 0.625rem 0 0; font: 600 clamp(1.75rem, 1.2rem + 2.4vw, 3.25rem)/1.02 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.blueprint-draw__body { margin-top: 0.75rem; }
.blueprint-draw__lead { max-width: 32rem; margin: 0; color: var(--blueprint-draw-copy); font-size: clamp(0.9375rem, 0.9rem + 0.25vw, 1.0625rem); line-height: 1.55; }
.blueprint-draw__checks { display: none; margin: 1.5rem 0 0; padding: 0; list-style: none; }
.blueprint-draw__checks li {
  display: flex; align-items: center; gap: 0.75rem; padding: 0.5625rem 0;
  border-top: 1px solid var(--blueprint-draw-grid-major); font: 500 0.8125rem/1.3 var(--font-mono);
}
.blueprint-draw__checks li:last-child { border-bottom: 1px solid var(--blueprint-draw-grid-major); }
.blueprint-draw__checks li::before { content: ""; flex: none; width: 0.4375rem; height: 0.4375rem; border: 1.5px solid var(--blueprint-draw-markup); rotate: 45deg; }
.blueprint-draw__actions { display: flex; margin-top: 1rem; }
.blueprint-draw__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1.25rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem var(--font-sans); text-decoration: none;
  box-shadow: var(--highlight), 0 14px 32px -14px color-mix(in srgb, var(--surface-deep) 85%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.blueprint-draw__btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.blueprint-draw__btn:hover { transform: translateY(-2px); box-shadow: var(--highlight), 0 20px 40px -14px color-mix(in srgb, var(--surface-deep) 90%, transparent); }
.blueprint-draw__btn:hover svg { translate: 3px 0; }
.blueprint-draw__btn:active { transform: scale(0.97); }
.blueprint-draw :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }
.blueprint-draw__meter {
  display: none; align-items: center; gap: 0.75rem; margin-top: 2rem;
  color: var(--blueprint-draw-copy); font: 500 0.6875rem/1 var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase;
}
.blueprint-draw__track { position: relative; flex: 1; height: 1px; background: var(--blueprint-draw-grid-major); }
.blueprint-draw__track::after {
  content: ""; position: absolute; inset: -0.5px 0; background: var(--blueprint-draw-markup);
  transform: scaleX(var(--blueprint-draw-p, 1)); transform-origin: left;
}

/* Figure: the sheet keeps the 3:2 viewBox ratio and shrinks to the space left in the stage */
.blueprint-draw__figure { display: flex; flex-direction: column; gap: 0.875rem; flex: 1 1 auto; min-height: 0; }
.blueprint-draw__plate { display: grid; place-items: center; flex: 1 1 auto; min-height: 9rem; container-type: size; }
.blueprint-draw__sheet { position: relative; width: 100%; width: min(100cqw, 150cqh); aspect-ratio: 3 / 2; }
.blueprint-draw__svg { display: block; width: 100%; height: 100%; overflow: visible; }

/* The draw: each path maps the shared progress onto its own from/to range */
.blueprint-draw__art { fill: none; stroke: var(--blueprint-draw-ink); stroke-linejoin: round; }
.blueprint-draw__art :is(path, text) {
  --blueprint-draw-t: clamp(0, (var(--blueprint-draw-p, 1) - var(--blueprint-draw-from, 0)) / max(0.001, var(--blueprint-draw-to, 1) - var(--blueprint-draw-from, 0)), 1);
}
.blueprint-draw__art [pathLength] { stroke-dasharray: 1; stroke-dashoffset: calc(1 - var(--blueprint-draw-t)); }
.blueprint-draw__l1 { stroke: var(--blueprint-draw-ink); stroke-width: 3.4; }
.blueprint-draw__l2 { stroke: var(--blueprint-draw-ink-2); stroke-width: 2.4; }
.blueprint-draw__l3 { stroke: var(--blueprint-draw-ink-3); stroke-width: 1.7; }
.blueprint-draw__cut { fill: var(--blueprint-draw-poche); fill-opacity: clamp(0, var(--blueprint-draw-t) * 2 - 1, 1); }
.blueprint-draw__solid { fill: var(--blueprint-draw-ink-2); fill-opacity: clamp(0, var(--blueprint-draw-t) * 2 - 1, 1); }
.blueprint-draw__earth { fill: url(#blueprint-draw-hatch); stroke: none; opacity: var(--blueprint-draw-t); }
.blueprint-draw__hatch { stroke: var(--blueprint-draw-ink-3); stroke-width: 1.2; }
.blueprint-draw__art text {
  display: none; fill: var(--blueprint-draw-ink-2); stroke: none;
  font: 500 9px var(--font-mono); letter-spacing: 0.14em; opacity: min(1, var(--blueprint-draw-t) * 4);
}
.blueprint-draw__art .blueprint-draw__fig { display: inline; fill: var(--blueprint-draw-ink); font-size: 19px; letter-spacing: 0; font-variant-numeric: tabular-nums; }
.blueprint-draw__art .blueprint-draw__strong { fill: var(--blueprint-draw-ink); font-size: 12px; font-weight: 600; }
.blueprint-draw__art .blueprint-draw__tiny { font-size: 7px; letter-spacing: 0.06em; }

/* Markups: a switch flips to 1 at each note's threshold; transitions turn the flip into a pop */
.blueprint-draw__leaders { display: none; }
.blueprint-draw__leaders path, .blueprint-draw__pin, .blueprint-draw__note {
  --blueprint-draw-on: clamp(0, (var(--blueprint-draw-p, 1) - var(--blueprint-draw-at, 0)) * 1000, 1);
}
.blueprint-draw__leaders path {
  fill: none; stroke: var(--blueprint-draw-markup); stroke-width: 1.4;
  stroke-dasharray: 1; stroke-dashoffset: calc(1 - var(--blueprint-draw-on));
  transition: stroke-dashoffset var(--dur-4) var(--ease-out);
}
.blueprint-draw__pin {
  position: absolute; left: calc(var(--blueprint-draw-x) / 960 * 100%); top: calc(var(--blueprint-draw-y) / 640 * 100%);
  display: grid; place-items: center; width: 1.375rem; height: 1.375rem; border-radius: 50%; pointer-events: none;
  background: var(--blueprint-draw-markup); color: var(--text-main); font: 700 0.6875rem/1 var(--font-mono);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--blueprint-draw-markup) 26%, transparent), 0 8px 18px -6px color-mix(in srgb, var(--surface-deep) 80%, transparent);
  translate: -50% -50%; opacity: var(--blueprint-draw-on); scale: calc(0.3 + 0.7 * var(--blueprint-draw-on));
  transition: opacity var(--dur-2) var(--ease-out), scale var(--dur-4) var(--ease-spring);
}

/* Notes: a legend under the sheet on small screens */
.blueprint-draw__notes { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0.5rem 1rem; flex: none; margin: 0; padding: 0; list-style: none; }
.blueprint-draw__note {
  display: flex; align-items: center; gap: 0.5rem; min-width: 0; font: 500 0.75rem/1.25 var(--font-mono);
  opacity: var(--blueprint-draw-on); translate: 0 calc((1 - var(--blueprint-draw-on)) * 0.5rem);
  transition: opacity var(--dur-3) var(--ease-out), translate var(--dur-4) var(--ease-spring);
}
.blueprint-draw__note strong { display: block; font-weight: 500; }
.blueprint-draw__note small { display: none; color: var(--blueprint-draw-copy); font-size: 0.6875rem; }
.blueprint-draw__num {
  flex: none; display: grid; place-items: center; width: 1.375rem; height: 1.375rem; border-radius: 50%;
  background: var(--blueprint-draw-markup); color: var(--text-main); font-size: 0.6875rem; font-weight: 700;
}

@media (min-width: 768px) {
  .blueprint-draw__copy { display: grid; grid-template-columns: 1fr 1fr; column-gap: 2.5rem; align-items: end; }
  .blueprint-draw__eyebrow, .blueprint-draw__title { grid-column: 1; }
  .blueprint-draw__body { grid-column: 2; grid-row: 1 / span 2; margin-top: 0; }
  .blueprint-draw__notes { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .blueprint-draw__l1 { stroke-width: 2.6; }
  .blueprint-draw__l2 { stroke-width: 1.7; }
  .blueprint-draw__l3 { stroke-width: 1.2; }
  .blueprint-draw__art text { display: inline; }
  .blueprint-draw__art .blueprint-draw__fig { font-size: 14px; }
}

/* Desktop: copy beside the sheet; notes sit on the drawing as markups with leader lines */
@media (min-width: 1024px) {
  .blueprint-draw { --blueprint-draw-glow-at: 66% 50%; height: 340vh; }
  .blueprint-draw__inner { display: grid; grid-template-columns: minmax(16rem, 22rem) minmax(0, 1fr); align-items: center; gap: clamp(2rem, 4vw, 4.5rem); }
  .blueprint-draw__copy { display: block; }
  .blueprint-draw__body { margin-top: 1.25rem; }
  .blueprint-draw__checks { display: grid; }
  .blueprint-draw__meter { display: flex; }
  .blueprint-draw__figure {
    position: relative; display: block; justify-self: center;
    width: min(100%, calc((100vh - 5rem) * 1.5)); width: min(100%, calc((100svh - 5rem) * 1.5));
  }
  .blueprint-draw__plate { display: block; container-type: normal; }
  .blueprint-draw__sheet { width: 100%; }
  .blueprint-draw__l1 { stroke-width: 2.2; }
  .blueprint-draw__l2 { stroke-width: 1.4; }
  .blueprint-draw__l3 { stroke-width: 1; }
  .blueprint-draw__art .blueprint-draw__fig { font-size: 12px; }
  .blueprint-draw__leaders { display: inline; }
  .blueprint-draw__pin { width: 0.625rem; height: 0.625rem; font-size: 0; }
  .blueprint-draw__notes { position: absolute; inset: 0; display: block; pointer-events: none; }
  .blueprint-draw__note {
    position: absolute; left: calc(var(--blueprint-draw-x) / 960 * 100%); top: calc(var(--blueprint-draw-y) / 640 * 100%);
    padding: 0.4375rem 0.875rem 0.4375rem 0.4375rem; border-radius: var(--radius-lg); white-space: nowrap;
    background: color-mix(in srgb, var(--blueprint-draw-paper) 82%, var(--surface-deep));
    box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--blueprint-draw-markup) 55%, transparent), var(--highlight-inverse),
      0 16px 32px -16px color-mix(in srgb, var(--surface-deep) 90%, transparent);
    translate: 0.375rem -50%; scale: calc(0.86 + 0.14 * var(--blueprint-draw-on)); transform-origin: 0 50%;
    transition: opacity var(--dur-3) var(--ease-out) var(--dur-3), scale var(--dur-4) var(--ease-spring) var(--dur-3);
  }
  .blueprint-draw__note small { display: block; }
}

/* With scripting on, start undrawn (no flash); if the script never takes over, draw anyway */
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .blueprint-draw:not(.is-live) { animation: blueprint-draw-failsafe 1.6s var(--ease-in-out) 2.5s both; }
}
@keyframes blueprint-draw-failsafe { from { --blueprint-draw-p: 0; } to { --blueprint-draw-p: 1; } }

/* Demo scroll room */
.blueprint-draw-demo__intro, .blueprint-draw-demo__outro {
  display: grid; place-content: center; justify-items: center; gap: 0.75rem; min-height: 70vh; padding: 3rem var(--gutter);
  background: var(--surface-deep); color: var(--text-inverse); font-family: var(--font-sans); text-align: center;
}
.blueprint-draw-demo__kicker { margin: 0; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.blueprint-draw-demo__line { max-width: 22ch; margin: 0; font: 600 clamp(1.5rem, 1.1rem + 2vw, 2.5rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.blueprint-draw-demo__hint { display: inline-flex; align-items: center; gap: 0.375rem; margin-top: 1rem; color: var(--text-inverse-muted); font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; }
.blueprint-draw-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: blueprint-draw-nudge 1.6s var(--ease-in-out) 3; }
@keyframes blueprint-draw-nudge { 50% { translate: 0 4px; } }

@media (prefers-reduced-motion: reduce) {
  .blueprint-draw-demo *, .blueprint-draw-demo *::before, .blueprint-draw-demo *::after { animation: none !important; }
}
```

## JS

```js
const clamp01 = (n) => Math.min(1, Math.max(0, n));
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? clamp01(-r.top / range) : 0; };
const feet = (inches) => `${Math.floor(inches / 12)}'-${inches % 12}"`;
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-blueprint-draw]').forEach((root) => {
  // Dimension figures count over the same from/to range their lines draw in (read from the CSS custom properties)
  const figures = [...root.querySelectorAll('[data-blueprint-draw-count]')].map((el) => {
    const css = getComputedStyle(el);
    const from = parseFloat(css.getPropertyValue('--blueprint-draw-from')) || 0;
    const to = parseFloat(css.getPropertyValue('--blueprint-draw-to')) || 1;
    return { el, from, span: Math.max(0.001, to - from), total: Number(el.dataset.blueprintDrawCount), shown: -1 };
  });
  let near = false;
  let frame = 0;

  // One write per frame: the progress variable drives every stroke, fill and markup in CSS
  const render = () => {
    frame = 0;
    const p = reduce.matches ? 1 : progress(root);
    if (reduce.matches) root.style.removeProperty('--blueprint-draw-p');
    else root.style.setProperty('--blueprint-draw-p', p.toFixed(4));
    figures.forEach((f) => {
      const t = clamp01((p - f.from) / f.span);
      const value = Math.round(f.total * (1 - (1 - t) ** 3));
      if (value !== f.shown) { f.shown = value; f.el.textContent = feet(value); }
    });
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(render); };

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; queue(); }, { rootMargin: '25% 0px' }).observe(root);
  addEventListener('scroll', queue, { passive: true });
  addEventListener('resize', queue, { passive: true });
  reduce.addEventListener('change', render);
  render();
  root.classList.add('is-live'); // hands control from the CSS failsafe to the script
});
```

## Notes

- The drawing is one `role="img"` SVG with a text alternative; the four callouts are a real ordered list that stays in the accessibility tree the whole time (the scroll pop-in is visual only). From 1024px they sit on the sheet as amber markups with leader lines; below that they become numbered pins with a legend under the sheet.
- `--blueprint-draw-p` is a registered `<number>` with an initial value of 1, so without JS, and under reduced motion, the sheet renders fully drawn with every callout and the final dimensions. With scripting on, a CSS failsafe holds it undrawn (no flash) and draws it after 2.5s if the script never adds `.is-live`.
- Authoring: give any stroke `pathLength="1"` and a `--blueprint-draw-from`/`--blueprint-draw-to` range (0–1 of the pinned scroll) on it or its `<g>`. Keep each drawable path to a single subpath, since dash patterns restart per subpath. `data-blueprint-draw-count` (in inches) makes a `<text>` count up over its group's range; callout thresholds are `--blueprint-draw-at`, and positions use viewBox units (`--blueprint-draw-x/y`).
- Contrast: the paper is `--primary` and `--surface-deep` mixed 50/50 (about #16377f). `--text-inverse` is 10.6:1, body copy (78% mix) is 7.1:1 and stays at 5.9:1 on the brightest glow. Amber badges carry `--text-main` at 6.8:1.
- Needs `@property`, `color-mix()`, container query units and `@media (scripting)`. Older engines fall back to the fully drawn sheet. The hatch and mask ids are prefixed; give them unique suffixes if a page shows two sheets.
