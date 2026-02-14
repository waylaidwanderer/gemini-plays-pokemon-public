# Warehouse Switch Puzzle - Recovery
- **Target State (Hypothesis):** [Sw3 OFF, Sw2 ON, Sw1 ON].
- **Current Task:** Entering Corridor.
- **Switch 3:** Verified OFF (Turn 42216) (Marker says ON - Conflict).
- **Switch 2:** Verified ON (Turn 42189).
- **Switch 1:** Verified ON (Turn 42238).
- **Status:** Shutter at (12, 8) is OPEN.
- **Next:** Check shutter at (6, 8).
- **Plan:** If (6, 8) closed, go to Switch 3. If open, go to Director.

## Plan
1. Move to Switch 1 (16, 2).
2. Verify/Set Sw1 to **ON**.
3. Go to (12, 8) and enter the corridor.
4. Go West to (6, 8) (Target Shutter).
5. Go South to Director.