# Strategy for Ecruteak City
1. Defeat the 5 Kimono Girls in the Dance Theater to get HM03 Surf. (COMPLETED)
2. Defeat Gym Leader Morty (Ghost/Poison).
3. Explore Burned Tower.

# Key Items & Progress
- HM03 Surf obtained from Gentleman in Dance Theater (Turn #4888).
- Plain Badge (Whitney): Used Strength outside battle, increases Speed.
- Hive Badge (Bugsy): Used Cut outside battle.
- Zephyr Badge (Falkner): Used Flash outside battle.

# Gym Prep: Morty (Ghost)
- Team: Gastly, Haunter, Gengar (Ghost/Poison).
- Weaknesses: Ground, Psychic, Ghost, Dark.
- Strategy: Use GNEISS (Graveler) with Magnitude.

# PC Storage
## Box 1 (Current)
- Blarney (SUDOWOODO) Lv20
- ROCKY (ONIX) Lv6
- ICARUS (PIDGEY) Lv11

## Party
- GNEISS (GRAVELER) Lv26: STAB Magnitude.
- Calcifer (QUILAVA) Lv27
- FRITTATA (TOGEPI) Lv5
- KIMCHI (ODDISH) Lv7
- EGG (CLEFFA) Lv5

# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable. Chance of wild encounters.
- LEDGE_HOP_DOWN: One-way traversable (down only).
- WARP_CARPET: Map transition point.
- Objects (NPCs, Signs): Impassable. Interaction from adjacent tile.
- WARP (Hole/Ladder): Triggers map transition.

# Type Effectiveness (Verified)
- Normal vs Dark (Umbreon): Neutral damage.
- Normal vs Psychic (Espeon): Neutral damage.
- Ground vs Dark (Umbreon): Neutral damage.
- Ground vs Ghost/Poison (Gastly): Super Effective.
- Fire vs Dark (Umbreon): Neutral damage.
- Fire vs Psychic (Espeon): Neutral damage.

# Trainer Rosters (Dance Theater)
- Miki: Jolteon
- Kuni: Vaporeon
- Zuki: Umbreon
- Sayo: Espeon
- Naoko: Flareon

# Burned Tower 1F (3_13)
- Entrance: (9, 15) and (10, 15) from Ecruteak City (4, 4).
- Eusine (ID 2) at (9, 14): Searching for Suicune.
- Morty (ID 4) at (14, 15): Ecruteak Gym Leader.
- Holes to B1F: (5, 14), (14, 14), (15, 14), (7, 15).

# Next Steps
- Teach Surf to a Pokemon (Need to catch a Water-type).
- Investigate Burned Tower at (4, 4).
- Challenge Gym Leader Morty at (10, 27).
- Youngster at (11, 13) mentioned rampaging Pokémon at Lake of Rage (Turn #4900).
- Rival Malice (ID 3) at (8, 9) in Burned Tower 1F.

# Lessons Learned
- Always check for `is-warp="true"` in map XML before planning paths in dangerous areas like Burned Tower.
- Use `find_path` tool to avoid manual coordinate errors.
- Mark all holes/warps immediately to assist pathfinding logic.
- Rival Malice Battle (Turn #4945):
  - Malice sent out Haunter (Lv 20).
  - GNEISS (Lv 26) is leading. Strategy: Magnitude.