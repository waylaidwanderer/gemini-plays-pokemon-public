# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- PIT: Warp tile. Falling through takes you to the floor below.
- LADDER: Warp tile. Used to travel between floors.
- BOULDER: Object. Impassable. Can be pushed with Strength.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- ROCK: Destructible with ROCK SMASH.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S movement.
- LEDGE_HOP_RIGHT: One-way jump West to East.
- LEDGE_HOP_LEFT: One-way jump East to West.
- LEDGE_HOP_DOWN: One-way jump North to South.
- CAVE: Warp tile (Cave entrance).
- WATER: Requires Surf to traverse.
- DOOR: Warp tile.
- Warp Pathing: Navigate tool does not automatically avoid warp tiles. Use intermediate coordinates to steer around.

# Blackthorn City Discoveries
- Pokemon Center: (21, 29). Sign at (22, 29).
- Emy's House: (29, 23). Inside: Lass wants to trade DODRIO for female DRAGONAIR.
- Sign at (34, 24): "BLACKTHORN CITY - A Quiet Mountain Retreat"
- Cooltrainer F (Flavor NPC): (35, 19).
- Ice Path Exit: (36, 9) on map 5_10 (Warp from 3_61 at 36, 27).
- Move Deleter's House: (9, 31).
- Dragon Speech House: (13, 21). Inside: Granny and Dratini (Ekans sprite).
- Blackthorn Gym Entrance: (18, 11). Sign at (17, 13).

# Blackthorn Gym Exploration
- Strategy:
  1. Defeat Gym Trainers for EXP [Done]
  2. Solve Gym Puzzle (2F/1F) [In Progress]
  3. Defeat Gym Leader Clair.
- Trainers Defeated: Paul (1, 15) on 1F, Fran (4, 11) on 2F, Cody (4, 1) on 2F.
- Gym Guide (7, 15) Advice: Clair uses Dragon-type Pokemon. They are weak against Ice-type moves.

# Strategy: Gym Leader Clair
- Opponent: Clair (Dragon User).
- Team (Crystal): 
  - Dragonair (Lv37): Dragonbreath, Surf, Thunder Wave, Slam.
  - Dragonair (Lv37): Dragonbreath, Ice Beam, Thunder Wave, Slam.
  - Dragonair (Lv37): Dragonbreath, Thunderbolt, Thunder Wave, Slam.
  - Kingdra (Lv40): Dragonbreath, Surf, Smokescreen, Hyper Beam.
- Battle Strategy: Lead with Calcifer. Chip away at Kingdra. Switch to Gneiss to tank Hyper Beam.

# Reflection & Lessons
- **Turn Tracking:** Sourced from Game State Info.
- **Warp Pathing:** Navigate tool does not avoid warps. Manually steer around.
- **Boulder Tracking:** Link markers to object_id for moving objects.
- **Pit Destinations:** Pit (2, 5) -> (2, 6) on 1F.

# Time Tracking
- Boulder Puzzle Started: Turn 29238.

# Blackthorn Gym Layout Theory
- The gym is split into sections on both floors.
- 1F Layout: West side contains Ladders (1, 7). East side island (7, 9).
- 2F Layout: Quadrants NW, NE, SW, SE. Row 13 connects East and West.
- Strategy: Use 2F Row 13 to move between quadrants.

# Blackthorn Gym Puzzle Progress
- Boulder 3 (8, 2): Pushed into Pit (8, 3). [Turn 29284]
- Boulder 4 (2, 4): Pushed into Pit (2, 5). [Turn 29318]
- Boulder 6 (3, 3): Moved to clear path. [Currently at (3, 3) after reset]
- Boulder 7 (6, 1): Investigating.
- Boulder 8 (8, 14): Target is Pit (8, 7). Path: (8, 14) -> (8, 11) -> (9, 11) -> (9, 7) -> (8, 7).
- Boulder 5 (6, 16): Path blocker.
- Pits filled: (8, 3), (2, 5).
- SE Puzzle Plan:
  1. Navigate to (6, 15).
  2. Push Boulder 5 (6, 16) DOWN to (6, 17).
  3. Walk (6, 15) -> (6, 16) -> (7, 16) -> (8, 16) -> (8, 15).
  4. Push Boulder 8 (8, 14) UP to (8, 11).
  5. Move to (8, 12), push RIGHT to (9, 11).
  6. Push UP to (9, 7).
  7. Push LEFT into Pit (8, 7).