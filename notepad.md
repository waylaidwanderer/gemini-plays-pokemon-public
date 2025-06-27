# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Current Plans & Hypotheses
- **Corrective Action:** My previous "maze-solving algorithm" was based on a flawed interpretation of a system notice and has been discarded.
- **Current Strategy:** I will now rely on my `navigation_agent` for complex pathfinding and trust my direct observations of tile mechanics. My goal is to navigate to Violet City.

## Game Mechanics & Discoveries

### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.
- **World Knowledge Graph:** I must use `manage_world_knowledge` every time I transition between maps to keep my internal world map accurate.
- **Dynamic Map Tiles:** On Route 29, some tiles can dynamically change (e.g. WALL -> LEDGE) as I move nearby. I must mark these with ⚠️.
- **Custom Agents:** My `navigation_agent` is the primary tool for pathfinding in areas with complex mechanics like ledges.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics
- **WALL:** Impassable.
- **FLOOR:** Traversable.
- **TALL_GRASS:** Traversable, wild encounters.
- **HEADBUTT_TREE:** Impassable.
- **CUT_TREE:** Impassable, requires HM 'Cut'.
- **DOOR:** Warp tile.
- **LEDGE / HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** These tiles appear to be one-way traversal paths based on direct observation. My previous assumption that they were bidirectional was incorrect. I will trust my `navigation_agent` to handle these correctly.
- **WATER:** Impassable, likely requires HM 'Surf'.
- **VOID:** Impassable boundary tile.
- **WARP_CARPET_DOWN:** Warp tile.

## Roadblocks & Re-evaluation
- **Route 29 Dead End:** My `navigation_agent` has confirmed that the path to Cherrygrove City is currently blocked by a `CUT_TREE` at (21, 11). I cannot proceed west on this route until I acquire the HM 'Cut'.
- **Strategy Pivot:** My previous goal to reach Violet City is on hold. My new primary objective is to find the HM 'Cut'.

## Agent & Navigation Failures
- **Navigation Agent Unreliable on Route 29:** After multiple refinements and failures (providing paths into walls, ledges, and incorrectly declaring 'no path found'), the `navigation_agent` has been deemed unreliable for this specific map. I am now disregarding its output for Route 29.
- **New Navigation Strategy:** I will now use the system-mandated maze-solving algorithm (always turn left at an intersection; if blocked, turn right) to navigate complex areas like this one.