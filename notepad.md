# I. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data (e.g., reachable warps) is the ultimate source of truth. If my tools or understanding contradict this data, my tools/understanding are wrong and must be corrected immediately. I will not proceed with actions based on faulty assumptions.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics like secret passages unless all other possibilities, especially tool failure, have been disproven through systematic debugging.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result (e.g., `pathfinder` failing to find a confirmed reachable warp), debugging and fixing that tool becomes my absolute highest priority, superseding any navigational or puzzle-solving goal.

# II. Game Intel
## A. Map Marker Legend (Strict)
- **Warps:** ↕️ (Used), 🛬 (Arrival)
- **Gates:** ✅ (Open), 🔴 (Closed)
- **Switches:** 🔄 (Toggled)
- **Items:** 💰 (Found), ❌ (Trap)
- **Navigation:** 🚫 (Dead End), 🕳️ (Hole)

## B. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

# III. Puzzle Logs & Future Plans
## A. Pokémon Mansion: Master Plan
- **Objective:** Find the SECRET KEY.
- **Guiding Strategy (from multi_floor_puzzle_strategist_agent):** The puzzle requires activating a sequence of four switches across four floors to open all gates and access the key.
- **Step 1 (Done):** On 1F, activate the switch at (3, 6).
- **Step 2 (Done):** Ascend to 2F via stairs at (6, 11).
- **Step 3 (Done):** On 2F, activate the switch at (3, 12).
- **Step 4 (Done):** Ascend to 3F and activate the switch at (11, 6).
- **Step 5 (Hypothesis):** The previous actions should have opened the Central Gates at (21, 18)/(22, 18).
- **Step 6 (Next):** Go to 1F and check the Central Gates. If open, proceed through them to the warp at (22, 24) to reach B1F.
- **Step 7:** On B1F, activate the final switch at (19, 26). This should open the Western Gates on 1F.
- **Step 8:** Return to 1F via the warp at (24, 23).
- **Step 9:** Navigate to the now-open Western Gates at (25, 14)/(26, 14) and retrieve the SECRET KEY.

## B. Future Tool Development
- **`grid_visualizer`:** Create a tool to print a formatted grid from the `map_xml_string` for easier pathfinding debugging. This would be more efficient than manually adding print statements to `run_code`.