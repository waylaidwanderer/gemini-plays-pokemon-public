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
- **Confirmation Bias in Problem-Solving:** Persisting with a failed hypothesis is a critical error. After a few failed attempts, I must invalidate the hypothesis and pivot to a new one.
- **Data Maintenance Efficiency:** Map connection markers (entry and exit) must be placed in the same turn immediately following a map transition to avoid inefficient backtracking.

# II. World Data

## A. Solved Puzzles & Key Events
- **Snorlax (Routes 11 & 12):** Awakened using the POKé FLUTE from the ITEM menu.
- **Pokémon Tower Ghost:** Used SILPH SCOPE to reveal the ghost.
- **Seafoam Islands Current:** Solved multi-floor boulder puzzle to stop the strong water current.
- **Pewter Museum Puzzle:** Solved by a sequence of interactions with the Aerodactyl Fossil and an invisible follower Pikachu, which caused a blocking Youngster to move.

## B. Obstacles & Solutions
- **Rocket Grunt (Mt. Moon B2F at 30, 12):** Confirmed via dialogue that he is blocking the path south and demands a fossil to pass.
- **Officer Jenny (Cerulean City):** Blocking path east. All local hypotheses have failed. The trigger is likely elsewhere.

# III. Game Mechanics & Tile Properties

## A. Tile Traversal Rules
- **ground:** Standard walkable tile.
- **impassable:** Cannot be entered. Walls, rocks, etc.
- **elevated_ground:** Walkable, but can only be accessed from `steps` tiles or other `elevated_ground` tiles.
- **steps:** Allows movement between `ground` and `elevated_ground`.
- **ladder_up / ladder_down:** Acts as a warp to a different floor. Walkable.
- **ledge:** A one-way obstacle. Can be jumped down (from Y-1 to Y+2 in one move), but not climbed up. Acts as a wall from below or the sides.
- **grass:** Tall grass where wild Pokémon can be encountered. Walkable like `ground`.
- **unknown:** Tile type has not been visually confirmed.

# IV. Tool & Agent Development

## A. Future Development Ideas
- **GymLeaderStrategist Agent:** An agent that takes a gym leader's known roster and my current party to suggest an optimal team order before the battle begins.
- **Team Builder Agent:** An agent that can analyze my entire PC box and suggest an optimal team for a specific upcoming challenge, like a Gym Leader or the Elite Four.

# V. Untested Hypotheses & Test Plans
- **Silent Healing:** I observed that my party was healed at the Pewter Pokémon Center without any confirmation dialogue. Hypothesis: This is a consistent mechanic. Test Plan: Next time I heal my Pokémon, I will pay close attention to the dialogue flow and see if the healing happens silently again. I will try this at two different Pokémon Centers to verify.
- **Battling Nurses:** Confirmed that Nurse Joy in Fuchsia City will repeatedly challenge me to a battle immediately after healing my party. Hypothesis: This behavior may be unique to this specific Nurse Joy. Test Plan: Visit a different Pokémon Center (e.g., Saffron City) and heal my party to see if a battle is triggered there.
- **Maze Solver Agent:** An agent that can take warp data for a maze-like area and determine the correct sequence of warps to reach a specific destination.
- **Warp Pathfinder Tool:** A computational tool that automates maze navigation by parsing warp data and calculating the optimal path, then returning a sequence of coordinates to follow.