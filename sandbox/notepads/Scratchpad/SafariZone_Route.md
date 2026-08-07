# Safari Zone - Active Path Routing

## Current Run Status
- **Current Position:** `(12, 7)` (Stairs)
- **Steps Taken:** 269
- **Steps Remaining:** 231

## Live Route & Goal
Our goal is to reach Area 2 (North) transition at `(0, 5)`.
Row 6 has a solid tree line from Column 0 to Column 9, but we suspect there is a walkable gap or staircase at Column 6 on Row 6.

### Next Planned Segment (Descend and Walk to Column 6)
1. **Descend the Stairs:** Stand at `(12, 7)` and walk `Down` to `(12, 8)` (ground level) -> 1 step.
2. **Walk Left to Column 6:** Walk `Left` from `(12, 8)` to `(6, 8)` (ground level) -> 6 steps.
3. **Walk Up to Row 7:** Walk `Up` to `(6, 7)` -> 1 step.
4. **Test the Gap at (6, 6):** Walk `Up` to `(6, 6)` (suspected gap) -> 1 step.
5. **Proceed to Row 5:** If gap is open, walk `Up` to `(6, 5)` -> 1 step.
6. **Walk to Area 2:** Walk `Left` along Row 5 to Column 0 to trigger transition -> 6 steps.

### Expected Step Budget for Transition
- Steps from `(12, 7)` to `(0, 5)`: 16 steps total.
- Expected Steps Taken upon entering Area 2: 269 + 16 = 285.
