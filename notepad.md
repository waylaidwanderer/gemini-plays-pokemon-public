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
- **Status:** Sw1 OFF, Sw2 OFF, Sw3 ON. ([0,0,1])
- **Hypothesis:** This is the correct "First Move" (Left End Switch).
- **Plan:**
  1. Verify Gates for [0,0,1].
  2. If Entry (2-6) is Open, check for Cross (12-8 or 6-8).
  3. If this opens the path, navigate to Director.