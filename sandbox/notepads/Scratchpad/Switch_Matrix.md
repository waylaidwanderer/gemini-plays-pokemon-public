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
- **2F West Row 9 Wall (Columns 2-9):** Permanent solid horizontal wall separating southern hallway from northern rooms.
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
- **2F West Column 10 Row 8 Gate:** OPEN (verified on Turn 55967).
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

   - From `(11, 6)`, walk RIGHT to Column 21 `(21, 6)` -> LEFT 2 steps to `(19, 6)` -> UP to Row 3 `(19, 3)` (bypassing the Row 5/6 pitfalls) -> RIGHT along Row 3 to `(26, 3)` (walk UP Row 3 to get to Row 4).
   - Step DOWN/RIGHT onto Column 26 to fall through the pit, landing on 1F East inside the fenced room at `(26, 4)`.

5. **Warp DOWN to B1F East & Retrieve Secret Key:**
   - On 1F East inside the fenced room, walk to `(21, 2)` -> step RIGHT onto stairs at `(22, 2)` and walk UP to warp down to B1F East (landing at `(22, 3)`).
   - On B1F East, walk horizontally along Row 5 across Column 9 gate (now open in State B) directly to B1F West at `(1, 5)`.
   - Stand at `(1, 5)` facing UP and retrieve the Secret Key at `(1, 4)`!
   - Escape via DIG back to Cinnabar Island.
---

## Verified Switch Mechanics & Spatial Constraints (Turn 58016)

1. **Global Switch Persistence:**
   - The global Mewtwo statue switch state (State A vs State B) persists across DIG warps, player blackouts, and complete mansion exits/re-entries. Once toggled to State B, the mansion remains in State B until explicitly toggled back to State A at any switch. (Verified Turn 57829-57840).

2. **3F West Staircase Warp Trap at (7, 10):**
   - The staircase at `(7, 10)` on 2F West warps the player up to `(7, 10)` on 3F West.
   - However, `(7, 10)` on 3F West also acts as an immediate automatic DOWN warp back to 2F West at `(7, 11)` if entered from the overworld, or if the destination tile on 3F West is blocked.
   - In State A, the shutter gate on 3F West at Row 10/9 is CLOSED, which blocks the warp landing tile at `(7, 10)` on 3F West. Because of this, warping UP in State A immediately triggers a collision pushback, sending the player back down to 2F West at `(7, 11)`.
   - In State B, the shutter gate is OPEN, allowing the player to land safely on 3F West at `(7, 10)` and stay on the floor.

3. **3F West Column 8 and Row 7 Layout & Bypass:**
   - To navigate 3F West without stepping on the `(5, 10)` down-staircase warp, the player MUST walk on Row 11:
     - From landing at `(7, 10)`, walk DOWN to `(7, 11)`.
     - Walk LEFT along Row 11 to Column 1 `(1, 11)`.
     - Walk UP Column 1 to Row 9 `(1, 9)`.
     - This path is completely open in State B and safely circumvents the `(5, 10)` staircase warp and the `(8, 9)` rock block.

## 🔍 Switch Interaction Mechanics (Corrected Turn 58507)
- **3F West Switch Interaction Coordinates:**
  - Stand at `(2, 12)` facing UP towards the statue at `(2, 11)`.
  - Press `A` to interact.
  - Choose YES to toggle the switch.
  - The switch can ONLY be interacted with from the bottom (standing at `(2, 12)` facing UP). Interaction from the left side (standing at `(1, 11)` facing RIGHT) is completely non-interactive. It will select "NO" by default or ignore A presses, leaving the mansion stuck in State A.
  - This direction-dependence is a hardcoded Gen 1 engine quirk of this specific switch.
## The Verified State B 2F West to 3F East Bypass Route (Verified Turn 59714)
The gate at `(6, 7)` on 2F West is CLOSED in State B, so we cannot walk UP Column 6 past Row 8.
However, Column 5 on 2F West is completely OPEN vertically in State B (since there are no cabinets or shutter gates blocking Column 5 on Rows 3-11).
Thus, the correct State B bypass route on 2F is:
1. Walk from 2F West landing `(5, 11)` UP Column 5 directly to Row 3 `(5, 3)`.
2. Walk RIGHT along Row 3 to Column 18 `(18, 3)` (this crosses horizontally from 2F West to 2F East, completely above all barriers).
3. Walk DOWN Column 18 to Row 10 `(18, 10)`.
4. Walk LEFT along Row 10 to `(15, 10)`.
5. Step DOWN onto the stairs at `(15, 11)` on 2F East to warp UP to 3F East!
6. On 3F East, land at `(16, 11)`. Since we are in State B, the Row 11 gate at `(14, 11)` is OPEN, allowing us to walk RIGHT along Row 11 to Column 20, then UP Column 20 to Row 3, RIGHT Row 3 to `(26, 3)` and drop through the pitfall to 1F East inside the fenced room!

## Verified Parity Log (Turn-Stamped)
- **Turn 58742:** Player at `(2, 12)` facing RIGHT, pressed `A` (Did NOT toggle switch).
- **Turn 58747:** Player at `(2, 12)` facing UP, selected YES to toggle. Toggled from State B to State A (Row 9 gates CLOSED, Row 12 OPEN).
- **Turn 58757:** `toggle_and_drop.py` aborted mid-execution (exceeded button limit). State remained State A.
- **Turn 58759:** Player at `(2, 12)` facing UP, selected NO by pressing B too quickly on YES/NO menu. Did NOT toggle switch.
- **Turn 58764:** Player at `(2, 12)` facing UP, selected YES to toggle. Toggled from State A to State B (Row 9 gates OPEN, Row 12 CLOSED). Verified open on Turn 58765.
- **Turn 58766:** `walk_to_pitfall_correct.py` ran. Battle desynchronization at `(2, 12)` caused the script to accidentally press `A` on the overworld after the battle ended, toggling the switch back from State B to State A.
- **Turn 58776:** Player at `(2, 12)` facing RIGHT, pressed `A` (Did NOT toggle switch).
- **Turn 58777:** Player at `(2, 12)` facing UP, selected NO by pressing B too quickly on YES/NO menu. Did NOT toggle switch.
- **Turn 58780:** Player at `(2, 12)` facing UP, selected YES to toggle. Toggled from State A to State B (Row 9 gates OPEN). Verified OPEN on Turn 58782. Current mansion state: **STATE B**.
## Decorative Mewtwo Statues (No Switches)
- **2F East / 3F East Statues:** The Mewtwo statues at `(13, 9)` and `(13, 11)` on 2F East and 3F East have been empirically tested and are completely decorative. Pressing A on them does not open any switch dialogue and will not toggle the shutter gates. Do not waste turns attempting to interact with them.


## Verified 3F West Switch Statue Interaction Coordinates (Turn 60244)
- **Switch Statue Coordinate:** `(2, 12)` on 3F West.
- **Player Standing Position:** `(2, 13)` facing UP.
- **Interaction:** Press A from `(2, 13)` facing UP to toggle.
- **Rubble block at (2, 12):** The statue pedestal at `(2, 12)` behaves as a solid block/rubble obstacle from all other sides.


## Verified 3F West Switch Statue Interaction Coordinates (Updated Turn 61084)
- **Primary Switch Statue:** Coordinates at `(2, 10)` on 3F West.
  - Standing Position: Stand at `(2, 11)` facing UP towards `(2, 10)`.
  - Interaction: Press A to open dialogue, select YES, and press A again to dismiss.
- **Secondary Switch Statue:** Coordinates at `(1, 12)` on 3F West (verified on Turn 61072).
  - Standing Position: Stand at `(1, 13)` facing UP towards `(1, 12)`.
  - Collision Obstacle: Since the statue at `(1, 12)` is solid, Column 1 is blocked at Row 12 in both State A and State B!
  - **Bypass Route (Column 2 Row 13):** From `(1, 13)`, walk RIGHT to `(2, 13)`, and walk UP Column 2 directly to Row 6 `(2, 6)` (this bypasses the solid statue at `(1, 12)` completely on Column 2, which is open floor!).
- Shutter Gate at (6, 9) and (1, 9): OPEN in State B, CLOSED in State A.
- Column 6/7 Row 9 is blocked by a permanent solid structural wall on 3F West. To cross from the southern hallway to the northern rooms of 3F West, you MUST walk along Column 2 through the Row 9 gate which is OPEN in State B.