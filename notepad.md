# Strategy: Lake of Rage Investigation
- Goal: Locate the source of the "rampage" (Red Gyarados).
- Path: Follow Route 43 North to Lake of Rage.
- Status: Gatehouse passage unlocked (paid ¥1000 toll). ICARUS moved to lead.
- Method: Lead with ICARUS (Lv11 Pidgey) for EXP sharing. Switch to GNEISS or Calcifer for tough battles.
- Contingencies: If blocked, search for Lance or explore water with Surf.

# Party Training Status
- ICARUS (PIDGEY): Lv12. Current Lead for EXP sharing.
- KIMCHI (GLOOM): Lv21. Evolved from Oddish.
- GNEISS (GRAVELER): Lv35.
- Calcifer (TYPHLOSION): Lv36.
- Ravioli (KRABBY): Lv10.
- Blarney (SUDOWOODO): Lv20.

# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable only with Surf (HM03) and Fog Badge.
- TALL_GRASS: Traversable. Triggers wild encounters.
- MART_SHELF: Impassable.
- COUNTER: Impassable. Interacting from an adjacent tile allows talking to NPCs behind it.
- WARP_CARPET_DOWN / WARP_CARPET / LADDER / STAIRS / DOOR: Map transition.
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt.
- CUT_TREE: Impassable. Can be removed using Cut (HM01) and Hive Badge.
- PC: Impassable. Interacting from below (facing UP) allows access.
- LEDGE_HOP_DOWN: One-way passage (Down only).

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
- Mahogany Mart (11, 7): NPCs mention Gyarados experiments. Suspicious tile at (7, 3) currently inactive.
- Mahogany Gym (6, 13): Blocked by Fisher at (6, 14) until Lake of Rage investigation.
- Pokefan M at (8, 1) in PC: Saw "men in black" (Team Rocket) at Lake of Rage.
- Camper Spencer (Route 43): Sandshrew (Lv17), Zubat (Lv19), Sandslash (Lv17).
- Fisher Tully (Route 42): Qwilfish (Water/Poison).
- Pokemaniac Shane (Route 42): Nidorina (Poison), Nidorino (Poison).
- Hiker Benjamin (Route 42): Diglett (Ground), Dugtrio (Ground), Geodude (Rock/Ground).

# PC Storage (Box 1)
- ROCKY (ONIX): Lv6, EGG (CLEFFA): Lv5, XFDW (MEOWTH): Lv16, FRITTATA (TOGEPI): Lv5, SHUCKIE (SHUCKLE): Lv15.

# Discovered Locations
- Route 42: MT.MORTAR WATERFALL CAVE INSIDE. Sign at (54, 8): ECRUTEAK CITY - MAHOGANY TOWN.
- Mahogany Town: Welcome to the Home of the Ninja.

# Reflection Turn #50 Lessons
- Methodical progression: Always clear the exploration alert by verifying reachable unseen tiles.
- Tool hygiene: Defined `check_reachable_unseen` to automate exploration checks.
- Battle efficiency: ICARUS training is the priority for wild encounters.
- Goal status: Primary goal (Lake of Rage) is active. Path is clear.
- Verification: Root hypotheses for recent puzzles were correct. No major errors to report.
- Pokemaniac Brent (Route 43): Lickitung (Lv19♂). Found at (13, 20).