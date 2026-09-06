# Scratchpad: Vermilion Gym Lock Puzzle

## Clues & Dialogue
- Gym Guide: "LT. SURGE is very cautious! You'll have to break a code to get to him!"
- Trainer at (3, 8) [Rocker]: "I'm a lightweight, but I'm good with electricity!"
- Trainer at (0, 10) [Sailor]: "This is no place for kids!"
- Trainer at (9, 6) [Gentleman]: "When I was in the Army, LT.SURGE was my strict CO!" / Defeat: "GENTLEMAN: Stop! You're very good!"

## Structure & Coordinates
- 5x3 Grid of 15 Trash Cans:
  - Rows: 7, 9, 11
  - Cols: 1, 3, 5, 7, 9
- Grid Matrix Map:
  - Row 7:  (1, 7)  (3, 7)  (5, 7)  (7, 7)  (9, 7)
  - Row 9:  (1, 9)  (3, 9)  (5, 9)  (7, 9)  (9, 9)
  - Row 11: (1, 11) (3, 11) (5, 11) (7, 11) (9, 11)
- Aisles:
  - Vertical: cols 0, 2, 4, 6, 8
  - Horizontal: rows 6, 8, 10, 12
- Barrier: Located at rows 4..5 blocking passage to Lt. Surge.

## Testing Log & Hypotheses
- Status: Systematic inspection of 15 cans for 1st switch.
- [x] Can (7, 7): Checked Turn 3306 -> Only trash.
- [x] Can (9, 7): Checked Turn 3307 -> Only trash.
- [x] Can (9, 9): Checked Turn 3308 -> Only trash.
- [x] Can (7, 9): Checked Turn 3310 -> Only trash.
- [ ] Can (9, 11): Inspecting Turn 3310.
