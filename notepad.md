# Tile Mechanics (Global)
- FLOOR: Traversable. Verified: Yes.
- WALL: Impassable. Verified: Yes.
- WATER: Traversable with Surf. Verified: Yes.
- TALL_GRASS: Traversable. Wild encounters. Verified: Yes.
- HEADBUTT_TREE: Impassable. Verified: Yes.
- COUNTER: Impassable. Face to interact. Verified: Yes.
- WARP_CARPET: Traversable. Map transition. Verified: Yes.
- LEDGE_HOP_DOWN: One-way (Down). Verified: Yes.
- DOOR: Warp tile. Verified: Yes.

# Menu Mechanics
- Start Menu Order: 1.POKEDEX, 2.POKEMON, 3.PACK, 4.POKEGEAR, 5.GEM, 6.SAVE, 7.OPTION, 8.EXIT.
- Persistence: The Start menu cursor persists on the last selected category even after overworld movement and map transitions.
- Fly Map (Hypothesis): The cursor persists on the last highlighted destination. [Verification Needed]

# Legendary Roamer Hunt Strategy
- Overview: Ecruteak Shuffle (Route 37 <-> Ecruteak).
- Repel Trick: Lv 19 lead (ICARUS) with Super Repel active.
- Status: Super Repel Active (Used Turn 45288).
- Encounter Contingency: If Roamer appears -> PACK -> Right to BALLS -> MASTER BALL -> USE.
- Roamer Status: NOT YET ENCOUNTERED. Use Master Ball on sight.

# Strategy Tools
- roamer_strategist: Agent for hunt efficiency.
- grass_pacer: Tool for wild encounter pacing.

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Strategy: Ecruteak Shuffle
- Path: Ecruteak City <-> Route 37.
- Method: Transition maps, pace ~10 steps in Route 37 tall grass, repeat.
- Lead: ICARUS (Lv 19).