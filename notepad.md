# Goldenrod Radio Tower Takeover
## Strategy (HOW)
- Map 3_54 Switch Puzzle: Use Switch 1, 2, and 3 to manipulate shutters.
- Radio Tower: Defeat Fake Director on 5F, get Basement Key, rescue real Director in Underground Warehouse.
- Resource Management: Restock healing items at Goldenrod Dept. Store 2F.

# Global Knowledge
## Tile Mechanics
- FLOOR:
  - Individual Behavior: Standard walkable surface.
  - Relational Behavior: Can be entered from any adjacent traversable tile.
  - Mechanics: Allows normal player movement.
- WALL / MART_SHELF:
  - Individual Behavior: Impassable barrier.
  - Relational Behavior: Cannot be entered from any direction.
  - Mechanics: Blocks movement.
- COUNTER:
  - Individual Behavior: Impassable barrier.
  - Relational Behavior: Interactable from the front tile (usually a FLOOR tile).
  - Mechanics: Prevents walking but allows talking to NPCs behind them.
- WARP_CARPET / LADDER / STAIRCASE:
  - Individual Behavior: Triggers a map transition (warp).
  - Mechanics: Connects different floors or maps.
- ELEVATOR_DOOR:
  - Individual Behavior: Warp tile leading to elevator interior (Map 11_17).
  - Mechanics: Appears like a wall or staircase but functions as a warp.

## Pokemon Type Effectiveness
- Rock/Ground -> Poison: Super Effective (GNEISS vs Koffing)
- Fire -> Grass: Super Effective (Calcifer vs Gloom)
- Water -> Fire: Super Effective (vs Growlithe)
- Flying -> Bug: Super Effective (Icarus vs Spinarak)

# Resource Management Strategy
- Goal: Purchase 10 Hyper Potions and 5 Revives.
- Current Status: Checking Goldenrod Dept. Store floors. 4F sells Vitamins.
- Return Path: Elevator -> 1F -> Exit -> Goldenrod City (9, 5) -> Underground North Entrance -> Warp at (21, 25) -> Map 3_54.

# Switch Room Puzzle (Map 3_54)
- Task started: Turn 9122.
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Logic:
  - Switch 1: Toggles (16, 6) and (17, 6).
  - Switch 3 ON: Opens (12, 8), (12, 9). Closes (6, 9).
  - Switch 3 OFF: Opens (10, 6), (10, 7).
  - Switch 2 ON -> OFF: Closes (10, 6), (10, 7).

# Area Notes: Goldenrod Dept. Store 4F
- NPCs: Bug Catcher (ID 3), Gameboy Kid (ID 4).
- Shop: Clerk at (13, 5) sells Vitamins (Protein, Iron, etc.).
- Elevator Button: (3, 0) - Non-functional.
- Elevator Entrance: (2, 0) - Leads to 11_17.
- Staircases: (12, 0), (15, 0).

# Area Notes: Goldenrod Dept. Store 2F
- NPCs: Cooltrainer F (ID 4), Gentleman (ID 5).
- Elevator Entrance: (2, 0) - Leads to 11_17.
- Directory: (3, 0).