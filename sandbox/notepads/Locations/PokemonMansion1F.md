# Pokémon Mansion 1F - Layout & Exploration

## Overview
- First floor of the ruined Pokémon Mansion in northwest Cinnabar Island.
- Features red carpet grand entrance, marble floors, Mewtwo statue switches, ruined walls, and an enclosed eastern wing accessible only by dropping from 3F.

## Layout & Landmarks

### Main Sector (West & Central)
- Central Grand Hallway: Columns 4-7, rows 14-27 (separated from northern central area by row 17 table barrier)
- Entrance Area: Row 26-27 (cols 1-7)
- Decorative Displays / Pillars: (3, 24) and (8, 24)
- Stairs up to 2F: Located at (5, 10) in the central sector. Accessible from northern wing corridors (rows 1-7). Ground-level passage from entrance is blocked by row 17 table barrier.

### Northwest Sector (Fully Mapped Turn 19090)
- Boundaries: cols 0-8, rows 0-9.
- Rubble / Rocks: (1..3, 2..3) and (1, 4..5).
- Mewtwo Statue Switch: (2, 4..5) facing south.
- Large Wooden Table: (6..7, 4..5).
- Green Display Table: (4, 6..7).
- Top Hallway (Row 1-2): cols 1-12 open corridor connecting to column 12 thoroughfare.
- South Divider (Row 9): Solid wall across cols 1-7.
- Shutter Divider (Column 9): Closed metal shutter at (9, 4..7).

### Northern Landing Sector (Accessible via 3F Right Balcony Drop at (19, 14))
- Balcony Landing Tile (Arrival): 1F (18, 14) [Departed 3F at (19, 14), Verified Turn 19000]
- Pillar / Pedestal: (15, 8..11) [Decorative structure; no switch dialogue, verified Turns 19669-19672]
- Research Journal: (18, 2) on table in northeast office
- Corridor Passage to West/Central: Column 9 is a continuous solid wall from row 8 to row 16. West-east bypass is only at row 22.
- Corridors: Row 2-7 (cols 10-27 north of row 8 wall), Row 10 (cols 10-24), Col 12 (rows 9-16, blocked at row 8), Col 18-24 (rows 9-16)

### Northeast Wing Chamber
- Large Table/Desk Structure: (24..25, 8..9) [Solid 2x2 display, verified Turn 19076]
- Traversal Corridor: Column 26 (rows 4-10) and Column 23 (rows 7-10).
- Southern Boundary: Solid horizontal wall across row 8 (cols 24-28). (Empirically verified Turns 19675-19678).

### Enclosed Eastern Sector (Accessible via 3F Balcony Drop)
- Balcony Landing Tile (Arrival): 1F (16, 14) [Departed 3F at (16, 14)]
- Scientist NPC: (17, 17) [Scientist Ted: Electrode Lv 29, Weezing Lv 29; Defeated Turn 18533]
- Item Ball: (18, 21) [TM03 Swords Dance - Collected Turn 18509]
- Corridors: Row 14 (cols 12-17), Row 16 (cols 18-25 solid wall divider), Row 20-21 (cols 12-23), Row 22 (cols 6-13 passage west of col 14 wall), Row 24-26 (cols 12-23), Column 20 (rows 10-15), Column 25 (rows 14-23)
### B1F Staircase & Shutter Gate Connections
- Access to Northern Landing Sector: Dropping from 3F Right Balcony Pit at (19, 14) lands on 1F Northern Landing Sector at (18, 14).
- Shutter Gate (North Row 13): (12..17, 13) [OPEN in State A, CLOSED in State B] (Empirically verified Turn 19705). Connects column 12 corridor directly south into Enclosed East Wing.
- Column 9 Barrier: Continuous solid vertical wall from row 8 to row 16 blocking westward passage. West-East wing bypass on 1F is located at Row 22 (cols 6-13).
- Interior Displays: Hedges at rows 18 & 22 (cols 14-19); Statues at rows 19 & 23 (cols 14-19); Tables/Bookshelves at row 17 (cols 18-19, 22-23)
### Negative Collision Constraints & Blocked Paths (Verified Turns 19921-20403)
- Row 8 Horizontal Wall & Gate: Wall across (8..25, 8) with shutter gate at (18..19, 8) [OPEN in State B, CLOSED in State A]. In State B, provides open north-south passage between Landing Sector (row 10) and Northern Hallway (rows 1-7). Column 12 is blocked at (12, 8).
- Northeast Chamber Obstacles: Rubble at (23..26, 6..7), (22..24, 4..5), (22..23, 8..10), (26, 9); wall barriers at (20..21, 5) and (22, 2). Row 3 (cols 20-26) is a clear east-west corridor.
- Row 17 Horizontal Table Barrier: Solid barrier across (1..9, 17). The ONLY north-south opening through row 17 is at (10..12, 17).
- Column 25 Vertical Wall: Solid divider across (25, 9..16) separating East Wing landing (cols 18-24) from B1F Staircase corridor (cols 26-28).
- Column 9 Vertical Wall: Solid divider across (9, 9..16) separating Central Hallway (cols 1-8) from East corridor (cols 10-12).
- Table/Railing Barrier at (26..27, 17): Table barrier dividing east corridor.
- Southeast Corner at (26..27, 27): Dead-end alcove; no doorway or external transition.
### Southeast Enclosed Room & Switch (Verified Turns 19959-19969)
- Mewtwo Statue Switch: Located at (18, 25). Interactable from (18, 26) facing Up or (17, 25) facing Right. Toggles global mansion shutters between State A and State B.
- Item Ball: Located at (19, 25) (immediately east of statue switch).
- Southeast Room Entrance: Open doorway at (13, 22..23) connecting column 12 to (14, 22..23). Column 13 is a solid wall at rows 24-27 (row 26 cannot be entered directly from column 12).
- Route to Switch/Item: From column 12 -> (13, 22..23) doorway -> (14, 23) -> South to row 26 (14, 26) -> East along row 26 to (18..19, 26) -> (18, 25) switch / (19, 25) item ball.
### B1F Staircase Location (Observed Turn 19991)
- Descending Staircase to B1F: Located at (26..27, 27).
- North Landing: Located at row 26 (26..27, 26). Stairs must be entered from the NORTH at row 26 stepping DOWN into (26..27, 27).
- Item Ball at (1, 22): Full Restore [Collected Turn 20065]
### Isolated B1F Staircase Enclosure & Access Rule (Verified Turns 20090-20104)
- **Isolated Enclosure**: The chamber at (26..28, rows 8..16) containing the Scientist at (27, 11) and the B1F Staircase North Landing at (26, 16) is COMPLETELY ENCLOSED by walls on 1F:
  - North: Wall at row 8 (cols 8-25).
  - South: Staircase and table barriers at row 17 (25..28, 17). Stepping Up from row 18 (26..27, 18) collides with the solid south railing.
  - West: Solid vertical wall at column 25 (25, 9..16).
  - East: Solid exterior wall at column 29.
- **Entry Method**: This enclosure CANNOT be entered from 1F ground level. It must be entered by dropping from the far-right section of the 3F balcony pits!
- **Decorative Object at (23, 22)**: (23, 22) is a decorative pedestal/display, NOT a floor warp or staircase.
### Verified Multi-Floor Switch State Table
| Gate / Shutter Location | Floor | State A (Default) | State B (Toggled) |
|---|---|---|---|
| (18..19, 8) Shutter Gate | 1F | CLOSED | OPEN |
| (12..17, 13) Shutter Gate | 1F | OPEN | CLOSED |
| (9, 4..5) Shutter Gate | 2F | OPEN | CLOSED |
| (21, 17) Shutter Gate | 2F | CLOSED | OPEN |
| (15, 10..11) Shutter Gate | 3F | CLOSED | OPEN |

## Verified B1F Access Solution (Turn 20508)
- 1F NW Mewtwo statue switch at (2, 5) MUST be interacted with from (2, 6) facing UP (interacting from (3, 5) does not work).
- Toggling switch to State A opens the shutter gate at (24..25, 13).
- Direct path to B1F stairs: From NW room / (5, 1) -> East along row 1 to (26, 1) -> South down col 26 to (26, 12) -> West 2 steps to (24, 12) -> South 4 steps through open gate at (24, 13) to (24, 16) -> East 2 steps to (26, 16) -> South 1 step into (26, 17) descending stairs to B1F.