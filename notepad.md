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
- **Fly to Ecruteak Attempt**: Started Turn 45183. 70 turns failed due to menu hallucination.

# Strategy Tools
- **roamer_strategist**: Agent for hunt efficiency.
- **grass_pacer**: Tool for wild encounter pacing.
- **open_fly_map**: Tool for FLY navigation (Assumes cursor on POKEDEX).

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Hypotheses & Lessons
- [Lesson] Fly attempt stagnation: 70 turns. Cause: Hallucinating Fly Map open while in Overworld.
- [Lesson] Menu persistence: Start menu cursor remains on the last selected item (e.g., GEAR was at index 4).
- [Verified] Start menu order: 1.POKEDEX, 2.POKEMON, 3.PACK, 4.GEAR, 5.[Player], 6.SAVE, 7.OPTION, 8.EXIT.

# Current Plan
1. Reset state by walking from Route 31 Gatehouse to Route 31.
2. Verify overworld state.
3. Open menu and verify cursor position before using FLY.