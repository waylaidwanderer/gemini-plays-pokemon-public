# Pokémon Mansion - Switch Matrix & Shutter Gate Log

## Overview
- Mewtwo statues act as secret switches toggling global electronic shutter gates between DEFAULT (State A) and TOGGLED (State B).
- Changing floors preserves the active switch state.

## Shutter Gate Configurations

### State A (Default)
- **3F shutter gates at (18, 8) and (19, 8):** OPEN.
- **B1F South-East gate at (10, 11):** OPEN (allows crossing between B1F East and West on Row 11).
- **3F gate at (20, 5) and (21, 5):** CLOSED.
- **3F East gate at (15, 11) (stairs):** CLOSED.

### State B (Toggled)
- **3F shutter gates at (18, 8) and (19, 8):** CLOSED.
- **B1F South-East gate at (10, 11):** CLOSED.
- **3F gate at (20, 5) and (21, 5):** OPEN.
- **3F East gate at (15, 11) (stairs):** OPEN.
- **B1F North-Central gate at (9, 5):** OPEN.
- **B1F West gates on Columns 3 & 4 (North-South):** OPEN (bypasses Row 9 solid brick wall).
- **Secret Key Room at (1, 4):** OPEN.

---

## The Two Master Victory Routes to B1F & Secret Key

### Route 1: The State A Pit Drop Route (Recommended)
1. Ensure switch is in **State A** (Default).
2. Walk to the East side of 3F:
   - Path: West Stairs landing at `(7, 11)` -> walk Right to `(12, 11)` -> UP Column 12 to `(12, 6)` -> Right Row 6 to `(19, 6)` (bypasses solid wall Column 14!) -> Down Column 19 to `(19, 11)` -> Right Row 11 to `(21, 11)`.
3. From `(21, 11)`, walk LEFT Row 11 to Column 11:
   - Path: `(21, 11) -> (11, 11)` (Row 11 is completely open in State A!).
4. From `(11, 11)`, walk UP Column 11 to Row 3:
   - Path: `(11, 11) -> (11, 3)` (Column 11 is completely open vertically!).
5. Walk Right along Row 3 to Column 26:
   - Path: `(11, 3) -> (26, 3)` (Row 3 is completely open, bypassing all Row 4-7 rubble!).
6. Walk Down Column 26 to Row 6:
   - Path: `(26, 3) -> (26, 6)`.
7. Walk Left 1 step onto the pit at `(25, 6)` to drop through to 1F inside the fenced area!
8. On 1F, walk UP onto the stairs at `(7, 10)` to warp DOWN to B1F East SOUTH landing at `(7, 10)` or `(7, 11)`.
9. On B1F East SOUTH, walk Left to B1F West SOUTH via Row 11 (open in State A).
10. Walk to the B1F West Mewtwo switch at `(2, 11)` (accessed from `(2, 12)`) and toggle to **State B**!
11. Walk UP Column 4 through the now-open gates to B1F West NORTH, walk Left to `(1, 5)` facing UP, and retrieve the **Secret Key** at `(1, 4)`!

### Route 2: The State B Pit Drop Route (Alternative)
1. Ensure switch is in **State B** (Toggled).
2. Walk on 3F from `(2, 12)` to `(11, 10)` -> UP Column 11 to Row 6 -> Right on Row 6 to `(21, 6)`.
3. Walk UP Column 21 through open gate `(21, 5)` to Row 3:
   - Path: `(21, 6) -> (21, 3)` (gate is open in State B!).
4. Walk Right Row 3 to Column 26:
   - Path: `(21, 3) -> (26, 3)`.
5. Walk Down Column 26 to Row 6:
   - Path: `(26, 3) -> (26, 6)`.
6. Step Left onto pit at `(25, 6)` to drop to 1F inside the fenced area!
7. On 1F, walk UP onto the stairs at `(7, 10)` to warp DOWN to B1F East SOUTH.
8. On B1F East SOUTH (State B), walk UP Column 19 to Row 5, and walk Left through the open gate at `(9, 5)` to B1F West NORTH.
9. Retrieve the **Secret Key** at `(1, 4)`!
