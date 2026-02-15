# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Need to open Gate (6,8) or (12,8) to cross to the back.
- **Truth Table (Entry | Cross | Exit):**
  - [000] (OFF,OFF,OFF): 2-6 | 6-8 | 16-10 (Recall)
  - [001] (OFF,OFF,ON): 2-6 | - | 16-10
  - [011] (OFF,ON,ON): 2-6 | - | 16-10
  - [101] (ON,OFF,ON): 2-6 | - | 16-10
  - [111] (ON,ON,ON): 2-6, 10-6 | - | 16-10
  - [110] (ON,ON,OFF): Testing Now.
- **Plan:**
  1. Turn Sw3 OFF (State: [110]).
  2. Check Gate States.
  3. If no progress, try [100] (Sw2 OFF) or [010] (Sw1 OFF).