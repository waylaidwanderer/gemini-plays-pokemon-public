# Murkrow Solution: The Wiggle Test

## Current Status
- P(20, 13). M(18, 13) [Calculated].
- Goal: Determine Y-Axis Behavior (Mimic vs Mirror).

## Execution
1. **Move Down**:
   - P moves to (20, 14).
   - **Observe M**:
     - If M moves to (18, 14): **Mimic Y**.
     - If M stays at (18, 13): **Mirror Y** (Blocked by Wall 18,12).

## Contingency Plans
- **Case Mirror Y (Likely)**:
  1. P(20, 14), M(18, 13).
  2. Move Right to (22, 14). M -> (20, 13).
  3. Bump Right x2 (on Door). M -> (22, 13).
  4. Move Up to (22, 13). M -> (22, 14) [Plate].
  5. Enter Door.
- **Case Mimic Y**:
  1. P(20, 14), M(18, 14).
  2. Needs replanning to align M above Plate.