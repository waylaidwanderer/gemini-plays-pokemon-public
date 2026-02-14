# Underground Warehouse
- **Goal:** Rescue Director.
- **Status:**
  - Sw3: ON.
  - Sw2: OFF (Map shows (2, 6) OPEN, (16, 6) CLOSED).
  - Sw1: ON.
  - (12, 8) is CLOSED (Wall).
  - (2, 10) is CLOSED (Wall).
- **New Plan:**
  1. Toggle Sw3 (Target: Open (2, 10)).
  2. If (2, 10) opens, go South along x=2 to Director.
- **Mechanics (Verified XML):**
- **Plan:**
  1. Turn Sw2 OFF.
  2. Go to Sw1 area.
  3. Walk South along x=16.
- **Mechanics (Verified XML):**
  - Sw3 ON: Opens (16, 10), Closes (6, 8).
  - Sw2 ON: Opens (2, 6), Closes (16, 6).
  - Sw1 ON: Opens (16, 7) & (12, 8).
- **Gate Check:**
  - (2, 10): Closed with ALL ON.
- **Plan:**
  1. Turn Sw3 ON (In Progress).
  2. Go to Sw2 (10, 1).
  3. Turn Sw2 ON.
  4. Go to Sw1 (16, 1).
  5. Turn Sw1 ON.
- **Hypothesis:** "End is the one to press first" -> Start with 3 or 1.
- **Reminder:** Bag is full.
- **Success:**
  - Sw2 OFF opened (16, 6).
  - Path confirmed: South to (16, 7), then West to (12, 7), then South through (12, 8).