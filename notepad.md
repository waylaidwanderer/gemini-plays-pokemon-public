# Team Rocket HQ - Murkrow Puzzle

## STATUS: EXECUTING "SHUTTER CHECK"
**Goal**: Verify if Shutter at (15, 10) is Open.
**Reason**: Access to Boss Area requires Shutter.

## Step 1: Navigate to Shutter (Safe Path)
1. **Ratchet M Up**:
   - P(4, 8). M(6, 2).
   - Up 6. P(4, 2).
   - M Down 6 -> Blocked at (6, 4) Wall. M stops at (6, 3).
   - *State*: P(4, 2), M(6, 3).
2. **Move to Center**:
   - Right 11. P(15, 2). M(17, 3).
3. **Check Shutter**:
   - Down 8. P(15, 10) [Shutter].
   - M Up 8 -> Blocked at top. M stops at (17, 0).

## Step 2: Decision
- **If P passes (15, 10)**: Shutter is OPEN. Proceed to "SHUTTER ENTRY" Strategy.
- **If P bumps**: Shutter is CLOSED. Navigate to Switch (19, 11) via Right Side, Toggle, Reset.