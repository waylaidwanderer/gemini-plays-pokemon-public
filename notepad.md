# I. Core Principles & Lessons Learned
- **System Validation is Absolute Truth:** The game's validation data is the ultimate source of truth. If my tools or understanding contradict this data, they are wrong and must be corrected immediately.
- **Rigorous Hypothesis Testing:** When faced with a puzzle, I will form a single, testable hypothesis and design a minimal experiment to confirm or deny it. I will not assume hidden mechanics unless all other possibilities have been disproven.
- **Tool Integrity is Paramount:** A faulty tool is worse than no tool. If a tool provides an incorrect result, debugging and fixing it becomes my absolute highest priority, superseding any other goal.
- **Immediate Documentation:** All discoveries, plans, and state changes must be documented *immediately* in the notepad or with map markers to avoid hallucinations and redundant actions.

# II. Game Intel
## A. Tile Mechanics
- `ground`: Walkable tile.
- `impassable`: Walls, counters, etc. Cannot be entered.
- `warp`: Teleports the player to a new location.
- `open_gate`: A gate that is visibly open and acts as `ground`.
- `closed_gate`: A gate that is visibly closed and acts as `impassable`.
- `gate_offscreen`: A gate whose state is unknown. Must be treated as potentially open for pathfinding unless a marker indicates otherwise.
- **Switches**: Must be activated by standing on the tile directly below them, facing up, and pressing A.
- `ledge`: Can be jumped down, but not climbed up. Acts as ground when approached from above (Y-1), but as a wall from all other directions.
- `hole`: Warps the player to a lower floor, usually into an isolated area.

## B. Confirmed ROM Hack Mechanics
- **Type Matchups:** Psychic > Ghost/Poison; Ghost > Psychic; Electric > Rock/Water; CUT (Normal) > VICTREEBEL (Grass/Poison); Flying > Grass/Poison; Psychic > Flying; Ice > Ground; Ground > Poison; Ground > Fire; Rock > Fire.
- **Type Resistances:** Normal !> Psychic; Electric !> Grass; Rock !> Ground; Psychic !> Psychic; Bite (Normal) !> HAUNTER (Ghost/Poison); Ice !> Gyarados (Water/Flying); Poison !> Poison; Ice !> Water; Poison !> Ground.
- **Type Immunities:** Flying immune to Ground; Ground immune to Electric; MUK immune to Poison; HYPNO immune to STUN SPORE; MUK immune to THUNDER WAVE; MAROWAK immune to POISON GAS.
- **Field/Battle Rules:** Switches require standing below and facing up. Losing in a gym does not warp you out. FLY can end wild battles indoors. ROAR can end wild battles.

# III. Tool Debugging Logs
## A. Pathfinder Tool
- **Status:** Critical Failure
- **Symptom:** Tool produces no output, not even a 'Path not found' message or debug logs.
- **Hypothesis 1:** The script is crashing silently due to a logic or parsing error.
- **Test 1:** Overwrite the tool with a minimal script containing only a print statement.
- **Result 1:** SUCCESS. The minimal script executed and printed its output. This confirms the tool's execution environment is working.
- **Conclusion:** The error lies within the logic of the original, complex A* script.
- **Hypothesis 2:** The grid generation logic in the A* script is incorrectly marking a necessary tile as impassable.
- **Test 2:** Restore the full A* script with detailed debug logs.
- **Result 2:** FAILED. The script produced a `ModuleNotFoundError` for `xml.et`.
- **Conclusion:** The error is not in the logic, but in the import statement itself.
- **Hypothesis 3:** The import statement `import xml.et.ElementTree as ET` is incorrect and should be `import xml.etree.ElementTree as ET`.
- **Test 3:** Correct the import statement in the `pathfinder` tool and re-run it.
- **Result 3:** FAILED. The tool still produced no output, indicating another silent crash.
- **Conclusion:** The typo was one problem, but not the only one.
- **Hypothesis 4:** The `ET.fromstring(map_xml_string)` call is the source of the silent crash.
- **Test 4:** Overwrite the tool with a script that *only* attempts to parse the XML and prints a success/failure message.
- **Result 4:** SUCCESS. The XML parsing script ran without error.
- **Conclusion:** The silent crash occurs *after* the XML is parsed but *before* the A* search begins.
- **Hypothesis 5:** The crash is occurring during the player position finding, grid generation, or A* initialization phases.
- **Test 5:** [PENDING] Restore the full script with hyper-granular print statements at every stage of the setup process to pinpoint the exact line of failure.