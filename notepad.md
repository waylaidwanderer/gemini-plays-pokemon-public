# Underground Warehouse
- **Goal:** Rescue Director (Likely in Bottom Right).
- **Grunt Hint:** "The switch on the end is the one to press first." (Implies Sw1 or Sw3).
- **Current State:** [1,1,1] (All ON).
- **Discovery:** Gate (2,6) OPEN.
- **Hazard:** Reaching (3,8) caused a reset to (3,5). Suspect Trap Warp at (2,8) or (3,8).
- **Hazard:** Reaching (10,9) caused a reset to (10,5). Suspect Trap Warp at (10,9).
- **Plan:**
  1. Navigate around (10,9) via column 9.
  2. Check Gate (10,10).
  3. If closed or trapped, try Left Path [1,0,1] or reset to [0,1,0].
- **Plan:**
  1. Check Gates for [0,1,0].
  2. If Gate 12-8 (Right Cross) or 10-6 (Mid Entry) opens, investigate.
  3. If fail, reconsider [0,1,1] pathing (Left -> Mid) or [1,0,1].
  - [001] (OFF,OFF,ON): 2-6(L) Open. 10-6(M) Closed. 16-6(R) Closed.
  - [010] (OFF,ON,OFF): ?
  - [011] (OFF,ON,ON): 2-6(L) | 6-8(L) | - (Stuck Left).
  - [100] (ON,OFF,OFF): 16-6(R) Closed. Checking Mid/Left.
  - [101] (ON,OFF,ON): All Entry Gates (2,6|10,6|16,6) Open. Navigating Mid.
  - [110] (ON,ON,OFF): 10-6(M) | 6-8(L) | - (Stuck Mid/Left).
  - [111] (ON,ON,ON): 2-6(L) Open. 10-6(M) Closed. 16-6(R) Open.
- **Analysis:** [1,1,1] opens the Right Gate!
- **Hazard:** Reaching (16,8) caused a reset.
- **Hazard:** Reaching (17,8) or (17,9) caused a reset to (17,5). Suspect Trap Zone.
- **CORRECTION:** Tool reversed types. [3fe2=OPEN], [2889=CLOSED].
- **Current State:** [0,1,1] (OFF, ON, ON).
- **Gate States:**
  - Entry: Left(Closed), Mid(OPEN), Right(Closed).
  - Inner: Left(Closed), Mid-Cross(OPEN), Right-Cross(OPEN).
  - Exit: Left(Closed), Mid(Closed), Right(OPEN).
- **Plan:**
  1. Enter Mid Gate (10, 6).
  2. Go Right thru Gate (12, 8).
  3. Navigate to Right Exit (16, 10). (Hope Sw1 OFF disabled trap at 16,8).
- **Map Locations:**
  - Sw3 (Left): (2,1)
  - Sw2 (Mid): (10,1)
  - Sw1 (Right): (16,1)
  - Trap: (15,4)