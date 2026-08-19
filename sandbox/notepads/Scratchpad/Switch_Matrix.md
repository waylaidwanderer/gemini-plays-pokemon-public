# Pokémon Mansion - Switch Matrix & Shutter Gate Log

## Overview
- Switches are located on Mewtwo statues. They toggle the states of electronic shutter gates globally across all floors.
- Standard state of gates has two modes: **DEFAULT (State A)** and **TOGGLED (State B)**.

## Switch Locations
- **1F:** No active switches verified (the statues on 1F appear to be decorative).
- **2F:** Mewtwo statues located at `(12, 9)` and `(12, 11)` (east-central corridor). 
- **3F:** Mewtwo statue located near the stairs.
- **B1F:** Mewtwo statue switch located near the center-left.

## Gate Configurations by State

### DEFAULT STATE (State A)
- **1F B1F stairs gate at `(22, 2)`:** **OPEN** (Allows access to B1F stairs).
- **2F stairs gate at `(5, 7)`:** **OPEN** (Allows direct access to 3F).
- **2F Column 11 gates:** **CLOSED** (Blocks access to the east-central room).
- **3F gate at `(21, 5)`:** **OPEN** (Allows access to the north side and the (22, 6) pit).

### TOGGLED STATE (State B)
- **1F B1F stairs gate at `(22, 2)`:** **CLOSED** (Blocks B1F stairs).
- **2F stairs gate at `(5, 7)`:** **CLOSED** (Blocks Column 5).
- **2F Column 11 gates:** **OPEN** (Allows access to the east-central room).
- **3F gate at `(21, 5)`:** **CLOSED** (Blocks access to the north side and the (22, 6) pit).
- **B1F Secret Key Room:** **OPEN**.

## Refuted Hypotheses & State B Skip
- **"State B Speedrun" Hypothesis (Refuted):** We hypothesized that since the 1F B1F stairs gate at `(22, 2)` is open in State B, we could walk directly on foot from the west entrance/lobby to the B1F stairs on 1F.
- **Collision Proof (Turns 46797-46799):** We attempted to cross from column 10 to column 12 on foot at 1F rows 18, 22, and 26. We bumped and were completely blocked on all tested rows. Column 11 forms a solid, continuous vertical wall on 1F that divides the west lobby from the east side. Horizontal crossing on foot is physically impossible on 1F.
- **Mansion Reset Mechanic:** Leaving the building to Cinnabar Island **DOES reset the gates to State A (Default)**.
- **Standard Routing:**
  1. Enter Mansion (State A).
  2. Walk UP column 5 on 1F, step onto (5, 10) stairs to warp to 2F.
  3. On 2F, walk UP column 5 through the open (5, 7) gate, step onto (5, 10) stairs to warp to 3F.
  4. On 3F, walk east to (22, 6) pit and fall to 2F.
  5. On 2F, fall down to 1F fenced-in room.
  6. Go down B1F stairs, flip switch to State B to open Secret Key Room, and retrieve the Secret Key.
