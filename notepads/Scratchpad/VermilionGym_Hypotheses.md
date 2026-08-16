# Vermilion Gym - Hypotheses & Switch Tracking

## Puzzle Status: In Progress (Active Search)
- Gates are CLOSED at (4, 4) and (5, 4).
- Electric locks were reset. Switch 1 is currently randomized among the 15 cans.

## Search Strategy
1. Check cans until Switch 1 is found ("The 1st electric lock opened!").
2. Immediately check adjacent cans (North, South, East, West) for Switch 2.
3. Verify passability past row 5 before declaring success.

## 15 Trash Can Coordinates
- Row 7: (1, 7), (3, 7), (5, 7), (7, 7), (9, 7)
- Row 9: (1, 9), (3, 9), (5, 9), (7, 9), (9, 9)
- Row 11: (1, 11), (3, 11), (5, 11), (7, 11), (9, 11)
