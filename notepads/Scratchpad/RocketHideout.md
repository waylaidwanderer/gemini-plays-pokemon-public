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
- **Lift Key Retrieval Run (Started Turn 34255)**:
  - Backtracked B3F -> B2F (Turn 34216).
  - Used DIG from B2F (11, 25) (Turn 34225) to return to Celadon City.
  - Entered Game Corner and went down to B1F (Turn 34254).
  - Went B1F (21, 2) -> B2F (27, 8) (Turn 34255).
  - Took direct B2F shortcut from (27, 8) to (21, 8) (Turn 34257-34259).
  - Planning to descend to B4F and navigate to the Lift Key Grunt's room.

## Lift Key Retrieval & Grunt Battle Plan (Turn 34337)
- **Hypothesis**: The Lift Key Grunt is located at (16, 12) inside the northwest spinner maze of B4F.
- **Route to Grunt**:
  - Step 1: Walk from (25, 6) to the entrance of the maze at (20, 11) / (15, 11).
    - From (25, 6), walk Left to (20, 6) (or (22, 6) first). Let's trace carefully: Row 6 is open from column 21 to column 28. Row 5 is also open. Row 7 is open.
    - Let's walk Left to column 20, then Down to row 11.
  - Step 2: From (20, 11), walk Left to (15, 11).
  - Step 3: From (15, 11), go: Right 5 to (20, 11) -> Up 2 to (20, 9) -> Left 7 to (13, 9) -> Down 2 to (13, 11).
  - Step 4: From (13, 11), walk Right onto (14, 11) Right-spinner to slide to (16, 11) stop tile, directly in front of the Grunt at (16, 12).
- **Verification**: Test if walking Right onto (14, 11) slides us to (16, 11) as hypothesized.