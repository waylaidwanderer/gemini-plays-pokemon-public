# Game Mechanics & Systems

## Tile Traversal Rules
- **BOOKSHELF**: Impassable.
- **BUOY**: Traversability unknown, assumed impassable.
- **CAVE**: Traversable warp.
- **COUNTER**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut. **Verified on turn 22550:** After using Cut, the tree sprite disappears, but the underlying tile remains impassable.
- **DOOR**: Typically a traversable warp. However, some instances may be impassable until a story condition is met. **Observation (Route 34 Ilex Forest Gate, map 11_23, tile (13, 41)):** A specific door was found to be impassable. This suggests conditional traversability.
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
 (Observed in Goldenrod Dept. Store).

- **TALL_GRASS**: Traversable, contains wild Pokémon.
- **TOWN_MAP**: Impassable.
- **TV**: Impassable.
- **UNKNOWN**: Confirmed to be a standard traversable floor tile.
- **VOID**: Impassable.
- **WALL**: Impassable.
- **WARP_CARPET_DOWN/LEFT/RIGHT**: Traversable warps. Activated by pressing the corresponding direction.
- **WATER**: Confirmed impassable. **Verified on turn 24006:** Attempted to move Up from (4, 14) onto the water tile at (4, 13) and was blocked.
- **WARP_CARPET_DOWN**: Traversable warp. Activated by pressing Down.
- **WARP_CARPET_UP**: Traversable warp. Activated by pressing Up.
- **WINDOW**: Impassable.

---

# Appendix: Core Lessons & Mechanics

## Cut Mechanic (CRITICAL DISCOVERY)
- Using Cut on a tree removes the visual sprite, but the underlying tile (`CUT_TREE`) remains impassable even after reloading the map. This is a persistent state, not a temporary one.

## Ilex Forest Puzzle
- **Initial State:** The puzzle involved herding a Farfetch'd. Early hypotheses involving talking to NPCs or searching twig piles failed. A full systematic search of the initial area was also performed before discovering the multi-stage nature of the puzzle.
- **Hypothesis 4 (VIA AGENT):** Agent suggested a second puzzle phase deeper in the forest.
- **Hypothesis 5 (FAILED):** Confirmed that interacting with the Farfetch'd from the wrong direction resets the second phase of the puzzle.
- **Hypothesis 6 (Turn 23851) - Trusting the Agent:** The correct solution involves repeating the steps to trigger the second chase, but then finding the correct interaction sequence in the western area to guide the Farfetch'd to the apprentice without causing a reset.

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

# Goldenrod City
- A POKEFAN_M in the Game Corner lost his COIN CASE in the UNDERGROUND. I need to find it to play the games.
- **Turn 24348:** Major location hallucination. Believed I was in Goldenrod City (11_18) at (14, 22) and tried to path to a non-existent warp at (18, 27). Was actually still in the Goldenrod Game Corner (11_19) at (2, 13).
 (Observed in Goldenrod Dept. Store).

# Goldenrod Dept. Store B1F Puzzle
- **Observation:** The basement is a warehouse with boxes (WALL tiles) blocking paths to items.
- **Hypothesis 1 (FAILED):** Interacting with the Machop at (7, 7) will trigger an event that moves the boxes.
  - **Test (Turn 24418):** Spoke to the Machop at (7, 7).
  - **Result:** It made a sound ('Maaacho!') but nothing else happened. The boxes did not move.
  - **Conclusion:** Simple interaction is not the solution.
- **Hypothesis 2 (FAILED):** The static Black Belt at (4, 8) can provide a clue or trigger the puzzle.
  - **Test (Turn 24425):** Spoke to the Black Belt at (4, 8).
  - **Result:** He said "I lose my passion for work if someone's watching. Come on, kid, scoot!". The boxes did not move.
  - **Conclusion:** This NPC is not the solution.
- **Hypothesis 3 (GAVE CLUE):** The moving Black Belt at (9, 11) provided a critical clue.
  - **Test (Turn 24437):** Spoke to the Black Belt at (9, 11).
  - **Result:** He said "Hey, kid! You're holding us up! Our policy is to work behind the scenes where no one can see us!".
  - Hypothesis 4 (FAILED): Leaving and re-entering the basement will trigger an event that moves the boxes.
  - **Test (Turn 24466):** Left the basement via the elevator and immediately returned.
  - **Result:** The boxes and NPCs were in the same positions. Nothing changed.
  - **Conclusion:** Simply re-loading the map is not the solution.
- **Hypothesis 5:** I need to leave the basement, go to a *different* floor in the department store, and then return. This might be the correct trigger for the 'behind the scenes' event.
- **Hypothesis 6 (Elevator Mechanics):** The elevator requires a two-step process. Step 1: Interact with the panel at (3, 0) to select a destination floor. Step 2: Manually walk onto one of the `WARP_CARPET_DOWN` tiles at (1, 3) or (2, 3) and press the corresponding direction (Down) to initiate travel.

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
- **DOOR**: Traversable warp. Verified in Goldenrod City.