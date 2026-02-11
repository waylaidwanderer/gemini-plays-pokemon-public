# Murkrow Solution: Search & Rescue (Again)

## Current Status
- P(20, 13). M is **LOST**.
- NOT at (19, 13), (19, 12), (22, 14), (20, 12).
- Possible Locations: (21, 12) (Maybe invisible?), (22, 12), (23, 12)? Or Reset to (7, 1).

## Execution
1. **Move Down**:
   - To (20, 14).
   - Check if M appears.
2. **Search**:
   - If not found, check Door at (23, 14).
   - If Door closed and M missing, go to (3, 14) -> Reset Room.