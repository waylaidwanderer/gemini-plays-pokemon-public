# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look. (COMPLETE)
- Evolve to Haunter (Lv 25) and train to ~Lv 38-40 (Speed 73-110) to outspeed Suicune.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Ultra Balls.
- Track Suicune using Pokedex AREA map. Cycle between adjacent routes to force movement.
- Item Goal: Buy Ultra Balls at Goldenrod or Blackthorn Marts.

## Verified Mechanics & Lessons
- Cursor Persistence: Battle move menu remembers selection. Always verify cursor position.
- Menu Navigation: Start, Party, and Battle menus wrap. Use relative navigation.
- Tool Hygiene: Refine custom tools immediately if they produce incorrect results. Use manual inputs to progress in battle.
- Tile Collision: NPCs, certain trees, and ledges block paths. Use 'run_code' to verify navigability.
- Status moves: Fails if the target already has a status condition (e.g. Hypnosis vs Paralyzed).
- Sweet Scent: Triggers immediate wild encounters on valid grass tiles.
- FLOOR_UP_WALL: One-way pathing (traversable North, impassable South). Acts as a ledge you jump UP. Blocks southward progression at y=6, 14, 24, 26, 34, 36, 72, 76, 86.
- LEDGE_HOP_DOWN: One-way pathing (traversable South, impassable North). Found at (12, 27), (16, 15), (6, 81), (8, 81).
- LEDGE_HOP_RIGHT: One-way pathing (traversable East, impassable West). Found at (17, 12), (17, 13), (17, 14), (9, 80).

## Type Effectiveness (Verified)
- Ghost Immunity: Ghost-type Pokemon are immune to Normal (e.g., Wrap, Leer) and Fighting-type moves.
- Ghost Ineffectiveness: Ghost moves (Lick) do not affect Normal-type Pokemon.
- Hoppip Immunity: Lick (Ghost) fails to affect wild Hoppip (Grass/Flying) in this game version.
- Fighting/Normal vs Ghost: Ineffective (Immunity).

## Training Log: XENON
- Status: Lv 13 reached. Mean Look learned.
- Next Goal: Lv 25 (Evolution).
- Method: Sweet Scent at (18, 15) Route 32. RUN from Normal-types and Hoppip.

## Exploration Plan
- Goal: Reveal 100% of Route 32.
- Current Task: Exit the 'pond' area via (10, 26) and head to the western corridor.
- Future Targets: West of (13, 10), East of (19, 28), Perimeter (1, 76-87).

## NPCs & Locations
- Fisher Tully: (15, 13) Route 32. Contact for fishing info.
- Slowpoketail Seller: (11, 67) Route 32. Selling tails for ¥1,000,000.