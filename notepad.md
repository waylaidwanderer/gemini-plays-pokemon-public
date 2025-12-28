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
- Pokemon Center: (21, 29).
- Emy's House: (29, 23). Inside: Lass wants to trade DODRIO for female DRAGONAIR.
- Sign at (34, 24): "A Quiet Mountain Retreat"
- Ice Path Exit: (36, 9) on map 5_10.
- Move Deleter's House: (9, 31).
- Dragon Speech House: (13, 21). Inside: Granny and Dratini.
- Blackthorn Gym Entrance: (18, 11). Sign at (17, 13).

# Blackthorn Gym Exploration
- Strategy:
  1. Defeat Gym Trainers for EXP [Done]
  2. Solve Gym Puzzle (2F/1F) [In Progress]
  3. Defeat Gym Leader Clair.
- Trainers Defeated: Paul (1, 15) on 1F, Mike (6, 8) on 1F, Fran (4, 11) on 2F, Cody (4, 1) on 2F.
- Gym Guide (7, 15) Advice: Clair uses Dragon-type Pokemon. They are weak against Ice-type moves.

# Strategy: Gym Leader Clair
- Opponent: Clair (Dragon User).
- Team (Crystal): 
  - Dragonair (Lv37): Dragonbreath, Surf, Thunder Wave, Slam.
  - Dragonair (Lv37): Dragonbreath, Ice Beam, Thunder Wave, Slam.
  - Dragonair (Lv37): Dragonbreath, Thunderbolt, Thunder Wave, Slam.
  - Kingdra (Lv40): Dragonbreath, Surf, Smokescreen, Hyper Beam.
- Battle Strategy: Lead with Calcifer. Use Thunderpunch (Special in Gen II). Use fodder for healing.

# Reflection & Lessons
- **Turn Tracking:** Sourced from Game State Info.
- **Boulder Tracking:** Link markers to object_id. Boulders 3 and 4 stay in pits after floor reset on 2F.
- **Pit Destinations:** Pit (2, 5) -> 1F Entry 5. Pit (8, 7) -> 1F Entry 6. Pit (8, 3) -> 1F Entry 7.

# Blackthorn Gym Puzzle Progress
- Status: Pits (8, 3) and (2, 5) are filled. Pit (8, 7) is EMPTY.
- The Loop Plan (Turn 29368):
  1. Push Boulder 8 (8, 15) DOWN to (8, 17) to clear Column 8.
  2. Walk (8, 13) -> (8, 17) -> (7, 17) -> (6, 17).
  3. From (6, 17), push Boulder 5 (6, 16) all the way UP to (6, 7).
  4. Navigate to (5, 7), push Boulder 5 RIGHT to (8, 7) (PIT).
- Current Status: Strength active. Boulder 8 at (8, 16). Pushing to (8, 17). [Time: Turn 29369]