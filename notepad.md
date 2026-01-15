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

# Strategy: Reach Suicune (The Northern Water Approach)
- Start Turn: 48227 (Pursuit began), 48532 (Current strategy)
- Step 1: Surf North to (20, 15).
- Step 2: East to (23, 15) (Buoy Gap 6).
- Step 3: North to (23, 14), then West to (18, 14) (Buoy Gap 4).
- Step 4: North to (18, 11), then West to (17, 11).
- Step 5: Land at (16, 11) and walk to Suicune sighting spot at (14, 10).
- Note: This path navigates the buoy maze by finding the specific gaps in Row 15 and Row 14. Verified that (16, 11) is a FLOOR tile.

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