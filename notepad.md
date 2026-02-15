# Underground Warehouse
- **Goal:** Rescue Director.
- **Tool Analysis [1,0,1]:**
  - Mid Entry (10,6): OPEN (3fe2).
  - Cross (12,8): OPEN (3fe2).
  - Exit (16,10): CLOSED (2889).
  - Conclusion: [1,0,1] is a Safe Path to a Locked Door.
- **Plan:**
  1. Go to Switch 2 (10,1).
  2. Turn Sw2 ON -> [1,1,1].
  3. Check Exit Gate status with Tool.
  4. If Exit OPEN, check entry/cross gates for a safe route.
- **Reflection (Turn 44555):**
  - Confirmed State [1,0,1] (Sw1 ON, Sw2 OFF, Sw3 ON):
  - Cross Gate (12,8) OPEN.
  - Wall (12,9) OPEN.
  - Gate 3 (16,6) CLOSED.
  - Exit (16,10) CLOSED.
- Current State: [1,1,?] (Sw1 ON, Sw2 ON, Sw3 Unknown).
- Goal: Determine Sw3 state and toggle it.
- Hypothesis:
  - If Sw3 is ON -> Current is [1,1,1] (All Closed). Toggle to [1,1,0].
  - If Sw3 is OFF -> Current is [1,1,0]. Toggle to [1,1,1].
- Clue: "The switch on the end is the one to press first."
  - Could mean Sw3 or Sw1. Sw1 didn't solve it. Trying Sw3.
- Verified States:
  - [1,0,1] (Assumed Sw3 ON): Opens (12,8) and (12,9). Closed (16,6) and (16,10).