# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
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
- Black Belt NPC: (25, 31).
- Ice Path Exit: (36, 9) on map 5_10 (Warp from 3_61 at 36, 27).
- Move Deleter's House: (9, 31).
- Dragon Speech House: (13, 21). Inside: Granny and Dratini (Ekans sprite).
- Blackthorn Gym Entrance: (18, 11). Sign at (17, 13).
- Water area: (12, 12) to (15, 13).
- Super Nerd NPC: (19, 12).
- Youngster NPC: (12, 15).

# Blackthorn Gym Exploration
- Gym Guide (7, 15) Advice: Clair uses Dragon-type Pokemon. They are weak against Ice-type moves.
- Gym Layout: 1F seems to have multiple paths and statues. Likely requires a puzzle from 2F.
- Trainers Defeated: Paul (1, 15).
- Strategy:
  1. Defeat Gym Trainers for EXP [Current: Turn 29227]
  2. Solve Gym Puzzle (2F/1F) [Started: Turn 29238]
  3. Defeat Gym Leader Clair.

# Strategy: Gym Leader Clair
- Opponent: Clair (Dragon User).
- Team (Crystal): 
  - Dragonair (Lv37): Dragonbreath, Surf, Thunder Wave, Slam.
  - Dragonair (Lv37): Dragonbreath, Ice Beam, Thunder Wave, Slam.
  - Dragonair (Lv37): Dragonbreath, Thunderbolt, Thunder Wave, Slam.
  - Kingdra (Lv40): Dragonbreath, Surf, Smokescreen, Hyper Beam.
- Party Status: Calcifer (Lv46), Gneiss (Lv44) are main fighters. Others are underleveled (Lv10-21).
- Battle Strategy (battle_analyst_v2 - Verified):
  - Lead with Calcifer.
  - Gneiss is immune to Thunderbolt, but 4x weak to Surf and 2x weak to Ice Beam. Use with extreme caution.
  - Strategy: Chip away at Kingdra with Calcifer. Switch to Gneiss to tank Hyper Beam (Rock resists Normal), then use recharge turn to attack or switch. Use others as fodder for safe switching/healing.

# History (Archive)
- Ice Path Items: TM44 Rest (B2F), PP UP (1F), PROTEIN (1F).
- Rescued Director from Team Rocket in Goldenrod.
- Disbanded Team Rocket at Goldenrod Radio Tower.

# Reflection Lessons (Turn 29216)
- **Verification:** Always verify Agent/NPC claims about party movesets against Game State Information. (Avoided "Graveler with Thunderbolt" error).
- **Turn Tracking:** Turn numbers must be sourced directly from Game State Information to avoid hallucinations.
- **Water Navigation:** The water at (12, 11)-(15, 13) may require Surf/Whirlpool to access the Gym or other key areas.
- **Warp Marking:** Visit and mark all discovered warps immediately to prevent navigation errors.

# Blackthorn Gym Puzzle (1F)
- Observation: The ladder at (7, 9) is in an isolated section (X=5-7, Y=8-10).
- Blockages: WALLs at (5-7, 11), (4, 8-11), and (8, 8-10).
- Hypothesis: Row 7 (currently unseen) provides a path to enter the ladder section from the north.
- Test: Navigate to the left side (Row 8), enter Row 7, and attempt to reach the ladder from the north. [Turn 29239]
- Attempt 1: Moving to (1, 8) to access Row 7. Conclusion: Failed. Path blocked by WALL at (3, 14).
- Attempt 2: Use Row 16 (all FLOOR) to reach the left side, then head north. [Turn 29240]. Conclusion: Failed. NPC at (1, 15) blocks the path.
- Attempt 3: Move to Column 0 (clear of NPCs), then head north to Row 8/7. [Turn 29241]
- Path: (1, 16) -> (0, 16) -> (0, 8) -> (0, 7).
- Attempt 4: Use the ladder at (1, 7) or (2, 6) to reach 2F. [Turn 29242]