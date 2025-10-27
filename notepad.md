# Gem's Pokémon Crystal Adventure Log

## Current Plan
- Test the traversability of all untested tiles in Elm's Lab (WALL, BOOKSHELF, TV, PC, WINDOW).

## Game Mechanics & Systems
*PC Storage*: Currently empty.

## Battle and Pokemon Information
*My Party*: Currently empty.
*Type Effectiveness Chart*: To be built based on battle observations.

## Area and Navigation Insights

### Tile Traversal and Movement Rules
- **FLOOR**: Traversable. (Verified)
- **DOOR**: Warp. (Verified)
- **STAIRCASE**: Warp. (Verified)
- **WARP_CARPET_DOWN**: Warp. (Verified)
- **WALL**: Impassable. (Verified)
- **BOOKSHELF**: Impassable. (Verified)
- **WINDOW**: Impassable. (Verified)
- **PC**: Impassable. Interacting from an adjacent tile can trigger events. (Verified)
- **TV**: Impassable. (Verified)
- **TOWN_MAP**: Appears impassable. (Untested)
- **WATER**: Appears impassable without Surf. (Untested)
- **HEADBUTT_TREE**: Appears impassable. (Untested)

## Obstacles and Solutions
- My own memory can be an obstacle. I must rely only on in-game observation.
- Stunning an NPC (Professor Elm) can break scripted events, causing dialogue loops.

### Elm's Lab Puzzle - Failed Hypotheses Log
*Core Problem:* Cannot trigger the event to receive a starter Pokémon.
*Verified Progression Trigger:* Interacting with the PC at (0, 1) triggered new dialogue from Professor Elm, but did not solve the puzzle.

*Failed Interaction Hypotheses:*
- Talking to Prof. Elm (multiple positions, multiple game states).
- Talking to Elm's Son (from front and back).
- Interacting with PC, then talking to Elm.
- Interacting with PC, leaving, re-entering, then talking to Elm.
- Interacting with PC, leaving, re-entering, talking to Son, then talking to Elm.
- Interacting with bookshelves (alone and after PC).
- Interacting with window.
- Interacting with the central table (confirmed non-interactable).

*Failed Movement Hypotheses:*
- Attempting to leave the lab.
- Stepping on all floor tiles.
- Walking into the corner behind the bookshelves.

## Reflection & Self-Correction
- **(Turn 103):** I have previously failed to manage data immediately and test assumptions. I must be more diligent.

- **Direct Interaction (Post-State Change 3 - after talking to son):**
  - Attempt 18: Talk to Prof. Elm from the front. (Result: Dialogue loop with wife).
- **Direct Interaction (Post-State Change 4 - after talking to son again):**
  - Attempt 19: Interact with Poké Ball machine. (Result: No effect).

### Elm's Lab Puzzle - Reflection & Correction
*Correction (Turn 264):* I have been operating under the false assumption that a "Poké Ball machine" exists in this room. It does not. All previous hypotheses involving this object are invalid. I must re-evaluate based only on observable objects.

*Verified Progression Trigger:*
- Interacting with the PC at (0, 1) triggered new dialogue from Professor Elm.

*Current Core Hypotheses:*
1. The event trigger requires another interaction with an object in the room (PC, TV, Elm, Son, etc.).
2. The event trigger requires moving to a specific tile.
3. The event trigger requires attempting to leave the lab again.