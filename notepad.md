# Tile Mechanics
- FLOOR: Traversable.
- SHUTTER: WALL when CLOSED, FLOOR when OPEN.

# Puzzle: Goldenrod Underground Switch Room
- Goal: Reach the Underground Warehouse (Map 3_55).
- Strategy: Use isolation data to identify the sequence that clears row 6 and row 8.

## Shutter Toggle Data (Isolation)
| Switch | State | (2,6) | (10,6) | (16,6) | (6,8) | (12,8) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| S1 (16,1) | (1,0,0) | CLOSED | CLOSED | OPEN | CLOSED | OPEN |
| S2 (10,1) | (0,1,0) | CLOSED | OPEN | CLOSED | OPEN | CLOSED |
| S3 (2,1) | (0,0,1) | OPEN | CLOSED | CLOSED | CLOSED | CLOSED |

## Sequence Results
- (0,1,1) [3->2]: (2,6) OPEN, (10,6) CLOSED, (12,8) OPEN.
- (1,1,1) [3->2->1]: (2,6) OPEN, (10,6) CLOSED, (16,6) CLOSED. BLOCKED.

## Plan
1. Reset all switches to OFF (0,0,0).
2. Execute sequence 3-2-1 and re-verify EVERY shutter collision.
3. If 3-2-1 fails, explore southeast quadrant using state (1,0,0) since isolation shows (16,6) and (12,8) are both OPEN.

# Area Notes
- Warehouse Entrance: Unseen warp in southeast quadrant.
- Key NPCs: Rocket Girl (19,12), Emergency Switch (20,11), Burglar Eddie (9,12).
- Return Ladders: (23,3), (21,25), (5,25).