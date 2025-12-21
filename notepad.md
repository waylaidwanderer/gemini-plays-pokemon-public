# Goldenrod Radio Tower Takeover
## Strategy (HOW)
- Map 3_54 Switch Puzzle: Switches 1, 2, and 3 control shutters.
- Solution Goal: Reach the warehouse entrance (likely far south/west).
- Resource Management: Visit Goldenrod Dept. Store to buy Hyper Potions and Revives.

# Global Knowledge
## Tile Mechanics
- FLOOR:
  - Individual Behavior: Standard walkable surface. No special effects.
  - Relational Behavior: Can be entered from any adjacent traversable tile.
  - Mechanics: Allows normal player movement and wild encounters (in specific maps).
- WALL:
  - Individual Behavior: Impassable barrier. Blocks player movement.
  - Relational Behavior: Cannot be entered from any direction.
  - Mechanics: In Map 3_54, specific WALL tiles function as dynamic shutters toggled by switches.
- COUNTER:
  - Individual Behavior: Impassable barrier. Blocks player movement.
  - Relational Behavior: Interactable from the front tile (usually a FLOOR tile).
  - Mechanics: Prevents walking but allows talking to NPCs behind them.
- WARP_CARPET_DOWN / WARP_CARPET_UP:
  - Individual Behavior: Triggers a map transition (warp) when entered.
  - Relational Behavior: Entered by walking onto the tile.
  - Mechanics: Automatically moves the player to a different map or coordinate.
- LADDER / STAIRCASE:
  - Individual Behavior: Interactive warp point.
  - Relational Behavior: Triggers warp when the player steps onto it.
  - Mechanics: Connects different floors or maps.

## Pokemon Type Effectiveness
- Rock/Ground -> Poison: Super Effective (GNEISS vs Koffing)
- Fire -> Grass: Super Effective (Calcifer vs Gloom)
- Water -> Fire: Super Effective (vs Growlithe)
- Flying -> Bug: Super Effective (Icarus vs Spinarak)

# Resource Management Strategy
- Exit via warp carpet at (21, 29) on Map 3_54 -> Goldenrod City (9, 5).
- Navigate to the Goldenrod Dept. Store (Map 3_6).
- Take the elevator to 5F (Pharmacy).
  1. Navigate to (3, 1) on 1F.
  2. Call elevator at (3, 0).
  3. Enter and select 5F.
  4. Walk out of elevator.
- Purchase 10 Hyper Potions and 5 Revives.
- Return to the Underground via the same path to resume the puzzle.

# Switch Room Puzzle (Map 3_54)
- Task started: Turn 9122.
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Grunt Hint: "Change the order of switching. That'll change the ways the shutters open and close."

## Verified Shutter Logic
- Switch 1: Toggles (16, 6) and (17, 6).
- Switch 3 ON: Opens (12, 8), (12, 9). Closes (6, 9).
- Switch 3 OFF: Opens (10, 6), (10, 7).
- Switch 2 ON -> OFF: Closes (10, 6), (10, 7).