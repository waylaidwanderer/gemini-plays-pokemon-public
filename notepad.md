# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW
- **Traversable:** FLOOR, GRASS
- **Standard Warps:** DOOR, LADDER, CAVE
- **Directional Warps:** WARP_CARPET_LEFT, WARP_CARPET_RIGHT, WARP_CARPET_DOWN
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

### World Knowledge Graph (WKG) Commitment
- **WKG Status:** My WKG is more complete than I thought. My attempts to retroactively add edges were based on a flawed memory. I must trust my tools' data analysis over my own assumptions and be diligent about adding *new* connections moving forward.

## II. Quest Progression & Blockers

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

### Azalea Town Slowpoke Well Puzzle
- **Current Hypothesis (from `quest_strategist`):** Speak to Kurt -> Speak to Rocket Grunt at well -> Return and speak to Kurt again.
- **Failed Attempts Log:**
  1. Talking to Kurt's apprentice after Kurt leaves the house does not clear the path.
  2. Talking to the Rocket Grunt at the gym does not clear the path.
  3. Talking to the Rocket Grunt at the well and then immediately talking to Kurt does not clear the path.
  4. Leaving Kurt's house immediately after talking to him does not trigger a new event.
  5. Leaving Azalea Town and re-entering does not change Kurt's dialogue.
  6. Pathing around the Rocket Grunt at the well is impossible due to ledges.

## III. Tool Notes
- **`path_master`:** My pathfinding tool is reliable. I must be more careful to provide it with valid, traversable coordinates as input to avoid failed calls.
  7. Speaking to Kurt -> Speaking to the Rocket Grunt at the well -> Returning and speaking to Kurt again does not trigger an event.
  8. Speaking to Kurt -> Speaking to the Rocket Grunt at the well -> Returning and speaking to the apprentice does not trigger an event.