# Vermilion Gym - Trash Can Empirical Trial Log & Mechanics

## Puzzle Mechanics (Gen 1 Retail)
- 15 cans in 5x3 grid at columns (1, 3, 5, 7, 9) and rows (7, 9, 11).
- Switch 1 is randomly assigned to one of the 15 cans.
- Once Switch 1 is pressed, Switch 2 is in an orthogonally adjacent can in the grid (North, South, East, West).
- If Switch 2 check fails, both locks reset and Switch 1 relocates.

## Sweep Protocol
- Check each can systematically.
- As soon as Switch 1 triggers, immediately check adjacent cans (dist 2 in coords).