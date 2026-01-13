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

# Legendary Roamer Hunt Strategy
- **Overview**: Ecruteak Shuffle (Route 37 <-> Ecruteak).
- **Repel Trick**: Lv 19 lead (ICARUS) with Super Repel active.
- **Status**: Super Repel Active (200 steps). Used at Turn 45241.
- **Roamer Status**: NOT YET ENCOUNTERED. Use Master Ball on sight.
- **Start Turn**: 45183

# Strategy Tools
- **roamer_strategist**: Use to analyze hunt efficiency.
- **grass_pacer**: Use for automated wild encounter pacing.
- **open_fly_map**: Robust tool for FLY navigation.

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Hypotheses & Lessons
- [Lesson] Fly attempt started Turn 45183. 60 turn stagnation due to menu/save loop hallucination.
- [Hypothesis] Moving in overworld resets Start menu cursor to POKEDEX.
- [Verified] Start menu order: 1.POKEDEX, 2.POKEMON, 3.PACK, 4.GEAR, 5.[Player], 6.SAVE, 7.OPTION, 8.EXIT.

# Attempted Fly to Ecruteak
- Started: Turn 45183.
- Status: Resetting mental state. Currently in Route 31 Gatehouse.
- Plan: Use open_fly_map tool, then navigate to Ecruteak manually.