# I. Core Directives & Lessons Learned
## A. Core Directives
- D1: IMMEDIATE DATA & TOOL MANAGEMENT: All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified. Deferring these actions is a critical failure.
- D2: ACT ON DOCUMENTATION: A documented lesson that does not result in a behavioral change is a critical failure.
- D3: ABANDON FAILED HYPOTHESES: If a strategy fails repeatedly, I must recognize the pattern, document it with attempt counts, and pivot to a new approach.
- D4: TRUST, BUT REFINE: I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
- D5: PROACTIVELY AUTOMATE: Before performing any complex or repetitive task, I must first consider if it can be automated with a tool or agent.
## B. Key Lessons Learned
- Confirmation Bias Kills Progress: My manual assessment of map connectivity and partitioning is highly unreliable. I MUST trust my `map_analyzer` tool and system warnings over my own intuition. Repeatedly attempting to path to unreachable locations or believing I am trapped are critical failures.
- Escape is Not Guaranteed (CRITICAL LESSON): I incorrectly assumed fleeing from wild battles was always possible. The DODRIO in Cerulean Cave proved this wrong by preventing escape, leading to a party wipe. I must not rely on running as a guaranteed safe option, especially when at low health.
- Tool Maintenance is NOT a 'Task': Listing tool repair as a 'to-do' item is a form of procrastination and a violation of D1.
- Dead End Validation Failure (Turn 190005): I incorrectly assessed Cerulean Mart as not a dead end. A map with only one exit (a single warp, warp group, or map connection) and zero reachable unseen tiles IS a dead end. This is a critical rule for the `is_in_dead_end_area` validation check that I must follow precisely.

# II. Game & World Mechanics
## A. Map Marker System
- `🚪 Used Warp`: For any warp that has been traversed.
- `☠️ Defeated Trainer`: For any trainer that has been battled.
- `✅ Item Picked Up`: For any overworld item that has been collected.
- `🚫 Dead End`: For paths that have been confirmed to lead nowhere.
- `🗝️ Puzzle Solved/Obstacle Cleared`: For puzzles or obstacles that have been overcome.
- `💬 Non-Battling NPC`: For NPCs that have been confirmed to not engage in battle.
- `💖 Healing Zone`: For tiles that provide party healing.
- `➡️ Arrival Point`: For the tile where I arrive on a new map after a transition.
## B. Tile Traversal & Movement Rules
- `elevated_ground` & `steps`: Movement between `ground` and `elevated_ground` is only possible via a `steps` tile.
- Ladders & Elevation: Movement between a `ladder_up`/`ladder_down` tile and an adjacent `elevated_ground` tile is possible.
- `teleport`: Instant warp tile within the same logical location.
- `spinner_up/down/left/right`: Forces movement in a specific direction.
- `boulder_switch`: Floor switch activated by a boulder.
- FLY HM: Cannot be used indoors or in caves to escape.
- SURF HM: Requires a conscious (non-fainted) Pokémon that knows Surf to be used in the overworld.
## C. Special Mechanics & Discoveries
- Menu Input Blocking (CRITICAL): Facing an impassable tile blocks that directional input in menus. This makes any menu navigation tool that relies on fixed directional inputs fundamentally unreliable unless the player is in an open space.
- HM Usage: Must be adjacent to and facing the target object before opening the party menu.
- Boulder Pushing: A multi-turn action. Cannot be done while surfing.
- Dead End Definition (Correction): A map is only a dead end if it has only one exit warp/connection and no reachable unseen tiles. The nature of the destination map is irrelevant to this classification.
- SURF vs. DIG: The move SURF will miss an opponent that is underground from using DIG.
- Healing Zone: A tile described as a "purified, protected zone" that fully heals all Pokémon in the party's HP and restores all their PP. Found on Pokémon Tower 5F.
- Respawning Obstacles: Cuttable trees respawn after a certain amount of time or after changing maps, as observed with the tree at Cerulean City (20, 29).
- Proactive Tile Testing: I need to be diligent in testing tiles that appear impassable (like small fences or rocks) to confirm their properties, as ROM hacks can have unusual traversal rules.
## D. Inventory Management (CRITICAL LESSON)
- Inventory Over-Capacity: If the inventory count is over the maximum (e.g., 21/20), the displayed item list may be truncated. Tossing an entire stack of an item successfully frees up a slot, bringing the count back to the maximum. Discarding a partial stack does NOT free up an inventory slot.
## E. Type Effectiveness & Insights
- Electric is not very effective against Electric-types.
- Electric is not very effective against Grass/Poison dual-types.
- Wild Pokémon Speed (Cerulean Cave): Wild Pokémon are deceptively fast.
- Wild Pokémon Moves (Cerulean Cave): GOLEM can use SELFDESTRUCT and EXPLOSION. Both moves are not very effective against Rock/Ground types, as confirmed in multiple battles. SELFDESTRUCT is neutrally effective vs. Ground-types.
- Type Immunity: Electric moves have no effect on Ground-types.
- Poison is not very effective against Ground-types.
## F. Known Pokemon Locations
- Cerulean Cave: Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL, GOLBAT, KADABRA.
- Pokémon Tower: GASTLY, CUBONE.
## G. Navigational Lessons & Discoveries
- Dead End Definition (Correction): A 'dead end area' assessment applies to the *entire map's* reachable exits. An isolated section is not a dead end if other exits exist elsewhere on the map, even if currently unreachable.
- Warp Reachability (Correction): A warp being listed in `Map Events` does not guarantee it is reachable from the current position. The map is often partitioned.
- Self-Assessment Insights (Turn 188789): Wasted time exploring rivers in Cerulean City/Route 24. Should have used a data-driven tool like `map_analyzer` sooner to confirm it was a dead end.
- Functional Dead Ends: An area may be reported as not a dead end by the system if a path exists that requires a specific HM (like Surf). However, if the Pokémon with that HM is fainted, the area becomes a 'functional dead end' from a practical standpoint, requiring backtracking.
## H. Unexplained Phenomena
- 'Unaffected' Battle Message: During a battle with a wild RHYDON, after using EARTHQUAKE, the message 'REVENANT is unaffected!' appeared. My Pokémon took no damage and received no status. The cause is unknown. I need to monitor if this happens again.

# III. Active Puzzles & Navigation Strategy
## A. Pokémon Tower 7F (Dead End Puzzle)
- Observation: Reached the top floor (7F) of the Pokémon Tower. The path is a confirmed dead end with no visible exits or interactable objects.
- Hypothesis 1 (Failed - 15+ attempts): Interacting with Pikachu or the environment would trigger a cutscene. Conclusion: This was a severe case of Confirmation Bias. Standard interaction is not the solution.
- Hypothesis 2 (Failed - Agent Suggestion): Use the POKé FLUTE at the northernmost point (12, 3) to trigger a spectral event. Result: The game displayed text confirming the flute was played, but no event occurred. Conclusion: The POKé FLUTE has no special effect on this floor.
- Hypothesis 3 (Failed - 1 attempt): Use the SILPH SCOPE from the item menu at (12, 3). Result: The game displayed the message "This isn't the time to use that!", preventing its use. Conclusion: The item cannot be actively used from a distance.
- Hypothesis 4 (Failed - 1 attempt): The SILPH SCOPE's effect is passive. Its presence in the inventory will automatically trigger an event by walking into the entity at (10, 16). Result: Movement was blocked. Conclusion: The item's effect is not passive in this manner.
- Hypothesis 5 (Failed - 1 attempt): Actively use the SILPH SCOPE from the item menu while standing adjacent to the invisible entity at (10, 16). Result: The game displayed the message "This isn't the time to use that!", preventing its use. Conclusion: Actively using the SILPH SCOPE from the menu is not the solution.
- Hypothesis 6 (Failed - 1 attempt): Register the SILPH SCOPE to the SELECT button, then press SELECT while adjacent to the entity at (10, 16). Result: The item sub-menu does not have a "REGISTER" option, only "USE", "INFO", and "TOSS". Conclusion: This method of interaction is not possible.

# IV. Solved Puzzles & Mechanics Reference
## A. Silph Co. Puzzles
- Gate Mechanic: Standing adjacent to a closed gate and pressing 'A' automatically uses the CARD KEY to open it.
- Elevator: A two-step process. First, interact with the control panel to select a floor. Second, walk onto a warp pad and press 'Down' to travel.
## B. Snorlax Puzzle (Route 12)
- The item menu is a single, scrollable list. After selecting 'ITEM' from the main menu, scroll down past the HMs (indicated by a '↓' arrow) to find Key Items like the POKé FLUTE. Using it from this menu wakes the Snorlax.
## C. Boulder Puzzle Mechanics
- Objective: Boulders are often pushed into holes to block water currents on lower floors.
- Movement: Pushing is a multi-turn action. Must be adjacent. First press turns/pushes. Subsequent pushes require moving to the new adjacent tile first.
- Surfing Limitation: Cannot push boulders while surfing (confirmed on Seafoam Islands B3F).
## D. Navigation Puzzles
- Cerulean City River: The city is divided by a river. The western section (where you arrive from Route 4) and the eastern section (where the path to Route 9 is) are separated. To cross between them, I must use Surf.
- Mt. Moon Entrances: There are two entrances to Mt. Moon from Route 4. The western entrance at (19, 6) leads to an isolated, dead-end section. The eastern entrance at (25, 6) leads to the main cave system and the path forward to Cerulean City.
## E. Item & Store Data
### Item Locations & Vendors
- Route 12 Super Rod House: Fishing Guru gives the SUPER ROD.
### Celadon Department Store (Reference)
- 5F: Sells TMs (WATRGUN, PAYDAY, SMCTOSS, TELEPRT) and stat-boosters (HP UP, PROTEIN, etc.).
- 4F: Sells POKé DOLL and evolution stones (FIRE, THUNDER, WATER).
- 2F: Sells POKé BALLs, Potions, and TMs (MEGPNCH, RZRWIND, etc.).

# V. Agent & Tool Development History
## A. Retired Concepts & Tools
- `use_hm_from_party`, `switch_pokemon_navigator`, `menu_navigator`: These tools are retired due to fundamental flaws related to non-deterministic menu cursor positions and the 'Menu Input Blocking' mechanic. They serve as a critical lesson that menu automation requires environment-aware parsing (`menu_analyzer`) and targeted selection (`select_menu_option`), not blind input sequences.
## B. Key Development Lessons
- `select_pokemon_from_party` Critical Failure (Turns 189613-189620): The tool repeatedly failed to parse the multi-line party menu, causing incorrect Pokémon selections even after multiple fix attempts. The current implementation is fundamentally flawed. Conclusion: Manual selection is required until a complete redesign and robust testing can be performed in a safe environment.
- `use_hm_from_party` Manual Test (Cut): Discovered player must be facing the target *before* opening the menu.
- Snorlax Puzzle (Route 12): Confirmed item menu is a single scrollable list, not pocketed.
- Menu Cursor Behavior (Critical Lesson): Menu cursor starting positions are non-deterministic. Tools must force a known state (e.g., by spamming 'Up') rather than assuming a start position.
- Sequential Tool Call Failure: Calling multiple menu-altering tools in the same turn is unreliable. Only one should be called per turn.
- Decoy Entrances: Be wary of entrances that lead to isolated areas (e.g., Cerulean Cave's fake entrance).
## C. Tool Malfunctions & Bugs
- `find_path` Failure (Route 7): The tool is currently bugged on Route 7 (ID 18). It incorrectly reports paths as blocked by impassable tiles when they are clear (e.g., path from (20, 10) to the grassy area). Manual navigation is required on this map until the tool can be debugged and fixed.
## D. Untested Assumptions & Future Development
- Mewtwo's Location: While Cerulean Cave is the strongest lead, it is not 100% confirmed to be Mewtwo's only possible location. I must remain open to other possibilities if the cave does not yield results.
- Fly Menu Order: I have been assuming the list of flyable locations is in a fixed, static order. I need to test if this order can change based on my current location or other factors.
- Route 10 North Connectivity: I have assumed the northern section of Route 10 is a dead end that only leads to the Power Plant. I need to fly back to Cerulean City and approach from Route 9 to test if there are other paths I missed.
- **Tool Development Idea:** `auto_battle_trivial_encounter`: A tool to fully automate battles against low-level wild Pokémon. It would take a move name as input and handle selecting FIGHT, navigating the menu, and executing the move in one go.
- **Tool Development Idea:** `register_item_to_select`: A tool to automate registering a key item to the SELECT button. This would involve parsing the item menu, selecting the item, and choosing the 'REGISTER' option. This would be useful if this becomes a recurring puzzle mechanic.
- **Agent Development Idea:** `Retreat Strategist`: An agent to be called after a party wipe or when a primary goal is critically stalled. It would analyze the last known safe location (e.g., last used Pokémon Center), the player's available HMs (like Fly), and the nature of the obstacle that caused the failure (e.g., 'party wipe due to unexpected high-level trainer' or 'navigational dead end'). Its output would be a recommended, safe location to retreat to (e.g., 'Fly to Pallet Town') and a high-level suggestion for the next course of action (e.g., 'Regroup and train' or 'Investigate alternative routes from a different hub city').

# VI. Self-Correction & Hallucination Log
## A. Navigational Hallucinations
- Cerulean Cave 1F Partition (Turn 189610): Incorrectly believed I was trapped on an isolated platform at (28, 2). A system warning corrected me, revealing that another ladder at (8, 2) was reachable. Conclusion: Reinforces the absolute necessity of trusting system data over intuition.
- Route 24 Unseen Tiles (Turn 188804): Incorrectly reported 67 reachable unseen tiles when there were 0. Conclusion: Manual assessment is unreliable. MUST use `map_analyzer`.
- Warp Hallucination (Cerulean Gym - Turn 188811): Incorrectly reported 0 reachable warps when the exit was reachable. Conclusion: MUST use `map_analyzer`.
- Dead End Hallucination (Cerulean Cave B1F - Turn 189197): Incorrectly reported being in a dead end. Conclusion: Reinforces the absolute necessity of the `map_analyzer` tool.
- Saffron City Warp Reachability (Turn 190629): Incorrectly reported a warp at (30, 30) as unreachable due to a moving NPC, causing a system warning. This reinforces that my manual assessment of reachability is flawed and I must rely on system data.
- Route 7 Dead End (Turn 190623): Incorrectly assessed Route 7 as a dead end, triggering a critical system warning. I must trust the system's data that another exit exists, even if my tools and visual assessment fail to find it.
## B. Positional & Turn Count Hallucinations
- Route 24 Arrival (Turn 188858): Hallucinated arrival coordinates. Conclusion: Must always verify position from Game State after map transitions.
- Turn Numbers (Multiple): Hallucinated the turn number. Conclusion: Must always trust the Game State Information.
## C. Methodological Improvements
- Proactive Tile Testing: I need to be diligent in testing tiles that appear impassable (like small fences or rocks) to confirm their properties, as ROM hacks can have unusual traversal rules.
- Hypothesis Falsification: A key part of the scientific method is trying to prove a hypothesis wrong. After a test seems to confirm a hypothesis, I should perform another test that tries to *disprove* it to avoid confirmation bias.

# VII. System Critiques & Resolved Tasks
## A. `find_path` Tool Refinement (Resolved)
- Critique (Turn 189302): The tool lacked diagnostic features for map partitioning.
- Resolution (Turn 189308 & 189328): The tool was successfully updated to perform a reachability analysis and report failures due to disconnected map partitions. A critical typo in the XML library import was also fixed.

# VIII. Puzzle Solving & Agent Usage
## A. Cerulean Gym Puzzle
- Lesson: I fell into a confirmation bias loop trying to interact with Pikachu at (5, 4). After multiple failures, I correctly pivoted to a new hypothesis (Pikachu must stand on the tile), which worked. Correction: I must recognize these loops faster and use my `puzzle_solver_agent` to generate new hypotheses when my own attempts fail more than twice.
## B. Inventory Slot Management (CRITICAL LESSON)
- Discarding a partial stack of an item does NOT free up an inventory slot. To create space, an entire stack of an item must be discarded. My `inventory_manager` agent has been updated to reflect this.
- **Tool/Agent Development Idea:** `npc_pathing_assistant`: An agent or tool to handle navigation around moving NPCs. It could take start/end coordinates and a blocking sprite ID. If the path is blocked by that NPC, it could suggest using `stun_npc` at a strategic location or calculate a path that waits for the NPC to move out of the way.

# IX. Self-Assessment Log (Turn 190738)
- **Data Integrity Failure:** I had a major navigational hallucination, believing I was on Route 12 when I was still on Route 11, and placed a marker on the wrong map. This is a critical failure. I MUST always verify my location from the Game State *before* placing markers or making navigational decisions.
- **Marker Usage Failure:** I wasted a turn trying to interact with a Fisher on Route 12 that I had *already marked* as a non-battler. This is a failure to use my own documented data. I MUST check map markers for a target tile before planning an interaction.
- **Proactive Tile Testing:** I have not been diligent about testing tiles that appear impassable, like fences. I need to add this to my standard exploration procedure to avoid missing hidden paths in this ROM hack.
- **Untested Assumption:** The hypothesis that the Underground Path connects Route 7 and Route 8 remains untested. I will keep this in mind as a potential alternate route if my current path is blocked.

# IX. Self-Assessment Log (Turn 190751)
- **Data Integrity Failure:** I had a major navigational hallucination, believing I was on Route 13 when I was still on Route 12, and placed a marker on the wrong map. This is a critical failure. I MUST always verify my location from the Game State *before* placing markers or making navigational decisions.
- **Marker Usage Failure:** I wasted a turn trying to interact with a Fisher on Route 12 that I had *already marked* as a non-battler. This is a failure to use my own documented data. I MUST check map markers for a target tile before planning an interaction.
- **Proactive Tile Testing:** I have not been diligent about testing tiles that appear impassable, like fences. I need to add this to my standard exploration procedure to avoid missing hidden paths in this ROM hack.
- **Untested Assumption:** The hypothesis that the Underground Path connects Route 7 and Route 8 remains untested. I will keep this in mind as a potential alternate route if my current path is blocked.