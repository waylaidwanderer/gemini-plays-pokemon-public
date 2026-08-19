# Pokémon Mansion - Switch Matrix & Shutter Gate Log

## Overview
- Switches are located on Mewtwo statues. They toggle the states of electronic shutter gates globally across all floors.
- Standard state of gates has two modes: **DEFAULT (State A)** and **TOGGLED (State B)**.

## Switch Locations
- **1F:** No active switches verified (the statues on 1F appear to be decorative and do not open a dialogue).
- **2F:** Mewtwo statues located at `(12, 9)` and `(12, 11)` (east-central corridor). 
- **3F:** Mewtwo statue located near the stairs.
- **B1F:** Mewtwo statue switch located near the center-left.

## Gate Configurations by State

### DEFAULT STATE (State A)
- **2F stairs gate at `(5, 7)`:** **OPEN** (Allows direct access to 3F).
- **2F Column 11 gates:** **CLOSED** (Blocks access to the east-central room).
- **1F B1F stairs gate at `(22, 2)`:** **CLOSED** (Blocks B1F stairs).

### TOGGLED STATE (State B)
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **2F Column 11 gates:** **OPEN** (Allows access to the east-central room).
- **1F B1F stairs gate at `(22, 2)`:** **OPEN** (Allows access to B1F stairs).
- **B1F Secret Key Room:** **OPEN**.

## Traversal Options in Current State (State B)
Since the gates did not reset when we used DIG to leave the Mansion, they are currently locked in State B. We must find an accessible switch to flip the mansion back to State A.
- **2F West Side:** We can walk freely from `(7, 11)` stairs to the northwest diary room and southwest area, but there are no statues here.
- **2F East Side:** Blocked by Column 11 gates and Column 10 rubble.
- **3F:** Unreachable because the 2F stairs gate at `(5, 7)` is closed.
- **B1F:** Unreachable because the 1F stairs gate at `(22, 2)` is closed.
- **1F West/Center:** Accessible on foot from the entrance. We must explore the southwest of 1F to check if there is an active Mewtwo statue switch there.
## VERIFIED SPEEDRUN ROUTE (State B Skip) - Verified Turn 46787
- **Discovery:** The electronic gates in Pok�mon Mansion DO NOT reset when leaving the Mansion (either via DIG or front door). They remain in State B if they were toggled to State B.
- **State B Traversal:**
  - In State B, the 2F stairs gate at `(5, 7)` is CLOSED, blocking access to the 3F northwest room.
  - BUT we do not need to go to 3F at all!
  - In State B, the 1F B1F stairs gate at `(22, 2)` is OPEN.
  - This gate separates the 1F fenced-in room from the main 1F lobby.
  - Since the gate is OPEN, we can walk directly on foot into the fenced-in room on 1F, go down the stairs to B1F, and retrieve the Secret Key immediately!
  - On B1F, the Secret Key Room is OPEN in State B, so the key is completely unblocked!
- **Current Position:** We are on 1F at `(5, 10)`. We are walking south down the lobby to find the eastern corridor to reach the B1F stairs at `(22, 2)`.
