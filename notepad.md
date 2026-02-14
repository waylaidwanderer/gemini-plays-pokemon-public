# Underground Warehouse
- **Goal:** Rescue Director.
- **Status:**
  - Sw3: ON (Target: Turn OFF).
  - Sw2: OFF.
  - Sw1: ON.
  - (2, 6) is CLOSED (Wall in XML).
  - (2, 10) is CLOSED (Wall in XML).
- **Correction:**
  - Previous note about (2, 6) being OPEN was false. XML shows Wall.
  - Previous note about (12, 8) being OPEN was false. XML shows Wall.
- **Plan (Reset & Retry):**
  1. Turn Sw3 OFF.
  2. Go to Sw1 and Turn OFF (Reset all to OFF).
  3. Try Sequence: Sw3 -> Sw2 -> Sw1.
  4. If that fails, try Sw1 -> Sw2 -> Sw3.
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