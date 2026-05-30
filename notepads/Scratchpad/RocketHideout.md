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
  - Row 7 is a completely open horizontal corridor running from column 13 to column 25.
  - Column 22 is a solid vertical wall (TYPE_2889) extending from Row 8 down to at least Row 15, dividing the East and West sections of B1F.
  - Column 15 is a solid vertical wall (TYPE_2889) extending from Row 8 down to at least Row 11, dividing the West-Center corridor (Columns 17-20) from the Far-West corridor (Columns 13-14).
  - Row 8 has walls at (13, 8)-(14, 8) and plant pots at (16, 8).
  - The Far-West corridor (Columns 13-14, Rows 9-11) is passable but cannot be accessed from Row 7 on columns 13-14 due to the Row 8 wall. We will explore further left to see if there is an entrance.

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

## Detailed Dungeon Battle Log
- **Floor B1F**:
  - [x] Grunt 1 at (26, 8) (Defeated Turn 31059, Gained ¥630)
  - [ ] Grunt 2 at (12, 6)
- **Floor B2F**:
  - [ ] Grunts: TBD
- **Floor B3F**:
  - [ ] Grunts: TBD
- **Floor B4F**:
  - [ ] Grunts: TBD
  - [ ] Boss Giovanni: TBD