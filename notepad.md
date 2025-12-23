# Suicune Capture Strategy
## Strategy: The Mean Look Pivot
- Train XENON (Gastly) to Lv 13 to learn Mean Look.
- Evolve to Haunter (Lv 25) to ensure Base 95 Speed (Suicune is Base 85). Haunter needs to be faster than Suicune to use Mean Look before it flees.
- Track Suicune using Pokedex AREA map.
- Lead with Haunter: Mean Look (Turn 1) -> Hypnosis -> Great Balls.
- Note: Strategy Advisor suggests training to Lv 30 for survivability.

## Game Mechanics & Lessons
- Ghost-type Moves: Lick (Ghost) does not affect Normal types.
- Ghost-type Resistances: Leech Life (Bug) is "not very effective" against Ghost types.
- Accuracy/Status: Status moves like Supersonic can hit Ghost types (not immune); misses are due to accuracy/luck.
- Sweet Scent: Triggers immediate encounters on valid grass tiles.
- Type Effectiveness: Use `get_type_effectiveness_gen2` tool for verified matchups.
- Menu Wrapping: The Start menu (8 items) and Party menu (6 items) in Crystal wrap. Tracking cursor position is mandatory for tool reliability.
- Phone Calls: Incoming calls interrupt button sequences. Tools must start with B-presses to clear dialogue.

## Training Plan: XENON (How)
- Method: Grind on Route 32 grass using Sweet Scent.
- Target: Lv 13 for Mean Look, then Lv 30.
- Strategy: Flee from Normal-types (Rattata, Hoothoot, Pidgey) to conserve Lick PP.
- Maintenance: Use Fresh Water/Lemonade from pack to heal when HP < 10.

## Route 32 Observations
- Ledge at (14, 6): Jumpable south.
- Slowpoketail Scam: NPC at (11, 67) tries to sell a tail for ¥1,000,000. Verified dead end/scam.
- Fisher NPC: Located at (15, 13) (marked 📍).

## Tile Mechanics (Verified)
- FLOOR: Standard traversable tile.
- TALL_GRASS: Standard encounter tile.
- WALL/HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN: Jumpable one-way movement. Verified at (14, 6).
- WARP_CARPET: Map transition. Verified.
- WATER: Traversable with HM SURF. Verified.
- ICE: Sliding movement. Verified.
- COUNTER: Interaction point for NPCs; impassable.
- LADDER: Vertical map transition; traversable.
- NPC: Map objects that block movement. Verified.