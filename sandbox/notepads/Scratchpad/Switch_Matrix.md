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
- **1F B1F stairs gate at `(18, 8)`/`(19, 8)`:** **CLOSED** (Blocks access to bottom-right of 1F).
- **1F 1F/2F stairs gate at `(22, 2)`:** **CLOSED** (Blocks stairs going up to 2F).
- **1F central gates at `(5, 8)`/`(6, 8)`/etc.:** **CLOSED** (Blocks north to south traversal).
- **2F stairs gate at `(5, 7)`:** **OPEN** (Allows direct access to 3F stairs/warps).
- **3F gate at `(10, 11)` / `(10, 12)` (Room Exit):** **OPEN** (Allows walking east to the rest of 3F).
- **3F gate at `(21, 5)`:** **CLOSED** (Blocks column 21 access to northeast room/pit).

### TOGGLED STATE (State B)
- **1F B1F stairs gate at `(18, 8)`/`(19, 8)`:** **OPEN** (Allows access to bottom-right of 1F).
- **1F 1F/2F stairs gate at `(22, 2)`:** **OPEN** (Allows access to 2F stairs).
- **1F central gates at `(5, 8)`/`(6, 8)`/etc.:** **OPEN** (Allows north to south traversal).
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **3F gate at `(10, 11)` / `(10, 12)` (Room Exit):** **CLOSED** (Blocks room at column 10).
- **3F gate at `(21, 5)`:** **OPEN** (Allows access to column 21 and the northeast room/pit).
- **B1F Secret Key Room:** **OPEN**.

## Verified 3F Layout Constraints
- **Row 12 & 13 Blockage:** Columns 6 and 7 are completely blocked by a solid counter/desk at `(6, 12)`, `(7, 12)`, `(6, 13)`, `(7, 13)` on 3F. Row 13 is a dead end at column 5.
- **Rubble block:** Rubble completely blocks row 11-12 columns 2-3 on 3F. There is **NO** Mewtwo statue at `(2, 11)` on 3F (this is rubble).

## Standard routing to B1F & Secret Key (State A -> State B)
1. Enter Mansion (State A).
2. Walk UP column 5 on 1F, step onto `(5, 10)` stairs to warp to 2F (lands at `(5, 11)`).
3. On 2F, walk UP column 5 through the open gate at `(5, 7)`, walk East to column 7, and step onto `(7, 10)` to warp to 3F (lands at `(7, 11)`).
4. On 3F, since State A is active, the gate at column 10 is OPEN. Walk East to the east-central section of 3F.
5. On 3F, interact with the eastern Mewtwo statue and toggle the switch to State B.
6. Now in State B, the 3F gate at `(21, 5)` is OPEN. Walk to `(21, 5)`, go to the northeast room, and step into the pit at `(24, 5)` to drop to 1F southeast `(28, 7)`.
7. On 1F, walk Left to column 24, Up to row 3, Left along row 3 to column 19, Down column 19 to row 24, Right to column 21, and down the stairs to B1F at `(21, 24)`.
8. On B1F, retrieve the Secret Key.
## Verified 2F Layout Constraints (Logged Turn 48355)
- **Column 15 Cabinets:** On 2F, column 15 is blocked by solid brown cabinets on rows 8-10, separating the column 15 corridor.
- **Southeast Stairs Gate:** On 2F, the shutter gate at `(18, 8)` / `(19, 8)` is physically **CLOSED** in State B, blocking access to the stairs from the north (row 7). It is **OPEN** in State A, allowing entry.
## Verified 2F Switch Shortcut (Logged Turn 48421)
- **Shortcut Discovery:** The Mewtwo statue switch at `(2, 11)` on 2F can be successfully interacted with and toggled from the left tile at `(1, 11)` by facing **Right**! This completely bypasses the rocky rubble at `(2, 12)` and `(3, 12)` and allows the player to toggle the switch directly without taking detours through the lower half of 2F!