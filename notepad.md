# Pokémon Crystal Journey

## Key Information
- **Rival:** A red-haired boy named KAINE stole a Totodile from Professor Elm's lab.

## Current Plans & Hypotheses
- **Objective:** Return to Professor Elm in New Bark Town with the Mystery Egg.
- **Core Conflict:** My direct observations (e.g., being blocked by ledges) contradict the stickied system notice which states there are no one-way paths and I am never trapped. The notice is the highest authority.
- **Current Strategy:** I must strictly adhere to the system-mandated maze-solving algorithm to find the exit.
  - Rule 1: Always attempt to turn left at an intersection.
  - Rule 2: If an obstacle is encountered, attempt to walk through it to confirm it's impassable.
  - Rule 3: If it is truly impassable, turn right relative to the direction of travel and continue.

## Game Mechanics & Discoveries

### System Mechanics
- **Stuck on Warp/Event Tile:** If movement is locked, opening and closing the main menu ('Start' -> 'B') can resolve the issue.
- **World Knowledge Graph:** I must use `manage_world_knowledge` every time I transition between maps to keep my internal world map accurate.
- **Dynamic Map Tiles:** On Route 29, some tiles can dynamically change (e.g. WALL -> LEDGE) as I move nearby. I must mark these with ⚠️.

### Battle Mechanics
- **Held Items (Berries):** Pokémon can use held Berries to heal themselves in battle.
- **Catching:** Weakening a Pokémon makes it easier to catch.

### Tile & Environmental Mechanics (Re-evaluation in progress)
*The system notice on turn 2523 invalidates my previous understanding. All mechanics must be re-tested.*
- **WALL:** Impassable (verified multiple times).
- **FLOOR:** Traversable.
- **TALL_GRASS:** Traversable, wild encounters.
- **HEADBUTT_TREE:** Impassable.
- **CUT_TREE:** Impassable, requires HM 'Cut'.
- **DOOR:** Warp tile.
- **LEDGE:** Mechanics unconfirmed. System states it's not one-way, but my tests show otherwise. Must follow maze algorithm.
- **HOP_DOWN / HOP_LEFT / HOP_RIGHT / HOP_DOWN_LEFT / HOP_DOWN_RIGHT:** Mechanics unconfirmed. Must follow maze algorithm.
- **WATER:** Impassable, likely requires HM 'Surf'.
- **VOID:** Impassable boundary tile.
- **WARP_CARPET_DOWN:** Warp tile.