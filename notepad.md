# Warehouse Switch Puzzle - Strategy
- Trap: (12, 9) warps to (12, 5).
- Current Status: Switch 1 ON, Switch 3 ON, Switch 2 ON (Just toggled).
- Shutter Status: (12, 8) Open (Trap path), (6, 8) Pending Check.
- Goal: Check Shutter 2 (6, 8).

## Plan
1. Confirm Switch 2 is ON.
2. Navigate to (6, 8).
3. If Shutter 2 is Open, check (6, 9) for traps.
4. If (6, 9) is safe, proceed to Director (9, 12).
5. If Shutter 2 Closed, try turning Switch 1 OFF.