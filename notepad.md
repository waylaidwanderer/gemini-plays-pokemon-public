# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW
- **Traversable:** FLOOR, GRASS
- **Standard Warps:** DOOR, CAVE, LADDER
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).
- **WARP_CARPET_LEFT/RIGHT:** These warps are currently disabled in IlexForestAzaleaGate. Activation is likely tied to a story event/flag. All attempts to enter from any direction have failed.

## II. Quest Progression

### Current Objective: Get the HM for CUT

#### Ilex Forest Gatehouse Puzzle
- **Goal:** Find a way out of the Ilex Forest Azalea Gatehouse.
### Agent Hypotheses (Ranked):
1. Show the hatched Togepi to the Officer at (5, 2) by interacting over the counter.
2. Place the hatched Togepi in the first slot of the party, then speak to the Granny at (1, 3) again.
3. Use the Pokégear to call other contacts besides Professor Elm.
4. Search for a hidden Pokémon ('protector') in the gatehouse.
5. Interact with every tile of the counter separating me from the Officer.
  1. Attempting to use the warps at (0,4) and (0,5) by walking onto them from every possible direction (left, right, above, below). (FAILED)
  2. Talking to the Granny at (1, 3). (FAILED - Repeated dialogue)
  3. Showing my newly hatched Togepi to the Granny at (1, 3). (FAILED - No new dialogue)
  4. Interacting with all scenery (potted plants, counter). (FAILED)
  5. Using a key item (OLD ROD) on the Granny. (FAILED)
  6. Pushing the Granny. (FAILED)
  7. Stunning the Granny with `stun_npc` and attempting to walk through her or talk to her. (FAILED)
  8. Systematically walking into every wall tile to check for hidden passages. (FAILED)

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

## III. World Knowledge & Tool Notes

- **World Knowledge Graph:** I have completely failed to update this. I MUST start recording every inter-map transition immediately using `manage_world_knowledge` to build a reliable world map. This is a critical failure.
- **`path_master`:** My pathfinding tool is reliable. I must be more careful to provide it with valid, traversable coordinates as input to avoid failed calls.