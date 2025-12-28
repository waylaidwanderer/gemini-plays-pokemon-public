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
- Spatial Constraint: Boulders cannot be pushed down from Row 1 because Row 0 is all WALL. Boulder 7 (6, 1) is a decoy.

# Blackthorn City Discoveries
- Pokemon Center: (21, 29).
- Emy's House: (29, 23). Inside: Lass wants to trade DODRIO for female DRAGONAIR.
- Sign at (34, 24): "A Quiet Mountain Retreat"
- Ice Path Exit: (36, 9) on map 5_10.
- Move Deleter's House: (9, 31).
- Dragon Speech House: (13, 21). Inside: Granny and Dratini.
- Blackthorn Gym Entrance: (18, 11). Sign at (17, 13).
- Trainers Defeated: Paul (1, 15) on 1F, Mike (6, 8) on 1F, Fran (4, 11) on 2F, Cody (4, 1) on 2F.
- Gym Guide (7, 15) Advice: Clair uses Dragon-type Pokemon. They are weak against Ice-type moves.

# Strategy: Gym Leader Clair (Battle Analyst Turn 29347)
- Opponent: Clair (Dragon User).
- Team: Dragonair (Lv37) x3 (Surf, Ice Beam, Thunderbolt), Kingdra (Lv40).
- Battle Strategy: Lead with Calcifer (Lv46). Use Thunderpunch as primary attack. Use fodder to heal/revive Calcifer.

# Blackthorn Gym Layout Theory
- 1F Layout: West side contains Ladder (1, 7). East side island contains Ladder (7, 9).
- 2F Layout: Quadrants NW, NE, SW, SE. Row 13 connects East and West sides.
- Pit Destinations:
  - 2F Pit (2, 5) -> 1F (2, 6) [Entry 5]
  - 2F Pit (8, 7) -> 1F (7, 7) [Entry 6]
  - 2F Pit (8, 3) -> 1F (7, 6) [Entry 7]

# Blackthorn Gym Boulder Puzzle Strategy
- Status: Pits (8, 3) and (2, 5) are filled. Pit (8, 7) is EMPTY.
- Goal: Fill Pit (8, 7) using Boulder 5 (6, 16).
- Plan:
  1. Move Boulder 8 (8, 17) to clear Column 8 [Done].
  2. Navigate to (6, 17). [Done]
  3. Push Boulder 5 (6, 8) north to (6, 7). [In Progress: Currently at (6, 8)]
  4. Move to (5, 7), push Boulder 5 right into Pit (8, 7).
- Verification: Boulders 3 and 4 were pushed in turns 29284 and 29318. They remain in pits after reset.

# Reflection & Lessons
- **Turn Tracking:** Sourced from Game State Info.
- **Boulder Persistence:** Pushed boulders stay in pits even if the 2F floor is reset by changing floors.
- **Scientific Method:** Formed hypothesis that Boulder 7 was the key for Pit (8,7). Disproved it by observing Row 0 walls. Revised to Boulder 5.
- **Warp Safety:** Entry points on 1F (6, 7, 5) correspond to specific pits on 2F. Verified via entry point data. (Turn 29374)