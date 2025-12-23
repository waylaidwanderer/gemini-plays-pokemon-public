# Suicune Capture Strategy
## The Repel Trick (Stale)
- Method: Super Repel filters wild Pokemon (Lv 13-16). Suicune (Lv 40) is the only possible encounter.
- Status: Roamer location reset by FLY at Turn #13845. Current location: UNKNOWN.

## Strategy: The Mean Look Pivot
1. Catch a Gastly in Sprout Tower (Night only, Lv 3-6).
2. Train Gastly to Lv 13 to learn Mean Look.
3. Evolve to Haunter (Lv 25) to ensure Base 95 Speed (Suicune is Base 85).
4. Track Suicune using Pokedex AREA map.
5. Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Great Balls.

## Hunting Session Tracking
- Sprout Tower Hunt Start: Turn #13848
- Target: Gastly (Night only, Lv 3-6)
- Pacing Area: (14, 11) <-> (13, 11)
- Total Great Balls: 40

## Global Tile Mechanics
- FLOOR: Standard traversable tile.
- TALL_GRASS: Standard encounter tile. Movement registers as steps.
- WALL/HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN/LEFT/RIGHT: One-way movement.
- WARP_CARPET_RIGHT/DOWN: Map transition.
- WATER: Traversable with HM SURF.
- ICE: Sliding movement.
- COUNTER: Interaction point for NPCs behind them.
- LADDER: Vertical map transition.

## Lessons Learned
- Roamer Logic: FLY and map boundary transitions cause roamers to move.
- Navigation: Avoid mixing directional and action buttons in a single sequence.
- Pacing: Change coordinates (X or Y) to count steps; spinning in place does not trigger encounters.
- Hallucination Prevention: If stuck in a tile loop, move to a new coordinate before resuming pacing.