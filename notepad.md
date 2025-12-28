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
- Gym Sign: (17, 13).
- Water area: (12, 12) to (15, 13).

# Strategy: Gym Leader Clair
- Opponent: Clair (Dragon User).
- Team (Crystal): Dragonair (Lv37) x3, Kingdra (Lv40).
- Party Status: Calcifer (Lv45), Gneiss (Lv44) are main fighters. Others are underleveled (Lv10-21).
- Battle Strategy (battle_analyst_v2 - Verified):
  - Lead with Calcifer.
  - Dragonairs use Dragonbreath, Surf, Ice Beam, Thunderbolt, and Thunder Wave.
  - Gneiss is immune to Thunderbolt, but 4x weak to Surf and 2x weak to Ice Beam. Use with extreme caution.
  - Kingdra uses Dragonbreath, Surf, Smokescreen, and Hyper Beam.
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

# Tile Mechanics Update
- WATER: Requires Surf to traverse.
- DOOR: Warp tile.
- LEDGE_HOP_DOWN: One-way movement (North to South).
- CAVE: Warp tile.