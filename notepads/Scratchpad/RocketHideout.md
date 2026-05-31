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
  - [ ] Location: Rocket Grunt 1 at B4F (23, 12).
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
  - [ ] Grunt 1 at (23, 12) (Undefeated, stands in front of stairs UP to B2F)

## Deadlock Resolution: Socratic Rigor Audit (Turn 35228)
### Question 1: If the Lift Key is a hardcoded drop in vanilla, but B4F Grunt 1 (northeast) and Grunt 2 (southwest) both use door-guard/standard dialogue and do not drop the key, does this imply the Lift Key is held by an entirely different Rocket Grunt in this ROM?
- **Analysis**: No! The previous northeast/southwest grunts we fought were actually on B3F (Map 0_201). Rocket Grunt 1 on B4F (Map 0_202) is standing at (23, 12) in the right section and is undefeated. He is the true vanilla dropper of the Lift Key! When we defeat him, he will drop the key.
- **Action/Parameters**: Backtrack to B3F, ascend to B2F, navigate B2F to (21, 8), descend B2F stairs to B4F right section (25, 6), and fight the undefeated Rocket Grunt 1 at (23, 12).

### Question 2: B1F Grunt 3 at (28, 18) remains undefeated. Have we exhaustively verified every single boundary and warp on B1F and B2F to prove that no other path exists to the southern B1F area?
- **Analysis**: We've confirmed B1F southern area is unreachable from B1F north. The elevator is the intended progression route, which we will access once we retrieve the Lift Key from B4F.

### Question 3: Could the Lift Key have been dropped as an item ball by one of the defeated Grunts on B3F or B2F?
- **Analysis**: Unlikely since Rocket Grunt 1 on B4F (23, 12) is undefeated and is the true source of the Lift Key.

## Northeast Section Stairs Connection Hypothesis (Turn 35403)
- **Socratic Challenge / Strategy Critique**: How do we reach the eastern room of B4F (Map 0_202) where Rocket Grunt 1 (holding the Lift Key) is located?
- **Verification Findings (Turn 35496)**:
  - We systematically swept the northeast room of B3F (Map 0_201) on Turns 35438-35465.
  - **Results**:
    - The northeast room is a complete cul-de-sac. It contains ONLY the staircase UP to B2F (21, 8) located at (25, 6), and a single defeated Rocket Grunt standing at (26, 11)/(26, 12).
    - When spoken to, this Grunt says: "Go ahead and go! But, you need the LIFT KEY to run the elevator!"
    - No other staircases or pathways down to B4F exist in this room.
  - **Conclusion**: The hypothesis that there is a staircase DOWN to B4F in the B3F northeast room is definitively disproven. B4F eastern section either does not exist or is completely isolated, meaning the Lift Key Grunt MUST be located in the western/northwestern section of B4F (Map 0_202) accessible via the B3F western stairs at (18, 16). We must return to the B4F northwest room to find the Lift Key.

## Verified B3F East-West Traversal (Turn 35664)
- **Result**: Successfully verified that rows 5, 6, and 7 are fully open and walkable on Map 0_201 (B3F). We walked directly from B3F East (25, 6) to B3F West (11, 6) along row 6, completely bypassing the spinner maze backtrack!
## B3F Western Corridor to B4F Direct Route (Turn 35914 - Active)
- **Methodology**: To bypass all spinner-puzzles and avoid any collision traps, we utilize a completely deterministic, spinner-free, and 100% safe vertical shortcut. Steps 1-4 have been successfully completed.
- **Remaining Steps**:
  5. Walk West along the northern corridor on row 6 to (11, 6).
  6. Walk Down columns 10-11 to row 25.
  7. Walk East along row 25 to column 18.
  8. Walk Up column 18 to row 19.
  9. Walk Right from (18, 19) to (19, 19) to descend the stairs to B4F!
- This has been systematically planned and cross-verified against established floor collision maps.