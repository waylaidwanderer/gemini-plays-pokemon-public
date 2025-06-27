# Pokémon Crystal Journey

## My Pokémon Party
- **Hestia (Cyndaquil):** TACKLE, LEER, SMOKESCREEN, EMBER (Fire-type).
- **Vermin (Rattata):** TACKLE, TAIL WHIP
- **Hedwig (Hoothoot):** TACKLE, GROWL

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Current Plans & Hypotheses
- **Objective:** Return to Professor Elm in New Bark Town with the Mystery Egg.
- **Reasoning:** I am currently on Route 29. My navigation agent has confirmed that the path east to New Bark Town is blocked by a series of one-way ledges. Therefore, the only way forward is to travel west to Cherrygrove City and then south to New Bark Town. I am currently in an isolated southern pocket of Route 29 and must find the exit.
- **Current Strategy:** Employ the 'left-hand rule' maze-solving algorithm to systematically explore the pocket I am in, starting from the westernmost point of the southern corridor at (24, 16).

### Untested Assumptions to Verify
- The path north on Route 30 will open after speaking with Elm.
- The Youngster NPC at (27, 16) has a larger-than-normal collision box or a hidden trigger that blocks adjacent tiles.

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
- **LEDGE (Confirmed One-Way):** My experiment at (42, 14) confirms that ledges are strictly one-way. It is impossible to move from a lower elevation to a higher one by jumping up a ledge.
- **HOP_DOWN:** One-way ledge tile that can only be traversed by moving down (to Y+1).
- **HOP_LEFT:** One-way ledge tile that can only be traversed by moving left (to X-1).
- **HOP_RIGHT:** One-way ledge tile that can only be traversed by moving right (to X+1).
- **HOP_DOWN_LEFT:** One-way ledge tile that can only be traversed by moving down (to Y+1) OR left (to X-1).
- **HOP_DOWN_RIGHT:** One-way ledge tile that can only be traversed by moving down (to Y+1) OR right (to X+1).
- **Dynamic Map Tiles:** On Route 29, some tiles initially appearing as WALLs can dynamically change to LEDGEs as I move nearby. This is a critical mechanic to track with map markers.

## Agent & Tool Development

### Current Tools & Agents
- **`navigation_agent` (ACTIVE - Requires Careful Use):** A sophisticated pathfinding agent. It correctly understands one-way ledge mechanics. Its failures have been due to my own errors (incomplete impassable lists, distrusting correct output). I must trust its analysis.
- **`pathfinder_tool` (DEPRECATED):** This tool does not correctly interpret ledge traversal and should not be used.

### Future Development Ideas
- **`maze_solver_agent`:** Automate the 'left-hand rule' exploration strategy.
- **`map_preprocessor_tool`:** A tool to parse the `map_xml_string` and provide a simplified grid to the `navigation_agent`.