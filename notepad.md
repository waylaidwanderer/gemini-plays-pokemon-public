# Blackthorn City Strategy

- **Goal:** Earn Rising Badge (Clair).
- **Immediate:** Locate Pokemon Center & Heal.
- **Next:** Clear Bag Space, Challenge Gym.

# Tile Mechanics
- **LEDGE_HOP_DOWN**: One-way traversable (South only). Jump over to descend.
- **FLOOR**: Standard walkable tile.
- **WALL**: Impassable obstacle.
- **FLOOR_UP_WALL**: Cliff/Ledge impassable from below.

# Key Locations
- **Ice Path Entrance:** (36, 9)
- **Cooltrainer F:** (35, 19)
- **Sign (34, 24):** "Blackthorn City - A Quiet Mountain Retreat"

# Archived: Ice Path
- Solved. Exited via 1F East.
- **Emy's House:** Located at (29, 23). Contains Lass (Emy?).
- **Observation:** Row 28 (Cols 31-35) is blocked by a cliff/wall (`FLOOR_UP_WALL`).
- **Pathing:** Must route West to Col 29 to proceed South.
- **Observation:** Row 32 (Cols 25-29) is `FLOOR_UP_WALL` (Cliff). Path South is blocked here.
- **Pathing:** Must investigate West of Col 25.
- **NPC:** Black Belt at (25, 31), facing Left. Avoid line of sight if avoiding battle.