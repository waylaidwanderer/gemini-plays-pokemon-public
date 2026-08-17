# Vermilion Gym - Trash Can Switch Matrix & Trial Log

## Puzzle Mechanics Analysis
- 15 trash cans arranged in a 3x5 grid:
  - Row 7: (1, 7), (3, 7), (5, 7), (7, 7), (9, 7)
  - Row 9: (1, 9), (3, 9), (5, 9), (7, 9), (9, 9)
  - Row 11: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11)
- Observation (Turn 2418): All 15 cans were inspected in sequence and all returned "Nope, there's only trash here."
- Hypothesis:
  1. In Gen 1 Pokémon Blue engine, `wFirstTrashCan` is generated via `Random` on map initialization. If the random value rolled index 15 (out of bounds for 0..14), no can matches.
  2. Re-rolling occurs upon map load (stepping outside to Vermilion City and re-entering).

## Test Protocol:
- Turn 2419: Press B to dismiss, press A on (1, 7) again.
- If still empty -> Walk south to exit (4, 17), step out to Vermilion City, re-enter Gym to generate fresh `wFirstTrashCan` seed.
