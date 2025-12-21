# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: WALL when CLOSED, FLOOR when OPEN.
- SwitchScript (2,1), (10,1), (16,1): Toggles specific shutters.

# Puzzle: Goldenrod Underground Switch Room
- Goal: Reach the Underground Warehouse (Map 3_55).
- Mission: Identify shutter/switch mapping via isolation testing.
- Start Turn: 10079

## Isolation Testing Matrix (0 = OFF, 1 = ON)
| State (S1,S2,S3) | (2,6) | (3,6) | (10,6) | (16,6) | (6,8) | (12,8) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| (0, 0, 0) [T10099] | CLOSED | CLOSED | ? | ? | ? | ? |
| (1, 0, 0) | ? | ? | ? | ? | ? | ? |
| (0, 1, 0) | ? | ? | ? | ? | ? | ? |
| (0, 0, 1) | OPEN | OPEN | CLOSED | CLOSED | CLOSED | OPEN |

## Observations
- (0, 0, 0): (2,6)=CLOSED, (3,6)=CLOSED. (Observed Turn 10099).
- (1, 1, 1): (2,6)=OPEN, (3,6)=OPEN, (6,8)=OPEN, (10,6)=CLOSED, (16,6)=CLOSED, (12,8)=CLOSED. (Observed Turn 10081)
- (0, 1, 1): (12,8) shifted from CLOSED to OPEN (Observed Turn 10087).
- (0, 0, 1): (2,6)=OPEN, (3,6)=OPEN, (10,6)=CLOSED, (16,6)=CLOSED, (6,8)=CLOSED, (12,8)=OPEN. (Observed Turn 10094)

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11).
- Return Ladders: (23,3), (21,25), (5,25).