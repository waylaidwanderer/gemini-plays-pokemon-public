# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Scanner pillars (18, 21) and (20, 21) verified 100% inert; platform chairs verified empty per Turn 20098; north wall across columns 21-23 is solid brick with timetable board mounted.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- H60-H94 (Baseline Sweeps & Local Trigger Invalidation - Turns 7232-20521): FALSIFIED. Comprehensive audits across Sovio City, the Metro Station, and Sovio Sewers confirmed that all civilian residences (Wii house 39, 7; Gumball house 29, 14; Karate house 14, 15; Terrace house 49, 14; Name Rater 31, 26), Central Plaza confrontation ground tiles (cols 41-46, rows 13-15), in-game Start Menu RTC schedule correlation, Metro lobby fixtures/turnstiles, and post-retreat sewer platforms/storage rooms are 100% static with zero hidden progression triggers. Jackson was never verified held in the sewers, and local Sovio/sewer options are completely exhausted.
- **Route 1 Cut Tree (Turn 20616-20622)**: Performed stationary, unchained 'A' interaction facing North from (5, 45) into the Cut tree at (5, 44). Confirmed ZERO textbox or dialogue prompt appears when Cut is unlearned; acts as a silent solid tile obstacle.
- **H95: Lancio Town Regional & Facility Audit (Turns 20616-20723)**: FALSIFIED. Comprehensive empirical audit across Lancio Town confirmed:
  - Cap boy at (32, 14): Static ambient text ("Living in a small town sucks... There's nothing to do. I wanna live in the big capital, Amor City!").
  - Professor Ivo's Lab (20, 6): Static ambient text ("Hey, Ashi, how's your new Pokémon?").
  - Lab Basement Stairs (12, 7): Static barrier active ("I probably shouldn't head down here...").
  - TM17 house (25, 10): Static behavior (boy displays "Get out!" and kicks Asher outside).
  - Old Couple at (32-33, 8): Static ambient text (Old Man: "I have grown up in this place, and I never want to leave it..."; Old Woman: "With my husband we have been living here for over 30 years...").
  - Lancio Harbor pier (32-34, 23-25): Pier is completely empty, Harry is absent, no boat is moored, zero maritime triggers exist.
  - Fisherman at (38, 22): Ambient fishing advice.
  Concluded: Zero external story triggers or side quest leads exist in Lancio Town. The progression blocker ("I should find dad first!") is strictly rooted in Sovio City.

## Active Hypotheses for Progression
### Hypothesis H96: Tremor Environmental Consequences & Multi-Angle Structural Audit in Sovio City
- **Premise**: When the sudden seismic tremor shook the Sovio Metro Station, Dad immediately ran outside into Sovio City to investigate the source of the tremor. Main story progression ("I should find dad first!") is gated by locating Dad or triggering an event tied to the tremor's environmental consequences. Features previously dismissed as "decorative" (sewer manholes, terrace structures, turnstile scanners, or single-angle interactions) must be systematically audited with active multi-angle inspections.
- **Targets for Systematic Multi-Angle Testing in Sovio City**:
  1. **Sewer Manholes across Sovio City**:
     - Manhole at (40, 13) in northern alcove outside Wii house / Pokémon Center.
     - Manholes at (54, 19) and (54, 21) near the eastern Route 2 border.
     - Central Park manhole at (42, 27) near the southern bushes.
     - West Avenue manholes at (13, 19) and (13, 27).
     - Terrace manhole at (51, 16) above the Metro portal.
     - *Testing Protocol*: Interact with 'A' from all adjacent cardinal directions (North, South, East, West) and step directly onto each tile.
  2. **Sovio Metro Lobby Structural & Inspection Targets**:
     - Scanner pillars at (18, 21) and (20, 21): Test 'A' interactions from South, East, and West.
     - North wall timetable board (21-23, 23): Retest each column.
     - Platform edge and station attendant interaction.
  3. **Central Plaza Confrontation Ground**:
     - Re-audit the exact tiles where Mother, Grunts, and altered Pidgey stood outside the Pokémon Center.
- **Falsifiable Success Criteria**: Triggering a new inspection dialogue, opening an underground passage/manhole, finding Jackson, or lifting the turnstile script ("I should find dad first!").
