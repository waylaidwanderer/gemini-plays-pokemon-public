# Fuchsia City Gym - Invisible Walls & Navigation

## Map Dimensions & Basic Layout
- The Gym is a square room, roughly from x=4 to x=9 (walkable columns) and y=5 to y=17 (walkable rows).
- Entrance door: `(5, 17)`.
- Gym Guide: `(7, 15)`.

## Verified Walkable Path & Coordinates
- **Row 17:** `(4, 17)`, `(5, 17)`, `(6, 17)`, `(7, 17)` are open and walkable.
- **Row 16:** Completely walkable from `(9, 16)` west to `(1, 16)`. Specifically: `(9, 16)`, `(8, 16)`, `(7, 16)`, `(6, 16)`, `(5, 16)`, `(4, 16)`, `(3, 16)`, `(2, 16)`, `(1, 16)` are open and walkable.
- **Column 9:** Completely walkable from `(9, 16)` up to `(9, 1)`. Specifically: `(9, 15)`, `(9, 14)`, `(9, 13)`, `(9, 12)`, `(9, 11)`, `(9, 10)`, `(9, 9)`, `(9, 8)`, `(9, 7)`, `(9, 6)`, `(9, 5)`, `(9, 4)`, `(9, 3)`, `(9, 2)`, `(9, 1)` are walkable.
- **Column 8:** `(8, 3)`, `(8, 4)`, `(8, 5)`, `(8, 6)`, `(8, 9)`, `(8, 10)`, `(8, 11)`, `(8, 12)` are open and walkable.
- **Column 7:** `(7, 6)`, `(7, 7)`, `(7, 8)`, `(7, 9)` are open and walkable.
- **Column 1:** `(1, 15)`, `(1, 16)` are open and walkable.
- **Row 8:** `(9, 8)` is open and walkable.

## Collision Points & Invisible Walls
- **(4, 17) boundaries:** Walking Up from `(4, 17)` is blocked by an invisible wall. Walking Right from `(4, 17)` is blocked by an invisible wall? No, we successfully walked Right to `(5, 17)`.
- **(5, 30) signpost:** Outside the gym, the signpost is at `(5, 29)`, which blocks direct northern movement.
- **Row 31:** Outside the gym, the log fence is solid at columns 4, 5, 6, 7.
- **Column 8 to Column 7 barriers:** Blocked moving Left from `(8, 3)` to `(7, 3)`, from `(8, 4)` to `(7, 4)`, and from `(8, 5)` to `(7, 5)`.
- **Column 7 to Column 6 barriers:** Blocked moving Left from `(7, 6)` to `(6, 6)`, from `(7, 7)` to `(6, 7)`, from `(7, 8)` to `(6, 8)`, and from `(7, 9)` to `(6, 9)`.
- **Row 10 barriers:** Blocked moving Down from `(7, 9)` to `(7, 10)`.
- **Row 5 barriers:** Blocked moving Up from `(7, 6)` to `(7, 5)`.

## Defeated Gym Trainers
- **Juggler Kirk:** Standing at `(8, 8)` (challenged from `(9, 8)` on Turn 20456). Defeated on Turn 20492. Roster: DROWZEE Lv 31, DROWZEE Lv 31, KADABRA Lv 31, DROWZEE Lv 31. Prize money: ¥1085.
- **Tamer Phil:** Standing at `(8, 2)` (challenged from `(9, 2)` on Turn 20504). Defeated on Turn 20534. Roster: Arbok Lv 33, Sandslash Lv 33, Arbok Lv 33. Prize money: ¥1320.
- **Juggler Edgar:** Standing at `(8, 13)` (challenged from `(8, 12)` on Turn 20572). Defeated on Turn 20593. Roster: Hypno Lv 38. Prize money: ¥1330.
- **Juggler Shawn:** Standing at `(1, 14)` (challenged from `(1, 15)` on Turn 20607). Defeated on Turn 20625. Roster: Drowzee Lv 34, Kadabra Lv 34. Prize money: ¥1190.