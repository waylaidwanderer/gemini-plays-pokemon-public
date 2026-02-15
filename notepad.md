# Underground Warehouse
- **Goal:** Rescue Director.
- **Hypothesis:** Need to open Gate (6,8) or (12,8) to cross to the back.
- **Truth Table (Entry | Cross | Exit):**
  - [000] (OFF,OFF,OFF): 2-6 | 6-8 | 16-10 (Recall)
  - [111] (ON,ON,ON): 2-6, 10-6 | - | 16-10
  - [110] (ON,ON,OFF): 10-6 | 6-8 | 16-10 (Dead End: Left+Mid)
  - [100] (ON,OFF,OFF): Testing Now.
- **Correction:** Accidentally spoke to Grunt instead of Switch 2. Sw2 is still ON.
- **Plan:**
  1. Finish dialogue.
  2. Turn Sw2 OFF (State: [100]).
  3. Check Gate States.
  4. If fail, Turn Sw1 OFF -> [000].
- **Grunt Hint:** "The switch on the end is the one to press first, but... I forgot which end..."
- **Interpretation:** Sequence starts with End Switch.
  - Test 1: Reset -> Sw1 (Right End). State: [ON, OFF, OFF]. (Current Target)
  - Test 2: Reset -> Sw3 (Left End). State: [OFF, OFF, ON].
- **Status:** Sw1 OFF, Sw2 OFF, Sw3 OFF. ([0,0,0])
- **Verified Results:**
  - [0,0,0] (OFF,OFF,OFF): All Entries CLOSED.
  - [1,0,0] (ON,OFF,OFF): All Entries CLOSED.
  - [1,1,0] (ON,ON,OFF): 10-6 Open (Mid Entry). 6-8 Open. Stuck in Mid.
  - [0,1,1] (OFF,ON,ON): 2-6 Open (Left Entry). 6-8 Open. Stuck in Mid.
- **Deduction:** Sw1 First (Right) failed. Hint says "End Switch First".
- **Plan:**
  1. Go to Sw3 (2,2).
  2. Turn Sw3 ON -> State [0,0,1].
  3. Check Gates. Hoping for 2-6 Open & 12-8 Open (or 16-6 Open).