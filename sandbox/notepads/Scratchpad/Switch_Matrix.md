# Pok&eacute;mon Mansion - Verified Switch Matrix & Master Route

## Overview
- Global Mewtwo statue switches toggle electronic shutter gates between DEFAULT (State A) and TOGGLED (State B).
- Floor transitions preserve the active state.
- B1F West SOUTH is permanently separated from B1F West NORTH by a solid brick wall on Row 9.
- 1F East is blocked from going up to 2F East in State B because the gate at `(15, 8)` is closed, and Column 14 is permanently blocked by rubble on Rows 12-16.

---

## Shutter Gate Configurations & Structural Barriers

### Permanent Structural Barriers
- **Column 22 on 2F East:** Solid permanent wall blocking horizontal passage below Row 3 (verified by bumping at (22, 11) on Turn 54878 and (22, 10) on Turn 54882).

### State A (Default)
- **B1F South-East gate at `(10, 11)`:** OPEN (allows crossing between West and East B1F SOUTH on Row 11).
- **3F East gate at `(15, 11)` (stairs):** OPEN (as a DOWN warp to 2F East).
- **1F East gate at `(15, 8)`:** OPEN.
- **B1F North-Central gate at `(9, 5)`:** CLOSED.
- **2F East Row 7 Gates:** OPEN (allows vertical crossing on Column 15).
- **3F West Row 9 Gates:** CLOSED.\n- **3F West Row 11 Column 11:** OPEN (this is the only open passage horizontally across Column 11 in State A!).
- **3F West Row 12 Gates:** OPEN.

### State B (Toggled)
- **B1F South-East gate at `(10, 11)`:** CLOSED.
- **3F East gate at `(15, 11)` (stairs):** OPEN (as an UP warp to 3F East).
- **1F East gate at `(15, 8)`:** CLOSED.
- **B1F North-Central gate at `(9, 5)`:** OPEN (allows horizontal crossing from B1F East NORTH to B1F West NORTH!).
- **2F East Row 7 Gates (Columns 14-17):** CLOSED (blocks vertical crossing on Column 15 on Row 7).
- **3F West Row 9 Gates:** OPEN.
- **3F West Row 12 Gates:** CLOSED.

---

## The Definitive Verified Master Route to B1F East & Secret Key
1. **Enter Mansion in State A:**
   - Walk from Cinnabar Island `(11, 12) -> (18, 12) -> (18, 5) -> (6, 5) -> (6, 4) -> (6, 3)` (bypassing the girl and signpost on Row 6/7) and step UP to enter 1F West (landing at `(5, 27)`).

2. **Navigate 1F West to 2F West (State A):**
   - Walk UP Column 5 to Row 11: `(5, 27) -> (5, 11)`.
   - Walk RIGHT along Row 11 to Column 8: `(5, 11) -> (8, 11)`.
   - Walk UP Column 8 to Row 10: `(8, 11) -> (8, 10)`.
   - Walk LEFT to Column 5: `(8, 10) -> (5, 10)`.
   - Step LEFT onto the stairs at `(5, 10)` to warp UP to 2F West (landing at `(5, 11)`).

3. **Navigate 2F West to 3F West (State A):**
   - Walk RIGHT to Column 7: `(5, 11) -> (7, 11)`.
   - Step UP onto the stairs at `(7, 10)` to warp UP to 3F West (landing at `(7, 11)`).

4. **Toggle 3F West Switch to State B:**
   - Walk RIGHT along Row 11 to Column 12: `(7, 11) -> (12, 11)`.
   - Walk LEFT along Row 11 to Column 3: `(12, 11) -> (3, 11)`.
   - Walk LEFT to Column 3 Row 12: `(3, 11) -> (3, 12)`.
   - Walk LEFT to Column 2 Row 12: `(3, 12) -> (2, 12)`.
   - Stand at `(2, 12)` facing UP and press A to toggle the Mewtwo statue switch at `(2, 11)` to State B!

5. **Walk to Balcony on 3F East (State B) and Drop to B1F East:**
   - Walk back RIGHT and UP to Row 6: `(2, 12) -> (3, 12) -> (3, 11) -> (12, 11) -> (12, 6)`.
   - Walk RIGHT along Row 6 to Column 21: `(12, 6) -> (21, 6)`.
   - Walk DOWN Column 21 to Row 15 (Column 21 is blocked at Row 8, so we must walk down Column 19 past the open Row 8 shutter gate to Row 12, then walk RIGHT to Column 21 Row 12, and then walk DOWN Column 21 past the open Row 13 gap to Row 15): `(21, 6) -> (19, 6) -> (19, 12) -> (21, 12) -> (21, 15)`.
   - Walk LEFT along Row 15 to Column 19: `(21, 15) -> (19, 15)`.
   - Walk DOWN Column 19 to Row 16: `(19, 15) -> (19, 16)`.
   - Walk LEFT along Row 16 to the edge at `(18, 16)`: `(19, 16) -> (18, 16)`.
   - Walk LEFT (West) from `(18, 16)` to drop over the balcony railing to B1F East (landing at `(19, 16)` on B1F East).

6. **Retrieve Secret Key on B1F East (State B) and Escape:**
   - Walk UP Column 19/20 to Row 5, and use the open Row 5 gate to walk to northwest room: `(19, 16) -> (21, 16) -> (21, 5) -> (1, 5)`.
   - Stand at `(1, 5)` facing UP and press A to retrieve the **Secret Key** at `(1, 4)`!
   - Use **DIG** to escape back to Cinnabar Island!
## Chronological Turn-Stamps & State Transitions
- **Turn 54967:** Toggled 3F West Mewtwo statue switch to State B (Mansion was in State A after entry at Turn 54917).
- **Turn 55006:** Verified we were in State A (discovered Row 12 gate at (11, 12) was OPEN, meaning a previous reset or mis-toggle occurred).
- **Turn 55011:** Toggled 3F West switch at (2, 11) to State B from (2, 12) facing UP (Mansion is now confirmed in State B).


## Discovered Spatial Constraints & Structural Barriers
- **Column 22 on 2F East:** Solid permanent wall blocking horizontal passage below Row 3 in both States (verified by bumping at (22, 11) on Turn 54878 and (22, 10) on Turn 54882).
- **Row 13 on 3F East Column 19:** Shutter gate that is CLOSED in State B (verified by bumping on Turn 54982 and Turn 55109).
- **Row 16 on 3F East Columns 18-26:** Completely solid wooden railing across all columns (including 20, 21), making Row 16 impassable from Row 15 in both States (unless a gate is specifically open).
