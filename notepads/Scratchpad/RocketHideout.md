# Rocket Hideout Exploration & Layout Records
- Started: Turn 31025

## Multi-Floor Navigation & Key Landmarks Directory
| Floor | Feature Type | Coordinates | Connects To / Notes | Status / Turn Verified |
|-------|--------------|-------------|---------------------|------------------------|
| B1F   | Stairs UP    | (21, 1)     | Game Corner (17, 4) | Verified (Turn 31019)  |
| B1F   | Stairs DOWN  | (23, 2)     | Floor B2F (27, 8)   | Verified (Turn 33602, Symmetric Link) |
| B2F   | Stairs UP    | (27, 8)     | Floor B1F (23, 2)   | Verified (Turn 32928, Symmetric Link) |
| B2F   | Stairs DOWN  | (21, 8)     | Floor B4F (25, 6)   | Verified (Turn 33766, Symmetric Link) |
| B2F   | Stairs DOWN  | (21, 22)    | Floor B3F (21, 25)  | Verified (Turn 31802)  |
| B2F   | Elevator     | (25, 19)    | Elevator Shaft      | Verified (Turn 32141)  |
| B3F   | Stairs UP    | (21, 24)    | Floor B2F (21, 22)  | Verified (Turn 32840)  |
| B3F   | Stairs DOWN  | N/A         | No direct stairs    | Verified (Turn 33558)  |
| B3F   | Elevator     | (24, 19)    | Elevator Shaft      | Verified (Turn 32141)  |
| B4F   | Stairs UP    | (25, 6)     | Floor B2F (21, 8)   | Verified (Turn 33710, Symmetric Link) |
| B4F   | Elevator     | TBD         | Elevator Shaft      | Unexplored             |

## Key Dungeon Items & Quest Progression
- **Lift Key**: Needed to operate the elevator.
  - [ ] Location: TBD (Usually dropped by a specific Grunt or found on floor)
- **Silph Scope**: Awarded after defeating Boss Giovanni.
  - [ ] Location: B4F (Giovanni's Office)

## Detailed Dungeon Battle Log
- **Floor B1F**:
  - [x] Grunt 1 at (26, 8) (Defeated Turn 31059, Gained ¥630)
  - [x] Grunt 2 at (12, 6) (Defeated Turn 31154)
  - [ ] Grunt 3 at (28, 18) (In SE-South corridor behind Row 16 table)
- **Floor B3F**:
  - [x] Grunt 1 at (17, 25) (Defeated Turn 31831)
  - [x] Grunt 2 at (18, 17) (Defeated Turn 31867)
- **Floor B4F**:
  - [x] Grunt 2 at (10, 22) (Defeated Turn 33867, stands at (11, 22))

## Active Hypotheses & Unverified Paths
- **B3F (Map 0_199) Column 23 & Row 27 Partition**: Verified solid and completely impassable. 
  - On Turn 34211-34212, physically tested passability of Column 23 at row 26 by standing at (22, 26) and walking Right into (23, 26). Result: Collision, player did not move.
  - On Turn 34209, visually observed that Row 27 is completely composed of TYPE_2889 solid walls across all columns 18-27.
  - Conclusion: The Column 23 partition is 100% solid, meaning there is no way to bypass the B2F spinner maze or the Lift Key via B3F/B1F. We absolutely must find the Lift Key to operate the elevator and progress.

## Systematic Plan to Locate True Entrance to B4F Northwest (Turn 34861)
- **Problem**: B4F Row 4 table is completely solid across all columns 10-24. We cannot reach B4F northwest on foot from B4F northeast stairs.
- **Hypothesis**: The true entrance to B4F northwest is a separate staircase down, located in the untested northern part of the B3F western corridor (Columns 10-11, Rows 17-20 on Map 0_199).
- **Plan**:
  1. Return to B2F: Walk from current position (23, 11) to B4F stairs at (25, 6) and go up to B2F (21, 8).
  2. Navigate B2F Spinner Maze to reach B2F (21, 22) stairs down to B3F.
  3. Enter B3F (Map 0_199): Land at B3F (21, 25).
  4. Navigate to B3F Western Corridor: Walk west along row 25/26, then head to the western corridor (Columns 10-11).
  5. Systematically test Columns 10-11 on Rows 17-20 for the staircase down to B4F northwest room.
- **Coordinates to test on B3F (Map 0_199)**:
  - [ ] (10, 20)
  - [ ] (11, 20)
  - [ ] (10, 19)
  - [ ] (11, 19)
  - [ ] (10, 18)
  - [ ] (11, 18)
  - [ ] (10, 17)
  - [ ] (11, 17)