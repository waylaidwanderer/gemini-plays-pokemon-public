# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look.
- Evolve to Haunter (Lv 25) and train to ~Lv 38-40 (Speed 73-110) to outspeed Suicune.
- Track Suicune using Pokedex AREA map. Cycle between adjacent routes (e.g., 36/37) to force encounter.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Ultra Balls.
- Item Goal: Buy Ultra Balls at Goldenrod or Blackthorn Marts.

## Game Mechanics & Lessons
- Type Matchups: Ghost is immune to Normal/Fighting. Lick (Ghost) is ineffective against Normal types.
- Move Effectiveness: Leech Life (Bug) is NVE against Ghost.
- Status Accuracy: Status moves can hit Ghost types. Missing moves display "It didn't affect".
- Switching: Resets confusion and stat changes.
- Sweet Scent: Immediate wild encounter on valid grass tiles.
- Menu Behavior:
    - Start Menu: Resets to POKEDEX (1) after battle.
    - Party Menu: Remembers last selection.
    - Battle Move Menu: Remembers last selection within the same battle.
- Navigation: NPCs and certain trees/ledges block paths. Verify collision before planning long routes. Use 'run_code' to check tile navigability.
- Battle Discipline: Always verify cursor position after closing sub-menus or between turns, as the menu remembers the previous selection.

## Training Log: XENON
- Start Turn: 14423
- Goal: Lv 13 (1261 Total EXP).
- Progress: 20 EXP remaining.
- Strategy: Sweet Scent at (18, 15) Route 32. Lick Gastly/Bellsprout/Hoppip. RUN from Normal-types.
- PP/HP: Return to Pokecenter if Lick PP < 5 or HP < 10.

## Tile Mechanics
- TALL_GRASS: Encounter-eligible.
- WALL/HEADBUTT_TREE: Impassable. Markers placed in Violet City.
- LEDGE_HOP: One-way movement. Markers placed on Route 32 and Violet City.
- COUNTER: Interaction point; impassable.

## Exploration Plan
- Goal: Reveal 100% of Route 32.
- Targets: West of (13, 10), East of (19, 28), South/West of (11, 37), Perimeter (1, 76-87).