# Pokémon Crystal Journey

## My Pokémon Party
- **Hestia (Cyndaquil):** TACKLE, LEER, SMOKESCREEN, EMBER (Fire-type).
- **Vermin (Rattata):** TACKLE, TAIL WHIP
- **Hedwig (Hoothoot):** TACKLE, GROWL

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Current Plans & Hypotheses
- **Objective:** Return to Professor Elm in New Bark Town with the Mystery Egg.
- **Reasoning:** Professor Elm called urgently. This is the main story quest. The path east is blocked by one-way ledges, so I must travel west through Cherrygrove City.
- **Immediate Steps:**
    1. Navigate through Route 29 to reach Cherrygrove City.
    2. Travel from Cherrygrove City to New Bark Town.
    3. Enter Professor Elm's Lab and speak to him.

### Untested Assumptions to Verify
- The path north on Route 30 will open after speaking with Elm.
- The Guide Gent is not permanently gone; he will appear in his house later.

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
- **LEDGE:** A one-way barrier that can only be jumped over from the higher side.
- **HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** One-way ledge tiles that can only be traversed in the specified direction.
- **Dynamic Map Tiles:** On Route 29, some tiles initially appearing as WALLs can dynamically change to LEDGEs as I move nearby. This can interrupt pathing and requires caution. I must mark these as I find them.
- **BUOY:** Encountered in Cherrygrove City. Need to test if it's a hard wall or if it can be interacted with.

## Agent & Tool Development

### Current Tools & Agents
- **`navigation_agent` (ACTIVE):** A sophisticated pathfinding agent that correctly understands complex tile mechanics like ledges. It has proven reliable, and its outputs should be trusted.
- **`pathfinder_tool` (DEPRECATED):** This tool does not correctly interpret ledge traversal and should not be used.
- **`map_analyzer_agent`:** Analyzes a pre-processed list of unseen tile coordinates to identify clusters for exploration.

### Future Development Ideas
- **`battle_strategist_agent`:** Suggests the optimal move in difficult battles.
- **`party_manager_agent`:** Suggests party composition and healing needs.
- **`auto_repel_tool`:** A tool to automatically use a Repel from the bag.

## Archived Notes & Lessons Learned
- **`puzzle_solver_agent` Hallucinations:** An early agent repeatedly provided incorrect advice based on the wrong map and player abilities. It was deleted after multiple failed refinement attempts. Lesson: Agents require very specific, context-rich prompts to be effective.