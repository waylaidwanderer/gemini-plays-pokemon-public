# Pokémon Mansion - Verified Switch Matrix & Master Route

## Overview
- Global Mewtwo statue switches toggle electronic shutter gates between DEFAULT (State A) and TOGGLED (State B).
- Floor transitions preserve the active state.
- B1F West SOUTH is permanently separated from B1F West NORTH by a solid brick wall on Row 9.
- 1F East is blocked from going up to 2F East in State B because the gate at `(15, 8)` is closed, and Column 14 is permanently blocked by rubble on Rows 12-16.

---

## Shutter Gate Configurations & Structural Barriers

### Permanent Structural Walls
- **Column 13 Wall (2F):** A solid permanent wall on Rows 7-12, completely blocking horizontal crossing. (Open on Rows 4-6).
- **Column 22 Wall (2F):** A solid permanent wall on Rows 4-12, completely dividing 2F East into East-Central and West-Central sections. (Open only on Row 3).

### State A (Default)
- **B1F South-East gate at `(10, 11)`:** OPEN (allows crossing between West and East B1F SOUTH on Row 11).
- **3F East gate at `(15, 11)` (stairs):** OPEN (as a DOWN warp to 2F East).
- **1F East gate at `(15, 8)`:** OPEN.
- **B1F North-Central gate at `(9, 5)`:** CLOSED.
- **3F Balcony Gate at `(20, 17)`:** CLOSED.
- **2F East Row 7 Gates:** OPEN (allows vertical crossing on Column 15).
- **3F West Row 9 Gates:** CLOSED.
- **3F West Row 12 Gates:** OPEN.

### State B (Toggled)
- **B1F South-East gate at `(10, 11)`:** CLOSED.
- **3F East gate at `(15, 11)` (stairs):** OPEN (as an UP warp to 3F East).
- **1F East gate at `(15, 8)`:** CLOSED.
- **B1F North-Central gate at `(9, 5)`:** OPEN (allows horizontal crossing from B1F East NORTH to B1F West NORTH!).
- **3F Balcony Gate at `(20, 17)`:** OPEN.
- **2F East Row 7 Gates (Columns 14-17):** CLOSED (blocks vertical crossing on Column 15 on Row 7).
- **3F West Row 9 Gates:** OPEN.
- **3F West Row 12 Gates:** CLOSED.

---

## Chronological Turn-Stamps of Global Switches
- **Turn 54222:** Mansion reset to State A (Default) via overworld exit.
- **Turn 54284:** Mansion reset to State A (Default) via DIG escape to Cinnabar Island.
- **Turn 54332:** Toggled 3F West switch at `(2, 11)` to State B from `(2, 12)` facing UP.
- **Turn 54341:** Dismissed State B dialogue. Row 9 gates open, Row 12 gates closed on 3F West.
- **Turn 54345:** Re-verified Mansion reset to State A (Default). Row 9 gates closed, Row 12 gates open.

---

## The Definitive Verified Master Route to B1F East & Secret Key
1. **Enter Mansion in State A:**
   - Walk from Cinnabar Island `(11, 12) -> (18, 12) -> (18, 4) -> (6, 4) -> (6, 3)` and step UP to enter 1F West (landing at `(5, 27)`).

2. **Ascend to 3F West (State A):**
   - Walk UP Column 5 on 1F West: `(5, 27) -> (5, 10)` (stairs). Step UP to warp to 2F West (landing at `(5, 11)`).
   - Walk RIGHT to Column 7 on 2F West: `(5, 11) -> (7, 11)`. Step UP to warp to 3F West (landing at `(7, 11)`).

3. **Cross 3F West to 3F East (State A):**
   - Walk DOWN to `(7, 12)` (open in State A).
   - Walk RIGHT along Row 12 to Column 11: `(7, 12) -> (11, 12)`.
   - Walk UP Column 11 to Row 6: `(11, 12) -> (11, 6)` (bypassing all walls/plants).
   - Walk RIGHT along Row 6 to Column 19 on 3F East: `(11, 6) -> (19, 6)`.
   - Walk DOWN Column 19 to Row 11: `(19, 6) -> (19, 11)`.
   - Walk LEFT along Row 11 to the stairs at `(15, 11)`: `(19, 11) -> (15, 11)`.
   - Step onto `(15, 11)` to warp DOWN to 2F East (landing at `(16, 11)`).

4. **Toggle 2F East Switch to State B:**
   - On 2F East, walk LEFT to the switch at `(12, 11)`: `(16, 11) -> (12, 11)`.
   - Stand at `(12, 11)` facing RIGHT (towards statue at `(13, 11)`) and press A to toggle the switch to State B!

5. **Climb back to 3F East (State B) and Drop to B1F East:**
   - Walk back to `(15, 11)` on 2F East and step UP onto the stairs to warp UP to 3F East!
   - On 3F East (State B), walk to the balcony: `(15, 11) -> (21, 11) -> (21, 15) -> (20, 15) -> (20, 18) -> (19, 18)`.
   - Stand at `(19, 18)` and step DOWN (South) to drop to B1F East (landing at `(19, 16)`).

6. **Retrieve Secret Key on B1F East (State B) and Escape:**
   - Walk UP Column 19/20 to Row 5, and use the open Row 5 gate to walk to northwest room: `(19, 16) -> (21, 16) -> (21, 5) -> (1, 5)`.
   - Stand at `(1, 5)` facing UP and press A to retrieve the **Secret Key** at `(1, 4)`!
   - Open menu, select POKÉMON, select TRUFFLE (Paras), and use **DIG** to escape back to Cinnabar Island!
