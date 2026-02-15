# Underground Warehouse
- **Goal:** Rescue Director (Likely in Bottom Right).
- **Grunt Hint:** "The switch on the end is the one to press first." (Implies Sw1 or Sw3).
- **Current State:** [0,0,1] (Sw3 ON).
- **Discovery:** Gate (2,6) OPEN.
- **Hazard:** Reaching (3,8) caused a reset to (3,5). Suspect Trap Warp at (2,8) or (3,8).
- **Plan:**
  1. Move to (2,8).
  2. If safe, check Gate (2,10) and Silver (4,8).
  3. If warped, mark trap and try another path.
- **Plan:**
  1. Check Gates for [0,1,0].
  2. If Gate 12-8 (Right Cross) or 10-6 (Mid Entry) opens, investigate.
  3. If fail, reconsider [0,1,1] pathing (Left -> Mid) or [1,0,1].
  - [001] (OFF,OFF,ON): 2-6(L) Open. 10-6(M) Closed. 16-6(R) Closed.
  - [010] (OFF,ON,OFF): ?
  - [011] (OFF,ON,ON): 2-6(L) | 6-8(L) | - (Stuck Left).
  - [100] (ON,OFF,OFF): 16-6(R) Closed. Checking Mid/Left.
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