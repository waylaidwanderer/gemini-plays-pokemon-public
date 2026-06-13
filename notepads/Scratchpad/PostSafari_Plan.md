# Post-Safari Zone Route & Progression Plan (Cinnabar Mansion)

## Cinnabar Mansion Deep B1F Routing & Switch Matrix (Turn 78160)
- **State A (Statue 2 Default)**:
  - Gate 1 on 1F (25, 13) is CLOSED, blocking foot access to the Southeast room.
  - Gate 3 on 2F (18, 8)-(19, 8) is OPEN (Verified OPEN on Turn 78836).
  - Gate 4 on 1F East (21, 17) is OPEN.
  - Gate 6 on 2F (9, 4)-(9, 5) is CLOSED.
  - Gate 18 on 2F (2, 18) is CLOSED.
  - Gate 26 on 2F (12, 26)-(13, 26) is CLOSED.
  - Gate 13 on 2F (12, 13)-(13, 13) is CLOSED.

- **State B (Statue 2 Toggled)**:
  - Gate 1 on 1F (25, 13) is OPEN, allowing foot access to the Southeast room.
  - Gate 3 on 2F (18, 8)-(19, 8) is CLOSED (Verified CLOSED on Turn 84976).
  - Gate 4 on 1F East (21, 17) is CLOSED.
  - Gate 6 on 2F (9, 4)-(9, 5) is OPEN.
  - Gate 18 on 2F (2, 18) is OPEN (Verified on Turn 86403 by toggling Statue 2 to State B).
  - Gate 26 on 2F (12, 26)-(13, 26) is CLOSED.
  - Gate 13 on 2F (12, 13)-(13, 13) is CLOSED.

## State B Southeast Room Isolation Verification (Turn 85829 Verification)
- **Hypothesis**: The Southeast room (Columns 25-28) of 1F East is completely isolated on foot from the B1F stairs at (21, 23) under State B.
- **Methodology**: Stood at (25, 21) on Turn 85829 and visually analyzed the surrounding tile map:
  - Column 24 has a solid wall of TYPE_2889 extending vertically on Rows 19-23.
  - Column 24 and 25 have solid rubble of TYPE_2889 at (24, 24), (25, 24), and (25, 25).
  - Therefore, there is no horizontal pathway connecting Column 25 and Column 21 on the south side.
- **Definitive Conclusion**: The Southeast room of 1F East is indeed completely isolated on foot from the rest of 1F. We must backtrack and toggle the switch to State B to cross to 3F East on foot.

## State B Southeast Room Search Verification (Turn 85901 Completed)
- **Definitive Conclusion**: On Turn 85901, we completed 100% of our systematic floor coverage of the entire Southeast room of 1F East under State B (tested Rows 14-26, Columns 24-28). None of the tiles triggered a staircase transition or warp. This empirically and definitively proves that there is no staircase in the Southeast room of 1F East under State B.
- **State A Northeast Staircase Verification (Turn 85926 Completed)**:
  - We toggled Statue 1 back to State A (Default) on Turn 85913, navigated back to 1F East Northeast room, and tested walking Up onto (27, 11) from (27, 12).
  - **Result**: Direct collision bump against (27, 11), remaining at (27, 12) on Turn 85926.
  - **Definitive Conclusion**: The Northeast staircase at (27, 11) / (27, 10) remains completely solid, blocked, and impassable under State A as well. There is no staircase on 1F East under any state.

## Cinnabar Mansion Breakthrough Exploration Phase (Turn 79491)
- **Verified Fact**: 2F East South Column 22 is completely solid/rubble under both State A and State B across rows 8-15. This separates Column 21 from Column 23 on these rows.

- **B1F Mapping Protocol**:
  - Once in B1F, we will walk along every passable tile, logging items, statues, and gates.
  - We will record all B1F gates and switch dependencies in `Scratchpad/Mansion_Gate_Matrix` using our structured circuit matrix format.

### 3F East Pit-Mapping Spatial Safety Protocol (Added Turn 79515)
- **The Risk**: Overworld pit tiles (such as TYPE_21ec, visually dark voids) trigger immediate, irreversible map transitions/falls upon step contact. Rushing can result in an accidental fall before mapping is complete.
- **Safety Protocol**:
  1. Once we cross into the eastern wing on 3F East, we will limit all movements near boundaries or unfamiliar areas to **1-tile chunks** (pressing only one directional button at a time).
  2. We will verify the screen and tile labels after every single step.
  3. We will NEVER step blindly onto any tile that has not been confirmed to be a standard floor tile (such as TYPE_3fe2).
  4. We will systematically map the coordinates of all walls, balconies, and pit boundaries from a safe distance before choosing which pit to fall into.

## Socratic Socratic Answers (Turn 79575)
### Socratic Question 1: 3F East Pit Landing & Escape Protocol
- **Historical Note (State B)**: Under State B, we previously analyzed dropping to the 1F south-central pocket. However, physical testing has proved that Column 24 is a solid wall on Rows 19-24 and Gate 4 is closed under State B, meaning the 1F Southeast room is completely isolated on foot from the B1F stairs. Therefore, the State B Pit Drop Route is disproven.

### Socratic Question 3: Basement Switch Architecture (B1F)
- **Mapping Plan**: B1F is completely unmapped. We will walk every walkable corridor on B1F, logging coordinates of all walls, items, and gates.
- **Circuit Matrix Logging**: We will record all basement gates and their status under State A and State B in `Scratchpad/Mansion_Gate_Matrix`.
- **Statue 4 Evaluation**: If we discover a fourth Mewtwo Statue (Statue 4), we will stand adjacent, face it, and interact with 'A' to toggle it. We will then systematically map which gates in B1F open/close, logging the exact turn and proof of work in our matrix.

## Strategic Notes from Overwatch Audit (Turn 80167)
- **1F West Switch Statue 1 Plan**: If we need to find and toggle Statue 1 on 1F West in the future, we must explore the westernmost room (Columns 1-4, typically around (2, 5)), as the statue at (10, 8) has been proven decorative.

## Socratic Strategy & Coordinate Verification (Turn 80913 Audit) - Verified & Updated
- **Analysis of Southeast Room Rows**:
  - The Southeast room is documented to span Rows 9-15 on 2F East (Map 0_214).
  - Physical testing on Turn 76552-76760 has proven that the Southeast room is 100% isolated and cannot be reached on foot on 2F under both State A and State B because Column 22 is completely blocked by solid rubble/walls on Rows 8-15.
  - Socratic Question 1 is fully resolved: the 2F Southeast room is completely unreachable on foot.
- **Definitive 3F Crossover Passability Audit (Updated Turn 81543)**:
  - We have previously concluded that 3F West is completely blocked from 3F East under both State A and State B.
  - However, our previous testing under State B (Turn 81045) was flawed because we stood on a solid wall tile (8, 12) and tried to walk Right onto (9, 12), resulting in a bump. In Gen 1, attempting to walk from an already solid tile always results in a collision.
  - On Turn 81534, we tested walking Down from the open tile (9, 11) onto (9, 12) under State B (Statue 2 Toggled). Result: **Bump**, remaining at (9, 11). This empirically proves that (9, 12) is indeed 100% solid and impassable under State B.
  - On Turn 81538, we tested walking Right from the open tile (9, 11) onto (10, 11) under State B (Statue 2 Toggled). Result: **Bump**, remaining at (9, 11). This empirically proves that (10, 11) is indeed 100% solid and impassable under State B.
  - Since Column 10 is completely solid rubble/walls on Rows 8-15, and Row 12 Column 9 is solid rubble/wall under State B, the 3F West-East crossover is 100% physically blocked and impassable on foot under BOTH State A and State B. There is no walkthrough connection on 3F.

## State B Northeast Room Complete Sweep Disproof (Turn 86172 Completed)
- **Definitive Conclusion**: On Turn 86172, we completed 100% of our systematic floor coverage of the entire Northeast room of 1F East under State B (tested Rows 1-11, Columns 23-28 on all walkable tiles). Absolutely none of the tiles triggered a staircase transition or warp, and (27, 11) is a solid, closed rubble wall when approached from the proper southern direction at (27, 12). This empirically and definitively disproves the existence of any active staircase or warp in the Northeast room of 1F East under State B.
## Active State A Northeast Room Hypothesis (Started Turn 86221)
- **The Hypothesis**: Since 3F West-East crossover is completely solid under both states, and the 2F Southeast room (with stairs up to 3F East) is isolated, and 1F East Northeast room has no stairs under State B, the active staircase to 2F East Southeast/Northeast must be active and accessible under State A!
  - Under State A, we can enter the Northeast room of 1F East on foot via the northern crossover on Column 22 Row 3 (which is open under State A).
  - We successfully toggled Mewtwo Statue 1 to State A (Default) on Turn 86214.
  - We will now systematically test all tiles in the Northeast room on foot under State A and log every coordinate-specific outcome below.

## State A Northeast Room Systematic Exploration Logs
- Turn 86234: Successfully entered the Northeast room of 1F East at (23, 3) under State A.
- Turn 86241: Completed Row 1 sweep (Columns 23-28). Verified all are standard floor tiles with no staircases or warps.
- Turn 86246: Completed Row 2 sweep (Columns 23-27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86249: Completed Row 3 sweep (Columns 23-27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86253: Completed Row 4 sweep (Columns 26-27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86255: Completed Row 5 sweep (Columns 23-27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86258: Completed Row 6 sweep (Columns 23-28). Verified all are standard floor tiles with no staircases or warps.
- Turn 86259: Completed Row 7 sweep (Columns 23-28). Verified all are standard floor tiles with no staircases or warps.
- Turn 86263: Completed Row 8 sweep (Columns 23, 26, 27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86273: Completed Row 9 sweep (Columns 23, 26, 27). Verified all are standard floor tiles with no staircases or warps.
- Turn 86282: Completed Row 10 sweep (Columns 23-26). Verified all are standard floor tiles with no staircases or warps.
- Turn 86286: Completed Row 11 sweep (Columns 23-26). Verified all are standard floor tiles with no staircases or warps.
- **Definitive 1F East Northeast Room Complete Sweep Disproof**: We have now systematically and physically walked over every single passable floor tile in the Northeast room of 1F East under both State A (Default) and State B. Absolutely none of the tiles triggered a staircase transition or warp. This empirically and definitively disproves the existence of any active staircase or warp in the Northeast room. Combined with the complete sweep disproof of the Southeast room of 1F East, we can definitively state that **1F East is completely staircase-less**. The staircase to 2F East South/Southeast must be accessed by some other means.

## 3F West Gate & Balcony Complete Audit (Turn 86326)
- **Turn 86316 Gate (8, 8) Test**: Stood at (8, 9) facing Up under State A and pressed Up. Result: BUMP against (8, 8), proving the gate is CLOSED and impassable under State A.
- **Turn 86323 Balcony (2, 16) Test**: Stood at (2, 16) facing Down under State A and pressed Down. Result: BUMP against (2, 17), proving Column 2 Row 17 is solid and impassable under State A.
- **Turn 86325 Balcony (1, 16) Test**: Stood at (1, 16) facing Down under State A and pressed Down. Result: BUMP against (1, 17), proving Column 1 Row 17 is solid and impassable under State A.
- **Definitive 3F West Balcony Disproof**: All balcony drop directions on 3F West are 100% solid and blocked under both State A and State B. There is no drop-off to 2F East South from the 3F West balcony. We must find another crossover method.
- Active Phase Start: Turn 86550. Currently on Turn 86739.

## breakthrough discovery: 3F Row 12 corridor under State B
On Turn 86575, we fell through Pit A under State B by executing a path that took us South of Row 12 (specifically to Row 14/15, where we fell through the pit). However, Row 12 on 3F East is a completely solid, safe corridor leading to the eastern balcony (3F East)!
Therefore, the correct plan is:
1. Walk Up onto the stairs at (7, 10) on 3F West to descend to 2F West.
2. Go to Mewtwo Statue 2 at (2, 11) on 2F West and toggle to State B.
3. Return to 3F West via the stairs.
4. Walk to (9, 11), step Down to (9, 12), and walk straight East (Right) along Row 12 to 3F East (the balcony): (10, 12) -> (11, 12) -> (12, 12) -> (13, 12) -> (14, 12) -> and keep going right!
5. On 3F East balcony, jump down the rightmost pit to land on 1F East near B1F stairs.
6. Retrieve the Secret Key from B1F!

## Disproven State B 2F East South Balcony Drop Strategy (Completed)
- **Result**: Exhaustively tested and disproven on Turns 86660-86689. All tested balcony drops are solid and blocked. Backtracked out of the room successfully on Turn 86700.
- Turn 86688 Test: Walking Down from (13, 16) onto (13, 17) under active State B does NOT trigger any balcony drop animation, proving Column 13 Row 17 is a normal passable floor tile under State B. This exhaustively disproves the existence of any active balcony drops under State B.

## Active State A 1F Northeast Staircase Walkthrough Strategy (Started Turn 86790)
- **Objective**: Reach B1F by utilizing the State A 1F East Northeast staircase.
- **Topological Plan**:
  1. Toggle Statue 2 to State A on 2F West (Completed Turn 86780).
  2. Descend to 1F West (Completed Turn 86783).
  3. Walk from 1F West to 1F East on foot (Completed Turn 86785).
  4. Navigate to Column 22 Row 3 on 1F East under State A.
  5. Cross Column 22 Row 3 East into the Northeast room of 1F East.
  6. Walk South to Row 12, and step onto the (26, 12) Northeast staircase to go up to 2F East.
  7. On 2F East, walk South through the open Row 8 gate to the 2F East Southeast room.
  8. Climb the stairs at (25, 14) up to 3F East.
  9. On 3F East, walk onto the balcony and drop down the rightmost pit to land in the isolated 1F East south-central pocket where the B1F stairs are located.
  10. Descend to B1F!

## State B Crossover Corridor (9, 12) and (10, 12) Passability Testing Protocol
- **Objective**: Determine if Column 9 Row 12 (9, 12) is completely passable under State B when the Scientist NPC is not blocking it.
- **Methodology & Outcome (Turn 86575-86582)**:
  - Toggled Statue 2 on 2F West to State B on Turn 86561.
  - Returned to 3F West via the stairs at (7, 10) on Turn 86564.
  - Attempted to cross Row 12 under State B: from (9, 11) pressed Down, Right, Right, Down, Right, Right, Right, Down, Down.
  - **Results**: Stepping onto Column 11 Row 12 (11, 12) on 3F immediately triggered a fall through Pit A (The Secret Fall), landing us on 2F (Map 0_214) at (12, 12).
  - **Conclusion**: Row 12 on 3F under State B is passable on Columns 9 and 10, but Column 11 Row 12 (11, 12) is Pit A. This fall is fully passable, dropping us directly to the isolated 2F East South room at (12, 12). We are now positioned at 2F (12, 12).
- **Systematic Exploration Plan (2F East South Landing)**:
  - Since we landed at (12, 12) on 2F East South under State B, we must investigate this isolated pocket.
  - Socratic Question: Does this pocket contain the stairs going down to 1F East Southeast?
  - Socratic Question 2: In unmodded Gen 1, the stairs down from this isolated 2F room are located at (25, 14) on 2F East. Can we navigate to the Southeast room on 2F from this landing pocket (X=12, Y=12)?
  - Let's analyze Column 13 to Column 21 passability on foot under State B. If Column 22 blocks rows 8-15, we must determine if there is a vertical passage.
  - Let's proceed carefully, mapping every tile in 2F East South on foot in 1-tile chunks.