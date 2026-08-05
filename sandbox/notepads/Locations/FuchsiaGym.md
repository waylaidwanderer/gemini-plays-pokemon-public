# Fuchsia City Gym - Invisible Walls & Navigation

## Map Dimensions & Basic Layout
- The Gym is a square room, roughly from x=4 to x=9 (walkable columns) and y=5 to y=17 (walkable rows).
- Entrance door: `(5, 17)`.
- Gym Guide: `(7, 15)`.

## Verified Walkable Path & Coordinates
- **Row 17:** `(4, 17)`, `(5, 17)`, `(6, 17)`, `(7, 17)` are open and walkable.
- **Row 16:** `(7, 16)`, `(8, 16)`, `(9, 16)` are open and walkable.
- **Column 9:** Completely walkable from `(9, 16)` up to `(9, 2)`. Specifically: `(9, 15)`, `(9, 14)`, `(9, 13)`, `(9, 12)`, `(9, 11)`, `(9, 10)`, `(9, 9)`, `(9, 8)`, `(9, 7)`, `(9, 6)`, `(9, 5)`, `(9, 4)`, `(9, 3)`, `(9, 2)` are walkable.
- **Row 8:** `(9, 8)` is open and walkable.

## Collision Points & Invisible Walls
- **(4, 17) boundaries:** Walking Up from `(4, 17)` is blocked by an invisible wall. Walking Right from `(4, 17)` is blocked by an invisible wall? No, we successfully walked Right to `(5, 17)`.
- **(5, 30) signpost:** Outside the gym, the signpost is at `(5, 29)`, which blocks direct northern movement.
- **Row 31:** Outside the gym, the log fence is solid at columns 4, 5, 6, 7.

## Defeated Gym Trainers
- **Juggler Kirk:** Standing at `(8, 8)` (challenged from `(9, 8)` on Turn 20456). Defeated on Turn 20492. Roster: DROWZEE Lv 31, DROWZEE Lv 31, KADABRA Lv 31, DROWZEE Lv 31. Prize money: ¥1085.
- **Tamer Phil:** Standing at `(8, 2)` (challenged from `(9, 2)` on Turn 20504). Defeated on Turn 20534. Roster: Arbok Lv 33, Sandslash Lv 33, Arbok Lv 33. Prize money: ¥1320.