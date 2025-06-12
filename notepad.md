# Pokémon Yellow Legacy - Hard Mode Notes

## Current Status & Immediate Objectives
- Location: Viridian School House (Map ID 43) at (5,7).
- Immediate Objective: Interact with Little Girl at (5,6). Then, explore other interactables (Cooltrainer F, Notebook, Blackboard). Then, exit and find Poké Mart in Viridian City.

## Pokémon Party Status
1. SPARKY (PIKACHU): Lv7 (26/26 HP, EXP: 442/512 to Lv8) | Moves: THUNDERSHOCK (30/30 PP), GROWL (40/40 PP), QUICK ATTACK (30/30 PP)

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
- **STAT Experience:** Pokémon gain increased stats from EXP that enemy trainers' Pokémon don't have. Training a Pokémon from a low level (e.g., Lv5 to Lv50) can result in stats comparable to a much higher level opponent (e.g., Lv60). (Learned from Youngster on Route 1 (16,14))
- Enemy trainers are not limited by Power Points (PP) for their moves, unlike the player's Pokémon. (Learned from sign in Viridian City (22,30))
- PC Log Off: Selecting "LOG OFF" from the main PC menu (after selecting your name) saves the game.
- CUT is a Bug-type HM move. (Learned from Brunette Girl in Viridian School House (4,6))

## Level Caps
- 0 badges: 12
- 1 badge: 21
- 2 badges: 24
- 3 badges: 35
- 4 badges: 43
- 5 badges: 50
- 6 badges: 53
- 7 badges: 55
- 8 badges: 57 (Original game has 60 for E4. This is 57, then 58, 59, 62, 65. Need to confirm in-game if these are correct for this hack)

## Current Goals & Plans
- **Primary:** Defeat Brock, the Pewter City Gym Leader.
  - *Plan:* Find way to Pewter City (likely north of Viridian City, through Viridian Forest). Train SPARKY.
- **Secondary:** Acquire Poké Balls from Viridian City's Poké Mart.
  - *Plan:* Systematically explore Viridian City buildings until Poké Mart is found.
- **Tertiary:** Explore the Viridian School House for any items or information. (Current)
  - *Plan:* Interact with all NPCs and objects in the School House.

## Strategy Notes & Lessons Learned
- **World Knowledge Graph (WKG):** Record transitions (map changes) immediately. `add_node` payload should NOT include an `id`. Use descriptive names and tags for nodes. Ensure `destination_entry_point` is accurate for warp edges. Double-check `map_id` for nodes. Add edges promptly after nodes.
- **Map Markers:** Mark used warps (entry/exit), defeated trainers/info NPCs, strategic points, interaction loops, dead ends, and static info signs. Use distinct emojis for clarity.
- **Interaction Strategy:** Avoid repeating interactions with objects/NPCs in confirmed loops without a new trigger. If an NPC or object is unresponsive or in a loop after 1-2 attempts, move on. Mark loops clearly. Pay close attention to adjacency and facing requirements for interaction.
- **Event Triggers:** Prioritize common Pokémon game event triggers when other interactions fail or lead to loops.
- **Path Planning:** Consult Map Memory carefully to identify obstacles. For simple maps, manual pathing is often faster than relying on agents that might fail. Be careful with assumptions about tile passability and NPC blocking.
- **NPC Movement:** NPCs can move and block paths. Be prepared to reroute. Stun if necessary for interaction.
- **Warp Mechanics:** 1x1 warps are usually instant. 2x1 or 1x2 warps (like exit mats) require moving onto the warp then into the boundary/direction of warp.
- **Pikachu on Warp Tiles:** If Pikachu is on a warp tile I need to use/pass, and I'm not facing him, it takes two presses in his direction to move onto the tile (first turns, second moves). This can trigger unintended warps.
- **PC Interaction:** To interact with a PC, stand BELOW it (e.g., if PC is at (X,Y), stand at (X, Y+1)), face UP, and press A.

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

## Defeated Trainers / Info NPCs
(Format: [NPC Name/Type] - [Map Name] at (X,Y) - Info/Item)
- Youngster - Route 1 (6,26) - Gave Potion.
- Youngster - Route 1 (16,14) - Explained STAT Experience.
- Brunette Girl - Viridian School House (4,6) - CUT is Bug-type HM; SLAM type unknown.

## Key Discoveries & Event Chronology
- Pallet Town: Got Town Map from Daisy. Got PIKACHU from Oak. Battled BLAZe (won).
- Route 1: Got Potion. Learned about STAT Experience. Trained SPARKY to Lv7.
- Viridian City: Arrived. Learned enemy trainers have unlimited PP. Healed & Saved at Pokémon Center.
- Viridian School House: Entered. Learned CUT is Bug-type HM.

## Defined Agents
- **route_pathfinder**: Calculates a sequence of moves (Up, Down, Left, Right) to navigate from a start coordinate to an end coordinate on the current map. Input: {start_x, start_y, end_x, end_y}. Output: {path_found, steps[]}. (Code-enabled)
- **exploration_prioritizer_agent**: Analyzes current map data to suggest the most strategically valuable exploration target. Input: {player_x, player_y, current_objectives}. Output: {prioritized_target_type, target_coordinates, reasoning}. (Code-enabled)

## Agent Usage & Failures
- **route_pathfinder (Turn 477):** Failed with error "Agent LLM resp missing content (Iter 1)" when trying to path from (14,21) to (17,14) on Route 1. Needs further testing on simpler paths.
- **exploration_prioritizer_agent (Turn 534):** Suggested exploring the Pokémon Center warp (24,26) in Viridian City immediately after exiting it. Unhelpful. Prompt needs refinement.

- Little Girl - Viridian School House (5,6) - Confirmed Pokémon evolve by training, no trade needed.

- Cooltrainer F - Viridian School House (5,2) - Advised to read blackboard.

## Blackboard Status Info (Viridian School House)
- **SLP (Sleep):** Pokémon can't attack. Stays asleep after battles. Cure: AWAKENING.
- **BRN (Burn):** Reduces power, causes ongoing damage. Stays burnt after battles. Cure: BURN HEAL.
- **PSN (Poison):** Health steadily drops. Lingers after battles. Cure: ANTIDOTE.
- **FRZ (Freeze):** Pokémon becomes totally immobile. Stays frozen after battles. Cure: ICE HEAL.
- **PAR (Paralyze):** Pokémon moves might misfire. Stays paralyzed after battles. Cure: PARLYZ HEAL.

- **exploration_prioritizer_agent (Turn 621):** Suggested exploring the Pokémon Center warp (24,26) in Viridian City again, immediately after exiting it. Still unhelpful. (Attempt 2 of this type of failure).