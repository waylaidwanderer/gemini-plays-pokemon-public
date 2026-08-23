# Pokémon Mansion - Verified Switch Matrix & Master Route

## Overview
- Global Mewtwo statue switches toggle electronic shutter gates between DEFAULT (State A) and TOGGLED (State B).
- Floor transitions preserve the active state.
- B1F West SOUTH is permanently separated from B1F West NORTH by a solid brick wall on Row 9.
- 1F East is blocked from going up to 2F East in State B because the gate at `(15, 8)` is closed, and Column 14 is permanently blocked by rubble on Rows 12-16.
- 3F West is permanently separated from 3F East by a solid column of rubble at Column 10 on Rows 9-16. This blocks all horizontal crossing on 3F in State A (except Row 6, which is in the northern rooms).

---

## Shutter Gate Configurations & Structural Barriers

### Permanent Structural Barriers
- **Column 22 on 2F East:** Solid permanent wall blocking horizontal passage below Row 3 (verified by bumping at (22, 11) on Turn 54878 and (22, 10) on Turn 54882).
- **3F West Pitfall Trap at (5, 9):** Permanent structural hazard that warps/drops the player down to 2F West at (5, 10) (verified on Turn 55204). Avoid walking UP to Row 9 Column 5 on 3F West in both State A and State B!
- **3F West Row 9 Wall (Columns 6-7):** Permanent solid vertical wall separating the southern hallway from northern rooms, blocking vertical traversal on these columns (verified on Turn 55219).
- **1F West Row 9 Columns 3-9 Wall:** Permanent solid horizontal wall separating southern hallway (Row 10-14) from northern rooms (Row 5-8).

### State A (Default)
- **1F West Row 9 Gates:** CLOSED.
- **2F West Row 9 Gates:** CLOSED.
- **2F West Column 10 Row 8:** OPEN (verified on Turn 55967).
- **2F Column 15 Row 6:** OPEN (verified on Turn 55941).
- **B1F South-East gate at `(10, 11)`:** OPEN (allows crossing between West and East B1F SOUTH on Row 11).
- **3F East gate at `(15, 11)` (stairs):** OPEN (as a DOWN warp to 2F East).
- **1F East gate at `(15, 8)`:** OPEN.
- **B1F North-Central gate at `(9, 5)`:** CLOSED.
- **2F East Row 7 Gates:** OPEN (allows vertical crossing on Column 15).
- **3F West Row 9 Gates:** CLOSED.
- **3F West Row 11 Column 11:** OPEN.
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
   - Walk from Cinnabar Island `(11, 12) -> (18, 12) -> (18, 5) -> (6, 5) -> (6, 4) -> (6, 3)` and step UP to enter 1F West (landing at `(5, 27)`).

2. **Warp UP 1F West -> 2F West -> 3F West (State A):**
   - Walk to `(5, 11)` -> `(8, 11)` -> `(8, 10)` -> `(5, 10)` -> step LEFT to warp to 2F West (landing at `(5, 11)`).
   - Walk Right 2 steps to `(7, 11)` -> step UP onto stairs at `(7, 10)` to warp UP to 3F West (landing at `(7, 11)`).

3. **Toggle 3F West Mewtwo Switch to State B:**
   - On 3F West: walk to `(4, 11)` -> `(4, 13)` -> `(1, 13)` -> `(2, 13)` -> `(2, 12)`.
   - Stand at `(2, 12)` facing UP towards the Mewtwo statue switch at `(2, 11)` and toggle it to State B! (Select YES).

4. **Cross 3F West to 3F East & Drop to 1F East:**
   - From `(2, 12)`, walk LEFT to `(1, 12)` -> UP to `(1, 10)` -> DOWN to `(1, 13)` -> RIGHT along Row 13 to Column 11 `(11, 13)` -> UP Column 11 to Row 6 `(11, 6)`.
   - From `(11, 6)`, walk RIGHT to Column 21 `(21, 6)` -> LEFT 2 steps to `(19, 6)` -> UP to Row 3 `(19, 3)` (bypassing the Row 5/6 pitfalls) -> RIGHT along Row 3 to `(26, 3)`.
   - Step DOWN/RIGHT onto Column 26 to fall through the pit, landing on 1F East inside the fenced room at `(26, 3)`.

5. **Warp DOWN to B1F East & Retrieve Secret Key:**
   - On 1F East inside the fenced room, walk to `(21, 2)` -> step RIGHT onto stairs at `(22, 2)` and walk UP to warp down to B1F East (landing at `(22, 3)`).
   - On B1F East, walk horizontally along Row 5 across Column 9 gate (now open in State B) directly to B1F West at `(1, 5)`.
   - Stand at `(1, 5)` facing UP and retrieve the Secret Key at `(1, 4)`!
   - Escape via DIG back to Cinnabar Island.