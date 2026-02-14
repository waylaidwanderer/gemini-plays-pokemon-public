# Underground Warehouse
- **Goal:** Rescue Director.
- **Status:**
  - Sw3: ON.
  - Sw2: ON (Target: Turn OFF).
  - Sw1: ON.
- **New Hypothesis:**
  - Need Sw2 OFF to OPEN (16, 6).
  - Need Sw1 ON to OPEN (16, 7) & (12, 8).
  - Path: Sw2(OFF) -> Go to Col 16 -> Down (16, 6 is open) -> Down (16, 7 is open) -> West to (12, 8) -> South.
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