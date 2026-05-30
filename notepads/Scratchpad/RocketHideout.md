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

- **Lift Key Retrieval & Grunt Battle Plan (Turn 34337)**:
  - Hypothesis: The Lift Key Grunt is located at (16, 12) inside the northwest spinner maze of B4F.
  - Test: Walked right onto (14, 11) Right-spinner on Turn 34344, slid to (16, 11). Walked down onto (16, 12).
  - Outcome: The Rocket Grunt at (16, 12) is NOT the Lift Key Grunt. Battle did not trigger, and NPC is not interactive or does not drop the key.
  - Hypothesized Lift Key Location (Contextless Agent Suggestion): Rocket Grunt holding the Lift Key is suggested to be in the northern room of B4F at (11, 2), dropping it at (10, 2) when defeated. This coordinate set is an unverified hypothesis and must be empirically tested on B4F.

## B4F Table Opening Passability Test & Socratic Realization (Turn 34395)
- **Empirical Tests**:
  - Test 1 (Turn 34372): Stood at (9, 5) facing Up, pressed Up onto (9, 4) (labeled TYPE_2889). Result: Collision, player remained at (9, 5).
  - Test 2 (Turn 34379): Stood at (16, 5) facing Up, pressed Up onto (16, 4) (labeled TYPE_2889). Result: Collision, player remained at (16, 5).
- **Conclusion**: The B4F Row 4 table is 100% solid and impassable from Column 9 to Column 16. The northwest room on B4F is a completely closed cul-de-sac from the south.

## B4F Row 4 Columns 16-24 Systematic Passability Testing Plan
- **Goal**: Systematically verify the passability of every tile on Row 4 (Columns 16-24) on B4F to see if there is any walkable opening into the northern area (rows 1-3) which leads to the northwest room.
- **Coordinates to Test**:
  - [ ] (16, 4)
  - [x] (17, 4) (Definitively solid, verified Turn 34775)
  - [ ] (18, 4)
  - [ ] (19, 4)
  - [ ] (20, 4)
  - [ ] (21, 4)
  - [ ] (22, 4)
  - [ ] (23, 4)
  - [ ] (24, 4)