# Pok�mon Mansion 1F - Layout & Exploration

## Overview
- First floor of the ruined Pok�mon Mansion in northwest Cinnabar Island.
- Features red carpet grand entrance, marble floors, Mewtwo statue switches, ruined walls, and an enclosed eastern wing accessible only by dropping from 3F.

## Layout & Landmarks

### Main Sector (West & Central)
- Central Grand Hallway: Columns 4-7, rows 14-27 (separated from northern central area by row 17 table barrier)
- Entrance Area: Row 26-27 (cols 1-7)
- Decorative Displays / Pillars: (3, 24) and (8, 24)
- Stairs up to 2F: Located at (5, 10) in the central sector. Accessible from northern wing corridors (rows 1-7). Ground-level passage from entrance is blocked by row 17 table barrier.

- Decorative Garden Statues: Statues at (13, 9) and (13, 11) are decorative scenery (Negative Test Turn 20908: Pressing A facing Right at (12, 9) yielded no dialogue or switch trigger).

### Northwest Sector (Fully Mapped)
- Boundaries: cols 0-8, rows 0-9.
- Rubble / Rocks: (1..3, 2..3) and (1, 4..5).
- Mewtwo Statue Switch: (2, 4..5) (base/switch at (2, 5)).
- Large Wooden Table: (6..7, 4..5).
- Green Display Table: (4, 6..7).
- Column 9 Divider: Solid vertical wall from Row 0 to Row 8 with shutter gate at (9, 4..5) (OPEN in State A, CLOSED in State B).
- South Divider (Row 9): Solid wall across cols 1-7.

### Northern Landing Sector (Accessible via 3F Right Balcony Drop at (19, 14))
- Balcony Landing Tile (Arrival): 1F (18, 14) [Departed 3F at (19, 14), Verified Turn 19000 & 20893]
- Shutter Gate at (18..19, 8): OPEN in State B, CLOSED in State A. Connects Landing Sector (row 10) north into Northern Wing (rows 1-7).
- Corridors: Row 2-7 (cols 10-24 north of row 8 wall), Row 6 is open from col 11 to col 21.

### Enclosed Southern & Eastern Sector (Accessible via 3F Left Balcony Drop at (16, 14))
- Balcony Landing Tile (Arrival): 1F (16, 14)
- Scientist NPC: (17, 17) [Scientist Ted: Electrode Lv 29, Weezing Lv 29; Defeated Turn 18533]
- Item Ball: (18, 21) [TM03 Swords Dance - Collected Turn 18509]
- Garden Area (cols 12-23, rows 14-27): Hedges at rows 18 & 22; Statues at rows 19 & 23; clear paths along cols 12-13, col 20, row 16, row 20, row 21, row 24-26.
- Eastern Chamber (cols 25-28, rows 16-27): Open corridor connected via row 16 hallway at (24..25, 16).
- Shutter Gate (Row 13): (24..25, 13) [OPEN in State A, CLOSED in State B]. Connects the northern corridor directly to the eastern corridor leading to B1F staircase.

## Verified Multi-Floor Switch State Table
| Gate / Shutter Location | Floor | State A (Default) | State B (Toggled) |
|---|---|---|---|
| (18..19, 8) Shutter Gate | 1F | CLOSED | OPEN |
| (9, 4..5) Shutter Gate | 1F | OPEN | CLOSED |
| (24..25, 13) Shutter Gate | 1F | OPEN | CLOSED |
| (9, 4..5) Shutter Gate | 2F | OPEN | CLOSED |
| (21, 17) Shutter Gate | 2F | CLOSED | OPEN |
| (15, 10..11) Shutter Gate | 3F | CLOSED | OPEN |