# Vermilion Gym - Puzzle State & Strategy

## Current Search Status
- State: Sweeping cans for Switch 1 (Row 7 sweep in progress).
- Checked on current reset:
  - Can (9, 7): Empty
  - Can (7, 7): Empty
  - Can (5, 7): Empty
  - Next: Can (3, 7)

## Protocol When Switch 1 is Found
1. Note exact can coordinate (x, y).
2. Cleanly advance dialogue until text closes.
3. Immediately test an adjacent can in the 5x3 grid:
   - Up: (x, y-2)
   - Down: (x, y+2)
   - Left: (x-2, y)
   - Right: (x+2, y)
4. If Switch 2 is found -> Door unlocks permanently! Proceed to Lt. Surge.
5. If locks reset -> Resume systematic sweep for Switch 1.
