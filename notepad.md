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

## Insights & Corrections
- My biggest obstacle is my own memory. I must only trust in-game observation.
- Stunning an NPC can break scripted events, causing dialogue loops.
- The 'Poké Ball machine' was a hallucination.

### Elm's Lab Puzzle - Archived Failed Hypotheses
A comprehensive list of failed attempts has been archived to improve readability. The core summary is that all simple interaction (NPCs, objects, sequences) and movement triggers (all accessible tiles) have been exhaustively tested and have failed to progress the game. Repeating these actions is not a valid strategy.
- Attempting to leave the lab.
- Stepping on all floor tiles.
- Walking into the corner behind the bookshelves.

- **Direct Interaction (Post-State Change 3 - after talking to son):**
  - Attempt 18: Talk to Prof. Elm from the front. (Result: Dialogue loop with wife).
- **Direct Interaction (Post-State Change 4 - after talking to son again):**
  - Attempt 19: Interact with Poké Ball machine. (Result: No effect).

## Insights & Corrections
- My biggest obstacle is my own memory. I must only trust in-game observation.
- The 'Poké Ball machine' was a hallucination and does not exist in this room.

## Refactored Notes (To Be Integrated)

### Insights & Corrections
- My biggest obstacle is my own memory. I must only trust in-game observation.
- Stunning an NPC can break scripted events, causing dialogue loops.
- The 'Poké Ball machine' was a hallucination.

### Elm's Lab Puzzle - Archived Failed Hypotheses
A comprehensive list of failed attempts has been archived to improve readability. The core summary is that all simple interaction (NPCs, objects, sequences) and movement triggers (all accessible tiles) have been exhaustively tested and have failed to progress the game. Repeating these actions is not a valid strategy.

## Core Assumptions & Alternative Hypotheses
- **Assumption:** I must get a Pokémon in Elm's Lab to progress the game.
- **Alternative:** The game may require me to leave the lab and trigger a different event in New Bark Town before I can receive a Pokémon. This should be tested if all in-lab hypotheses are exhausted.