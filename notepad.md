# Main Story Progression: 8th Gym Badge
- Goal: Reach Blackthorn City and defeat Gym Leader Clair.
- Current Status: 7 Badges.
- Quest Start: Turn 27941 | Saturday, Dec 27, 2024, 10:15 PM
- Plan:
  1. Fly to Mahogany Town.
  2. Travel East through Route 44.
  3. Navigate Ice Path to reach Blackthorn City.
  4. Challenge Blackthorn Gym.

## Battle Strategy (Blackthorn Gym)
- Gym Leader Clair: Dragon-types.
- Counters: 
  - GNEISS (Graveler): Earthquake/Rollout for general damage.
  - Calcifer (Typhlosion): Thunderpunch for Gyarados/Kingdra (if applicable).
  - Ravioli (Krabby): Needs training or replacement.
  - KIMCHI (Gloom): Sleep Powder for status support.

# Lessons Learned
- Suicune Sighting Sequence: Strictly sequential and mandatory. Clear Bell does NOT bypass sightings.
- Decision Making: If a side quest stalls for >100 turns, pivot to main story progression.
- Tin Tower Sages: Do not engage until wild sightings are confirmed in Pokedex or cutscene.
- HM Usage: Whirlpool will be needed for Dragon's Den after the 8th Gym. Ensure a party member can learn it (Ravioli/Krabby can).
- Fly Map Navigation: Cursor cycles through visited cities. Observe movement rather than geographic directions.
- FLOOR_UP_WALL: Impassable barrier, likely representing the base of a building or fence. Verified impassable from above.

# Tile Mechanics - Global
- FLOOR: Standard walkable tile. Verified traversable.
- WALL: Impassable boundary. Verified impassable.
- WATER: Traversable only with Surf. Verified traversable with HM03.
- BUOY: Impassable boundary in water. Verified impassable.
- WARP_CARPET: Triggers map transition when walked off the map edge. Verified functional.
- HEADBUTT_TREE: Blocking object; can be interacted with using Headbutt. Verified impassable.
- CUT_TREE: Blocking object; requires HM01 Cut. Verified impassable until cut. Regrows on map reload.
- COUNTER: Impassable barrier often found in shops or gatehouses; allows interaction with NPCs behind it. Verified impassable.
- CAVE: Map transition entry point. Verified functional.
- TALL_GRASS: Walkable; triggers wild battles. Verified traversable.
- LONG_GRASS: Walkable; triggers wild battles. Verified traversable.
- LEDGE_HOP_DOWN: One-way jump down; impassable from below. Verified one-way movement.
- LEDGE_HOP_LEFT: One-way jump left; impassable from right. Verified one-way movement.
- FLOOR_UP_WALL: Impassable boundary. Verified impassable.
- VOID: Impassable area outside map boundaries. Verified impassable.
- POKECENTER_SIGN: Background object; displays Pokemon Center info. Verified interactable.
- MART_SIGN: Background object; displays Poké Mart info. Verified interactable.
- SIGNPOST: Background object; displays area or direction info. Verified interactable.

# Exploration: Route 44 Central Lake
- Hypothesis: Surfing across the central lake from the mainland launch point at (20, 12) will allow access to the northern path leading to the Ice Path.
- Test 1: Navigate to (19, 12), face (20, 12), and use HM03 Surf.
- Status: In progress.
- Attempt 1: Turn 28000.

# Navigation: Reaching Ice Path Entrance
- Observation: The eastern part of Route 44 is on a high platform.
- Barrier: Row 9 (X=51-57) and Row 13 (X=47-48, 50-53) are one-way ledges hopping down.
- Discovery: X=49 is a traversable corridor from Row 14 up to Row 4.
- Route:
  1. (19, 12) -> (18, 14) to avoid Fisher Edgar.
  2. (18, 14) -> (49, 14) east along the main path.
  3. (49, 14) -> (49, 7) north through the corridor.
  4. (49, 7) -> (52, 7) -> (52, 8) -> (56, 8) -> (56, 7) to bypass the sign at (53, 7).
- Status: Commencing. Turn 28010.