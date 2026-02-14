# Warehouse Switch Puzzle - Solution Testing
- Critical Correction: Switch 3 was OFF when I thought it was ON.
- Current State: Sw1 ON, Sw2 OFF, Sw3 OFF.
- Observation: (3, 6) is CLOSED.
- Implication: This combo is wrong.
- New Hypothesis: Since I haven't actually tested Sw3 ON yet, maybe that's the key.
- Target State: [Sw1 ON, Sw2 OFF, Sw3 ON].

## Plan
1. Go to Switch 3 (2, 1).
2. Turn Switch 3 ON.
3. Check Shutter (3, 6) again.
4. If Closed, I might need to reset all to OFF and follow the clue "Switch on the end first".