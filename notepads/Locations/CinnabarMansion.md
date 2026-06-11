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
  - Under State B (Statue 2 Toggled):
    - Gate 2 on 3F Column 11 is CLOSED (Verified Turn 75612).
    - Left side of 3F is accessible from the stairs landing (7, 11). We can bypass the scientist NPC at (4, 11) by walking around his position.
- **B1F**: Basement floor. This is where the **Secret Key** is hidden.
- **Escape Strategy**: Once we find the Secret Key, we can use an **Escape Rope** from our bag to immediately warp out of the Mansion. We currently have 2 Escape Ropes in our bag.

---

## 1F: Ground Floor Exploration State
- **Stairs**:
  - Up to 2F: Located at (5, 10) (Verified Turn 74945)
- **Switches & Gates**:
  - Statue 1: (TBD, TBD) | State: [ ] Default
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
  - **Northern Open Corridors (Crossings)**: Column 11 and Column 13 are open at the North on Rows 4, 5, 6 (open floor TYPE_3fe2), allowing players to walk directly between 1F West and 1F East on foot (Verified Turn 76210). Furthermore, Column 22 is open on Rows 2, 3 (open floor TYPE_3fe2), allowing player to cross into the eastern-most room (Columns 23-28) on foot (Verified Turn 76221). Thus, 1F East is fully accessible on foot from 1F West under both State A and State B.
  - A passable corridor on Column 12 (open floor TYPE_3fe2) starts at Row 7 and goes South to Row 11, connecting the eastern room to the southern corridor.

---

## 2F: Second Floor Exploration State
- **Stairs**:
  - Down to 1F: (5, 10) (Verified Turn 77411)
  - Up to 3F: (7, 10) (Verified Turn 75056)
- **Switches & Gates**:
  - Statue 2: (2, 11) | State: [x] State A (Toggled on Turn 78771)
  - Gate 6: (9, 4)-(9, 5) | State: CLOSED under State A, OPEN under State B (Verified CLOSED on Turn 75868)
  - Gate 3: (18, 8)-(19, 8) | State: CLOSED under State A (Verified CLOSED on Turn 80229), OPEN under State B (Verified OPEN on Turn 79932)
  - Column 11 Row 22 Gate/Corridor: OPEN under State B, CLOSED under State A.
  - Columns 12-13 Row 13 Gate: CLOSED under State A (Verified Turn 78855), and CLOSED under State B (Verified Turn 79849 by bumping into (12, 13) from (12, 12)). This gate is 100% closed under both states, meaning 2F East South cannot be accessed via Column 12-13 on Row 13.
  - Columns 12-13 Row 26 Gate: CLOSED under BOTH State A and State B (Verified CLOSED on Turn 80627 under State A by bumping from (12, 25)). This gate is 100% closed under both states, meaning there is no foot access to Row 27.
- **Balcony Drop**:
  - Location: (12, 27)-(13, 27) on 2F East South (Hypothesized to drop to 1F East south-central pocket. Untested as of Turn 78871).
- **Row 10 Crossover**: (9, 10) consists of standard open floor (TYPE_3fe2) and is completely OPEN and passable under State A (Verified Turn 78826).
- **Physical Blockages & Routing Constraints (Empirically Verified)**:
  - **Column 15 Partition Wall**: Column 15 is a solid vertical wall of TYPE_2889 on Rows 1-5 (Verified Turn 76704 by bumping into (15, 2) from (14, 2)). Column 15 is completely OPEN and passable on Row 6 (Verified Turn 76718 by successfully stepping onto (15, 6) from (14, 6)) and visually open on Row 7.
  - **2F West Row 9 Blockage (Verified Turn 81012)**: Row 9 is completely blocked by a solid vertical wall of TYPE_2889 from Column 3 to Column 9 on 2F West, preventing direct vertical traversal between Row 8 and Row 10 on the west side of the floor. All vertical traversal between the northern and southern halves of 2F West must detour through the open Column 10/11/12 corridor.
  - **Northeast Room Obstacles (Rubble Blockage)**: Columns 23 to 27 on Row 6 and Row 7 are completely blocked by impassable solid rubble of TYPE_2889 (Verified Turn 76734). There is no direct access to the lower half on these columns.
  - **Column 22 Blockage**: Bounded by solid rubble (TYPE_2889) on Rows 8-15 under both State A and B, separating Column 21 from Column 23 on these rows (Verified Turn 76533). Row 4 and Row 5 on Column 22 are also solid rubble (Verified Turn 76734). Row 3 on Column 22 is completely open floor of TYPE_3fe2 (Verified Turn 76734).
  - **Row 8 Blockage**: Row 8 is a solid partition wall of TYPE_2889 from Column 22 to 28, blocking vertical crossing from the Northeast room to the Southeast room under both State A and B (Verified Turn 76559).
  - **Southeast Room Isolation**: Due to the Column 22 and Row 8 blockages, the Southeast room is permanently isolated and unreachable on foot from 2F East North and 2F West under BOTH State A and State B. On Turn 77674-77680, we physically foot-tested (25, 14) on 1F East on foot under State B. Standing directly on the tile confirmed it is a normal floor tile (TYPE_3fe2) with no warp or stairs in this ROM. This empirically disproves the bidirectional warp hypothesis and confirms that the 2F Southeast room (and its down stairs) is indeed 100% isolated on foot on both floors. Therefore, the southeast stairs can ONLY be reached by dropping down from a pit on 3F East.
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
  - Statue 3: (10, 9) on 3F West | State: Purely Decorative (No Switch) (Verified Turn 78784)
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
    - Column 2: Tested on Turn 76931 by pressing Down from (2, 16) and bumped, proving (2, 17) is a solid railing under State B.
    - Column 1: Tested on Turn 76933 by pressing Down from (1, 16) and bumped, proving (1, 17) is a solid railing under State B.
- **State A (Statue 2 Default) SW Balcony Ledge Testing**:
    - Column 5: Tested on Turn 77948 by pressing Down from (5, 16) facing Down. Result: **Bump** against (5, 17). Confirmed 100% solid, impassable railing.
    - Column 4: Tested on Turn 77946 by pressing Down from (4, 16) facing Down. Result: **Bump** against (4, 17). Confirmed 100% solid, impassable railing.
    - Column 3: Tested on Turn 77953 by pressing Down from (3, 16) facing Down. Result: **Bump** against (3, 17). Confirmed 100% solid, impassable railing.
    - Column 2: Tested on Turn 77960 by pressing Down from (2, 16) facing Down. Result: **Bump** against (2, 17). Confirmed 100% solid, impassable railing.
    - Column 1: Tested on Turn 77964 by pressing Down from (1, 16) facing Down. Result: **Bump** against (1, 17). Confirmed 100% solid, impassable railing.
- **Trainers**:
  - Burglar: Standing at (4, 11). Defeated on Turn 75104. Uses a Level 38 Ninetales. Marked with a ☠️ map marker.

---

## B1F: Basement Floor Exploration State
- **Switches & Gates**:
  - Statue 4: (TBD, TBD) | State: [ ] Default
- **Secret Key**:
  - Coordinates: (TBD, TBD) | State: [ ] Uncollected
## 1F: Ground Floor Eastern Room Audit (Turns 75245-75258)
- To the east of Column 17, the rest of the room has been explored up to Column 28.
- Physical layout:
  - Row 13 has a solid block of walls/rubble starting at (11, 13) and extending East to (22, 13) (all are TYPE_2889).
  - An electronic gate panel is located on Row 13 at (24, 13) and (25, 13) (TYPE_a83b).
  - Columns 26, 27, 28 are bounded by solid walls and rubble (26, 13 is solid, 27, 10-11 and 28, 8-11 are rubble).
  - A large wooden table occupies (24, 8)-(25, 9) (TYPE_2889), surrounded by passable floor of TYPE_3fe2.
  - The electronic gate at (25, 13) was tested on Turn 75301 and found to be CLOSED and impassable. This blocks access to the southern section of the eastern room on 1F (Rows 14-16, Columns 22-27).
  - **State A Row 13 Passability Verification (Turns 79215-79227)**:
    - Column 23 Row 12 (stone pillar/statue TYPE_2889): Verified 100% solid on Turn 79215 by attempting to walk Down from (23, 11) and bumping. This blocks Column 23 vertical traversal before reaching Row 13.
    - Column 24 Row 13 (Gate 1 TYPE_a83b): Verified CLOSED on Turn 79220 by attempting to walk Down from (24, 12) and bumping.
    - Column 25 Row 13 (Gate 1 TYPE_a83b): Verified CLOSED on Turn 79227 by attempting to walk Down from (25, 12) and bumping.
    - This conclusively proves Row 13 is 100% closed on foot under State A, isolating the 1F East south-central pocket.
  - Under State B (Statue 2 Toggled):
    - Gate 1 at (25, 13) is OPEN and passable (Verified Turn 75550).
    - Gate 4 at (21, 17) is CLOSED (Verified Turn 75551).
    - Gate 5 at (26, 27) / (27, 27) is CLOSED (Verified Turn 75568).
    - The south-east pocket (Columns 25-28, Rows 18-26) is explored and verified empty. Column 24 acts as a solid vertical partition wall from Row 19 to Row 27.
    - Crossing left/west into the south-west pocket is possible along Rows 14, 15, and 16.
- Column 11 on 1F consists of solid vertical wall (TYPE_2889) on Rows 13-27, but on Row 11, Column 11 is completely open, passable floor (TYPE_3fe2). This provides an open horizontal crossover between 1F West (Column 10) and 1F East (Column 12) on Row 11 on foot under both states (Verified Turn 77099).
- Column 2: Tested on Turn 76931 by pressing Down from (2, 16) and bumped, proving (2, 17) is a solid railing.
- Column 1: Tested on Turn 76933 by pressing Down from (1, 16) and bumped, proving (1, 17) is a solid railing.
- SW Balcony Ledge Exploration Complete: All five columns (1 to 5) on Row 17 of 3F West have been systematically tested and are confirmed 100% solid, impassable railings under State B. There is no jump-down ledge or balcony exit in this southwest quadrant.
- Northeast Room Gate Audit (Turn 76971 & 80197): Systematically verified on foot that Row 8 (Columns 24 to 28) consists of solid closed gates of TYPE_2889 under BOTH State A and State B. There is no open gate or passage in this section, meaning the 2F Southeast room is completely isolated and unreachable on foot on 2F under both states. Combined with prior testing, the Southeast room (Columns 23-28, Rows 9-15) is 100% isolated on foot on 2F under BOTH State A and State B.
- Hypothesis Verification: Since the Southeast room is completely isolated on foot on 2F, the staircase at (25, 14) can ONLY be accessed by dropping down from 3F East. Our previous "State A Walkthrough Breakthrough" hypothesis is formally disproven. Row 8 gates are closed in both states.

## Disproven 2F East walkthrough (State A vs State B)
Our testing has systematically verified that:
1. Under State A: Gate 3 is CLOSED and impassable across BOTH tiles (18, 8) and (19, 8). (Verified by bump on Turn 80229).
2. Under State B: Gate 3 is OPEN and passable. (Verified Turn 79932).
3. Under both states, the Southeast room (Columns 23-28, Rows 9-15) on 2F is 100% isolated and cannot be reached on foot.
Therefore, the only walkthrough connection to 3F East is on 3F West: under State B, Gate 2 on 3F (Column 11 Row 12) is OPEN, and the Row 11 path from Column 9 to Column 12 is completely unblocked on foot when the Scientist NPC is not blocking it. This allows direct walkthrough from 3F West to 3F East to reach the B1F pit fall.
- Critical Path to B1F: To reach B1F, we must locate and use the secret pit/fall on 3F. We know Pit A is at (11, 12) on 3F, but it is blocked by Gate 2 (Col 11) being CLOSED. We must investigate how to open Gate 2 on 3F. Let's find any remaining un-toggled statues or paths.
- 3F West Column 10/11 Empirical Verification under State B (Turn 77004): 
  - Stand at (9, 11) facing Right, and press Right. Result: Collided with (10, 11) (visited 0 tiles, stayed at (9, 11)), proving (10, 11) is indeed a solid rock wall/rubble of TYPE_2889.
  - Since (10, 11), (10, 12), and (9, 12) are all solid rubble (TYPE_2889), we cannot physically reach Column 11 on foot from the West. 
  - This definitively proves that there is no walkable connection between 3F West and 3F East under State B.
  - Therefore, we must return to 1F and explore the 1F East wing under State B (since Gate 1 at (25, 13) is open under State B!).
- 3F West Column 10/11 Empirical Verification under State A (Turns 77043-77051):
  - Turn 77043: Standing at (9, 11) under State A, attempted to walk Right into (10, 11). Result: Collided, proving (10, 11) is solid rubble of TYPE_2889 under State A.
  - Turn 77051: Standing at (9, 12) under State A, attempted to walk Right into (10, 12). Result: Collided, proving (10, 12) is solid rubble of TYPE_2889 under State A.
  - This empirically proves that 3F West is completely blocked from 3F East at Columns 9/10 on Rows 11 and 12 under BOTH State A and State B.
- **Row 2 Crossing Verification (Turn 77237)**: Under State B, Row 2 is fully passable on foot across Column 9. Coordinates: (10, 2), (9, 2), (8, 2), (7, 2), (6, 2) are all TYPE_3fe2. Column 9 Row 3 at (9, 3) is a solid, impassable wall (TYPE_2889).
- **Route to Stairs to 2F at (5, 10)**: From (10, 6) in 1F West, we can walk:
  1. Up 4 steps to (10, 2).
  2. Left 5 steps to (5, 2).
  3. Walk Down Column 10 to Row 11: From (5, 2), walk Right 5 steps to (10, 2), then walk Down 9 steps to (10, 11).
  4. From (10, 11), walk Left 5 steps to (5, 11).
  5. Step Up 1 step to (5, 10) to enter the stairs.
This is because Row 9 Column 5 is a solid, impassable wall of TYPE_2889, blocking direct vertical passage down Column 5 (Verified Turn 77387).

## 1F South-Central Pocket Isolation Proof of Work
We have mathematically and physically verified that the 1F south-central pocket (Columns 21-23, Rows 18-27) is permanently isolated and unreachable on foot from the rest of 1F under BOTH Gate States:
1. Under State B: Gate 4 at (21, 17) is CLOSED, blocking southern vertical entry into Columns 21-23.
2. Under State A: Row 13 Column 21 is a solid wall of TYPE_2889, blocking vertical descent along Column 21.
3. In both States: Column 22 is solid rubble on Rows 8-15, completely blocking horizontal entry from the East.
Therefore, ground-level entry is impossible, proving the 1F south-central pocket can only be accessed via the 3F balcony drop.
- **Mewtwo Switch Interaction Rule (Verified Turn 81523)**:
  - Mewtwo switch statues can ONLY be interacted with from the front (facing Up from the southern tile, e.g., (2, 12)).
  - Standing at (3, 11) facing Left and pressing 'A' does NOT trigger the switch, proving that side interactions are disabled.

## 1F Southeast Room Systematic Passability Audit (Turns 81703-81732)
- **Objective**: Systematically and physically test every walkable tile on 1F East Southeast room under State B on foot to find any staircase warp.
- **Verified Facts (Turns 81703-81732)**:
  - We stood directly on and tested the following coordinates on foot under State B:
    - Row 12: (24, 12), (25, 12), (26, 12), (27, 12), (28, 12). Result: No warp.
    - Row 13: (24, 13) (Gate 1). Result: No warp.
    - Row 14: (22, 14), (23, 14), (24, 14), (25, 14), (26, 14), (27, 14). Result: No warp.
    - Row 15: (22, 15). Result: No warp.
    - Row 16: (22, 16), (28, 16). Result: No warp.
    - Row 21: (25, 21), (26, 21), (27, 21), (28, 21). Result: No warp.
    - Rows 22-24: (28, 22), (28, 23), (28, 24). Result: No warp.
    - Row 25: (26, 25), (27, 25), (28, 25). Result: No warp.
  - **Conclusion**: None of these walkable tiles trigger any map warp under State B. This physically disproves the existence of any active staircase warp in the 1F East Southeast room under State B, confirming that the 2F Southeast room is completely isolated on foot on both floors under State B.