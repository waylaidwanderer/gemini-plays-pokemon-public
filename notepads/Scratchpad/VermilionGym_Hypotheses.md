# Vermilion Gym - Trash Can Switch Matrix & Empirical Trial Log

## Empirical Engine Analysis & Proven Retail Mechanics
- 15 trash cans arranged in a 3x5 grid (indices 0..14).
- On map load, the game executes a random 4-bit roll (values 0..15).
- If index 0..14 is rolled (93.75% probability), Switch 1 is active in that specific can.
- If index 15 is rolled (6.25% probability), no can matches until map re-entry.
- wFirstTrashCan is static during a search cycle and does NOT re-roll on empty checks.
- When Switch 1 is found, Switch 2 is assigned to an adjacent neighbor in the 3x5 matrix.
- If Switch 2 fails, locks reset and a new random index is chosen.

## Sweep Protocol:
1. Re-enter Gym via south door to ensure fresh 93.75% active seed.
2. Sweep cans starting from top-left (1, 7), (3, 7), (5, 7)...
3. As soon as Switch 1 triggers, immediately test adjacent neighbors.
