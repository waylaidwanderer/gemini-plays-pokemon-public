# Vermilion Gym - Trash Can Switch Matrix & Trial Log

## Puzzle Mechanics Analysis
- 15 trash cans arranged in a 3x5 grid:
  - Row 7: (1, 7), (3, 7), (5, 7), (7, 7), (9, 7)
  - Row 9: (1, 9), (3, 9), (5, 9), (7, 9), (9, 9)
  - Row 11: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11)
- Verified: `wFirstTrashCan` is fixed per map initialization. If rolled out-of-bounds on map entry, no can will open.
- Strategy: Step outside to Vermilion City via (4, 17) and immediately re-enter to initialize a fresh `wFirstTrashCan` value.

## Active Run Protocol (Re-roll Map Init):
1. Step out to Vermilion City at (4, 17).
2. Step Up into Vermilion Gym.
3. Check (1, 7) / (3, 7) / adjacent cans systematically.
