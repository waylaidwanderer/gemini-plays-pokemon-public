# Game Mechanics & Systems
## Tile Mechanics
- FLOOR / TALL_GRASS: Walkable.
- WALL / COUNTER: Impassable.
- LEDGE_HOP_DOWN (⤵️): One-way jump North to South.
- FLOOR_UP_WALL: Verified as impassable from the North in current strategy, but engine typically allows jumping DOWN. Need to verify by attempting to move South from (37, 19) to (37, 20).
- Blackthorn Elevation: Tiered city separated by ledges/walls. Gaps allow Northward walking.
- Pits (Blackthorn Gym): Drop the player to the same coordinates on the floor below.

# Pokemon & Party Information
## Strategy for Gym Leader Clair
- Clair's Team: Dragonair x3 (Lv37), Kingdra (Lv40).
- Matchups: Dragon resists Fire, Water, Electric, Grass. Kingdra (Water/Dragon) is only weak to Dragon. Haunter (Xenon) is immune to Normal. Haunter's Night Shade does fixed damage (36). Haunter's Hypnosis/Confuse Ray can disable.
- Tactical Plan:
  - Lead Calcifer (Lv49): Use Return for high neutral damage. Calcifer's level advantage is key.
  - Xenon (Lv36): Backup for Hypnosis/Confuse Ray support if Calcifer is weakened.
  - Gneiss (Lv48): Backup, but beware of Surf/Ice Beam. Earthquake for neutral damage.

# Exploration Strategy
## Blackthorn Gym Boulder Puzzle (2F)
- Goal: Push boulders into pits to bridge gaps on 1F.
- Boulder 6 (3, 3) -> Pit (2, 5):
  1. Push Down from (3, 2) to (3, 4).
  2. Push Left from (3, 4) to (2, 4).
  3. Push Down from (2, 3) to (2, 5).
- Boulder 7 (6, 1) -> Pit (8, 3):
  1. Push Right from (5, 1) to (7, 1).
  2. Push Right from (7, 1) to (8, 1).
  3. Push Down from (8, 2) to (8, 3).
- Boulder 8 (8, 14) -> Pit (8, 7):
  1. Push Up from (8, 15) to (8, 7). (Verify pathing around walls).

# Obstacles & Solutions
- Accessing Route 45 East: Use Column 39 corridor. Entrance at (39, 8).

# Lessons Learned
- Blackthorn Gym 2F: Column 4 is mostly walls, but gaps exist in Row 11 and below.
- Boulder Puzzles: If a push seems blocked by a wall, check if the player can reach the other side of the boulder via a different floor or a gap.
- Hallucination Check (Turn #34046): Verified that (37, 20) in Blackthorn City is likely a wall face (FLOOR_UP_WALL) which is impassable from the north. The eastern strip access via Column 39 is the correct hypothesis.
- Pathing: Defeated trainers remain as obstacles in this game engine.