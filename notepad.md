# I. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data (e.g., reachable warps) is the ultimate source of truth. If my tools or understanding contradict this data, my tools/understanding are wrong and must be corrected immediately. I will not proceed with actions based on faulty assumptions.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics like secret passages unless all other possibilities, especially tool failure, have been disproven through systematic debugging.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result (e.g., `pathfinder` failing to find a confirmed reachable warp), debugging and fixing that tool becomes my absolute highest priority, superseding any navigational or puzzle-solving goal.

# II. Game Intel
## A. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

## B. Tile Mechanics
- **ground**: Walkable tile.
- **impassable**: Cannot be walked on.
- **gate_offscreen**: A gate that is not currently visible on the screen. Its state is unknown. For pathfinding purposes, this is treated as potentially open.
- **warp**: A tile that transports the player to another location.

# III. Puzzle Logs & Hypotheses

## A. Pokémon Mansion 2F Navigation
- **Observation:** The game state consistently reports that the warp at (7, 2) is reachable from my current position in the southern segment of the map. However, my `pathfinder` tool repeatedly fails to find a path.
- **Conclusion (from Overwatch):** My `pathfinder` tool's logic is flawed. It does not correctly interpret the map data, leading it to believe this area is isolated when it is not.
- **Current Plan:**
  1. **(DONE)** Fix the critical bug in the `pathfinder` tool's path reconstruction logic (`came_from[neighbor] = current`).
  2. **(Next)** Use the now-fixed `pathfinder` tool to calculate a path to the warp at (7, 2).
  3. Follow the calculated path to finally exit this area and proceed to the third floor as per the master plan.