# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW
- **Traversable:** FLOOR, GRASS
- **Standard Warps:** DOOR, LADDER, CAVE
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN (Must walk in the indicated direction to activate, 'A' button does not work).
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

## II. Quest Progression & Blockers

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

### Azalea Town Slowpoke Well Puzzle
- **Current Hypothesis:** The game has flagged Kurt as having gone to the well, even though he is visually still in his house. I need to go to the well for the event to trigger.
- **Failed Attempts Log (Consolidated):**
  1. Revealing the Farfetch'd statue in Kurt's house does not make the Rocket Grunt at the well disappear.
  2. Talking to the Rocket Grunt at the well after the Farfetch'd reveal results in the same dialogue.
  3. Talking to Kurt's apprentice after the Farfetch'd reveal results in the same dialogue.
  4. Talking to Kurt after the Farfetch'd reveal results in the same dialogue.
  5. Talking to Gramps after the Farfetch'd reveal results in the same dialogue.
  6. Visiting the well and then immediately returning to Kurt's house does not trigger a new event or dialogue.
  7. Interacting directly with the well structure is impossible as the Rocket Grunt blocks the path.
  8. A strict sequence of talking to Kurt -> apprentice -> well has been attempted and failed.

## III. Strategic Notes & Reflections
- **WKG Maintenance:** I must be more diligent about adding new connections to my World Knowledge Graph immediately upon discovering them. My memory is unreliable.
- **Dynamic Markers:** I must use dynamic markers linked to `object_id` for all moving NPCs to avoid confusion.
- **Untested Assumptions:** If I remain stuck, I will test the assumption that the solution is in Azalea Town by pivoting to my secondary goal of visiting Professor Elm.