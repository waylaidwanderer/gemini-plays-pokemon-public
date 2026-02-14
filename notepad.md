# Warehouse Switch Puzzle - Wall Check
- **Status:** At (9, 9). Path South looks blocked by (9, 10).
- **Hypothesis:** Row 10 is a wall. Need to find an opening.
- **Next Test:** Check [Sw3 OFF, Sw2 ON, Sw1 ON]. (Previous test 42156 showed (6,8) open, might allow access to (6,10)).

## Plan
1. Attempt to move South to (9, 10).
2. If blocked, move back to Switches.
3. Set State: Sw3 OFF, Sw2 ON, Sw1 ON.
4. Enter via (12, 8) -> West to (6, 8) -> South.