# Pokémon Mansion (Cinnabar Mansion) Exploration Records (Map Region)

## Core Puzzle Mechanics & Safety Rules
- **Switch Statues**: Throughout the Mansion, there are Mewtwo statues with switches inside them.
  - Interacting with a statue toggles the state of gates (doors with iron bars) throughout the floor or building.
  - Status check: There are two types of gates: **Open Gates** and **Closed Gates**.
  - Statues toggle these states: when one type opens, the other type closes.
- **Floors**:
  - **1F**: Entry floor. Contains stairs to 2F.
  - **2F**: Second floor. Contains stairs to 1F, stairs to 3F, and several balconies/falls.
  - **3F**: Third floor. Contains stairs to 2F, and specific fall-down spots (pits/ledges) that drop the player to lower floors (including B1F!).
  - Under State A (Statue 2 Default):
    - Left side of 3F is accessible from the stairs landing (7, 11). We can bypass the scientist NPC at (4, 11) by walking around his position.
- **B1F**: Basement floor. This is where the **Secret Key** is hidden.
- **Escape Strategy**: Once we find the Secret Key, we can use an **Escape Rope** from our bag to immediately warp out of the Mansion. We currently have 2 Escape Ropes in our bag.

---

## 1F: Ground Floor Exploration State
- **Stairs**:
  - Up to 2F: Located at (5, 10) (Verified Turn 74945)
- **Switches & Gates**:
  - Statue 1: (2, 5) on 1F West | State: State A (Default) (As of Turn 84031)
  - Gate 1: (25, 13) | State: CLOSED under State A (Verified Turn 82243), OPEN under State B.
  - Gate 4: (21, 17) | State: OPEN under State A, CLOSED under State B (Verified Turn 80849).
  - Column 21 Row 13 Passability: CLOSED under State A (Verified Turn 83750 by standing at (21, 12) facing Down and pressing Down, resulting in a bump). The entire Row 13 across Columns 13 to 22 is completely blocked by solid/impassable partition walls (TYPE_2889) under State A, meaning there is no foot crossing to the southern half on 1F East under State A.
- **Global Switch Mechanics**:
  - **Verified Gen 1 Mechanic**: The gate switches in Cinnabar Mansion are **global and persistent**. Toggling a statue on any floor changes the gate configuration (State A vs. State B) for all floors simultaneously. Switches do NOT reset upon floor transitions (such as taking stairs or falling down pits). If a gate is found closed, it is because we previously toggled a statue back to its opposite state (e.g., toggling Statue 2 to State A on Turn 83035 before arriving on 1F East on Turn 83091). We must always align our active route with the single global switch state.
- **Items**:
  - Escape Rope: (14, 3) | State: [x] Collected (Turn 74964)
- **Trainers**:
  - Trainer 1: (TBD, TBD) | State: [ ] Undefeated
- **Wild Encounters**:
  - Wild Ponyta: Caught at (25, 5) | State: [x] Captured (Turn 75405). Named EPONA (Level 28), stored in PC Box 1.
  - Wild Vulpix: Sighted at (24, 3) | State: [ ] Uncaught (Turn 75416, fled using Roar).
- **Eastern Room & Western Corridor**:
  - The large eastern room of 1F is bounded on the left by a solid wall (TYPE_2889) at Column 9.
  - Rubble (TYPE_2889) blocks columns 8 to 11 on Rows 8 and 9.
  - **Northern & Central Open Corridors (Crossings)**: Column 11 and Column 13 are open at the North on Rows 4, 5, 6 (open floor TYPE_3fe2) (Verified Turn 76210), and also horizontally along Row 11 (Verified Turn 83494). This allows players to walk directly between 1F West and 1F East on foot. Furthermore, Column 22 is open on Rows 2, 3 (open floor TYPE_3fe2), allowing players to cross into the eastern-most room (Columns 23-28) on foot (Verified Turn 76221). Thus, 1F East is fully accessible on foot from 1F West under both State A and State B.
  - A passable corridor on Column 12 (open floor TYPE_3fe2) starts at Row 7 and goes South to Row 11, connecting the eastern room to the southern corridor.
  - **Column 24 Passability (Verified Turn 83182)**: Column 24 Row 14 is completely open and passable on foot under State B. This allows us to walk directly into the Southeast room of 1F East from Gate 1.

---

## 2F: Second Floor Exploration State
- **Stairs**:
  - Down to 1F: (5, 10) (Verified Turn 77411)
  - Up to 3F: (7, 10) (Verified Turn 75056)
- **Switches & Gates**:
  - Statue 2: (2, 11) | State: [x] State A (Toggled on Turn 78771)
  - Gate 6: (9, 4)-(9, 5) | State: CLOSED under State A, OPEN under State B (Verified CLOSED on Turn 75868)
  - Gate 3: (18, 8)-(19, 8) | State: CLOSED under State A (Verified CLOSED on Turn 80229), OPEN under State B (Verified OPEN on Turn 79932)
  - Column 11 Row 22 Gate/Corridor: OPEN under both State A and State B (Verified OPEN on Turn 84642 under State B and on Turn 84697 under State A).
  - Columns 12-13 Row 13 Gate: CLOSED under State A (Verified Turn 78855), and CLOSED under State B (Verified Turn 79849 by bumping into (12, 13) from (12, 12)). This gate is 100% closed under both states, meaning 2F East South cannot be accessed via Column 12-13 on Row 13.
  - Columns 12-13 Row 26 Gate: CLOSED under BOTH State A and State B (Verified CLOSED on Turn 80627 under State A by bumping from (12, 25)). This gate is 100% closed under both states, meaning there is no foot access to Row 27.
- **Balcony Drop (DEFINITIVELY DISPROVEN)**:
  - We systematically and exhaustively tested the 2F East South balcony area under the true State A (Default) (Turns 84804-84838) and proved it is completely closed with no active drop:
    - Column 11 Row 16: BUMPED (Turn 84748)
    - Column 12 Row 15: BUMPED (Turn 84737)
    - Column 13 Row 15: BUMPED (Turn 84742)
    - Column 14 (Railing): BUMPED on all Rows 16 to 25 under State A, proving Column 14 is a continuous, solid, impassable wall that completely separates Column 13 from the open atrium on Columns 15-17.
  - Thus, there is NO active balcony drop under State A on 2F East South. B1F cannot be accessed via any 2F balcony drops. We must utilize the State B 3F West balcony drop strategy.
- **Row 10 Crossover**: (9, 10) consists of standard open floor (TYPE_3fe2) and is completely OPEN and passable under State A (Verified Turn 78826).
- **Physical Blockages & Routing Constraints (Empirically Verified)**:
  - **Column 15 Partition Wall**: Column 15 is a solid vertical wall of TYPE_2889 on Rows 1-5 (Verified Turn 76704 by bumping into (15, 2) from (14, 2)). Column 15 is completely OPEN and passable on Row 6 (Verified Turn 76718 by successfully stepping onto (15, 6) from (14, 6)) and visually open on Row 7.
  - **2F West Row 9 Blockage (Verified Turn 81012)**: Row 9 is completely blocked by a solid vertical wall of TYPE_2889 from Column 3 to Column 9 on 2F West, preventing direct vertical traversal between Row 8 and Row 10 on the west side of the floor. All vertical traversal between the northern and southern halves of 2F West must detour through the open Column 10/11/12 corridor.
  - **Northeast Room Obstacles (Rubble Blockage)**: Columns 23 to 27 on Row 6 and Row 7 are completely blocked by impassable solid rubble of TYPE_2889 (Verified Turn 76734). There is no direct access to the lower half on these columns.
  - **Column 22 Blockage**: Bounded by solid rubble (TYPE_2889) on Rows 8-15 under both State A and B, separating Column 21 from Column 23 on these rows (Verified Turn 76533). Row 4 and Row 5 on Column 22 are also solid rubble (Verified Turn 76734). Row 3 on Column 22 is completely open floor of TYPE_3fe2 (Verified Turn 76734).
  - **Row 8 Blockage**: Row 8 is a solid partition wall of TYPE_2889 from Column 22 to 28, blocking vertical crossing from the Northeast room to the Southeast room under both State A and B (Verified Turn 76559). On Turn 83391, we stood at (28, 7) facing Down and pressed Down under State B. Resulted in a direct collision bump against (28, 8), physically proving Column 28 Row 8 is indeed solid and impassable under State B.
  - **Southeast Area Accessibility & Room Isolation**: 
    - The Northeast room of 2F East (Columns 23-28, Rows 2-7) contains no staircases or transitions.
    - Column 22 is completely blocked by solid rubble on Rows 8-15 under both State A and State B. This separates Column 21 (central-east corridor) from Column 23 (the Southeast room) on these rows.
    - Under State A, Gate 3 at (18, 8)-(19, 8) is OPEN and the Row 10 crossover at (9, 10) is OPEN. This allows us to walk on foot from 2F West directly to the central-east corridor on 2F East South (Columns 16-21). However, there is no staircase at (21, 10) as previously misidentified. The tile (21, 10) is a standard open floor tile (TYPE_3fe2).
    - Note: The staircase graphic at (25, 14) inside the Southeast room is the actual staircase on this half of the floor, but it is located in the Southeast room which is isolated under both State A and State B due to the Column 22 blockages and closed gates on 1F. The staircase/doorway inside the Southeast room can only be accessed by climbing to 3F East (or falling from 3F East). Since there is no walkthrough crossover from 3F West to 3F East, let's re-verify how to access B1F or the rest of the mansion.
  - **Northeast Room Staircase Hypothesis (DISPROVEN Turn 83409)**: We systematically and physically walked over every single passable floor tile in the Northeast room of 2F East (Columns 23-28, Rows 1-7) under State B (Turns 83379-83409). None of the tiles triggered a warp or staircase transition. This empirically and definitively disproves the existence of any staircase in the Northeast room.
- **Falls/Pits**:
  - Fall Spot 1: (TBD, TBD) -> Drops to (TBD, TBD) on 1F
- **Items**:
  - Calcium: (28, 7) | State: [x] Collected (Turn 75736)
- **Wild Encounters**:
  - Wild Muk: Caught at (3, 11) | State: [x] Captured (Turn 75484). Named SLUDGY (Level 39), stored in PC Box 1.

---

## 3F: Third Floor Exploration State
- **Stairs**:
  - Down to 2F: Located at (7, 10) (Verified Turn 75056)
- **Switches & Gates**:
  - Statue 3: (10, 8) on 3F West | State: Purely Decorative (No Switch) (Verified Turn 78784). Front tile (10, 9) and surroundings are solid wall/rubble (TYPE_2889).
  - Gate 2 (3F, Row 8 at (8, 8)-(11, 8)): CLOSED and impassable under BOTH State A and State B.
    - State B Proof of Work: Tested on Turn 79283 by standing at (9, 9) facing Up and pressing Up against (9, 8), resulting in a direct collision.
    - State A Proof of Work: Tested on Turn 79330 by standing at (9, 9) facing Up and pressing Up against (9, 8), resulting in a direct collision.
    - Conclusion: The 3F West-East on-foot connection is permanently blocked under both states. 3F East cannot be reached on foot from 3F West.
- **Falls/Pits**:
  - Pit A (The Secret Fall): (11, 12) | State: Static Pit (Verified Turn 75091)
- **Mansion Diaries**:
  - Table with Diary: (6, 12) (Verified Turn 75127). Read text: 'Diary: Feb. 6 MEW gave birth. We named the newborn MEWTWO.'
- **Items**:
  - Max Potion: (1, 16) | State: [x] Collected (Turn 75157)
- **Wild Encounters**:
  - Wild Grimer: Caught at (3, 16) | State: [x] Captured (Turn 75147). Named GLOOP (Level 31), stored in PC Box 1.
  - Wild Magmar: Caught at (9, 10) | State: [x] Captured (Turn 75664). Nicknamed KILN (Level 34), stored in PC Box 1.
- **Left Side of 3F**:
  - Accessible via Row 13: (1, 13), (2, 13), (3, 13), (4, 13), (5, 13). (Verified passable on foot on Turn 76810).
  - **Column 1 Row 9 Blockage**: Empirically proven to be a solid wall of TYPE_2889 on Turn 76873 by attempting to step Up from (1, 10) and colliding.
  - **Northern Half Isolation**: Rows 6 and 7 are entirely blocked by solid wall/rubble of TYPE_2889 across all columns on 3F West, meaning the northern half of 3F West (Rows 1-5) is completely isolated and unreachable on foot from the southern half under both states.
  - **Balcony Ledge Testing**: Systematically testing Row 17 on Columns 1-5 on 3F West to find a balcony jump-down spot.
    - Column 5: Tested on Turn 76905 by pressing Down from (5, 16) and bumped, proving (5, 17) is a solid railing under State B.
    - Column 4: Tested on Turn 76919 by pressing Down from (4, 16) and bumped, proving (4, 17) is a solid railing under State B.
    - Column 3: Tested on Turn 76924 by pressing Down from (3, 16) and bumped, proving (3, 17) is a solid railing under State B.
- **State B (Statue 2 Toggled) Balcony East-Edge Drop Tests**:
    - Column 5 (Row 11): Tested on Turn 84865 -> Stepped Right onto (6, 11) (Normal floor, no drop).
    - Column 5 (Row 12): Tested on Turn 84927 -> Stepped Right onto (6, 12) (Bump against solid table, no drop).
    - Column 5 (Row 13): Tested on Turn 84917 -> Stepped Right onto (6, 13) (Bump against solid table, no drop).
    - Column 5 (Row 14): Tested on Turn 84900 -> Stepped Right onto (6, 14) (Normal floor, no drop).
    - Column 5 (Row 15): Tested on Turn 84896 -> Stepped Right onto (6, 15) (Normal floor, no drop).
    - Column 5 (Row 16): Tested on Turn 80781 by standing at (5, 16) facing Right and pressing Right. Result: **Bump** against (6, 16). Confirmed 100% solid, impassable under State B.
    - Column 6 (Row 15): Tested on Turn 83021 by standing at (6, 15) facing Down and pressing Down. Result: **Bump** against (6, 16). Confirmed 100% solid, impassable under State B.
    - Column 7 (Row 15): Tested on Turn 83026 by standing at (7, 15) facing Down and pressing Down. Result: **Bump** against (7, 16). Confirmed 100% solid, impassable under State B.
    - Column 1 (Row 16): Tested on Turn 83032 by standing at (1, 16) facing Down and pressing Down. Result: **Bump** against (1, 17). Confirmed 100% solid, impassable under State B.
    - Column 2 (Row 16): Tested on Turn 83034 by standing at (2, 16) facing Down and pressing Down. Result: **Bump** against (2, 17). Confirmed 100% solid, impassable under State B.
    - **Conclusion**: There is absolutely no walkthrough or drop-off connection on 3F West under State B either. All tested balcony and crossover directions are completely blocked under both State A and State B.
- **State B Column 10 Row 11 Passability Test (CORRECTED & VERIFIED)**:
    - On Turn 84939, we stood at (9, 11) under the mathematically and visually verified State B (Mewtwo Statue 2 toggled to State B, Gate 6 open on 2F West) and pressed Right to step onto (10, 11). Result: **Bump** against (10, 11), remaining at (9, 11).
    - **Definitive Conclusion**: Column 10 Row 11 is 100% solid, closed, and impassable under the true State B. This confirms that there is absolutely no walkthrough crossover on 3F between the West and East sides of the floor under either state.
- **State A (Statue 2 Default) Balcony East-Edge Drop Tests**:
    - Column 5 (Row 16): Tested on Turn 82976 by standing at (5, 16) facing Right and pressing Right. Result: **Bump** against (6, 16). Confirmed 100% solid, impassable under State A.
    - Column 6 (Row 15): Tested on Turn 82978 by standing at (6, 15) facing Down and pressing Down. Result: **Bump** against (6, 16). Confirmed 100% solid, impassable under State A.
    - Column 7 (Row 15): Tested on Turn 82979 by standing at (7, 15) facing Down and pressing Down. Result: **Bump** against (7, 16). Confirmed 100% solid, impassable under State A.
    - **Conclusion**: There is absolutely no walkthrough or drop-off connection on 3F West under State A (Default). All tested balcony and crossover directions are completely blocked.
- **State A (Default) Column 10 Row 11 Passability Test**:
    - Tested on Turn 82928 by standing at (9, 11) facing Right and pressing Right. Result: **Bump** against (10, 11) (stayed at (9, 11)). Confirmed 100% solid, impassable wall/closed gate under State A. This officially disproves any on-foot crossover under State A.
- **Trainers**:
  - Burglar: Standing at (4, 11). Defeated on Turn 75104. Uses a Level 38 Ninetales. Marked with a ☠️ map marker.

---

## B1F: Basement Floor Exploration State
- **Switches & Gates**:
  - Statue 4: (TBD, TBD) | State: [ ] Default
- **Secret Key**:
  - Coordinates: (TBD, TBD) | State: [ ] Uncollected
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

## 2F East South Column 22 Balcony Passability Plan (Turn 81307) - Completed & Disproven
- **The Hypothesis**: In unmodded Pokémon Red/Blue, the southern balcony on the second floor (2F East South) is a completely continuous and open walkway spanning horizontally across Column 22 on Rows 16 and 17, or Row 26 provides a walkthrough bypass to Row 27 (the southern balcony).
- **The Strategy Results**: This strategy has been **fully executed and 100% disproven**. We have systematically and physically tested Column 22 on Rows 9-15 under both State A and State B, and Row 26 on Column 11 and Column 14 under State A. All resulted in physical collisions (bumps), proving that 2F East South is completely isolated and has no walkable connection or bypass to Row 27 under State A.

## State A Column 22 Balcony Passability Test Logs (Turn 81341)
- **Turn 81341 (Row 15)**: Stood at (21, 15) under State A and pressed Right to attempt to step onto (22, 15) (TYPE_2889). Result: **Bump**, remaining at (21, 15). This physically and empirically proves that Column 22 is CLOSED and solid/impassable on Row 15 under State A.
- **Turn 81347 (Row 14)**: Stood at (21, 14) under State A and pressed Right to attempt to step onto (22, 14) (TYPE_2889). Result: **Bump**, remaining at (21, 14). This physically and empirically proves that Column 22 is CLOSED and solid/impassable on Row 14 under State A.
- **Turn 81358 (Row 13)**: Stood at (21, 13) under State A and pressed Right to attempt to step onto (22, 13) (TYPE_2889). Result: **Bump**, remaining at (21, 13). This physically and empirically proves that Column 22 is CLOSED and solid/impassable on Row 13 under State A.
- **Turns 81365-81371 State A Column 22 passability tests**:
  - Stand at (21, 12) under State A, pressed Right. Result: **Bump** against (22, 12) (Turn 81365).
  - Stand at (21, 11) under State A, pressed Right. Result: **Bump** against (22, 11) (Turn 81367).
  - Stand at (21, 10) under State A, pressed Right. Result: **Bump** against (22, 10) (Turn 81369).
  - Stand at (21, 9) under State A, pressed Right. Result: **Bump** against (22, 9) (Turn 81371).
  - **Conclusion**: Column 22 is completely blocked by solid/impassable rubble across all Rows from 9 to 15 under BOTH State A and State B. This confirms that 2F East South and the isolated 2F Southeast room are 100% separated on foot on this floor.
- **Turn 81471-81472 State A Row 25 Column 14 passability test**:
  - Stand at (13, 25) under State A, pressed Right to attempt to step onto (14, 25) (TYPE_2889).
  - Result: **Bump**, remaining at (13, 25) (Turn 81472).
  - **Conclusion**: Column 14 Row 25 is completely solid/impassable under State A. This disproves the hypothesis that we can bypass Gate 26 on foot by walking east onto Column 14.
- **Turn 81479 State A Row 26 Column 11 passability test**:
  - Stand at (10, 26) under State A, pressed Right to attempt to step onto (11, 26) (TYPE_2889).
  - Result: **Bump**, remaining at (10, 26) (Turn 81479).
  - **Conclusion**: Column 11 Row 26 is completely solid/impassable under State A. This disproves the hypothesis that we can bypass Gate 26 on foot by walking west onto Column 11.
- **Systematic Column 14 and 2F East South Passability Audit (Completed Turn 83895)**:
  - **Turn 83870 Test**: Stood at (13, 22) facing Right and pressed Right under State B. Result: **Bump** against (14, 22) (solid wall of TYPE_2889).
  - **Turn 83892 Verification**: Visually and physically confirmed that Column 13 is blocked north of Row 16 by solid wall/rubble of TYPE_2889 at (13, 15), (12, 15), and (14, 15).
  - **Column 14 Continuity**: Visually verified that Column 14 is a continuous vertical wall of TYPE_2889 on Rows 16-26.
  - **Final Conclusion**: The 2F East South sector (Columns 12-13, Rows 16-25) is a completely closed pocket with absolutely zero on-foot connection to the 2F Southeast room.
- On Turn 85112, we stood at (9, 9) facing Right under State A and pressed Right. Result: Bump against (10, 9), physically proving Column 10 Row 9 is solid and impassable on 3F West under State A.
- On Turn 85119, we stood at (7, 8) facing Up under State A and pressed Up. Result: Bump against (7, 7), physically proving Column 7 Row 7 is solid and impassable on 3F West under State A.
- On Turn 84976, we stood at (18, 7) facing Down under State B and pressed Down. Result: Bump against (18, 8), physically proving Gate 3 at (18, 8)-(19, 8) is CLOSED and impassable under State B.