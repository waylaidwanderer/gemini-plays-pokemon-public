# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- SHUTTER: Impassable when CLOSED (WALL), traversable when OPEN (FLOOR).

# Puzzle: Goldenrod Underground Switch Puzzle
- Started: Turn 9640
- Goal: Reach the Underground Warehouse (Map 3_55).

## Lessons Learned
- Initial state and order of operations are critical.
- Previous baseline was hallucinated; re-entering map to reset.
- Memory of "3-2-1" solution must be verified against current reality.

## Plan
1. Reset map by leaving and re-entering (Done Turn 9878).
2. Visually verify EVERY shutter and switch state without interaction.
3. Record TRUE baseline.
4. Execute Switch 3 ON -> Switch 2 ON -> Switch 1 ON.

## Verified Baseline (Default after fresh map entry)
- All switches OFF.
- Shutter (2, 6): OPEN
- Shutter (10, 6): CLOSED
- Shutter (16, 6): CLOSED
- Shutter (12, 8): OPEN
- Shutter (6, 8): CLOSED

## Sequence Progress: 3-2-1
- Step 1: Switch 3 (2, 1) -> ON (Done Turn 9890).
- Step 2: Switch 2 (10, 1) -> ON (Done Turn 9898).
- Step 3: Switch 1 (16, 1) -> Moving to turn ON.

# Area Notes
- Warehouse Entrance: South-east unseen area.
- Trainers: All defeated.
- Return Ladders: (23, 3), (21, 25), and (5, 25) lead to 3_53.
- Rocket Girl: (19, 12).
- Emergency Switch: (20, 11).