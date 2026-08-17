# Vermilion Gym - Trash Can Puzzle Mechanics & Optimal Strategy

## Mechanics Synthesis
- Each trash can check has a ~1/15 probability of being Switch 1.
- In both Sweep Run #4 and Run #5, all 15 cans were checked sequentially and returned empty (~35.5% probability per 15-check sequence).
- Once Switch 1 is found, Switch 2 is randomly placed in one of the cardinal adjacent neighbors.

## Optimal Rapid Solution (Position: (8, 11))
- Stand at (8, 11) between trash can (7, 11) [Left] and (9, 11) [Right].
- Alternate checking (7, 11) and (9, 11) until Switch 1 activates: "Hey! There's a switch under the trash! Turn it on! The 1st electric lock opened!"
- Immediate Response Protocol:
  - If Switch 1 is at (9, 11): Immediately check (7, 11) [`Left`, `A`] or (9, 9) [`Up`, `Right`, `A`].
  - If Switch 1 is at (7, 11): Immediately check (9, 11) [`Right`, `A`], (7, 9) [`Up`, `Left`, `A`], or (5, 11) [`Left`, `Left`, `A`].
- Once both switches are active: Motorized door opens, walk directly north to challenge Gym Leader Lt. Surge!
