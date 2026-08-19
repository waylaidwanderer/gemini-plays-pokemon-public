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
- **2F Column 11 gates:** **OPEN** (Allows access to the east-central room).
- **1F B1F stairs gate at `(22, 2)`:** **CLOSED** (Blocks B1F stairs).

### TOGGLED STATE (State B) (Current State)
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **2F Column 11 gates:** **CLOSED** (Blocks access to east-central statues).
- **1F B1F stairs gate at `(22, 2)`:** **CLOSED** (Wait, is it closed? Yes, we verified it blocked).
- **B1F Secret Key Room:** **OPEN**.

## Traversal Options in Current State (State B)
Since the gates did not reset when we used DIG to leave the Mansion, they are currently locked in State B. We must find an accessible switch to flip the mansion back to State A.
- **2F West Side:** We can walk freely from `(7, 11)` stairs to the northwest diary room and southwest area, but there are no statues here.
- **2F East Side:** Blocked by Column 11 gates and Column 10 rubble.
- **3F:** Unreachable because the 2F stairs gate at `(5, 7)` is closed.
- **B1F:** Unreachable because the 1F stairs gate at `(22, 2)` is closed.
- **1F West/Center:** Accessible on foot from the entrance. We must explore the southwest of 1F to check if there is an active Mewtwo statue switch there.