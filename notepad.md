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
## Insights & Corrections
- My biggest obstacle is my own memory. I must only trust in-game observation.
- Stunning an NPC (Professor Elm) can break scripted events, causing dialogue loops.
- The 'Poké Ball machine' was a hallucination and does not exist in this room.

### Elm's Lab Puzzle - Failed Hypotheses Summary
- Exhausted all simple interaction and movement hypotheses. This includes talking to all NPCs from multiple positions, interacting with all objects in various sequences, and testing for movement triggers in all accessible areas. Repeating these actions is not a valid strategy.
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

## Insights & Corrections
- My biggest obstacle is my own memory. I must only trust in-game observation.
- The 'Poké Ball machine' was a hallucination and does not exist in this room.