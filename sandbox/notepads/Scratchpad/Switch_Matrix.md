# Pokémon Mansion - Verified Switch Matrix & Master Route

## Overview
- Global Mewtwo statue switches toggle electronic shutter gates between DEFAULT (State A) and TOGGLED (State B).
- Floor transitions preserve the active state.
- B1F West SOUTH is permanently separated from B1F West NORTH by a solid brick wall on Row 9.
- 1F East is blocked from going up to 2F East in State A because the gate at `(15, 8)` is closed.

---

## Shutter Gate Configurations

### State A (Default)
- **B1F South-East gate at `(10, 11)`:** OPEN (allows crossing between West and East B1F SOUTH on Row 11).
- **3F East gate at `(15, 11)` (stairs):** CLOSED.
- **1F East gate at `(15, 8)`:** CLOSED.
- **B1F North-Central gate at `(9, 5)`:** CLOSED.
- **3F Balcony Gate at `(20, 17)`:** CLOSED.

### State B (Toggled)
- **B1F South-East gate at `(10, 11)`:** CLOSED.
- **3F East gate at `(15, 11)` (stairs):** OPEN.
- **B1F North-Central gate at `(9, 5)`:** OPEN (allows horizontal crossing from B1F East NORTH to B1F West NORTH!).
- **3F Balcony Gate at `(20, 17)`:** OPEN.

---

## The Ultimate Verified Master Route to B1F East & Secret Key
1. **Prepare Mansion in State B:**
   - From 1F West (State A), go UP the stairs to 2F West.
   - On 2F West, walk Left to `(2, 11)` and standing at `(2, 12)` face UP to toggle the switch to State B.
2. **Cross to 2F East and warp UP to 3F East:**
   - Since we are in State B, the horizontal passage at Row 6 on 2F is OPEN.
   - Walk from `(2, 11)` -> `(12, 11)` -> `(12, 6)` -> `(15, 6)`.
   - Wait, Row 7 gate is CLOSED on 2F East, so we cannot go Down to the stairs from Row 6 in State B.
   - Instead, walk back to 2F West, go down to 1F West.
   - On 1F West (State B), walk through the open gate at `(15, 8)` to 1F East, and go UP the stairs to 2F East.
   - On 2F East (State B), we land on the south side of the gate, so walk directly to the stairs at `(15, 11)` and warp UP to 3F East (landing at `(16, 11)`).
3. **Ascend to 3F East via alternate stairs in State A:**
   - Go UP from 1F East alternate stairs at `(18, 10)` in State A, landing at `(22, 7)` on 2F East.
   - Walk LEFT along Row 7 to `(19, 7)` and go DOWN to `(19, 8)` to enter the stairs (which are open in State A).
   - Warp UP to 3F East (landing on the West-Central side of 3F East).
   - From 3F East, walk to the balcony drop-off at `(19, 16)` and step LEFT to drop.
   - Land on B1F East South at `(19, 16)` in State A.
4. **Retrieve Secret Key on B1F:**
   - On B1F East (State A), walk to the B1F East switch at `(12, 20)` and toggle it to State B.
   - Now the mansion is in State B, and the B1F North-Central gate at `(9, 5)` is OPEN.
   - Walk: `(12, 20) -> (19, 20) -> (19, 5) -> (10, 5) -> (1, 5)`.
   - Retrieve the **Secret Key** at `(1, 4)`!
5. **Escape:**
   - Use DIG to escape back to Cinnabar Island!