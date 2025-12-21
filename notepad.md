# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: WALL when CLOSED, FLOOR when OPEN. (Represented as WALL in XML when closed).
- SwitchScript (2,1), (10,1), (16,1): Interactable from row 2 (facing UP). Toggles specific shutters.

# Puzzle: Goldenrod Underground Switch Room
## Isolation Testing Matrix (0 = OFF, 1 = ON)
| State (S1,S2,S3) | (2,6) | (3,6) | (10,6) | (16,6) | (6,8) | (12,8) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0, 0, 0) | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED | CLOSED |
| (1, 0, 0) | CLOSED | CLOSED | CLOSED | OPEN | CLOSED | CLOSED |
| (0, 1, 0) | ? | ? | OPEN | CLOSED | ? | ? |
| (0, 0, 1) | OPEN | OPEN | CLOSED | CLOSED | CLOSED | OPEN |

## Verified Observations
- (0, 0, 0): All shutters CLOSED. (Turn 10102)
- (1, 0, 0): (16, 6) OPEN. (Turn 10106)
- (0, 0, 1): (2, 6), (3, 6), (12, 8) OPEN. (Turn 10094)
- (1, 1, 1): (2, 6), (3, 6) OPEN; (10, 6), (16, 6) CLOSED. (Turn 10081)

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).