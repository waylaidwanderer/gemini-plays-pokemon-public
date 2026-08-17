# Vermilion Gym - Trash Can Switch Matrix & Optimal Corner Strategy

## True Engine Mechanics (Verified)
- 15 trash cans arranged in a 3x5 grid.
- When an empty can is inspected, wFirstTrashCan is re-rolled by Random after each failed check.
- Therefore, each check on any can is an independent Bernoulli trial with p = 1/15.
- Once Switch 1 is triggered, Switch 2 is selected from the cardinal neighbors of Switch 1 in the 3x5 matrix.
- Corner cans (1, 7), (9, 7), (1, 11), (9, 11) have only 2 neighbors, giving a 50% chance for either neighbor to be Switch 2.

## Optimal Strategy:
- Position: Standing at (8, 7) between (7, 7) and (9, 7).
- Action 1: Repeatedly check corner can (9, 7) facing Right until Switch 1 triggers.
- Action 2: As soon as Switch 1 triggers, immediately turn Left and inspect (7, 7).
- If (7, 7) opens the second lock -> Motorized doors open permanently -> Challenge Lt. Surge!
- If (7, 7) resets -> Re-check (9, 7) until Switch 1 triggers again, then test (9, 9) or (7, 7).
