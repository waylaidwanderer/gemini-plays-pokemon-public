# Gem's Pokémon Crystal Adventure!

## Game Plan
- Complete Professor Elm's errand by visiting MR. POKéMON.
- Find out what the "mystery" is at MR. POKéMON's house.

## Tile Mechanics
*This section consolidates all observed tile behaviors.*

### Confirmed Traversable
- `TYPE_3fe2`: Standard floor tile.
- `TYPE_ffbb`: Doormat warp tile. Acts as an exit/entrance from a building.

### Confirmed Impassable
- `TYPE_2889`: Wall or solid object.
- `TYPE_1dc2`: Wall/object.
- `TYPE_a82`: PC.
- `TYPE_1fdc`: TV.
- `TYPE_201b`: Building doorway tile. Appears impassable from the outside.
- `TYPE_4e8c`: Edge of water.
- `TYPE_80fc`: Edge of water.

### Confirmed Warp
- `TYPE_17bc`: Stairs.
- `TYPE_ffbb`: Doormat warp tile.

## Town Map Puzzle
- **Observation:** After interacting with the bookshelf at (6, 0), all movement was blocked.
- **Initial Incorrect Hypothesis:** I was soft-locked by a story event.
- **Corrected Observation:** The screen displayed text ('SILVER CAVE') that did not match the current location (PlayersHouse2F). This indicates I was viewing the Town Map, not the overworld.
- **New Hypothesis:** Pressing 'B' (the cancel/back button) will close the Town Map view.
- **Lesson Learned:** Screen elements beyond transcribed text are critical. An unexpected screen display signals a change in game state that may alter input controls.

- **Hypothesis 1 (Re-test):** Walk directly left onto stair tile `TYPE_2889` at (0, 4) after viewing the Town Map.
- **Result:** Failed. Movement was blocked.
- **Conclusion:** Viewing the Town Map did not change the properties of the stair tiles. `TYPE_2889` remains impassable. This hypothesis is definitively false.

- **Hypothesis 5 (New):** The warp trigger is an invisible event on a traversable floor tile at the top landing of the stairs.
- **Test 1:** Stand on tile (1, 4). Result: No event.
- **Test 2 Plan:** Move to and stand on tile (1, 5).
- **Test 2:** Stand on tile (1, 5). Result: No event.
- **Conclusion:** Hypothesis 5 is false. Standing on the floor tiles at the top of the stairs does not trigger a warp.

- **Hypothesis 6 (New):** The way forward is unlocked via the main menu, which may have updated after viewing the Town Map.
- **Test 1 Plan:** Press 'Start' to open the menu and inspect it for new options or items.

- **Hypothesis 7 (From `puzzle_solver`):** Interacting with the bed will trigger a story event.
- **Test 1:** Faced bed from (1, 4) and pressed 'A'.
- **Result:** No event triggered.
- **Conclusion:** Hypothesis 7 is false. Interacting with the bed does not advance the story.

## Puzzle Update: Radio Success!
- **Hypothesis (from `puzzle_solver`):** Interact with the radio.
- **Test:** Interacted with the radio at (3, 1).
- **Result:** Triggered the 'PROF.OAK'S POKéMON TALK!' dialogue.
- **Conclusion:** This is the correct story trigger! The current objective is to advance through this dialogue.

## Current Puzzle: Leaving the Bedroom

**Key Discovery:** Interacting with the radio at (3, 1) triggers a story event ('PROF.OAK'S POKéMON TALK!'). This appears to be the main trigger, but its effect is unknown.

**Post-Radio Failed Hypotheses:**
- The stairs were not unlocked immediately after the event.

- Opening/closing the main menu after the event did not unlock the stairs.

- The 'OPTION' menu did not contain any new settings.

- The PC interaction was unchanged after the radio event; it still triggered the TV.
- The SELECT button on the radio only displayed a generic help message.
- **Hypothesis (from `puzzle_solver`):** Interacting with the radio and then using a directional button would unlock the stairs.
- **Test:** Interacted with radio, pressed 'Right'. The dialogue box closed (a new result), but the stairs at (0, 4) remained impassable.
- **Conclusion:** This hypothesis is false.
- **Hypothesis (from `puzzle_solver`):** A timed event will occur if I wait in the room.
- **Test:** Waited for 3 turns in the center of the room.
- **Result:** No event triggered.
- **Conclusion:** Hypothesis is false.
- **Hypothesis (from `puzzle_solver`):** The radio event updated the character status screen with a new objective.
- **Test:** Opened the main menu and selected 'GEC' to view the status screen.
- **Result:** The status screen was normal, with no new information or options.
- **Conclusion:** Hypothesis is false.

## Untested Tile Types
- `TYPE_989e` (Neighbor's House - Bookshelf?)
- `TYPE_4a21` (Neighbor's House - Chair?)
- `TYPE_9f3` (Elm's Lab - Starter Machine?)
- `TYPE_a82` (Elm's Lab - PC?)
- `TYPE_1fdc` (Elm's Lab - TV?)

## General Lessons
- **Lesson on Scripted Events:** During a cutscene or scripted event, the game state (like party composition) might appear strange. Don't try to debug this mid-event. The priority is to advance the dialogue and wait for the event to conclude, as the state will likely normalize afterward.
- `TYPE_9f3`: Elm's Lab - Starter Machine. Impassable.
- `TYPE_a82`: Elm's Lab - PC. Impassable.
- `TYPE_1fdc`: Elm's Lab - TV. Impassable.

## General Lessons
- **Lesson on Positional Awareness:** Always verify my current position against the Game State before planning a path, especially after a potential screen transition or cutscene, to avoid hallucinations.

## Missing Pokémon Puzzle
- **Hypothesis 3 (from `puzzle_solver`):** Speak to Professor Elm again.
- **Test:** Interacted with Professor Elm at (5, 4).
- **Result:** He repeated his original dialogue about the errand for MR. POKéMON.
- **Conclusion:** Hypothesis 3 is false for Professor Elm. The dialogue has not changed.

## Missing Pokémon Puzzle
- **Hypothesis 3 (from `puzzle_solver`):** Speak to Professor Elm's aide.
- **Test:** Interacted with the aide at (1, 5).
- **Result:** No new dialogue was triggered.
- **Conclusion:** Hypothesis 3 is false. Neither Elm nor his aide have new dialogue.