# Strategy for Primary Goal (Defeat Gym Leader Chuck)
- Battle started at Turn 7161.
- Observation: Chuck uses Fighting-type Pokémon (Primeape Lv27, Poliwrath Lv30).
- Team Assets: KIMCHI (Poison resists Fighting), Blarney (Sudowoodo). 
- Note: Poliwrath is Water/Fighting. GNEISS and Calcifer are weak to Water.
- Plan: Train KIMCHI to Lv21+ for evolution into Gloom. Use Sleep Powder and Grass moves against Poliwrath. KIMCHI reached Lv18 at Turn 7171 and learned Sleep Powder.
- Battle Status (Turn #7210): Primeape defeated. Poliwrath is asleep. Calcifer (Lv35, 36/96 HP) is in. Strategy: Using Headbutt while Poliwrath is asleep to deal physical damage. Calcifer landed a critical hit last turn.

# Tile Mechanics
- FLOOR: Traversable.
- WALL / BUOY / ROCK / BOOKSHELF / TV / RADIO / TOWN_MAP / STATUE / COUNTER: Impassable.
- WATER: Traversable via Surf (HM03 + Fog Badge).
- WHIRLPOOL: Impassable (likely requires HM).
- LADDER / DOOR / PIT / WARP_CARPET: Map transition.
- Relational: Counter NPCs (face counter), PCs/Switches (face UP from BELOW).

# Lessons Learned
- Tool Maintenance: find_path_v2 logic for water-to-land transitions must allow movement onto land tiles even when the player is on a water tile (Surfing).
- Map Markers: Always verify the map_id when placing markers, especially when near map boundaries.
- Battle Mechanics: Karate Chop is a Fighting-type move in Crystal (verified turn 7167).

# Type Effectiveness Chart
- Magnitude (Ground) vs Tentacruel (Water/Poison): Super effective.
- Rollout (Rock) vs Mantine (Water/Flying): Super effective.
- Fighting (Karate Chop) vs Poison (Oddish): Not very effective.
- Fighting (Karate Chop) vs Rock/Ground (Graveler): Super effective.
- Water vs Fire (Quilava): Super effective.
- Water vs Rock/Ground (Graveler): 4x Super effective.
- Grass vs Water/Fighting (Poliwrath): Super effective.

# PC Storage (Box 1)
- ROCKY (ONIX) Lv6, ICARUS (PIDGEY) Lv11, EGG (CLEFFA) Lv5, XFDW (MEOWTH) Lv16, FRITTATA (TOGEPI) Lv5.

# Weakness Reference
- Abra (Psychic): Bug, Ghost, Dark.
- Growlithe (Fire): Water, Ground, Rock.
- Snubbull (Normal): Fighting.

# Cianwood Gym Boulder Puzzle (Solved)
- Observation: Boulders at (3, 7), (4, 7), (5, 7) block path.
- Solution: Push (3, 7) up to (3, 6), (5, 7) up to (5, 6), and (4, 7) to either side.