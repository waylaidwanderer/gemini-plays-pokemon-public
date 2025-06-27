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
- **LEDGE:** A one-way barrier that can only be jumped over from the higher side. Its appearance can change.
- **HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** One-way ledge tiles that can only be traversed in the specified direction.
- **Dynamic Map Tiles:** On Route 29, some tiles initially appearing as WALLs can dynamically change to LEDGEs as I move nearby. This can interrupt pathing and requires caution.

### Untested Tile Mechanics
- **BUOY:** Encountered in Cherrygrove City. Need to test if it's a hard wall or if it can be interacted with.

## Agent & Tool Development

### Current Tools & Agents
- **map_analyzer_agent:** Analyzes a pre-processed list of unseen tile coordinates to identify clusters for exploration.
- **pathfinder_tool (DEPRECATED):** The current pathfinder does not correctly interpret the traversal rules for LEDGE tiles, often creating invalid paths. It should no longer be used.

### Development Plan
- **`navigation_agent` (High Priority):** An improved pathfinding agent that correctly understands complex tile mechanics.
  - **Function:** To replace the faulty `pathfinder_tool`.
  - **Logic:** It will implement an A* search algorithm that correctly parses the map XML.
  - **Key Features:**
    1.  Correctly identify and handle one-way traversal for all `LEDGE` and `HOP_*` tile types.
    2.  Treat all `<Object>` elements as impassable walls.
    3.  Accept a list of impassable tile types as an argument for flexibility.
  - **Status:** To be defined immediately.

- **`battle_strategist_agent` (Idea):** Suggests the optimal move in difficult battles.
- **`party_manager_agent` (Idea):** Suggests party composition and healing needs.
- **`auto_repel_tool` (Idea):** A tool to automatically use a Repel from the bag.

## Current Plans & Hypotheses
- **Objective:** Return to Professor Elm in New Bark Town with the Mystery Egg.
- **Reasoning:** Professor Elm called urgently. This is the main story quest.
- **Immediate Steps:**
    1.  Define `navigation_agent` to fix pathing issues.
    2.  Use the new agent to calculate a reliable path to New Bark Town.
    3.  Enter Professor Elm's Lab and speak to him.
- **Untested Assumptions to Verify:**
    1. The path north on Route 30 will open after speaking with Elm.
    2. The Guide Gent is not permanently gone; he will appear in his house later.

## Archived Notes & Lessons Learned
- **`puzzle_solver_agent` Hallucinations:** The agent repeatedly provided incorrect advice based on the wrong map and player abilities. It was deleted after multiple failed refinement attempts. Lesson: Agents require very specific, context-rich prompts to be effective.