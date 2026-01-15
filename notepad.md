# PC Storage (Box 1)
1. DAPXWW (LARVITAR): Lv20
2. GLAIVE (SCYTHER): Lv14
3. SELKIE (SEEL): Lv24
4. DELTA (MANTINE): Lv20
5. RANGOON (KRABBY): Lv22
6. NOMURA (TENTACOOL): Lv17
7. Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
8. Ouroboros (DRATINI): Lv15 (Extremespeed)
9. SPINARAK: Lv13
10. LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Global)
- FLOOR: Standard ground. Traversable.
- WATER: Surf required. Traversable.
- BUOY: Impassable water obstacle.
- WALL: Impassable ground/object.
- DOOR: Warp point. Traversable.
- FLOOR_UP_WALL: Impassable ledge face. Blocks South movement.
- LEDGE_HOP_DOWN: One-way jump (North to South).

# Strategy: Reach Suicune (The Buoy Maze Landing)
- Start Turn: 48227 (Pursuit began), 48536 (Current strategy)
- Step 1: Surf from (20, 16) South to Row 21.
- Step 2: West through gap at (19, 21) to (16, 21).
- Step 3: North through gap at (16, 20) to (16, 17).
- Step 4: East to X=17, then North to (17, 16).
- Step 5: West to (14, 16) and land at (13, 16).
- Step 6: Walk to Suicune sighting spot at (14, 10) via (11, 15).
- Note: This path bypasses the solid buoy walls at Row 15 and X=19/22 by using the specific gaps at (19, 21) and (16, 20). Verified (13, 16) as a landing spot.

# Area Notes: Cianwood City
- Photo Studio: (9, 31)
- Poke Seer: (5, 17)
- Pharmacy: (15, 47)
- Gym: (8, 43)
- Breakable Rocks: (5, 29), (8, 16), (9, 17), (10, 27), (4, 19), (4, 25)

# General Lessons
- Buoy layouts in water channels often create dead-end pockets (e.g., Row 10 in Cianwood). Always verify the northern/southern exits before committing.
- City layouts with many ledges (like Cianwood) are best navigated by finding a perimeter path rather than cutting through the center.
- `FLOOR_UP_WALL` tiles typically block movement in one direction (usually South in this region). Document verified directions in the Tile Mechanics section.