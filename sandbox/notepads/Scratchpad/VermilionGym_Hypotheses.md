# Vermilion Gym - Trash Can Mechanics & Strategy

## Verified Mechanics (Retail Pokémon Blue)
1. **Switch 1**: Whenever an incorrect trash can is checked, Switch 1 is re-randomized to a random can (1/15 chance per check).
2. **Switch 2**: Once Switch 1 is activated, Switch 2 is randomly placed in one of the cardinal adjacent trash cans (North, South, East, West).
3. **Reset**: If a non-Switch-2 can is checked after Switch 1 is activated, the locks reset and Switch 1 re-randomizes.

## Rapid Loop Strategy
- Stand at (8, 7) between trash cans (7, 7) and (9, 7).
- Alternate checking (7, 7) [facing Left] and (9, 7) [facing Right] until Switch 1 activates.
- Once Switch 1 activates:
  - If Switch 1 is at (7, 7): Immediately check neighbors: (5, 7) [West], (7, 9) [South], (9, 7) [East].
  - If Switch 1 is at (9, 7): Immediately check neighbors: (7, 7) [West], (9, 9) [South].