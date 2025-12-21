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
| (0, 0, 1) | CLOSED | CLOSED | CLOSED | OPEN | CLOSED | CLOSED |
| (0, 1, 0) | CLOSED | CLOSED | OPEN | CLOSED | OPEN | CLOSED |
| (1, 0, 0) | OPEN | OPEN | CLOSED | CLOSED | CLOSED | OPEN |
(Note: S3=Left, S2=Middle, S1=Right)

## Strategy: Shutter Sequence Testing
- Goal: Open path to the southeast (cols 14+). Requires (12,8) or (16,6) to be OPEN.
- Current Switch States:
  - Switch 3 (2,1): ON (1)
  - Switch 2 (10,1): ON (1)
  - Switch 1 (16,1): ON (1)
- Shutter State (1,1,1) Verification:
  - (2,6): OPEN
  - (10,6): CLOSED
  - (16,6): CLOSED
  - (6,8): OPEN
  - (12,8): CLOSED
- Result: State (1,1,1) blocks the southeast path.
- Hypothesis: Combination (0,1,1) [S2, S1 ON] will have (10,6) and (16,6) OPEN.
- Plan:
  1. Toggle Switch 3 (2,1) to OFF. (Current state will become 0,1,1)
  2. Verify shutters at (10,6) and (16,6).
  3. If open, proceed to Warehouse Entrance.
- Current Step: Moving to Switch 3 to toggle to OFF.

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).