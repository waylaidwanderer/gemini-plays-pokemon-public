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
  - A passable corridor on Column 12 (open floor TYPE_3fe2) starts at Row 7 and goes South to Row 11, connecting the eastern room to the southern corridor.

---

## 2F: Second Floor Exploration State
- **Stairs**:
  - Down to 1F: (TBD, TBD)
  - Up to 3F: (TBD, TBD)
- **Switches & Gates**:
  - Statue 2: (2, 11) | State: [x] Toggled (Successfully toggled on Turn 75468. Failed attempt on Turn 75336 due to facing Down instead of Left)
- **Falls/Pits**:
  - Fall Spot 1: (TBD, TBD) -> Drops to (TBD, TBD) on 1F
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
- **Left Side of 3F**:
  - Accessible via Row 13: (1, 13), (2, 13), (3, 13), (4, 13), (5, 13).
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