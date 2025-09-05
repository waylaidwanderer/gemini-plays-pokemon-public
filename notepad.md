# I. Core Directives & Key Lessons Learned
## A. Core Directives
- D1: IMMEDIATE DATA & TOOL MANAGEMENT: All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
- D2: ACT ON DOCUMENTATION: A documented lesson that does not result in a behavioral change is a critical failure.
- D3: ABANDON FAILED HYPOTHESES: If a strategy fails repeatedly, I must recognize the pattern, document it with attempt counts, and pivot to a new approach.
- D4: TRUST, BUT REFINE: I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
- D5: PROACTIVELY AUTOMATE: Before performing any complex or repetitive task, I must first consider if it can be automated with a tool or agent.
## B. CRITICAL Lessons from Overwatch Critique (Turn 191004)
- **Tool Usage Discipline:** I have repeatedly failed to use tools correctly (forgetting `autopress_buttons: true`, providing incorrect coordinates to `find_path`). This is a critical failure. I MUST verify my position from the Game State before every pathfinding call and double-check all flags for tools that generate button presses.
- **Proactive Automation is Key:** I have good ideas for tools but fail to implement them. I must prioritize building tools like `npc_pathing_assistant` to solve recurring problems instead of just documenting them as ideas.
## C. Other Key Lessons Learned
- **Positional Awareness:** I have repeatedly hallucinated my position, leading to failed movements. I MUST verify my current coordinates from the Game State Information *before* every single action.
- **Confirmation Bias:** My manual assessment of map connectivity (dead ends, partitions) is highly unreliable. I MUST trust my `map_analyzer` tool and system warnings over my own intuition.
- **Escape is Not Guaranteed:** Fleeing from wild battles is not always possible (e.g., DODRIO in Cerulean Cave). I must not rely on running as a guaranteed safe option.

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
## A. Pokémon Tower 7F (Ghost Puzzle)
- **Current Status:** All attempts to interact with the ghost on 7F using the SILPH SCOPE or other items have failed. Speaking to Mr. Fuji resulted in a dialogue loop about his POKé FLUTE, providing no new information. This path is a dead end.
- **New Hypothesis:** The solution is not on 7F. There may be a hidden switch or alternate path on a lower floor (5F or 6F) that was previously missed.
- **Next Action:** Thoroughly re-explore Pokémon Tower 5F and 6F. Test every wall and interact with every object.

## B. Untested Assumptions
- **Assumption:** The ghost on 7F is the *only* way forward.
- **Test:** Re-explore floors 5 and 6 for alternative paths or hidden switches.
- **Assumption:** The SILPH SCOPE is the *only* solution to the ghost problem.
- **Test:** If re-exploration fails, I must re-evaluate my key items to see if another item has a hidden purpose.

# IV. Solved Puzzles & Mechanics Reference

## C. Boulder Puzzle Mechanics
- Objective: Boulders are often pushed into holes to block water currents on lower floors.
- Movement: Pushing is a multi-turn action. Must be adjacent. First press turns/pushes. Subsequent pushes require moving to the new adjacent tile first.
- Surfing Limitation: Cannot push boulders while surfing (confirmed on Seafoam Islands B3F).
## D. Navigation Puzzles
- Cerulean City River: The city is divided by a river. The western section (where you arrive from Route 4) and the eastern section (where the path to Route 9 is) are separated. To cross between them, I must use Surf.
- Mt. Moon Entrances: There are two entrances to Mt. Moon from Route 4. The western entrance at (19, 6) leads to an isolated, dead-end section. The eastern entrance at (25, 6) leads to the main cave system and the path forward to Cerulean City.
- Route 8 Gatehouse: The gatehouse connecting the two halves of Route 8 has a 1x2 warp. To enter from the west, I had to stand on the southern tile (2, 11) and press Right.
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
- `find_path` on Route 7 (Correction): The tool is NOT bugged. My previous assessment was a hallucination. The tool correctly identifies that Route 7 is partitioned by impassable ledges and walls. The eastern and western sections are not connected on this map. The tool's 'no path found' result is accurate.

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

# IX. Self-Assessment Log
- **Data Integrity Failure (Turn 190738 & 190751):** I had major navigational hallucinations, believing I was on the wrong route and placing markers on the wrong map. This is a critical failure. I MUST always verify my location from the Game State *before* placing markers or making navigational decisions.
- **Marker Usage Failure (Turn 190751):** I wasted a turn trying to interact with a Fisher on Route 12 that I had *already marked* as a non-battler. This is a failure to use my own documented data. I MUST check map markers for a target tile before planning an interaction.
- **Proactive Tile Testing:** I have not been diligent about testing tiles that appear impassable, like fences. I need to add this to my standard exploration procedure to avoid missing hidden paths in this ROM hack.
- **Untested Assumption:** The hypothesis that the Underground Path connects Route 7 and Route 8 remains untested. I will keep this in mind as a potential alternate route if my current path is blocked.

# X. Self-Assessment Insights & Future Development
## A. Methodological Improvements
- Proactive Tile Testing: I have not been diligent about testing tiles that appear impassable. I must add this to my standard exploration procedure to avoid missing hidden paths, especially in a ROM hack.
## B. Untested Assumptions
- Pokémon Tower Puzzle: I am assuming the ghost on 7F is the only way forward and that the SILPH SCOPE is the only solution. If my next hypothesis fails, I must test this by thoroughly exploring floors 5 and 6 for hidden switches or paths.
- Mr. Fuji's Role: I am assuming Mr. Fuji is the key to solving the puzzle, but this is unverified.
## C. Tool & Agent Development Ideas
- `auto_battle_trivial_encounter` (Improvement): The current tool relies on a hardcoded moveset for REVENANT. A more robust version would parse the active Pokémon's moves from the screen or take them as an argument to be more flexible.
- `npc_pathing_assistant`: An agent or tool to handle navigation around moving NPCs. It could take start/end coordinates and a blocking sprite ID. If the path is blocked by that NPC, it could suggest using `stun_npc` at a strategic location or calculate a path that waits for the NPC to move out of the way.

# XI. Self-Assessment Insights (Turn 190995)
- **Positional Awareness Failure (CRITICAL):** I have repeatedly hallucinated my position (e.g., Turn 190985), leading to failed movements and incorrect tool inputs. I MUST verify my current coordinates from the Game State Information *before* every single action.
- **Tool Usage Failure (CRITICAL):** I have failed to use my own tools correctly (e.g., omitting `autopress_buttons: true` for `auto_battle_trivial_encounter` on Turns 190983 & 190984), causing repeated failed turns. I must verify the arguments and flags for every tool call.
- **Confirmation Bias (Mr. Fuji):** My hypothesis that Mr. Fuji was the key to the ghost puzzle was based on an assumption. After he entered a dialogue loop, I correctly identified this as a dead end and pivoted to a new hypothesis, which is the correct procedure.

# VI. Reference Library (Solved Puzzles, Mechanics, etc.)
## B. Snorlax Puzzle (Route 12)
- The item menu is a single, scrollable list. After selecting 'ITEM' from the main menu, scroll down past the HMs (indicated by a '↓' arrow) to find Key Items like the POKé FLUTE. Using it from this menu wakes the Snorlax.