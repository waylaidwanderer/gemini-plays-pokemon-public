# Game Mechanics & Systems

## Tile Traversal Rules
- **BOOKSHELF**: Impassable.
- **BUOY**: Traversability unknown, assumed impassable.
- **CAVE**: Traversable warp.
- **COUNTER**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut. **Verified on turn 22550:** After using Cut, the tree sprite disappears, but the underlying tile remains impassable.
- **DOOR**: Traversable warp.
- **FLOOR**: Traversable.
- **FLOOR_UP_WALL**: A complex one-way tile. Behavior is location-dependent.
- **GRASS**: Traversable, contains wild Pokémon.
- **HEADBUTT_TREE**: Confirmed impassable. Assumed to be interactable with the move Headbutt.
- **INCENSE_BURNER**: Impassable.
- **LADDER**: Complex warp with directional activation.
- **LEDGE_HOP_DOWN/LEFT/RIGHT**: One-way traversal. **Verified (LEFT) on turn 23091:** Attempted to move Right onto the tile at (22, 22) from (21, 22) and was blocked.
- **LONG_GRASS**: Traversable, contains wild Pokémon.
- **MART_SHELF**: Impassable.
- **PC**: Impassable.
- **PILLAR**: Conditionally passable in Sprout Tower.
- **RADIO**: Impassable.
- **STAIRCASE**: Traversable warp.
- **TALL_GRASS**: Traversable, contains wild Pokémon.
- **TOWN_MAP**: Impassable.
- **TV**: Impassable.
- **UNKNOWN**: Confirmed to be a standard traversable floor tile.
- **VOID**: Impassable.
- **WALL**: Impassable.
- **WARP_CARPET_DOWN/LEFT/RIGHT**: Traversable warps. Activated by pressing the corresponding direction.
- **WATER**: Confirmed impassable. **Verified on turn 24006:** Attempted to move Up from (4, 14) onto the water tile at (4, 13) and was blocked.
- **WINDOW**: Impassable.

---

# Appendix: Core Lessons & Mechanics

## Cut Mechanic (CRITICAL DISCOVERY)
- Using Cut on a tree removes the visual sprite, but the underlying tile (`CUT_TREE`) remains impassable even after reloading the map. This is a persistent state, not a temporary one.
- **CRITICAL HALLUCination (Turn 11872):** Believed a warp to Union Cave existed at (11, 9) on the AzaleaTown map (8_7). The system confirmed no warp exists there. The actual warp to Union Cave is on Route 33 (8_6) at (11, 9). This was a major failure in location awareness.
- **CRITICAL HALLUCINATION (Turn 11928):** Believed a warp to Dark Cave existed at (34, 5) on the VioletCity map (10_5). The system confirmed no warp exists there. This was a major failure in location awareness.

- **Initial State:** The puzzle involved herding a Farfetch'd. Early hypotheses involving talking to NPCs or searching twig piles failed. A full systematic search of the initial area was also performed before discovering the multi-stage nature of the puzzle.

- **Hypothesis 4 (VIA AGENT):** Agent suggested a second puzzle phase deeper in the forest.

## Hypothesis 5 (Turn 23851) - FAILED
- **Observation:** After successfully herding the Farfetch'd to the western part of the forest, interacting with it from the right at (21, 24) caused the entire puzzle to reset, returning the Farfetch'd to (15, 25).
- **Hypothesis:** Interacting from the right is the incorrect final step for the second phase of the puzzle.
- **Conclusion:** The test failed.

## Hypothesis 6 (Turn 23851) - Trusting the Agent
- **Observation:** The `puzzle_solver_assistant` previously suggested a second chase phase begins around (23, 25). My actions herded the Farfetch'd to this general area, but my final interaction was wrong, causing a reset.
- **Hypothesis:** The correct solution involves repeating the steps to trigger the second chase, but then finding the correct interaction sequence in the western area to guide the Farfetch'd to the apprentice without causing a reset. The next attempt should involve interacting from a different direction (e.g., from above or below) once the Farfetch'd is in the western area.
- **Test:**
    1. Re-solve the first part of the puzzle to move the Farfetch'd west.
    2. Once it is in the western area, approach it from a different direction than last time (e.g., from above at (20, 23)) and interact.

## HEADBUTT_TREE Mechanics Test
- **Observation:** The `HEADBUTT_TREE` tile type is impassable.
- **Hypothesis 1 (Turn 24065):** The `HEADBUTT_TREE` is an interactable object that responds to the 'A' button.
- **Test:** Stood at (25, 4), faced down, and pressed 'A' on the tree at (25, 5).
- **Result:** No text appeared, and no action occurred.
- **Conclusion:** Hypothesis 1 is FALSE. The tree does not respond to a standard 'A' button interaction. It is likely that the move 'Headbutt' is required to interact with these trees. For now, they are impassable obstacles.