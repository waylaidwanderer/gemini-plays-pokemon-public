# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Scanner pillars (18, 21) and (20, 21) verified 100% inert; platform chairs verified empty per Turn 20098; north wall across columns 21-23 is solid brick with timetable board mounted.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- H60-H94 (Baseline Sweeps & Local Trigger Invalidation - Turns 7232-20521): FALSIFIED. Comprehensive audits across Sovio City, the Metro Station, and Sovio Sewers confirmed that all civilian residences (Wii house 39, 7; Gumball house 29, 14; Karate house 14, 15; Terrace house 49, 14; Name Rater 31, 26), Central Plaza confrontation ground tiles (cols 41-46, rows 13-15), in-game Start Menu RTC schedule correlation, Metro lobby fixtures/turnstiles, and post-retreat sewer platforms/storage rooms are 100% static with zero hidden progression triggers. Jackson was never verified held in the sewers, and local Sovio/sewer options are completely exhausted.

## Active Hypotheses for Progression
### Hypothesis H95: Regional Investigation of External Triggers & Route 1 Obstacles
- **Empirical Test - Route 1 Cut Tree (Turn 20616-20622)**: Performed stationary, unchained 'A' interaction facing North from (5, 45) into the Cut tree at (5, 44). Confirmed ZERO textbox or dialogue prompt appears when Cut is unlearned; the tree acts as an inert solid tile obstacle blocking the path north into the forest.
- **Evaluation of Lancio Town & Macro-Oscillation**:
  - Critique analysis: Professor Ivo's post-Siara dialogue ("Hey, Ashi, how's your new Pokémon?") and lab basement barrier ("I probably shouldn't head down here...") were documented static, and no causal inventory item, story flag, or quest milestone has changed since Turn 243. Trekking to Lancio Town without a new game state variable repeats past macro-oscillation.
- **Next Direction & Root Cause Analysis**:
  - The core progression block is the Metro Station turnstile: "I should find dad first!".
  - When the tremor occurred at the Metro Station, Dad ran outside into Sovio City to investigate the source of the tremor.
  - In Sovio Sewers, Team Siara was defeated and Marie called a retreat, but Dad was never found in the sewers.
  - We must methodically investigate Sovio City for Dad's whereabouts or any trigger associated with the tremor.
