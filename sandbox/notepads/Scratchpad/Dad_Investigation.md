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
- **Hypothesis S1 (Sewers Storage Room & Grunt Retreat Site Re-Audit)**:
  - **Context**: Grunts vacated after Marie's radio order (Turn 2682), but Jackson was never located. The Eastern Storage Room at (37, 14) displayed 'Its a simple storage room...'.
  - **Targets**: Eastern Storage Room at (37, 14), red mat tile behavior, and adjacent canal perimeters.
  - **Method**: Return to Sovio Sewers via Metro lobby mat (18-19, 25), navigate to (37, 14), systematically probe all adjacent tiles and mat entry orientations.
  - **Falsification Criteria**: If (37, 14) and surrounding perimeter remain strictly inert with no entry or dialogue, rule out Eastern Storage Room as an accessible holding cell.
