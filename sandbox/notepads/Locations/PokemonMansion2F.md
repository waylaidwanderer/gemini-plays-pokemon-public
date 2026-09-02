# Pokémon Mansion 2F - Map & Navigation Log

## Physical Layout & Walkable Areas
- **Size:** 20 Columns x 18 Rows.
- **Horizontal Split in State B:**
  - Row 6 is blocked horizontally in **State B** by a closed shutter gate at `(9, 6)`.
  - Row 5 is completely open horizontally on Columns 2 to 10 in State B, containing a 1-tile gap past Column 9 at `(9, 5)`. This allows horizontal passage between 2F East and 2F West in both states!
- **2F West Layout & Landmarks:**
  - **Mewtwo Statue Switch:** Located at `(2, 11)`. Interacted from `(2, 12)` facing UP. Toggling to State A opens the Row 9 gates and 2F East staircase gate.
  - **3F West Staircase Warp:** Located at `(5, 10)`. Stepping here warps the player UP to 3F West.
  - **1F West Staircase Warp:** Located at `(7, 10)`. Stepping here warps the player DOWN to 1F West (landing at 7, 11).
  - **Shutter Gate at (5, 9):** Blocks Column 5 Row 9 in State B; open in State A.
- **2F East Layout & Landmarks:**
  - **Staircase Warp at (22, 2):** Warps UP to 3F East (landing at 22, 2).
    - Blocked by a closed shutter gate at `(22, 2)` in **State B**!
    - Open in **State A**, allowing access to 3F East.
  - **Row 5 Shutter Gates:** Closed at `(20, 5)` and `(21, 5)` in State B.
  - **Row 4 Bypass:** Completely open horizontally on Columns 18-21.

## Verified Routing Protocols
- To go from **2F East** (southern/northern) to **2F West** in **State B**:
  1. Walk to `(10, 5)` on Row 5.
  2. Walk Left along Row 5 through `(9, 5)` to `(2, 5)` on 2F West.
- To go from **2F West** to **3F West** in **State B**:
  1. Walk to `(2, 12)`.
  2. Face UP towards the switch at `(2, 11)` and toggle to **State A**.
  3. Walk Right to `(5, 12)`, then UP to `(5, 10)` to take the stairs to 3F West.