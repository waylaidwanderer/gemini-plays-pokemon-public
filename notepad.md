# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Current Strategy & Roadblocks
- **Primary Roadblock:** My `navigation_agent` has confirmed that the path to Cherrygrove City on Route 29 is currently blocked by a `CUT_TREE` at (21, 11). I cannot proceed west on this route until I acquire the HM 'Cut'.
- **Strategy Pivot:** My previous goal to reach Violet City is on hold. My new primary objective is to find the HM 'Cut'. I will explore all other available areas.
- **Agent Trust:** I will trust my refined `navigation_agent`'s conclusions, even if they contradict general system notices. The agent's ability to analyze the specific map state is more reliable.

## Game Mechanics & Discoveries

### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.
- **World Knowledge Graph:** I must use `manage_world_knowledge` every time I transition between maps to keep my internal world map accurate.
- **Custom Agents:** My `navigation_agent` is my primary tool for pathfinding. For efficiency, I should pre-process large data like the map XML using `run_code` before passing it to the agent.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics
- **WALL, HEADBUTT_TREE, VOID:** Impassable.
- **CUT_TREE:** Impassable, requires HM 'Cut'.
- **WATER:** Impassable, likely requires HM 'Surf'.
- **FLOOR, TALL_GRASS:** Traversable.
- **DOOR, WARP_CARPET_DOWN:** Warp tiles.
- **LEDGE / HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** One-way traversal tiles. It is impossible to move *onto* these tiles from an adjacent tile. They can only be exited in their specified direction.
## Discoveries & Roadblocks
- My `navigation_agent` has confirmed that the POKE_BALL at (48, 2) on Route 29 is unreachable from the lower sections of the route. This area is likely accessed from another route or requires an HM.