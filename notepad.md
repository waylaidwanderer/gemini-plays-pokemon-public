# Murkrow Solution: The Wall Bump Test

## Current Status
- P(21, 13). M(22, 12) [On Wall].
- Goal: Move M to (22, 14).

## Hypothesis
- **Mirror Y**: Pressing Up (Bump Wall) sends M Down.
- **Mimic Y**: Pressing Down (Move) sends M Down.

## Execution Plan
1. **Test Mirror Y (Bump Up)**:
   - Press **Up** (Bump Wall 21, 12).
   - If M moves to (22, 13): **Mirror Y Confirmed**.
     - Press **Up** again -> M moves to (22, 14). **SOLVED**.
   - If M moves to (22, 11) or stays: **Mimic Y Likely**.
     - Move **Left** to (20, 13).
     - Move **Down** to (20, 15) to drag M Down.