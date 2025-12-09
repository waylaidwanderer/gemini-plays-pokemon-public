# LESSONS LEARNED

## Tool & Agent Management
- **Proactive Tool Testing:** I must test tools in their expected environments (e.g., a pathfinder on a water route) *before* relying on them for critical navigation to avoid mid-task failures.
- **Tool-Game Mechanic Parity:** Tools will fail catastrophically if their internal model of the game is inaccurate (e.g., not accounting for all traversable tile types like WATER, or not understanding a menu's structure). All tools must be designed with a perfect understanding of the game mechanics and UI they interact with.
- **UI Parser Integrity:** A tool's pathfinding logic can be correct, but will fail catastrophically if its UI parser is not robust. A parser must be anchored and use boundary detection (like the 'CANCEL' option) to avoid including non-selectable UI elements in its data. Feeding corrupt data (wrong list size, wrong indices) to a correct algorithm produces incorrect results.
- **Simplify, Don't Over-Engineer:** When a complex tool repeatedly fails debugging, replace it with a simpler, more robust version that accomplishes a smaller part of the task reliably. This avoids wasting turns on complex, buggy automation.
- **`advanced_route_planner` Behavior:** The tool correctly calculates paths that cross both land and water. However, it does not automate the transition. I must manually use SURF when the generated path moves from a land tile to an adjacent water tile. The tool's output is a set of coordinates; the method of traversal is my responsibility.

## Navigation & Exploration
- **Fly Map Navigation:** The Fly map is not a free-roam grid. It consists of fixed, sometimes non-intuitive paths between cities that may not follow the geographical layout of the world map.
- **Pathfinding & Moving NPCs:** The `advanced_route_planner` uses a static map snapshot. It cannot predict the movement of NPCs. For reliable pathfinding in areas with moving NPCs, use the `stun_npc` tool on the relevant NPC *before* calling the planner to ensure the generated path remains clear.
- **Trust Tools & Pivot:** When stuck in a navigational puzzle, I must trust my `advanced_route_planner`'s 'No path found' output. If a path is confirmed to be a dead end after multiple attempts, I must abandon that path and test a fundamentally different hypothesis (like descending to ascend differently), as recommended by the `puzzle_solver` agent, instead of repeating the failed strategy.

## Hypothesis Testing
- **Precise Test Execution:** When testing a hypothesis from an agent, I must follow the test plan precisely. Incomplete tests can lead to incorrect conclusions and wasted time.
- **Trust Tools & Pivot:** When stuck in a navigational puzzle, I must trust my `advanced_route_planner`'s 'No path found' output and my own analysis. If a path is confirmed to be a dead end after multiple attempts, I must abandon that path and test a fundamentally different hypothesis (like descending to ascend differently), as recommended by the puzzle_solver agent, instead of repeating the failed strategy.

# IMMEDIATE TASKS
- **Ecruteak Gym Warp Mapping:** After defeating the Gym Leader, I must systematically step on every single `PIT` tile in this gym. The system alert has confirmed they are warps. I will document the destination of each one with a `define_map_marker` call to ensure my map data is complete. This is a high-priority task to address the map hygiene critique.
- **Olivine Lighthouse 2F Warp Mapping:** Once accessible, investigate and mark the warps (pits) at (16, 13) and (17, 13).

# CRITICAL DIRECTIVE: ANTI-HALLUCINATION & POSITIONAL VERIFICATION PROTOCOL
- My memory is unreliable. The Game State Information is the absolute source of truth. I am forbidden from using knowledge from other games or previous playthroughs; all strategies MUST be derived from verified, in-game observations from the current session.
- **Before EVERY navigational action, goal setting, or use of a pathfinding tool:**
  1. I MUST verify my `current_map_id` and `current_position` from the Game State Information.
  2. If the goal involves a warp, I MUST verify its existence and coordinates in the `Game State Information -> Map Events -> Warps` list for the **current map** and that the tile has `is-warp="true"` in the map XML before planning a route to it. Never assume a map transition exists based on map shape or common game tropes.
- **After EVERY map transition, system warning, or unexpected event (e.g., phone call):**
  1. I MUST immediately re-verify my `current_map_id` and `current_position`.
  2. I MUST discard any previous plan based on a now-invalidated location and re-evaluate my next action from the correct state.
- Failure to adhere to this protocol is the root cause of all major strategic failures and wasted turns. Trusting my own memory leads to critical hallucinations.

# STRATEGIC PROTOCOL

## 1. Core Principles & Planning
- **Plan-Execute-Verify Cycle:** I must follow a strict cycle: 1) Consult my knowledge base (notepad, markers) before acting. 2) Execute a methodical plan. 3) Verify the outcome and update my knowledge base immediately.
- **Proactive Mindset:** I must anticipate future needs (HMs, items, levels) and proactively address them before they become blockers. When a plan is repeatedly interrupted by a variable (e.g., moving NPC), I must switch to a deterministic strategy (e.g., `stun_npc`) immediately.
- **Pre-Battle Level Assessment:** Before challenging a Gym Leader or other major opponent, assess the level gap. If my team is significantly lower-leveled (5+ levels), I must prioritize level grinding to a competitive level before attempting the battle. Rushing in under-leveled leads to wasted resources and time.

## 2. Navigation & Exploration
- **Systematic Exploration:** When in a new area, I MUST systematically explore every single reachable tile before exiting to avoid missing hidden paths. An area is NOT a 'dead end' if there are any reachable unseen tiles.
- **Obstacle Management:** All critical obstacles (blockers, required HMs) MUST be marked with '🚫' immediately upon discovery. When a path is repeatedly blocked by a moving NPC, use `stun_npc` immediately instead of retrying the same failed path.
- **Trust the Pathfinder:** If the `route_planner` returns 'No path found,' the root assumption about the map's geography or the destination's reachability is likely flawed. I must trust the tool's output and re-evaluate my understanding of the map instead of assuming the tool is broken.

## 3. Puzzle Solving & Logic
- **Challenge Root Assumptions:** When stuck in a puzzle loop, the root assumption is likely flawed. I must aggressively re-verify the foundational belief that led to the current strategy. Test all variables, even those that seem like hazards or dead ends (e.g., pits in a lighthouse).
- **Escalate to Puzzle Solver:** When stuck in a puzzle loop, especially one where I'm trapping myself, the root assumption about the solution's structure is likely wrong. I must escalate to the `puzzle_solver` agent to challenge my flawed hypotheses instead of repeating them.

## 4. NPC & Object Interaction
- **Interaction Pre-check:** Before pressing 'A', I must verify I am adjacent to and facing the target directly. Close all dialogue boxes before attempting to move.
- **Interaction Loop Protocol:** If an NPC interaction enters a repetitive loop (e.g., repeatedly opening a shop menu), repeating the same interaction is not the solution. I must break the loop by changing the context, such as leaving and re-entering the area or interacting with other objects/NPCs before returning.
- **Trust But Verify Dialogue:** Trust NPC guidance that opens up new paths (e.g., Gym Guide), but be skeptical of dialogue that claims a path is a dead end, especially if it contradicts physical evidence (like a sign). Always verify with my own exploration.

## 5. Tool & Agent Management
- **Tool Maintenance is Highest Priority:** If a tool fails, it MUST be fixed immediately, overriding any in-game action. Deferring a fix is a critical failure. After applying a fix, especially from an agent, the tool's functionality must be verified with a simple test case.
- **Trust Agent for Tool Repair:** Manual debugging of UI parsing tools has a high failure rate. When a UI automation tool fails, I must escalate to the `python_code_debugger` agent for a robust solution instead of attempting multiple manual fixes.
- **Robust UI Parsing:** UI automation tools MUST use robust, flexible parsing that can handle minor variations in text and spacing. Relying on exact string matches or flawed assumptions about UI structure (e.g., name and level on the same line) is a critical point of failure.
- **Verify Inputs and Context:** Before assuming a tool is broken, I must first verify that my inputs are valid and the tool's configuration (e.g., `is_surfing`) is correct for the current context. A 'No path found' result is often accurate data about the map, not a tool failure.
- **Tool Logic Must Mirror Game Mechanics:** A tool will fail if its internal model of the game is inaccurate (e.g., not accounting for the 'CANCEL' option in a circular menu). All future tools must be designed with a perfect understanding of the UI and mechanics they interact with.

# KNOWLEDGE BASE

## Game Systems & Mechanics
- **Day/Night Cycle:** An important mechanic, affecting events.
- **POKé BALLS:** Received 5 from the scientist in Elm's Lab. Can now catch wild Pokémon.
- **PC Storage:** Used for Pokémon and item storage in Pokémon Centers.
- **BERRY Trees:** Grow new BERRIES every day.
- **Healing:** Pokémon Centers restore all HP/PP and cure status conditions.
- **Game State Updates:** Map data (like a `CUT_TREE` changing to a `FLOOR`) doesn't fully update until all on-screen text is cleared. Using tools like `route_planner` before the overworld is fully interactive will use stale data and fail.
- **HEADBUTT Mechanic:** Can be used outside of battle on `HEADBUTT_TREE` tiles to encounter sleeping Pokémon.
- **Evolution Methods:** Some Pokémon (MACHOKE, KADABRA, HAUNTER, GRAVELer) evolve when traded.
- **`stun_npc` Mechanic:** The stun effect is very short-lived and resets when leaving and re-entering a map. The tool will also fail if the target NPC is not currently on-screen and rendered in the game.
- **Rematch Mechanic:** Some trainers will call for a rematch via the Pokégear. Interacting with them after a call will trigger a new battle. My previous assumption that trainers could only be fought once was incorrect.
- **Roaming Legendaries:** Encounters with Pokémon like Entei can be random. They may flee on the first turn, even if the player's attempt to run fails.
- **Verify Before Acting:** I must verify on-screen text and game state information *before* creating map markers or editing the notepad to prevent hallucinations and data errors. This is a critical check against my own faulty memory.
- **SURF Mechanic:** To use SURF, the player must be standing on a tile adjacent to water AND be facing the water tile. The game will NOT automatically turn the character.
- **Gift Pokémon Nicknaming:** Gift Pokémon may be automatically given a nickname by the game upon receipt. This was observed with the Shuckle received from the Rocker in ManiasHouse.
- **Marker Emoji Reliability:** Using complex or uncommon emojis for map markers can cause tool failures. Stick to simple, standard emojis (like arrows, checkmarks, etc.) to ensure reliability and avoid wasting turns on preventable errors.
- **HM Move Permanence:** HM moves cannot be forgotten by a Pokémon once they have been taught. This was confirmed when attempting to replace FLASH on Togetic.
- **Dialogue Loop Evasion:** If an NPC's dialogue repeatedly triggers and blocks progress, it's likely due to being in their line of sight. Instead of repeatedly trying to clear the dialogue, move out of the trigger zone to break the loop.
- **Verify Before Marking:** A critical error was creating numerous hallucinatory map markers based on faulty memory. I MUST verify the existence of an object or warp and its exact coordinates in the Game State Information *before* using `define_map_marker`.
- **STRENGTH HM Mechanic:** Using STRENGTH is a two-step process. First, the move must be selected from the Pokémon's menu while standing adjacent to a boulder to 'activate' the ability. Second, the player must then walk into the boulder to push it. Simply walking into it without prior activation does nothing.

## Tile & Object Mechanics
- **BOOKSHELF**: An impassable object.
- **BUOY**: An impassable object found in water, functions as a WALL tile within a WATER area.
- **CAVE**: A traversable warp tile that functions as an entrance to a cave.
- **COUNTER**: Impassable terrain, usually a barrier in front of an NPC. To interact with NPCs behind counters, face the counter tile directly in front of them and press A.
- **CUT_TREE**: An impassable tree that likely requires the HM move Cut to remove.
- **DOOR**: A traversable warp tile leading into or out of a building.
- **Ecruteak Gym Floor**: Appears as a PIT, but is a traversable FLOOR tile that forms an invisible path. The path is revealed by defeating trainers.
- **FENCE (Visual):** The fence-like structure on Route 38 at (30, 11) is functionally an impassable `WALL` tile.
- **FLOWER**: Fully traversable decorative tile.
- **FLOOR**: A standard, fully traversable tile.
- **FLOOR_UP_WALL**: Confirmed impassable from below and from the side. My tool's logic was based on the faulty assumption it was a one-way ledge, but in-game movement attempts to move DOWN onto this tile from an adjacent `FLOOR` tile and from the side have both failed. It should be treated as a solid wall until proven otherwise.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item when interacted with for the first time.
- **GRASS**: Fully traversable tile, similar to TALL_GRASS. Wild Pokémon can be encountered here.
- **HEADBUTT_TREE**: An interactable tree, requires the Headbutt move. Impassable.
- **INCENSE_BURNER**: An impassable decorative object.
- **Item Interaction:** The game requires a specific item type for some interactions. The sick Miltank needs a generic 'BERRY' and will not accept functionally similar but differently named items (e.g., 'MINT BERRY'). This was confirmed by the interaction prompt.
- **LADDER:** Can function as a standard traversable tile (e.g., on a pier) or a warp tile. Its function must be verified by checking for a <Warp> child element in the map XML. Activation methods are complex and context-dependent. Activation can be complex. Stepping onto a ladder tile from an adjacent `FLOOR_UP_WALL` tile above it has been confirmed to trigger the warp.
- **LEDGE_HOP_DOWN/LEFT/RIGHT**: One-way traversable tiles.
- **LONG_GRASS**: Fully traversable tile. Wild Pokémon can be encountered here.
- **MART_SHELF**: Impassable terrain, functions like a wall.
- **PC**: An interactable object used to access the Pokémon Storage System. Impassable.
- **PIT (Context-Dependent):** This tile's function varies by location.
  - **Olivine Lighthouse:** One-way warp downwards.
  - **Burned Tower:** Inactive puzzle element, requires an external trigger (defeating rival).
  - **Ecruteak Gym:** Confirmed to be one-way warps that send the player back to the gym entrance area.
- **PLANT**: A decorative object that functions as an impassable WALL tile.
- **RADIO**: An impassable object.
- **SIGN**: An impassable, interactable object. Functions as a wall.
- **STAIRCASE**: A traversable warp tile that moves the player between floors.
- **TALL_GRASS**: Fully traversable tile. Wild Pokémon can be encountered here.
- **TOWN_MAP**: An interactable object on a wall; impassable.
- **TV**: An impassable object.
- **unseen**: A tile that has not yet been explored. Its properties are unknown until visited. It is treated as impassable by pathfinding tools.
- **unknown**: A tile type whose properties have not yet been observed. It is treated as impassable by pathfinding tools until its true nature is revealed.
- **VOID**: An impassable tile type found at the edges of some maps, functions as a wall.
- **WALL**: An impassable tile that blocks movement.
- **WARP_CARPET_UP/DOWN/LEFT/RIGHT**: A warp tile at the edge of a map. The activation method is direction-specific. For a `WARP_CARPET_DOWN`, pressing 'Down' while standing on the tile has been confirmed to trigger the warp. Other directions are still under investigation.
- **Warp (FLOOR):** A special tile type that appears to be a normal FLOOR tile but also functions as a warp. Observed as landing zones after falling through a PIT.
- **Warp (WALL):** Observed in Burned Tower. Appears to be a WALL tile that also functions as a warp. Its activation method is currently unknown.
- **WATER**: Traversable using the HM move SURF.
- **WATERFALL:** Appears to be an impassable tile, similar to a WALL. Further investigation is needed to see if an HM is required to traverse it.
- **WHIRLPOOL**: An obstacle in the water. Traversability is currently unknown, but it likely requires a specific HM move to cross. Observed on Route 41 at (42, 24).
- **WINDOW**: An impassable object that can be interacted with to display text. Functions like a wall.
- **NPC Objects (TEACHER, LASS, etc.)**: These are impassable and function as walls.
- **Verify Interaction Methods:** Do not assume all objects of the same type (e.g., ladders) have the same activation method. If a simple interaction (step-on, 'A' press from adjacent tile) fails, the object may require a different, non-obvious trigger. Systematically test and document interaction attempts.

## Battle & Resource Management
- **Inventory Pre-check:** Before starting a resource-dependent task (like catching Pokémon), I must verify I have the necessary items (e.g., Poké Balls). Running out mid-task is a critical failure of preparation.
- **Blocked Movement vs. Battle Start:** A 'Movement Blocked' alert does not guarantee a wild battle has started. I must wait for the battle screen text to appear before assuming I am in a battle and pressing 'A' to advance dialogue. This prevents wasted turns from incorrect assumptions.
- **Struggle Mechanic Failure:** Repeatedly selecting a 0 PP move does not trigger Struggle in this game. If a Pokémon runs out of PP, the only viable options are to switch out or use an item. Do not get stuck in a loop trying to force Struggle.
- **Resource Management:** Avoid inefficient battles (e.g., against high-defense, low-EXP opponents) that drain PP for minimal gain. Running away is often the more strategic option to conserve resources for more important fights or exploration.
- **Type Disadvantage Switching:** When a Pokémon is facing an opponent with a significant type advantage (e.g., Rock/Ground vs. Fighting), switching out is not just an option, it's a critical necessity to avoid taking massive damage or being knocked out. Preserving HP is key.
- **Battle Interruption:** Battles, even with rival trainers, can be unexpectedly interrupted by in-game cutscenes or story events.
- Pokémon holding a BERRY can automatically use it to heal themselves when their HP gets low in battle.
- Poisoned Pokémon lose 1 HP every four steps outside of battle and remain poisoned after a wild battle concludes.
- Accuracy-lowering moves like SMOKESCREEN are not a guaranteed defense.
- The auto-activation threshold for a held BERRY is likely below 25% HP.
- A single high-level Pokémon cannot carry an entire under-leveled team through a major battle like a Gym.
- Levels Over Type Advantage: A significant level disparity can completely negate type advantages.
- Low-HP Threat: A low-HP Pokémon with a status move like Hypnosis is still a major threat.
- Type Immunity vs. Level Disparity: Type immunity is not a guaranteed defense against a much higher-level opponent.

## Type Effectiveness Chart (Verified)
| Attacking Type | Defending Type | Effectiveness |
| :--- | :--- | :--- |
| Grass | Fire | Not Very Effective |
| Normal | Ghost | No Effect |
| Normal | Rock | Not Very Effective |
| Flying | Rock | Not Very Effective |
| Fire | Rock | Not Very Effective |
| Ground | Flying | No Effect |
| Normal | Water/Rock | Not Very Effective |
| Rock | Flying | Super Effective |
| Rock | Bug | Super Effective |
| Water | Fire | Super Effective |
| Water | Rock | Super Effective |
| Water | Ground | Super Effective |
| Water | Water | Not Very Effective |
| Fighting | Rock | Super Effective |

## Menu Navigation
- For complex menu inputs (like on-screen keyboards), perform all directional movements in one turn and the final confirmation ('A' button) in the next.
- In the party screen, the 'SWITCH' option is used to reorder Pokémon. The 'MOVE' option is for reordering a Pokémon's moves.
- The main battle menu options are laid out in a 2x2 grid: FIGHT (top-left), PKMN (top-right), PACK (bottom-left), RUN (bottom-right).

## LORE & DIALOGUE
- **Hiker Anthony (Phone):** Confirmed that DUNSPARCE are found in DARK CAVE in large numbers, specifically in areas where there are no strong POKéMON.
- **POKEFAN_M in Violet City House:** Traded Pokémon grow quickly but may disobey without the correct Gym Badge.
- Received MIRACLE SEED from a trainer on Route 32.
- **FIREBREATHER WALT on Route 35:** Said "I'm practicing my fire breathing." despite appearing as a FISHER sprite. Likely a Fire-type trainer.
- A POKEFAN_M in the Game Corner lost his COIN CASE in the UNDERGROUND. This is likely required to play the games.
- **Route 34 Gatehouse:** A Lass at (3, 5) mentioned a shrine in Ilex Forest honoring a 'protector' that 'watches over the FOREST from across time' and is likely a Grass-type POKéMON.
- **POKEFAN_F in Bill's House (Goldenrod):** Her son, BILL, is an expert on Pokémon and is at the Pokémon Center in ECRUTEAK CITY. Her husband is at the GAME CORNER.
- **LASS on Goldenrod Dept. Store 5F:** A lady gives away TMs on Sundays.
- **Scientist in Ruins of Alph Research Center:** Confirmed that the appearance of Pokémon in the ruins is a recent and incredible discovery that needs investigation. The UNOWN Pokémon are very similar to the drawings on the walls of the ruins, implying there are many different kinds.
- **Computer in Ruins of Alph Research Center:** Displays 'RUINS OF ALPH Exploration Year 10'.
- **Bookshelf at (6, 5) in Ruins of Alph Research Center:** contains books titled "Ancient Ruins…" and "Mysteries of the Ancients…".
- **Youngster in Route 32 Gatehouse:** Mentioned trying to move the stone panels in the ruins, wondering what they are.
- **Officer in Route 32 Gatehouse:** Said "RUINS OF ALPH".
- **Route 32 Sign at (13, 5):** Reads 'ROUTE 32, VIOLET CITY - AZALEA TOWN'.
- **GRAMPS in Route 36 Gatehouse:** Mentioned the strange tree was the reason fewer people were visiting the RUINS OF ALPH.
- **FISHER on Ecruteak City (9, 22):** Heard a rumor that the Pokémon at the Olivine Lighthouse is sick.
- **Fisher in Olivine Pokémon Center:** A sailor in the Olivine Cafe next door can teach the move STRENGTH, which can move big boulders.
- **Teacher in Olivine Pokémon Center:** Mentioned a person in Cianwood City, across the sea, who has a rare POKéMON.
- **POKEFAN_F on OlivineLighthouse1F (16, 9):** Mentioned that in the past, Pokémon were used to light the sea at night, and the lighthouse was built in their honor.
- **Gentleman on OlivineLighthouse2F (17, 8):** The sick Pokémon at the top needs 'special medicine'.
- **COOLTRAINER_M in EcruteakItemfinderHouse:** Mentioned finding items in the BURNED TOWER.
- **COOLTRAINER_F in Ecruteak Pokémon Center:** "MORTY, the GYM LEADER, is soooo cool. His POKéMON are really tough too."
- **GYM_GUIDE in Ecruteak Pokémon Center:** Mentioned a 'GYARADOS swarm' at the 'LAKE OF RAGE' and a potential 'conspiracy'. This seems like a major plot point.

## KEY ITEMS & TMs
## Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.
- **HM01 CUT:** Obtained from the charcoal maker in Ilex Forest. Allows cutting small trees outside of battle. Requires the Hive Badge.
- **HM02 FLY:** Obtained from Chuck's wife in Cianwood City. Allows flying to previously visited towns.
- **PLAINBADGE:** From Whitney. Boosts POKéMON's Speed and allows the use of STRENGTH outside of battle.
- **STORMBADGE:** From Chuck. Makes all POKéMON up to L70 obey and enables the use of FLY outside of battle.

## TMs
- **TM01 DYNAMICPUNCH:** From Chuck. An inaccurate but powerful move that causes confusion when it hits.
- **TM12 SWEET Scent**
- **TM31 MUD-SLAP**
- **TM39 SWIFT**
- **TM45 ATTRACT**
- **TM49 FURY CUTTER**
- **TM08 ROCK SMASH:** Received from a man on Route 36 after a battle.

## Crafting
- Kurt in Azalea Town can make special POKé BALLS from APRICORNS. I received a LURE BALL from him as an example.

## Solved Puzzles
### Azalea Gym
- Gym Guide: The Gym Leader is BUGSY. His Bug POKéMON are weak to Fire and Flying-type moves.
- **Solution:** The gym puzzle involves finding two hidden floor switches. The first, located on the path to the right-side trainer, makes a new trainer appear on the left side. The second, on the path to the left-side trainer, makes another new trainer appear. The path to these trainers is not blocked by the Twins in the middle; it is possible to walk around the bottom of the gym. Defeating all trainers is not required to reach Bugsy.

### Goldenrod Department Store
- **Elevator:** The elevator is controlled by the panel at (3, 0). Interacting with the panel brings up a floor selection menu. After selecting a floor, you must walk onto the corresponding warp carpet to travel. The warp to B1F is at (1, 3) and the warp to 1F is at (2, 3).
- **B1F Box Puzzle:** My own movement is causing changes in the a map layout. A WALL at (5, 10) changed to a FLOOR after I moved. The Machop at (7, 7) is likely the key to solving the puzzle. The previous solution of leaving and returning the room seems to be only a partial trigger.

### Goldenrod Gym
- Gym Guide: This is a Normal-type gym. Fighting-type POKéMON are recommended.
- **Puzzle Mechanic:** The gym puzzle is solved by walking along the outer perimeter of the entrance room. The direction and sequence of these walks cause different trainers to appear and disappear, opening and closing paths. The correct sequence of perimeter walks and trainer battles is required to open the path to the main gym area.

### Goldenrod Underground Switch Room Puzzle
- **Failed Hypothesis:** The puzzle is solved by repeatedly entering and exiting the 'GoldenrodUndergroundSwitchRoomEntrances' area to cycle through different room configurations. (Failed after 5+ attempts, triggered a loop warning).
- **New Hypothesis:** The puzzle requires accessing the switch rooms from a different path. The main underground connects the north and south city entrances. I will re-enter the underground from the southern entrance in Goldenrod City and explore the lower level again, as my path was previously blocked and new events (Granny NPC) may have occurred.

### Ruins of Alph - Kabuto Chamber Puzzle
- **Clue:** "A POKéMON that hid on the sea floor. Eyes on its back scanned the area."
- **Solution:** The image is KABUTO.

### Olivine Lighthouse Puzzle
- **Root Cause Analysis:** My progress was catastrophically stalled by a single, flawed root hypothesis: "The way forward MUST be in the western section of the lighthouse." I failed to trust my `route_planner` tool, which repeatedly and correctly told me the western and eastern sections were disconnected on floors 3 and 4. Instead of trying to falsify my hypothesis (e.g., by immediately attempting a strategic retreat to a lower floor), I spent dozens of turns in a loop, trying to force a path that didn't exist. The western column is a confirmed dead-end loop.
- **Descending Path Fallacy:** Just because a path goes down (like a pit) does not mean it leads to progress. As seen in the Olivine Lighthouse, some descending paths are simply one-way exits or resets designed to force the player to restart the ascent. I must evaluate these paths critically and not assume they are the correct way forward.

### Moomoo Farm Puzzle Solution
- The sick Miltank needs to be fed 'lots o' BERRIES' to get better. This was confirmed by the farmer. The FRUIT_TREE at (9, 3) on Route 39 only gives a MINT BERRY and is not the solution.

### Burned Tower Puzzle
- **Puzzle Solution:** Defeating my rival, SILVER, on the first floor caused the floor to collapse, revealing the basement and the legendary beasts.

### Ecruteak Gym Puzzle
- **Agent Hypothesis #1 (Talk to Sage):** FAILED. Interacted with the Sage at (3, 13) after defeating Morty. The dialogue was generic and did not provide a clue or unblock the path.

### Cianwood Gym Boulder Puzzle Solution
- **Failed Hypothesis 1:** Push all boulders straight up. This blocks the path and creates a dead end.
- **Correct Solution:** The puzzle requires creating an empty space to maneuver the boulders. The correct sequence is:
  1. Push the leftmost boulder (3, 7) up to (3, 6).
  2. Push the middle boulder (4, 7) left into the now-empty space at (3, 7).
  3. Now that the central path is clear, the remaining boulders can be pushed up to reach the Gym Leader.

## Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.
- **Rival on Route 40:** Confirmed that interacting with SILVER on Route 40 after accepting Jasmine's quest does not trigger a battle or make him move. He remains a static blocker.
- **Route 42 Impasse:** All three Mt. Mortar entrances on Route 42 have been confirmed to be isolated dead ends from the west side. Surfing across the central lakes does not connect the western and eastern landmasses. The path is completely blocked. Do not attempt to cross Route 42 again until a new key item or story event provides a solution.
- A `CUT_TREE` at (24, 13) on Route 42 was identified as a potential obstacle. However, my `advanced_route_planner` confirmed the area is unreachable from the west side of the route.

## Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

## PC Inventory
- **Box 1:**
  - Hestia (MAGBY), Lv15, Female

## Rematch Opportunities
- Hiker Anthony on Route 33 called for a battle.
- Youngster Joey on Route 30 called for a rematch.
- Sailor Huey at the Olivine Lighthouse called for a rematch.

## Tools & Agents
### Built-in Tools
- `notepad_edit`
- `run_code`
- `define_agent`
- `delete_agent`
- `define_map_marker`
- `delete_map_marker`
- `stun_npc`
- `define_tool`
- `delete_tool`
- `select_battle_option`

### Custom Tools
- `advanced_route_planner`
- `find_adjacent_unseen`
- `select_item`
- `select_move`
- `switch_pokemon`

### Custom Agents
- `python_code_debugger`
- `puzzle_solver`

## Ongoing Investigations
### Cianwood Gym Puzzle
- **Hypothesis:** The gym puzzle involves moving boulders with STRENGTH to clear a path to the Gym Leader, Chuck. Some of the Black Belts in the gym are non-battling NPCs.
- **Teacher in CianwoodLugiaSpeechHouse:** Mentioned a mythical sea creature hiding in the four islands between Cianwood and Olivine.
- **Lass in CianwoodLugiaSpeechHouse:** Mentioned a creature that can only be seen if you have a SILVER WING.

### Cianwood Gym Puzzle Log
- **Hypothesis 1:** Push boulders by walking into them. **Result:** Failed. Character bumps into boulder without moving it.
- **Hypothesis 2:** Push boulders by pressing 'A' while facing them. **Result:** Failed. Displays generic text 'A POKéMON may be able to move this' but does not trigger the move.
- **New Hypothesis:** I must use the HM STRENGTH directly from the Pokémon party menu on the Pokémon that knows the move.
- **Training Efficiency:** If a grinding location consistently provides poor matchups or low EXP yield, it is a strategic failure to remain there. I must immediately pivot to a new location or a different training method (like finding un-battled trainers) to maintain efficiency. Battling trainers is far more efficient than grinding wild Pokémon.
- **JUGGLER IRWIN (Phone):** Called to congratulate me on defeating MORTY, even though I just defeated CHUCK. This is a strange inconsistency.

## Olivine City Gym Strategy
- **Gym Leader:** Jasmine
- **Known Information:** She was caring for a sick Ampharos (Electric-type), which implies she might use Electric or Steel types, given the lighthouse's theme. The gym is likely Steel-type, as Olivine is known for its steel.
- **Team Composition:**
  - VULCAN (Quilava): Fire-type moves will be super-effective against Steel.
  - CLAUDIUS (Krabby): Water-type moves are neutral, but STRENGTH is useful.
  - CRUNCH (Pinsir): Fighting-type moves (Seismic Toss) are super-effective against Steel.
  - JUBILEE (Togetic): Normal/Flying, likely weak to Steel/Rock moves. Should be used cautiously.
- **Plan:** Lead with VULCAN to deal heavy damage. Switch to CRUNCH if VULCAN is in trouble. Use CLAUDIUS as a backup. Avoid using JUBILEE unless necessary.

- **Re-evaluate Core Assumptions:** When multiple paths in a single area (like the three Mt. Mortar caves) all lead to dead ends, the fundamental assumption about needing to go through that area is likely wrong. I must broaden my search for alternatives instead of re-testing the same failed area.

## Olivine Lighthouse
- Jasmine disappeared after I moved onto the tile she was standing on at (8,9) on the 6th floor. This might be a scripted trigger.