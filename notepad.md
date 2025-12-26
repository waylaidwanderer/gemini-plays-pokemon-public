# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower -> 2. Cianwood -> 3. Route 42 -> 4. Route 38 Western Ledge (Current) -> 5. Route 14 -> 6. Tin Tower 1F.
- Route 38 Ledge: Reachable ONLY via Olivine -> Route 39 -> Route 38 West.
- Battle Strategy (Tin Tower): Lead XENON (GASTLY). Use MEAN LOOK, HYPNOSIS, and NIGHT SHADE.

# Tile Mechanics (Global)
- FLOOR: Traversable.
- DOOR/WARP/WARP_CARPET_DOWN: Trigger map transition.
- WALL/HEADBUTT_TREE/BERRY_TREE/BUOY/VOID: Impassable.
- TALL_GRASS: Traversable; triggers wild encounters.
- LEDGE_HOP (DOWN/LEFT/RIGHT): One-way traversal.
- WATER: Traversable with Surf.

# Navigation: Fly Map (Johto)
- Discovery (Turn 20966): Linear list navigated by Up/Down.
- Order (Up): New Bark -> Cherrygrove -> Violet -> Azalea -> Goldenrod -> Ecruteak -> Olivine -> Cianwood -> Mahogany -> Blackthorn.

# Plan: Reach Route 38 Western Ledge
- Start Turn: 20970
- Status: Exploring Route 38 Western Ledge for Suicune sighting 4.
- Strategy:
  1. Exit Pokecenter. (Done)
  2. Walk North to Route 39 (exit at 21, 0). (Done)
  3. Walk North to Route 38 West. (Done)
  4. Explore ledge to find Suicune. (In Progress)
  5. Trigger Suicune flee (Scripted).

# Side Quests & Observations
- Arthur (Route 36): Looping introduction on Thursday. Hypothesis: May require specific badge, story trigger (e.g. Radio Tower), or item.
- Clear Bell: Verified in Key Items.

# Lessons Learned
- Fly Map: It is a linear list, not a grid.
- Pathfinding: Be careful with `find_path_v2` near warps to avoid accidental building entry.
- Arthur Loop: Repeated intro x3 without item. Strategy: Pivot if loop persists.
- Pathing Caution: Avoid using find_path_v2 for movements ending adjacent to warps. Walk the final tiles manually.