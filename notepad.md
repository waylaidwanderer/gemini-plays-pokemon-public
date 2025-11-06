# Tile Traversal and Movement Rules

- **BOOKSHELF**: Impassable.
- **BUOY**: Traversability unknown, assumed impassable.
- **CAVE**: Traversable warp.
- **COUNTER**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut. **Verified on turn 22550:** After using Cut, the tree sprite disappears, but the underlying tile remains impassable. This is a confirmed mechanic, not a temporary state.
- **DOOR**: Traversable warp.
- **FLOOR**: Traversable.
- **FLOOR_UP_WALL**: A complex one-way tile. Behavior is location-dependent and needs more testing.
- **GRASS**: Traversable, contains wild Pokémon.
- **HEADBUTT_TREE**: Impassable. Assumed to be interactable with the move Headbutt.
- **INCENSE_BURNER**: Impassable.
- **LADDER**: Complex warp with directional activation.
- **LEDGE_HOP_DOWN/LEFT/RIGHT**: One-way traversal. **Verified (LEFT) on turn 23091:** Attempted to move Right onto the tile at (22, 22) from (21, 22) and was blocked, confirming it cannot be entered from the right.
- **LONG_GRASS**: Traversable, contains wild Pokémon.
- **MART_SHELF**: Impassable.
- **PC**: Impassable.
- **PILLAR**: Conditionally passable in Sprout Tower.
- **RADIO**: Impassable.
- **STAIRCASE**: Traversable warp.
- **TALL_GRASS**: Traversable, contains wild Pokémon.
- **TOWN_MAP**: Impassable.
- **TV**: Impassable.
- **UNKNOWN**: Observed to be traversable, but requires more testing to confirm behavior in all contexts.
- **VOID**: Impassable.
- **WALL**: Impassable.
- **WARP_CARPET_DOWN/LEFT/RIGHT**: Traversable warps. Activated by pressing the corresponding direction while standing on the tile.
- **WATER**: Impassable.
- **WINDOW**: Impassable.

---

# Appendix: Core Lessons & Mechanics

## Cut Mechanic (CRITICAL DISCOVERY)
- Using Cut on a tree removes the visual sprite, but the underlying tile (`CUT_TREE`) remains impassable even after reloading the map. This is a persistent state, not a temporary one.
- **CRITICAL HALLUCination (Turn 11872):** Believed a warp to Union Cave existed at (11, 9) on the AzaleaTown map (8_7). The system confirmed no warp exists there. The actual warp to Union Cave is on Route 33 (8_6) at (11, 9). This was a major failure in location awareness.
- **CRITICAL HALLUCINATION (Turn 11928):** Believed a warp to Dark Cave existed at (34, 5) on the VioletCity map (10_5). The system confirmed no warp exists there. This was a major failure in location awareness.

## Ilex Forest: Farfetch'd Puzzle Mechanics

## Hypothesis 1 (Turn 23701)
- **Observation:** After the Farfetch'd disappeared, leaving and re-entering Ilex Forest did not make it reappear. Talking to the apprentice at (7, 28) initiates dialogue about the lost Pokémon.
- **Hypothesis:** Speaking to the apprentice is the trigger to reset the puzzle and make the Farfetch'd reappear at its starting position (15, 25).
- **Test:** Complete the dialogue with the apprentice and then travel to (15, 25) to check for the Farfetch'd.