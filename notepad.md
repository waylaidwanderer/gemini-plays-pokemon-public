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
- BUOY: Impassable water boundary. Verified: Yes.

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
- Fly Attempt History: Turn 45439-45501 (62 turns fumbling). 
- Fly Loop Resolution: Opening Fly map and stopping to verify grid (Turn 45502).
- Verified Fly Logic: Start -> Pokemon -> Icarus -> Fly -> (Map).
- Current Position: Cherrygrove City (29, 4). Target: Ecruteak City (17, 35).

# Fly Map Grid (Johto)
- New Bark Town: Base (East)
- Cherrygrove City: 1x Left from New Bark.
- Violet City: 1x Up from Cherrygrove.
- Ecruteak City: 1x Up, 1x Left from Violet? (To be verified)

# Dana's Gift
- NPC: Lass Dana.
- Location: Route 38.
- Status: Gift waiting (Turn 45331 call).

# Lessons Learned
- Menu Navigation: Always verify the Start menu is open before using `menu_navigator_v2`. The cursor persists.
- Roamer Hunting: Efficiency comes from map transitions, not grass pacing.
- Repel Steps: Verify overworld movement for step count. Menu loops do not count.
- Fly Grid: Cherrygrove -> Up -> Violet. Up from Violet is blocked or same. Ecruteak is likely West of the Violet column.