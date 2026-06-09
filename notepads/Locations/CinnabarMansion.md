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
  - Down to 1F: (TBD, TBD)
  - Up to 3F: (TBD, TBD)
- **Switches & Gates**:
  - Statue 2: (2, 11) | State: [x] State B (Toggled on Turn 76662)
  - Gate 6: (9, 4)-(9, 5) | State: CLOSED under State A, OPEN under State B (Verified CLOSED on Turn 75868)
  - Gate 3: (18, 8)-(19, 8) | State: OPEN under State A, CLOSED under State B (Verified OPEN on Turn 75880 and Turn 76143)
- **Physical Blockages & Routing Constraints (Empirically Verified)**:
  - **Column 15 Partition Wall**: Column 15 is a solid vertical wall of TYPE_2889 on Rows 1-5 (Verified Turn 76704 by bumping into (15, 2) from (14, 2)). Column 15 is completely OPEN and passable on Row 6 (Verified Turn 76718 by successfully stepping onto (15, 6) from (14, 6)) and visually open on Row 7.
  - **Northeast Room Obstacles (Rubble Blockage)**: Columns 23 to 27 on Row 6 and Row 7 are completely blocked by impassable solid rubble of TYPE_2889 (Verified Turn 76734). There is no direct access to the lower half on these columns.
  - **Column 22 Blockage**: Bounded by solid rubble (TYPE_2889) on Rows 8-15 under both State A and B, separating Column 21 from Column 23 on these rows (Verified Turn 76533). Row 4 and Row 5 on Column 22 are also solid rubble (Verified Turn 76734). Row 3 on Column 22 is completely open floor of TYPE_3fe2 (Verified Turn 76734).
  - **Row 8 Blockage**: Row 8 is a solid partition wall of TYPE_2889 from Column 22 to 28, blocking vertical crossing from the Northeast room to the Southeast room under both State A and B (Verified Turn 76559).
  - **Southeast Room Isolation**: Due to the Column 22 and Row 8 blockages, the Southeast room (and the stairs at (25, 14)) are hypothesized to be unreachable on foot from 2F East North and 2F West under State A (Verified Row 8 Column 28 is solid under State B, Turn 76760). We must test if Column 25 Row 8 (Gate E) opens under State B to allow foot access.
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
  - Statue 3: (TBD, TBD) | State: [ ] Default
  - Column 11 Gate: Currently CLOSED (solid wall of TYPE_2889 on Column 11 from Row 8 to 15).
  - Gate status on 3F is currently CLOSED, blocking access to the right side of 3F (including the pit chute at (11, 12)).
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
    - Column 5: Tested on Turn 76905 by pressing Down from (5, 16) and bumped, proving (5, 17) is a solid railing.
    - Column 4: Tested on Turn 76919 by pressing Down from (4, 16) and bumped, proving (4, 17) is a solid railing.
    - Column 3: Tested on Turn 76924 by pressing Down from (3, 16) and bumped, proving (3, 17) is a solid railing.
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
  - Under State B (Statue 2 Toggled):
    - Gate 1 at (25, 13) is OPEN and passable (Verified Turn 75550).
    - Gate 4 at (21, 17) is CLOSED (Verified Turn 75551).
    - Gate 5 at (26, 27) / (27, 27) is CLOSED (Verified Turn 75568).
    - The south-east pocket (Columns 25-28, Rows 18-26) is explored and verified empty. Column 24 acts as a solid vertical partition wall from Row 19 to Row 27.
    - Crossing left/west into the south-west pocket is possible along Rows 14, 15, and 16.
- Column 2: Tested on Turn 76931 by pressing Down from (2, 16) and bumped, proving (2, 17) is a solid railing.
- Column 1: Tested on Turn 76933 by pressing Down from (1, 16) and bumped, proving (1, 17) is a solid railing.
- SW Balcony Ledge Exploration Complete: All five columns (1 to 5) on Row 17 of 3F West have been systematically tested and are confirmed 100% solid, impassable railings under State B. There is no jump-down ledge or balcony exit in this southwest quadrant.
- Northeast Room Gate Audit (Turn 76971): Systematically verified on foot that Row 8 (Columns 24 to 28) consists of solid closed gates of TYPE_2889 under State B. There is no open gate or passage in this section, meaning the 2F Southeast room is completely isolated and unreachable on foot from 2F East North under State B. Combined with prior testing, the Southeast room (Columns 23-28, Rows 9-15) is 100% isolated on foot on 2F under BOTH State A and State B.
- Hypothesis Verification: Since the Southeast room is completely isolated on foot on 2F, the staircase at (25, 14) can ONLY be accessed by dropping down from 3F East.
- Critical Path to B1F: To reach B1F, we must locate and use the secret pit/fall on 3F. We know Pit A is at (11, 12) on 3F, but it is blocked by Gate 2 (Col 11) being CLOSED. We must investigate how to open Gate 2 on 3F. Let's find any remaining un-toggled statues or paths. We must return to 2F West to toggle Statue 2 back to State A to see if Gate 2 on 3F opens under State A, or search 1F for Statue 1!