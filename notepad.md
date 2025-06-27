# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## My Pokémon Party
- **Hestia (Cyndaquil):** TACKLE, LEER, SMOKESCREEN, EMBER (Fire-type).
- **Vermin (Rattata):** TACKLE, TAIL WHIP
- **Hedwig (Hoothoot):** TACKLE, GROWL

## Game Mechanics & Discoveries

### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.
- **World Knowledge Graph:** I must use `manage_world_knowledge` every time I transition between maps to keep my internal world map accurate. This is a top priority.
- **Map-altering events:** Some routes, like Route 29, can have their layout change due to scripted events.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics
- **WALL:** An impassable obstacle.
- **FLOOR:** A standard, traversable tile.
- **TALL_GRASS:** Traversable tile where wild Pokémon encounters can occur.
- **DOOR:** A warp tile that leads into and out of buildings.
- **CUT_TREE:** Impassable, requires HM 'Cut'.
- **FRUIT_TREE:** An impassable object.
- **VOID:** An impassable boundary tile.
- **WARP_CARPET_DOWN:** A warp tile at building entrances/exits.
- **HEADBUTT_TREE:** An impassable tree.
- **WATER:** An impassable body of water, likely requires HM 'Surf'.
- **LEDGE:** A one-way barrier that can only be jumped over from one side. Its appearance can change.
- **HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** One-way ledge tiles that can only be traversed in the specified direction.

### Untested Tile Mechanics
- **BUOY:** Encountered in Cherrygrove City. Need to test if it's a hard wall or if it can be interacted with.

## Agent & Tool Development

### Custom Agents
- **puzzle_solver_agent:** Generates hypotheses when stuck.
- **map_analyzer_agent:** Analyzes a pre-processed list of unseen tile coordinates to identify clusters for exploration. (Refined to be more efficient).

### Agent & Tool Ideas
- **battle_strategist_agent:** Suggests the optimal move in difficult battles.
- **route_summary_agent:** Parses map data to summarize a route's completion status.
- **party_manager_agent:** Suggests party composition and healing needs.
- **world_knowledge_navigator:** Plans multi-map routes using the world knowledge graph.
- **auto_repel_tool:** A tool to automatically use a Repel from the bag.

## Current Plans & Hypotheses
- **Objective:** Return to Professor Elm in New Bark Town with the Mystery Egg.
- **Reasoning:** Professor Elm called urgently. This is the main story quest. My previous hypothesis about battling the rival in Cherrygrove was incorrect.
- **Immediate Steps:**
    1. Navigate from Route 29 east to New Bark Town.
    2. Enter Professor Elm's Lab and speak to him.
- **Untested Assumptions to Verify:**
    1. The path north on Route 30 will open after speaking with Elm.
    2. The Guide Gent is not permanently gone; he will appear in his house later.