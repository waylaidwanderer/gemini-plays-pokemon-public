# Scratchpad: Post-Tremor Investigation & Progression Hypotheses

## Core Active Progression Barriers
- **Metro Turnstile (19, 21)**: Scripted barrier triggers verbatim "I should find dad first!" and forces Asher south to (19, 22). Gates train platform to Amor City.
- **Route 2 Eastern Exit (52, 19-22)**: Scripted barrier triggers verbatim "I can't go yet... I have things to do!" and forces Asher west.

## Distilled Physical Constraints & Verified Negative Facts
- **Metro Station Lobby**: Timetable, west seating, and scanner pillars are inert. Direct 'A' on turnstile from (19, 22) produces zero dialogue; barrier is strictly a walk-over tripwire on (19, 21).
- **Route 1**: All trainers (Duke, Sonia, Mike) and cottage resident have static pre-tremor dialogue.
- **Sovio City Exterior & Residents**: All residential interiors (Nana/granddaughter, elderly Wii man/son, Gumball family, Karate family/Machop, Name Rater) and outdoor NPCs (Bikers, Boy Rocky, Central Park dating couple, Jigglypuff family, Pokémon Center Camper/Boy) repeat static ambient dialogue.
- **Sovio Sewers**: Grunts retreated following Marie's radio directive; all corridors vacated. Eastern Storage Platform (37, 14) confirmed physically impassable: stepping Down into (37, 15) produces solid collision (0 tiles visited, no warp), and interacting facing South displays verbatim "Its a simple storage room..".
- **Sovio City Central Plaza Perimeter**: Stepped across all exterior plaza tiles (rows 14-16, columns 41-46) where the Siara confrontation occurred; confirmed 100% inert with zero active tripwires or story scripts.
- **Terrace Exterior**: Elevated terrace above Metro portal has no active NPCs or secret passages; manhole at (51, 16) is inert.

## Active Investigation
### Hypothesis H10: Southern Regional Transit & Lancio Post-Tremor Story Audit (Concluded & Falsified - Turn 27081)
- **Premise**: Progression in Sovio City is blocked at the Metro turnstiles ("I should find dad first!") and Route 2 ("I can't go yet... I have things to do!"). Following the sewer grunts' retreat, we audit Lancio Town (Professor Ivo's lab dialogue, lab basement stairs at 12, 7, and harbor dock) and the Route 1 Cut tree to definitively determine whether any unflagged regional trigger was set.
- **Empirical Results (Verified Turn 27062 - 27080)**:
  1. Route 1 Cut tree at (5, 44): Verified solid obstacle with zero interaction (Turn 27062).
  2. Lancio Town harbor dock (32-34, 23-25): Verified empty—Harry absent, no boat moored (Turn 27068).
  3. Professor Ivo's Lab basement stairs at (12, 7): Verified physically blocked verbatim by "I probably shouldn't head down here..." (Turn 27076).
  4. Professor Ivo dialogue at (20, 6): Verified verbatim repeat of static ambient greeting: "Hey, Ashi, how's your new Pokémon?" (Turn 27080).
- **Conclusion**: Hypothesis H10 is conclusively falsified. Lancio Town and Route 1 have zero active story updates, zero unflagged triggers, and are permanently eliminated from the active progression search space.

## Active Investigation: Inventory Audit & Progression Re-evaluation (Started Turn 27081)
- **Objective**: Conduct a complete, rigorous audit of the player's Bag (Items, Key Items, Poké Balls, TMs) and party state to re-evaluate the core assumptions behind the Metro turnstile barrier ("I should find dad first!") and Route 2 barrier ("I can't go yet...").
### Hypothesis H11: Sovio Sewers Storage Platform & Metro Attendant Audit (Active - Started Turn 27093)
- **Premise**: With Lancio Town and Route 1 conclusively eliminated (H10 falsified) and inventory audited, the progression gate to Amor City resides strictly within the Sovio City / Metro / Sewers sector. We return to Sovio City and systematically audit: (1) the Eastern Storage Platform (37, 14) in Sovio Sewers—testing all surrounding wall tiles, mat angles, and potential hidden triggers—and (2) the Metro Station lobby and platform attendant to determine the exact event required to clear the "I should find dad first!" tripwire.
- **Routing Plan**:
  1. Exit Professor Ivo's Lab into Lancio Town.
  2. Traverse east through Lancio Town avenue onto Route 1 cobblestone road (0, 45-46).
  3. Route east through Route 1 (Southern Bypass, Cypress Bypass, Northwest Clearing corridor, meadow) to Sovio City gateway (53, 0).
  4. Enter Sovio Metro Station and descend into Sovio Sewers.