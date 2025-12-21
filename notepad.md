# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: WALL type in XML when CLOSED, FLOOR type in XML when OPEN.
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP). Toggles specific shutters.
- LADDER: Warp point to another map.
- WARP_CARPET_DOWN: Warp point to another map.

# Puzzle: Goldenrod Underground Switch Room
- Puzzle Start Turn: ~10125
## Isolation Testing Matrix (0 = OFF, 1 = ON)
| State (S3,S2,S1) | (2,6) | (3,6) | (10,6) | (16,6) | (6,8) | (12,8) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0, 0, 0) | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED |
| (0, 0, 1) | OPEN | OPEN | CLOSED | CLOSED | CLOSED | OPEN |
| (0, 1, 0) | CLOSED | CLOSED | OPEN | CLOSED | OPEN | CLOSED |
| (1, 0, 0) | CLOSED | CLOSED | CLOSED | OPEN | CLOSED | CLOSED |
(Note: Switch 3 at 2,1; Switch 2 at 10,1; Switch 1 at 16,1)

## Strategy: Shutter Sequence Testing
- Goal: Open path to the southeast (cols 14+). Requires (12,8) or (16,6) to be OPEN.
- Current Switch States:
  - Switch 3 (2,1): OFF (0)
  - Switch 2 (10,1): OFF (0)
  - Switch 1 (16,1): ON (1)
- Observed Shutters (Current): (2,6) OPEN, (3,6) OPEN, (12,8) OPEN. Others CLOSED.
- Plan:
  1. Reset all switches to OFF (0, 0, 0).
  2. Test sequence 3-2-1 (Left, Middle, Right) from (0,0,0).
- Current Step: Moving to Switch 1 to reset to OFF.

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).