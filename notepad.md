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

# Strategy: Reach Suicune (The Great Western Loop)
- Start Turn: 48227 (Pursuit began), 48514 (Current strategy)
- Step 1: Walk to (23, 51) via Row 44.
- Step 2: Walk West at Row 51 to X=2.
- Step 3: Walk North at X=2 to Row 10.
- Step 4: Walk East at Row 10 to (14, 10).
- Note: This avoids the maze of walls and ledges in the city center.

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