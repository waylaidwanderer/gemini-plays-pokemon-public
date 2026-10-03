# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher south to (19, 22). Scanner pillars (18, 21) and (20, 21) verified 100% inert; platform chairs verified empty per Turn 20098; north wall across columns 21-23 is solid brick with timetable board mounted.
- **Rugged Rocks (Sovio Sewers)**: Obstacles at (22, 10) in Dark Sector and (10, 18) / (9, 17) in southwest corridor require specialized equipment.
- **Storage Room (37, 14)**: Verified single static inspection trigger ("Its a simple storage room..") with solid collision at (37, 15); platform fully audited.

## Concluded Hypotheses
- H60-H94 (Baseline Sweeps & Local Trigger Invalidation - Turns 7232-20521): FALSIFIED. Comprehensive audits across Sovio City, the Metro Station, and Sovio Sewers confirmed that all civilian residences (Wii house 39, 7; Gumball house 29, 14; Karate house 14, 15; Terrace house 49, 14; Name Rater 31, 26), Central Plaza confrontation ground tiles (cols 41-46, rows 13-15), in-game Start Menu RTC schedule correlation, Metro lobby fixtures/turnstiles, and post-retreat sewer platforms/storage rooms are 100% static with zero hidden progression triggers. Jackson was never verified held in the sewers, and local Sovio/sewer options are completely exhausted.
- **Route 1 Cut Tree (Turn 20616-20622)**: Performed stationary, unchained 'A' interaction facing North from (5, 45) into the Cut tree at (5, 44). Confirmed ZERO textbox or dialogue prompt appears when Cut is unlearned; acts as a silent solid tile obstacle.

## Active Hypotheses for Progression
### Hypothesis H95: Lancio Town Story & Side Quest Audit
- **Premise**: With Sovio Metro blocked by "I should find dad first!" and Route 2 blocked by "I can't go yet... I have things to do!", audit Lancio Town to test if external triggers, updated dialogues, or uncompleted side quests (Medic!, Egg Research, Squirtle Gang) unlock progression.
- **Specific Falsifiable Tests & Expected Baselines**:
  1. **Cap NPC at (32, 14)**:
     - Baseline: "Living in a small town sucks... There's nothing to do. I wanna live in the big capital, Amor City!"
     - Result (Turn 20675-20676): FALSIFIED. Textbox verbatim displayed baseline ("Living in a small town sucks... There's nothing to do. I wanna live in the big capital, Amor City!"). Confirmed 100% static ambient flavor with zero quest or story triggers.
  2. **Professor Ivo's Pokémon Laboratory**:
     - Professor Ivo at (20, 6): Baseline is "Hey, Ashi, how's your new Pokémon?".
       - Result (Turn 20683-20684): FALSIFIED. Textbox verbatim displayed baseline ("Hey, Ashi, how's your new Pokémon?"). Zero updated story dialogue regarding Dad, the tremor, or Team Siara. Confirmed 100% static ambient flavor.
     - Lab Basement Stairs at (12, 7): Baseline is "I probably shouldn't head down here...".
       - Result (Turn 20685-20686): FALSIFIED. Stepping onto (12, 7) triggers verbatim baseline ("I probably shouldn't head down here..."). Confirmed barrier is 100% active and static.
  3. **Lancio Harbor & Dock (32-34, 23-25)**:
     - Baseline: Pier empty, Harry/boat absent.
     - Test: Verify if Harry, a vessel, or new maritime trigger is present.
     - Fisherman at (38, 22): Baseline is ambient fishing advice. Test if quest or story trigger is offered.
  4. **Town Residents**:
     - TM17 House at (25, 10):
       - Result (Turn 20706-20707): FALSIFIED. Textbox verbatim displayed baseline ("Get out!") and kicks Asher outside. Confirmed 100% static behavior.
     - Old Couple at (32-33, 8):
       - Old Man at (32, 8): Result (Turn 20715-20716): FALSIFIED. Textbox verbatim displayed baseline ("I have grown up in this place, and I never want to leave it... This is home for me."). Confirmed static ambient flavor.
       - Old Woman at (33, 8): Baseline is 30-year residency / Sinnoh flavor. Test for tremor or side quest leads.
- **Decision Rule**: Execute tests 1 through 4 sequentially. If all baseline conditions repeat with zero updates, conclude and archive Hypothesis H95 as FALSIFIED before moving to any new geographic region.
