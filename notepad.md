# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Goal: Reach the Underground Warehouse (Map 3_55).

## Lessons Learned
- Initial state and order of operations are critical.
- Previous baseline was hallucinated/inconsistent.
- Resetting the map (leaving and re-entering) is necessary to clear toggle state confusion.

## Plan
1. Exit to Map 3_52 via (23, 3) and re-enter.
2. Visually verify EVERY shutter state (2,6), (6,8), (10,6), (12,8), (16,6) without touching any switches.
3. Record the TRUE baseline.
4. Execute Switch 3 ON -> Switch 2 ON -> Switch 1 ON.

# Area Notes
- Warehouse Entrance: South-east unseen area.
- Trainers: All defeated.
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead to 3_52.
- Rocket Girl: (19, 12).
- Emergency Switch: (20, 11).