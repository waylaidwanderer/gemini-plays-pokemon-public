# Tile Mechanics
- FLOOR: Walkable surface. Verified.
- WALL: Impassable barrier. Verified.
- MART_SHELF: Impassable barrier. Verified.
- COUNTER: Impassable barrier. Interactable from the front tile. Verified.
- STAIRCASE: Triggers map transition. Verified.
- WARP_CARPET: Triggers map transition. Verified.
- ELEVATOR_DOOR: Warp to Elevator Interior (11_17). Verified.

# Global Knowledge
## Lessons Learned
- **Elevators:** Elevator doors are warps. If a button doesn't work, try walking into the door.
- **Counters:** To talk to someone behind a counter, stand in front of the counter tile and face it.
- **Shopping:** Check all clerks at a counter; they often have different inventories.
- **Input Hygiene:** NEVER mix directional buttons with A/B/Start/Select in a single turn when precision is required (e.g., interacting with objects).
- **Vending Machines:** Lemonade (350) is the best value for HP restoration (80 HP).

## Pokemon Type Effectiveness
- Rock/Ground -> Poison: Super Effective (GNEISS vs Koffing)
- Fire -> Grass: Super Effective (Calcifer vs Gloom)
- Water -> Fire: Super Effective (vs Growlithe)
- Flying -> Bug: Super Effective (Icarus vs Spinarak)

# Resource Management Strategy (COMPLETED)
- Task: Restock healing items (Lemonades, Super Potions).
- Status: 10 Lemonades and 10 Super Potions purchased.
- Note: Revives are still needed (source unknown).
- Return Path: Elevator -> 1F -> Exit -> Goldenrod City (9, 5) -> Underground North Entrance -> Warp at (21, 25) -> Map 3_54.

# Shop Inventories
## Goldenrod Dept. Store 2F
- Clerk 1 (13, 5): Potion, Super Potion, Antidote, Parlyz Heal, Awakening, Burn Heal, Ice Heal.
- Clerk 2 (13, 6): Poke Ball, Great Ball, Escape Rope, Repel.
## Goldenrod Dept. Store 3F
- Clerk (6, 1): X Speed, X Special, X Defend, X Attack.
## Goldenrod Dept. Store 4F
- Clerk (13, 5): Protein, Iron, Carbos, Calcium.
## Goldenrod Dept. Store 5F
- Clerk (8, 5): TMs.
## Goldenrod Dept. Store 6F
- Vending Machines (8, 1 to 11, 1): Fresh Water (200), Soda Pop (300), Lemonade (350).

# Switch Room Puzzle (Map 3_54)
- Task started: Turn 9122.
- Switches: 1 (16, 1), 2 (10, 1), 3 (2, 1).
- Logic:
  - Switch 1: Toggles (16, 6) and (17, 6).
  - Switch 3 ON: Opens (12, 8), (12, 9). Closes (6, 9).
  - Switch 3 OFF: Opens (10, 6), (10, 7).
  - Switch 2 ON -> OFF: Closes (10, 6), (10, 7).

# Area Notes
## Goldenrod Dept. Store 4F
- NPCs: Bug Catcher (ID 3), Gameboy Kid (ID 4).
- Elevator Entrance: (2, 0) - Leads to 11_17.
- Staircase: (13, 0).
## Goldenrod Dept. Store 2F
- NPCs: Cooltrainer F (ID 4), Gentleman (ID 5), Youngster (ID 3) at (9, 7).
- Elevator Entrance: (2, 0) - Leads to 11_17.
- Staircase: (12, 0).
- Directory: (14, 0).
## Goldenrod Dept. Store 3F
- NPCs: Super Nerd (ID 2), Rocker (ID 3).
- Shop: Battle Collection (X Items).
- Staircase: (13, 0).
- Directory: (14, 0) - "3F BATTLE COLLECTION".
## Goldenrod Dept. Store 6F
- NPCs: Super Nerd (ID 2) at (8, 2), Lass (ID 1) at (9, 2).
- Elevator Entrance: (2, 0) - Leads to 11_17.
- Elevator Button: (3, 0).
- Vending Machines: (8, 1), (9, 1), (10, 1), (11, 1).
- Staircase: (13, 0).

# Switch Room Strategy (Verified by Agent)
- Standard Solution: 3-2-1 sequence.
- Current Progress: Switch 3 ON, Switch 2 ON.
- Next Step: Activate Switch 1 (16, 1) to clear the path to the stairs.