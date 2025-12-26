# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower -> 2. Cianwood -> 3. Route 42 -> 4. Route 38 Sighting (Current) -> 5. Route 14 -> 6. Tin Tower 1F.
- Logic: Suicune is stationary in scripted spots until Tin Tower. The Pokedex "AREA" dot shows the scripted location.
- Battle Strategy (Tin Tower): Lead XENON (GASTLY). Use MEAN LOOK, HYPNOSIS, NIGHT SHADE.

# Tile Mechanics (Global)
- FLOOR: Traversable.
- DOOR/WARP: Map transition.
- WALL/HEADBUTT_TREE: Impassable.
- TALL_GRASS: Traversable; wild encounters.
- LEDGE_HOP (DOWN/LEFT/RIGHT): One-way traversal. Can only jump in the direction indicated.
- Route 38 (3, 9): Verified traversable FLOOR despite WALL label.

# Navigation: Fly Map (Johto)
- Discovery: Linear list navigated by Up/Down.
- Order (Up): New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Blackthorn.

# Plan: Find Suicune on Route 38
- Objective: Trigger Sighting 4.
- Strategy:
  1. Check Pokedex AREA map for the exact location dot.
  2. Navigate to the blinking dot on Route 38.
  3. Look for the Suicune overworld sprite.

# Side Quests
- Arthur (Route 36): Thursday only. Gives Hard Stone. (Check today!)
- Clear Bell: In Key Items.

# Lessons Learned
- Fly Map: Linear list, not 2D grid. Use Up/Down and check Screen Text.
- Pathfinding: Avoid find_path_v2 near warps to prevent accidental entry. Walk final tiles manually.
- Collision Verification: Some WALL-labeled tiles (like Route 38 (3, 9)) are traversable. Test everything.
- Sprite Identification: Verify sprites before assuming (e.g. Beauty vs Suicune).