# Pokémon Mansion - Switch Matrix & Shutter Gate Log

## Overview
- Switches are located on Mewtwo statues. They toggle the states of electronic shutter gates globally across all floors.
- Standard state of gates has two modes: **DEFAULT (State A)** and **TOGGLED (State B)**.
- Note: Changing floors (via stairs, ladders, or pits) in Pokémon Mansion preserves the global switch state! It does NOT reset!

## Switch Locations
- **2F:** Mewtwo statues located at `(12, 9)` / `(12, 11)` and `(2, 11)` (northwest diary room).
- **3F:** Mewtwo statue switch located in the east-central section (access requires State A).
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
- **Southeast Stairs Gate:** On 2F, the shutter gate at `(18, 8)` / `(19, 8)` is physically **CLOSED** in State B, blocking access to the stairs from the north (row 7). It is **OPEN** in State A, allowing entry.
- **Rubble wall at column 7:** On 2F, column 7 is blocked by solid brick wall at rows 8-9, preventing direct northern traversal from (7, 10). Row 7 is open horizontally across columns 8-12 and can be accessed from column 11 or 12.

## Verified 3F Layout Constraints
- **Northeast Columns:** On 3F, columns 18 and 19 on row 8 are blocked by solid columns/machines (empirically verified on Turn 48596).
- **Row 7 Open Corridor:** On 3F, row 7 is completely open horizontally across columns 5 to 22 in both State A and State B, allowing free horizontal traversal across the entire map.

## Verified 2F Switch Shortcut
- **Shortcut Discovery:** The Mewtwo statue switch at `(2, 11)` on 2F can be successfully interacted with and toggled from the left tile at `(1, 11)` by facing **Right**! This completely bypasses the rocky rubble at `(2, 12)` and `(3, 12)`.

## Absolute Master Route to B1F & Secret Key
1. Enter Mansion (State A).
2. Go to 2F via stairs at `(7, 10)` (land at `(7, 11)` on 2F).
3. On 2F (State A), walk to `(2, 11)` switch:
   - Walk `Left` to `(2, 11)`. (Shortcut: Stand at `(1, 11)` and face `Right` to toggle the switch to **State B**).
4. Walk to northeast stairs at `(18, 2)` on 2F (State B):
   - Walk `Down` to `(1, 13)`.
   - Walk `Right` to `(12, 13)` (or `(12, 12)`).
   - Walk `Up` to `(12, 5)`.
   - Walk `Right` to `(18, 5)` (gate at `(15, 5)` is **OPEN** in State B).
   - Walk `Up` to `(18, 2)` stairs -> Warp to 3F!
5. On 3F (State B):
   - Walk `Right` to `(24, 2)` (gate at `(21, 5)` is **OPEN** in State B).
   - Walk all the way `Down` the eastern balcony to `(24, 14)`.
   - Step `Left` off the balcony edge to drop to 1F!
6. On 1F, you will land directly south of the closed gates, in front of the B1F stairs.
7. Step onto B1F stairs and retrieve the Secret Key!

## Turn 48635 Empirical Discoveries & Corrections
- **East-Central Statues are Decorative:** The Mewtwo statues located at `(13, 9)` and `(13, 11)` on 3F do NOT function as switches. Interacting with them from any side (including standing at `(13, 12)` facing UP, or `(12, 11)` facing RIGHT) has no effect. They are purely decorative.
- **East-Central Dead End:** `(13, 12)` is walkable on 3F but is a physical dead end. Column 14 is blocked by rubble starting at `(14, 12)`, and Row 13 is blocked by a railing/wall at `(13, 13)`.
- **Row 8 Blockages:** Columns 14, 15, 16, and 17 are physically blocked on 3F Row 8 by rubble, preventing direct horizontal or southern traversal across those tiles from the east-central section.
- **Search for True 3F Switch:** Since the east-central statues are decorative, the actual 3F Mewtwo statue switch must be located elsewhere on 3F (likely in the central-western or northwestern rooms near the stairs/bookshelves).
