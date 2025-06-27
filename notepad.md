# Pokémon Crystal Journey

## My Pokémon Party
- **Hestia (Cyndaquil):** TACKLE, LEER, SMOKESCREEN, EMBER (Fire-type).
- **Vermin (Rattata):** TACKLE, TAIL WHIP
- **Hedwig (Hoothoot):** TACKLE, GROWL

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Current Plans & Hypotheses
- **Objective:** Return to Professor Elm in New Bark Town with the Mystery Egg.
- **Reasoning:** I am currently in what appears to be an isolated southern pocket of Route 29. The system has explicitly stated I am not trapped and that there are no one-way paths. My previous assumptions about ledges were incorrect.
- **Current Strategy:** I will employ the system-mandated maze-solving algorithm to find the exit. The rule is: always turn left at an intersection; if an obstacle is encountered, attempt to walk through it. If it is truly impassable, turn right relative to the direction of travel and continue.

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
- **HEADBUTT_TREE:** An impassable tree.
- **WATER:** An impassable body of water, likely requires HM 'Surf'.
- **VOID:** An impassable boundary tile.
- **WARP_CARPET_DOWN:** A warp tile at building entrances/exits.
- **LEDGE (Mechanics Unconfirmed):** The system has stated there are no one-way paths. My previous experiment showing them as one-way was flawed. I must re-test this mechanic under different conditions.
- **HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** The mechanics of these tiles are also unconfirmed and must be re-tested.
- **Dynamic Map Tiles:** On Route 29, some tiles initially appearing as WALLs can dynamically change to LEDGEs as I move nearby. This is a critical mechanic to track with map markers.

## Agent & Tool Development

### Current Tools & Agents
- **`navigation_agent` (SUSPENDED):** This agent's logic is based on a flawed understanding of ledge mechanics. I will not use it until I have re-verified and corrected the traversal rules.
- **`pathfinder_tool` (DEPRECATED):** This tool is obsolete.

### Future Development Ideas
- **`maze_solver_agent`:** Automate the 'left-hand rule' exploration strategy.
- **`map_preprocessor_tool`:** A tool to parse the `map_xml_string` and provide a simplified grid to an agent.