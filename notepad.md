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
- Strategy: Manually solve the puzzle using a step-by-step plan.
- Boulder 7 (6, 1) -> Pit (8, 3):
  1. From (5, 1), push Right. B7 moves to (7, 1). Player to (6, 1).
  2. From (6, 1), push Right. B7 moves to (8, 1). Player to (7, 1).
  3. From (7, 1), push Right. B7 moves to (9, 1). Player to (8, 1).
  4. Move Down to (8, 2), then Right to (9, 2).
  5. From (9, 2), push Left. B7 moves to (8, 2). Player to (9, 2).
  6. Move Up to (9, 1), then Left to (8, 1).
  7. From (8, 1), push Down. B7 falls into Pit (8, 3).
- Boulder 6 (3, 3) -> Pit (2, 5): (Plan pending verification of reachable tiles around (4, 3)-(4, 5)).
- Boulder 8 (8, 14) -> Pit (8, 7): (Plan pending verification).
- Observation: (5, 0), (7, 0), (8, 0) are walls. Column 4 is mostly walls. Column 6 is mostly walls. Row 4 is mostly walls. Row 1 is a key traversal route.
- Current Status: Strength is active. Standing at (5, 1) facing Boulder 7 at (6, 1). Ready to execute Step 1.

# Obstacles & Solutions
- Accessing Route 45 East: Use Column 39 corridor in Blackthorn City. Entrance at (39, 8).
- Gym Navigation: Use Column 4 gap at (4, 13) or Row 1 to cross between left and right sides.