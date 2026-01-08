# Game Mechanics & Systems
## Tile Mechanics
- FLOOR / TALL_GRASS: Walkable.
- WALL / COUNTER / FLOOR_UP_WALL (from North): Impassable.
- LEDGE_HOP_DOWN (⤵️): One-way jump North to South.
- NPCs: Impassable walls.
- Blackthorn Elevation: Tiered city. Gaps in ledges allow Northward walking (e.g., 13,17; 9,21; 13,23).
- Pits (Blackthorn Gym): One-way warp to the same coordinates on the floor below.
- Ladders (Blackthorn Gym): Two-way warp between floors.

# Pokemon & Party Information
## Strategy for Gym Leader Clair
- Goal: Acquire Rising Badge.
- Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Tactical Plan:
  - Lead Calcifer (Typhlosion, Lv49): Use Return (max happiness) or Thunderpunch for consistent neutral damage. Level advantage is key.
  - Xenon (Haunter, Lv36): Backup status support (Hypnosis/Confuse Ray). Haunter is immune to Normal moves.
  - Gneiss (Graveler, Lv48): Backup physical bulk. Beware of Surf/Ice Beam.

# Exploration Strategy
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Strategy: Use the `solve_gym_puzzle` tool to find the optimal sequence.

# Obstacles & Solutions
- Accessing Route 45 East: Use Column 39 corridor in Blackthorn City. Entrance at (39, 8).