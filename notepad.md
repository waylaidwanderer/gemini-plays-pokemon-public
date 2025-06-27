# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Current Strategy & Roadblocks
- **Primary Roadblock:** My path to Violet City is blocked by `CUT_TREE`s on Route 29 (at 21, 11) and Route 30 (at 8, 6). I cannot proceed until I acquire the HM 'Cut'.
- **Current Strategy:** My goal is to find the HM 'Cut'. I am currently navigating the complex maze of Route 29 using the `maze_solver_agent` after the `navigation_agent` proved unreliable. The eastern plateau of this route is a confirmed dead end.

## Game Mechanics & Discoveries

### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.
- **World Knowledge Graph:** I must use `manage_world_knowledge` every time I transition between maps to keep my internal world map accurate.
- **Agent Pivoting:** If an agent repeatedly fails (like the `navigation_agent` on Route 29), I must pivot to a different, more suitable agent or strategy (`maze_solver_agent`).

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics
- **WALL, HEADBUTT_TREE, VOID, CUT_TREE:** Impassable. CUT_TREE requires HM 'Cut'.
- **WATER:** Impassable, likely requires HM 'Surf'.
- **FLOOR, TALL_GRASS:** Traversable.
- **DOOR, WARP_CARPET_DOWN:** Warp tiles.
- **LEDGE / HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** One-way traversal tiles. It is impossible to move *onto* these tiles from an adjacent tile. They can only be exited in their specified direction. Confirmed impassable entry points are marked on the map (e.g., (43,9), (38,13)).