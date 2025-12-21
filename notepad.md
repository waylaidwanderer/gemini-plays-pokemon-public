# Strategy: Investigate Mahogany Radio Broadcast
- Starting Turn: 7780

# Global Tile Mechanics
- FLOOR: Verified traversable. Standard indoor/outdoor ground. (Verified on B1F, B2F)
- WALL: Verified impassable. Includes trees, fences, statues, and dividers. (Verified on B1F, B2F)
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
- GNEISS (GRAVELER): Lv37 (103/103 HP). Moves: Magnitude, Defense Curl, Strength, Rollout.
- ICARUS (PIDGEY): Lv16 (43/43 HP). Moves: Quick Attack, Sand-Attack, Gust, Fly.
- Calcifer (TYPHLOSION): Lv36 (114/114 HP).
- KIMCHI (GLOOM): Lv21 (57/57 HP).
- Ravioli (KRABBY): Lv10 (27/27 HP).
- Blarney (SUDOWOODO): Lv20 (60/60 HP).

# Area Mechanics: Team Rocket Base B1F
- Security Cameras: Located at (24, 1), (24, 5), and (6, 1). Walking past column 24 or column 6 triggers a Rocket Grunt battle. Statues contain cameras.
- Secret Switch: Hypothesis: A secret switch trips the camera alarms.
- Floor Traps: Column 3 has traps at (3, 7), (3, 8), (3, 9), and (3, 10). Tiles (3, 11-13) are safe.

# Area Mechanics: Team Rocket Base B2F
- Locked Doors: Located at (14, 12) and (15, 12).
- Radio Transmitter: Located at row 9.
- Lance: Healed the party at (5, 13) and moved right.

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

# General Knowledge & Lessons
- Battle: Sweet Scent lowers evasion. Karate Chop is Fighting-type.
- Navigation: Columns/Rows can trigger events (e.g., column 24 and 6 for cameras).
- Tool: find_path_v2 handles trees, water-to-land, ledges, and warps.
- Tool: check_reachable_unseen fixed to return buttons when autopress_buttons is True.
- Tool: battle_move_selector refined with 'sleep 500' to handle menu transitions.