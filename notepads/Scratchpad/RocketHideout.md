# Rocket Hideout Exploration & Layout Records
- Started: Turn 31025
- Primary Goal: Locate and clear Celadon Game Corner / Rocket Hideout to secure the SILPH SCOPE.

## Floor B1F (Map 0_199)
- Spawn Point/Stairs to Game Corner: (21, 1). Stair tile itself is at (21, 1).
- Room shape: Wall boundaries on top at row 0, left at column 18, right at column 25.
- There is a shelf/cabinet object at (23, 2).
- The room opens up at the bottom: row 4 has walls at columns 17-19 and columns 24-26, but is completely passable in columns 20-23 (TYPE_3fe2).
- Row 5 and 6 are checkered floor tiles (TYPE_3fe2) extending from column 17 to 26, meaning we can go south and then explore the rest of B1F.
- **West Side Layout (Verified Turns 31117-31120)**:
  - Row 7 is a completely open horizontal corridor running from column 13 to column 25, terminating at the west wall at column 8.
  - Column 22 is a solid vertical wall (TYPE_2889) extending from Row 8 down to at least Row 15, dividing the East and West sections of B1F.
  - Column 15 is a solid vertical wall (TYPE_2889) extending from Row 8 down to at least Row 11, dividing the West-Center corridor (Columns 17-20) from the Far-West corridor (Columns 13-14).
  - Row 8 has walls at (13, 8)-(14, 8), (23, 8)-(24, 8) and plant pots at (16, 8).
  - The Far-West corridor (Columns 9-14, Rows 9-13) can be entered via a gap at (11, 8)-(12, 8) on Row 8, linking the Row 7 corridor directly to this southern area.
  - A table is situated at rows 12-13 across columns 10-13, requiring navigation around column 9 or column 14.
  - Column 8 is a solid vertical wall (TYPE_2889) running from Row 3 to Row 11, verified by a collision test on Turn 31267 when attempting to move Left from (9, 7). No passage exists west of Column 9 on Row 7.

## Multi-Floor Navigation & Key Landmarks Directory
| Floor | Feature Type | Coordinates | Connects To / Notes | Status / Turn Verified |
|-------|--------------|-------------|---------------------|------------------------|
| B1F   | Stairs UP    | (21, 1)     | Game Corner (17, 4) | Verified (Turn 31019)  |
| B1F   | Stairs DOWN  | TBD         | Floor B2F           | Unexplored             |
| B1F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |
| B2F   | Stairs UP    | TBD         | Floor B1F           | Unexplored             |
| B2F   | Stairs DOWN  | TBD         | Floor B3F           | Unexplored             |
| B2F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |
| B3F   | Stairs UP    | TBD         | Floor B2F           | Unexplored             |
| B3F   | Stairs DOWN  | TBD         | Floor B4F           | Unexplored             |
| B3F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |
| B4F   | Stairs UP    | TBD         | Floor B3F           | Unexplored             |
| B4F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |

## Key Dungeon Items & Quest Progression
- **Lift Key**: Needed to operate the elevator.
  - [ ] Location: TBD (Usually dropped by a specific Grunt or found on floor)
- **Silph Scope**: Awarded after defeating Boss Giovanni.
  - [ ] Location: B4F (Giovanni's Office)

## Dungeon Items Log
- **Floor B1F**:
  - [x] Poké Ball at (11, 14) (ESCAPE ROPE, Turn 31175)
  - [ ] Poké Ball at (9, 17) (Visible in southwest section)

## Detailed Dungeon Battle Log
- **Floor B1F**:
  - [x] Grunt 1 at (26, 8) (Defeated Turn 31059, Gained ¥630)
  - [x] Grunt 2 at (12, 6) (Defeated Turn 31154)
  - [ ] Grunt 3 at (28, 18) (In SE-South corridor behind Row 16 table)
- **Floor B3F**:
  - [ ] Grunts: TBD
- **Floor B4F**:
  - [ ] Grunts: TBD
  - [ ] Boss Giovanni: TBD
- Row 16 has UP-pointing spinner tiles at (24, 16) and (25, 16) which block access to the southern area of the eastern room from the north.
- Row 16 has a solid wall of TYPE_2889 across columns 9-14, and column 15 is a solid vertical wall of TYPE_2889, meaning the southwest room (columns 9-14) is blocked from the south on B1F. The Poké Ball at (9, 17) is currently inaccessible from B1F.