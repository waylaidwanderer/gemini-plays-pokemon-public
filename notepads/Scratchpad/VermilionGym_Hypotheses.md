# Vermilion Gym - Trash Can Empirical Trial Log & Mechanics

## Puzzle Mechanics (Gen 1 Retail)
- 15 cans in 5x3 grid at columns (1, 3, 5, 7, 9) and rows (7, 9, 11).
- Switch 1 is randomly assigned to one of the 15 cans.
- Once Switch 1 is pressed, Switch 2 is in an orthogonally adjacent can in the grid (North, South, East, West).
- If Switch 2 check fails, both locks reset and Switch 1 relocates.

## Sweep Protocol
- Check each can systematically.
- As soon as Switch 1 triggers, immediately check adjacent cans (dist 2 in coords).

## Sweep Trial Log
- (3, 11): Trash (Turn 2665)
- (3, 9): Trash (Turn 2666)
- (1, 9): Trash (Turn 2667)
- (1, 7): Trash (Turn 2668)
- (3, 7): Trash (Turn 2669)
- (5, 7): Trash (Turn 2674)
- (5, 9): Trash (Turn 2675)
- (5, 11): Trash (Turn 2676)
- (7, 11): Checking (Turn 2678)
- (7, 11): Trash (Turn 2679)