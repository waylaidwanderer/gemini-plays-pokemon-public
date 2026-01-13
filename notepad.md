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
- **Status**: Super Repel Active (200 steps).
- **Roamer Status**: NOT YET ENCOUNTERED. Use Master Ball on sight.

# Strategy Tools
- **roamer_strategist**: Use to analyze hunt efficiency.
- **grass_pacer**: Use for automated wild encounter pacing.

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Hypotheses & Lessons
- [Hypothesis] Start menu cursor persists on last selected option (e.g., PACK).
- [Hypothesis] Fly map cursor persists on last highlighted destination or defaults to New Bark Town.
- [Lesson] Menu sequence tools can fail if the game state is not what's expected.
- [Lesson] Scripted phone calls interrupt sequences.

# Current Strategy: Fly to Ecruteak
- Initial State: Inside Pack (cursor on Super Repel).
- Step 1: Exit Pack and Start Menu (B, B).
- Step 2: Open Start menu (Start).
- Step 3: Select POKEMON (Up, A).
- Step 4: Select ICARUS -> FLY (A, A).
- Step 5: Navigate Fly Map to Ecruteak and press A.