# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP). Toggles specific shutters.

# Puzzle: Goldenrod Underground Switch Room
## Isolation Testing Matrix (0 = OFF, 1 = ON)
| State (S1,S2,S3) | (2,6) | (3,6) | (10,6) | (16,6) | (6,8) | (12,8) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0, 0, 0) | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED |
| (1, 0, 0) | CLOSED | CLOSED | CLOSED | OPEN | CLOSED | CLOSED |
| (0, 1, 0) | CLOSED | CLOSED | OPEN | CLOSED | OPEN | CLOSED |
| (0, 0, 1) | OPEN | OPEN | CLOSED | CLOSED | CLOSED | OPEN |

## Strategy: 3-2-1 Sequence
- Goal: Open path to the southeast warp (Underground Warehouse).
- Sequence: 
  1. Switch 3 (2, 1) -> ON (Current: ON)
  2. Switch 2 (10, 1) -> ON (Next Step)
  3. Switch 1 (16, 1) -> ON
- Expected Path: (10,2) -> (10,7) -> (12,8) -> Southeast Warp.

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).