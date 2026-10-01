# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Blockers & Status
- **Metro Turnstile**: Stepping onto (19, 21) triggers "I should find dad first!".
- **Route 2 Gate**: Stepping onto (52, 19) triggers "I can't go yet... I have things to do!".
- **Jackson Status**: Captured by Team Siara in sewers (Turn 1666-1707 cutscene). Jackson has remained missing, which is why turnstiles and Route 2 remain locked.

## Verified / Settled Locations
- **Lancio Town**: Professor Ivo's dialogue static ambient (Turns 7625, 13511), lab basement stairs blocked ("I probably shouldn't head down here..."), harbor boat empty/discontinued.
- **Route 1**: All trainers defeated; cottage boy gives Max Repel; open hedge passage connects column 30 to Northwest Clearing.
- **Sovio Surface**: Plaza confrontation tiles (43-44, 13-15), timetable (22, 24), and Central Park pond walkway (43-45, 23-26) return baseline ambient interactions.
- **Sovio Metro Lobby (Audited Turn 14177)**: Turnstile at (19, 21) strictly triggers 'I should find dad first!' forcing player to (19, 22); platform attendant at (22, 19) is inaccessible behind brick wall.
- **Sovio Route 2 Boundary (Audited Turn 14189)**: Barrier at (52, 19-22) strictly triggers 'I can't go yet... I have things to do!' forcing player back.
- **Sovio Buildings Audited This Cycle**:
  - SC1 (Pokémon Center 44, 12): Camper at (5, 7) Weedle text; Boy at (9, 6) PC text.
  - SC2 (North-Central House 39, 7): Elderly man repeats Wii text.
  - SC3 (Terrace House 49, 14): Granddaughter at (63, 34) non-interactive; Nana at (62, 31) repeats cooking text ('I\'m cooking something for my dear grandkid. She loves my cooking.'); Old Man and Machop absent from terrace (audited Turn 14196-14203). Terrace Complex 100% settled/ambient.
  - SC5 (Machop Family House 14, 15): Karate couple debate static; Machop flavor text permanently 'He seems a bit agressive...' regardless of quest status (re-verified Turn 14148).
- **Machop's Toy Quest**: Completed Turn 13331 (Black Belt obtained).
- **Deep Subterranean Sector (Sovio Sewers)**: Audited Turn 14052. 3x3 chamber (2, 38) perimeter walls probed inert; single-purpose quest room where Machop's toy was retrieved.

## Active Hypotheses & Primary Focus
- **Hypothesis SC4 (Gumball Residence SC4 Audit - Priority Lead)**:
  - **Context**: SC4 (29, 14) was approached on Turn 14160 but abandoned at (28, 16) without entering. It is the sole uninspected residential interior in Sovio City this cycle, as identified by the critique and narrative_analyst agent.
  - **Targets**: SC4 interior at (29, 14): 1F Mother at (27, 33), Boy at (25, 32), TV, and 2F bedroom resident at (27, 15-16).
  - **Method**: Ascend from sewers to surface, traverse West Avenue to (29, 14), enter SC4, test all NPCs and fixtures for Dad clues or story progression triggers.
  - **Falsification Criteria**: If all SC4 occupants repeat baseline flavor dialogue and no story flags/events update, declare SC4 100% settled/ambient.
