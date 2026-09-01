# Pokémon Mansion 2F - Map & Navigation Log

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
- **2F East/Middle Switches:**
  - **Mewtwo Statue Switch at (13, 9):** Fully active! Toggled by standing at `(12, 9)` facing RIGHT (verified on Turn 70917 and 70923). This is the ONLY active switch on 2F!
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
