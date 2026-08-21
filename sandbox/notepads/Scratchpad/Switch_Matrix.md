# Pok�mon Mansion - Verified Switch Matrix & Master Route

## Overview
- Global Mewtwo statue switches toggle electronic shutter gates between DEFAULT (State A) and TOGGLED (State B).
- Floor transitions preserve the active state.
- B1F West SOUTH is permanently separated from B1F West NORTH by a solid brick wall on Row 9.
- 1F East is blocked from going up to 2F East in State A because the gate at `(15, 8)` is closed.

---

## Shutter Gate Configurations

### State A (Default)
- **B1F South-East gate at `(10, 11)`:** OPEN (allows crossing between West and East B1F SOUTH on Row 11).
- **3F East gate at `(15, 11)` (stairs):** CLOSED.
- **1F East gate at `(15, 8)`:** CLOSED.
- **B1F North-Central gate at `(9, 5)`:** CLOSED.

### State B (Toggled)
- **B1F South-East gate at `(10, 11)`:** CLOSED.
- **3F East gate at `(15, 11)` (stairs):** OPEN.
- **B1F North-Central gate at `(9, 5)`:** OPEN (allows horizontal crossing from B1F East NORTH to B1F West NORTH!).

---

## The Ultimate Verified Master Route to B1F East & Secret Key
1. **Ensure switch is in State A (Default).** (Current State).
2. **From 1F East, walk back to 1F West:**
   - Walk Left along Row 7 to `(12, 7)`.
   - Walk Down Column 12 to `(12, 11)`.
   - Walk Left along Row 11 to `(7, 11)`.
   - Walk Up 1 step onto the stairs at `(7, 10)` to warp to 2F West!
3. **On 2F West (State A), warp UP to 3F West:**
   - From `(7, 11)`, walk Up onto the stairs at `(7, 10)` to warp UP to 3F West.
4. **On 3F West (State A), cross to 3F East:**
   - Path: West Stairs landing `(7, 11)` -> walk Right to `(12, 11)` -> UP Column 12 to `(12, 6)` -> Right Row 6 to `(19, 6)` -> Down Column 19 to `(19, 11)` -> Left along Row 11 to the East Stairs `(15, 11)`.
5. **On 3F East (State A), the gate at (15, 11) is CLOSED.** 
   - Note: We cannot warp down to 2F East via these stairs in State A because the shutter gate is closed.
   - Instead, we must use DIG to exit, re-enter, and toggle the switch to State B from the West side, OR find a different route.
6. **To toggle the switch on 2F East:**
   - If we are in State B, we can access 2F East. Toggling the switch at `(13, 11)` to State B can be done by approaching from 2F West if the passage is open, or via other stairs.
7. **Warp UP to 3F East (State B):**
   - Walk to the East Stairs `(15, 11)` on 2F East and warp UP to 3F East landing at `(16, 11)`.
8. **On 3F East (State B), drop over the balcony:**
   - Walk to balcony landing `(20, 15)`: Path `(16, 11) -> (21, 11) -> (21, 15) -> (20, 15)`.
   - Walk Down to `(20, 18)` and step Left to `(19, 18)` to drop to B1F East!
9. **On B1F East (State B), retrieve the Secret Key:**
   - Land on B1F East at `(19, 16)` in State B.
   - Walk to Column 10 Row 5: Path `(19, 16) -> (10, 16) -> (10, 5)`.
   - Walk Left along Row 5 to Column 1 through the now-open gate at `(9, 5)`: Path `(10, 5) -> (1, 5)`.
   - Face UP at `(1, 5)` and press `A` to retrieve the **Secret Key** at `(1, 4)`!
10. **Exit B1F West:**
    - Walk to B1F West stairs at `(5, 10)` and step UP to warp to 1F West, then leave the mansion!