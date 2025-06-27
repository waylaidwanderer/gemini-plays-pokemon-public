# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Game Mechanics & Discoveries

### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.
- **World Knowledge Graph:** I must use `manage_world_knowledge` every time I transition between maps to keep my internal world map accurate. This is a top priority.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.
- **Hestia (Cyndaquil) Moves:** TACKLE, LEER, SMOKESCREEN, EMBER (Fire-type).

### Tile & Environmental Mechanics
- **WALL:** An impassable obstacle. Cannot be walked through or interacted with (tested by pressing 'A').
- **FLOOR:** A standard, traversable tile.
- **TALL_GRASS:** Traversable tile where wild Pokémon encounters can occur.
- **DOOR:** A warp tile that leads into and out of buildings.
- **CUT_TREE:** These small trees are impassable and require the HM 'Cut' to be removed.
- **Fruit Trees:** These are impassable objects.
- **HOP_DOWN:** A one-way ledge that can only be jumped down from above.
- **VOID:** An impassable boundary tile, typically outside the playable area of a map.
- **WARP_CARPET_DOWN:** A warp tile, usually found at the entrance/exit of buildings.
- **HEADBUTT_TREE:** An impassable tree.
- **WATER:** An impassable body of water, likely requires HM 'Surf'.

### Untested Tile Mechanics
- **BUOY:** Encountered in Cherrygrove City. Need to test if it's a hard wall or if it can be interacted with (e.g., requires Surf).

## Agent & Tool Development

### Custom Agents
- **puzzle_solver_agent:** An agent for generating hypotheses when stuck. **NOTE:** This agent's prompt has been refined to consider physical constraints, making it more effective in 'trapped' scenarios. It cannot solve a truly unsolvable puzzle (like a softlock).
- **map_analyzer_agent:** Analyzes map XML provided via its `map_xml_string` input to identify and prioritize clusters of unseen tiles for exploration.

### Custom Agent Ideas
- **battle_strategist_agent:** Suggests the optimal move or action in difficult battles.
- **route_summary_agent:** Parses map data and markers to give a high-level summary of a route's completion status.
- **party_manager_agent:** Suggests when to heal or what Pokémon to lead with based on the current route's encounters.
- **world_knowledge_navigator:** Plans multi-map routes using the world knowledge graph.

## Current Plans
- **Objective:** Find the path to Violet City.
- **Current Strategy:** The eastern path around the central obstacle on Route 30 proved to be a dead-end loop. I am now backtracking to the main western path.
- **Immediate Steps:**
    1. Navigate south from the dead-end loop.
    2. Move west to get around the central trees and grass.
    3. Rejoin the main path at approximately (7, 30).
    4. Proceed north along the main path.