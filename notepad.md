# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Game Mechanics & Discoveries
### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics
- **WALL:** An impassable obstacle.
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

## Agent Development
### Existing Agents
- **pathfinder_tool:** A custom tool using A* to find paths. Still under development.
- **puzzle_solver_agent:** An agent for generating hypotheses when stuck.

### Agent Ideas
- **battle_strategist_agent:** Suggests the optimal move or action in difficult battles.
- **route_summary_agent:** Parses map data and markers to give a high-level summary of a route's completion status.
- **party_manager_agent:** Suggests when to heal or what Pokémon to lead with based on the current route's encounters.
- **world_knowledge_navigator:** Plans multi-map routes using the world knowledge graph.
- **map_analyzer_agent:** Analyzes the map XML to identify and prioritize clusters of unseen tiles for exploration.

## Pokémon Encounters
### Route 30
- **Ledyba (Lv. 3):** Bug/Flying type. Observed move: TACKLE.
- **Caterpie (Lv. 3-4):** Bug type. Observed moves: TACKLE, STRING SHOT.
- **Weedle (Lv. 3):** Bug/Poison type. Observed moves: STRING SHOT, POISON STING.
- **Pidgey (Lv. 3-4):** Normal/Flying type. No moves observed.
- **Hoppip (Lv. 4):** Grass/Flying type. No moves observed.
## Untested Tile Mechanics
- **BUOY:** Encountered in Cherrygrove City. Need to test if it's a hard wall or if it can be interacted with (e.g., requires Surf).
- **HEADBUTT_TREE:** Seen on Route 30. Likely requires the move Headbutt to interact with, but need to confirm it's impassable otherwise.
## Route 30 Puzzle Strategy
- **Hypothesis (from puzzle_solver_agent):** The side 'mazes' are not paths, but triggers. Visiting a specific point in both mazes might unlock the central path.
- **Plan:**
  1. Visit western maze dead-end at (2, 26). **(Completed)**
  2. Navigate to and fully explore the eastern maze to find its trigger point. **(Completed)**
  3. Return to the central path at (6, 30) to check for changes (e.g., NPC moved, path opened).