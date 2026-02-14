# Underground Warehouse Strategy
- **Current Status:** [Sw3 ON, Sw2 ON]. Gate (12, 8) CLOSED.
- **Problem:** Need [Sw3 OFF, Sw2 ON] to open (12, 8), but cannot reach Sw3 (Gate 2, 6 Closed).
- **Plan:**
  1. Toggle Sw2 OFF.
  2. Check if (2, 6) Opens (to access Sw3) and (10, 6) stays Open (to exit Sw2 room).
  3. If trapped, toggle Sw2 ON immediately.
  4. If (2, 6) opens, go to Sw3 -> Turn OFF. Then return to Sw2 -> Turn ON.
- Suspicion: Did I cancel the toggle in Turn 43452 with 'B'?
- Checking Switch 2 text now.
- If ON -> Turn OFF.
- If OFF -> Leave OFF.
- Goal: Reset all to OFF.