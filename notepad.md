# Strategy: Investigate Mahogany Radio Broadcast
- Starting Turn: 7780
- Objective: Locate and shut down the source of the "mysterious radio broadcast" in Mahogany Town.
- HOW:
    1. Explore Team Rocket Base B1F to find the transmitter.
    2. Find the secret switch to disable security cameras.

# Tile Mechanics
- FLOOR: Verified traversable. Standard indoor/outdoor ground.
- WALL: Verified impassable. Includes trees, fences, and building walls.
- WATER: Verified traversable only with Surf (HM03) and Fog Badge.
- TALL_GRASS / LONG_GRASS: Verified traversable. Triggers wild encounters.
- MART_SHELF: Verified impassable.
- COUNTER: Verified impassable. Interacting from an adjacent tile allows talking to NPCs behind it.
- WARP_CARPET_DOWN / WARP_CARPET / LADDER / STAIRS / DOOR: Verified map transition.
- HEADBUTT_TREE: Verified impassable. Can be interacted with using Headbutt.
- CUT_TREE: Verified impassable. Can be removed using Cut (HM01) and Hive Badge.
- PC: Verified impassable. Interacting from below (facing UP) allows access.
- LEDGE_HOP_DOWN: Verified one-way passage (Down only).
- FLOOR_UP_WALL: Verified traversable.

# Party Training Status
- ICARUS (PIDGEY): Lv16. Moves: Quick Attack, Sand-Attack, Gust, Fly.
- KIMCHI (GLOOM): Lv21. Evolved from Oddish.
- GNEISS (GRAVELER): Lv36.
- Calcifer (TYPHLOSION): Lv36.
- Ravioli (KRABBY): Lv10.
- Blarney (SUDOWOODO): Lv20.

# General Mechanics & Tools
- Battle: Sweet Scent lowers opponent's evasion. Karate Chop is Fighting-type.
- Tool: find_path_v2 handles trees, water-to-land, ledges, and warps.

# Type Matchups (Observed)
- Ground vs Water/Poison: Super Effective.
- Rock vs Water/Flying: Super Effective.
- Fighting vs Poison: Not Very Effective.
- Fighting vs Rock/Ground: Super Effective.
- Water vs Fire: Super Effective.
- Water vs Rock/Ground: 4x Super Effective.
- Grass vs Water/Fighting: Super Effective.
- Fighting vs Grass/Poison: Not Very Effective.

# Battle & NPC Knowledge
- Mahogany Mart (11, 7): Secret stairs revealed at (7, 3).
- Mahogany Gym (6, 13): Blocked by Fisher at (6, 14) until Lake of Rage investigation.
- Pokefan M at (8, 1) in PC: Saw "men in black" (Team Rocket) at Lake of Rage.
- Camper Spencer (Route 43): Sandshrew (Lv17), Zubat (Lv19), Sandslash (Lv17).
- Fisher Tully (Route 42): Qwilfish (Water/Poison).
- Pokemaniac Ron (Route 43): Nidoking (Lv19♂). Found at (14, 7). Mentions "MALICE" (rival) made fun of his Pokémon.
- Pokemaniac Brent (Route 43): Lickitung (Lv19♂). Found at (13, 20).
- Pokemaniac Ben (Route 43): Slowbro (Lv19♂). Found at (13, 5).
- Cooltrainer F (Lake of Rage): Saw a red Gyarados in the lake. Found at (24, 29).
- Fishing Guru (Lake of Rage, Magikarp House): Mentions the lake is a crater made by rampaging Gyarados. Rainwater filled it.

# Money & Economy
- ¥1000: Toll paid at Route 43 Gatehouse.
- Pokemaniac Ron: ¥1140 (Turn 7679).
- Pokemaniac Brent: ¥1140 (Turn 7654).
- Pokemaniac Ben: ¥1140 (Turn 7699).

# PC Storage (Box 1)
- ROCKY (ONIX): Lv6, EGG (CLEFFA): Lv5, XFDW (MEOWTH): Lv16, FRITTATA (TOGEPI): Lv5, SHUCKIE (SHUCKLE): Lv15.

# Discovered Locations
- Route 42: MT.MORTAR WATERFALL CAVE INSIDE. Sign at (54, 8): ECRUTEAK CITY - MAHOGANY TOWN.
- Mahogany Town: Welcome to the Home of the Ninja.
- Route 43 Sign (13, 3): LAKE OF RAGE - MAHOGANY TOWN.

# Pokémon Swarms
- Route 35: Ditto (Arnie's call, Turn 7769).

# Lessons: Turns 7500-7650
- Coordination: Always verify NPC coordinates in Game State before marking or pathing.
- Tool Usage: `stun_npc` is essential for interacting with pacing NPCs like Cooltrainer F.
- Training: Switch-training ICARUS is highly effective; he reached Lv15 and learned Quick Attack.
- Navigation: Surfing requires updated exploration tools to handle water tiles.

# Lessons: Turns 7650-7800
- Capturing: Burn status is efficient but risky for low-HP targets like Red Gyarados. Sleep is safer.
- Fly Map: Navigation requires precise cursor movement; check intermediate states to verify cursor position.
- False Constraints: If a goal seems too complex, re-evaluate the root assumption (e.g., don't assume an NPC must move if there's a path around).
- Efficiency: Use Fly to bypass long routes when the party is weak.

# Lessons: Turns 7800-7850
- Security Mechanics: Column 24 in the Rocket Base B1F triggers intruder alerts via cameras at (24, 1) and (24, 5).
- Agent Hygiene: Always verify current screen state before calling battle agents to avoid stale data (Turn 7828 mistake).
- Immediate Action: If a marker is missed or a lesson learned, record it immediately to avoid context loss.

# Area Mechanics: Team Rocket Base B1F
- Security Cameras: Located at (24, 1) and (24, 5). Walking past them (e.g., column 24) triggers an "Intruder alert!" and a Rocket Grunt battle.
- Hypothesis: Surveillance cams are in the POKéMON statues. Rocket Grunts will keep appearing until a secret switch is tripped (based on NPC dialogue).