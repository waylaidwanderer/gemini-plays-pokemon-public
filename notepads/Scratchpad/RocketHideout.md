# Rocket Hideout Exploration & Layout Records
- Started: Turn 31025

## Multi-Floor Navigation & Key Landmarks Directory
| Floor | Feature Type | Coordinates | Connects To / Notes | Status / Turn Verified |
|-------|--------------|-------------|---------------------|------------------------|
| B1F   | Stairs UP    | (21, 1)     | Game Corner (17, 4) | Verified (Turn 31019)  |
| B1F   | Stairs DOWN  | (23, 2)     | Floor B2F (27, 8)   | Verified (Turn 33602, Symmetric Link) |
| B2F   | Stairs UP    | (27, 8)     | Floor B1F (23, 2)   | Verified (Turn 32928, Symmetric Link) |
| B2F   | Stairs DOWN  | (21, 8)     | Floor B3F (25, 6)   | Verified (Turn 33766, Symmetric Link) |
| B2F   | Stairs UP    | (21, 22)    | Floor B1F (21, 25)  | Verified (Turn 31802)  |
| B2F   | Elevator     | (25, 19)    | Elevator Shaft      | Verified (Turn 32141)  |
| B3F   | Stairs UP    | (25, 6)     | Floor B2F (21, 8)   | Verified (Turn 33710, Right Section) |
| B1F   | Stairs DOWN  | (21, 25)    | Floor B2F (21, 22)  | Verified (Turn 34946, Southern Section) |
| B3F   | Stairs DOWN  | (19, 19)    | Floor B4F (19, 10)  | Verified (Turn 35235)  |
| B3F   | Elevator     | (24, 19)    | Elevator Shaft      | Verified (Turn 32141)  |
| B4F   | Stairs UP    | (19, 10)    | Floor B3F (19, 19)  | Verified (Turn 35235, Left Section) |

## Key Dungeon Items & Quest Progression
- **Lift Key**: Needed to operate the elevator.
  - [x] Lift Key: Obtained (Turn 36614)
  
- **Silph Scope**: Awarded after defeating Boss Giovanni.
  - [ ] Location: B4F (Giovanni's Office)

## Detailed Dungeon Battle Log
- **Floor B1F (Map 0_199)**:
  - [x] Grunt 1 at (26, 8) (Defeated Turn 31059)
  - [x] Grunt 2 at (12, 6) (Defeated Turn 31154)
  - [ ] Grunt 3 at (28, 18) (In SE-South corridor behind Row 16 table)
- **Floor B2F (Map 0_200)**:
  - [x] Grunt 1 at (20, 13) (Defeated Turn 31616)
- **Floor B3F (Map 0_201)**:
  - [x] Grunt 1 at (17, 25) (Defeated Turn 31831)
  - [x] Grunt 2 at (18, 17) (Defeated Turn 31867)
  - [x] Grunt 3 at (10, 22) (Defeated Turn 33867) (Note: Formerly misidentified as B4F southwest Grunt)
- **Floor B4F (Map 0_202)**:
  - [x] Grunt 1 (Defeated, dropped Lift Key at 10, 2)

## Verified B2F Elevator Route from (16, 13)
- **Status**: Tested and 100% verified collision-free on Turn 36659.
- **Starting Position**: (16, 13) on Map 0_200.
- **Route Steps**:
  1. Move Right to (17, 13) and then (18, 13).
  2. Walk Up to (18, 12) and (18, 11).
  3. Walk Left onto (17, 11) Left-spinner (TYPE_55d0). This slides us Left to (16, 11).
  4. Walk Left through (15, 11), (14, 11), and (13, 11).
  5. Walk Left onto (12, 11) Up-spinner (TYPE_cf9b). This slides us Up to (12, 10).
  6. Walk Up onto (12, 9) Left-spinner (TYPE_55d0). This slides us Left to (11, 9).
  7. Walk Left onto (10, 9) Left-spinner (TYPE_55d0). This slides us Left to (9, 9).
  8. Walk Left onto (8, 9) Left-spinner (TYPE_55d0). This slides us Left to (7, 9).
  9. Walk Left through (6, 9) and (5, 9).
  10. Walk Left onto (4, 9) Left-spinner (TYPE_55d0). This slides us Left to (1, 9).
  11. From (1, 9), walk Right to (2, 9) and then (3, 9) (bypassing the Left-spinner).
  12. Walk Down along column 3 through (3, 10), (3, 11), (3, 12), and (3, 13).
  13. Walk Right to (4, 13) [Current Position on Turn 36664].

## Remaining B2F Elevator Route from (4, 13) to (24, 19)
- **Start Turn**: 36682 (Commenced final maze traversal leg)
- **Coordinates to Navigate**:
  - Walk Down from (4, 13) to (4, 14).
  - Walk Right onto (5, 14) Right-spinner (TYPE_64a2) -> slides to (6, 14).
  - Walk Right through (7, 14) and (8, 14).
  - Walk Right onto (9, 14) Down-spinner (TYPE_55cd) -> slides to (9, 15).
  - Walk Right onto (10, 15) Up-spinner (TYPE_cf9b) -> slides to (10, 14).
  - Walk Down onto (10, 15) Up-spinner -> slides back to (10, 14) (no-op/alignment).
  - Walk Right onto (11, 14) Down-spinner (TYPE_55cd) -> slides to (11, 15).
  - Walk Down onto (11, 16) Right-spinner (TYPE_64a2) -> slides to (15, 18) Stop tile (via 12,16 -> 13,16 Right-spinner -> 14,16 -> 15,16 Down-spinner -> 15,17 -> 15,18).
  - Walk Down from (15, 18) to (15, 19) -> wait, (15, 19) is blocked!
  - Walk Right from (15, 18) to (16, 18).
  - Walk Down through (16, 19) and (16, 20).
  - Walk Right through (17, 20), (18, 20), and (19, 20).
  - Walk Up to (19, 19).
  - Walk Right through (20, 19), (21, 19), (22, 19), (23, 19), and enter the elevator at (24, 19).

## B3F Western Spinner Maze Bypass Discovery & Verification (Turns 36406 - 36472)
- **Hypothesis**: We can reach the B3F West stairs DOWN to B4F West at (19, 19) by navigating through the B3F spinner maze.
- **Physical Testing & Verification**:
  1. Turn 36411: Navigated to (16, 11).
  2. Turn 36414: Stepped on (17, 12) Down-spinner, slid to Stop tile at (17, 16).
  3. Turn 36430: Noticed (11, 10) and (12, 10) on Row 10 are solid TYPE_2889 blocks, meaning column 11 is blocked at Row 10.
  4. Turn 36444: Noticed (12, 17) on Row 17 is a Right-spinner, meaning column 12 is blocked at Row 17.
  5. Turn 36456: Noticed (11, 16), (10, 16), and (9, 16) on Row 16 are completely open and walkable TYPE_3fe2 tiles (correcting the old assumption that Row 16 was solid).
  6. Turn 36465: Noticed (13, 21) is a solid TYPE_2889 wall block, making Row 21 impassable.
  7. Turn 36466: Verified via custom BFS simulator that stepping Right onto (11, 18) Right-spinner slides us through (12, 18)-(14, 18) to the (15, 18) Down-spinner, which then slides us ALL the way down column 15 to the bottom wall at (15, 26). This completely bypasses the Row 21 wall!
- **Verified Collision-Free Route**:
  - From (12, 13) -> Down 3 to (12, 16) -> Left 3 to (9, 16) -> Down 1 to (9, 17). (Successfully executed Turn 36464!)
  - From (9, 17) -> Down 1 to (9, 18) -> Right 2 to (11, 18) (triggers slide to 15, 26) -> Up 5 to (15, 21) -> Right 4 to (19, 21) -> Up 2 to (19, 19) (Stairs down).
- **Result**: Definitively proven to be 100% collision-free.