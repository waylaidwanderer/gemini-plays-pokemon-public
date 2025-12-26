# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower -> 2. Cianwood -> 3. Route 42 -> 4. Route 38 Sighting (Current) -> 5. Route 14 -> 6. Tin Tower 1F.
- Logic: Scripted sightings (1-5) are fixed overworld events. Suicune remains stationary until approached. The Pokedex "AREA" map tracks the roamer, which only begins appearing AFTER the Tin Tower event.
- Battle Strategy (Tin Tower): Lead XENON (GASTLY). Use MEAN LOOK, HYPNOSIS, NIGHT SHADE.

# Tile Mechanics (Global)
- FLOOR: Traversable. [Tested]
- DOOR/WARP: Map transition. [Tested]
- WALL/HEADBUTT_TREE: Impassable. [Tested]
- TALL_GRASS: Traversable; wild encounters. [Tested]
- LEDGE_HOP (DOWN/LEFT/RIGHT): One-way traversal. [Tested]
- Route 38 (3, 9): FLOOR. [Verified via Game State]

# Navigation: Fly Map (Johto)
- Discovery: Linear list navigated by Up/Down.
- Order (Up): New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Blackthorn.

# Plan: Find Suicune on Route 38
- Quest Start: Turn 20970 (Dec 25, 5:00 PM)
- Strategy:
  1. Use Super Repel. (Active: Turn 21106)
  2. Navigate to the trough area on the western side of Route 38 (approx 10, 14).
  3. Trigger Suicune Sighting 4.
  4. Fly to Route 36 to collect Hard Stone from Arthur.

# Side Quests
- Arthur (Route 36): Thursday only. Gives Hard Stone at (15, 7).
- Clear Bell: In Key Items.

# Lessons Learned
- Fly Map: Linear list, not 2D grid. Use Up/Down and check Screen Text.
- Pathfinding: Avoid find_path_v2 near warps to prevent accidental entry. Walk final tiles manually.
- Collision Verification: Verify collision using movement tests before documenting.
- Sprite Identification: Verify sprites before assuming (e.g. Beauty vs Suicune).
- Pokedex Tracking: Pokedex "AREA" map is for the roamer. Scripted sightings are fixed overworld events.
- Week Siblings: Arthur (Thursday) is on Route 36 near the Ruins of Alph path.