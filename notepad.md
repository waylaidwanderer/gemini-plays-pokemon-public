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

## Strategy: Shutter Sequence Testing
- Goal: Open path to the southeast (cols 14+). Requires (12,8) or (16,6) to be OPEN.
- Current Switch Positions: All ON (1, 1, 1).
- Observed Shutters: (2,6) OPEN, (6,8) OPEN, (10,6) CLOSED, (16,6) CLOSED, (12,8) CLOSED.
- Hypothesis: The grunt's hint (3-2-1) refers to a sequence that depends on the *starting state* or is a specific permutation.
- Plan: 
  1. Reset all switches to OFF (0, 0, 0).
  2. Test sequence 1-2-3 (Right, Middle, Left).
  3. Test sequence 3-2-1 (Left, Middle, Right) again from (0,0,0) if 1-2-3 fails.
- Current Step: Resetting Switch 2 (Middle) to OFF.
- Switch 3: OFF (0).
- Switch 2: ON (1).
- Switch 1: ON (1).

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).