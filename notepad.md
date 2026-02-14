# Underground Warehouse
- **Goal:** Rescue Director.
- **Status:**
  - Sw3: ON.
  - Sw2: OFF (Verified).
  - Sw1: ON.
- **New Hypothesis:**
  - Sw2 OFF -> (16, 6) OPEN.
  - Sw1 ON -> (16, 7) & (12, 8) OPEN.
  - Path: (10, 2) -> (16, 2) -> South to (16, 8) -> West to (12, 8) -> South to Director.
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