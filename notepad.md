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
- **Status:** Sw1 ON, Sw2 OFF, Sw3 OFF. ([ON, OFF, OFF])
- **Plan:**
  1. Verify [ON, OFF, OFF] gates.
  2. Navigate to Sw1 (16,1).
  3. Turn Sw1 OFF (Reset to [0,0,0]).
  4. Verify [0,0,0] gates.
  5. If [0,0,0] opens full path (2-6 -> 6-8 -> 12-8 -> 16-10), EXECUTE.