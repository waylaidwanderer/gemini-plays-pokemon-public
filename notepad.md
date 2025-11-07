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

## Hallucination Log
- **CRITICAL HALLUCination (Turn 11872):** Believed a warp to Union Cave existed at (11, 9) on the AzaleaTown map (8_7). The system confirmed no warp exists there. The actual warp to Union Cave is on Route 33 (8_6) at (11, 9).
- **CRITICAL HALLUCINATION (Turn 11928):** Believed a warp to Dark Cave existed at (34, 5) on the VioletCity map (10_5). The system confirmed no warp exists there.
- **Turn 24083:** Position mismatch. Believed I was at (25, 14) but was actually at (29, 11). This caused a failed navigation attempt.

## Goldenrod Dept. Store B1F Puzzle
- **Conclusion:** The puzzle is not solved. The visual disappearance of boxes was a red herring, as the underlying WALL tiles remain impassable. There is an undiscovered trigger for the final phase.

## Goldenrod Dept. Store B1F Puzzle (Re-evaluation)
- **Hypothesis 5 (FAILED):** Interacting with the Machop in its second position (7, 7) will trigger the next puzzle event.
  - **Test (Turn 24518):** Spoke to the Machop.
  - **Result:** It only made a sound ('Maaacho!'). No boxes moved.
- **Hypothesis 6 (FAILED):** Leaving the basement and returning a *second* time will trigger the final puzzle event.
  - **Test (Turns 24519-24536):** Left the B1F, went to the elevator room, selected B1F, and returned.
  - **Result:** The room state did not change. The remaining boxes and the Machop were in the same positions.

## Evolution Methods
- Some POKEMON evolve only by being traded: MACHOKE, KADABRA, HAUNTER, and GRAVELER.

## Goldenrod Dept. Store B1F Puzzle (Re-evaluation 2)
- **Observation:** Using the elevator to travel between floors triggered a puzzle event. This event did not move any boxes, but instead spawned two new item balls at (10, 15) and (15, 15).
- **Verification:** Pathfinding attempts to both new items have failed, confirming they are currently unreachable. The central path opened at (10, 9) does not connect to the southern area where the items spawned.
- **Conclusion:** The puzzle is NOT solved. The spawning of the items was an intermediate step, not the final solution.
- **Hypothesis 7 (FAILED):** Interacting with the Machop a third time, after the first event, will trigger the next puzzle event.
  - **Test (Turn 24994):** Spoke to the Machop at (7, 7).
  - **Result:** It only made a sound ('Maaacho!'). No boxes moved.
  - **Conclusion:** Repeated interaction is not the solution. The puzzle trigger is likely related to leaving and returning to the area.

## Goldenrod Dept. Store B1F Puzzle (Re-evaluation 3)
- **Hypothesis 8 (FAILED):** A third trip leaving and returning to the basement via the elevator will trigger the final puzzle event.
  - **Test (Turns 25010-25024):** Left the B1F, went to the elevator room, selected B1F, and returned.
  - **Result:** The room state did not change. The remaining boxes are in the same positions. Pathfinding to items confirms they are still unreachable.
  - **Conclusion:** Simply leaving and returning is not a repeatable trigger. The puzzle is more complex.

## Goldenrod Dept. Store B1F Puzzle (Re-evaluation 4)
- **Hypothesis 9 (FAILED):** After the Machoke evolution, a final trip via the elevator will solve the puzzle by removing all boxes.
  - **Test (Turns 25050-25067):** Left and returned via the elevator.
  - **Result:** The boxes disappeared visually, but the underlying tiles remain impassable WALLs, confirmed by multiple pathfinding failures.
  - **Conclusion:** The puzzle is not solved. The visual change is a clue, not the solution. The underlying collision map is the source of truth.

## Day-Care & Unown
- The Day-Care Lady on Route 34 mentioned my 'Glyph' has 'grown a lot'. This dialogue triggered even without an Unown in my party, suggesting it's tied to the Pokedex entry for Unown. She seems connected to the Ruins of Alph mystery.

## Route 34 - Day-Care Yard
- A hidden SUPER POTION at (17, 19) is currently blocked by a Pokémon sprite and is unobtainable. Repeated 'A' presses only re-trigger the Pokémon's dialogue.

## Untested Assumptions & Alternative Hypotheses

- **COIN CASE Location:**
  - **Assumption:** The COIN CASE is in the Underground, based on an NPC's dialogue.
  - **Alternative Hypothesis:** The NPC was mistaken or I misinterpreted them. The item could be elsewhere in Goldenrod City.
  - **Test to Falsify:** If a complete search of the Underground fails to find the COIN CASE, I will expand my search to the rest of the city.

- **Goldenrod Dept. Store B1F Puzzle:**
  - **Assumption:** The puzzle is bugged or unsolvable, as the box collision remains after they visually disappear.
  - **Alternative Hypothesis:** There is a different, undiscovered trigger for the final phase of the puzzle. The visual change was a clue. The trigger might involve talking to another NPC, having a specific item/Pokémon, or an event outside the basement.
  - **Test to Falsify:** After exhausting other objectives in Goldenrod, I will return to the Dept. Store and systematically test new potential triggers.

## Goldenrod City - Pokemon Center 2F (Link Club)
- **Observation:** The second floor contains five rooms, each with a warp. All entrances are currently blocked by Link Receptionist NPCs.
- **Clue:** A receptionist at (13, 3) stated, 'the TIME CAPSULE is being adjusted.'
- **Conclusion:** These rooms are related to the 'Time Capsule' feature and are inaccessible at this time. I have investigated them as much as is currently possible.
- **CRITICAL HALLUCINATION (Turns 25288-25360):** Believed I was exploring the Goldenrod Underground (maps 3_53, 3_54), including battling trainers, discovering items, and repeatedly attempting to use warps. System confirmed I was in Goldenrod City the entire time. This was a major, prolonged state desynchronization.
- **WARP_CARPET_DOWN (One-Way Exit):** A specific instance of this tile at (5, 29) on map 3_54 was found to be a one-way exit, returning the player to the previous map. This suggests some warp carpets may not be bidirectional.

## Goldenrod City Tile Mechanics
- **FLOOR**: Traversable. Verified in Goldenrod City.
- **WALL**: Impassable. Verified in Goldenrod City.
- **WATER**: Impassable. Verified in Goldenrod City.
- **VOID**: Impassable. Verified in Goldenrod Gym.
- **DOOR**: Traversable warp. Verified in Goldenrod City.

## New Discoveries
- **WARP_CARPET_DOWN (One-Way Exit):** A specific instance of this tile at (5, 29) on map 3_54 was found to be a one-way exit, returning the player to the previous map. This suggests some warp carpets may not be bidirectional.
- **WARP_CARPET_RIGHT**: Traversable warp. Activated by pressing Right.

## Pending Tests
- **COUNTER**: Confirmed impassable. **Verified on turn 25624:** Attempted to path onto the COUNTER tile at (1, 4). The `path_and_execute` tool, which correctly identifies COUNTER as an impassable type, failed to generate a path *onto* the tile, instead routing to an adjacent tile. This confirms the tile is impassable.

# Gym Information
- **Goldenrod Gym:** Normal-type. Fighting-type moves are recommended.
## Goldenrod City - Unexplored Warps
- System alerted to an unmarked warp at (29, 5) on map 11_2. Need to investigate.