# Game Mechanics & Systems
## Tile Mechanics
- FLOOR / TALL_GRASS: Walkable.
- WALL / COUNTER / FLOOR_UP_WALL (from North): Impassable.
- LEDGE_HOP_DOWN (⤵️): One-way jump North to South.
- NPCs: Impassable walls (even after defeat).
- Blackthorn Elevation: Tiered city. Gaps in ledges allow Northward walking (e.g., 13,17; 9,21; 13,23).
- Pits (Blackthorn Gym): One-way warp to same coords on floor below. Hypothesis: Filling pits on 2F bridges paths on 1F.
- Ladders (Blackthorn Gym): Two-way warp between floors. Usually triggers by stepping ON, but may require 'A' press.

# Pokemon & Party Information
## Training Session (Route 45)
- Start: Turn #33584.
- Goal: Kimchi (Lv33) and Xenon (Haunter, Lv36) to Lv40.
- Method: Kimchi holds Exp. Share. Lead Xenon.

## Strategy for Gym Leader Clair
- Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Tactical Plan:
  - Lead Calcifer (Typhlosion, Lv49): Use Return (max happiness) or Thunderpunch for consistent neutral damage. Level advantage is key.
  - Xenon (Haunter, Lv36): Backup status support (Hypnosis/Confuse Ray). Haunter is immune to Normal moves.
  - Gneiss (Graveler, Lv48): Backup physical bulk. Beware of Surf/Ice Beam.

# Exploration Strategy
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push 3 boulders into pits on 2F to bridge gaps on 1F.
- Verified Pits (2F): (2, 5), (8, 3), (8, 7).
- Current Boulder Positions: Boulder 6 (3, 3), Boulder 7 (6, 1), Boulder 8 (8, 14).
- Strategy: follow the `solve_gym_puzzle` output exactly.

# Obstacles & Solutions
- Accessing Route 45 East: Use Column 39 corridor in Blackthorn City. Entrance at (39, 8).
- Gym Navigation: Use Column 4 gap at (4, 13) or Row 1 to cross between left and right sides.