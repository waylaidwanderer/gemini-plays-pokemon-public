# I. Game Mechanics & Traversal
## A. Core Rules
- **Level Cap:** 8 badges = Level 65.
- **PC Interaction:** Stand directly below the PC, face up, and press 'A'.
- **HM Usage:** HMs are used from the party menu. Fainted Pokémon can use field moves.
- **Surfing:** Not all `ground` tiles adjacent to `water` are valid starting points.
- **Puzzle Resets:** Leaving and re-entering a floor resets all boulders to their original positions.
- **Off-Screen State Changes:** An object's state will not update in the map data until it is visible on-screen.
- **Boulder Pushing:** It is possible to push a boulder by standing adjacent to it, facing it, and moving towards it (e.g., standing below at Y+1, facing up, and pressing Up to push it to Y-1). You do not need to be on the opposite side. Boulders cannot be pushed into `impassable` tiles.

## B. Tile Glossary & Movement Rules
- `ground`: Standard walkable tile.
- `grass`: Wild Pokémon encounters.
- `water`: Requires SURF.
- `impassable`: Wall.
- `ledge`: One-way traversal. Can only be jumped DOWN from the tile directly above. Acts as a wall from all other directions.
- `elevated_ground`: Walkable, different elevation. It is NOT possible to step down from an `elevated_ground` tile to an adjacent `ground` tile.
- `steps`: Allows movement between `ground` and `elevated_ground` in both directions.
- `boulder_switch`: Floor switch for boulders.
- `boulder_barrier`: Impassable barrier linked to a boulder switch.
- `cleared_boulder_barrier`: A former barrier that acts as a one-way ramp. It is possible to move from it onto `elevated_ground` (elevation 2), but it is NOT possible to move from it directly back down to `ground` or to enter it from ANY adjacent `ground` tile.
- `hole`: Drops to a lower floor. Pushing a boulder into one causes it to appear on the floor below.
- `spinner`: Forces movement.
- `ladder_up` / `ladder_down`: Warps between floors.
- `cuttable`: A tree that can be removed with the HM Cut.

# II. Battle Intel
## A. Type Effectiveness Chart (Verified)
- **Super Effective (2x):** Psychic > Ghost, Poison; Ghost > Psychic; Electric > Rock, Water; Flying > Grass, Poison, Fighting; Ice > Ground, Grass, Flying, Dragon; Ground > Poison, Fire, Electric, Rock, Ground; Rock > Fire, Ice, Flying, Bug; Fighting > Normal, Rock, Ice; Water > Fire, Ground, Rock; Grass > Water, Ground, Rock; Bug > Grass, Poison, Psychic; Poison > Grass, Bug
- **Not Very Effective (0.5x):** Normal !> Rock; Electric !> Grass, Electric, Dragon; Rock !> Psychic; Psychic !> Psychic; Poison !> Poison, Ground, Rock, Ghost; Ice !> Water, Ice, Fire; Fighting > Poison, Flying, Psychic, Bug; Water !> Water, Grass, Dragon; Grass !> Fire, Grass, Poison, Flying, Bug, Dragon
- **Immune (0x):** Flying immune to Ground; Ground immune to Electric; Ghost immune to Normal, Fighting
- **Correction:** Psychic-type moves deal NEUTRAL (1x) damage to Rock-type Pokémon.

## B. Strategic Notes
- **"No Will to Fight" Message:** A party menu cursor error on a fainted Pokémon, not a refusal to battle.
- **Victory Road Trainers:** Defeated trainers in Victory Road are PASSABLE. My previous assumption they were impassable was a hallucination proven false by system feedback.
- **Struggle Mechanic:** Struggle is only used automatically when a Pokémon is out of PP for ALL of its moves.

# III. Tool Development & Debugging
## A. Tool Status
- **`gem_pathfinder_v2` Status (Fixed):** The tool's logic has been corrected multiple times based on system feedback from Victory Road 1F.
  - It no longer incorrectly treats defeated trainers as impassable obstacles.
  - Its elevation logic now correctly enforces strict elevation rules, as the hypothesis of a map-specific exception was proven false by game feedback.
  - The tool is reliable for finding existing paths.
## B. Debugging Principles & Lessons
- **Scientific Method:** Use a scientific approach: form a hypothesis, test it, and document the conclusion.
- **Trust System Feedback:** System feedback (like warnings or tool errors) is the source of truth and MUST be trusted over personal assumptions or agent outputs.
- **IMMEDIATE ACTION:** Flaws in tools or data management (notepad, markers) must be addressed immediately, not deferred as goals.
- **Agent vs. Tool Workflow:** Agents provide strategic advice, but I am responsible for executing that advice using basic button presses. I must not invent tools (e.g., `select_battle_option`) to automate actions that are performed via manual input.

# IV. Current Plan: Return to Victory Road 1F
**Status:** Party is fully healed. I am on Route 23.
**Current Step:** My priority is to return to Victory Road 1F and solve the boulder puzzle to finally reach the Indigo Plateau.

# V. Archived Plans & Disproven Hypotheses
- **Hypothesis (Disproven):** It might be possible to step down from an `elevated_ground` tile to a `ground` tile on Victory Road 1F. **Test:** Attempted to move from (6, 10) [`elevated_ground`] to (6, 9) [`ground`]. **Result:** Movement was blocked. **Conclusion:** The rule that you cannot step down from `elevated_ground` is confirmed to be true for this map.