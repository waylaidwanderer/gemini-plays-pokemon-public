# Goldenrod Radio Tower Takeover
## Strategy (HOW)
- Map 3_54 Switch Puzzle: Switches 1, 2, and 3 control shutters.
- Solution Goal: Reach the warehouse entrance (likely far south/west).
- Resource Management: Visit Goldenrod Dept. Store 4F (Medicine Box) to buy Hyper Potions and Revives.

# Global Knowledge
## Tile Mechanics
- FLOOR:
  - Individual Behavior: Standard walkable surface.
  - Relational Behavior: Can be entered from any adjacent traversable tile.
  - Mechanics: Allows normal player movement.
- WALL / MART_SHELF:
  - Individual Behavior: Impassable barrier.
  - Relational Behavior: Cannot be entered from any direction.
  - Mechanics: Blocks movement. In Map 3_54, specific WALL tiles are dynamic shutters.
- COUNTER:
  - Individual Behavior: Impassable barrier.
  - Relational Behavior: Interactable from the front tile (usually a FLOOR tile).
  - Mechanics: Prevents walking but allows talking to NPCs behind them.
- WARP_CARPET / LADDER / STAIRCASE:
  - Individual Behavior: Triggers a map transition (warp).
  - Mechanics: Connects different floors or maps.

## Pokemon Type Effectiveness
- Rock/Ground -> Poison: Super Effective (GNEISS vs Koffing)
- Fire -> Grass: Super Effective (Calcifer vs Gloom)
- Water -> Fire: Super Effective (vs Growlithe)
- Flying -> Bug: Super Effective (Icarus vs Spinarak)

# Resource Management Strategy
- Goal: Purchase 10 Hyper Potions and 5 Revives at the 4F Medicine Box.
- Return Path: Elevator/Stairs -> 1F -> Exit -> Goldenrod City (9, 5) -> Underground North Entrance -> Warp at (21, 25) -> Map 3_54.

# Switch Room Puzzle (Map 3_54)
- Task started: Turn 9122.
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Grunt Hint: "Change the order of switching. That'll change the ways the shutters open and close."

## Verified Shutter Logic
- Switch 1: Toggles (16, 6) and (17, 6).
- Switch 3 ON: Opens (12, 8), (12, 9). Closes (6, 9).
- Switch 3 OFF: Opens (10, 6), (10, 7).
- Switch 2 ON -> OFF: Closes (10, 6), (10, 7).

# Active Task Tracking
- Shopping Trip (Restock): Started Turn 9181.
- Current Location: Goldenrod Dept. Store 4F.
- Goal: Find clerk selling Hyper Potions/Revives.

# Area Notes: Goldenrod Dept. Store 4F
- NPCs: Bug Catcher (ID 3), Gameboy Kid (ID 4).
- Shop: Clerk at (13, 5) sells Vitamins (Protein, Iron, etc.).
- Elevator Button: (3, 0).
- Staircase: (2, 0), (12, 0), (15, 0).