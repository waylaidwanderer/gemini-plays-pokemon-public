# Pokémon Yellow Legacy - Hard Mode Notes

## Current Status & Immediate Objectives
- Location: Viridian City (Map ID 1) at (22,31).
- Immediate Objective: Navigate to Pokémon Center at (24,26) to heal and save. Then find Poké Mart.

## Pokémon Party Status
1. SPARKY (PIKACHU): Lv7 (23/26 HP, EXP: 442/512 to Lv8) | Moves: THUNDERSHOCK (20/30 PP), GROWL (40/40 PP), QUICK ATTACK (30/30 PP)

## Game Mechanics & Rules
- Battle Style: Set
- No items in battle.
- HMs can be forgotten, used from menu, not storable in PC.
- All 151 Pokémon obtainable.
- Trade evolutions by level (e.g., Haunter -> Gengar at 42, Machoke -> Machamp at 38).
- Smarter Trainer AI with anti-sweep tactics.
- Tougher boss fights.
- Dynamic scaling for Gyms 4-6.
- EXP. All obtainable without special requirements.
- Poisoned Pokémon lose 1 HP every 4 steps outside battle.
- **STAT Experience:** Pokémon gain increased stats from EXP that enemy trainers' Pokémon don't have. Training a Pokémon from a low level (e.g., Lv5 to Lv50) can result in stats comparable to a much higher level opponent (e.g., Lv60).
- Enemy trainers are not limited by Power Points (PP) for their moves, unlike the player's Pokémon.

## Level Caps
- 0 badges: 12
- 1 badge: 21
- 2 badges: 24
- 3 badges: 35
- 4 badges: 43
- 5 badges: 50
- 6 badges: 53
- 7 badges: 55
- 8 badges: 57
- After Lorelei: 58
- After Bruno: 59
- After Agatha: 62
- After Lance: 65

## Current Goals & Plans
- **Primary:** Defeat Brock, the Pewter City Gym Leader.
- **Secondary:** Acquire Poké Balls from Viridian City's Poké Mart.
- **Tertiary:** Continue training SPARKY towards level 8-9.

## Strategy Notes & Lessons Learned
- **World Knowledge Graph (WKG):** Record transitions (map changes) immediately. `add_node` payload should NOT include an `id`. Use descriptive names and tags for nodes. Ensure `destination_entry_point` is accurate for warp edges. Correct mistakes in WKG promptly.
- **Map Markers:** Mark used warps (entry/exit), defeated trainers, strategic points, interaction loops, dead ends, and static info signs. Use distinct emojis for clarity.
- **Interaction Strategy:** Avoid repeating interactions with objects/NPCs in confirmed loops without a new trigger. If an NPC or object is unresponsive or in a loop after 2-3 attempts, move on. Mark loops clearly. Pay close attention to adjacency and facing requirements for interaction.
- **Default vs. Event Locations:** During events, interactions might be required at default sprite locations, not visual event locations, or vice-versa. Test both if stuck.
- **Notepad `replace` Action:** Must use the exact current text from the notepad for `old_text`. Game suggestions for `old_text` can be outdated. Copy-paste is safest. Verify notepad state before replacing.
- **Event Triggers:** Prioritize common Pokémon game event triggers (e.g., attempting to leave the starting town, Mom's dialogue) when other interactions fail or lead to loops.
- **Path Planning:** Consult Map Memory carefully to identify obstacles (fences, impassable tiles). Plan routes to avoid known blockages. For simple maps, manual pathing is often faster than relying on agents that might fail. Be careful with assumptions about tile passability.
- **NPC Movement:** NPCs can move and block paths. Be prepared to reroute.
- **Warp Mechanics:** 1x1 warps are usually instant. 2x1 or 1x2 warps (like exit mats) require moving onto the warp then into the boundary/direction of warp.

## Tile Types Discovered
- **ground**: Walkable tile.
- **impassable**: Walls, objects, bookcases, fences etc. Cannot be entered or traversed.
- **warp**: Tile that initiates a map transition. Rules for activation vary.
- **water**: Requires Surf to cross.
- **grass**: Tall grass where wild Pokémon encounters occur.
- **ledge**: Can be jumped down, not up.

## Type Matchup Discoveries
- Ghost-type > Psychic-type.
- Poison-type > Bug-type; Bug-type !> Poison-type.

## Defeated Trainers
(Format: [Trainer Name] - [Map Name] at (X,Y))

## Key Discoveries & Event Chronology
- **Player's House Second Floor (Map ID 38):** PC at (1,2).
- **Pallet Town (Map ID 0) - Initial Exploration:** Signs, Rival's House, Oak's Lab entrances identified.
- **Rival's House (Map ID 39):** Daisy dialogue, obtained Town Map.
- **Player's House First Floor (Map ID 37):** Mom dialogue triggered Oak's Lab event.
- **Oak's Lab (Map ID 40) - Pre-Starter:** Scientist/Girl dialogue (type matchups).
- **Pallet Town (Map ID 0) - Starter Event Trigger:** Attempting to enter Route 1 grass triggered Oak.
- **Oak's Lab (Map ID 40) - Starter Pokémon Event:** Received PIKACHU (SPARKY). Battled BLAZe (EEVEE Lv5). SPARKY to Lv6, learned QUICK ATTACK. Oak explained Pikachu's behavior.
- **Route 1 (Map ID 12):** Youngster at (6,26) gave Potion. Sign at (10,28). Youngster at (16,14) explained STAT Experience.
- **Wild Battles (Route 1):** Multiple Pidgey, Rattata. SPARKY reached Lv7. Defeated Spearow Lv5 (SPARKY EXP to 442).
- **Viridian City (Map ID 1):** Arrived from Route 1. Sign at (22,30) explained enemy trainers are not limited by PP.

## Pathing Lessons & Observations
- **Pikachu on Warp Tiles:** If Pikachu is on a warp tile I need to use/pass, and I'm not facing him, it takes two presses in his direction to move onto the tile (first turns, second moves). This can trigger unintended warps.

## Defined Agents
- **route_pathfinder**: Calculates a sequence of moves (Up, Down, Left, Right) to navigate from a start coordinate to an end coordinate on the current map. Input: {start_x, start_y, end_x, end_y}. Output: {path_found, steps[]}. (Code-enabled)

## Agent Usage & Failures
- **route_pathfinder (Turn 477):** Failed with error "Agent LLM resp missing content (Iter 1)" when trying to path from (14,21) to (17,14) on Route 1. Needs further testing on simpler paths.

## Future Agent Ideas

- **CUT is a Bug-type HM move** (Learned from Brunette Girl in Viridian School House).