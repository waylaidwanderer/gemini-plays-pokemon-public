# Underground Warehouse
- **Goal:** Rescue Director.
- **Action:** Turning Sw3 ON.
- **Correction:** Path blocked by Grunt at (3,2). Detouring via Row 3.
- **Path:** (4,2) -> Down -> Left -> Left -> Up -> (2,2).
- **Strategy: The "Inside Job" (Execution)**
  - **Findings:** Gate (10,10) CLOSED. Gate (2,6) OPEN.
  - **Deduction:** Current State is [OFF, OFF, OFF].
  - **Goal:** Set State to [OFF, OFF, ON].
  - **Important:** Row 4 connects all switch rooms. (15,4) is a TRAP.
  - **Plan:**
    1. Turn Switch 3 ON.
    2. Use `check_gate_states` to confirm [OFF, OFF, ON] effects.
    3. If (10,10) opens, find open entry gate ((2,6), (10,6), or (16,6)) via Row 4.