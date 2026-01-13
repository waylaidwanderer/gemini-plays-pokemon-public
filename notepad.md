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
- Repel Trick: Lv 19 lead (ICARUS) with Super Repel active. Roamers are Lv 40.
- Encounter Contingency: If Roamer appears -> PACK -> Right to BALLS -> MASTER BALL -> USE.
- Roamer Status: NOT YET ENCOUNTERED. Use Master Ball on sight.
- Strategist Tips: Pokegear map is useless until first encounter. Pace max 4-5 steps in grass per shuffle. Minimize battles to keep lead under Lv 40.

# Session Tracking
- Session 4 (Ecruteak Shuffle) Start: Turn 45281.
- Completed Shuffles: 23.
- Current Shuffle: 24 (In Progress).
- Total Encounters: 0.
- Repel Status: Applied Turn 45439. Steps Taken: 3/200.

# Strategy: Ecruteak Shuffle (Pre-Encounter)
- Path: Ecruteak City <-> Route 37.
- Method: 
  1. Enter Route 37 at (7, 0) or (8, 0).
  2. Move to tall grass at (7, 2).
  3. Pace exactly 4 steps using grass_pacer.
  4. Return to Ecruteak at (17, 35) or (18, 35).
  5. Repeat.
- Note: Pokegear Map is useless until the first encounter.
- Lead: ICARUS (Lv 19).

# Strategy Tools
- grass_pacer: Tool for wild encounter pacing.

# Dana's Gift
- NPC: Lass Dana.
- Location: Route 38.
- Status: Gift waiting (Turn 45331 call).

# Lessons Learned
- Menu Navigation: Always verify the Start menu is open before using `menu_navigator_v2`. The cursor persists, but the menu must be active.
- Notepad Editing: Be extremely precise with `old_text`. Special characters like < can be tricky.
- Roamer Hunting: Efficiency comes from map transitions, not grass pacing. The map icon is the fastest check (post-encounter). Pre-encounter, 4 steps in grass is optimal.
- Repel Steps: Verify step count against actual movement rather than estimated button presses.

# Yanma Swarm
- Route 35.
- Status: Active (Turn 45457 call).
- Note: Yanma is already registered in Pokedex. Roamer hunt remains priority.
- BUOY: Impassable water boundary. Verified: Yes.
- Session Tracking Update: Turn 45459 Reflection completed. Focus remains on reaching Ecruteak for the shuffle.
- Lesson: Fly Map navigation requires precise cursor counts. Cherrygrove to Ecruteak is 2x Up. Goldenrod to Ecruteak is 1x Up, 1x Right. Violet to Ecruteak is 1x Up.
- Error Analysis: Recent navigation failures were due to miscounting map grid steps. Starting position on the Fly map is ALWAYS the current city/route.