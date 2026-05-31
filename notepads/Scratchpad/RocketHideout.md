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

## Rocket Hideout Structural Deadlock Resolution Plan (Turn 35163)
- **Problem Statement**: We have thoroughly searched B4F's northeast room (Grunt 1's positions at (26, 9) and (26, 12)) and confirmed the Lift Key is not there. The elevator doors on B2F, B3F, and B4F are locked and require the Lift Key.
- **Objective**: Systematically investigate all alternative possibilities to locate the Lift Key or bypass the lock.
- **Hypotheses to Test**:
  1. **Hypothesis 1: Rocket Grunt 2 in the southwest of B4F (11, 22) is the actual Lift Key dropper.**
     - *Testing Method*: Navigate to the southwest of B4F, talk to Grunt 2 at (11, 22), and systematically search the surrounding floor (X=9-13, Y=21-24).
  2. **Hypothesis 2: B1F Grunt 3 at (28, 18) is reachable or B1F has another pathway to the southern area.**
     - *Testing Method*: If Hypothesis 1 fails, we will backtrack to B1F and systematically test the B1F boundaries to verify if there is an overlooked path to the south.
  3. **Hypothesis 3: The Lift Key was dropped by a defeated Grunt on B3F at (18, 17) or B2F at (20, 13).**
     - *Testing Method*: If Hypotheses 1 and 2 fail, we will sweep the floors of B3F and B2F around their defeated Grunts' coordinates.
  4. **Hypothesis 4: Superposition Soft-lock Theory (Grunt 1 blocks Lift Key at (26, 12)).**
     - *Description*: In Gen 1, if the Lift Key was dropped at Grunt 1's starting position (26, 12), and the Grunt reset to (26, 12) upon re-entering the map, his overworld sprite collision completely overrides the Lift Key item-pickup.
     - *Testing/Mitigation*:
       - Try speaking to him from different angles/different states to trigger a coordinate shift.
       - Verify if leaving and re-entering without saving/reloading resolves his position.
       - Consider if there is a different floor transition or container we missed.

### Active Execution:
- Navigating through the B4F spinner maze to reach the southwest corner at (11, 22) to test Hypothesis 1.