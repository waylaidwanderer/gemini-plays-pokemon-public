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

# VI. Game Mechanics & Tile Properties

## A. Tile Traversal Rules
- **ground:** Standard walkable tile.
- **impassable:** Cannot be entered. Walls, rocks, etc.
- **elevated_ground:** Walkable, but can only be accessed from `steps` tiles or other `elevated_ground` tiles.
- **steps:** Allows movement between `ground` and `elevated_ground`.
- **ladder_up / ladder_down:** Acts as a warp to a different floor. Walkable.
- **ledge:** A one-way obstacle. Can be jumped down (from Y-1 to Y+2 in one move), but not climbed up. Acts as a wall from below or the sides.
- **grass:** Tall grass where wild Pokémon can be encountered. Walkable like `ground`.

## D. Agent Usage Notes
- Reminder: Use existing agents like `puzzle_solver_agent` more consistently for complex problems like the fossil hunt, rather than relying solely on manual hypothesis generation.
- **TeamBuilder Agent Idea:** An agent that takes my PC box contents and a Gym Leader's roster (from my notes) to suggest an optimal team composition and move order.
- **MarkerCleanup Tool:** A tool to parse the `relevant_map_markers` list, group markers by coordinate, and identify those with similar labels that could be consolidated.

# --- REORGANIZED NOTEPAD (PENDING DELETION OF OLD CONTENT) ---

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

# III. World Data

## A. Solved Puzzles & Key Events
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.

## B. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Confirmed via dialogue that he is blocking the path south and demands a fossil to pass.
- **Officer Jenny (Cerulean City):** Blocking path east. All local hypotheses have failed. The trigger is likely elsewhere.

# IV. Puzzles & Hypotheses

## A. Mt. Moon Fossil Puzzle (Stalled)
- **Obstacle:** Rocket Grunt at (30, 12) on Mt. Moon B2F blocks the path south, demanding a fossil.
- **Status:** All leads are exhausted for now. This goal is a distraction from the main story path.

## B. Cerulean City Officer Jenny Puzzle (Deprioritized)
- **Obstacle:** Officer Jenny blocks the path east out of Cerulean City.
- **Status:** The `stuck_navigator_agent` suggests this path requires the HM 'Cut' and I should explore north first.

## C. Pewter Museum Exploration
- **Hypothesis 1:** The Pewter Museum of Science contains clues about where to find a fossil.
  - **Test Plan:** Explore both floors of the museum, examine all exhibits, and speak to relevant NPCs.
- **Hypothesis 2 (Counter-Hypothesis):** The museum is an optional area with no critical path information.
  - **Test Plan:** If a full exploration yields no key items or direct clues for progression, I will assume it's optional and focus on finding the exit from Pewter City.

# V. Tool & Agent Development

## A. Development Lessons
- **Trust System Data:** I must trust system data (map memory, tool outputs) over my own assumptions.
- **Menu Cursor Behavior:** Menu cursor starting positions are non-deterministic.
- **Battle Move Selection:** The move selection menu is a single-column list navigated with UP/DOWN only.
- **Fly Destination Verification:** I must verify that a location is on the Fly menu list *before* attempting to navigate to it.
- **Map Partitions:** Some areas (like Mt. Moon and Route 2) are heavily partitioned. Pathfinding tools will correctly fail if the start and end points are in disconnected partitions.
- **Discipline:** I must be more disciplined about using existing automation for tasks like menu navigation and getting unstuck.

## B. Future Development Ideas
- **GymLeaderStrategist Agent:** An agent that takes a gym leader's known roster and my current party to suggest an optimal team order before the battle begins.
- **select_party_member Tool:** A tool that takes the party list and a target Pokémon's name to automate selecting them from the party menu.
- **navigation_diagnostics_agent:** An agent that takes a failed pathfinder output and the current player state to suggest a root cause.
- **NPC Prioritization Agent:** An agent that suggests which NPC to interact with first based on sprite type (e.g., Scientists > Youngsters) to maximize information gain efficiency.

# VI. Game Mechanics & Tile Properties

## A. Tile Traversal Rules
- **ground:** Standard walkable tile.
- **impassable:** Cannot be entered. Walls, rocks, etc.
- **elevated_ground:** Walkable, but can only be accessed from `steps` tiles or other `elevated_ground` tiles.
- **steps:** Allows movement between `ground` and `elevated_ground`.
- **ladder_up / ladder_down:** Acts as a warp to a different floor. Walkable.
- **ledge:** A one-way obstacle. Can be jumped down (from Y-1 to Y+2 in one move), but not climbed up.
- **grass:** Tall grass where wild Pokémon can be encountered. Walkable like `ground`.

# --- REORGANIZED NOTEPAD (PENDING DELETION OF OLD CONTENT) ---

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

# III. World Data

## A. Solved Puzzles & Key Events
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.

## B. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Confirmed via dialogue that he is blocking the path south and demands a fossil to pass.
- **Officer Jenny (Cerulean City):** Blocking path east. All local hypotheses have failed. The trigger is likely elsewhere.

# IV. Puzzles & Hypotheses

## A. Mt. Moon Fossil Puzzle (Stalled)
- **Obstacle:** Rocket Grunt at (30, 12) on Mt. Moon B2F blocks the path south, demanding a fossil.
- **Status:** All leads are exhausted for now. This goal is a distraction from the main story path.

## B. Cerulean City Officer Jenny Puzzle (Deprioritized)
- **Obstacle:** Officer Jenny blocks the path east out of Cerulean City.
- **Status:** The `stuck_navigator_agent` suggests this path requires the HM 'Cut' and I should explore north first.

## C. Pewter Museum Exploration
- **Hypothesis 1:** The Pewter Museum of Science contains clues about where to find a fossil.
  - **Test Plan:** Explore both floors of the museum, examine all exhibits, and speak to relevant NPCs.
- **Hypothesis 2 (Counter-Hypothesis):** The museum is an optional area with no critical path information.
  - **Test Plan:** If a full exploration yields no key items or direct clues for progression, I will assume it's optional and focus on finding the exit from Pewter City.

# V. Tool & Agent Development

## A. Development Lessons
- **Trust System Data:** I must trust system data (map memory, tool outputs) over my own assumptions.
- **Menu Cursor Behavior:** Menu cursor starting positions are non-deterministic.
- **Battle Move Selection:** The move selection menu is a single-column list navigated with UP/DOWN only.
- **Fly Destination Verification:** I must verify that a location is on the Fly menu list *before* attempting to navigate to it.
- **Map Partitions:** Some areas (like Mt. Moon and Route 2) are heavily partitioned. Pathfinding tools will correctly fail if the start and end points are in disconnected partitions.
- **Discipline:** I must be more disciplined about using existing automation for tasks like menu navigation and getting unstuck.

## B. Future Development Ideas
- **GymLeaderStrategist Agent:** An agent that takes a gym leader's known roster and my current party to suggest an optimal team order before the battle begins.
- **select_party_member Tool:** A tool that takes the party list and a target Pokémon's name to automate selecting them from the party menu.
- **navigation_diagnostics_agent:** An agent that takes a failed pathfinder output and the current player state to suggest a root cause.
- **NPC Prioritization Agent:** An agent that suggests which NPC to interact with first based on sprite type (e.g., Scientists > Youngsters) to maximize information gain efficiency.

# VI. Game Mechanics & Tile Properties

## A. Tile Traversal Rules
- **ground:** Standard walkable tile.
- **impassable:** Cannot be entered. Walls, rocks, etc.
- **elevated_ground:** Walkable, but can only be accessed from `steps` tiles or other `elevated_ground` tiles.
- **steps:** Allows movement between `ground` and `elevated_ground`.
- **ladder_up / ladder_down:** Acts as a warp to a different floor. Walkable.
- **ledge:** A one-way obstacle. Can be jumped down (from Y-1 to Y+2 in one move), but not climbed up.
- **grass:** Tall grass where wild Pokémon can be encountered. Walkable like `ground`.