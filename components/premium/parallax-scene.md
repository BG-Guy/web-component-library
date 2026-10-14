# Parallax Neighborhood

A pinned, illustrated street scene that goes from first light to morning as you scroll. Hills, houses, the street and the foreground fence rise into place at different speeds, the sky warms from navy to day while the sun climbs, lit windows click off one by one, and the branded van drives in, settles on its suspension and parks outside a customer's house. On phones the scene crops around that house (`preserveAspectRatio` slice) and drops minor details. Depends on `tokens/variables.css`.

**Motion:** depth parallax (scroll scrub, `translate` per layer) · dawn-to-day sky crossfade and land filter (smoothstep) · sun rise (ease-out) · window and lamp switch-off (`--dur-3` `--ease-out`) · van drive (cubic ease-out) with wheel spin and a `sin()` brake dip · "On site" bubble pop (`--ease-spring`).

## HTML

```html
<div class="parallax-scene-demo">
  <div class="parallax-scene-demo__intro">
    <p class="parallax-scene-demo__kicker">5:48 AM · Springfield</p>
    <p class="parallax-scene-demo__line">Scroll to bring up the sun.</p>
    <span class="parallax-scene-demo__hint" aria-hidden="true">Scroll
      <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><path d="M12 5v14M6 13l6 6 6-6" /></svg>
    </span>
  </div>

  <section class="parallax-scene" aria-labelledby="parallax-scene-title" data-parallax-scene>
    <div class="parallax-scene__stage">
      <div class="parallax-scene__sky" aria-hidden="true"></div>
      <div class="parallax-scene__stars" aria-hidden="true"></div>

      <!-- Shared paint servers and symbols for every layer -->
      <svg class="parallax-scene__defs" aria-hidden="true" focusable="false">
        <defs>
          <linearGradient id="parallax-scene-glass-fill" x1="0" y1="0" x2="0" y2="1"><stop class="parallax-scene__stop-glass-a" offset="0" /><stop class="parallax-scene__stop-glass-b" offset="1" /></linearGradient>
          <linearGradient id="parallax-scene-warm-fill" x1="0" y1="0" x2="0" y2="1"><stop class="parallax-scene__stop-warm-a" offset="0" /><stop class="parallax-scene__stop-warm-b" offset="1" /></linearGradient>
          <radialGradient id="parallax-scene-halo-fill"><stop class="parallax-scene__stop-halo" offset="0" /><stop class="parallax-scene__stop-halo-clear" offset="1" /></radialGradient>
          <radialGradient id="parallax-scene-sun-fill"><stop class="parallax-scene__stop-sun" offset="0" /><stop class="parallax-scene__stop-sun-clear" offset="1" /></radialGradient>
          <linearGradient id="parallax-scene-brand-fill" x1="0" y1="0" x2="1" y2="0"><stop class="parallax-scene__stop-brand-a" offset="0" /><stop class="parallax-scene__stop-brand-b" offset="1" /></linearGradient>
          <pattern id="parallax-scene-siding" width="8" height="9" patternUnits="userSpaceOnUse"><rect class="parallax-scene__shade" y="8" width="8" height="1" /></pattern>
          <pattern id="parallax-scene-slats" width="7" height="8" patternUnits="userSpaceOnUse"><rect class="parallax-scene__shade" width="1.5" height="8" /></pattern>
          <pattern id="parallax-scene-pickets" y="944" width="26" height="56" patternUnits="userSpaceOnUse">
            <path class="parallax-scene__picket" d="M6 56V9l7-8 7 8v47z" /><path class="parallax-scene__shade" d="M13 1l7 8v47h-3V10z" />
          </pattern>
          <symbol id="parallax-scene-win" viewBox="0 0 40 52" overflow="visible">
            <rect class="parallax-scene__trim" width="40" height="48" rx="2" />
            <rect class="parallax-scene__glass" x="4" y="4" width="32" height="40" />
            <path class="parallax-scene__glint" d="M7 40 21 8h7L14 40z" />
            <path class="parallax-scene__trim" d="M19 4h2v40h-2zM4 23h32v2H4z" />
            <rect class="parallax-scene__trim" x="-3" y="46" width="46" height="5" rx="1.5" />
            <rect class="parallax-scene__shade" x="-3" y="51" width="46" height="3" />
          </symbol>
          <symbol id="parallax-scene-win-lit" viewBox="0 0 40 52" overflow="visible">
            <ellipse class="parallax-scene__halo" cx="20" cy="24" rx="48" ry="42" />
            <rect class="parallax-scene__warm" x="4" y="4" width="32" height="40" />
            <path class="parallax-scene__mullion" d="M19 4h2v40h-2zM4 23h32v2H4z" />
          </symbol>
          <symbol id="parallax-scene-door" viewBox="0 0 32 66">
            <rect class="parallax-scene__trim" width="32" height="66" rx="1" />
            <rect class="parallax-scene__paint" x="3" y="3" width="26" height="63" />
            <rect class="parallax-scene__panel" x="7" y="8" width="18" height="18" rx="1" />
            <rect class="parallax-scene__panel" x="7" y="31" width="18" height="28" rx="1" />
            <circle class="parallax-scene__knob" cx="24" cy="38" r="1.8" />
          </symbol>
          <symbol id="parallax-scene-tree" viewBox="0 0 120 200" overflow="visible">
            <path class="parallax-scene__trunk" d="M55 200V118h10v82zM60 150l16-18 4 3-17 19z" />
            <circle class="parallax-scene__leaf-dark" cx="58" cy="84" r="52" />
            <circle class="parallax-scene__leaf-dark" cx="24" cy="108" r="28" />
            <circle class="parallax-scene__leaf-dark" cx="94" cy="110" r="26" />
            <circle class="parallax-scene__leaf" cx="68" cy="72" r="42" />
            <circle class="parallax-scene__leaf" cx="34" cy="94" r="24" />
            <circle class="parallax-scene__leaf-lit" cx="80" cy="56" r="20" />
          </symbol>
          <symbol id="parallax-scene-bush" viewBox="0 0 90 44" overflow="visible">
            <path class="parallax-scene__leaf-dark" d="M0 44a22 22 0 0 1 20-26a24 24 0 0 1 42-8a20 20 0 0 1 28 34z" />
            <path class="parallax-scene__leaf" d="M18 44a16 16 0 0 1 16-20a18 18 0 0 1 32-2a14 14 0 0 1 18 22z" />
          </symbol>
        </defs>
      </svg>

      <svg class="parallax-scene__layer parallax-scene__layer--sun" viewBox="0 0 2400 1000" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
        <circle class="parallax-scene__sun-halo" cx="1360" cy="430" r="140" />
        <circle class="parallax-scene__sun-dawn" cx="1360" cy="430" r="42" />
        <circle class="parallax-scene__sun-day" cx="1360" cy="430" r="42" />
      </svg>

      <svg class="parallax-scene__layer parallax-scene__layer--clouds" viewBox="0 0 2400 1000" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
        <path class="parallax-scene__cloud" d="M1500 260h253a33 33 0 0 0 -33 -46.2a48.4 48.4 0 0 0 -88 -24.2a37.4 37.4 0 0 0 -68.2 11a44 44 0 0 0 -63.8 59.4z" />
        <path class="parallax-scene__cloud parallax-scene__minor" d="M1990 180h144a19.2 19.2 0 0 0 -16 -24a28.8 28.8 0 0 0 -51.2 -16a24 24 0 0 0 -44.8 11.2a22.4 22.4 0 0 0 -32 28.8z" />
        <path class="parallax-scene__cloud" d="M1080 540h161a21 21 0 0 0 -21 -29.4a30.8 30.8 0 0 0 -56 -15.4a23.8 23.8 0 0 0 -43.4 7a28 28 0 0 0 -40.6 37.8z" />
        <path class="parallax-scene__cloud parallax-scene__minor" d="M400 530h144a19.2 19.2 0 0 0 -16 -24a28.8 28.8 0 0 0 -51.2 -16a24 24 0 0 0 -44.8 11.2a22.4 22.4 0 0 0 -32 28.8z" />
        <path class="parallax-scene__cloud parallax-scene__minor" d="M2180 420h138a18 18 0 0 0 -18 -25.2a26.4 26.4 0 0 0 -48 -13.2a20.4 20.4 0 0 0 -37.2 6a24 24 0 0 0 -34.8 32.4z" />
      </svg>

      <div class="parallax-scene__scrim" aria-hidden="true"></div>

      <div class="parallax-scene__land" aria-hidden="true">
        <svg class="parallax-scene__layer parallax-scene__layer--far" viewBox="0 0 2400 1000" preserveAspectRatio="xMidYMax slice" focusable="false">
          <path class="parallax-scene__hill-far" d="M0 600C160 560 300 548 460 566S760 600 940 578S1240 530 1420 552S1760 596 1960 570S2280 540 2400 556V1000H0Z" />
          <path class="parallax-scene__hill-far-2" d="M0 640C220 610 380 612 560 628S900 660 1100 632S1480 600 1680 622S2100 662 2400 628V1000H0Z" />
          <g class="parallax-scene__hill-tree parallax-scene__minor">
            <circle cx="300" cy="616" r="9" /><circle cx="314" cy="612" r="11" /><circle cx="328" cy="617" r="8" />
            <circle cx="1560" cy="610" r="9" /><circle cx="1574" cy="606" r="12" /><circle cx="1590" cy="611" r="8" />
          </g>
        </svg>

        <svg class="parallax-scene__layer parallax-scene__layer--near" viewBox="0 0 2400 1000" preserveAspectRatio="xMidYMax slice" focusable="false">
          <path class="parallax-scene__hill-near" d="M0 700C200 668 380 664 560 684S900 716 1120 690S1520 654 1740 680S2140 712 2400 682V1000H0Z" />
          <g class="parallax-scene__hill-tree parallax-scene__minor">
            <circle cx="430" cy="676" r="13" /><circle cx="450" cy="670" r="16" /><circle cx="470" cy="677" r="12" />
            <circle cx="1480" cy="664" r="12" /><circle cx="1498" cy="658" r="15" /><circle cx="1516" cy="665" r="11" />
            <circle cx="2230" cy="690" r="13" /><circle cx="2250" cy="684" r="16" />
          </g>
        </svg>

        <svg class="parallax-scene__layer parallax-scene__layer--houses" viewBox="0 0 2400 1000" preserveAspectRatio="xMidYMax slice" focusable="false">
          <rect class="parallax-scene__grass" y="786" width="2400" height="214" />

          <g class="parallax-scene__minor" style="--parallax-scene-wall: color-mix(in srgb, var(--primary-2) 18%, var(--surface-light)); --parallax-scene-roof: color-mix(in srgb, var(--primary-2) 50%, var(--surface-deep)); --parallax-scene-door: var(--accent)">
            <rect class="parallax-scene__wall" x="340" y="690" width="170" height="100" />
            <path class="parallax-scene__wall" d="M348 692 425 628l77 64z" />
            <path class="parallax-scene__roof" d="M326 700 425 612l99 88h-18l-81-72-81 72z" />
            <circle class="parallax-scene__trim" cx="425" cy="668" r="11" /><circle class="parallax-scene__glass" cx="425" cy="668" r="7.5" />
            <use href="#parallax-scene-win" x="358" y="716" width="34" height="44" />
            <use href="#parallax-scene-win" x="458" y="716" width="34" height="44" />
            <use href="#parallax-scene-door" x="410" y="728" width="30" height="62" />
            <rect class="parallax-scene__stone" x="336" y="783" width="178" height="7" />
          </g>

          <g style="--parallax-scene-wall: color-mix(in srgb, var(--primary) 16%, var(--surface-light)); --parallax-scene-roof: color-mix(in srgb, var(--text-main) 82%, var(--primary)); --parallax-scene-door: var(--primary)">
            <rect class="parallax-scene__chimney" x="728" y="566" width="20" height="44" />
            <rect class="parallax-scene__chimney-cap" x="724" y="560" width="28" height="8" rx="1" />
            <path class="parallax-scene__roof" d="M548 636 596 582h138l48 54z" />
            <path class="parallax-scene__fascia" d="M548 636 596 582h138l48 54" />
            <rect class="parallax-scene__wall" x="560" y="634" width="210" height="156" />
            <rect class="parallax-scene__siding" x="560" y="640" width="210" height="142" />
            <rect class="parallax-scene__shade" x="560" y="634" width="210" height="7" />
            <use href="#parallax-scene-win" x="578" y="650" width="40" height="52" />
            <use href="#parallax-scene-win" x="645" y="650" width="40" height="52" />
            <use href="#parallax-scene-win" x="712" y="650" width="40" height="52" />
            <path class="parallax-scene__roof" d="M624 716h82l8 12H616z" />
            <rect class="parallax-scene__trim" x="622" y="728" width="5" height="58" />
            <rect class="parallax-scene__trim" x="703" y="728" width="5" height="58" />
            <use href="#parallax-scene-door" x="649" y="724" width="32" height="66" />
            <use href="#parallax-scene-win" x="578" y="730" width="38" height="48" />
            <use href="#parallax-scene-win" x="714" y="730" width="38" height="48" />
            <rect class="parallax-scene__stone" x="556" y="782" width="218" height="8" />
            <use href="#parallax-scene-bush" x="566" y="768" width="58" height="28" />
          </g>

          <g style="--parallax-scene-wall: color-mix(in srgb, var(--accent) 24%, var(--surface-light)); --parallax-scene-roof: color-mix(in srgb, var(--danger) 50%, var(--text-main)); --parallax-scene-door: var(--primary-2)">
            <path class="parallax-scene__roof" d="M812 710 860 656h100l48 54z" />
            <path class="parallax-scene__fascia" d="M812 710 860 656h100l48 54" />
            <rect class="parallax-scene__wall" x="890" y="664" width="40" height="34" />
            <path class="parallax-scene__roof" d="M884 668 910 646l26 22z" />
            <use href="#parallax-scene-win" x="899" y="670" width="22" height="26" />
            <rect class="parallax-scene__wall" x="828" y="706" width="164" height="84" />
            <rect class="parallax-scene__siding" x="828" y="712" width="164" height="70" />
            <rect class="parallax-scene__shade" x="828" y="706" width="164" height="6" />
            <use href="#parallax-scene-win" x="842" y="722" width="36" height="46" />
            <use href="#parallax-scene-win" x="942" y="722" width="36" height="46" />
            <use href="#parallax-scene-door" x="896" y="728" width="28" height="62" />
            <rect class="parallax-scene__stone" x="824" y="782" width="172" height="8" />
          </g>

          <g class="parallax-scene__lamp">
            <rect class="parallax-scene__iron" x="1015" y="700" width="6" height="104" />
            <rect class="parallax-scene__iron" x="1009" y="800" width="18" height="6" rx="2" />
            <path class="parallax-scene__iron" d="M1006 700h24l-4-6h-16z" />
            <path class="parallax-scene__lantern" d="M1008 694l2-18h16l2 18z" />
            <path class="parallax-scene__iron" d="M1004 676h28l-14-10z" />
          </g>
          <g class="parallax-scene__minor">
            <rect class="parallax-scene__iron" x="1046" y="770" width="4" height="34" />
            <rect class="parallax-scene__mailbox" x="1037" y="758" width="22" height="14" rx="6" />
          </g>

          <g style="--parallax-scene-wall: var(--surface-light); --parallax-scene-trim: color-mix(in srgb, var(--surface-muted) 40%, var(--border-subtle)); --parallax-scene-roof: color-mix(in srgb, var(--primary) 38%, var(--surface-deep)); --parallax-scene-door: var(--primary)">
            <rect class="parallax-scene__chimney" x="1196" y="548" width="20" height="56" />
            <rect class="parallax-scene__chimney-cap" x="1192" y="542" width="28" height="8" rx="1" />
            <rect class="parallax-scene__wall" x="1060" y="618" width="180" height="172" />
            <path class="parallax-scene__wall" d="M1060 620 1150 552l90 68z" />
            <rect class="parallax-scene__siding" x="1060" y="624" width="180" height="158" />
            <path class="parallax-scene__roof" d="M1040 622 1150 530l110 92h-22l-88-72-88 72z" />
            <rect class="parallax-scene__shade" x="1060" y="622" width="180" height="5" />
            <circle class="parallax-scene__trim" cx="1150" cy="592" r="13" /><circle class="parallax-scene__glass" cx="1150" cy="592" r="9" />
            <use href="#parallax-scene-win" x="1082" y="640" width="40" height="52" />
            <use href="#parallax-scene-win" x="1178" y="640" width="40" height="52" />
            <path class="parallax-scene__roof" d="M1110 712h80l8 12h-96z" />
            <rect class="parallax-scene__trim" x="1108" y="724" width="5" height="62" />
            <rect class="parallax-scene__trim" x="1187" y="724" width="5" height="62" />
            <use href="#parallax-scene-door" x="1134" y="724" width="32" height="66" />
            <use href="#parallax-scene-win" x="1068" y="728" width="34" height="46" />
            <use href="#parallax-scene-win" x="1198" y="728" width="34" height="46" />
            <rect class="parallax-scene__stone" x="1056" y="782" width="188" height="8" />
            <rect class="parallax-scene__stone" x="1126" y="790" width="48" height="6" />
            <rect class="parallax-scene__stone" x="1120" y="796" width="60" height="6" />
            <rect class="parallax-scene__wall" x="1240" y="694" width="100" height="96" />
            <path class="parallax-scene__wall" d="M1246 698 1290 666l44 32z" />
            <path class="parallax-scene__roof" d="M1230 700 1290 654l60 46h-16l-44-34-44 34z" />
            <rect class="parallax-scene__shade" x="1240" y="698" width="100" height="5" />
            <rect class="parallax-scene__trim" x="1254" y="716" width="72" height="74" rx="2" />
            <path class="parallax-scene__groove" d="M1258 738h64M1258 756h64M1258 774h64" />
            <path class="parallax-scene__glass" d="M1259 722h13v9h-13zM1276 722h13v9h-13zM1293 722h13v9h-13zM1310 722h13v9h-13z" />
            <rect class="parallax-scene__iron" x="1243" y="722" width="7" height="10" rx="2" />
            <path class="parallax-scene__drive" d="M1254 790h72l12 16h-96z" />
            <path class="parallax-scene__drive" d="M1132 802h36l6 4h-48z" />
          </g>

          <g style="--parallax-scene-wall: color-mix(in srgb, var(--text-muted) 32%, var(--surface-light)); --parallax-scene-roof: var(--text-main); --parallax-scene-door: var(--accent); --parallax-scene-wood: color-mix(in srgb, var(--warning) 62%, var(--surface-light))">
            <rect class="parallax-scene__wood" x="1480" y="630" width="130" height="72" />
            <rect class="parallax-scene__slats" x="1480" y="630" width="130" height="72" />
            <rect class="parallax-scene__roof" x="1472" y="622" width="146" height="9" rx="1" />
            <use href="#parallax-scene-win" x="1494" y="644" width="102" height="44" />
            <rect class="parallax-scene__wall" x="1420" y="702" width="200" height="88" />
            <rect class="parallax-scene__roof" x="1412" y="696" width="216" height="9" rx="1" />
            <use href="#parallax-scene-win" x="1436" y="716" width="94" height="62" />
            <use href="#parallax-scene-door" x="1560" y="724" width="30" height="66" />
            <rect class="parallax-scene__stone" x="1416" y="782" width="208" height="8" />
          </g>

          <g style="--parallax-scene-wall: color-mix(in srgb, var(--success) 18%, var(--surface-light)); --parallax-scene-roof: color-mix(in srgb, var(--text-main) 88%, var(--surface-light)); --parallax-scene-door: var(--danger)">
            <rect class="parallax-scene__chimney" x="1868" y="600" width="20" height="50" />
            <rect class="parallax-scene__chimney-cap" x="1864" y="594" width="28" height="8" rx="1" />
            <path class="parallax-scene__roof" d="M1666 714 1730 622h140l64 92z" />
            <path class="parallax-scene__fascia" d="M1666 714 1730 622h140l64 92" />
            <rect class="parallax-scene__wall" x="1728" y="654" width="36" height="38" />
            <path class="parallax-scene__roof" d="M1722 658 1746 638l24 20z" />
            <use href="#parallax-scene-win" x="1735" y="660" width="22" height="28" />
            <rect class="parallax-scene__wall" x="1836" y="654" width="36" height="38" />
            <path class="parallax-scene__roof" d="M1830 658 1854 638l24 20z" />
            <use href="#parallax-scene-win" x="1843" y="660" width="22" height="28" />
            <rect class="parallax-scene__wall" x="1680" y="708" width="240" height="82" />
            <rect class="parallax-scene__siding" x="1680" y="714" width="240" height="68" />
            <rect class="parallax-scene__shade" x="1680" y="708" width="240" height="6" />
            <path class="parallax-scene__roof" d="M1690 722h8v46h-8zM1738 722h8v46h-8zM1852 722h8v46h-8zM1900 722h8v46h-8z" />
            <use href="#parallax-scene-win" x="1700" y="722" width="36" height="46" />
            <use href="#parallax-scene-win" x="1862" y="722" width="36" height="46" />
            <use href="#parallax-scene-door" x="1784" y="724" width="32" height="66" />
            <rect class="parallax-scene__stone" x="1676" y="782" width="248" height="8" />
          </g>

          <g class="parallax-scene__minor" style="--parallax-scene-wall: color-mix(in srgb, var(--danger) 12%, var(--surface-light)); --parallax-scene-roof: color-mix(in srgb, var(--danger) 45%, var(--text-main)); --parallax-scene-door: var(--primary)">
            <path class="parallax-scene__roof" d="M1968 652 2030 604h100l62 48z" />
            <rect class="parallax-scene__wall" x="1980" y="650" width="200" height="140" />
            <rect class="parallax-scene__shade" x="1980" y="650" width="200" height="6" />
            <use href="#parallax-scene-win" x="2000" y="666" width="40" height="52" />
            <use href="#parallax-scene-win" x="2120" y="666" width="40" height="52" />
            <use href="#parallax-scene-win" x="2000" y="734" width="38" height="46" />
            <use href="#parallax-scene-door" x="2124" y="724" width="32" height="66" />
          </g>

          <use href="#parallax-scene-tree" x="487" y="632" width="96" height="160" />
          <use href="#parallax-scene-tree" x="1332" y="626" width="100" height="166" />
          <use href="#parallax-scene-tree" x="1604" y="644" width="90" height="148" />
          <use class="parallax-scene__minor" href="#parallax-scene-tree" x="1904" y="630" width="96" height="160" />
        </svg>

        <svg class="parallax-scene__layer parallax-scene__layer--road" viewBox="0 0 2400 1000" preserveAspectRatio="xMidYMax slice" focusable="false">
          <rect class="parallax-scene__sidewalk" y="806" width="2400" height="22" />
          <path class="parallax-scene__joints" d="M0 817H2400" />
          <rect class="parallax-scene__apron" x="1242" y="806" width="96" height="22" />
          <rect class="parallax-scene__curb" y="826" width="2400" height="8" />
          <rect class="parallax-scene__asphalt" y="834" width="2400" height="166" />
          <path class="parallax-scene__gutter" d="M0 839H2400" />
          <path class="parallax-scene__lane" d="M0 904H2400" />

          <g class="parallax-scene__van">
            <ellipse class="parallax-scene__van-shadow" cx="1208" cy="926" rx="172" ry="9" />
            <g class="parallax-scene__van-body">
              <path class="parallax-scene__rack" d="M1084 764v-12h176v12M1090 746h164M1090 740h164M1100 740v6M1120 740v6M1140 740v6M1160 740v6M1180 740v6M1200 740v6M1220 740v6M1240 740v6" />
              <path class="parallax-scene__van-paint" d="M1056 904V786q0-22 22-22h192q16 0 26 12l32 54q22 4 28 20q2 6 2 12v42z" />
              <path class="parallax-scene__van-stripe" d="M1056 866c90-4 170-26 252-34l40 2c4 4 7 9 9 14c-96 6-196 28-301 40z" />
              <rect class="parallax-scene__van-skirt" x="1056" y="888" width="302" height="16" />
              <path class="parallax-scene__van-glass" d="M1262 786h30l22 40h-52z" />
              <path class="parallax-scene__glint" d="M1272 786h9l-19 34v-17z" />
              <path class="parallax-scene__van-seam" d="M1256 772v114" />
              <rect class="parallax-scene__van-trim" x="1264" y="838" width="14" height="4" rx="2" />
              <rect class="parallax-scene__van-trim" x="1316" y="800" width="8" height="16" rx="3" />
              <path class="parallax-scene__van-light" d="M1342 846h12q4 0 4 6v4h-16z" />
              <rect class="parallax-scene__van-tail" x="1052" y="790" width="7" height="28" rx="2" />
              <rect class="parallax-scene__van-bumper" x="1334" y="886" width="28" height="18" rx="4" />
              <rect class="parallax-scene__van-bumper" x="1050" y="888" width="16" height="16" rx="4" />
              <rect class="parallax-scene__van-badge" x="1074" y="782" width="30" height="30" rx="8" />
              <path class="parallax-scene__van-glyph" d="M1081 799l8-7 8 7v8h-16z" />
              <text class="parallax-scene__van-word" x="1112" y="806">Brand</text>
              <text class="parallax-scene__van-tag" x="1113" y="824">HOME SERVICES</text>
              <text class="parallax-scene__van-tel" x="1076" y="852">(555) 555-0123</text>
              <path class="parallax-scene__van-arch" d="M1080 904a32 32 0 0 1 64 0zM1268 904a32 32 0 0 1 64 0z" />
            </g>
            <g class="parallax-scene__wheel">
              <circle class="parallax-scene__tire" cx="1112" cy="902" r="24" />
              <circle class="parallax-scene__rim" cx="1112" cy="902" r="14" />
              <path class="parallax-scene__spokes" d="M1112 889v26M1099 902h26M1103 893l18 18M1121 893l-18 18" />
              <circle class="parallax-scene__hub" cx="1112" cy="902" r="4" />
            </g>
            <g class="parallax-scene__wheel">
              <circle class="parallax-scene__tire" cx="1300" cy="902" r="24" />
              <circle class="parallax-scene__rim" cx="1300" cy="902" r="14" />
              <path class="parallax-scene__spokes" d="M1300 889v26M1287 902h26M1291 893l18 18M1309 893l-18 18" />
              <circle class="parallax-scene__hub" cx="1300" cy="902" r="4" />
            </g>
          </g>

          <g class="parallax-scene__bubble">
            <path class="parallax-scene__bubble-bg" d="M1226 694h150q10 0 10 10v22q0 10-10 10h-62l-12 12-12-12h-64q-10 0-10-10v-22q0-10 10-10z" />
            <circle class="parallax-scene__bubble-dot" cx="1240" cy="715" r="5" />
            <text class="parallax-scene__bubble-text" x="1254" y="721">On site · 8:00</text>
          </g>
        </svg>

        <svg class="parallax-scene__layer parallax-scene__layer--front" viewBox="0 0 2400 1000" preserveAspectRatio="xMidYMax slice" focusable="false">
          <rect class="parallax-scene__grass-near" y="930" width="2400" height="70" />
          <path class="parallax-scene__trunk" d="M168 1000c8-90 0-170 16-292h22c12 120 8 200 20 292zM196 800c30-30 62-44 98-50l4 12c-36 8-64 22-90 50z" />
          <circle class="parallax-scene__leaf-dark" cx="150" cy="640" r="150" />
          <circle class="parallax-scene__leaf-dark" cx="300" cy="700" r="96" />
          <circle class="parallax-scene__leaf" cx="200" cy="580" r="118" />
          <circle class="parallax-scene__leaf" cx="318" cy="660" r="62" />
          <circle class="parallax-scene__leaf-lit" cx="268" cy="536" r="58" />
          <path class="parallax-scene__trunk" d="M2232 1000c-8-90 0-170-16-292h-22c-12 120-8 200-20 292zM2204 800c-30-30-62-44-98-50l-4 12c36 8 64 22 90 50z" />
          <circle class="parallax-scene__leaf-dark" cx="2250" cy="640" r="150" />
          <circle class="parallax-scene__leaf-dark" cx="2100" cy="700" r="96" />
          <circle class="parallax-scene__leaf" cx="2200" cy="580" r="118" />
          <circle class="parallax-scene__leaf" cx="2082" cy="660" r="62" />
          <circle class="parallax-scene__leaf-lit" cx="2132" cy="536" r="58" />
          <rect class="parallax-scene__fence" y="944" width="2400" height="56" />
          <rect class="parallax-scene__rail" y="958" width="2400" height="6" />
          <rect class="parallax-scene__rail" y="982" width="2400" height="6" />
          <use href="#parallax-scene-bush" x="380" y="900" width="150" height="74" />
          <use href="#parallax-scene-bush" x="1436" y="912" width="110" height="56" />
          <use href="#parallax-scene-bush" x="1880" y="904" width="130" height="66" />
          <use class="parallax-scene__minor" href="#parallax-scene-bush" x="760" y="920" width="100" height="50" />
        </svg>
      </div>

      <!-- Window and lamp lights: above the land so they glow; they move with the houses -->
      <svg class="parallax-scene__layer parallax-scene__layer--lights" viewBox="0 0 2400 1000" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
        <use class="parallax-scene__lit parallax-scene__minor" href="#parallax-scene-win-lit" x="458" y="716" width="34" height="44" style="--parallax-scene-at: .4" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="645" y="650" width="40" height="52" style="--parallax-scene-at: .34" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="714" y="730" width="38" height="48" style="--parallax-scene-at: .5" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="899" y="670" width="22" height="26" style="--parallax-scene-at: .3" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="842" y="722" width="36" height="46" style="--parallax-scene-at: .56" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="1082" y="640" width="40" height="52" style="--parallax-scene-at: .44" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="1068" y="728" width="34" height="46" style="--parallax-scene-at: .6" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="1494" y="644" width="102" height="44" style="--parallax-scene-at: .38" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="1436" y="716" width="94" height="62" style="--parallax-scene-at: .62" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="1735" y="660" width="22" height="28" style="--parallax-scene-at: .32" />
        <use class="parallax-scene__lit" href="#parallax-scene-win-lit" x="1862" y="722" width="36" height="46" style="--parallax-scene-at: .48" />
        <g class="parallax-scene__lit" style="--parallax-scene-at: .55">
          <circle class="parallax-scene__halo" cx="1018" cy="685" r="70" />
          <path class="parallax-scene__warm" d="M1008 694l2-18h16l2 18z" />
        </g>
        <g class="parallax-scene__lit" style="--parallax-scene-at: .52">
          <circle class="parallax-scene__halo" cx="1246" cy="727" r="30" />
          <rect class="parallax-scene__warm" x="1243" y="722" width="7" height="10" rx="2" />
        </g>
      </svg>

      <div class="parallax-scene__inner">
        <div class="parallax-scene__copy">
          <p class="parallax-scene__time" aria-hidden="true">
            <svg viewBox="0 0 24 24" width="16" height="16" focusable="false"><circle cx="12" cy="12" r="4" /><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4" /></svg>
            <span data-parallax-scene-clock>8:00 AM</span>
          </p>
          <h2 id="parallax-scene-title" class="parallax-scene__title">Your neighbors already trust us</h2>
          <p class="parallax-scene__lead">1,200+ homes across Westlake, Northside and Riverside booked us last year, most on a neighbor's word.</p>
          <div class="parallax-scene__actions">
            <a class="parallax-scene__btn" href="#book">
              Book a visit
              <svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true" focusable="false"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
            </a>
            <p class="parallax-scene__rating"><strong>4.9/5</strong> from 1,200+ reviews</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <div class="parallax-scene-demo__outro">
    <p class="parallax-scene-demo__kicker">Same-day visits</p>
    <p class="parallax-scene-demo__line">On your street before the coffee's cold.</p>
  </div>
</div>
```

## CSS

```css
@property --parallax-scene-p { syntax: "<number>"; inherits: true; initial-value: 1; }

/* Palette (all token mixes) and the values derived from scroll progress. p = 1 is midday: the static fallback. */
.parallax-scene {
  --parallax-scene-sky-day-1: color-mix(in srgb, var(--primary) 80%, var(--surface-deep));
  --parallax-scene-sky-day-2: var(--primary);
  --parallax-scene-sky-day-3: color-mix(in srgb, var(--primary) 45%, var(--surface-light));
  --parallax-scene-sky-day-4: color-mix(in srgb, var(--primary-2) 12%, var(--surface-light));
  --parallax-scene-sky-dawn-1: color-mix(in srgb, var(--primary) 20%, var(--surface-deep));
  --parallax-scene-sky-dawn-2: color-mix(in srgb, color-mix(in srgb, var(--primary) 55%, var(--danger)) 45%, var(--surface-deep));
  --parallax-scene-sky-dawn-3: color-mix(in srgb, color-mix(in srgb, var(--danger) 55%, var(--accent)) 70%, var(--parallax-scene-sky-dawn-2));
  --parallax-scene-sky-dawn-4: color-mix(in srgb, var(--accent) 60%, var(--surface-light));
  --parallax-scene-hill-far: color-mix(in srgb, var(--primary) 26%, var(--surface-light));
  --parallax-scene-hill-far-2: color-mix(in srgb, var(--primary-2) 34%, var(--parallax-scene-hill-far));
  --parallax-scene-hill-near: color-mix(in srgb, var(--success) 50%, var(--parallax-scene-hill-far-2));
  --parallax-scene-hill-tree: color-mix(in srgb, var(--success) 70%, var(--primary-2));
  --parallax-scene-grass: color-mix(in srgb, var(--success) 62%, var(--surface-light));
  --parallax-scene-grass-near: color-mix(in srgb, var(--success) 80%, var(--surface-light));
  --parallax-scene-leaf-dark: color-mix(in srgb, var(--success) 72%, var(--surface-deep));
  --parallax-scene-leaf: color-mix(in srgb, var(--success) 90%, var(--primary-2));
  --parallax-scene-leaf-lit: color-mix(in srgb, var(--success) 66%, color-mix(in srgb, var(--accent) 45%, var(--surface-light)));
  --parallax-scene-trunk: color-mix(in srgb, var(--warning) 50%, var(--text-main));
  --parallax-scene-asphalt: color-mix(in srgb, var(--text-main) 88%, var(--primary));
  --parallax-scene-sidewalk: color-mix(in srgb, var(--surface-muted) 72%, var(--text-muted));
  --parallax-scene-curb: color-mix(in srgb, var(--surface-muted) 50%, var(--text-muted));
  --parallax-scene-stone: color-mix(in srgb, var(--surface-muted) 55%, var(--text-muted));
  --parallax-scene-chimney: color-mix(in srgb, var(--danger) 42%, var(--text-muted));
  --parallax-scene-iron: color-mix(in srgb, var(--text-main) 92%, var(--primary));
  --parallax-scene-shade: color-mix(in srgb, var(--surface-deep) 16%, transparent);
  --parallax-scene-trim: var(--surface-light);
  --parallax-scene-glass-a: color-mix(in srgb, var(--primary) 34%, var(--surface-light));
  --parallax-scene-glass-b: color-mix(in srgb, var(--primary-2) 14%, var(--surface-light));
  --parallax-scene-warm-a: color-mix(in srgb, var(--accent) 70%, var(--surface-light));
  --parallax-scene-warm-b: color-mix(in srgb, var(--accent) 88%, var(--danger));
  --parallax-scene-sun-drop: 7%;
  --parallax-scene-run: 240vh;
  --parallax-scene-settle: clamp(0, var(--parallax-scene-p, 1) / 0.8, 1);
  --parallax-scene-dt: clamp(0, (var(--parallax-scene-p, 1) - 0.05) / 0.65, 1);
  --parallax-scene-day: calc(var(--parallax-scene-dt) * var(--parallax-scene-dt) * (3 - 2 * var(--parallax-scene-dt)));
  --parallax-scene-rt: clamp(0, var(--parallax-scene-p, 1) / 0.75, 1);
  --parallax-scene-rise: calc(1 - (1 - var(--parallax-scene-rt)) * (1 - var(--parallax-scene-rt)));
  position: relative; background: var(--parallax-scene-grass-near); color: var(--text-inverse); font-family: var(--font-sans);
}

/* Stage and sky: day gradient underneath, dawn gradient fading out on top */
.parallax-scene__stage { position: sticky; top: 0; height: 100vh; height: 100svh; overflow: hidden; isolation: isolate; }
.parallax-scene__sky, .parallax-scene__sky::before, .parallax-scene__stars, .parallax-scene__scrim, .parallax-scene__land { position: absolute; inset: 0; pointer-events: none; }
.parallax-scene__sky {
  background: linear-gradient(180deg, var(--parallax-scene-sky-day-1), var(--parallax-scene-sky-day-2) 50%, var(--parallax-scene-sky-day-3) 70%, var(--parallax-scene-sky-day-4) 90%);
}
.parallax-scene__sky::before {
  content: ""; opacity: calc(1 - var(--parallax-scene-day));
  background: linear-gradient(180deg, var(--parallax-scene-sky-dawn-1), var(--parallax-scene-sky-dawn-2) 38%, var(--parallax-scene-sky-dawn-3) 58%, var(--parallax-scene-sky-dawn-4) 72%);
}
.parallax-scene__stars {
  bottom: 45%; opacity: clamp(0, 1 - var(--parallax-scene-p, 1) / 0.32, 1);
  background-image:
    radial-gradient(1.5px 1.5px at 8% 14%, var(--text-inverse) 60%, transparent),
    radial-gradient(1px 1px at 17% 38%, var(--text-inverse) 60%, transparent),
    radial-gradient(1.5px 1.5px at 29% 9%, var(--text-inverse) 60%, transparent),
    radial-gradient(1px 1px at 41% 27%, var(--text-inverse) 60%, transparent),
    radial-gradient(1px 1px at 52% 6%, var(--text-inverse) 60%, transparent),
    radial-gradient(1.5px 1.5px at 63% 22%, var(--text-inverse) 60%, transparent),
    radial-gradient(1px 1px at 71% 44%, var(--text-inverse) 60%, transparent),
    radial-gradient(1.5px 1.5px at 79% 12%, var(--text-inverse) 60%, transparent),
    radial-gradient(1px 1px at 88% 31%, var(--text-inverse) 60%, transparent),
    radial-gradient(1px 1px at 94% 8%, var(--text-inverse) 60%, transparent);
}
.parallax-scene__scrim {
  background: linear-gradient(180deg, color-mix(in srgb, var(--surface-deep) 24%, transparent), color-mix(in srgb, var(--surface-deep) 8%, transparent) 40%, transparent 56%);
}

/* Layers: full-stage SVGs cropped with slice; each sinks by its depth and settles into place */
.parallax-scene__layer {
  position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; will-change: translate;
  translate: 0 calc((1 - var(--parallax-scene-settle)) * var(--parallax-scene-depth, 0) * 100%);
}
.parallax-scene__layer--sun { translate: 0 calc((1 - var(--parallax-scene-rise)) * 44% + var(--parallax-scene-sun-drop)); }
.parallax-scene__layer--clouds { translate: calc(var(--parallax-scene-p, 1) * -4%) calc((1 - var(--parallax-scene-settle)) * 6%); }
.parallax-scene__layer--far { --parallax-scene-depth: 0.08; }
.parallax-scene__layer--near { --parallax-scene-depth: 0.14; }
.parallax-scene__layer--houses, .parallax-scene__layer--lights { --parallax-scene-depth: 0.22; }
.parallax-scene__layer--road { --parallax-scene-depth: 0.3; }
.parallax-scene__layer--front { --parallax-scene-depth: 0.44; }
.parallax-scene__land { filter: brightness(calc(0.5 + 0.5 * var(--parallax-scene-day))) saturate(calc(0.72 + 0.28 * var(--parallax-scene-day))); }
.parallax-scene__defs { position: absolute; width: 0; height: 0; overflow: hidden; }
.parallax-scene__minor { display: none; }

/* Sun and clouds */
.parallax-scene__sun-halo { fill: url(#parallax-scene-sun-fill); }
.parallax-scene__sun-dawn { fill: color-mix(in srgb, var(--accent) 72%, var(--danger)); }
.parallax-scene__sun-day { fill: color-mix(in srgb, var(--accent) 30%, var(--surface-light)); opacity: var(--parallax-scene-day); }
.parallax-scene__cloud { fill: var(--surface-light); opacity: calc(0.35 + 0.55 * var(--parallax-scene-day)); }

/* Landscape paints */
.parallax-scene__hill-far { fill: var(--parallax-scene-hill-far); }
.parallax-scene__hill-far-2 { fill: var(--parallax-scene-hill-far-2); }
.parallax-scene__hill-near { fill: var(--parallax-scene-hill-near); }
.parallax-scene__hill-tree { fill: var(--parallax-scene-hill-tree); }
.parallax-scene__grass { fill: var(--parallax-scene-grass); }
.parallax-scene__grass-near { fill: var(--parallax-scene-grass-near); }
.parallax-scene__leaf-dark { fill: var(--parallax-scene-leaf-dark); }
.parallax-scene__leaf { fill: var(--parallax-scene-leaf); }
.parallax-scene__leaf-lit { fill: var(--parallax-scene-leaf-lit); }
.parallax-scene__trunk { fill: var(--parallax-scene-trunk); }

/* Houses: each house group sets --parallax-scene-wall / -roof / -door (and -trim, -wood) inline */
.parallax-scene__wall { fill: var(--parallax-scene-wall); }
.parallax-scene__roof { fill: var(--parallax-scene-roof); }
.parallax-scene__fascia { fill: none; stroke: var(--parallax-scene-trim); stroke-width: 5; stroke-linejoin: round; stroke-linecap: round; }
.parallax-scene__trim { fill: var(--parallax-scene-trim); }
.parallax-scene__glass { fill: url(#parallax-scene-glass-fill); }
.parallax-scene__glint { fill: color-mix(in srgb, var(--surface-light) 45%, transparent); }
.parallax-scene__shade { fill: var(--parallax-scene-shade); }
.parallax-scene__siding { fill: url(#parallax-scene-siding); }
.parallax-scene__slats { fill: url(#parallax-scene-slats); }
.parallax-scene__wood { fill: var(--parallax-scene-wood); }
.parallax-scene__stone, .parallax-scene__drive { fill: var(--parallax-scene-stone); }
.parallax-scene__chimney { fill: var(--parallax-scene-chimney); }
.parallax-scene__chimney-cap { fill: color-mix(in srgb, var(--parallax-scene-chimney) 70%, var(--surface-deep)); }
.parallax-scene__paint { fill: var(--parallax-scene-door); }
.parallax-scene__panel { fill: color-mix(in srgb, var(--parallax-scene-door) 82%, var(--surface-deep)); }
.parallax-scene__knob { fill: var(--accent); }
.parallax-scene__groove { fill: none; stroke: var(--parallax-scene-shade); stroke-width: 2; }
.parallax-scene__iron { fill: var(--parallax-scene-iron); }
.parallax-scene__lantern { fill: var(--parallax-scene-glass-b); }
.parallax-scene__mailbox { fill: var(--primary); }
.parallax-scene__stop-glass-a { stop-color: var(--parallax-scene-glass-a); }
.parallax-scene__stop-glass-b { stop-color: var(--parallax-scene-glass-b); }

/* Street and fence */
.parallax-scene__sidewalk { fill: var(--parallax-scene-sidewalk); }
.parallax-scene__apron { fill: color-mix(in srgb, var(--parallax-scene-sidewalk) 60%, var(--surface-light)); }
.parallax-scene__joints { fill: none; stroke: var(--parallax-scene-shade); stroke-width: 22; stroke-dasharray: 1.5 78.5; }
.parallax-scene__curb { fill: var(--parallax-scene-curb); }
.parallax-scene__asphalt { fill: var(--parallax-scene-asphalt); }
.parallax-scene__gutter { fill: none; stroke: color-mix(in srgb, var(--surface-deep) 30%, transparent); stroke-width: 6; }
.parallax-scene__lane { fill: none; stroke: color-mix(in srgb, var(--accent) 70%, var(--surface-light)); stroke-width: 4; stroke-dasharray: 48 36; }
.parallax-scene__fence { fill: url(#parallax-scene-pickets); }
.parallax-scene__picket { fill: var(--surface-light); }
.parallax-scene__rail { fill: color-mix(in srgb, var(--surface-light) 86%, var(--text-muted)); }

/* Lit windows and lamps: each switches off at its own --parallax-scene-at */
.parallax-scene__lit {
  opacity: clamp(0, (var(--parallax-scene-at, 0) - var(--parallax-scene-p, 1)) * 1000, 1);
  transition: opacity var(--dur-3) var(--ease-out);
}
.parallax-scene__halo { fill: url(#parallax-scene-halo-fill); }
.parallax-scene__warm { fill: url(#parallax-scene-warm-fill); }
.parallax-scene__mullion { fill: color-mix(in srgb, var(--warning) 60%, var(--surface-deep)); }
.parallax-scene__stop-warm-a { stop-color: var(--parallax-scene-warm-a); }
.parallax-scene__stop-warm-b { stop-color: var(--parallax-scene-warm-b); }
.parallax-scene__stop-halo, .parallax-scene__stop-sun { stop-color: var(--accent); stop-opacity: 0.5; }
.parallax-scene__stop-halo-clear, .parallax-scene__stop-sun-clear { stop-color: var(--accent); stop-opacity: 0; }

/* The van: eased drive, wheel spin matched to distance, a brake dip as it stops */
.parallax-scene__van {
  --parallax-scene-drive: clamp(0, (var(--parallax-scene-p, 1) - 0.42) / 0.5, 1);
  --parallax-scene-ease: calc(1 - (1 - var(--parallax-scene-drive)) * (1 - var(--parallax-scene-drive)) * (1 - var(--parallax-scene-drive)));
  translate: calc((var(--parallax-scene-ease) - 1) * 1400px) 0;
}
.parallax-scene__van-body { transform-origin: 1300px 926px; rotate: calc(sin(clamp(0, (var(--parallax-scene-drive) - 0.86) / 0.14, 1) * 180deg) * 1.4deg); }
.parallax-scene__wheel { transform-box: fill-box; transform-origin: center; rotate: calc(var(--parallax-scene-ease) * 3342deg); }
.parallax-scene__van-shadow { fill: color-mix(in srgb, var(--surface-deep) 30%, transparent); }
.parallax-scene__van-paint { fill: var(--surface-light); }
.parallax-scene__van-skirt, .parallax-scene__rim { fill: color-mix(in srgb, var(--surface-muted) 55%, var(--text-muted)); }
.parallax-scene__van-stripe, .parallax-scene__van-badge { fill: url(#parallax-scene-brand-fill); }
.parallax-scene__stop-brand-a { stop-color: var(--primary); }
.parallax-scene__stop-brand-b { stop-color: var(--primary-2); }
.parallax-scene__van-glass { fill: color-mix(in srgb, var(--text-main) 88%, var(--primary)); }
.parallax-scene__van-seam { fill: none; stroke: var(--parallax-scene-shade); stroke-width: 2; }
.parallax-scene__van-trim, .parallax-scene__van-bumper, .parallax-scene__van-arch, .parallax-scene__tire, .parallax-scene__hub { fill: var(--parallax-scene-iron); }
.parallax-scene__van-light { fill: color-mix(in srgb, var(--accent) 40%, var(--surface-light)); }
.parallax-scene__van-tail { fill: var(--danger); }
.parallax-scene__van-glyph { fill: var(--surface-light); }
.parallax-scene__van-word { fill: var(--primary); font: 700 28px var(--font-display); letter-spacing: -0.03em; }
.parallax-scene__van-tag { fill: var(--text-muted); font: 500 9px var(--font-mono); letter-spacing: 0.2em; }
.parallax-scene__van-tel { fill: var(--text-main); font: 500 12px var(--font-mono); }
.parallax-scene__rack, .parallax-scene__spokes { fill: none; stroke: var(--parallax-scene-iron); stroke-width: 3; stroke-linecap: round; }

/* "On site" bubble pops once the van has parked */
.parallax-scene__bubble {
  --parallax-scene-on: clamp(0, (var(--parallax-scene-p, 1) - 0.94) * 1000, 1);
  opacity: var(--parallax-scene-on); scale: calc(0.6 + 0.4 * var(--parallax-scene-on)); transform-origin: 1302px 748px;
  transition: opacity var(--dur-2) var(--ease-out), scale var(--dur-4) var(--ease-spring);
}
.parallax-scene__bubble-bg { fill: var(--surface-light); stroke: var(--parallax-scene-shade); stroke-width: 2; }
.parallax-scene__bubble-dot { fill: var(--success); }
.parallax-scene__bubble-text { fill: var(--text-main); font: 600 15px var(--font-sans); }

/* Copy in the sky */
.parallax-scene__inner { position: relative; max-width: var(--container-max); margin-inline: auto; padding: clamp(1.25rem, 6vh, 3.5rem) var(--gutter) 0; }
.parallax-scene__copy { max-width: 40rem; text-shadow: 0 1px 24px color-mix(in srgb, var(--surface-deep) 30%, transparent); }
.parallax-scene__time {
  display: inline-flex; align-items: center; gap: 0.5rem; margin: 0; padding: 0.375rem 0.75rem 0.375rem 0.5rem; border-radius: var(--radius-full);
  background: color-mix(in srgb, var(--surface-deep) 24%, transparent); box-shadow: inset 0 0 0 1px var(--border-inverse), var(--highlight-inverse);
  font: 500 0.75rem/1 var(--font-mono); letter-spacing: 0.06em; font-variant-numeric: tabular-nums; text-shadow: none;
}
.parallax-scene__time svg { fill: none; stroke: var(--accent); stroke-width: 2; stroke-linecap: round; }
.parallax-scene__title {
  margin: 0.875rem 0 0; font: 600 clamp(2rem, 1.2rem + 3.4vw, 3.75rem)/1.02 var(--font-display);
  letter-spacing: var(--tracking-display); text-wrap: balance;
}
.parallax-scene__lead { max-width: 32rem; margin: 0.75rem 0 0; font-size: clamp(0.9375rem, 0.9rem + 0.3vw, 1.125rem); line-height: 1.5; }
.parallax-scene__actions { display: flex; flex-wrap: wrap; align-items: center; gap: 0.5rem 1.25rem; margin-top: 1.25rem; }
.parallax-scene__btn {
  display: inline-flex; align-items: center; gap: 0.5rem; height: 2.75rem; padding: 0 1.25rem; border-radius: var(--radius-full);
  background: var(--surface-light); color: var(--text-main); font: 600 0.9375rem var(--font-sans); text-decoration: none; text-shadow: none;
  box-shadow: var(--highlight), 0 14px 32px -14px color-mix(in srgb, var(--surface-deep) 80%, transparent);
  transition: transform var(--dur-3) var(--ease-spring), box-shadow var(--dur-3) var(--ease-out);
}
.parallax-scene__btn svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; transition: translate var(--dur-3) var(--ease-spring); }
.parallax-scene__btn:hover { transform: translateY(-2px); }
.parallax-scene__btn:hover svg { translate: 3px 0; }
.parallax-scene__btn:active { transform: scale(0.97); }
.parallax-scene__rating { display: none; margin: 0; font: 500 0.8125rem var(--font-mono); }
.parallax-scene :is(a, button):focus-visible { outline: 2px solid var(--text-inverse); outline-offset: 3px; }

@media (min-width: 768px) {
  .parallax-scene { --parallax-scene-sun-drop: 0%; }
  .parallax-scene__minor { display: inline; }
}
@media (min-width: 1024px) {
  .parallax-scene { --parallax-scene-run: 280vh; }
}
@media (min-height: 640px) {
  .parallax-scene__rating { display: block; }
}

/* The long scroll only exists when the script drives it and motion is allowed */
@media (prefers-reduced-motion: no-preference) {
  .parallax-scene.is-live { height: var(--parallax-scene-run); }
}
@media (scripting: enabled) and (prefers-reduced-motion: no-preference) {
  .parallax-scene { height: var(--parallax-scene-run); }
  .parallax-scene:not(.is-live) { animation: parallax-scene-failsafe 1.8s var(--ease-in-out) 2.5s both; }
}
@keyframes parallax-scene-failsafe { from { --parallax-scene-p: 0; } to { --parallax-scene-p: 1; } }

/* Demo scroll room */
.parallax-scene-demo__intro, .parallax-scene-demo__outro {
  display: grid; place-content: center; justify-items: center; gap: 0.75rem; min-height: 70vh; padding: 3rem var(--gutter);
  font-family: var(--font-sans); text-align: center;
}
.parallax-scene-demo__intro { background: linear-gradient(var(--surface-deep), color-mix(in srgb, var(--primary) 20%, var(--surface-deep))); color: var(--text-inverse); }
.parallax-scene-demo__outro { background: var(--surface-light); color: var(--text-main); }
.parallax-scene-demo__kicker { margin: 0; font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; opacity: 0.8; }
.parallax-scene-demo__line { max-width: 22ch; margin: 0; font: 600 clamp(1.5rem, 1.1rem + 2vw, 2.5rem)/1.1 var(--font-display); letter-spacing: var(--tracking-tight); text-wrap: balance; }
.parallax-scene-demo__hint { display: inline-flex; align-items: center; gap: 0.375rem; margin-top: 1rem; font: 500 0.75rem var(--font-mono); letter-spacing: 0.14em; text-transform: uppercase; color: var(--text-inverse-muted); }
.parallax-scene-demo__hint svg { fill: none; stroke: currentColor; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; animation: parallax-scene-nudge 1.6s var(--ease-in-out) 3; }
@keyframes parallax-scene-nudge { 50% { translate: 0 4px; } }

@media (prefers-reduced-motion: reduce) {
  .parallax-scene-demo *, .parallax-scene-demo *::before, .parallax-scene-demo *::after { animation: none !important; }
}
```

## JS

```js
const clamp01 = (n) => Math.min(1, Math.max(0, n));
const progress = (el) => { const r = el.getBoundingClientRect(); const range = r.height - innerHeight; return range > 0 ? clamp01(-r.top / range) : 0; };
const reduce = matchMedia('(prefers-reduced-motion: reduce)');

document.querySelectorAll('[data-parallax-scene]').forEach((root) => {
  const clock = root.querySelector('[data-parallax-scene-clock]');
  let near = false;
  let frame = 0;
  let shown = '';

  // One write per frame: CSS derives every layer, colour, light and the van from --parallax-scene-p
  const render = () => {
    frame = 0;
    const still = reduce.matches;
    root.classList.toggle('is-live', !still); // tall scroll on, CSS failsafe off
    const p = still ? 1 : progress(root);
    if (still) root.style.removeProperty('--parallax-scene-p');
    else root.style.setProperty('--parallax-scene-p', p.toFixed(4));
    // The clock runs from 5:48 AM to 8:00 AM, when the van parks
    const minutes = Math.round(348 + 132 * p);
    const label = `${Math.floor(minutes / 60)}:${String(minutes % 60).padStart(2, '0')} AM`;
    if (label !== shown) { shown = label; clock.textContent = label; }
  };
  const queue = () => { if (near && !frame) frame = requestAnimationFrame(render); };

  new IntersectionObserver(([entry]) => { near = entry.isIntersecting; queue(); }, { rootMargin: '25% 0px' }).observe(root);
  addEventListener('scroll', queue, { passive: true });
  addEventListener('resize', queue, { passive: true });
  reduce.addEventListener('change', render);
  render();
});
```

## Notes

- The illustration is entirely `aria-hidden`; the heading, line, link and rating are real text in the sky. The clock and the "On site" bubble are decoration (screen readers don't hear the time change).
- Without JS, or with reduced motion, `--parallax-scene-p` keeps its registered initial value of 1, so you get a normal-height section with the static midday scene: van parked, lights off, bubble shown. The long pinned scroll only exists when the script runs (`.is-live`); with scripting on, a CSS failsafe holds the dawn start (no flash) and plays the morning through if the script never arrives.
- Contrast: the copy stays in the upper half of the sky. At worst (full day, just above mid-height), `--text-inverse` on `--primary` is 4.9:1, plus a top scrim. Dawn is 9:1 or more, and the crossfade never drops below 6.3:1. Keep the copy above the hills if you change the scene.
- Performance: each layer is a full-stage SVG moved only with `translate` (`will-change`). The dawn darkening is one CSS filter on the land group, and window glows sit in a separate unfiltered layer that moves with the houses. Lights are timed to switch off before the van passes in front of them.
- Uses `@property`, `color-mix()`, individual transforms on SVG and CSS `sin()` for the brake dip, which is simply skipped where `sin()` is unsupported. To retheme, edit the palette on `.parallax-scene`; each house takes `--parallax-scene-wall/-roof/-door` inline. The ids are prefixed, so use one scene per page or suffix them.
