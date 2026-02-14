# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2`: Conflicting results. (10, 6) reported OPEN once, CLOSED later.
  - **Hypothesis:** The Trap Warp at (15, 1) might reset switches (specifically Sw1).
- **Current Execution:**
  - Sequence Attempt: `3 -> 1 -> 2` (CLEAN RUN - No Traps).
  - Step 1: Turn Sw3 ON. (Done).
  - Step 2: Turn Sw1 ON. (Done).
  - Step 3: Turn Sw2 ON. (Done).

# Switch Status (After this turn)
- Sw1: ON (Verified)
- Sw2: ON (Just turned ON)
- Sw3: ON (Verified)
- Goal: Check Gate at (10, 6).