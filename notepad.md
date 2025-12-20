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
- GNEISS (GRAVELER) Lv27: STAB Magnitude.
- Calcifer (QUILAVA) Lv27
- FRITTATA (TOGEPI) Lv5
- KIMCHI (ODDISH) Lv10
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
- Ground vs Ghost/Poison (Haunter): Super Effective.
- Fire vs Dark (Umbreon): Neutral damage.
- Fire vs Psychic (Espeon): Neutral damage.
- Rock vs Flying/Poison (Zubat): Super Effective (4x).

# Trainer Rosters
## Dance Theater
- Miki: Jolteon, Kuni: Vaporeon, Zuki: Umbreon, Sayo: Espeon, Naoko: Flareon.
## Burned Tower
- Malice defeated (Turn #4982): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18.

# Ecruteak City (4_9)
- Burned Tower Entrance: (5, 5).
- Pokemon Center: (23, 27).
- Dance Theater: (23, 21).
- Tin Tower Entrance: (18, 11).
- Ecruteak Gym Entrance: (6, 27).
- Building at (5, 21).
- Building at (13, 27).
- Strategy: Heal at PC, then challenge Morty.
- City Navigation Start: Turn #5019.

# Burned Tower 1F (3_13)
- Entrance: (9, 15) and (10, 15) from Ecruteak City (4, 4).
- Morty and Eusine have left the tower (Turn #5015). Morty likely returned to the Gym.
- Holes to B1F: (5, 14), (14, 14), (15, 14), (7, 15), (10, 9), (4, 14), (15, 4), (15, 5), (5, 5), (5, 6), (4, 6).

# Burned Tower B1F (3_14)
- Exit Ladder: (7, 15).
- Arrival from 1F hole: (10, 9).
- Legendary Beasts: Released (Turn #4995). Raikou, Entei, and Suicune fled.
- Strategy: Exit via (7, 15), check 1F, then proceed to Ecruteak Gym.
- Exit Attempt Start: Turn #5009.

# Exploration Targets
- Reachable unseen tiles on B1F: (To be refreshed by tool).
- Unseen tiles adjacent to walkable (1F): (15, 0), (16, 0), (18, 3-8).

# Defeated Trainers
- Malice (Burned Tower 1F): Haunter Lv20, Croconaw Lv22, Zubat Lv20, Magnemite Lv18. (Turn #4982)

# Ecruteak Pokecenter 1F (4_3)
- Nurse: (3, 1) area (behind counter).
- PC: (9, 1) area.
- Gym Guide: (7, 1) area.
- Strategy: Talk to Nurse from (3, 2) to heal.
- Tile Mechanics Update: COUNTER (Impassable, interact over it).
- Heal Attempt Complete: Turn #5027. Party at 100%.

# Ecruteak Gym (4_7)
- Entrance/Exit: (4, 17) and (5, 17).
- Sage Ping: (3, 13).
- Gym Guide Advice: Trainers have secret motives; winning reveals secrets about Ecruteak.
- Pit Warps (Reset to start): (4, 14), (3, 12), (4, 12), (5, 12), (7, 12), (7, 13).
- Invisible Path Puzzle: The floor appears to have pits that warp the player back to the start.
- Strategy: Identify the safe path by testing adjacent tiles. Document safe coordinates.
- Start Turn: #5034.

# Tile Mechanics Update
- PIT: Warp tile that resets position to the Gym entrance.
- FLOOR: Generally safe, but in this Gym, some FLOOR tiles might be adjacent to invisible PITS.
- STATUE: Impassable background object.

# Safe Path Findings (is-warp='false')
- Row 16: (0-9, 16)
- Row 15: (0-2, 15), (4-5, 15), (7-9, 15)
- Row 14: (0-2, 14), (5, 14), (7-9, 14)
- Row 13: (2, 13), (3, 13), (4, 13), (5, 13), (6, 13)
- Row 12: (0, 12), (6, 12), (9, 12)
- Row 11: (0, 11), (3, 11), (4, 11), (5, 11), (6, 11)
- Row 10: (0, 10), (3, 10), (6, 10)
- Row 9: (0, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9)

# Pit Warps Discovered (is-warp='true')
- Row 14: (4, 14)
- Row 13: (7, 13)
- Row 12: (2, 12), (3, 12), (4, 12), (5, 12), (7, 12)
- Row 11: (2, 11), (7, 11)
- Row 10: (2, 10), (4, 10), (5, 10), (7, 10)
- Row 9: (2, 9)

# Strategy
- Avoid all tiles with `is-warp='true'` or Pit markers.
- Use `find_path` to navigate between safe tiles.