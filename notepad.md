# Pokémon Yellow Legacy - Hard Mode Notes

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
- **Secondary:** Prepare for the Pewter City Gym battle (train Pikachu, potentially catch more Pokémon).
- **Tertiary:** Explore Pallet Town and Route 1 for items, trainers, and Pokémon.

## Strategy Notes & Lessons Learned
- **World Knowledge Graph (WKG):** Record transitions (map changes) immediately. `add_node` payload should NOT include an `id`. Use descriptive names and tags for nodes. Ensure `destination_entry_point` is accurate for warp edges.
- **Map Markers:** Mark used warps (entry/exit), defeated trainers, strategic points, interaction loops, dead ends, and static info signs. Use distinct emojis for clarity.
- **Interaction Strategy:** Avoid repeating interactions with objects/NPCs in confirmed loops without a new trigger. If an NPC or object is unresponsive or in a loop after 2-3 attempts, move on. Mark loops clearly.
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

## Type Matchup Discoveries
- Ghost-type > Psychic-type.
- Poison-type > Bug-type; Bug-type !> Poison-type.

## Defeated Trainers
(Format: [Trainer Name] - [Map Name] at (X,Y))

## Key Discoveries & Event Chronology
- **Player's House Second Floor (Map ID 38):** PC at (1,2).
- **Pallet Town (Map ID 0) - Initial Exploration:**
    - PALLETTOWN_PLAYERSHOUSE_SIGN at (4,6) interacted: "PLAYER's HOUSE".
    - PALLETTOWN_SIGN at (8,10) interacted: "PALLET TOWN - Shades of your journey await!".
    - Rival's House entrance (Warp): (14,6). Leads to Rival's House (Map ID 39).
    - Oak's Lab entrance (Warp): (13,12). Leads to Oak's Lab (Map ID 40).
- **Rival's House (Map ID 39):**
    - Spoke to Daisy at (3,4). She said BLAZe is at Grandpa's lab.
    - Obtained Town Map from Rival's House at (4,4) after talking to Daisy.
- **Player's House First Floor (Map ID 37):**
    - Mom (PLAYERSHOUSE1F_MOM) at (6,5) said: "Right. All kids leave home someday. It said so on TV. PROF.OAK, next door, is looking for you." (Key trigger for Oak's Lab event).
- **Oak's Lab (Map ID 40) - Pre-Starter Interactions & Loops:**
    - Scientist 1 (OAKSLAB_SCIENTIST1) at (3,11): Ghost > Psychic.
    - Girl (OAKSLAB_GIRL) at (2,10): Poison > Bug; Bug !> Poison.
    - Scientist 2 (OAKSLAB_SCIENTIST2) at (9,11): Repeated Ghost > Psychic.
    - Pokédexes at (3,2) & (4,2): "pages are blank!".
- **Pallet Town (Map ID 0) - Starter Event Trigger:**
    - Attempting to walk north into the grass at (11,1) (towards Route 1) triggered Professor Oak's appearance.
    - Oak's dialogue led to player following Oak into Oak's Lab.
- **Oak's Lab (Map ID 40) - Starter Pokémon Event:**
    - Prof. Oak at (6,3) after being followed into lab.
    - BLAZe at (5,4) tried to take the Pokémon at (8,4).
    - Oak offered player PIKACHU, which was received. Player named it SPARKY.
    - BLAZe has an EEVEE Lv5 (encountered in first battle).

## Future Agent Ideas
(None currently planned)

- **Oak's Lab (Map ID 40) - Post-Starter Events:**
    - Battled BLAZe in Oak's Lab. BLAZe has an EEVEE (Lv5).
    - SPARKY (Pikachu) defeated EEVEE and grew to Lv6.
    - SPARKY learned QUICK ATTACK.
    - Player received ¥175 for winning.
    - Professor Oak confirmed SPARKY dislikes Poké Balls and will follow the player outside.
    - Player can talk to SPARKY to check its mood.

## Pathing Lessons & Observations
- **Pikachu on Warp Tiles:** If Pikachu is standing on a warp tile, and I need to move onto that tile (e.g., to pass through or if it's on my direct path), I must be extremely careful. If I am not facing Pikachu, the first directional press towards Pikachu will only turn me. The second press will move me onto the tile. If that tile is a warp, I will warp. This means I need to plan routes around Pikachu if he's on a critical warp tile I don't want to use, or if the warp is my destination, account for the two-press interaction if not facing him. Repeatedly entering Oak's Lab from Pallet Town was due to this; Pikachu was on (13,12) which is the Lab warp, and my path from (13,13) involved stepping onto (13,12).

- **Route 1 (Map ID 12):**
    - Youngster at (6,26) is not a trainer. Gave player x1 Potion and mentioned Poké Marts sell Poké Balls. (Interacted at turn 397)

- SPARKY (Pikachu) defeated a wild Pidgey (Lv4) on Route 1 at (13,23). SPARKY gained 31 EXP (222 -> 253).

- SPARKY (Pikachu) defeated a wild Pidgey (Lv2) on Route 1 at (16,23). SPARKY gained 15 EXP (253 -> 268).

- SPARKY (Pikachu) defeated a wild Rattata (Lv2) on Route 1 at (14,26). SPARKY gained 16 EXP (268 -> 284).

- SPARKY (Pikachu) defeated a wild Pidgey (Lv3) on Route 1 at (13,25). SPARKY gained 23 EXP (284 -> 307).

- SPARKY (Pikachu) defeated a wild Pidgey (Lv3) on Route 1 at (15,23). SPARKY gained 23 EXP (307 -> 330).

## Future Agent Ideas (Post-Reflection Turn 461)
- **Exploration Prioritizer Agent:** To analyze `Reachable Unseen Tiles` and `Reachable Undiscovered Map Connections` to suggest optimal exploration targets.

- SPARKY (Pikachu) defeated a wild Pidgey (Lv3) on Route 1 at (14,25). SPARKY gained 23 EXP (330 -> 353) and grew to Lv7!

- SPARKY (Pikachu) defeated a wild Rattata (Lv3) on Route 1 at (13,23). SPARKY gained 24 EXP (353 -> 377).

## Defined Agents
- **route_pathfinder**: Calculates a sequence of moves (Up, Down, Left, Right) to navigate from a start coordinate to an end coordinate on the current map, considering obstacles. Uses `map_xml_string` for pathfinding. Input: {start_x, start_y, end_x, end_y}. Output: {path_found, steps[]}.

## Agent Usage & Failures
- **route_pathfinder (Turn 477):** Failed with error "Agent LLM resp missing content (Iter 1)" when trying to path from (14,21) to (17,14) on Route 1. Had to resort to manual path planning.

## Game Mechanics & Rules (Additions)
- **STAT Experience:** Pokémon gain increased stats from EXP that enemy trainers' Pokémon don't have. Training a Pokémon from a low level (e.g., Lv5 to Lv50) can result in stats comparable to a much higher level opponent (e.g., Lv60).

- SPARKY (Pikachu) defeated a wild Spearow (Lv5) on Route 1 at (17,10). SPARKY gained 41 EXP (401 -> 442).