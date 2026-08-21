# Pokémon Mansion - Switch Matrix & Shutter Gate Log

## Overview
- Switches are located on Mewtwo statues. They toggle the states of electronic shutter gates globally across all floors.
- Standard state of gates has two modes: **DEFAULT (State A)** and **TOGGLED (State B)**.
- Note: Changing floors (via stairs, ladders, or pits) in Pokémon Mansion preserves the global switch state! It does NOT reset!

## Switch Locations
- **2F:** Mewtwo statues located at `(12, 9)` / `(12, 11)` and `(2, 11)` (northwest diary room).
- **3F:** Mewtwo statue switch located at `(2, 11)`, accessed from `(2, 12)` facing Up or `(1, 11)` facing Right.
- **B1F:** Mewtwo statue switch located near the center-left.

## Gate Configurations by State

### DEFAULT STATE (State A)
- **3F shutter gates at `(18, 8)` / `(19, 8)`:** **OPEN** (Verified on Turn 50696; allows vertical traversal between row 7 and row 11 to reach the eastern stairs at `(15, 11)`).
- **1F B1F stairs gate at `(18, 16)`/`(19, 16)`:** **CLOSED** (Blocks access to bottom-right of 1F).
- **1F 1F/2F stairs gate at `(22, 2)`:** **CLOSED** (Blocks stairs going up to 2F).
- **1F central gates at `(5, 8)`/`(6, 8)`/etc.:** **CLOSED** (Blocks north to south traversal).
- **2F stairs gate at `(5, 7)`:** **OPEN** (Allows direct access to 3F stairs/warps).
- **3F gate at `(10, 11)` / `(10, 12)` (Room Exit):** **OPEN** (Allows walking east to the rest of 3F).
- **3F gate at `(20, 5)`:** **CLOSED** (Blocks column 21 access to northeast room/pit).
- **3F gate at `(20, 17)` / `(21, 17)` (Balcony Shutter):** **CLOSED** (Blocks access to balcony Row 18+).

### TOGGLED STATE (State B)
- **1F B1F stairs gate at `(18, 16)`/`(19, 16)`:** **CLOSED** (Blocks column 19 access to row 24).
- **1F 1F/2F stairs gate at `(22, 2)`:** **OPEN** (Allows access to 2F stairs).
- **1F central gates at `(5, 8)`/`(6, 8)`/etc.:** **OPEN** (Allows north to south traversal).
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **2F northeast gate at `(15, 5)`:** **OPEN** (Allows horizontal access to column 18).
- **3F gate at `(10, 11)` / `(10, 12)` (Room Exit):** **CLOSED** (Blocks room at column 10).
- **3F gate at `(20, 5)`:** **OPEN** (Allows access to column 21 and the northeast room/pit).
- **3F gate at `(20, 17)` / `(21, 17)` (Balcony Shutter):** **OPEN** (Allows access to balcony Row 18+).
- **B1F Secret Key Room:** **OPEN**.

## Verified 2F Layout Constraints
- **Column 15 Cabinets:** On 2F, column 15 is blocked by solid brown cabinets on rows 8-10, separating the column 15 corridor.
- **Rubble wall at column 7:** On 2F, column 7 is blocked by solid brick wall at rows 8-9, preventing direct northern traversal from (7, 10). Row 7 is open horizontally across columns 8-12 and can be accessed from column 11 or 12.

## Verified 3F Layout Constraints
- **Northeast Columns:** On 3F, columns 18 and 19 on row 8 are blocked by solid columns/machines (empirically verified on Turn 48596).
- **Row 7 Blocked on West:** On 3F, row 7 is physically blocked by rubble across columns 5-9 on the west side, but open across columns 10-14 on the east side.
- **Row 3 Column 18/19 Cabinets:** On 3F, columns 18 and 19 on row 3 are blocked by solid cabinets, separating the west/center from the east.
- **Column 15 Wall:** On 3F, column 15 is physically blocked by a solid brick wall across rows 1-4, preventing horizontal traversal past column 15 on those rows.
- **Row 6 Open Passage:** On 3F, row 6 is wide-open horizontally across columns 11-20, allowing horizontal crossing between the east and west wings.
- **3F Switch Location:** The true Mewtwo statue switch on 3F is located at `(2, 11)`, accessed from `(2, 12)` facing Up or `(1, 11)` facing Right.
- **Column 9 Wall:** On 3F, column 9 is a solid vertical wall from row 0 to row 6. (Empirically verified on Turn 49004 by attempting to walk Left from (10, 3) to (9, 3) and being blocked by a solid wall boundary).
- **Column 8 and 3 Green Cabinets:** On 3F, Columns 8 and 3 are blocked by solid green cabinets/pillars at even rows 10, 12, 14, 16. (Empirically verified on Turn 49559/49566). Odd rows 11, 13, 15 are open and walkable horizontally across Column 8 and 3.
- **Column 11 Row 8 Rubble:** On 3F, Column 11 Row 8 is physically blocked by a solid pile of rubble/debris (empirically verified on Turn 49590). Column 12 is completely open vertically and must be used to traverse vertically.



## Absolute Master Route to B1F & Secret Key (Verified Turn 48801)
1. Enter Mansion (State A).
2. Go to 2F via stairs at `(7, 10)` (land at `(7, 11)` on 2F).
3. On 2F (State A), walk to `(1, 11)` and face `Right` to toggle the switch at `(2, 11)` to **State A** (Default).
   - Note: If the switch is already in State A, skip this step.
4. Walk back to the stairs at `(7, 10)` on 2F (State A) and ascend to 3F:
   - Correct bypass route: `Down` to `(1, 13)` -> `Right` to `(4, 13)` -> `Up` to `(4, 10)` -> `Right` to `(7, 10)` stairs (Warp to 3F).
5. On 3F (State A), walk to the true west-side Mewtwo statue switch at `(2, 11)`:
   - From `(7, 11)` landing, walk Left to `(2, 12)` and face Up.
   - Press `A` to toggle the switch to **State B**!
6. On 3F (State B), walk to the balcony drop on the east side of 3F:
   - From `(2, 12)`, walk Right to `(7, 12)` -> Down to `(7, 13)` -> Right to `(9, 13)` -> Up to `(9, 10)` (bypassing column 8 even-row pillars) -> Right to `(11, 10)`.
   - Walk Up column 11 to `(11, 5)` -> Right along row 5 to `(20, 5)` (Gate at (20, 5) is OPEN in State B!).
   - Walk Up to `(21, 3)` -> Right to `(26, 3)` (bypassing row 4 wall at cols 22-25) -> Down to `(26, 5)` -> Left to `(24, 5)`.
   - Walk Down column 24 to `(24, 7)`.
   - Walk Right to `(26, 7)` -> Down column 26 to `(26, 12)` (bypassing row 8 raised platform) -> Left to `(25, 12)` -> Down column 25 to `(25, 14)` -> Left to `(22, 14)` (bypassing row 13 railing at col 26).
   - Enter balcony doorway at `(21, 15)` and step onto the landing at `(20, 15)`.
   - Walk Down through the open shutter gate at `(20, 17)` to `(20, 18)`.
7. Step Left onto `(19, 18)` to drop over the balcony railing to B1F!
## Turn 48635 Empirical Discoveries & Corrections
- **East-Central Statues are Decorative:** The Mewtwo statues located at `(13, 9)` and `(13, 11)` on 3F do NOT function as switches. Interacting with them from any side (including standing at `(13, 12)` facing UP, or `(12, 11)` facing RIGHT) has no effect. They are purely decorative.
- **East-Central Dead End:** `(13, 12)` is walkable on 3F but is a physical dead end. Column 14 is blocked by rubble starting at `(14, 12)`, and Row 13 is blocked by a railing/wall at `(13, 13)`.
- **Row 8 Blockages:** Columns 14, 15, 16, and 17 are physically blocked on 3F Row 8 by rubble, preventing direct horizontal or southern traversal across those tiles from the east-central section.

## Empirical Reset Verification (Burden of Proof)
- **DIG / Exit Reset:** On Turn 49084, DIG was used to exit the mansion. Upon re-entering the mansion on Turn 49111, the gate at `(10, 11)` on 3F was observed OPEN, and the gate at `(2, 12)` was OPEN, empirically proving that exiting and re-entering resets the global switch to **State A**.

## Mapped East Wing & Corridor Constraints (Turns 49145-49271)
- **Column 10 Gates:** Closed vertical shutter gate on rows 11 to 15 in State B (empirically blocked on Turn 49259; open in State A).
- **Row 11 Horizontal Passage:** Completely open horizontally across column 22 in both states, allowing horizontal bypass of column 22 rubble.
- **Column 22 Rubble:** Blocked by solid rubble piles on rows 8, 9, 10, 12, 13 (verified on Turn 49185).
- **Columns 4-7 Red Corridor:** Enclosed corridor on rows 10-18 in State B. Gate at column 3/4 is CLOSED on rows 12-20 in State B (verified on Turn 49212). Gate at column 7/8 is CLOSED on rows 10-20 in State B.
- **Row 9 West Wall:** Solid horizontal wall across columns 2 to 7 on row 9 (empirically blocked on Turn 49251).

- **3F gate at (24, 13) / (25, 13):** CLOSED in State B (verified on Turn 49350), OPEN in State A.
- **3F gate at (20, 8) / (21, 8):** **CLOSED in State B** (Empirically verified on Turn 50793; column 20 is blocked at row 8 in State B, requiring the northeast detour through columns 21-26).
## Critical 2F/3F Cross-Floor Traversals (Verified Turn 51120)
- **Isolation of 2F East Side:** The east side of 2F (including the East Stairs at `(15, 11)`) is completely physically isolated from the west side of 2F. Row 11 is blocked by Mewtwo statue at `(13, 11)`. Row 12-16 at column 14 are completely solid yellow-brown rubble walls. There is NO WAY to walk from the west side to the east side on 2F!
- **3F West-East Crossing (State A):** The only way to cross from the west side of the mansion to the east side of the mansion is on **3F** in **State A**.
  - Path on 3F (State A): From West Stairs landing at `(7, 11)`, walk Right to `(12, 11)` (gate at 10, 11 is OPEN). Walk Up column 12 to `(12, 6)`. Walk Right on row 6 to column 19 (bypassing solid column 14!). Walk Down column 19 to `(19, 11)` (gate at 19, 8 is OPEN). Walk Left along row 11 to `(15, 11)` East Stairs!
  - Warp down to 2F (East side, State A) landing at `(16, 11)`.
- **Switch to State B on 2F East Side:**
  - On 2F (East side, State A), walk Left to `(12, 11)`. Face Right (towards Mewtwo switch at `(13, 11)`) and press `A` to toggle to **State B**!
- **Balcony Drop (State B):**
  - On 2F (East side, State B), walk Right to `(15, 11)` East Stairs and warp UP to 3F (State B).
  - Land on 3F (East side, State B) at `(16, 11)`. Walk Right along row 11 to `(21, 11)` -> Down column 21 to `(21, 15)` -> Left to `(20, 15)` balcony landing.
  - Walk Down through open balcony shutter gate at `(20, 17)` to `(20, 18)` and step Left to `(19, 18)` to drop to B1F!
## Verified 3F State B Layout & Constraints (Turns 51230-51255)
- **Column 11 Vertical Gate:** CLOSED in State B on rows 11-15. Bypassed by walking horizontally through Row 10 `(11, 10)` which is wide-open and has no gate!
- **Row 5 Shutter Gate:** CLOSED in State B at `(15, 5)`/`(16, 5)`/`(20, 5)`/`(21, 5)`. OPEN at columns 18 and 19!
- **Row 3 Column 19 Counter:** Solid 2-tile high wooden counter blocks Column 19 at `(19, 2)`/`(19, 3)`. Reachable only on Row 4 `(19, 4)`!
- **Column 21 Row 3 Corridor:** Wide-open and pink walkable tile, allowing vertical crossing from Row 4 to Row 3.
- **Row 5 Rubble Blockage:** Columns 22, 23, and 24 on Row 5 are physically blocked by permanent yellow-brown rubble. Bypassed in State B by walking horizontally on Row 3 to Column 25, then Down Column 25 to `(25, 5)`, and Left horizontally on Row 5 to `(22, 5)` pit (which is open in State B!).

## Verified State B B1F Descent Path
1. Stand at `(1, 11)` on 3F West.
2. Walk to `(5, 11)` via Row 13.
3. Cross Column 11 vertical gate via Row 10: `(5, 11) -> (9, 11) -> (9, 10) -> (11, 10)`.
4. Walk Up Column 11 to Row 5, then Right to Column 19: `(11, 10) -> (11, 5) -> (19, 5)`.
5. Walk Up Column 19 to Row 4, then Right on Row 4 to Column 21: `(19, 5) -> (19, 4) -> (21, 4)`.
6. Walk Up Column 21 to Row 3, then Right to Column 25: `(21, 4) -> (21, 3) -> (25, 3)`.
7. Walk Down Column 25 to Row 5, then Left to the pit at `(22, 5)`: `(25, 3) -> (25, 5) -> (22, 5)`.
8. Fall through the pit to 2F East landing at `(22, 6)`.
9. On 2F East, walk to the East Stairs `(15, 11)`: `(22, 6) -> (22, 11) -> (15, 11)`.
10. Warp UP to 3F East (lands at `(16, 11)` in State B, South of the closed Row 8 gates!).
11. Walk directly to the balcony landing `(20, 15)`: `(16, 11) -> (21, 11) -> (21, 15) -> (20, 15)`.
12. Walk Down to `(20, 18)` and step Left to drop to B1F!