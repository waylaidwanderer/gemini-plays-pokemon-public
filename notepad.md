# Underground Warehouse Strategy
- **Clue:** "The switch on the end is the one to press first."
- **Tested Sequences & Results:**
  - `3 -> 1 -> 2`: Conflicting results. (10, 6) reported OPEN once, CLOSED later.
  - **Hypothesis:** The Trap Warp at (15, 1) might reset switches (specifically Sw1).
- **Current Execution:**
  - Sequence Attempt: `3 -> 1 -> 2` (CLEAN RUN - No Traps).
  - Step 1: Turn Sw3 ON. (Doing now).
  - Next: Turn Sw1 ON.
  - Next: Turn Sw2 ON.

# Switch Status (After this turn)
- Sw1: OFF (Verified)
- Sw2: OFF (Verified)
- Sw3: ON (Just turned ON)
- Goal: Execute `3 -> 1 -> 2`. Avoid Traps!