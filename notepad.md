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
- LEDGE_HOP_DOWN: One-way jump down; impassable from below. Verified one-way movement.

# Main Story Progression: 8th Gym Badge
- Goal: Reach Blackthorn City and defeat Gym Leader Clair.
- Current Status: 7 Badges.
- Quest Start Turn: 27941.
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
- Turn 27975: Mandatory 50-turn reflection performed. No deferred tasks. Markers updated. New tool 'get_reachable_unseen_tiles' defined.