# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: WALL when CLOSED, FLOOR when OPEN.
- SwitchScript (2,1), (10,1), (16,1): Toggles specific shutters.

# Puzzle: Goldenrod Underground Switch Room
- Goal: Reach the Underground Warehouse (Map 3_55).
- Mission: Identify shutter/switch mapping via isolation testing.
- Start Turn: 10079

## Shutter Verification Matrix
| State (S1,S2,S3) | (2,6) | (3,6) | (10,6) | (16,6) | (6,8) | (12,8) | Path Clear? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0, 0, 0) | ? | ? | ? | ? | ? | ? | ? |
| (1, 0, 0) | ? | ? | ? | ? | ? | ? | ? |
| (0, 1, 0) | ? | ? | ? | ? | ? | ? | ? |
| (0, 0, 1) | ? | ? | ? | ? | ? | ? | ? |
| (0, 1, 1) [T10087] | OPEN | OPEN | CLOSED | CLOSED | OPEN | OPEN | NO |
| (1, 1, 1) [T10081] | OPEN | OPEN | CLOSED | CLOSED | OPEN | CLOSED | NO |

## Shutter/Switch Mapping (Hypothesis)
- S1: Toggles (12,8). (Observed transition 1,1,1 -> 0,1,1).

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).