# Warehouse Switch Puzzle - Strategy
- Clue: "The switch on the end is the one to press first."
- Interpretation: Switch 3 (Left End) is the correct start. Switch 1 (Right End) led to a trap.
- Current State: Switch 3 ON, Switch 2 ON, Switch 1 OFF (Transitioning).
- Objective: Isolate the correct path by eliminating the Trap Path (Switch 1).

## Trap Registry
- (12, 9): Warps to (12, 5). Avoid!

## Plan
1. Confirm Switch 1 is OFF.
2. Navigate to Shutter 2 at (6, 8).
3. Check status.
   - If OPEN: Proceed to Director.
   - If CLOSED: Turn Switch 2 OFF (Testing "Only Switch 3" hypothesis).