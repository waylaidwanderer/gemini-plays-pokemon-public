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
- **WALL:** An impassable obstacle.
- **FLOOR:** A standard, traversable tile.
- **TALL_GRASS:** Traversable tile where wild Pokémon encounters can occur.
- **DOOR:** A warp tile that leads into and out of buildings.
- **CUT_TREE:** Impassable, requires HM 'Cut'.
- **FRUIT_TREE:** An impassable object.
- **HOP_DOWN:** A one-way ledge that can only be jumped down from above.
- **VOID:** An impassable boundary tile.
- **WARP_CARPET_DOWN:** A warp tile at building entrances/exits.
- **HEADBUTT_TREE:** An impassable tree.
- **WATER:** An impassable body of water, likely requires HM 'Surf'.

### Untested Tile Mechanics
- **BUOY:** Encountered in Cherrygrove City. Need to test if it's a hard wall or if it can be interacted with.

## Agent & Tool Development

### Custom Agents
- **puzzle_solver_agent:** Generates hypotheses when stuck. Has proven to be very effective at identifying story-based progression blockers.
- **map_analyzer_agent:** Analyzes map XML to identify clusters of unseen tiles for exploration. Requires `map_xml_string` as input.

### Custom Agent Ideas
- **battle_strategist_agent:** Suggests the optimal move in difficult battles.
- **route_summary_agent:** Parses map data to summarize a route's completion status.
- **party_manager_agent:** Suggests party composition and healing needs.
- **world_knowledge_navigator:** Plans multi-map routes using the world knowledge graph.

## Current Plans
- **Objective:** Trigger the Rival battle and return to Professor Elm.
- **Agent Hypothesis:** My `puzzle_solver_agent` determined that I am story-locked, not physically stuck. Progress north is blocked until I backtrack and complete key events.
- **Current Strategy:** Follow the agent's highest-ranked hypotheses to progress the story.
- **Immediate Steps:**
    1. Navigate from Route 30 south to Cherrygrove City.
    2. Go to the western exit of Cherrygrove City to trigger the mandatory battle with my Rival, KAINE.
    3. After the battle, continue south through Route 29 to New Bark Town.
    4. Enter Professor Elm's Lab and speak to him.