# I. Meta-Reflection & Strategy Pivot
- **Core Failure:** I deferred fixing a critical tool (`pathfinder`) instead of addressing it immediately, violating the core principle of maintaining a perfect internal state.
- **Goal Discipline:** My goals must be *outcomes* (e.g., 'Obtain the Secret Key'), not *methods* (e.g., 'Fix the tool'). Fixing tools is an immediate, non-negotiable action, not a deferred goal.
- **Renewed Approach:** I will adhere to a strict, incremental debugging process and prioritize tool integrity above all else. I will not use a tool I know to be broken.

# II. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data is the ultimate source of truth. If my tools or understanding contradict this data, they are wrong and must be corrected immediately.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics unless all other possibilities have been disproven.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result, debugging and fixing it becomes my absolute highest priority, superseding any other goal.
- **Immediate Documentation:** All discoveries, plans, and state changes must be documented *immediately* in the notepad or with map markers to avoid hallucinations and redundant actions.

# III. Game Intel
## A. Tile Mechanics
- `ground`: Walkable tile.
- `impassable`: Walls, counters, etc. Cannot be entered.
- `warp`: Teleports the player to a new location.
- `open_gate`: A gate that is visibly open and acts as `ground`.
- `closed_gate`: A gate that is visibly closed and acts as `impassable`.
- `gate_offscreen`: A gate whose state is unknown. Must be treated as potentially open for pathfinding unless a marker indicates otherwise.
- `ledge`: Can be jumped down, but not climbed up. Acts as ground when approached from above (Y-1), but as a wall from all other directions.
- `hole`: Warps the player to a lower floor, usually into an isolated area.

## B. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

# V. Pokémon Mansion Puzzle Log
- **Observation:** The mansion puzzle involves interconnected switches on 1F and 2F.
- **Hypothesis 1 (Failed):** Flipping the 2F switch, then the 1F switch, will open a path to the Secret Key.
- **Test 1:** Flipped 2F switch at (3,12). Went to 1F. Flipped 1F switch at (3,6).
- **Conclusion 2:** Attempts to use the 2F switch resulted in a loop. The solution does not appear to involve the 2F switch in this way. Hypothesis failed.
- **Hypothesis 3 (Confirmed):** The switch at (3,6) on 1F toggles the state of the gates at (17,8) and (18,8).
- **Conclusion 3:** The path forward is through the eastern gates, but the path is blocked by a wall at (17,11).
- **Hypothesis 4 (Current):** I am missing an interaction or another switch. I will re-explore the entire accessible area of 1F.
- **Test 4 Plan:**
    1. Systematically explore all reachable areas on 1F to look for any missed clues or switches.

# III. Pokémon Mansion Puzzle Strategy (Agent-Devised)
- **Goal:** Find the Secret Key
- **Step 1:** (1F) Activate the switch at (3,6).
- **Step 2:** (1F) Use the warp at (6,11) to travel to 2F.
- **Step 3:** (2F) Activate the switch at (3,12).
- **Step 4 (FAILED):** Agent's plan to use warp at (8,11) on 2F was incorrect. It leads back to 1F.
- **Step 5:** (3F) Activate the switch at (11,6).
- **Step 6:** (3F) Intentionally fall through the 'Hole to 2F'.
- **Step 7:** (2F) From the new landing zone, fall through the 'Hole to 1F'.
- **Step 8:** (1F) Proceed to the warp at (22,24) and travel to the basement.
- **Step 9:** (B1F) Activate the switch at (19,26).
- **Step 10:** (B1F) Navigate through the now-open gates to find and retrieve the Secret Key.

# Pokémon Mansion Puzzle Strategy (Agent-Devised)
- **Goal:** Find the Secret Key
- **Step 1:** (1F) Activate the switch at (3,6).
- **Step 2:** (1F) Use the warp at (6,11) to travel to 2F.
- **Step 3:** (2F) Activate the switch at (3,12).
- **Step 4 (FAILED):** Agent's plan to use warp at (8,11) on 2F was incorrect. It leads back to 1F.
- **Step 5:** (3F) Activate the switch at (11,6).
- **Step 6:** (3F) Intentionally fall through the 'Hole to 2F'.
- **Step 7:** (2F) From the new landing zone, fall through the 'Hole to 1F'.
- **Step 8:** (1F) Proceed to the warp at (22,24) and travel to the basement.
- **Step 9:** (B1F) Activate the switch at (19,26).
- **Step 10:** (B1F) Navigate through the now-open gates to find and retrieve the Secret Key.

# Pokémon Mansion Puzzle Corrections
- The warp at (8,11) on 2F leads to 1F, not 3F.
- The warp at (7,2) on 2F also leads to 1F.
- The agent's plan is therefore invalid from Step 4 onwards. A new path to 3F is required.