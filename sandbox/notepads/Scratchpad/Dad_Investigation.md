# Scratchpad: Investigating Jackson's Whereabouts & Progression Blockers

## Core Verified Blockers
- **Route 2 Barrier (52, 19-22)**: Triggers "I can't go yet... I have things to do!" and blocks eastern exit from Sovio City.
- **Metro Turnstile (19, 21)**: Triggers "I should find dad first!" and forces Asher 1 step south to (19, 22). Attendant at (22, 18-19) is unreachable behind solid wall/turnstile structure.
- **Rugged Rocks (Sewers)**: (22, 10) and (10, 18) display "It's a rugged rock, but with some equipment, I could smash it." Zero equipment currently in possession.
- **Storage Room Mat (Sewers 37, 14)**: Displays "Its a simple storage room..." and has solid void collision to south with zero warp. Closed inquiry: storage room does not contain Jackson and has no active warp.

## Structured Hypotheses

### Hypothesis H1: Covered Passage beneath Roof in South Commercial Block (Sovio City)
- **Premise**: Columns 47-51, rows 20-22 feature a walkable covered corridor beneath a roof graphic connecting row 19 east to column 52. An unprobed door or NPC trigger may exist under this roof.
- **Test Coordinates**: Systematically step across columns 47-51 along rows 20-22 and probe all north-facing and south-facing wall tiles with 'A'.
- **Pass Criteria**: Discovery of an enterable doorway warp, NPC interaction, or item.
- **Fail Criteria**: All tiles under the roof graphic are plain traversable walkway with solid walls and zero interactable scripts.
- **Result (Tested Turn 16147)**: FALSIFIED. Columns 47-51 along rows 20-22 audited tile-by-tile facing North and South; confirmed plain traversable corridor with zero doors, hidden triggers, or items.

### Hypothesis H2: Tan Building Exterior Facade (Sovio City)
- **Premise**: Tan building at columns 32-37, rows 8-12 was only checked at shutters (34-35, 12). A real door may exist at columns 32-33 or 36-37.
- **Test Coordinates**: Probe foundation and wall tiles along row 12 across columns 32, 33, 36, 37 with collision and 'A'.
- **Pass Criteria**: Discovery of an entrance door warp or interaction prompt.
- **Fail Criteria**: All facade tiles return solid wall collision with zero warps or text prompts.
- **Result (Tested Turn 16148)**: FALSIFIED. Columns 32-37 along row 12 audited tile-by-tile; all returned solid wall collision with zero doors or interaction scripts. Tan building is 100% decorative exterior.
