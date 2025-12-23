# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look.
- Evolve to Haunter (Lv 25) and train to ~Lv 38-40 (Speed 73-110) to outspeed Suicune.
- Track Suicune using Pokedex AREA map. Cycle between adjacent routes (e.g., 36/37) to force encounter.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Ultra Balls.
- Item Goal: Buy Ultra Balls at Goldenrod or Blackthorn Marts.

## Lessons Learned
- Cursor Persistence: The battle move menu remembers the last selected move across turns and battles. Always verify cursor position.
- Menu Navigation: Start, Party, and Battle menus wrap. Use relative navigation for efficiency.
- Tool Reliability: Custom tools must be verified and refined immediately if they produce incorrect results.
- Tile Navigability: NPCs, certain trees, and ledges block paths. Verify collision with 'run_code' before planning long routes.
- Type Matchups: Ghost is immune to Normal/Fighting. Lick (Ghost) is ineffective against Normal types.

## Game Mechanics & Insights
- Move Effectiveness: Leech Life (Bug) is NVE against Ghost.
- Status Accuracy: Status moves can hit Ghost types. Missing moves display "It didn't affect".
- Switching: Resets confusion and stat changes.
- Sweet Scent: Immediate wild encounter on valid grass tiles.

## Training Log: XENON
- Start Turn: 14423
- Goal: Lv 13 (1261 Total EXP).
- Remaining: 20 EXP.
- Strategy: Sweet Scent at (18, 15) Route 32. Lick Gastly/Bellsprout/Hoppip. RUN from Normal-types.
- PP/HP Management: Return to Pokecenter if Lick PP < 5 or HP < 10.

## Tile Mechanics
- TALL_GRASS: Encounter-eligible.
- WALL/HEADBUTT_TREE: Impassable. Markers placed in Violet City.
- LEDGE_HOP: One-way movement. Markers placed on Route 32 and Violet City.
- COUNTER: Interaction point; impassable.

## Exploration Plan
- Goal: Reveal 100% of Route 32.
- Targets: West of (13, 10), East of (19, 28), South/West of (11, 37), Perimeter (1, 76-87).