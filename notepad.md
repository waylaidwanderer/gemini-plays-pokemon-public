# Quest Log
- **Goal:** Defeat Blue at Viridian Gym (Earth Badge).
- **Badges:** 15/16 (Volcano Badge obtained).
- **Next:** Travel to Viridian City.

# Current Strategy: Viridian City
- **Location:** Viridian City (Outside Pokemon Center).
- **Status:** Navigating manually to (23, 25) because `find_path` failed to see Ledges as obstacles from the South.
- **Action:** Move Left to gap at (19, 27), then to Pokemon Center door.
- **Goal:** Heal at Pokemon Center.
- **Tool Note:** `find_path` needs fixing to treat `LEDGE_HOP_DOWN` as a wall when moving North.

# Tile Mechanics
- **LEDGE_HOP_DOWN:** One-way South.
- **WARP_CARPET:** Step on to exit map.
- **CUT_TREE:** Obstacle unless Cut is used.
- **PIT:** Drops player to floor below.
- **LADDER:** Transitions between floors.
- **FLOOR_UP_WALL:** Acts as a wall when approaching from above (North).
- **BUOY:** Water boundary/Wall.

# Reflection (Turn 24875)
- **Status:** Traversing Route 1 Northbound.
- **Lesson:** Red's Mom (Pallet Town) does not heal the player in this version.
- **Strategy:** Bypass ledges via the gap at Cols 4-6. Flank Cooltrainer F (9, 25) by staying on the left (she faces Right).
- **Next:** Reach Viridian City Pokemon Center.