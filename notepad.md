# Blackthorn City Strategy

- **Goal:** Earn Rising Badge (Clair).
- **Immediate:** Defeat Cooltrainer Lola, reach Clair.
- **Next:** Defeat Clair, enter Dragon's Den.

# Blackthorn Gym Strategy
- **Status:** All Puzzles Solved. Both bridges on 1F East are formed.
- **Current Task:** Reach Gym Leader Clair (1F North-East).
- **Navigation:**
  - Currently at (9, 3) on 1F.
  - Path: Cross bridge at (8, 3) West to reach Clair at (5, 3).

## Puzzle State
- **East Side:** Complete (Boulders 4 & 5 in Pits).
- **West Side:** Complete (Boulder 1 in Pit).

# Key Locations
- **Gym Leader Clair:** 1F (5, 3).
- **Ice Path Entrance:** (36, 9).
- **Move Deleter:** Blackthorn City.

# Lessons Learned
- **Verify Paths:** Always check the full path of a boulder push before executing.
- **Sacrifice:** Some boulders are decoys.
- **1F Layout:** The 1F West and East sides are isolated by a central wall; must use 2F to cross.

# Tile Mechanics
- **LEDGE_HOP_DOWN**: One-way traversable (South only).
- **FLOOR**: Standard walkable tile.
- **WALL**: Impassable obstacle.
- **FLOOR_UP_WALL**: Cliff/Ledge impassable from below.
- **PIT**: Hole in floor. Drops to 1F.
- **LADDER**: Vertical transport.
- **BOULDER**: Pushable object.
- **WARP**: Map transition.