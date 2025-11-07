# Game Mechanics & Systems

## Tile Traversal Rules
- **Impassable:** BOOKSHELF, BUOY (assumed), COUNTER, CUT_TREE, HEADBUTT_TREE, INCENSE_BURNER, MART_SHELF, PC, PILLAR (usually), RADIO, TOWN_MAP, TV, VOID, WALL, WATER, WINDOW.
- **Traversable:** FLOOR, GRASS, LONG_GRASS, TALL_GRASS, UNKNOWN.
- **Warps:** CAVE, DOOR (conditional), LADDER (directional), WARP_CARPET (directional), WARP_CARPET_UP (directional), WARP_CARPET_DOWN (directional, sometimes one-way), WARP_CARPET_RIGHT (directional).
- **One-Way:** FLOOR_UP_WALL, LEDGE_HOP (directional).

## Evolution Methods
- Some POKEMON evolve only by being traded: MACHOKE, KADABRA, HAUNTER, and GRAVELER.

---

# Appendix: Core Lessons & Puzzles

## Cut Mechanic (CRITICAL DISCOVERY)
- Using Cut on a tree removes the visual sprite, but the underlying tile (`CUT_TREE`) remains impassable even after reloading the map. This is a persistent state.

## Ilex Forest Puzzle
- The correct solution involved a multi-stage chase, herding the Farfetch'd through the forest by interacting with it from specific directions and using twig piles to alter its path, ultimately leading it to its owner's apprentice.

## HEADBUTT_TREE Mechanics Test
- **Observation:** The `HEADBUTT_TREE` tile type is impassable.
- **Hypothesis 1 (Turn 24065):** The `HEADBUTT_TREE` is an interactable object that responds to the 'A' button.
- **Test:** Stood at (25, 4), faced down, and pressed 'A' on the tree at (25, 5).
- **Result:** No text appeared, and no action occurred.
- **Conclusion:** Hypothesis 1 is FALSE. The tree does not respond to a standard 'A' button interaction. It is likely that the move 'Headbutt' is required to interact with these trees. For now, they are impassable obstacles.

## Goldenrod Dept. Store B1F Puzzle
- **Conclusion:** The puzzle was solved by repeatedly using the elevator to leave and re-enter the basement, which triggered box movements. A final interaction with the Machop completed the sequence, although a visual bug left impassable collision where the boxes used to be.

## Day-Care & Unown
- The Day-Care Lady on Route 34 mentioned my 'Glyph' has 'grown a lot'. This dialogue triggered even without an Unown in my party, suggesting it's tied to the Pokedex entry for Unown. She seems connected to the Ruins of Alph mystery.

## Route 34 - Day-Care Yard
- A hidden SUPER POTION at (17, 19) is currently blocked by a Pokémon sprite and is unobtainable. Repeated 'A' presses only re-trigger the Pokémon's dialogue.

## Untested Assumptions & Alternative Hypotheses
- **Goldenrod Dept. Store B1F Puzzle:**
  - **Assumption:** The puzzle is bugged or unsolvable, as the box collision remains after they visually disappear.
  - **Alternative Hypothesis:** There is a different, undiscovered trigger for the final phase of the puzzle. The visual change was a clue. The trigger might involve talking to another NPC, having a specific item/Pokémon, or an event outside the basement.
  - **Test to Falsify:** After exhausting other objectives in Goldenrod, I will return to the Dept. Store and systematically test new potential triggers.

## Goldenrod City - Pokemon Center 2F (Link Club)
- **Observation:** The second floor contains five rooms, each with a warp. All entrances are currently blocked by Link Receptionist NPCs.
- **Clue:** A receptionist at (13, 3) stated, 'the TIME CAPSULE is being adjusted.'
- **Conclusion:** These rooms are related to the 'Time Capsule' feature and are inaccessible at this time. I have investigated them as much as is currently possible.

## Goldenrod City Tile Mechanics
- **FLOOR**: Traversable. Verified in Goldenrod City.
- **WALL**: Impassable. Verified in Goldenrod City.
- **WATER**: Impassable. Verified in Goldenrod City.
- **VOID**: Impassable. Verified in Goldenrod Gym.
- **DOOR**: Traversable warp. Verified in Goldenrod City.
- **WARP_CARPET_DOWN (One-Way Exit):** A specific instance of this tile at (5, 29) on map 3_54 was found to be a one-way exit, returning the player to the previous map. This suggests some warp carpets may not be bidirectional.
- **WARP_CARPET_RIGHT**: Traversable warp. Activated by pressing Right.

# Gym Information
- **Goldenrod Gym:** Normal-type. Fighting-type moves are recommended.

## Goldenrod City - Unexplored Warps
- System alerted to an unmarked warp at (29, 5) on map 11_2. Need to investigate.

## Side Quests
- GINA on Route 34 has an item for me. (Re-added after accidental deletion)
- Snubbull is a Normal-type Pokémon.