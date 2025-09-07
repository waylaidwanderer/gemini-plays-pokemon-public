# I. Core Directives & Lessons

## A. Core Directives
1.  **IMMEDIATE MAINTENANCE:** All data management (notepad, markers) and tool/agent refinement is the HIGHEST priority and MUST be performed in the same turn a need is identified.
2.  **PROACTIVE AUTOMATION:** Before any complex or repetitive task, I must first consider automating it with a tool or agent. If one doesn't exist, creating it is the new priority.
3.  **TRUST, BUT REFINE:** I must trust the outputs of my agents and system data. If an agent or tool is suboptimal, I must prioritize refining it immediately.
4.  **ABANDON FAILED HYPOTHESES:** If a strategy fails repeatedly, I must recognize the pattern, document it, and pivot to a new approach.

## B. Key Lessons & Recurring Failures
- **Positional & Data Awareness:** I must verify my current coordinates, turn number, and system-provided data from the Game State Information *before* every action and trust it over my own manual assessment.
- **Dead End Definition:** A map is a dead end ONLY if it has 1 or fewer reachable exits (warps/connections) AND 0 reachable unseen tiles. I must be rigorous in this calculation.
- **System vs. Local Reachability:** System warnings about "reachable" tiles/warps are a global check for the entire map and may not reflect what is reachable from my current partitioned location.
- **Confirmation Bias in Problem-Solving:** Persisting with a failed hypothesis is a critical error. My handling of the Officer Jenny puzzle and the `automated_path_navigator` debugging are key examples of this failure. After a few failed attempts, I must invalidate the hypothesis and pivot to a new one.
- **Data Maintenance Efficiency:** Map connection markers (entry and exit) must be placed in the same turn immediately following a map transition to avoid inefficient backtracking.

# II. Game Data

## A. Type Chart (Verified)
- Electric is not very effective against Electric, Grass/Poison, and Bug/Grass types.
- Ground moves do not affect GASTLY (Ghost/Poison).
- Normal moves do not affect Ghost-types.
- Normal is not very effective against GEODUDE (Rock/Ground).
- Poison is not very effective against Ground-types.

## B. Known Pokemon Locations
- **Cerulean Cave:** Ditto, Wigglytuff, Electrode, Golem, Raichu, Sandslash, Parasect, Lickitung, Magneton, Dodrio, RHYDON, VICTREEBEL, GOLBAT, KADABRA.
- **Pokémon Tower:** GASTLY, CUBONE.
- **Mt. Moon:** ZUBAT, SANDSHREW, PARAS.

## C. Key Trainer Rosters
- **Nurse Joy (Fuchsia Pokecenter):** KANGASKHAN (Lv 65): DOUBLE-EDGE, DOUBLE TEAM; SNORLAX (Lv 65): ICE BEAM, REST

# III. World Data

## B. Solved Puzzles & Key Events
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.

## C. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Confirmed via dialogue that he is blocking the path south and demands a fossil to pass.
- **Officer Jenny (Cerulean City):** Blocking path east. All local hypotheses have failed. The trigger is likely elsewhere.

# IV. Puzzles & Hypotheses

## A. Mt. Moon Fossil Puzzle
- **Obstacle:** Rocket Grunt at (30, 12) on Mt. Moon B2F blocks the path south, demanding a fossil.
- **Clue:** Super Nerd at (13, 9) on Mt. Moon B2F mentioned a Pokémon Lab on Cinnabar Island that regenerates fossils.
- **Hypothesis 1 (Invalidated):** A fossil is an item hidden in an unexplored partition of Mt. Moon.
  - **Test Result:** A full exploration of all reachable partitions of Mt. Moon, including the area east of the mountain on Route 4, yielded no fossil item. This hypothesis is now considered invalid.
- **Hypothesis 2 (Active):** The fossil is not located in Mt. Moon or the immediate surrounding areas. The next step is to progress the main story elsewhere to find new leads.

## B. Cerulean City Officer Jenny Puzzle
- **Obstacle:** Officer Jenny blocks the path east out of Cerulean City.
- **Hypothesis 1 (Invalidated):** The trigger is in the Trashed House or its backyard. (Pre-Rocket events)
- **Hypothesis 2 (Invalidated):** The trigger is on Route 24/Nugget Bridge.
- **Hypothesis 3 (Invalidated):** The trigger is defeating Team Rocket elsewhere.
  - **Test Result:** Interacting with Officer Jenny after clearing Silph Co. changed her dialogue, but she did not move. This confirms the event state is linked, but the trigger is more specific.
- **Hypothesis 4 (Invalidated):** The trigger is interacting with the Fishing Guru in the robbed house after recovering the stolen TM DIG.
  - **Test Result:** Spoke to the Fishing Guru. His dialogue confirmed the robbery but did not trigger any event or reward.
- **Hypothesis 5 (Invalidated):** The trigger is interacting with the *other* resident of the robbed house, the Girl.
  - **Test Result:** Spoke to the Girl. Her dialogue confirmed the robbery but did not trigger any event or reward.
- **Hypothesis 6 (Active):** The trigger for Officer Jenny is not in Cerulean City. I must progress the main story elsewhere, likely by traveling south towards Vermilion City, as suggested by my `puzzle_solver_agent`.

# V. Tool & Agent Development

## A. Development Lessons
- **Lesson: Trust System Data:** I must trust system data (map memory, tool outputs) over my own assumptions. My failure to believe the pathfinder's correct output regarding an impassable tile was a critical error that wasted significant time.
- **Lesson: Menu Cursor Behavior:** Menu cursor starting positions are non-deterministic.
- **Lesson: Battle Move Selection:** The move selection menu is a single-column list navigated with UP/DOWN only. LEFT/RIGHT have no effect.
- **Lesson: Fly Destination Verification:** The `automated_fly_navigator` tool correctly identifies invalid destinations. I must verify that a location is on the Fly menu list *before* attempting to navigate to it. Pewter City is not a flyable location.
- **Lesson: Mt. Moon Partitions:** The lower floors of Mt. Moon are heavily partitioned. My pathfinding tools were failing because I was trying to navigate between disconnected areas. I repeatedly misidentified these partitions as dead ends, failing to account for all reachable warps.
- **Lesson: Discipline:** I must be more disciplined about using existing automation (agents and tools) for tasks like menu navigation and getting unstuck, rather than resorting to error-prone manual attempts.

## D. Future Development Ideas
- **GymLeaderStrategist Agent:** An agent that takes a gym leader's known roster and my current party to suggest an optimal team order before the battle begins.

# VI. Game Mechanics & Rules

## A. Tile Traversal Rules (Verified)
- **ground:** Standard walkable tile.
- **grass:** Walkable tile where wild Pokémon encounters can occur.
- **water:** Can only be crossed using the HM Surf.
- **impassable:** A solid barrier like a wall, tree, or object. Cannot be entered.
- **cuttable:** A small tree that can be removed with the HM Cut. Becomes 'ground' after use but respawns on map change.
- **ledge:** Can only be jumped down from above (Y-1). Jumping moves the player to Y+2 in one step. Acts as a wall from below and sides.
- **ladder_up / ladder_down:** Acts as a warp tile, moving the player between floors.
- **steps:** The only tile type that allows movement between `ground` and `elevated_ground`.
- **elevated_ground:** Walkable ground at a higher elevation, only accessible via `steps`.