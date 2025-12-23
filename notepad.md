# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
1. Catch a Gastly in Sprout Tower (Night only, Lv 3-6).
2. Train Gastly to Lv 13 to learn Mean Look.
3. Evolve to Haunter (Lv 25) to ensure Base 95 Speed (Suicune is Base 85).
4. Track Suicune using Pokedex AREA map.
5. Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Great Balls.

## Global Tile Mechanics
- FLOOR: Standard traversable tile. In Sprout Tower, some FLOOR tiles are "safe" (no encounters).
- TALL_GRASS: Standard encounter tile. Movement registers as steps.
- WALL/HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN/LEFT/RIGHT: One-way movement.
- WARP_CARPET_RIGHT/DOWN: Map transition.
- WATER: Traversable with HM SURF.
- ICE: Sliding movement.
- COUNTER: Interaction point for NPCs behind them.
- LADDER: Vertical map transition.
- NPC: Map objects that block movement.

## Sprout Tower 1F Observations
- Sweet Scent failed at (14, 6) and (10, 11). These tiles are "safe".
- Goal: Find a FLOOR tile that supports wild encounters.

## Lessons Learned
- Roamer Logic: FLY and map boundary transitions cause roamers to move.
- Navigation: Avoid mixing directional and action buttons in a single sequence.
- Pacing: Change coordinates (X or Y) to count steps; spinning in place does not trigger encounters.
- Sweet Scent: Triggers an immediate wild encounter in areas with wild Pokemon. If it says "nothing here", the tile is safe.