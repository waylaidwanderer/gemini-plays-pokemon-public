# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified & In-Progress)
*This section is for verified mechanics. Untested tiles are in the verification plan below.*

- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW.
- **Traversable:** FLOOR, GRASS.
- **Standard Warps:** DOOR, CAVE, LADDER.
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT (Cannot be climbed up).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

### Tile Mechanics Verification Plan
*I will systematically test every new tile type encountered to confirm its properties.*

- **WARP_CARPET_LEFT:** 
  - **Hypothesis:** Activated by walking into it from the right.
  - **Status:** FAILED. Repeated attempts have not triggered the warp. 
  - **Next Step:** Must test entry from all four directions (Up, Down, Left, Right) to confirm activation conditions or if it's event-locked.
- **WARP_CARPET_RIGHT:** 
  - **Hypothesis:** Activated by walking into it from the left.
  - **Status:** FAILED. Repeated attempts have not triggered the warp. 
  - **Next Step:** Must test entry from all four directions (Up, Down, Left, Right) to confirm activation conditions or if it's event-locked.

## II. Quest Progression

### Current Objective: Get the HM for CUT

#### Ilex Forest Gatehouse Puzzle
- **Goal:** Find a way out of the Ilex Forest Azalea Gatehouse.
- **Status:** STUCK. Both warps (to Ilex Forest and Azalea Town) are currently non-functional. I am physically blocked from reaching the Officer on the right side of the room.
- **Current Hypothesis:** Showing my newly hatched Togepi to the Granny at (1, 3) will trigger a story event.
- **Failed Attempts Log:**
  1. Attempting to use the warp to Azalea Town at (9, 4) and (9,5) by walking onto it from the left. (FAILED)
  2. Attempting to use the warp to Ilex Forest at (0, 4) by walking onto it from the right. (FAILED)
  3. Talking to the Granny at (1, 3) without Togepi in the lead. (FAILED - Repeated dialogue)

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

## III. World Knowledge & Tool Notes

- **World Knowledge Graph:** I have neglected to update this. I MUST start recording every inter-map transition immediately using `manage_world_knowledge` to build a reliable world map.
- **`path_master`:** My pathfinding tool is reliable. I must be more careful to provide it with valid, traversable coordinates as input to avoid failed calls.