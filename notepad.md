# Warehouse Switch Puzzle - Solution Testing
- State: Sw1 ON, Sw2 OFF, Sw3 ON (Turning ON now).
- Hypothesis: Switch 3 ON opens (3, 6).
- Logic: "Switch on the end first" -> Sw3. Sw2 OFF prevents (3, 6) closure. Sw1 ON keeps (6, 8) open.
- Route: Check (3, 6). If Open -> South -> East -> Director.

## Plan
1. Turn Switch 3 ON (Press A multiple times).
2. Move to (3, 5).
3. Check Shutter (3, 6).
4. If Open, proceed. If Closed, I am officially confused.