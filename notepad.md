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
- Repel Status: Applied Turn 45439. Steps Taken: 0/200.
- Fly Attempt History: Turn 45439-45489 (50 turns fumbling). Resetting loop.
- Verified Fly Logic: Start -> Pokemon -> Icarus -> Fly -> (Map). From Violet to Ecruteak = Up, A.
- Current Position: Violet City (31, 26). Target: Ecruteak.
- Fly Map Grid (Johto):
  - Cherrygrove
  - Violet (1x Up from Cherrygrove)
  - Ecruteak (1x Up from Violet)
  - Goldenrod (1x Left from Violet)
  - Azalea (1x Down from Goldenrod)
  - Olivine (1x Left from Goldenrod)
  - Cianwood (1x Left from Olivine)
  - Mahogany (1x Right from Ecruteak)
  - Blackthorn (1x Right from Mahogany)
  - Indigo Plateau (1x Up from Mahogany)
  - New Bark Town (1x Right from Cherrygrove)

# Dana's Gift
- NPC: Lass Dana.
- Location: Route 38.
- Status: Gift waiting (Turn 45331 call).

# Lessons Learned
- Menu Navigation: Always verify the Start menu is open before using `menu_navigator_v2`. The cursor persists, but the menu must be active.
- Roamer Hunting: Efficiency comes from map transitions, not grass pacing. The map icon is the fastest check (post-encounter). Pre-encounter, 4 steps in grass is optimal.
- Repel Steps: Verify overworld movement for step count.

# Yanma Swarm
- Route 35.
- Status: Active (Turn 45457 call).
- Note: Yanma is already registered in Pokedex. Roamer hunt remains priority.
- BUOY: Impassable water boundary. Verified: Yes.