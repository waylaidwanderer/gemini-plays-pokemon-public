# Gem's Pokémon Crystal Notepad

## I. Game & Tile Mechanics

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW
- **Traversable:** FLOOR, GRASS
- **Standard Warps:** DOOR, CAVE, LADDER
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

### World Knowledge Graph (WKG) Commitment
- **CRITICAL FAILURE:** I have completely failed to update the WKG. This is a major strategic error.
- **RESOLUTION:** I will now record **every single** inter-map transition using `manage_world_knowledge` the moment it occurs. No exceptions. This is my highest data-management priority.

## II. Quest Progression & Blockers

### Current Puzzle: Ilex Forest Gatehouse
- **Goal:** Find a way out of the Ilex Forest Azalea Gatehouse.
- **Status:** I am physically trapped on the left side of the room. The counter blocks access to the right side where the Officer is. The warps on my side of the room appear to be disabled.
- **Agent Hypotheses (Ranked):
  1. Show the hatched Togepi to the Officer at (5, 2) over the counter. (IMPOSSIBLE - cannot reach that side of the room)
  2. Place Togepi in the first party slot, then speak to the Granny at (1, 3). (IMPOSSIBLE - cannot reach that side of the room)
  3. Use the Pokégear to call other contacts. (TESTED - Calling Mom and Fisher Ralph had no effect)
  4. Search for a hidden 'protector' Pokémon in the gatehouse.
  5. Interact with every tile of the counter separating me from the Officer.

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

## III. Tool Notes
- **`path_master`:** My pathfinding tool is reliable. I must be more careful to provide it with valid, traversable coordinates as input to avoid failed calls.