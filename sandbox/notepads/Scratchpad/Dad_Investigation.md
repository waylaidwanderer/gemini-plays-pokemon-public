# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher 1 step south to (19, 22). Attendant at (22, 18-19) is unreachable behind solid wall/turnstile structure.
- **Rugged Rocks (Sewers)**: (22, 10) and (10, 18) display "It's a rugged rock, but with some equipment, I could smash it." Field obstacle clearance requires specialized player equipment rather than traditional HM moves. Zero equipment currently in possession.

## Settled Inquiries
- **Sovio Metro Turnstile & Sewer Storage Room (H25)**: Turnstile (19, 21) remains blocked by "I should find dad first!". Sewer storage room mat (37, 14) confirmed walkable but south transition is impassable/inactive ("Its a simple storage room...").
- **Route 1 & Lancio Town Audit (H24)**: Traversal verified devoid of active triggers for Jackson.
- **Route 1 Column 52 Hedge**: Probed (52, 13); solid collision at rows 14-16.

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
  - **Milestone 1 (Ascend to Metro Station Lobby)**: COMPLETED (Turn 17232). Arrived at (23, 24) on exit mat via autonomous subagent sewer_transit.
  - **Milestone 2 (Audit Metro Lobby Accessible Perimeter)**: COMPLETED (Turn 17232). Verified entire accessible lobby from (23, 24): zero NPCs present, turnstile still prompts "I should find dad first!", Valora is absent.
  - **Milestone 3 (Audit Sovio City Central Plaza & Elevated Terrace)**: COMPLETED (Turn 17240). Elevated terrace (cols 47-51, rows 14-17) audited: zero NPCs present. Nana's house at (49, 14) audited: granddaughter and Nana both confirmed 100% ambient flavor dialogue.
  - **Milestone 4 (Audit Pokémon Center 1F & 2F Mezzanine)**: COMPLETED 1F (Turn 17248-17253). Camper and Boy confirmed ambient; mezzanine bypassed.
  - **Milestone 5 (Audit Sovio City Residential Row & Route 2 Border)**: ACTIVE. Route 2 barrier at (52, 20) confirmed blocked ("I can't go yet..."). Auditing Karate House at (14, 15), then Gumball (29, 14), Wii (39, 7), and Name Rater (31, 26).
