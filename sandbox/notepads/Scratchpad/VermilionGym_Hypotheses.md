# Vermilion Gym - Trash Can Switch Matrix & Empirical Trial Log

## Empirical Engine Analysis (Reconciled Turn 2461)
- 80+ repeated trials on a single empty can (9, 7) in place yielded 0 switch triggers.
- Conclusion: wFirstTrashCan is FIXED upon map entry / lock reset, and is NOT re-rolled by inspecting an empty can.
- Switch 1 resides in one specific trash can for the duration of the current search cycle.
- Once Switch 1 is triggered, Switch 2 is assigned to an adjacent can (North, South, East, or West).
- If Switch 2 fails, locks reset and a new Switch 1 is selected.

## Complete 15-Can Systematic Manual Sweep (Current Seed):
- Column 1: (1, 7), (1, 9), (1, 11)
- Column 3: (3, 7), (3, 9), (3, 11)
- Column 5: (5, 7), (5, 9), (5, 11)
- Column 7: (7, 7), (7, 9), (7, 11)
- Column 9: (9, 7), (9, 9), (9, 11)

## Action Plan:
- Systematically visit and manually interact with each can tile-by-tile.
- When Switch 1 text appears on screen ("Hey! There's a switch under the trash! Turn it on!"), immediately record its exact coordinate and inspect adjacent neighbor cans for Switch 2.
