# Pok�mon Mansion - Verified Switch Matrix & Master Route

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

## Chronological Turn-Stamps & Layout Discoveries
- **Turn 54222:** Mansion reset to State A (Default) via overworld exit.
- **Turn 54284:** Mansion reset to State A (Default) via DIG escape to Cinnabar Island.
- **Turn 54332:** Toggled 3F West switch at `(2, 11)` to State B from `(2, 12)` facing UP.
- **Turn 54341:** Dismissed State B dialogue. Row 9 gates open, Row 12 gates closed on 3F West.
- **Turn 54345:** Re-verified Mansion reset to State A (Default). Row 9 gates closed, Row 12 gates open.
- **Turn 54399:** Visually and empirically verified via DFS that on 3F West in State A, the player's movement is strictly confined to a single isolated vertical corridor `[(8, 9), (8, 10), (8, 11), (8, 12), (8, 13)]`. It is completely blocked to the left and right by permanent rubble and column pillars, making horizontal crossing to 3F East physically impossible in State A.

---

## The Definitive Verified Master Route to B1F East & Secret Key
1. **Enter Mansion in State A:**
   - Walk from Cinnabar Island `(11, 12) -> (18, 12) -> (18, 4) -> (6, 4) -> (6, 3)` and step UP to enter 1F West (landing at `(5, 27)`).

2. **Walk to 1F East Stairs and Ascend to 2F East (State A):**
   - On 1F West, walk UP Column 5 to Row 11: `(5, 27) -> (5, 11)`.
   - Walk RIGHT along Row 11 to Column 12: `(5, 11) -> (12, 11)` (bypassing the Scientist at `(13, 11)` who permanently blocks Column 13).
   - Walk UP Column 12 to Row 7: `(12, 11) -> (12, 7)`.
   - Walk RIGHT along Row 7 to Column 18: `(12, 7) -> (18, 7)` (this corridor is completely open).
   - Walk DOWN Column 18 to Row 10: `(18, 7) -> (18, 10)` (stairs). Step DOWN onto the stairs to warp UP to 2F East (landing at `(18, 11)`).

3. **Toggle 2F East Switch to State B:**
   - On 2F East, walk LEFT along Row 11 to the switch at `(12, 11)`: `(18, 11) -> (12, 11)`.
   - Stand at `(12, 11)` facing RIGHT (towards statue at `(13, 11)`) and press A to toggle the switch to State B!

4. **Climb back to 3F East (State B) and Drop to B1F East:**
   - Walk RIGHT to the stairs at `(15, 11)` on 2F East: `(12, 11) -> (15, 11)`.
   - Step UP onto the stairs to warp UP to 3F East!
   - On 3F East (State B), walk to the balcony: `(15, 11) -> (21, 11) -> (21, 15) -> (20, 15) -> (20, 18) -> (19, 18)`.
   - Stand at `(19, 18)` and step DOWN (South) to drop to B1F East (landing at `(19, 16)`).

5. **Retrieve Secret Key on B1F East (State B) and Escape:**
   - Walk UP Column 19/20 to Row 5, and use the open Row 5 gate to walk to northwest room: `(19, 16) -> (21, 16) -> (21, 5) -> (1, 5)`.
   - Stand at `(1, 5)` facing UP and press A to retrieve the **Secret Key** at `(1, 4)`!
   - Open menu, select POK�MON, select TRUFFLE (Paras), and use **DIG** to escape back to Cinnabar Island!
