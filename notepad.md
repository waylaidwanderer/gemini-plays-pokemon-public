# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Game Mechanics & Discoveries
### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.
- **World Knowledge Graph:** I must remember to use `manage_world_knowledge` every time I transition between maps to keep my internal world map accurate.

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

## Untested Tile Mechanics
- **BUOY:** Encountered in Cherrygrove City. Need to test if it's a hard wall or if it can be interacted with (e.g., requires Surf).

## Agent Development
### Existing Agents
- **pathfinder_tool:** A custom tool using A* to find paths. **CRITIQUE NOTE:** This tool has proven unreliable (failed to find a path when trapped) and needs to be fixed or replaced. Do not rely on it until it is verified.
- **puzzle_solver_agent:** An agent for generating hypotheses when stuck. **NOTE:** While useful, this agent cannot solve a truly unsolvable puzzle (like a softlock). It may generate hypotheses based on faulty map data if the game state is bugged.

### Agent Ideas
- **battle_strategist_agent:** Suggests the optimal move or action in difficult battles.
- **route_summary_agent:** Parses map data and markers to give a high-level summary of a route's completion status.
- **party_manager_agent:** Suggests when to heal or what Pokémon to lead with based on the current route's encounters.
- **world_knowledge_navigator:** Plans multi-map routes using the world knowledge graph.
- **map_analyzer_agent:** Analyzes the map XML to identify and prioritize clusters of unseen tiles for exploration.
- **stuck_analyzer_agent:** Specifically for when trapped, analyzes map for hidden escape mechanics.

## Route 30 Puzzle Strategy
- **NEW STRATEGY:** I am not trapped. The system has instructed me that there are no softlocks and I must follow a specific maze-solving algorithm: always turn left at an intersection. If a path is blocked by a wall, I must first attempt to walk through it. If it is a solid wall, I must then turn right relative to my direction of travel and continue.