# CRITICAL DIRECTIVES

## ANTI-HALLUCINATION & POSITIONAL VERIFICATION PROTOCOL
- My memory is unreliable. The Game State Information is the absolute source of truth. I am forbidden from using knowledge from other games or previous playthroughs; all strategies MUST be derived from verified, in-game observations from the current session.
- **Before EVERY navigational action, goal setting, or use of a pathing tool:**
  1. I MUST verify my `current_map_id` and `current_position` from the Game State Information.
  2. If the goal involves a warp, I MUST verify its existence and coordinates in the `Game State Information -> Map Events -> Warps` list for the **current map** and that the tile has `is-warp="true"` in the map XML before planning a route to it. Never assume a map transition exists based on map shape or common game tropes.
- **After EVERY map transition, system warning, or unexpected event (e.g., phone call):**
  1. I MUST immediately re-verify my `current_map_id` and `current_position`.
  2. I MUST discard any previous plan based on a now-invalidated location and re-evaluate my next action from the correct state.
- Failure to adhere to this protocol is the root cause of all major strategic failures and wasted turns. Trusting my own memory leads to critical hallucinations.

## STRATEGIC PROTOCOL
- **Plan-Execute-Verify Cycle:** I must follow a strict cycle: 1) Consult my knowledge base (notepad, markers) before acting. 2) Execute a methodical plan. 3) Verify the outcome and update my knowledge base immediately.
- **Proactive Mindset:** I must anticipate future needs (HMs, items, levels) and proactively address them before they become blockers. When a plan is repeatedly interrupted by a variable (e.g., moving NPC), I must switch to a deterministic strategy (e.g., `stun_npc`) immediately.
- **Pre-Battle Level Assessment:** Before challenging a Gym Leader or other major opponent, assess the level gap. If my team is significantly lower-leveled (5+ levels), I must prioritize level grinding to a competitive level before attempting the battle. Rushing in under-leveled leads to wasted resources and time.
- **Systematic Exploration:** When in a new area, I MUST systematically explore every single reachable tile before exiting to avoid missing hidden paths. An area is NOT a 'dead end' if there are any reachable unseen tiles.
- **Obstacle Management:** All critical obstacles (blockers, required HMs) MUST be marked with '🚫' immediately upon discovery. When a path is repeatedly blocked by a moving NPC, use `stun_npc` immediately instead of retrying the same failed path.
- **Escalate to Puzzle Solver:** When stuck in a puzzle loop, especially one where I'm trapping myself, the root assumption about the solution's structure is likely wrong. I must escalate to the `puzzle_solver` agent to challenge my flawed hypotheses instead of repeating them.
- **Re-evaluate Core Assumptions:** When multiple paths in a single area (like the three Mt. Mortar caves) all lead to dead ends, the fundamental assumption about needing to go through that area is likely wrong. I must broaden my search for alternatives instead of re-testing the same failed area.
- **Interaction Pre-check:** Before pressing 'A', I must verify I am adjacent to and facing the target directly. Close all dialogue boxes before attempting to move.
- **Interaction Loop Protocol:** If an NPC interaction enters a repetitive loop (e.g., repeatedly opening a shop menu), repeating the same interaction is not the solution. I must break the loop by changing the context, such as leaving and re-entering the area or interacting with other objects/NPCs before returning.
- **Trust But Verify Dialogue:** Trust NPC guidance that opens up new paths (e.g., Gym Guide), but be skeptical of dialogue that claims a path is a dead end, especially if it contradicts physical evidence (like a sign). Always verify with my own exploration.
- **Tool Maintenance is Highest Priority:** If a tool fails, it MUST be fixed immediately, overriding any in-game action. Deferring a fix is a critical failure. After applying a fix, especially from an agent, the tool's functionality must be verified with a simple test case.

# KNOWLEDGE BASE

## Game Systems & Mechanics
- **Day/Night Cycle:** An important mechanic, affecting events.
- **POKé BALLS:** Received 5 from the scientist in Elm's Lab. Can now catch wild Pokémon.
- **PC Storage:** Used for Pokémon and item storage in Pokémon Centers.
- **BERRY Trees:** Grow new BERRIES every day.
- **Healing:** Pokémon Centers restore all HP/PP and cure status conditions.
- **Game State Updates:** Map data (like a `CUT_TREE` changing to a `FLOOR`) doesn't fully update until all on-screen text is cleared. Using tools before the overworld is fully interactive will use stale data and fail.
- **HEADBUTT Mechanic:** Can be used outside of battle on `HEADBUTT_TREE` tiles to encounter sleeping Pokémon.
- **Evolution Methods:** Some Pokémon (MACHOKE, KADABRA, HAUNTER, GRAVELer) evolve when traded.
- **`stun_npc` Mechanic:** The stun effect is very short-lived and resets when leaving and re-entering a map. The tool will also fail if the target NPC is not currently on-screen and rendered in the game.
- **Rematch Mechanic:** Some trainers will call for a rematch via the Pokégear. It has been observed that some trainers, like Sailor Huey and Hiker Anthony, can be battled again even without a new call, suggesting some rematches may be repeatable. My previous assumption that trainers could only be fought once was incorrect.
- **Roaming Legendaries:** Encounters with Pokémon like Entei can be random. They may flee on the first turn, even if the player's attempt to run fails.
- **Verify Before Acting:** I must verify on-screen text and game state information *before* creating map markers or editing the notepad to prevent hallucinations and data errors. This is a critical check against my own faulty memory.
- **SURF Mechanic:** To use SURF, the player must be standing on a valid tile (e.g., FLOOR) adjacent to water, face the water tile, and then manually select SURF from the Pokémon's party menu.
- **Gift Pokémon Nicknaming:** Gift Pokémon may be automatically given a nickname by the game upon receipt. This was observed with the Shuckle received from the Rocker in ManiasHouse.
- **Marker Emoji Reliability:** Using complex or uncommon emojis for map markers can cause tool failures. Stick to simple, standard emojis (like arrows, checkmarks, etc.) to ensure reliability and avoid wasting turns on preventable errors.
- **HM Move Permanence:** HM moves cannot be forgotten by a Pokémon once they have been taught. This was confirmed when attempting to replace FLASH on Togetic.
- **Dialogue Loop Evasion:** If an NPC's dialogue repeatedly triggers and blocks progress, it's likely due to being in their line of sight. Instead of repeatedly trying to clear the dialogue, move out of the trigger zone to break the loop.
- **Verify Before Marking:** A critical error was creating numerous hallucinatory map markers based on faulty memory. I MUST verify the existence of an object or warp and its exact coordinates in the Game State Information *before* using `define_map_marker`.
- **STRENGTH HM Mechanic:** Using STRENGTH is a two-step process. First, the move must be selected from the Pokémon's menu while standing adjacent to a boulder to 'activate' the ability. Second, the player must then walk into the boulder to push it. Simply walking into it without prior activation does nothing.

## TILE & OBJECT MECHANICS (CONSOLIDATED)
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
- **FLOOR_UP_WALL**: Confirmed to be a one-way ledge. It is impassable from below, but can be jumped down from. It is also impossible to move DOWN onto it from an adjacent FLOOR tile.
- **FRUIT_TREE**: An impassable, interactable object. Gives one BERRY item when interacted with for the first time.
- **GRASS**: Fully traversable tile, similar to TALL_GRASS. Wild Pokémon can be encountered here.
- **HEADBUTT_TREE**: An interactable tree, requires the Headbutt move. Impassable.
- **INCENSE_BURNER**: An impassable decorative object.
- **Item Interaction:** The game requires a specific item type for some interactions. The sick Miltank needs a generic 'BERRY' and will not accept functionally similar but differently named items (e.g., 'MINT BERRY'). This was confirmed by the interaction prompt.
- **LADDER:** A warp tile. Stepping onto a LADDER tile from an adjacent FLOOR tile has been confirmed to trigger the warp, moving the player between floors. This works for both ascending and descending.
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
- **WARP_CARPET_DOWN**: A warp tile at the edge of a map. Pressing 'Down' while standing on the tile has been confirmed to trigger the warp.
- **WARP_CARPET_RIGHT**: A warp tile at the edge of a map. Pressing 'Right' while standing on the tile has been confirmed to trigger the warp.
- **WARP_CARPET_LEFT**: A warp tile at the edge of a map. Pressing 'Left' while standing on the tile has been confirmed to trigger the warp.
- **Warp (FLOOR):** A special tile type that appears to be a normal FLOOR tile but also functions as a warp. Observed as landing zones after falling through a PIT.
- **Warp (WALL):** Observed in Burned Tower. Appears to be a WALL tile that also functions as a warp. Its activation method is currently unknown.
- **WATER**: Traversable using the HM move SURF. To initiate surfing, the player must be standing on a tile adjacent to the water, face the water tile, and then manually select SURF from the Pokémon's party menu.
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
- **Route 34 Gatehouse:** A Lass at (3, 5) mentioned a shrine in Ilex Forest honoring a 'protector' that 'watches over the FOREST from across time' and is likely a Grass-type POKéMON.

## KEY ITEMS & TMs
### Key Items
- **HIVEBADGE:** From Bugsy. Allows traded POKéMON up to L30 to obey and enables the use of CUT outside of battle.
- **POKéDEX:** A high-tech encyclopedia from PROF. OAK to record POKéMON data.
- **HM05 FLASH:** Obtained from the Elder of Sprout Tower. Illuminates dark caves. Requires the Zephyr Badge to use outside of battle.
- **HM01 CUT:** Obtained from the charcoal maker in Ilex Forest. Allows cutting small trees outside of battle. Requires the Hive Badge.
- **HM02 FLY:** Obtained from Chuck's wife in Cianwood City. Allows flying to previously visited towns.
- **PLAINBADGE:** From Whitney. Boosts POKéMON's Speed and allows the use of STRENGTH outside of battle.
- **STORMBADGE:** From Chuck. Makes all POKéMON up to L70 obey and enables the use of FLY outside of battle.

### TMs
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
- **Solution:** The gym puzzle involves finding two hidden floor switches. The first, located on the path to the right-side trainer, makes a new trainer appear on the left side. The second, on the path to the left-side trainer, makes another new trainer appear. The path to these trainers is not blocked by the Twins in the middle; it is possible to walk around the bottom of the gym. Defeating all trainers is not required to reach Bugsy.

### Goldenrod Department Store
- **Solution:** The elevator is controlled by the panel at (3, 0). Interacting with the panel brings up a floor selection menu. After selecting a floor, you must walk onto the corresponding warp carpet to travel. The warp to B1F is at (1, 3) and the warp to 1F is at (2, 3).

### Goldenrod Gym
- **Solution:** The gym puzzle is solved by walking along the outer perimeter of the entrance room. The direction and sequence of these walks cause different trainers to appear and disappear, opening and closing paths. The correct sequence of perimeter walks and trainer battles is required to open the path to the main gym area.

### Goldenrod Underground Switch Room Puzzle
- **Solution:** The puzzle requires accessing the switch rooms from a different path. The main underground connects the north and south city entrances. Re-entering the underground from the southern entrance in Goldenrod City and exploring the lower level again, after triggering the Granny NPC event, is the correct path.

### Ruins of Alph - Kabuto Chamber Puzzle
- **Solution:** The image is KABUTO. The clue was "A POKéMON that hid on the sea floor. Eyes on its back scanned the area."

### Olivine Lighthouse Puzzle
- **Solution:** The entire western ascent route is a red herring. Progress must be made by accessing the eastern column of the lighthouse. The correct path involves strategically falling through pits on the eastern side of the upper floors to access ladders on the western side of the lower floors.

### Moomoo Farm Puzzle Solution
- **Solution:** The sick Miltank needs to be fed 'lots o' BERRIES' to get better. The FRUIT_TREE on Route 39 is not the solution; multiple berries must be acquired and fed to it.

### Burned Tower Puzzle
- **Solution:** Defeating the rival, SILVER, on the first floor caused the floor to collapse, revealing the basement and the legendary beasts.

### Cianwood Gym Boulder Puzzle Solution
- **Solution:** The puzzle requires creating an empty space to maneuver the boulders. The correct sequence is: 1. Push the leftmost boulder (3, 7) up to (3, 6). 2. Push the middle boulder (4, 7) left into the now-empty space at (3, 7). 3. Now that the central path is clear, the remaining boulders can be pushed up to reach the Gym Leader.

## Obstacles and Solutions
- A strange tree blocks the road north of Goldenrod City (Route 35). It can be cleared using a SQUIRTBOTTLE, which is obtained from the Flower Shop after defeating Whitney. The Lass in the shop confirms this is the correct sequence of events.
- **Rival on Route 40:** Confirmed that interacting with SILVER on Route 40 after accepting Jasmine's quest does not trigger a battle or make him move. He remains a static blocker.
- **Route 42 Impasse:** All three Mt. Mortar entrances on Route 42 have been confirmed to be isolated dead ends from the west side. Surfing across the central lakes does not connect the western and eastern landmasses. The path to the east and the Lake of Rage is completely blocked from Ecruteak City. Do not attempt to cross Route 42 again until a new key item or story event provides a solution.
- A `CUT_TREE` at (24, 13) on Route 42 was identified as a potential obstacle. However, my exploration confirmed the area is unreachable from the west side of the route.

## Held Items
- **QUICK CLAW:** Received from a Teacher in the National Park. When held by a Pokémon, it may allow them to attack first in battle.

## PC Inventory
- **Box 1:** (Empty)
- **Box 2:** (Empty)
- **Box 3:** (Empty)
- **Box 4:**
  - M (CATERPIE), Lv15, Female
  - WEAVER (SPINARAK), Lv14, Male
  - CHRONO (HOOTHOOT), Lv16, Male
  - GIB RALTAR (GRAVELER), Lv37, Female
  - SHUCKIE (SHUCKLE), Lv15, Female

## Rematch Opportunities
- Hiker Anthony on Route 33 called for a battle.
- Youngster Joey on Route 30 called for a rematch.
- Sailor Huey at the Olivine Lighthouse called for a rematch (multiple calls).

# TOOLS & AGENTS
## Available Tools & Agents
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
- `select_item`
- `select_move`
- `switch_pokemon`
- `find_path_bfs`

### Custom Agents
- `python_code_debugger`
- `puzzle_solver`

## Tool Ideas
- **`use_hm_move` tool:** A tool to automate using an HM from the party menu (e.g., CUT, STRENGTH, FLASH). This would prevent manual menuing errors.
- **`systematic_area_checker` tool:** A tool that, when in a confined area, generates a path to visit every single reachable tile and presses 'A' on each to search for hidden items or switches. This would automate tedious brute-force searches.

# LESSONS LEARNED (CONSOLIDATED)
- **Tool Verification is Mandatory:** A critical hallucination occurred where I believed a custom tool existed when it did not. I MUST verify the existence of any custom tool by checking the provided `Available Tools` list before documenting or attempting to use it. Relying on memory is a critical failure.
- **Challenge Root Assumptions:** When stuck in a puzzle loop, the root assumption is likely flawed. I must aggressively re-verify the foundational belief that led to the current strategy, using the `puzzle_solver` agent if necessary.
- **Use `stun_npc` Proactively:** When a path is repeatedly blocked by a moving NPC, I must use the `stun_npc` tool immediately instead of wasting turns recalculating paths. A deterministic strategy is superior to repeated failed attempts with a probabilistic one.
- **Fly Map Navigation:** The Fly map is not a free-roam grid. It consists of fixed, non-intuitive paths between cities.
- **Positional Verification is Non-Negotiable:** My memory is unreliable. I MUST verify my `current_map_id` and `current_position` from the Game State Information after EVERY map transition. Failure to do so leads to catastrophic hallucinations and wasted turns.
- **Multi-Level Puzzle Logic:** When all paths on a single map level are confirmed dead ends, the solution likely involves vertical movement (other floors) or an external event trigger outside the current map. Do not remain stuck on a single-floor hypothesis.
- **Procedural Adherence:** When a documented procedure for a complex mechanic (like using an HM) exists in the notepad, I must follow it exactly instead of attempting unverified shortcuts.
- **Re-evaluate Core Assumptions:** When a documented mechanic (like using STRENGTH) fails to solve an apparent puzzle, the root assumption that it *is* the puzzle is likely flawed. The obstacle may be a distraction. Instead of repeating the failed action, I must immediately pivot to exploring alternate paths or re-evaluating the fundamental goal.
- **Perception Error:** I must be wary of perception errors, such as assuming a path is only one tile wide when it is wider. Before concluding a path is blocked, I must test adjacent tiles.
- **Exhaust Simple Solutions First:** My fixation on using SURF to cross the Slowpoke Well was a false constraint. It caused me to ignore a simple, valid land route. When a path seems blocked, I must exhaust all simple, alternative land routes before attempting complex solutions involving HMs.
- **Trust Tool Outputs Over Critiques:** If a tool like `notepad_edit` fails because text isn't found, it means the critique's premise was likely based on a hallucination. Verify the source of truth (the tool's output) before attempting a fix based on a critique's claim.
- **Automate Error-Prone Tasks:** When a manual process like path planning repeatedly fails due to simple errors, the correct response is to create a tool to automate validation and prevent future mistakes. Relying on flawed manual attempts is inefficient.
- **Tool Logic Must Mirror Game Mechanics:** A tool will fail if its internal model of the game is inaccurate. All future tools must be designed with a perfect understanding of the UI and mechanics they interact with.
- **Tool Logic Must Handle State Transitions:** My `path_planner` tool failed because it couldn't calculate a path from a water tile to a land tile. This is a critical logic flaw. Tools that automate movement must be able to handle transitions between different movement states (e.g., surfing to walking) by finding the nearest valid transition point and planning the path in segments.
- **Navigation Failure implies Puzzle:** When both automated (tools) and manual pathing attempts repeatedly fail in a small, seemingly simple area, the root cause is likely a misunderstanding of a puzzle, not a pathing error. I must pivot from trying to navigate to trying to solve the underlying puzzle.
- **Plan Shorter Manual Paths:** When navigating manually, especially in complex or unfamiliar areas, plan short, simple paths of only a few steps at a time. This reduces the chance of making a planning error and running into a wall, which wastes turns.

# IMMEDIATE TASKS
- **Ecruteak Gym Warp Mapping:** After defeating the Gym Leader, I must systematically step on every single `PIT` tile in this gym. The system alert has confirmed they are warps. I will document the destination of each one with a `define_map_marker` call to ensure my map data is complete. This is a high-priority task to address the map hygiene critique.
- **Olivine Lighthouse 2F Warp Mapping:** Once accessible, investigate and mark the warps (pits) at (16, 13) and (17, 13).

# ONGOING INVESTIGATIONS
- **JUGGLER IRWIN (Phone):** Called to congratulate me on defeating MORTY, even though I just defeated CHUCK. This is a strange inconsistency.
- **JUGGLER IRWIN (Phone):** Called to congratulate me on saving the POKéMON at the LIGHTHOUSE, even though I haven't done it yet. This is a strange inconsistency.
- **Mt. Mortar Dead Ends:** All three entrances on Route 42 lead to dead ends from the west. The area is currently impassable.
- **Silver Wing:** A Lass in the house at Cianwood (15, 37) mentioned a SILVER WING is needed to see a mythical sea creature. This item apparently has the same 'scent' as the creature.
- **GYM_GUIDE in Ecruteak Pokémon Center:** Mentioned a 'GYARADOS swarm' at the 'LAKE OF RAGE' and a potential 'conspiracy'. This seems like a major plot point.
- **Challenge False Constraints:** My belief that I was trapped in the Slowpoke Well was a false constraint born from repeated navigation failures. When a situation seems impossible (like being soft-locked), the root hypothesis is flawed. I must trust my tools when they report a path is blocked and aggressively re-evaluate the puzzle's premise instead of brute-forcing a solution based on a wrong assumption.
- **Tool Logic Must Handle State Transitions:** My `path_planner` tool failed because it couldn't calculate a path from a water tile to a land tile. This is a critical logic flaw. Tools that automate movement must be able to handle transitions between different movement states (e.g., surfing to walking) by finding the nearest valid transition point and planning the path in segments.
- **`find_path_bfs` Limitation:** The tool cannot generate a single path that requires a state change (e.g., walking to surfing). It will create an invalid path that tries to walk on water. Paths requiring HMs must be manually executed in segments: 1) Path to the HM usage point. 2) Use the HM. 3) Path from the new position to the destination.

## Slowpoke Well B2F Puzzle
- **Hypothesis 1 (Failed):** A hidden switch exists on the central island. **Test:** Systematically pressed 'A' on every tile of the island. **Conclusion:** No switch was found. This hypothesis is disproven.
- **`find_path_bfs` Limitation:** The tool cannot generate a single path that requires a state change (e.g., walking to surfing). It will create an invalid path that tries to walk on water. Paths requiring HMs must be manually executed in segments: 1) Path to the HM usage point. 2) Use the HM. 3) Path from the new position to the destination.
## Slowpoke Well B2F Puzzle
- **Hypothesis 1 (Failed):** A hidden pressure plate exists on the island floor. **Test:** Systematically walked over every single floor tile. **Conclusion:** No trigger activated. This hypothesis is disproven.
## LESSONS LEARNED
- **`find_path_bfs` Limitation:** The tool cannot generate a single path that requires a state change (e.g., walking to surfing). It will create an invalid path that tries to walk on water. Paths requiring HMs must be manually executed in segments: 1) Path to the HM usage point. 2) Use the HM. 3) Path from the new position to the destination.