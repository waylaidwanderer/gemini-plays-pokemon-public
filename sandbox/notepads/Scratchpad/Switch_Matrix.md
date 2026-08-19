# Pokémon Mansion - Switch Matrix & Shutter Gate Log

## Overview
- Switches are located on Mewtwo statues. They toggle the states of electronic shutter gates globally across all floors.
- Standard state of gates has two modes: **DEFAULT (State A)** and **TOGGLED (State B)**.
- Note: Changing floors (via stairs, ladders, or pits) in Pokémon Mansion preserves the global switch state! It does NOT reset!

## Switch Locations
- **2F:** Mewtwo statues located at `(12, 9)` and `(12, 11)` (east-central corridor). 
- **3F:** Mewtwo statue located at `(2, 11)` (northwest diary room).
- **B1F:** Mewtwo statue switch located near the center-left.

## Gate Configurations by State

### DEFAULT STATE (State A)
- **1F B1F stairs gate at `(18, 8)`/`(19, 8)`:** **OPEN** (Allows access to bottom-right stairs on 1F).
- **1F 1F/2F stairs gate at `(22, 2)`:** **CLOSED** (Blocks stairs going up to 2F).
- **2F stairs gate at `(5, 7)`:** **OPEN** (Allows direct access to 3F stairs at 5, 10).
- **3F gate at `(21, 5)`:** **CLOSED** (Blocks column 21 access to northeast room/pit).

### TOGGLED STATE (State B)
- **1F B1F stairs gate at `(18, 8)`/`(19, 8)`:** **CLOSED** (Blocks access to bottom-right of 1F).
- **1F 1F/2F stairs gate at `(22, 2)`:** **OPEN** (Allows access to 2F stairs).
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **3F gate at `(21, 5)`:** **OPEN** (Allows access to column 21 and the northeast room/pit).
- **B1F Secret Key Room:** **OPEN**.

## Standard Routing to B1F & Secret Key (Verified Turn 47498-47510)
1. Enter Mansion (State A).
2. Walk UP column 5 on 1F, step onto (5, 10) stairs to warp to 2F.
3. On 2F, walk UP column 5, step onto the stairs at (5, 10) to warp to 3F.
4. On 3F, walk Left to (2, 12), face UP, and toggle the Mewtwo statue switch at (2, 11) to State B.
5. On 3F, walk east along row 11/12, go north to column 12 row 7, walk east along row 7 to (21, 7), walk UP through the open gate at (21, 5) to the northeast room, and step into the pit at (24, 5).
6. The (24, 5) pit drops the player to 2F (which has a pit at 24, 5) and we fall through directly to the east wing of 1F, landing at `(22, 7)` in State B.
7. From `(22, 7)` on 1F, walk Left to column 19, walk Down through the open shutter gate at `(19, 8)`/`(19, 9)`, walk Down to row 24, walk Right to `(21, 24)`, and go down the stairs to B1F!
8. Retrieve the Secret Key from B1F.