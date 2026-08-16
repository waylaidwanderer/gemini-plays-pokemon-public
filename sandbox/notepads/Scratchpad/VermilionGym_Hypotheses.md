# Vermilion Gym - Switch Puzzle Log & Strategy

## Puzzle Mechanics (Gen 1 Red/Blue)
- 15 Trash Cans in 5x3 Grid across rows 7, 9, 11 (cols 1, 3, 5, 7, 9).
- Switch 1 is randomly assigned upon gym entry and re-randomized upon any failed Switch 2 check.
- When Switch 1 is found at (cx, cy), Switch 2 is guaranteed to be in one of the cardinally adjacent cans.
- Success requires activating Switch 1 and immediately checking the correct adjacent can.

## Current State (Turn 2297)
- Switch 1: FOUND at Can (9, 11) [Bottom-Right Corner]!
- Switch 2 Candidates (Only 2 possible neighbors!):
  1. Can (7, 11) [West Neighbor - checking now!]
  2. Can (9, 9) [North Neighbor]

- Turn 2305: Switch 1 found at (9, 7)! Testing adjacent can at (7, 7) for Switch 2.
- Turn 2307: Can (7, 7) was empty. Locks reset. Resuming systematic search starting at (9, 7).