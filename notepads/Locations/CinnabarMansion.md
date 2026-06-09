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
  - Statue 2: (2, 11) | State: [ ] Default (Toggled back on Turn 75189)
- **Falls/Pits**:
  - Fall Spot 1: (TBD, TBD) -> Drops to (TBD, TBD) on 1F

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
- Standing at (12, 11).
- Visually, the right side of 1F (Columns 12 to 17) has been inspected.
- At Column 16: (16, 10) and (16, 11) is a green pillar (TYPE_2889).
- Row 13 has a solid block of walls/rubble starting at (11, 13) and extending East to (17, 13) (all are TYPE_2889 except (13, 13) which is TYPE_3fe2).
- Let's check (13, 13): it says TYPE_3fe2 (passable) on the overlay but wait, is (13, 13) actually open or is it visually a wall? Let's check if we can walk there or if it's blocked by surrounding walls (12, 13) and (14, 13).
- To the east of Column 17 is off-screen. We can walk up to Row 7 on Column 12 to explore the northern part of this room.
- Let's verify if there is any item or statue in the northeast of 1F (above Row 10, Columns 12-17).