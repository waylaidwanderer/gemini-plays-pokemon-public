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
- **LEDGE:** A one-way barrier that can only be jumped over from one side. Its appearance can change. The system is currently updating tiles that were incorrectly displayed as WALLs to their correct LEDGE type, which can interrupt pathing.
- **HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** One-way ledge tiles that can only be traversed in the specified direction.

### Untested Tile Mechanics
- **BUOY:** Encountered in Cherrygrove City. Need to test if it's a hard wall or if it can be interacted with.

## Known Issues & Bugs
- **`puzzle_solver_agent` Hallucinations:** The agent has repeatedly provided incorrect advice based on the wrong map and player abilities. It has been deleted after multiple failed refinement attempts.
- **`pathfinder_tool` Ledge Issue:** The current pathfinder does not correctly interpret the traversal rules for LEDGE tiles, often creating invalid paths. This requires a future tool improvement.

## Agent & Tool Development

### Custom Agents
- **map_analyzer_agent:** Analyzes a pre-processed list of unseen tile coordinates to identify clusters for exploration.

### Agent & Tool Ideas
- **navigation_agent:** An improved pathfinding agent that correctly understands complex tile mechanics like ledges.
- **battle_strategist_agent:** Suggests the optimal move in difficult battles.
- **party_manager_agent:** Suggests party composition and healing needs.
- **auto_repel_tool:** A tool to automatically use a Repel from the bag.

## Current Plans & Hypotheses
- **Objective:** Return to Professor Elm in New Bark Town with the Mystery Egg.
- **Reasoning:** Professor Elm called urgently. This is the main story quest. My previous hypothesis about battling the rival in Cherrygrove was incorrect, as the path west is blocked by a non-rival NPC.
- **Immediate Steps:**
    1. Navigate manually east through Route 29 to reach New Bark Town.
    2. Enter Professor Elm's Lab and speak to him.
- **Untested Assumptions to Verify:**
    1. The path north on Route 30 will open after speaking with Elm.
    2. The Guide Gent is not permanently gone; he will appear in his house later.