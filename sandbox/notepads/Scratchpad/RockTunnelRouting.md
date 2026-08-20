# Rock Tunnel Master Traversal Plan

## Verified Directional Ladder Correspondence Matrix
| Ladder Name | Trigger Floor & Coord | Destination Floor & Coord | Direction / Sector | Verified Turns |
|---|---|---|---|---|
| Ladder 1 Ascent | B1F (33, 25) | 1F (37, 3) | B1F SE -> 1F Eastern Sector | Turns 4618, 5372, 5584, 6951, 7449 |
| Ladder 1 Descent | 1F (37, 3) | B1F (33, 25) | 1F Eastern Sector -> B1F SE | Turns 6954, 6978 |
| Ladder 3 Ascent | B1F (37, 17) | 1F (3, 3) | B1F East-Central -> 1F NW | Turns 4921, 5082, 5580 |
| Ladder 3 Descent | 1F (3, 3) | B1F (37, 17) | 1F NW -> B1F East-Central | Turns 6190 |
| Ladder 4 Ascent | B1F (5, 3) | 1F (27, 3) | B1F NW -> 1F Eastern Sector | Turn 6907 |
| Ladder 4 Descent | 1F (27, 3) | B1F (5, 3) | 1F Eastern Sector -> B1F NW | Turns 4364, 6104, 6401, 6907 |
| Ladder 5 Ascent | B1F (23, 11) | 1F (17, 11) | B1F Central -> 1F Central | Turn 6837 |
| Ladder 5 Descent | 1F (17, 11) | B1F (23, 11) | 1F Central -> B1F Central | Turns 6131, 7054 |

## Verified Topology & 1F Passage Routes (Turns 7450-7528)
- Rows 14-15 Rock Wall: Spans continuously across cols 18 to 37. Stepping Down from row 13 into row 14 is blocked at all cols 18-37.
- Open Vertical Corridors through Rows 14-15 on 1F:
  1. Column 17: (17, 14..15) is completely open floor connecting (17, 10..13) directly down into (17, 16..17).
  2. Middle Thoroughfare (rows 14-16, cols 8-16): Connects the Central Vertical Thoroughfare (cols 8-11) directly to (17, 16).
- South Sector Routing from (17, 16):
  - Descend south down cols 14-17 (rows 16-27).
  - Move west along row 25-27 to (14, 26).
  - Descend south down cols 14-17 to row 30-33 (the 1F Southern Highway).
  - Step Down into the exit doorway to trigger transition to Route 10 South!

## Verified 1-Turn Flee Protocol
- Sequence: `["B", "B", "B", "Down", "Right", "A", "B"]` (100% 1-turn success rate).

## Current Navigation Step
- Current Position: 1F (27, 13)
- Target: Reach Column 17 corridor / Middle Thoroughfare to descend to row 16-19 and the 1F southern sector.
- Immediate Step: Move Left 6 to (21, 13), Up 6 to (21, 7), Left 7 to (14, 7), and navigate through confirmed open floor to row 16.
