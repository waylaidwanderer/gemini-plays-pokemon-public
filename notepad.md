# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Need to open Gate (6,8) or (12,8) to cross to the back.
- **Truth Table (Entry | Cross | Exit):**
  - [000] (OFF,OFF,OFF): 2-6 | 6-8 | 16-10 (Recall)
  - [111] (ON,ON,ON): 2-6, 10-6 | - | 16-10
  - [110] (ON,ON,OFF): 10-6 | 6-8 | 16-10 (Dead End: Left+Mid)
  - [100] (ON,OFF,OFF): Testing Now.
- **Plan:**
  1. Turn Sw2 OFF (State: [100]).
  2. Check Gate States.
  3. If fail, Turn Sw1 OFF -> [000].