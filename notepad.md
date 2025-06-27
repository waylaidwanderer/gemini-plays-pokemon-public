# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Current Strategy & Roadblocks
- **Primary Roadblock:** My path to Violet City is blocked by `CUT_TREE`s on Route 29 (at 21, 11) and Route 30 (at 8, 6). I cannot proceed until I acquire the HM 'Cut'.
- **Strategy Pivot:** My goal is to find the HM 'Cut'. I will explore all available areas.
- **Agent Trust:** I will trust my `navigation_agent`'s conclusions. My previous distrust was based on a misunderstanding of the map layout. The agent correctly identified that the eastern plateau of Route 29 was a dead end, and my subsequent successful manual navigation was only possible after I had already transitioned to the main, connected part of the route.

## Game Mechanics & Discoveries

### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.
- **World Knowledge Graph:** I must use `manage_world_knowledge` every time I transition between maps to keep my internal world map accurate.
- **Custom Agents:** My `navigation_agent` is my primary tool for pathfinding. It is highly reliable.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics
- **WALL, HEADBUTT_TREE, VOID, CUT_TREE:** Impassable. CUT_TREE requires HM 'Cut'.
- **WATER:** Impassable, likely requires HM 'Surf'.
- **FLOOR, TALL_GRASS:** Traversable.
- **DOOR, WARP_CARPET_DOWN:** Warp tiles.
- **LEDGE / HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** One-way traversal tiles. It is impossible to move *onto* these tiles from an adjacent tile. They can only be exited in their specified direction.

## Route 29 Layout
- The eastern plateau of Route 29 is a dead end, completely separated from the western part of the route by one-way ledges. The only exit from this plateau is back to New Bark Town. The POKE_BALL at (48, 2) is on an unreachable ledge in this section.