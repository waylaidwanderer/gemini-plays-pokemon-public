# Pokémon Mansion - Switch Matrix & Shutter Gate Log

## Overview
- Switches are located on Mewtwo statues. They toggle the states of electronic shutter gates globally across all floors.
- Standard state of gates has two modes: **DEFAULT (State A)** and **TOGGLED (State B)**.

## Switch Locations
- **2F:** Mewtwo statues located at `(12, 9)` and `(12, 11)` (east-central corridor). 
- **3F:** Mewtwo statue located at `(2, 11)` (northwest diary room).
- **B1F:** Mewtwo statue switch located near the center-left.

## Gate Configurations by State

### DEFAULT STATE (State A)
- **1F B1F stairs gate at `(22, 2)`:** **CLOSED** (Blocks B1F stairs).
- **2F stairs gate at `(5, 7)`:** **OPEN** (Allows direct access to 3F stairs at 5, 10).
- **3F gate at `(21, 5)`:** **CLOSED** (Blocks column 21 access to northeast room/pit).

### TOGGLED STATE (State B)
- **1F B1F stairs gate at `(22, 2)`:** **OPEN** (Allows access to B1F stairs).
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **3F gate at `(21, 5)`:** **OPEN** (Allows access to column 21 and the northeast room/pit).
- **B1F Secret Key Room:** **OPEN**.

## Standard Routing to B1F & Secret Key
1. Enter Mansion (State A).
2. Walk UP column 5 on 1F, step onto (5, 10) stairs to warp to 2F.
3. On 2F, walk UP column 5, step onto the stairs at (5, 10) to warp to 3F.
4. On 3F, walk Left to (2, 12), face UP, and toggle the Mewtwo statue switch at (2, 11) to State B.
5. On 3F, walk east along row 11/12 (avoiding row 12 column 7 wall by walking through row 11), go north to column 12 row 7, walk east along row 7 to (21, 7), walk UP through the open gate at (21, 5) to the northeast room, and step into the pit at (24, 5).
6. The (24, 5) pit drops the player to 2F (9, 9) and then we fall through to 1F (9, 9) (the fenced-in room) in State B.
7. Go down B1F stairs at (22, 2) (which is open in State B), flip B1F switch to State B to open Secret Key Room, and retrieve the Secret Key.