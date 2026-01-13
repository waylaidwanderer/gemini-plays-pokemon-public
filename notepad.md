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

# Legendary Roamer Hunt Strategy
- Overview: Ecruteak Shuffle (Route 37 <-> Ecruteak).
- Repel Trick: Lv 19 lead (ICARUS) with Super Repel active.
- Repel Status: Applied at Turn 45316.
- Encounter Contingency: If Roamer appears -> PACK -> Right to BALLS -> MASTER BALL -> USE.
- Roamer Status: NOT YET ENCOUNTERED. Use Master Ball on sight.

# Session Tracking
- Session 4 (Ecruteak Shuffle) Start: Turn 45281.
- Shuffles Completed: 7.
- Total Encounters: 0.
- Repel Status: Applied Turn 45316. Steps Taken: 182/200.

# Strategy Tools
- roamer_strategist: Agent for hunt efficiency.
- grass_pacer: Tool for wild encounter pacing.

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Strategy: Ecruteak Shuffle (Pre-Encounter)
- Path: Ecruteak City <-> Route 37.
- Method: 
  1. Enter Route 37.
  2. Move to tall grass at (14, 12).
  3. Pace exactly 4 steps.
  4. If no encounter, return to Ecruteak and repeat.
- Note: Pokegear Map is useless until the first encounter.
- Lead: ICARUS (Lv 19).

# Dana's Gift
- NPC: Lass Dana.
- Location: Route 38.
- Status: Gift waiting (Turn 45331 call).

# Lessons Learned
- Menu Navigation: Always verify the Start menu is open before using `menu_navigator_v2`. The cursor persists, but the menu must be active.
- Notepad Editing: Be extremely precise with `old_text`. Special characters like < can be tricky.
- Roamer Hunting: Efficiency comes from map transitions, not grass pacing. The map icon is the fastest check.