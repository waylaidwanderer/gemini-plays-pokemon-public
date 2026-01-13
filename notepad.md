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
- **Status**: Super Repel Active (200 steps). Used at Turn 45249.
- **Roamer Status**: NOT YET ENCOUNTERED. Use Master Ball on sight.
- **Fly to Ecruteak Attempt**: Started Turn 45183. Stalled for 70+ turns due to menu/state hallucinations.

# Strategy Tools
- **roamer_strategist**: Agent for hunt efficiency.
- **grass_pacer**: Tool for wild encounter pacing.
- **open_fly_map**: Tool for FLY navigation (Assumes cursor on POKEDEX).

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Hypotheses & Lessons
- [Lesson] Start Menu Cursor persists even after overworld movement.
- [Verified] Start Menu Order: 1.POKEDEX, 2.POKEMON, 3.PACK, 4.POKEGEAR, 5.GEM, 6.SAVE, 7.OPTION, 8.EXIT.
- [Verified] Fly Map Navigation from New Bark: Left (Cherrygrove), Up (Violet), Up (Ecruteak).

# Current Plan
1. Fly Map is open at New Bark Town.
2. Navigate: Left (to Cherrygrove), Up (to Violet), Up (to Ecruteak).
3. Confirm with A.