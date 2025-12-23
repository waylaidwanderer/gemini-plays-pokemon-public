# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look.
- Evolve to Haunter (Lv 25) to ensure Base 95 Speed (Suicune is Base 85). Haunter needs to be faster than Suicune to use Mean Look before it flees.
- Track Suicune using Pokedex AREA map.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Great Balls.

## Tile Mechanics (Verified)
- FLOOR: Standard traversable tile. Verified traversable.
- TALL_GRASS: Standard encounter tile. Verified traversable.
- WALL/HEADBUTT_TREE: Impassable. Verified.
- LEDGE_HOP_DOWN/LEFT/RIGHT: Jumpable one-way movement. Jump Down verified at (14, 6).
- WARP_CARPET_RIGHT/DOWN: Map transition. Verified.
- WATER: Traversable with HM SURF. Verified.
- ICE: Sliding movement. Verified.
- COUNTER: Interaction point for NPCs; impassable. Verified.
- LADDER: Vertical map transition; traversable. Verified.
- NPC: Map objects that block movement. Verified.

## Game Mechanics
- Ghost-type Moves: Lick (Ghost) does not affect Normal types.
- Ghost-type Resistances: Leech Life (Bug) is "not very effective" against Ghost types.
- Accuracy/Status: Status moves like Supersonic can hit Ghost types (not immune); misses are due to accuracy/luck.
- Sweet Scent: Triggers immediate encounters on valid grass tiles.
- Type Effectiveness: Use `get_type_effectiveness_gen2` tool for verified matchups.

## Sprout Tower Analysis
- Layout: Middle section (x=5 to x=14) is isolated. Access outer ring via 2F ladders.
- Encounters: FLOOR tiles at (14, 6), (10, 11), and (14, 10) are safe zones. (6, 5) on 2F is a valid encounter tile.

## Training Plan: XENON (How)
- Grind Start: Turn #13980 (Tuesday 12:45 AM).
- Method: Grind on Route 32 grass using Sweet Scent.
- Target: Lv 13 for Mean Look.
- Strategy: Flee from Normal-types (Rattata, Hoothoot, Pidgey) to conserve Lick PP.
- Maintenance: Use Fresh Water/Lemonade from pack to heal when HP < 10.

## Route 32 Observations
- Ledge at (14, 6): Jumpable south.
- Slowpoketail Scam: NPC at (11, 67) tries to sell a tail for ¥1,000,000. Verified dead end/scam.