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
- **1F B1F stairs gate at `(18, 16)`/`(19, 16)`:** **CLOSED** (Blocks access to bottom-right of 1F).
- **1F 1F/2F stairs gate at `(22, 2)`:** **CLOSED** (Blocks stairs going up to 2F).
- **1F central gates at `(5, 8)`/`(6, 8)`/etc.:** **CLOSED** (Blocks north to south traversal).
- **2F stairs gate at `(5, 7)`:** **OPEN** (Allows direct access to 3F stairs/warps).
- **3F gate at `(10, 11)` / `(10, 12)` (Room Exit):** **OPEN** (Allows walking east to the rest of 3F).
- **3F gate at `(21, 5)`:** **CLOSED** (Blocks column 21 access to northeast room/pit).

### TOGGLED STATE (State B)
- **1F B1F stairs gate at `(18, 16)`/`(19, 16)`:** **CLOSED** (Blocks column 19 access to row 24).
- **1F 1F/2F stairs gate at `(22, 2)`:** **OPEN** (Allows access to 2F stairs).
- **1F central gates at `(5, 8)`/`(6, 8)`/etc.:** **OPEN** (Allows north to south traversal).
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **2F northeast gate at `(15, 5)`:** **OPEN** (Allows horizontal access to column 18).
- **3F gate at `(10, 11)` / `(10, 12)` (Room Exit):** **CLOSED** (Blocks room at column 10).
- **3F gate at `(21, 5)`:** **OPEN** (Allows access to column 21 and the northeast room/pit).
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
- **Column 9 Wall:** On 3F, column 9 is a solid vertical wall from row 0 to row 6. (Empirically verified on Turn 49004 by attempting to walk Left from (10, 3) to (9, 3) and being blocked by a solid wall boundary).
- **Column 9 Wall:** On 3F, column 9 is a solid vertical wall from row 0 to row 6. (Empirically verified on Turn 49004 by attempting to walk Left from (10, 3) to (9, 3) and being blocked by a solid wall boundary).



## Absolute Master Route to B1F & Secret Key (Verified Turn 48801)
1. Enter Mansion (State A).
2. Go to 2F via stairs at `(7, 10)` (land at `(7, 11)` on 2F).
3. On 2F (State A), walk to `(1, 11)` and face `Right` to toggle the switch at `(2, 11)` to **State A** (Default).
   - Note: If the switch is already in State A, skip this step.
4. Walk back to the stairs at `(7, 10)` on 2F (State A) and ascend to 3F:
   - Correct bypass route: `Down` to `(1, 13)` -> `Right` to `(4, 13)` -> `Up` to `(4, 10)` -> `Right` to `(7, 10)` stairs (Warp to 3F).
5. On 3F (State A), walk to the Mewtwo statue switch at `(12, 11)`:
   - From `(7, 11)` landing:
     - `Right` to `(8, 11)` -> `Right` to `(9, 11)` -> `Down` to `(9, 12)` -> `Right` to `(11, 12)` -> `Up` to `(11, 11)`.
     - Face `Right` (towards the statue at (12, 11)) and press `A` to toggle the switch to **State B**!
6. On 3F (State B), walk to the balcony drop at `(24, 14)` via Row 5:
   - Walk `Up` column 11 to `(11, 5)` -> Walk `Right` along row 5 to `(24, 5)` (Gate at (21, 5) is OPEN in State B!) -> Walk `Down` the balcony to `(24, 14)`.
7. Step `Left` off the balcony edge at `(24, 14)` to drop directly to 1F B1F stairs!
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
