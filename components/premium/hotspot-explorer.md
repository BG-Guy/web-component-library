# Home Anatomy Hotspots

A cutaway illustration of a whole house (roof, gutters, attic, bedroom, bathroom, living room, kitchen and a basement with the furnace, water heater and electrical panel) with numbered markers that pulse three times when the house first comes into view. Opening a marker springs a card out of it with the warning signs to watch for, a lifespan meter showing where this home's system sits, and a booking link. A side list mirrors the markers and lights up each spot on hover. On phones the card becomes a bottom sheet and the list stacks under the drawing. Depends on `tokens/variables.css`.

**Motion:** three finite marker pulses on entering view (1.4s × 3, staggered) · popover spring from its marker (`--dur-4`, `--ease-spring`; slide-up sheet on phones) · lifespan bar fill (`--dur-5`, `--ease-out`) · marker and list hover lift (`--dur-3`, `--ease-spring`).

## HTML

```html
<section class="hotspots" aria-labelledby="hotspots-title" data-hotspots>
  <div class="hotspots__inner">
    <header class="hotspots__head">
      <p class="hotspots__eyebrow">Home anatomy</p>
      <h2 id="hotspots-title" class="hotspots__title">Know your home, system by system.</h2>
      <p class="hotspots__lead">Tap a marker to see what wears out, the warning signs to look for and how long each system usually lasts, with this home's age marked on every one.</p>
    </header>

    <div class="hotspots__layout">
      <div class="hotspots__figure">
        <svg class="hotspots__art" viewBox="0 0 800 560" width="800" height="560" role="img" aria-labelledby="hotspots-art-title" focusable="false">
          <title id="hotspots-art-title">Cutaway of a two-storey house: roof and gutters, an insulated attic, a bedroom and bathroom upstairs, a living room and kitchen downstairs, and a basement with the furnace, water heater, washer and electrical panel.</title>
          <defs>
            <pattern id="hotspots-soil-grain" width="26" height="20" patternUnits="userSpaceOnUse">
              <circle class="hotspots__pebble" cx="6" cy="6" r="1.8" /><circle class="hotspots__pebble" cx="19" cy="15" r="1.3" />
            </pattern>
            <clipPath id="hotspots-attic-clip"><path d="M150 184V179L400 54 650 179V184z" /></clipPath>
          </defs>

          <!-- Sky and garden -->
          <path class="hotspots__cloud" d="M38 92a15 15 0 0 1 10-27 22 22 0 0 1 41-6 16 16 0 0 1 20 33z" />
          <path class="hotspots__cloud" d="M652 66a12 12 0 0 1 9-21 18 18 0 0 1 33-5 13 13 0 0 1 16 26z" />
          <rect class="hotspots__trunk" x="58" y="330" width="9" height="88" rx="3" />
          <circle class="hotspots__tree" cx="62" cy="310" r="34" />
          <circle class="hotspots__tree hotspots__tree--deep" cx="82" cy="330" r="22" />
          <circle class="hotspots__tree" cx="40" cy="334" r="20" />
          <path class="hotspots__tree hotspots__tree--deep" d="M712 418a20 20 0 0 1 34-15 15 15 0 0 1 28 15z" />
          <rect class="hotspots__soil" x="0" y="418" width="800" height="142" />
          <rect fill="url(#hotspots-soil-grain)" x="0" y="424" width="800" height="136" />
          <rect class="hotspots__grass" x="0" y="414" width="800" height="7" rx="3" />

          <!-- Rooms -->
          <path class="hotspots__room--attic" d="M150 184V179L400 54 650 179V184z" />
          <rect class="hotspots__room--bed" x="150" y="192" width="270" height="100" />
          <rect class="hotspots__room--bath" x="426" y="192" width="224" height="100" />
          <rect class="hotspots__room--living" x="150" y="300" width="250" height="110" />
          <rect class="hotspots__room--kitchen" x="400" y="300" width="250" height="110" />
          <rect class="hotspots__room--base" x="150" y="420" width="500" height="120" />

          <!-- Attic: insulation, stored boxes, king post and struts -->
          <path class="hotspots__insul" clip-path="url(#hotspots-attic-clip)" d="M150 184v-11q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0q12.5-9 25 0V184z" />
          <rect class="hotspots__obj hotspots__wood" x="282" y="148" width="44" height="28" rx="2" />
          <rect class="hotspots__obj hotspots__wood" x="292" y="132" width="26" height="16" rx="2" />
          <path class="hotspots__line" d="M282 158h44M304 148v10" />
          <path class="hotspots__timber" d="M400 60v120M398 178 304 110M402 178 496 110" />
          <path class="hotspots__brick" d="M530 74h32v54L530 112z" />
          <path class="hotspots__hair" d="M530 90h32M530 106h32M546 74v16M538 90v16M554 90v16" />
          <rect class="hotspots__cut" x="526" y="68" width="40" height="8" rx="1.5" />

          <!-- Bedroom -->
          <rect class="hotspots__obj hotspots__glass" x="186" y="212" width="62" height="48" rx="3" />
          <path class="hotspots__line" d="M217 212v48M186 236h62" />
          <rect class="hotspots__obj hotspots__white" x="334" y="210" width="44" height="30" rx="2" />
          <path class="hotspots__hair" d="m340 234 10-12 8 8 6-6 8 10" />
          <rect class="hotspots__obj hotspots__wood" x="262" y="266" width="22" height="26" rx="2" />
          <path class="hotspots__obj hotspots__glow" d="M265 246h16l4 13h-24z" />
          <path class="hotspots__line" d="M273 259v7M300 284v8M410 284v8" />
          <rect class="hotspots__obj hotspots__wood" x="296" y="238" width="8" height="54" rx="3" />
          <rect class="hotspots__obj hotspots__white" x="302" y="262" width="108" height="15" rx="5" />
          <rect class="hotspots__obj hotspots__white" x="307" y="253" width="28" height="11" rx="5" />
          <path class="hotspots__obj hotspots__fabric--alt" d="M340 258h66a4 4 0 0 1 4 4v15h-70z" />
          <rect class="hotspots__obj hotspots__wood" x="296" y="277" width="118" height="7" rx="2" />

          <!-- Bathroom -->
          <path class="hotspots__tile" d="M510 222h126M510 238h126M510 254h126M526 206v56M542 206v56M558 206v56M574 206v56M590 206v56M606 206v56M622 206v56" />
          <rect class="hotspots__obj hotspots__glass" x="452" y="212" width="30" height="38" rx="15" />
          <rect class="hotspots__obj hotspots__white" x="444" y="258" width="46" height="6" rx="3" />
          <rect class="hotspots__obj hotspots__wood" x="448" y="264" width="38" height="28" rx="2" />
          <path class="hotspots__line" d="M467 258v-6h6M467 264v28M649 212h-20v8M623 222h12M524 286v6M618 286v6" />
          <rect class="hotspots__obj hotspots__white" x="512" y="262" width="118" height="24" rx="11" />

          <!-- Living room -->
          <rect class="hotspots__obj hotspots__glass" x="198" y="316" width="104" height="34" rx="3" />
          <path class="hotspots__line" d="M233 316v34M267 316v34" />
          <ellipse class="hotspots__rug" cx="254" cy="408" rx="86" ry="3" />
          <rect class="hotspots__obj hotspots__fabric" x="192" y="352" width="122" height="26" rx="9" />
          <rect class="hotspots__obj hotspots__fabric--deep" x="186" y="372" width="134" height="24" rx="7" />
          <rect class="hotspots__obj hotspots__fabric" x="178" y="364" width="18" height="36" rx="7" />
          <rect class="hotspots__obj hotspots__fabric" x="310" y="364" width="18" height="36" rx="7" />
          <path class="hotspots__line" d="M253 356v14M192 400v8M314 400v8M354 408v-72" />
          <path class="hotspots__obj hotspots__glow" d="M343 322h22l-5 15h-12z" />
          <path class="hotspots__obj hotspots__wood" d="M368 392h20l-3 16h-14z" />
          <path class="hotspots__plant" d="M378 392c-11-6-15-19-9-28 5 9 9 16 9 28zm0 0c8-9 11-21 5-30-7 9-7 19-5 30z" />

          <!-- Kitchen -->
          <rect class="hotspots__obj hotspots__white" x="414" y="328" width="42" height="82" rx="4" />
          <rect class="hotspots__obj hotspots__wood" x="470" y="312" width="76" height="30" rx="2" />
          <rect class="hotspots__obj hotspots__glass" x="560" y="314" width="58" height="40" rx="3" />
          <rect class="hotspots__obj hotspots__wood" x="472" y="374" width="164" height="36" rx="2" />
          <rect class="hotspots__counter" x="466" y="367" width="176" height="7" rx="2" />
          <path class="hotspots__line" d="M414 354h42M449 334v12M449 360v18M508 312v30M589 314v40M526 374v36M582 374v36M520 388v8M532 388v8M576 388v8M588 388v8M598 367v-13h10v5" />

          <!-- Basement: furnace and ducts, water heater, washer, electrical panel -->
          <rect class="hotspots__obj hotspots__metal" x="164" y="424" width="66" height="12" rx="2" />
          <rect class="hotspots__obj hotspots__metal" x="228" y="430" width="48" height="16" rx="2" />
          <rect class="hotspots__obj hotspots__white" x="222" y="446" width="60" height="94" rx="4" />
          <rect class="hotspots__obj hotspots__glow" x="242" y="490" width="20" height="10" rx="2" />
          <rect class="hotspots__obj hotspots__metal" x="408" y="430" width="10" height="22" />
          <rect class="hotspots__obj hotspots__white" x="388" y="452" width="50" height="88" rx="12" />
          <rect class="hotspots__obj hotspots__glow" x="401" y="478" width="24" height="16" rx="2" />
          <rect class="hotspots__obj hotspots__white" x="474" y="486" width="46" height="54" rx="5" />
          <circle class="hotspots__obj hotspots__glass" cx="497" cy="517" r="14" />
          <rect class="hotspots__breaker-box" x="584" y="446" width="38" height="52" rx="3" />
          <path class="hotspots__breakers" d="M592 456h8M606 456h8M592 465h8M606 465h8M592 474h8M606 474h8M592 483h8M606 483h8" />
          <path class="hotspots__line" d="M232 460h40M232 467h40M232 474h40M222 520h60M482 495h18M603 446v-26" />

          <!-- Section cut: walls and slabs, with glazing in the cut walls -->
          <path class="hotspots__cut" d="M140 176h10v374h-10zM650 176h10v374h-10zM140 184h520v8H140zM140 292h520v8H140zM140 410h520v10H140zM140 540h520v10H140zM420 192h6v100h-6zM400 300h6v24h-6z" />
          <path class="hotspots__glass" d="M141 214h8v46h-8zM141 322h8v52h-8zM651 214h8v40h-8zM651 322h8v52h-8z" />
          <path class="hotspots__hair" d="M145 214v46M145 322v52M655 214v40M655 322v52" />

          <!-- Services through the slab: supply riser, hot and cold lines -->
          <rect class="hotspots__obj hotspots__metal" x="160" y="400" width="12" height="28" rx="1" />
          <path class="hotspots__line" d="M156 402h20" />
          <path class="hotspots__pipe hotspots__pipe--cold" d="M398 452v-24h158v-24" />
          <path class="hotspots__pipe hotspots__pipe--hot" d="M428 452v-18h138v-30" />

          <!-- Roof, gutters and downspout -->
          <path class="hotspots__roof" d="M88 196 400 40 712 196v14L400 54 88 210z" />
          <path class="hotspots__shingles" d="M92 199 400 45 708 199M92 203 400 49 708 203" />
          <path class="hotspots__obj hotspots__metal" d="M76 200h16v9a6 6 0 0 1-6 6h-4a6 6 0 0 1-6-6z" />
          <path class="hotspots__spout" d="M716 214v8l-46 26v158q0 10 10 10h22" />
          <path class="hotspots__obj hotspots__metal" d="M708 200h16v9a6 6 0 0 1-6 6h-4a6 6 0 0 1-6-6z" />
        </svg>

        <div class="hotspots__spots" role="toolbar" aria-label="Home systems">
          <button class="hotspots__spot" type="button" popovertarget="hotspots-pop-roof" aria-haspopup="dialog" data-hotspots-key="roof" style="--hotspots-x: 31.25%; --hotspots-y: 21.79%; --hotspots-i: 0; anchor-name: --hotspots-roof">
            <span class="hotspots__pin">1</span><span class="hotspots__sr"> Roof</span>
          </button>
          <button class="hotspots__spot" type="button" popovertarget="hotspots-pop-gutters" aria-haspopup="dialog" data-hotspots-key="gutters" style="--hotspots-x: 89.5%; --hotspots-y: 36.96%; --hotspots-i: 1; anchor-name: --hotspots-gutters">
            <span class="hotspots__pin">2</span><span class="hotspots__sr"> Gutters and downspouts</span>
          </button>
          <button class="hotspots__spot" type="button" popovertarget="hotspots-pop-attic" aria-haspopup="dialog" data-hotspots-key="attic" style="--hotspots-x: 58.75%; --hotspots-y: 25%; --hotspots-i: 2; anchor-name: --hotspots-attic">
            <span class="hotspots__pin">3</span><span class="hotspots__sr"> Attic and insulation</span>
          </button>
          <button class="hotspots__spot" type="button" popovertarget="hotspots-pop-hvac" aria-haspopup="dialog" data-hotspots-key="hvac" style="--hotspots-x: 31.5%; --hotspots-y: 83.93%; --hotspots-i: 3; anchor-name: --hotspots-hvac">
            <span class="hotspots__pin">4</span><span class="hotspots__sr"> HVAC unit</span>
          </button>
          <button class="hotspots__spot" type="button" popovertarget="hotspots-pop-heater" aria-haspopup="dialog" data-hotspots-key="heater" style="--hotspots-x: 51.63%; --hotspots-y: 87.14%; --hotspots-i: 4; anchor-name: --hotspots-heater">
            <span class="hotspots__pin">5</span><span class="hotspots__sr"> Water heater</span>
          </button>
          <button class="hotspots__spot" type="button" popovertarget="hotspots-pop-panel" aria-haspopup="dialog" data-hotspots-key="panel" style="--hotspots-x: 75.38%; --hotspots-y: 84.29%; --hotspots-i: 5; anchor-name: --hotspots-panel">
            <span class="hotspots__pin">6</span><span class="hotspots__sr"> Electrical panel</span>
          </button>
        </div>
      </div>

      <div class="hotspots__panel">
        <div class="hotspots__panel-head">
          <h3 id="hotspots-list-title" class="hotspots__panel-title">Systems to watch</h3>
          <span class="hotspots__panel-meta" aria-hidden="true">Avg. lifespan</span>
        </div>
        <ol class="hotspots__list" role="list" aria-labelledby="hotspots-list-title">
          <li><button class="hotspots__entry" type="button" popovertarget="hotspots-pop-roof" aria-haspopup="dialog" data-hotspots-key="roof"><span class="hotspots__num" aria-hidden="true">1</span><span class="hotspots__entry-text"><strong>Roof</strong><small>Inspect every spring</small></span><span class="hotspots__entry-life">20–25 yrs</span></button></li>
          <li><button class="hotspots__entry" type="button" popovertarget="hotspots-pop-gutters" aria-haspopup="dialog" data-hotspots-key="gutters"><span class="hotspots__num" aria-hidden="true">2</span><span class="hotspots__entry-text"><strong>Gutters</strong><small>Clear spring and autumn</small></span><span class="hotspots__entry-life">15–20 yrs</span></button></li>
          <li><button class="hotspots__entry" type="button" popovertarget="hotspots-pop-attic" aria-haspopup="dialog" data-hotspots-key="attic"><span class="hotspots__num" aria-hidden="true">3</span><span class="hotspots__entry-text"><strong>Attic &amp; insulation</strong><small>Check before winter</small></span><span class="hotspots__entry-life">20–30 yrs</span></button></li>
          <li><button class="hotspots__entry" type="button" popovertarget="hotspots-pop-hvac" aria-haspopup="dialog" data-hotspots-key="hvac"><span class="hotspots__num" aria-hidden="true">4</span><span class="hotspots__entry-text"><strong>HVAC unit</strong><small>Service every autumn</small></span><span class="hotspots__entry-life">12–15 yrs</span></button></li>
          <li><button class="hotspots__entry" type="button" popovertarget="hotspots-pop-heater" aria-haspopup="dialog" data-hotspots-key="heater"><span class="hotspots__num" aria-hidden="true">5</span><span class="hotspots__entry-text"><strong>Water heater</strong><small>Flush once a year</small></span><span class="hotspots__entry-life">8–12 yrs</span></button></li>
          <li><button class="hotspots__entry" type="button" popovertarget="hotspots-pop-panel" aria-haspopup="dialog" data-hotspots-key="panel"><span class="hotspots__num" aria-hidden="true">6</span><span class="hotspots__entry-text"><strong>Electrical panel</strong><small>Test once a year</small></span><span class="hotspots__entry-life">25–40 yrs</span></button></li>
        </ol>
        <a class="hotspots__panel-cta" href="#book">
          Book a whole-home inspection
          <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
        </a>
      </div>
    </div>

    <!-- Popover cards: lifespan bars use a 0–40 year scale (--hotspots-lo / -hi / -age as % of 40) -->
    <div class="hotspots__pops">
      <div class="hotspots__pop" id="hotspots-pop-roof" popover role="dialog" aria-labelledby="hotspots-pop-roof-title" style="position-anchor: --hotspots-roof; --hotspots-lo: 50%; --hotspots-hi: 62.5%; --hotspots-age: 42.5%">
        <div class="hotspots__pop-head">
          <span class="hotspots__pop-num" aria-hidden="true">1</span>
          <div><p class="hotspots__pop-eyebrow">Exterior</p><h3 id="hotspots-pop-roof-title" class="hotspots__pop-title">Roof</h3></div>
          <button class="hotspots__close" type="button" popovertarget="hotspots-pop-roof" popovertargetaction="hide" aria-label="Close"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
        </div>
        <p class="hotspots__label">Warning signs</p>
        <ul class="hotspots__signs" role="list"><li>Curling, cracked or missing shingles</li><li>Granules collecting in the gutters</li><li>Daylight or damp patches in the attic</li></ul>
        <div class="hotspots__life">
          <p class="hotspots__life-row"><span>Avg. lifespan</span><strong>20–25 yrs</strong></p>
          <div class="hotspots__meter" aria-hidden="true"></div>
          <p class="hotspots__scale" aria-hidden="true"><span>0</span><span>20</span><span>40 yrs</span></p>
          <p class="hotspots__yours">Yours: re-roofed in 2009 (17 yrs)</p>
        </div>
        <a class="hotspots__cta" href="#book">Book an inspection <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </div>

      <div class="hotspots__pop" id="hotspots-pop-gutters" popover role="dialog" aria-labelledby="hotspots-pop-gutters-title" style="position-anchor: --hotspots-gutters; --hotspots-lo: 37.5%; --hotspots-hi: 50%; --hotspots-age: 30%">
        <div class="hotspots__pop-head">
          <span class="hotspots__pop-num" aria-hidden="true">2</span>
          <div><p class="hotspots__pop-eyebrow">Exterior</p><h3 id="hotspots-pop-gutters-title" class="hotspots__pop-title">Gutters &amp; downspouts</h3></div>
          <button class="hotspots__close" type="button" popovertarget="hotspots-pop-gutters" popovertargetaction="hide" aria-label="Close"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
        </div>
        <p class="hotspots__label">Warning signs</p>
        <ul class="hotspots__signs" role="list"><li>Water spilling over the edge in heavy rain</li><li>Sagging runs or gaps at the joints</li><li>Peeling paint or stains below the eaves</li></ul>
        <div class="hotspots__life">
          <p class="hotspots__life-row"><span>Avg. lifespan</span><strong>15–20 yrs</strong></p>
          <div class="hotspots__meter" aria-hidden="true"></div>
          <p class="hotspots__scale" aria-hidden="true"><span>0</span><span>20</span><span>40 yrs</span></p>
          <p class="hotspots__yours">Yours: fitted in 2014 (12 yrs)</p>
        </div>
        <a class="hotspots__cta" href="#book">Book an inspection <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </div>

      <div class="hotspots__pop" id="hotspots-pop-attic" popover role="dialog" aria-labelledby="hotspots-pop-attic-title" style="position-anchor: --hotspots-attic; --hotspots-lo: 50%; --hotspots-hi: 75%; --hotspots-age: 62.5%">
        <div class="hotspots__pop-head">
          <span class="hotspots__pop-num" aria-hidden="true">3</span>
          <div><p class="hotspots__pop-eyebrow">Attic</p><h3 id="hotspots-pop-attic-title" class="hotspots__pop-title">Attic &amp; insulation</h3></div>
          <button class="hotspots__close" type="button" popovertarget="hotspots-pop-attic" popovertargetaction="hide" aria-label="Close"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
        </div>
        <p class="hotspots__label">Warning signs</p>
        <ul class="hotspots__signs" role="list"><li>Ice dams along the eaves in winter</li><li>Upstairs rooms too hot in summer</li><li>Damp, flattened or patchy insulation</li></ul>
        <div class="hotspots__life">
          <p class="hotspots__life-row"><span>Avg. lifespan</span><strong>20–30 yrs</strong></p>
          <div class="hotspots__meter" aria-hidden="true"></div>
          <p class="hotspots__scale" aria-hidden="true"><span>0</span><span>20</span><span>40 yrs</span></p>
          <p class="hotspots__yours">Yours: topped up in 2001 (25 yrs)</p>
        </div>
        <a class="hotspots__cta" href="#book">Book an inspection <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </div>

      <div class="hotspots__pop" id="hotspots-pop-hvac" popover role="dialog" aria-labelledby="hotspots-pop-hvac-title" style="position-anchor: --hotspots-hvac; --hotspots-lo: 30%; --hotspots-hi: 37.5%; --hotspots-age: 32.5%">
        <div class="hotspots__pop-head">
          <span class="hotspots__pop-num" aria-hidden="true">4</span>
          <div><p class="hotspots__pop-eyebrow">Basement</p><h3 id="hotspots-pop-hvac-title" class="hotspots__pop-title">HVAC unit</h3></div>
          <button class="hotspots__close" type="button" popovertarget="hotspots-pop-hvac" popovertargetaction="hide" aria-label="Close"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
        </div>
        <p class="hotspots__label">Warning signs</p>
        <ul class="hotspots__signs" role="list"><li>Rooms heating or cooling unevenly</li><li>Short cycling, rattling or a burning smell</li><li>Energy bills creeping up each year</li></ul>
        <div class="hotspots__life">
          <p class="hotspots__life-row"><span>Avg. lifespan</span><strong>12–15 yrs</strong></p>
          <div class="hotspots__meter" aria-hidden="true"></div>
          <p class="hotspots__scale" aria-hidden="true"><span>0</span><span>20</span><span>40 yrs</span></p>
          <p class="hotspots__yours">Yours: installed in 2013 (13 yrs)</p>
        </div>
        <a class="hotspots__cta" href="#book">Book an inspection <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </div>

      <div class="hotspots__pop" id="hotspots-pop-heater" popover role="dialog" aria-labelledby="hotspots-pop-heater-title" style="position-anchor: --hotspots-heater; --hotspots-lo: 20%; --hotspots-hi: 30%; --hotspots-age: 22.5%">
        <div class="hotspots__pop-head">
          <span class="hotspots__pop-num" aria-hidden="true">5</span>
          <div><p class="hotspots__pop-eyebrow">Basement</p><h3 id="hotspots-pop-heater-title" class="hotspots__pop-title">Water heater</h3></div>
          <button class="hotspots__close" type="button" popovertarget="hotspots-pop-heater" popovertargetaction="hide" aria-label="Close"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
        </div>
        <p class="hotspots__label">Warning signs</p>
        <ul class="hotspots__signs" role="list"><li>Rusty or cloudy hot water</li><li>Rumbling or popping as it heats</li><li>Water pooling around the base</li></ul>
        <div class="hotspots__life">
          <p class="hotspots__life-row"><span>Avg. lifespan</span><strong>8–12 yrs</strong></p>
          <div class="hotspots__meter" aria-hidden="true"></div>
          <p class="hotspots__scale" aria-hidden="true"><span>0</span><span>20</span><span>40 yrs</span></p>
          <p class="hotspots__yours">Yours: installed in 2017 (9 yrs)</p>
        </div>
        <a class="hotspots__cta" href="#book">Book an inspection <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </div>

      <div class="hotspots__pop" id="hotspots-pop-panel" popover role="dialog" aria-labelledby="hotspots-pop-panel-title" style="position-anchor: --hotspots-panel; --hotspots-lo: 62.5%; --hotspots-hi: 100%; --hotspots-age: 70%">
        <div class="hotspots__pop-head">
          <span class="hotspots__pop-num" aria-hidden="true">6</span>
          <div><p class="hotspots__pop-eyebrow">Basement</p><h3 id="hotspots-pop-panel-title" class="hotspots__pop-title">Electrical panel</h3></div>
          <button class="hotspots__close" type="button" popovertarget="hotspots-pop-panel" popovertargetaction="hide" aria-label="Close"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M6 6l12 12M18 6 6 18" /></svg></button>
        </div>
        <p class="hotspots__label">Warning signs</p>
        <ul class="hotspots__signs" role="list"><li>Breakers tripping more than once a month</li><li>A warm panel door or a burning smell</li><li>Lights flickering when appliances start</li></ul>
        <div class="hotspots__life">
          <p class="hotspots__life-row"><span>Avg. lifespan</span><strong>25–40 yrs</strong></p>
          <div class="hotspots__meter" aria-hidden="true"></div>
          <p class="hotspots__scale" aria-hidden="true"><span>0</span><span>20</span><span>40 yrs</span></p>
          <p class="hotspots__yours">Yours: upgraded in 1998 (28 yrs)</p>
        </div>
        <a class="hotspots__cta" href="#book">Book an inspection <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg></a>
      </div>
    </div>
  </div>
</section>
```

## CSS

```css
/* Section */
.hotspots {
  --hotspots-ink: color-mix(in srgb, var(--text-main) 60%, var(--surface-light));   /* outlines in the drawing */
  --hotspots-hair: color-mix(in srgb, var(--text-main) 22%, var(--surface-light));  /* hairlines in the drawing */
  anchor-scope: all; /* keeps anchor names local to each instance */
  background: var(--surface-light); color: var(--text-main); font-family: var(--font-sans);
}
.hotspots__inner { max-width: var(--container-max); margin-inline: auto; padding: clamp(4rem, 9vw, 7rem) var(--gutter); }
.hotspots__head { max-width: 42rem; margin-bottom: 2.5rem; }
.hotspots__eyebrow { margin: 0; color: var(--primary); font-size: 0.8125rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; }
.hotspots__title { margin: 0.75rem 0 0; font: 600 clamp(2rem, 1.2rem + 3vw, 3.25rem)/1.05 var(--font-display); letter-spacing: var(--tracking-display); text-wrap: balance; }
.hotspots__lead { max-width: 36rem; margin: 1rem 0 0; color: var(--text-muted); font-size: 1.0625rem; line-height: 1.6; }
.hotspots__layout { display: grid; gap: 1rem; align-items: start; }
.hotspots :is(.hotspots__close, .hotspots__cta, .hotspots__panel-cta) svg { flex: none; fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; }
.hotspots__sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* Figure: sky gradient behind the drawing, markers layered on top */
.hotspots__figure {
  position: relative; isolation: isolate; overflow: hidden; border-radius: var(--radius-2xl);
  background:
    radial-gradient(60% 50% at 82% 0%, color-mix(in srgb, var(--accent) 12%, transparent), transparent 70%),
    linear-gradient(180deg, color-mix(in srgb, var(--primary) 11%, var(--surface-light)), color-mix(in srgb, var(--primary-2) 5%, var(--surface-light)) 72%);
  box-shadow: var(--shadow-lg);
}
.hotspots__figure::after { content: ""; position: absolute; inset: 0; z-index: 2; border-radius: inherit; pointer-events: none; box-shadow: inset 0 0 0 1px color-mix(in srgb, var(--text-main) 9%, transparent); }
.hotspots__art { display: block; width: 100%; height: auto; }
.hotspots__spots { position: absolute; inset: 0; z-index: 1; }

/* Drawing palette */
.hotspots__art .hotspots__obj { stroke: var(--hotspots-ink); stroke-width: 1.5; stroke-linejoin: round; }
.hotspots__line, .hotspots__hair, .hotspots__tile, .hotspots__timber, .hotspots__shingles, .hotspots__pipe, .hotspots__spout, .hotspots__breakers { fill: none; stroke-linecap: round; stroke-linejoin: round; }
.hotspots__line { stroke: var(--hotspots-ink); stroke-width: 1.5; }
.hotspots__hair { stroke: var(--hotspots-hair); stroke-width: 1; }
.hotspots__cloud { fill: var(--surface-light); opacity: 0.85; }
.hotspots__trunk { fill: color-mix(in srgb, var(--warning) 55%, var(--text-main)); }
.hotspots__tree { fill: color-mix(in srgb, var(--primary-2) 40%, var(--surface-light)); }
.hotspots__tree--deep { fill: color-mix(in srgb, var(--primary-2) 62%, var(--surface-light)); }
.hotspots__soil { fill: color-mix(in srgb, var(--warning) 20%, var(--surface-light)); }
.hotspots__pebble { fill: color-mix(in srgb, var(--warning) 42%, var(--surface-light)); }
.hotspots__grass { fill: color-mix(in srgb, var(--success) 52%, var(--surface-light)); }
.hotspots__room--attic { fill: color-mix(in srgb, var(--accent) 15%, var(--surface-light)); }
.hotspots__room--bed { fill: color-mix(in srgb, var(--primary) 8%, var(--surface-light)); }
.hotspots__room--bath { fill: color-mix(in srgb, var(--primary-2) 11%, var(--surface-light)); }
.hotspots__room--living { fill: color-mix(in srgb, var(--accent) 9%, var(--surface-light)); }
.hotspots__room--kitchen { fill: color-mix(in srgb, var(--primary-2) 6%, var(--surface-light)); }
.hotspots__room--base { fill: color-mix(in srgb, var(--text-main) 10%, var(--surface-muted)); }
.hotspots__insul { fill: color-mix(in srgb, var(--danger) 20%, var(--surface-light)); stroke: color-mix(in srgb, var(--danger) 36%, var(--surface-light)); stroke-width: 1; }
.hotspots__timber { stroke: color-mix(in srgb, var(--warning) 50%, var(--surface-light)); stroke-width: 5; }
.hotspots__brick { fill: color-mix(in srgb, color-mix(in srgb, var(--danger) 45%, var(--warning)) 72%, var(--surface-light)); }
.hotspots__cut { fill: color-mix(in srgb, var(--text-main) 92%, var(--primary)); }
.hotspots__roof { fill: color-mix(in srgb, var(--text-main) 80%, var(--primary)); }
.hotspots__shingles { stroke: color-mix(in srgb, var(--surface-light) 26%, transparent); stroke-width: 1.5; stroke-dasharray: 9 5; }
.hotspots__metal { fill: color-mix(in srgb, var(--text-muted) 38%, var(--surface-light)); }
.hotspots__spout { stroke: color-mix(in srgb, var(--text-muted) 55%, var(--surface-light)); stroke-width: 7; }
.hotspots__glass { fill: color-mix(in srgb, var(--primary) 16%, var(--surface-light)); }
.hotspots__wood { fill: color-mix(in srgb, var(--warning) 28%, var(--surface-light)); }
.hotspots__white { fill: var(--surface-light); }
.hotspots__glow { fill: color-mix(in srgb, var(--accent) 65%, var(--surface-light)); }
.hotspots__fabric { fill: color-mix(in srgb, var(--primary) 46%, var(--surface-light)); }
.hotspots__fabric--deep { fill: color-mix(in srgb, var(--primary) 62%, var(--surface-light)); }
.hotspots__fabric--alt { fill: color-mix(in srgb, var(--primary-2) 42%, var(--surface-light)); }
.hotspots__rug { fill: color-mix(in srgb, var(--accent) 32%, var(--surface-light)); }
.hotspots__plant { fill: color-mix(in srgb, var(--success) 58%, var(--surface-light)); }
.hotspots__tile { stroke: color-mix(in srgb, var(--primary-2) 24%, var(--surface-light)); stroke-width: 1; }
.hotspots__counter { fill: color-mix(in srgb, var(--text-main) 72%, var(--surface-light)); }
.hotspots__breaker-box { fill: color-mix(in srgb, var(--text-main) 84%, var(--surface-light)); }
.hotspots__breakers { stroke: color-mix(in srgb, var(--surface-light) 72%, transparent); stroke-width: 3; }
.hotspots__pipe { stroke-width: 3; }
.hotspots__pipe--hot { stroke: color-mix(in srgb, var(--danger) 62%, var(--surface-light)); }
.hotspots__pipe--cold { stroke: color-mix(in srgb, var(--primary) 58%, var(--surface-light)); }

/* Markers: 44px buttons with a numbered pin; three pulses on entering view */
.hotspots__spot {
  position: absolute; left: var(--hotspots-x); top: var(--hotspots-y);
  display: grid; place-items: center; width: 2.75rem; height: 2.75rem; margin: -1.375rem 0 0 -1.375rem; padding: 0;
  border: 0; border-radius: 50%; background: none; cursor: pointer; -webkit-tap-highlight-color: transparent;
}
.hotspots__spot::before { content: ""; position: absolute; inset: 0.5rem; border: 2px solid var(--primary); border-radius: 50%; opacity: 0; pointer-events: none; }
.hotspots.is-pulsing .hotspots__spot::before { animation: hotspots-pulse 1.4s var(--ease-out) calc(var(--hotspots-i, 0) * 90ms + 200ms) 3; }
.hotspots__pin {
  position: relative; display: grid; place-items: center; width: 1.75rem; height: 1.75rem; border-radius: 50%;
  background: var(--surface-light); color: var(--text-main); font: 700 0.75rem/1 var(--font-mono);
  box-shadow: inset 0 0 0 2px var(--primary), 0 0 0 4px color-mix(in srgb, var(--primary) 20%, transparent), var(--shadow-md);
  transition: transform var(--dur-3) var(--ease-spring), background-color var(--dur-2), color var(--dur-2), box-shadow var(--dur-3) var(--ease-out);
}
.hotspots__spot:hover .hotspots__pin, .hotspots__spot.is-lit .hotspots__pin {
  transform: scale(1.15);
  box-shadow: inset 0 0 0 2px var(--primary), 0 0 0 7px color-mix(in srgb, var(--primary) 24%, transparent), var(--shadow-lg);
}
.hotspots__spot.is-active .hotspots__pin { transform: scale(1.2); background: var(--primary); color: var(--text-inverse); }
.hotspots__spot:active .hotspots__pin { transform: scale(0.94); }
.hotspots__spot:focus-visible { outline: 2px solid transparent; }
.hotspots__spot:focus-visible .hotspots__pin { box-shadow: inset 0 0 0 2px var(--primary), 0 0 0 3px var(--surface-light), 0 0 0 5px var(--primary), var(--shadow-lg); }

/* Side list */
.hotspots__panel { padding: 0.75rem; border-radius: var(--radius-2xl); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.hotspots__panel-head { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; padding: 0.5rem 0.5rem 0.75rem; }
.hotspots__panel-title { margin: 0; font: 600 1.0625rem/1.2 var(--font-display); letter-spacing: var(--tracking-tight); }
.hotspots__panel-meta, .hotspots__entry-life, .hotspots__pop-eyebrow, .hotspots__label, .hotspots__scale { font-family: var(--font-mono); letter-spacing: 0.06em; text-transform: uppercase; }
.hotspots__panel-meta { color: var(--text-muted); font-size: 0.6875rem; }
.hotspots__list { display: grid; gap: 0.25rem; margin: 0; padding: 0; list-style: none; }
.hotspots__entry {
  display: grid; grid-template-columns: auto minmax(0, 1fr) auto; align-items: center; gap: 0.75rem; width: 100%; min-height: 3.25rem;
  padding: 0.5rem 0.75rem 0.5rem 0.5rem; border: 0; border-radius: var(--radius-lg); background: transparent; color: inherit;
  font: inherit; text-align: left; cursor: pointer;
  transition: background-color var(--dur-2), box-shadow var(--dur-2);
}
.hotspots__entry:hover, .hotspots__entry.is-lit { background: var(--surface-light); box-shadow: inset 0 0 0 1px var(--border-subtle), var(--shadow-sm); }
.hotspots__entry[aria-expanded="true"] { background: var(--surface-light); box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--primary) 45%, transparent), var(--shadow-sm); }
.hotspots__num {
  display: grid; place-items: center; width: 2rem; height: 2rem; border-radius: 0.625rem;
  background: var(--surface-light); color: var(--text-main); font: 700 0.75rem/1 var(--font-mono);
  box-shadow: inset 0 0 0 1.5px color-mix(in srgb, var(--primary) 55%, transparent);
  transition: background-color var(--dur-2), color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.hotspots__entry:hover .hotspots__num, .hotspots__entry.is-lit .hotspots__num, .hotspots__entry[aria-expanded="true"] .hotspots__num { background: var(--primary); color: var(--text-inverse); transform: scale(1.06); }
.hotspots__entry-text strong { display: block; font-size: 0.9375rem; font-weight: 600; }
.hotspots__entry-text small { display: block; margin-top: 0.125rem; color: var(--text-muted); font-size: 0.8125rem; }
.hotspots__entry-life { color: var(--text-muted); font-size: 0.6875rem; white-space: nowrap; }
.hotspots__panel-cta {
  display: flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 2.75rem; margin-top: 0.75rem; padding: 0 1rem;
  border-radius: var(--radius-full); background: var(--text-main); color: var(--surface-light); font-size: 0.875rem; font-weight: 600; text-decoration: none;
  box-shadow: var(--highlight-inverse), 0 10px 22px -12px color-mix(in srgb, var(--text-main) 80%, transparent);
  transition: transform var(--dur-3) var(--ease-spring);
}

/* Card: a bottom sheet on phones, anchored to its marker from 768px */
.hotspots__pop {
  position: fixed; inset: auto 0.75rem max(0.75rem, env(safe-area-inset-bottom)); width: auto; max-width: 30rem; max-height: min(80svh, 36rem); margin: 0 auto;
  overflow: auto; overscroll-behavior: contain; padding: 1.25rem; border: 0; border-radius: var(--radius-2xl);
  background: var(--surface-light); color: var(--text-main);
  box-shadow: 0 0 0 1px var(--border-subtle), var(--shadow-xl), 0 30px 70px -24px color-mix(in srgb, var(--surface-deep) 40%, transparent);
  opacity: 0; transform: translateY(1.5rem) scale(0.98); transform-origin: 50% 100%;
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring);
  transition: opacity var(--dur-3) var(--ease-out), transform var(--dur-4) var(--ease-spring), overlay var(--dur-4) allow-discrete, display var(--dur-4) allow-discrete;
}
.hotspots__pop:popover-open { opacity: 1; transform: none; }
@starting-style {
  .hotspots__pop:popover-open { opacity: 0; transform: translateY(1.5rem) scale(0.98); }
}
.hotspots__pop::backdrop { background: color-mix(in srgb, var(--surface-deep) 30%, transparent); }
.hotspots__pop-head { display: grid; grid-template-columns: auto minmax(0, 1fr) auto; align-items: center; gap: 0.75rem; }
.hotspots__pop-num {
  display: grid; place-items: center; width: 2.5rem; height: 2.5rem; border-radius: 0.875rem;
  background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: var(--text-inverse); font: 700 0.875rem/1 var(--font-mono);
  box-shadow: var(--highlight-inverse), 0 8px 18px -8px var(--primary);
}
.hotspots__pop-eyebrow { margin: 0; color: var(--text-muted); font-size: 0.6875rem; }
.hotspots__pop-title { margin: 0.25rem 0 0; font: 600 1.25rem/1.15 var(--font-display); letter-spacing: var(--tracking-tight); }
.hotspots__close {
  display: grid; place-items: center; width: 2.25rem; height: 2.25rem; padding: 0; border: 0; border-radius: 50%; cursor: pointer;
  background: var(--surface-muted); color: var(--text-muted);
  transition: background-color var(--dur-2), color var(--dur-2), transform var(--dur-3) var(--ease-spring);
}
.hotspots__close:hover { background: var(--border-subtle); color: var(--text-main); transform: rotate(90deg); }
.hotspots__label { display: flex; align-items: center; gap: 0.625rem; margin: 1.25rem 0 0.625rem; color: var(--text-muted); font-size: 0.6875rem; }
.hotspots__label::after { content: ""; flex: 1; height: 1px; background: var(--border-subtle); }
.hotspots__signs { display: grid; gap: 0.5rem; margin: 0; padding: 0; list-style: none; font-size: 0.9375rem; line-height: 1.45; }
.hotspots__signs li { position: relative; padding-left: 1.375rem; }
.hotspots__signs li::before {
  content: ""; position: absolute; left: 0.1875rem; top: 0.45em; width: 0.5rem; height: 0.5rem; border-radius: 50%;
  background: var(--warning); box-shadow: 0 0 0 3px color-mix(in srgb, var(--warning) 18%, transparent);
}

/* Lifespan meter: 0–40 yrs; typical range in brand gradient, this home's age as a dark tick */
.hotspots__life { margin-top: 1.125rem; padding: 0.875rem 0.875rem 0.75rem; border-radius: var(--radius-lg); background: var(--surface-muted); box-shadow: inset 0 0 0 1px var(--border-subtle); }
.hotspots__life p { margin: 0; }
.hotspots__life-row { display: flex; align-items: baseline; justify-content: space-between; gap: 1rem; color: var(--text-muted); font-size: 0.8125rem; }
.hotspots__life-row strong { color: var(--text-main); font: 600 0.9375rem/1 var(--font-mono); }
.hotspots__meter {
  position: relative; height: 0.5rem; margin-top: 0.75rem; border-radius: var(--radius-full);
  background: repeating-linear-gradient(90deg, transparent 0 calc(25% - 1px), color-mix(in srgb, var(--text-main) 14%, transparent) calc(25% - 1px) 25%), color-mix(in srgb, var(--text-main) 7%, var(--surface-light));
}
.hotspots__meter::before {
  content: ""; position: absolute; inset: 0; border-radius: inherit;
  background: linear-gradient(90deg, color-mix(in srgb, var(--primary) 26%, var(--surface-light)) 0 var(--hotspots-lo), var(--primary) var(--hotspots-lo), var(--primary-2) var(--hotspots-hi), transparent var(--hotspots-hi));
  clip-path: inset(0 calc(100% - var(--hotspots-hi)) 0 0 round 999px);
}
.hotspots__meter::after {
  content: ""; position: absolute; top: -0.3125rem; bottom: -0.3125rem; left: var(--hotspots-age); width: 3px; margin-left: -1.5px;
  border-radius: 2px; background: var(--text-main); box-shadow: 0 0 0 2px var(--surface-muted);
}
.hotspots__pop:popover-open .hotspots__meter::before { animation: hotspots-fill var(--dur-5) var(--ease-out) 150ms both; }
.hotspots__life .hotspots__scale { display: flex; justify-content: space-between; margin-top: 0.4375rem; color: var(--text-muted); font-size: 0.625rem; }
.hotspots__life .hotspots__yours { display: flex; align-items: center; gap: 0.5rem; margin-top: 0.625rem; font-size: 0.8125rem; font-weight: 500; }
.hotspots__yours::before { content: ""; flex: none; width: 3px; height: 0.875rem; border-radius: 2px; background: var(--text-main); }
.hotspots__cta {
  display: flex; align-items: center; justify-content: center; gap: 0.5rem; min-height: 2.75rem; margin-top: 1rem; padding: 0 1rem;
  border-radius: var(--radius-full); background: linear-gradient(180deg, var(--primary), var(--primary-hover)); color: var(--text-inverse);
  font-size: 0.9375rem; font-weight: 600; text-decoration: none;
  box-shadow: inset 0 1px 0 color-mix(in srgb, var(--surface-light) 25%, transparent), 0 10px 24px -10px var(--primary);
  transition: transform var(--dur-3) var(--ease-spring);
}
.hotspots__cta:hover, .hotspots__panel-cta:hover { transform: translateY(-1px); }
.hotspots__cta:active, .hotspots__panel-cta:active { transform: scale(0.97); }
.hotspots__cta svg, .hotspots__panel-cta svg { transition: transform var(--dur-3) var(--ease-spring); }
.hotspots__cta:hover svg, .hotspots__panel-cta:hover svg { transform: translateX(3px); }
.hotspots :is(.hotspots__entry, .hotspots__close, .hotspots__cta, .hotspots__panel-cta):focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }

@media (min-width: 768px) {
  .hotspots__list { grid-template-columns: 1fr 1fr; }
  /* Fallback without anchor positioning or JS: centred on screen */
  .hotspots__pop { inset: 0; width: 21rem; max-height: none; margin: auto; transform: translateY(0.5rem) scale(0.9); }
  @starting-style {
    .hotspots__pop:popover-open { transform: translateY(0.5rem) scale(0.9); }
  }
  .hotspots__pop::backdrop { background: transparent; }
  /* JS placement (left/top set inline) */
  .hotspots--placed .hotspots__pop { position: absolute; inset: auto; margin: 0; }
  /* CSS anchor positioning: above the marker, flipping below or beside it when there's no room */
  @supports (position-area: top) {
    .hotspots__pop { position: absolute; inset: auto; margin: 0.75rem; position-area: top; position-try-fallbacks: flip-block, right, left; }
  }
}
@media (min-width: 1024px) {
  .hotspots__layout { grid-template-columns: minmax(0, 1fr) 20rem; gap: 1.5rem; }
  .hotspots__list { grid-template-columns: 1fr; }
}

/* No Popover API: show every card as a static grid under the drawing */
@supports not selector(:popover-open) {
  .hotspots__pops { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 18rem), 1fr)); gap: 1rem; margin-top: 1.5rem; }
  .hotspots__pop { position: static; inset: auto; width: auto; max-width: none; max-height: none; margin: 0; opacity: 1; transform: none; }
  .hotspots__close { display: none; }
}

@media (prefers-reduced-motion: reduce) {
  .hotspots *, .hotspots *::before, .hotspots *::after { animation: none !important; }
}
@keyframes hotspots-pulse { from { opacity: 0.75; transform: scale(1); } to { opacity: 0; transform: scale(2.4); } }
@keyframes hotspots-fill { from { clip-path: inset(0 100% 0 0 round 999px); } }
```

## JS

```js
const reduce = matchMedia('(prefers-reduced-motion: reduce)');
const wide = matchMedia('(min-width: 768px)');
const anchored = CSS.supports('position-area: top');

document.querySelectorAll('[data-hotspots]').forEach((root) => {
  if (!('popover' in HTMLElement.prototype)) return; // CSS shows every card as a static grid instead
  const spots = [...root.querySelectorAll('.hotspots__spot')];
  const entries = [...root.querySelectorAll('.hotspots__entry')];
  const spotFor = (el) => spots.find((spot) => spot.dataset.hotspotsKey === el.dataset.hotspotsKey);
  root.classList.toggle('hotspots--placed', !anchored);

  // Without CSS anchor positioning: sit above the marker, or below it when there's no room
  const place = (pop, spot) => {
    pop.style.left = pop.style.top = pop.style.transformOrigin = '';
    if (anchored || !wide.matches) return;
    const r = spot.getBoundingClientRect();
    const gap = 12;
    const above = r.top - pop.offsetHeight - gap > gap;
    const left = Math.min(Math.max(gap, r.left + r.width / 2 - pop.offsetWidth / 2), innerWidth - pop.offsetWidth - gap);
    pop.style.left = `${left + scrollX}px`;
    pop.style.top = `${(above ? r.top - pop.offsetHeight - gap : r.bottom + gap) + scrollY}px`;
    pop.style.transformOrigin = above ? '50% 100%' : '50% 0';
  };

  // Each card: its openers mirror it in aria-expanded, and its marker stays lit while it's open
  root.querySelectorAll('.hotspots__pop').forEach((pop) => {
    const openers = [...root.querySelectorAll(`[popovertarget="${pop.id}"]:not([popovertargetaction="hide"])`)];
    const spot = openers.find((el) => el.classList.contains('hotspots__spot'));
    openers.forEach((el) => el.setAttribute('aria-expanded', 'false'));
    pop.addEventListener('toggle', (e) => {
      const open = e.newState === 'open';
      openers.forEach((el) => el.setAttribute('aria-expanded', String(open)));
      spot.classList.toggle('is-active', open);
      if (open) place(pop, spot);
    });
    addEventListener('resize', () => { if (pop.matches(':popover-open')) place(pop, spot); });
  });

  // List entries and markers light each other up
  entries.forEach((entry) => {
    const spot = spotFor(entry);
    const lit = (on) => { spot.classList.toggle('is-lit', on); entry.classList.toggle('is-lit', on); };
    [entry, spot].forEach((el) => {
      el.addEventListener('pointerenter', () => lit(true));
      el.addEventListener('pointerleave', () => lit(false));
    });
    entry.addEventListener('focus', () => lit(true));
    entry.addEventListener('blur', () => lit(false));
  });

  // Markers are one tab stop; arrow keys move between them, and an open card follows the focus
  let current = 0;
  const rove = (index) => spots.forEach((spot, n) => { spot.tabIndex = n === index ? 0 : -1; });
  rove(0);
  spots.forEach((spot, n) => spot.addEventListener('focus', () => { current = n; rove(n); }));
  root.querySelector('.hotspots__spots').addEventListener('keydown', (e) => {
    const moves = { ArrowRight: current + 1, ArrowDown: current + 1, ArrowLeft: current - 1, ArrowUp: current - 1, Home: 0, End: spots.length - 1 };
    if (!(e.key in moves)) return;
    e.preventDefault();
    const following = root.querySelector('.hotspots__pop:popover-open');
    const next = spots[(moves[e.key] + spots.length) % spots.length];
    next.focus();
    if (following) document.getElementById(next.getAttribute('popovertarget')).showPopover({ source: next });
  });

  // Three pulses, the first time the house is in view
  if (reduce.matches) return;
  const io = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    io.disconnect();
    root.classList.add('is-pulsing');
  }, { threshold: 0.5 });
  io.observe(root.querySelector('.hotspots__figure'));
});
```

## Notes

- Markers are real `<button>`s with `popovertarget`, `aria-haspopup="dialog"` and an `aria-expanded` that tracks their card. The six markers form one toolbar tab stop: arrow keys and Home/End move between them, and an open card follows the focus. Each card is a non-modal `role="dialog"` popover labelled by its heading. Escape or a click outside closes it and returns focus to its opener, and Tab from the opener moves straight into the card. The side list repeats every system as an ordinary button, so nothing depends on finding a marker in the drawing.
- Without JS the Popover API still works on its own, so markers, list entries and close buttons all open and close their cards. Cards are anchored with CSS anchor positioning where it's supported (detected with `@supports (position-area: top)`); elsewhere JS places them above or below the marker, and with neither they open centred on screen. Below 768px every card is a bottom sheet over a soft backdrop. Browsers without the Popover API get all the cards as a static grid under the drawing.
- Reduced motion: no pulses (JS skips them and CSS removes the keyframes), and the spring, sheet slide and bar fill become instant. The pulses are finite: three 1.4s rings with a stagger, about 4.8s in all, so they stay under the 5s limit that would need a pause control.
- Contrast: marker numbers are `--text-main` on white (14.6:1), or white on `--primary` (5.2:1) when open. Card copy uses `--text-main`, with `--text-muted` on `--surface-muted` (4.5:1) for secondary labels. The drawing is a single `role="img"` with a full text description.
- To adapt it: marker positions are percentages of the 800 × 560 drawing (`--hotspots-x` / `--hotspots-y`), and lifespans are percentages of a 40-year scale (`--hotspots-lo`, `--hotspots-hi`, `--hotspots-age`). To add a system, add a marker, a list entry and a card that share a `data-hotspots-key` and the popover id.
