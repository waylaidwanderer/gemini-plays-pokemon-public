# Warehouse Switch Puzzle - Recovery
- **Target State:** [Sw3 OFF, Sw2 ON, Sw1 ON].
- **Current Task:** Adjusting Switch 3.
- **Current Position:** (4, 2) -> Moving to (2, 2).
- **Reason:** Grunt at (3, 2) blocks direct path.
- **Action:** Move around Grunt, interact with Sw3.
- **Next:** Verify Sw3 is OFF. Then check Sw1.

## Plan
1. Move to (2, 2) (Down, Left, Left, Up).
2. Interact with Switch 3.
3. If ON, turn OFF.
4. Move to Switch 1 (16, 2).
5. Verify Sw1 is ON.
6. Go to (12, 8).