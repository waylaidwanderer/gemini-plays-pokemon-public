# Murkrow Solution: The Blind Ratchet (Mirror Y)

## Current Status
- P(21, 13). M(22, 12) [Likely].
- Assumption: **Mirror Y** (based on Wiggle Test).
- Goal: M(22, 14).

## Execution Plan
1. **Move Left** to (20, 13).
   - M tries Left (21, 12) [Wall]. Stays (22, 12).
   - State: P(20, 13), M(22, 12).

2. **Move Up** to (20, 12).
   - M moves Down (Mirror) to (22, 13).
   - State: P(20, 12), M(22, 13).

3. **Move Up** to (20, 11).
   - M moves Down (Mirror) to (22, 14) [Plate].
   - **Door Opens**.

## Verification
- If Door fails to open, check M location.
- If M at (22, 10) or (22, 11), it was Mimic Y.
- Reverse and try Down.