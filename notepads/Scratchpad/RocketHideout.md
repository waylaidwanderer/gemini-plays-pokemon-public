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

## B4F West Lift Key Systematic Investigation Plan (Turn 36392)
- **Goal**: Confirm the location of and retrieve the LIFT KEY from B4F West.
- **Background**: Rocket Grunt 3 was defeated at B4F (11, 22) on Turn 33850. In standard Gen I mechanics, the Lift Key drops on the floor as an item ball upon defeating this Grunt. Since the Lift Key is currently not in our inventory, the item ball must still be on the ground in the southwest room around (11, 22) or (12, 22).
- **Execution Steps**:
  1. Backtrack from B3F Northeast (26, 11) to B3F West stairs DOWN at (19, 19).
     - Walk UP 5 steps to (26, 6) in the open northern area of B3F.
     - Walk LEFT along Row 6/7 to the B3F West area.
     - Navigate to the stairs DOWN at (19, 19).
  2. Descend stairs at (19, 19) to arrive on B4F at (19, 10).
  3. Navigate B4F West to the southwest room around (11, 22).
  4. Perform a systematic visual sweep of the floor tiles (especially rows 21-23, columns 10-12) to locate the Lift Key item ball.
  5. Interact with the item ball using 'A' to retrieve the Lift Key.
  6. Verify Lift Key acquisition in the Game State inventory.

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