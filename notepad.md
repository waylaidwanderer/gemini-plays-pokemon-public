# Underground Warehouse
- **Goal:** Rescue Director (Likely in Bottom Right).
- **Grunt Hint:** "The switch on the end is the one to press first." (Implies Sw1 or Sw3).
- **Current State:** [1,0,0] (Sw1 ON).
- **Hypothesis:** "End Switch" = Right End (Sw1).
- **Truth Table (Entry | Cross | Exit):**
  - [000] (OFF,OFF,OFF): All Closed (Verified).
  - [100] (ON,OFF,OFF): Testing Now.
  - [001] (OFF,OFF,ON): All Closed (Verified).
- **Plan:**
  1. Check Gates for [1,0,0].
  2. If Entry (16,6) or Cross (12,8) Opens, GO!
  3. If fail, then "End Switch First" might mean sequential (Sw1 -> Sw2...).
  - [001] (OFF,OFF,ON): Closed.
  - [010] (OFF,ON,OFF): ?
  - [011] (OFF,ON,ON): 2-6(L) | 6-8(L) | - (Stuck Left).
  - [100] (ON,OFF,OFF): ? (Target).
  - [101] (ON,OFF,ON): 2-6(L) | - | 16-10(R).
  - [110] (ON,ON,OFF): 10-6(M) | 6-8(L) | - (Stuck Mid/Left).
  - [111] (ON,ON,ON): 2-6,10-6 | - | 16-10.
- **Analysis:** No combination so far opens Gate 12-8 (Right Cross) or 16-6 (Right Entry).
- **Plan:**
  1. Reset to [0,0,0].
  2. Test [1,0,0] (Sw1 First).
  3. If [1,0,0] fails, Test [0,1,0].
- **Map Locations:**
  - Sw3 (Left): (2,1)
  - Sw2 (Mid): (10,1)
  - Sw1 (Right): (16,1)
  - Trap: (15,4)