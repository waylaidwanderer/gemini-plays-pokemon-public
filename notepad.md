# Murkrow Puzzle: Navigation via Overlap

## Current State
- P(2, 1). M(2, 1).
- **Strategy**: Top Corridor Express (Row 3).
- **Observation**: Row 3 is a clear corridor from Col 2 to Col 21. Avoids all traps and blocked columns.

## Execution Plan
1. **Access Top Corridor**:
   - Move Down to (2, 3).
   - **Result**: P(2, 3), M(2, 3).
2. **Traverse East**:
   - Move Right to (21, 3).
   - **Result**: P(21, 3), M(21, 3).
3. **Approach Door**:
   - Move Down to (21, 13).
   - Move Right to (22, 13).
   - **Interact**: Overlapped or Sidekick.

## Immediate Action
- Move Down to (2, 3).