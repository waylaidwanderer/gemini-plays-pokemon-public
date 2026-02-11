# Murkrow Solution: Verification Phase

## Current State
- P(22, 16).
- M Last Known: (22, 14) [Calculated].
- Note: M attempted to move to (22, 15) but it is a Wall. Thus, M should have stayed at (22, 14) [The Plate].

## Execution Plan
1. **Check Door**:
   - Move **Right** to (23, 16).
   - Look North at (23, 14).
   - If Open -> **ENTER**.
   - If Closed -> M is desynced. Search.