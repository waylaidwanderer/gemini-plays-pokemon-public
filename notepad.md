# PC Storage (Box 1)
- DAPXWW (LARVITAR): Lv20
- GLAIVE (SCYTHER): Lv14
- SELKIE (SEEL): Lv24
- DELTA (MANTINE): Lv20
- RANGOON (KRABBY): Lv22
- NOMURA (TENTACOOL): Lv17
- Ravioli (KRABBY): Lv10 (Surf, Whirlpool)
- Ouroboros (DRATINI): Lv15 (ExtremeSpeed)
- AAAAAAAAAA (SPINARAK): Lv13
- LAPIS (POLIWAG): Lv12 (Waterfall, Surf, Whirlpool)

# Tile Mechanics (Verified)
- FLOOR: Walkable.
- WALL / BUOY: Impassable.
- WATER: Traversable only via Surf.
- FLOOR_UP_WALL: Impassable from the NORTH.
- LEDGE_HOP_DOWN: One-way jump from NORTH to SOUTH.
- COUNTER: Impassable.

# Suicune Quest Strategy: 'The Island Bypass'
- Goal: Reach Suicune at (7, 4).
- Fact: Northern water is isolated from southern/eastern water by buoy walls.
- Solution: Sail south to the land bridge at Y=30, walk across to the western channel, then sail north and land on the north beach.
- Route:
    1. From (23, 16), sail Down to (23, 30).
    2. Sail Left to (20, 30) and land at (19, 30).
    3. Walk West across the land bridge to (15, 30).
    4. Face Up and Surf into (15, 29).
    5. Sail North in the western channel to (15, 19).
    6. Sail West and land at (4, 19).
    7. Walk to (14, 10) and then (7, 4).
- Preparation: Lead with XENON (Haunter) for Hypnosis. Be ready for Eusine.
- Status: At (12, 28). Abandoned Surfing plan in favor of the walking route along the western beach.
- Attempt 1 (Triple Gap Loop): Hallucinated/Incorrect.
- Attempt 2 (Island Bypass - Surf): Possible, but walking is more verified.
- Attempt 3 (Island Bypass - Walk): Walking along the western sand/beach to avoid buoy walls.
- Route (Triple Gap Loop):
    1. From (4, 29), move Up to (4, 28).
    2. Move Right and Down to (19, 30).
    3. Face Right and Surf into (20, 30).
    4. Sail to (27, 30) -> (27, 10).
    5. Move Left through gap at (26, 10) to (25, 10).
    6. Sail to (25, 8).
    7. Move Left through gap at (22, 8) to (21, 8).
    8. Sail to (14, 8) and land at (14, 10).
    9. Walk to Suicune sighting area at (7, 4).
- Preparation: Lead with XENON (Haunter) for Hypnosis. Be ready for Eusine.
- Note: (4, 30) is a FLOOR_UP_WALL (impassable from NORTH). (5, 29) is a ROCK.
- Reflection (Turn #47689):
    1. Deferrals: None.
    2. Notepad: Re-prioritized 'Triple Gap Loop'. The gaps at (26, 10) and (22, 8) are verified in the mental map.
    3. Map: Markers are accurate.
    4. Automation: find_path_crystal_v7_final will be used for overworld segments.
    5. Goal Clarity: Goals are outcome-based.
    6. Error Analysis: Attempt 3 (Island Bypass - Walk) failed because of the FLOOR_UP_WALL at (4, 30). Returning to the water route which is now fully mapped.
- Start Turn: 47680 (Suicune North Beach Quest)
- Start Time: Wednesday, Jan 14, 2026, 4:00 AM PST