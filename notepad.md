# Strategy for Primary Goal (Travel to Mahogany Town)
- Step 1: Go to Cianwood PC (23, 43). [DONE]
- Step 2: Swap a party member for ICARUS (PIDGEY). [DONE - Deposited SHUCKIE]
- Step 3: Teach FLY to ICARUS. [DONE]
- Step 4: Fly to Ecruteak City. [DONE]
- Step 5: Head east through Route 42 to Mahogany Town. [IN PROGRESS]

# Strategy for KIMCHI Training
- Route: Route 40/41 (Surf).
- Method: Lead with KIMCHI, switch to Calcifer/GNEISS for shared XP.
- Training Goal Started: Turn 7110. Goal: Lv21 for evolution into Gloom.

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
- Water vs Fire (Quilava/Typhlosion): Super effective.
- Water vs Rock/Ground (Graveler): 4x Super effective.
- Grass vs Water/Fighting (Poliwrath): Super effective.

# PC Storage (Box 1)
- ROCKY (ONIX) Lv6, EGG (CLEFFA) Lv5, XFDW (MEOWTH) Lv16, FRITTATA (TOGEPI) Lv5, SHUCKIE (SHUCKLE) Lv15.

# Weakness Reference
- Abra (Psychic): Bug, Ghost, Dark.
- Growlithe (Fire): Water, Ground, Rock.
- Snubbull (Normal): Fighting.

# General Lessons
- Fly Mechanics: HM02 Fly can only be used from the overworld (outdoors). Attempting to use it inside buildings or caves results in "Can't use that here."
- Menu Navigation: When using HMs like Fly, ensure you are in the overworld before opening the menu to avoid redundant navigation.