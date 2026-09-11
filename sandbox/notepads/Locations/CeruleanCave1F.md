# Cerulean Cave (Unknown Dungeon) 1F - Layout & Notes

## Connected Component Graph (1F)
- **Entrance / Exit**: (24..25, 17) connects to Route 24 northern waterway.
  - **CRITICAL WARP TRIGGER ZONE**: Stepping onto (24..25, 17) immediately triggers a map transition and ejects the player outside to Route 4 / Cerulean City. DO NOT walk South onto (24..25, 17) while traversing Row 17 on foot. Keep east of (23, 17) or west of (20, 17) when navigating ground.
  - **Optimal Transit from Entrance**: When entering 1F via water, remain Surfing and travel straight North along the East Water Channel (cols 24..27, rows 5..17) directly into the Northern Waterway (rows 3..5), then land at (18..19, 6) to access Ladder C at (18, 9).
- **Ladder B (East Landing)**: (22, 6) <-> 2F (22, 6).
- **Ladder C (Central Sector)**: (19, 7) <-> 2F (19, 7). Accessed from north via Row 5/6.
- **Ladder D (NE High Plateau)**: (27, 1) <-> 2F (29, 1).
- **Ladder E (NW Upper Shelf)**: (7, 1) <-> 2F (9, 1).
- **Ladder A (NW Lower Basin)**: Ladder graphic observed at (0, 6) in the NW lower basin; connectivity to B1F pending empirical traversal.

## Verified Topography & Transit (1F)
- **Central Platform**: Spans cols 11-18, rows 8-15.
  - Column 12 corridor (12, 9..15) is open continuous floor connecting Central Platform south to north.
  - Row 16 is solid rock across (14..20, 16).
  - Tile (13, 16) is the single verified open ground corridor/gap connecting Row 17 (13, 17) directly to the Central Platform at (13, 15).
  - Central-East transit corridor: (21, 6..9) is open continuous purple floor connecting Row 9 directly north to (21, 6) and the Northern Waterway at (21, 5).
  - Central-East transit corridor: (21, 6..9) is open continuous purple floor connecting Row 9 directly north to (21, 6) and Ladder B landing at (23, 7).
  - Collision Constraint: (20, 9)/(19, 9) is solid rock collision blocking horizontal passage along Row 9 between Ladder B landing (23, 7) and Ladder C (18, 9).
- **South Ground Highway (Row 17)**: Walkable ground spanning (10..19, 17).
  - West end of central pocket terminates at (10, 17); (9, 17) is blue rock.
  - Connects to Central Platform via (13, 17) <-> (13, 16) <-> (13, 15).
  - Row 11 Highway: (14..24, 11) is continuous open floor connecting east to Column 24 (24, 11..17) and the entrance water canal at (24..25, 17).
- **Western Ridge (South Sector)**: Cols 0-8, rows 8-13. Elevated plateau accessed via South Ramp at (1, 13).
  - Tile (3, 11) features a decorative ladder graphic; confirmed normal floor (no warp).
  - Northern boundary at (1, 8) -> (1, 7) is a solid cliff wall (no north passage).
- **Waterways & Northern Highway**:
  - East Water Channel: Cols 24..27, rows 10..17 from entrance mat (24..25, 17).
  - Northern Water Highway: Rows 3..5 across northern sector. Potential westward water transit to NW Lower Basin pending empirical testing.
## Verified 1F Ledge Traversal & Water Transit Breakthrough (Turn 44152)
- **1F Entrance Ledge Bypass**: When entering 1F on foot at (24..25, 17), walk to (21, 12) or (22, 12) facing North towards ledge (21, 11). Activating SURF from the menu traverses the south-facing ledge barrier and places the player on Row 9 at (21, 9)!
- **Transit from (21, 9)**:
  - Walk Up to (21, 6), face North at (21, 5) and use SURF to board Northern Waterway (rows 3..5).
  - Surf West to (18, 5), land South at (18, 6), and walk South to Ladder C at (18, 9).
  - Ascend Ladder C (18, 9) to reach 2F Central Hub at (19, 7) with direct access to S-Bypass and Ladder A (1, 3) -> B1F!