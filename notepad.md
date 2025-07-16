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

# III. Puzzle Logs & Hypotheses

## A. Pokémon Mansion 2F Navigation
- **Observation:** The game state consistently reported that the warp at (7, 2) was reachable. However, my `pathfinder` tool repeatedly failed to find a path.
- **Hypothesis:** My `pathfinder` tool's logic was flawed.
- **Test:** Debugged the tool by adding print statements.
- **Conclusion:** Hypothesis DENIED. The tool's logic was sound. The failure was caused by my own outdated map markers, which incorrectly labeled a gate as 'Closed', creating an artificial wall. This confirms that data integrity (my markers) is as critical as tool logic.
- **Current Plan:**
  1. **(DONE)** Deleted the incorrect map markers.
  2. **(DONE)** Used the `pathfinder` tool to calculate a path to the warp at (7, 2).
  3. **(Next)** Follow the calculated path to finally exit this area and proceed to the third floor.

## C. Pokémon Mansion 2F Switch Puzzle (Attempt 2)
- **Hypothesis:** The switch at (3, 12) is a simple toggle. Pressing it a second time should reopen the northern gates at (10, 5) and (10, 6).
- **Test:** Pressed the switch at (3, 12) for a second time.
- **Conclusion:** Hypothesis DENIED. The path north remains blocked. The switch's function is more complex than a simple toggle.

- **Data Discipline Reminder (from Overwatch):** I must update my notepad and map markers *immediately* upon discovering new information or environmental changes. No more deferring documentation. I will also avoid creating redundant map markers.
- **Data Discipline Reminder (from Overwatch):** I must update my notepad and map markers *immediately* upon discovering new information or environmental changes. No more deferring documentation. I will also avoid creating redundant map markers.

## B. Dead End Hallucination (Pokemon Mansion 2F)
- **Observation:** I believed I was trapped in an area after flipping a switch, and my `pathfinder` tool failed. I received a `Dead End Area Mismatch` critique, which stated I was not in a dead end because 3 exits were still reachable.
- **Hypothesis:** My mental model of the map was incorrect, and I was not actually trapped.
- **Conclusion:** Hypothesis CONFIRMED. The critique was correct. My failure to trust the game's validation data led to a hallucination. The path forward was blocked by newly closed gates, but other exits were still available. 
- **Lesson Learned:** The game's validation data (e.g., `is_in_dead_end_area`, `navigable_warps`) is the absolute source of truth. If my understanding or tools contradict this data, they are wrong and must be corrected. I will no longer assume I am trapped if the system says otherwise.

## D. Pokémon Mansion 1F Switch Access
- **Hypothesis:** The switch at (3, 6) is accessible through the gates at (17, 8) and (18, 8), which were opened by the switch on 2F.
- **Test:** Use pathfinder to plot a course to (17, 8).
- **Expected Outcome:** A valid path will be found.