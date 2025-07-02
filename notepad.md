# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW.
- **Traversable:** FLOOR, GRASS.
- **Standard Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN, WARP_CARPET_LEFT.
- **WARP_CARPET_RIGHT:** Confirmed bidirectional warp. Activated by walking into it from the left.
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT (Cannot be climbed up).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

### Tile Mechanics Verification Plan
*I will systematically test every new tile type encountered to confirm its properties.*
- **Goal:** For each new tile type, verify if it is traversable, if it is a warp, and if it has any special movement rules (e.g., one-way).

## II. Quest Progression

### Current Objective: Get the HM for CUT

#### Slowpoke Well Puzzle
- **Goal:** Get past the Rocket Grunt at (31, 9) to enter the well at (31, 7).
- **Status:** STUCK. I have exhausted all logical conversation paths with Kurt, his apprentice, and both Rocket Grunts. My `quest_strategist` agent's top remaining hypothesis is to investigate the Ilex Forest Shrine, based on Kurt's clue about a 'forest's protector'.

- **Failed Attempts Log:**
  1. Talk to Kurt, then the well grunt, then return to Kurt. (FAILED - Kurt repeats dialogue)
  2. Talk to the well grunt, then return to Kurt. (FAILED - Kurt repeats dialogue)
  3. Talk to the gym grunt, then Kurt. (FAILED - No event triggered)
  4. Talk to Kurt's apprentice after talking to the well grunt. (FAILED - Apprentice repeats dialogue)

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree at (8, 25) that requires CUT. I will return here after obtaining the HM.

## III. Tool Development Notes

- **`path_finder_plus`:** This tool is unreliable and seems to have a flawed pathfinding algorithm. I am replacing it with `path_master`.
- **`path_master`:** A new, advanced pathfinding tool using the A* algorithm. Should be more reliable for complex navigation.