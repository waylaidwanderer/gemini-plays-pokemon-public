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
- **Pit Destinations (Verified):** Pit (2, 5) -> 1F (2, 6). Pit (8, 7) -> 1F (7, 7). Pit (8, 3) -> 1F (7, 6).

# Blackthorn Gym Puzzle Progress
- Status: Verifying if floor reset (Turn 29336) restored Boulders 3 and 4 or if they remain in pits.
- Master Puzzle Plan (Turn 29347):
  1. Check landing spots (2, 6), (7, 6), (7, 7) on 1F.
  2. If boulders are missing, return to 2F and push them again.
  3. Final Pit to fill: (8, 7). Target: Boulder 8 (8, 14) or Boulder 7 (6, 1).
- SE Puzzle Plan (Plan B): Push Boulder 8 (8, 14) north to row 11, then right to col 9, then up to row 7, then left into pit (8, 7).
- NW Puzzle Plan (Plan C): Use Boulder 6 to clear path for Boulder 4 if reset.
- Verification: Stand at (6, 7) to see (7, 6) and (7, 7). Stand at (2, 7) to see (2, 6).

# Current Battle: Cooltrainer Mike (1F)
- Opponent Lead: Dragonair (Lv37).
- Strategy: Use Headbutt with Calcifer. Thunderpunch and Flame Wheel are resisted by pure Dragon-types.
- Goal: Defeat Mike to clear the path to the pits.