# Pokémon Mansion - Verified Switch Matrix & Master Route

## Overview
- Global Mewtwo statue switches toggle electronic shutter gates between DEFAULT (State A) and TOGGLED (State B).
- Floor transitions preserve the active state.
- B1F West SOUTH is permanently separated from B1F West NORTH by a solid brick wall on Row 9.
- 1F East is blocked from going up to 2F East in State A because the gate at `(15, 8)` is closed.

---

## Shutter Gate Configurations & Structural Barriers

### Permanent Structural Walls
- **Column 13 Wall (2F):** A solid permanent wall on Rows 7-12, completely blocking horizontal crossing. (Open on Rows 4-6).
- **Column 22 Wall (2F):** A solid permanent wall on Rows 4-12, completely dividing 2F East into East-Central and West-Central sections. (Open only on Row 3).

### State A (Default)
- **B1F South-East gate at `(10, 11)`:** OPEN (allows crossing between West and East B1F SOUTH on Row 11).
- **3F East gate at `(15, 11)` (stairs):** CLOSED.
- **1F East gate at `(15, 8)`:** CLOSED.
- **B1F North-Central gate at `(9, 5)`:** CLOSED.
- **3F Balcony Gate at `(20, 17)`:** CLOSED.
- **2F East Row 7 Gates:** OPEN (allows vertical crossing on Column 15).

### State B (Toggled)
- **B1F South-East gate at `(10, 11)`:** CLOSED.
- **3F East gate at `(15, 11)` (stairs):** OPEN.
- **B1F North-Central gate at `(9, 5)`:** OPEN (allows horizontal crossing from B1F East NORTH to B1F West NORTH!).
- **3F Balcony Gate at `(20, 17)`:** OPEN.
- **2F East Row 7 Gates (Columns 14-17):** CLOSED (blocks vertical crossing on Column 15 on Row 7).

---

## The Definitive Verified Master Route to B1F East & Secret Key
1. **Prepare Mansion in State B (Verified Turn 53772):**
   - From 1F West (State A), go UP the stairs at `(7, 10)` to 2F West.
   - On 2F West, walk Left to `(2, 11)` and standing at `(2, 12)` face UP to toggle the switch to State B.
2. **Return to 1F West and cross to 1F East (Verified Turn 53772):**
   - Go back to 2F West stairs at `(7, 10)` and go DOWN to 1F West.
   - On 1F West (State B), walk `(7, 11) -> (12, 11) -> (12, 3) -> (26, 3) -> (26, 11) -> (18, 11) -> (18, 10)` to reach the East stairs at `(18, 10)`. (We bypass Column 22 wall by crossing on Row 3!).
3. **Climb to 2F East and warp UP to 3F East (Verified Turn 53772):**
   - Go UP the stairs at `(18, 10)` on 1F East, warping UP to 2F East West-Central side at `(20, 16)`.
   - On 2F East (State B), walk `(20, 16) -> (15, 16) -> (15, 11)` and go UP the stairs to 3F East (landing at `(16, 11)`). (This avoids the closed Row 7 gate and Column 22 wall entirely!).
4. **Drop through Pitfall to 1F Fenced Room (Verified Turn 53783):**
   - On 3F East (State B) (landing at `(16, 11)`), walk to the pitfall at `(26, 6)`: `(16, 11) -> (10, 11) -> (10, 3) -> (26, 3) -> (26, 6)`.
   - Stand at `(26, 6)` and step LEFT to fall through the pitfall, landing on 1F inside the fenced room at `(25, 6)`.
5. **Warp to B1F East and Retrieve Secret Key (Verified Turn 53783):**
   - On 1F, walk UP 5 times onto the stairs to warp down to B1F East, landing at `(25, 5)`.
   - On B1F East (State B), bypass the Column 22 vertical wall by walking UP to Row 3: `(25, 5) -> (26, 5) -> (26, 3)`.
   - Walk LEFT along Row 3 to Column 21: `(26, 3) -> (21, 3)`.
   - Walk DOWN Column 21 to Row 5: `(21, 3) -> (21, 5)`.
   - Walk LEFT along Row 5 to the northwest room: `(21, 5) -> (1, 5)` (Koga's gate at `(9, 5)` is open in State B!).
   - Stand at `(1, 5)` facing UP and press A to retrieve the **Secret Key** at `(1, 4)`!
6. **Escape:**
   - Open the menu, select POKéMON, select TRUFFLE (Paras), and use **DIG** to escape back to Cinnabar Island!
