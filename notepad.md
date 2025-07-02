# Gem's Pokémon Crystal Notepad

## I. Game Mechanics & Systems

### Tile Traversal Rules (Verified)
- **Impassable:** WALL, VOID, CUT_TREE, WATER, HEADBUTT_TREE, PC, COUNTER, PILLAR, BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW.
- **Traversable:** FLOOR, GRASS.
- **Standard Warps:** DOOR, CAVE, LADDER, WARP_CARPET_DOWN, WARP_CARPET_LEFT.
- **WARP_CARPET_RIGHT:** Confirmed bidirectional warp. Activated by stepping onto the tile.
- **One-Way Down Ledges:** LEDGE, FLOOR_ALLOW_HOP_DOWN, FLOOR_ALLOW_HOP_DOWN_LEFT, FLOOR_ALLOW_HOP_DOWN_RIGHT (Cannot be climbed up).
- **Complex One-Way Tiles:** FLOOR_UP_WALL (Can only be entered from below, but not exited up or down. Sideways movement is permitted).

### Tile Mechanics Verification Log
*This log tracks every unique tile type encountered and its verified behavior.*
- **AzaleaTown (8_7):**
  - `FLOOR`: Traversable (Verified)
  - `WALL`: Impassable (Verified)
  - `HEADBUTT_TREE`: Impassable (Verified)
  - `WARP_CARPET_LEFT`: Warp (Verified)
  - `DOOR`: Warp (Verified)
  - `CAVE`: Warp (Verified)
  - `LEDGE`: One-way down (Verified)
  - `WALL`: Impassable (Verified)
  - `HEADBUTT_TREE`: Impassable (Verified)
  - `WARP_CARPET_LEFT`: Warp (Verified)
  - `DOOR`: Warp (Verified)
  - `CAVE`: Warp (Verified)
  - `LEDGE`: One-way down (Verified)
  - `WALL`: Impassable (Verified)
  - `HEADBUTT_TREE`: Impassable (Verified)
  - `WARP_CARPET_LEFT`: Warp (Verified)
  - `DOOR`: Warp (Verified)
  - `CAVE`: Warp (Verified)
  - `LEDGE`: One-way down (Verified)

### Key Learnings
- HMs must be used from the PACK menu.
- HM moves are permanent.
- All map objects (NPCs, items, signs) act as walls.

## II. Quest Progression

### Current Objective: Clear Team Rocket from Azalea Town
- **Status:** I am currently exploring Ilex Forest, which seems connected to the Farfetch'd quest needed to get the HM for CUT. This HM is required to advance past the tree blocking the path to the western part of the forest.

### Blocked Path: Ilex Forest West
- **Status:** The western part of Ilex Forest is blocked by a tree that requires CUT. I will return here after obtaining the HM.

## III. Strategy & Planning

### Ilex Forest Farfetch'd Puzzle
- **Goal:** Herd the Farfetch'd to the boy who ran off, likely waiting near the CUT tree at (8, 25).
- **Status Update:** My `farfetchd_herder` tool has confirmed the Farfetch'd is no longer on this map. This strongly suggests the puzzle in this area is complete.

### [ARCHIVED] Ilex Forest Puzzle Hypotheses
- **Hypothesis 1 (H1 - Top Priority):** Find the Farfetch'd's current location. From there, use the twigs at (22, 30) and (23, 30) to herd it towards the western ledge at (21, 22), as the Farfetch'd can likely cross terrain that is impassable for the player.
- **Hypothesis 2 (H2):** Systematically test each twig to map out the Farfetch'd's movement rules. It may move in a fixed direction (e.g., always north, or always away from the twig) each time a specific twig is stepped on, which will allow you to control it precisely.
- **Hypothesis 3 (H3 - FAILED):** Return to the exact tile where the boy 'vanished' and the Farfetch'd first appeared at (22, 29). Use the 'interact' button on this specific tile, as moving the Farfetch'd may have triggered a change or revealed an item.
- **Hypothesis 4 (H4):** Herd the Farfetch'd towards the one-way warp tile that trapped you in this area. The warp might function as an exit for the Farfetch'd, even if it is a one-way entrance for the player.

## IV. Tool Development Notes

### `farfetchd_herder`
- **Status:** Updated and functional. Now correctly searches the map for the Farfetch'd object before attempting any herding logic.
- **Complex Warps:** Some warps, like the 1x2 WARP_CARPET_RIGHT in Ilex Forest, may have special activation conditions (e.g., only one of the tiles is an exit).
- **Impassable:** BOOKSHELF, TV, RADIO, TOWN_MAP, WINDOW.