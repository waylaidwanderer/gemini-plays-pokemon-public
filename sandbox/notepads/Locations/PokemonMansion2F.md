# Pokmon Mansion 2F - Map & Navigation Log

## Physical Layout & Barriers (State-Dependent)
- **Column 10 Rubble & Gates (State B):**
  - Row 8 Column 10 (10, 8) is a CLOSED shutter gate in State B.
  - Row 9 Column 10 (10, 9) is blocked by solid rubble.
  - Row 10 Column 10 (10, 10) is blocked by solid rubble.
  - Row 11 Column 10 (10, 11) is blocked by closed gates / rubble.
- **Row 11 Shutter Gates (State B):**
  - Row 11 Column 7 (7, 11), Column 6 (6, 11), Column 5 (5, 11) are completely OPEN and walkable in State B!
  - This connects 2F East (Columns 12-28) and 2F West (Columns 1-11) horizontally on Row 11 in State B.
- **Northeast Stairs (22, 1):**
  - The northeast stairs at (22, 1) on 2F East only lead UP to 3F East (landing at 22, 1 on 3F).
  - They do NOT warp the player down to 1F.
- **State B Corridor & Stair warps (Verified Turn 67507/67570/69025):**
  - Row 4 on 2F is a completely open and passable horizontal corridor (Columns 5-12) in State B, connecting the western and eastern sections. Row 6 is blocked by a solid partition wall at (9, 6).
  - The stairs at (7, 10) on 2F West warp the player DOWN to 1F West, landing at (7, 11) on 1F.

## Mewtwo Statue Switches
- **2F West Switches:**
  - **Mewtwo Statue Switch at (2, 5):** Fully active! Toggled by standing at `(2, 6)` facing UP (verified on Turn 71035). This is the ONLY active switch on 2F!
  - Toggling this switch alternates the Mansion between **State A** and **State B**.

## State A vs State B Gate Configurations (Verified Turn 70924)
- **State B (Default):**
  - Shutter gate at `(5, 9)` on Column 5 (2F West) is CLOSED, blocking the stairs UP at `(5, 10)`.
  - Shutter gates on Row 11 (Columns 5, 6, 7) are OPEN.
  - Shutter gates on Row 5 (Columns 15, 16, 17) on 2F East are OPEN.
- **State A:**
  - Shutter gate at `(5, 9)` on Column 5 (2F West) is OPEN, unblocking the stairs UP at `(5, 10)`.
  - Shutter gates on Row 11 (Columns 5, 6, 7) are CLOSED.
  - Shutter gates on Row 5 (Columns 15, 16, 17) on 2F East are CLOSED.

## Southwest Staircase Warp Connections
- **Staircase (5, 10) on 2F West:** Warps UP to 3F West, landing at `(5, 11)` on 3F West.
- **Staircase (7, 10) on 2F West:** Warps DOWN to 1F West, landing at `(7, 11)` on 1F West.

## Empirical Gate Observations (Verified Turn 71043 / 71052)
- **State B (Default):**
  - Shutter gate at `(5, 9)` on Column 5 is CLOSED, blocking the stairs UP at `(5, 10)`.
  - Shutter gates on Row 11 (Columns 5, 6, 7) are OPEN, allowing horizontal passage between 2F West and 2F East.
- **State A:**
  - Shutter gate at `(5, 9)` on Column 5 is OPEN, unblocking the stairs UP at `(5, 10)`.
  - Shutter gates on Row 11 (Columns 5, 6, 7) are CLOSED, blocking horizontal passage along Row 11.
  - Horizontal passage on the north side of 2F between East and West is completely open along Row 2! Column 9 Row 2 is a pink checkered floor with no wall.
  - Row 6 Column 4 and Row 7 Column 4 on 2F West are blocked by solid window frames, so Row 8 is the primary horizontal corridor to cross Column 4 on the north side of 2F West.

## Mewtwo Switch Interaction Protocol (Verified Turn 71072)
- Exactly **4 A-presses** are required to fully complete the dialogue and physically toggle the gate states:
  1. First 'A' - Displays "A secret switch!"
  2. Second 'A' - Displays "Press it?" with YES/NO choice.
  3. Third 'A' - Confirms "YES".
  4. Fourth 'A' - Displays "Who wouldn't?" and then closes the textbox, returning control to the overworld.
- Walking away before the fourth 'A' is pressed will consume the first movement key to close the textbox, leaving the player in place and causing routing misalignment. Always verify the overworld is active before moving.
## Pitfall Warp landing (Verified Turn 71668)
- **3F East Pitfall landing:** Falling through the pitfall at `(26, 3)` on 3F East lands the player at `(26, 4)` on 2F East (Southeast fenced area).
- **2F East physical layout near landing:** Columns 22, 23, 24 on Row 4 on 2F East are permanently blocked by rubble. Row 3 Columns 21-27 is a completely open pink checkered horizontal path connecting Columns 21 and 25. Row 6 Column 15 is completely open and serves as the horizontal transition between 2F East and 2F West in State B.