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
- **3F West Pitfall Trap at (5, 9):** Permanent structural hazard that warps/drops the player down to 2F West at (5, 10) (verified on Turn 55204). Avoid walking UP to Row 9 Column 5 on 3F West in both State A and State B!
- **3F West Row 9 Wall (Columns 6-7):** Permanent solid vertical wall separating the southern hallway from northern rooms, blocking vertical traversal on these columns (verified on Turn 55219).

### State A (Default)
- **1F West Row 9 Gates:** CLOSED.
- **2F West Row 9 Gates:** CLOSED.
- **B1F South-East gate at `(10, 11)`:** OPEN (allows crossing between West and East B1F SOUTH on Row 11).
- **3F East gate at `(15, 11)` (stairs):** OPEN (as a DOWN warp to 2F East).
- **1F East gate at `(15, 8)`:** OPEN.
- **B1F North-Central gate at `(9, 5)`:** CLOSED.
- **2F East Row 7 Gates:** OPEN (allows vertical crossing on Column 15).
- **3F West Row 9 Gates:** CLOSED.\n- **3F West Row 11 Column 11:** OPEN (this is the only open passage horizontally across Column 11 in State A!).
- **3F West Row 12 Gates:** OPEN.

### State B (Toggled)
- **1F West Row 9 Gates:** CLOSED.
- **2F West Row 9 Gates:** OPEN.
- **B1F South-East gate at `(10, 11)`:** CLOSED.
- **3F East gate at `(15, 11)` (stairs):** OPEN (as an UP warp to 3F East).
- **1F East gate at `(15, 8)`:** CLOSED.
- **B1F North-Central gate at `(9, 5)`:** OPEN (allows horizontal crossing from B1F East NORTH to B1F West NORTH!).
- **2F East Row 7 Gates (Columns 14-17):** CLOSED (blocks vertical crossing on Column 15 on Row 7). We have empirically verified on foot that Columns 15 and 16 are CLOSED on Row 7 of 2F East in State B (Turns 55256, 55259).
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
   - Step LEFT onto the stairs at `(5, 10)` to warp UP to 2F West (landing at `(4, 11)`).

3. **Navigate 2F West to 3F West (State A):**
   - Walk RIGHT to Column 7: `(5, 11) -> (7, 11)`.
   - Step UP onto the stairs at `(7, 10)` to warp UP to 3F West (landing at `(7, 11)`).

4. **Toggle 3F West Switch to State B:**
   - Walk to the switch via Column 1 detour: Walk Left to Column 3 Row 11, Down to Column 3 Row 13, Left to Column 1 Row 13, Up to Column 1 Row 11, and face Right to toggle the Mewtwo statue switch at `(2, 11)` to State B!

5. **Walk to Balcony on 3F East (State B) and Drop to B1F East:**
   - Walk to 3F East: from (2, 11), walk DOWN to Row 12, RIGHT to Column 6, UP to Row 9, and RIGHT across Column 11 to (12, 9).
   - Walk UP Column 12 to Row 6: (12, 9) -> (12, 6).
   - Navigate to the Balcony and drop down to B1F East. (Path to be systematically verified on foot).

6. **Retrieve Secret Key on B1F East (State B) and Escape:**
   - Walk UP Column 19/20 to Row 5, and use the open Row 5 gate to walk to northwest room: `(19, 16) -> (21, 16) -> (21, 5) -> (1, 5)`.
   - Stand at `(1, 5)` facing UP and press A to retrieve the **Secret Key** at `(1, 4)`!
   - Use **DIG** to escape back to Cinnabar Island!



## Discovered Spatial Constraints & Structural Barriers
- **1F Column 13 Wall (Rows 6-13):** Solid vertical permanent wall separating 1F West from 1F East. The ONLY open horizontal crossings on Column 13 are on Row 4 and Row 5 (empirically verified on foot on Turn 55304).
- **3F East Row 7 Barriers (Columns 14-22):** Shutter gates on Columns 14-21 are CLOSED in State B (empirically verified on foot on Turn 55228, 55233, 55234, 55237). Column 22 is a solid vertical wall. This prevents any vertical passage from Row 6 to Row 8 on the East side in State B!
- **3F East Column 13 Wall (Rows 7-13):** Solid vertical permanent wall, blocking horizontal passage on Rows 7, 8, 9, 10, and 11 (verified on Turn 55240, 55243). Row 13 is a solid horizontal railing, blocking downward vertical passage on Column 12 (verified on Turn 55244).
- **Column 22 on 2F East:** Solid permanent wall blocking horizontal passage below Row 3 in both States (verified by bumping at (22, 11) on Turn 54878 and (22, 10) on Turn 54882).
- **Row 13 on 3F East Column 19:** Shutter gate that is CLOSED in State B (verified by bumping on Turn 54982 and Turn 55109).
- **Row 16 on 3F East Columns 18-26:** Completely solid wooden railing across all columns (including 20, 21), making Row 16 impassable from Row 15 in both States (unless a gate is specifically open).

## Newly-Discovered Structural Barriers (Updated Turn 55401)
- **2F West Column 13 Wall (Rows 7-11):** Solid vertical permanent wall separating 2F West from 2F East, blocking all horizontal traversal on these rows (empirically verified by bumping at (12, 11) on Turn 55251).
- **3F West Row 7 Hedge Wall (Columns 4-9):** Solid permanent vertical and horizontal hedge barrier, completely blocking all upward vertical traversal from Row 8 to Row 6 (empirically verified on foot on Turn 55368 and Turn 55389). Row 6 is also completely filled with hedges/rubble on Columns 3-9, meaning the southwest room on 3F is completely walled off from the northwest room of 3F West.

## Crucial Verification & Discoveries (Turn 55701)
- **Mewtwo Statues on East Side (2F East, 3F East) do NOT have switches:** They are purely decorative. Toggling back to State A once on the East side is physically impossible!
- **State A Crossing is Impossible:** Because the Row 9 gates are closed in State A on 1F West, 2F West, and 3F West, and Column 13/11 are solid walls below Row 9, the player is physically cut off from crossing from West to East in State A.
- **The Balcony Drop on 3F East is the ONLY Physical Way to B1F East:** Because the B1F stairs on 1F East (22, 4) are closed in State B, and Row 7 gates on 2F East are closed in State B, we cannot go down the stairs to B1F in State B. Since we can only cross in State B, the Balcony Drop is the only way to B1F East!
- **Mewtwo Statue at (2, 11) on 2F West has no collision in State B:** It is completely walkable when State B is active.