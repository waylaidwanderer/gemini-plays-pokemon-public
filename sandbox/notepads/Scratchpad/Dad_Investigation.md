# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher 1 step south to (19, 22). Attendant at (22, 18-19) is unreachable behind solid wall/turnstile structure.
- **Rugged Rocks (Sewers)**: (22, 10) and (10, 18) display "It's a rugged rock, but with some equipment, I could smash it." Field obstacle clearance requires specialized player equipment rather than traditional HM moves. Zero equipment currently in possession.

## Settled Inquiries
- **Sovio Metro Turnstile & Sewer Storage Room (Hypothesis H25 - Settled)**: In Turn 17175, Metro turnstile (19, 21) confirmed still blocked by "I should find dad first!". In Turn 17204-17207, Eastern Storage Room mat at (37, 14) was rigorously audited: tile (37, 14) is walkable, but stepping Down bumps into impassable boundary at row 15 (no active downward warp), and interacting facing South displays verbatim: "Its a simple storage room..." Storage room appears locked/inactive in the current game state pending a prerequisite event, key, or story trigger.
- **Sovio City Surface Initial Exploration**: All 5 residential buildings, interior residents, and public fixtures (Bikers, Rocky, street lamps, signposts) were checked during early exploration and confirmed ambient. Specific post-retreat event triggers (such as locating Valora or examining the Metro turnstile state after Marie's radio order) remain to be systematically verified.
- **Route 1 Column 52 Hedge**: Probed (52, 13); confirmed solid hedge collision at rows 14-16 with embedded rock spire. Column 52 does not continue south directly.
- **Route 1 & Lancio Town Audit (Hypothesis H24 - Settled: FAILED)**: All 5 milestones completed. Thoroughly audited all accessible surface pathways, residents, and facilities across Route 1 and Lancio Town (excluding HM Cut at (5, 44), water-gated terrain at (38, 4), and locked lab basement stairs at (12, 7)). Progression triggers for locating Jackson are confirmed localized to Sovio City or its subterranean sectors.

## Active Hypotheses for Progression

### Hypothesis H25: Sovio City Metro Station & Unchecked Subterranean Vectors
- **Premise**: With the western region (Route 1, Lancio Town, Inizio Isle) conclusively eliminated, the story progression blocker ("I should find dad first!" at the Metro turnstile and "I can't go yet..." at Route 2) is strictly localized to Sovio City or its subterranean sectors. Macro-traversal oscillation back to Lancio is strictly prohibited.
- **Decomposed Milestones**:
  - **Milestone 1 (Return Transit to Sovio City)**: COMPLETED (Turn 17156). Re-entered Sovio City Southern Avenue at (14, 39).
  - **Milestone 2 (Sovio Metro Station Lobby & Valora Search)**:
    1. Valora Search: Systematically check Sovio City Central Plaza, Pokémon Center, and Metro Station accessible lobby for Valora's presence.
    2. Metro Lobby Accessible Perimeter: Audit all accessible tiles in the Metro lobby before the turnstile (scanner pillars, ticket counter, entrance corners).
    3. Turnstile State: Verify whether the turnstile trigger changes or displays new text once Sovio City exterior is re-checked.
  - **Milestone 3 (Unchecked Sewers Topography & Equipment Sources)**:
    1. Re-examine the cutscene origin: If Jackson was held by grunts in a storage room, verify whether another door or passage exists that was overlooked (e.g. elevated walkways, hidden ladders).
    2. Investigate the "Equipment" mechanic: Determine where specialized rock-smashing equipment is obtained in Sovio City to clear the rugged rocks at (10, 18) and (22, 10).

### Hypothesis H26: Sovio City Surface Systematic Search for Valora & Jackson Triggers
- **Premise**: With the sewer storage room (37, 14) currently inactive and western routes exhausted, the immediate story progression triggers are localized to Sovio City surface (finding Valora, investigating equipment sources for rugged rocks, and locating Jackson). A systematic, tile-by-tile audit of the Metro lobby perimeter, Central Plaza, elevated terrace, Pok�mon Center, and city residences is required to locate Valora and find Jackson's trail.
- **Decomposed Milestones**:
  - **Milestone 1 (Ascend to Metro Station Lobby)**: Return from Sovio Sewers via the (38, 22) staircase to the Metro lobby at (23, 24).
  - **Milestone 2 (Audit Metro Lobby Accessible Perimeter)**: Systematically walk and inspect the eastern waiting area (cols 24-28, rows 21-25) and western seating alcove (cols 15-18).
  - **Milestone 3 (Audit Sovio City Central Plaza & Elevated Terrace)**: Re-examine Central Plaza outside the Pok�mon Center and inspect the elevated terrace at (47-51, 13-17) and Nana's house (49, 14).
  - **Milestone 4 (Audit Pok�mon Center 1F & 2F Mezzanine)**: Inspect every NPC inside the Pok�mon Center for Valora or updated story dialogue.
  - **Milestone 5 (Audit Sovio City Residential Row & Route 2 Border)**: Check all residential homes (Karate, Gumball, Wii, Name Rater) and the Route 2 border structure for updated triggers.