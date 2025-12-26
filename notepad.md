# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower -> 2. Cianwood -> 3. Route 42 -> 4. Route 38 Sighting (Current) -> 5. Route 14 -> 6. Tin Tower 1F.
- Logic: Scripted sightings are fixed overworld events. Suicune remains stationary until approached. The Pokedex "AREA" map tracks the roamer, which only appears AFTER Tin Tower.
- Battle Strategy (Tin Tower): Lead XENON (GASTLY). Use MEAN LOOK, HYPNOSIS, NIGHT SHADE.

# Tile Mechanics (Global)
- FLOOR: Traversable. (Verified)
- DOOR/WARP: Map transition. (Verified)
- WALL/HEADBUTT_TREE: Impassable. (Verified)
- TALL_GRASS: Traversable; wild encounters. (Verified)
- LEDGE_HOP (DOWN/LEFT/RIGHT): One-way traversal. (Verified)
- Route 38 (3, 9): Confirmed WALL via movement test.

# Navigation: Fly Map (Johto)
- Discovery: Linear list navigated by Up/Down.
- Order (Up): New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Blackthorn.

# Plan: Find Suicune on Route 38
- Quest Start: Turn 20970 (Dec 25, 5:00 PM)
- Strategy:
  1. Navigate to the western side of Route 38, near the Route 39 gate.
  2. Look for the Suicune overworld sprite (Sighting 4).

# Side Quests
- Arthur (Route 36): Thursday only. Gives Hard Stone at (15, 7).
- Clear Bell: In Key Items.

# Lessons Learned
- Fly Map: Linear list, not 2D grid. Use Up/Down and check Screen Text.
- Pathfinding: Avoid find_path_v2 near warps to prevent accidental entry. Walk final tiles manually.
- Collision Verification: Verify collision using movement tests before documenting. (3, 9) confirmed as WALL.
- Sprite Identification: Verify sprites before assuming (e.g. Beauty vs Suicune).
- Pokedex Tracking: Pokedex "AREA" map is for the roamer. Scripted sightings are fixed overworld events.
- Week Siblings: Arthur (Thursday) is on Route 36 near the Ruins of Alph path.