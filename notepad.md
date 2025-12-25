# Blackthorn City Strategy

- **Goal:** Earn Rising Badge (Clair).
- **Immediate:** Solve Gym Puzzle (West Side).
- **Next:** Defeat Clair, enter Dragon's Den.

# Tile Mechanics
- **LEDGE_HOP_DOWN**: One-way traversable (South only). Jump over to descend.
- **FLOOR**: Standard walkable tile.
- **WALL**: Impassable obstacle.
- **FLOOR_UP_WALL**: Cliff/Ledge impassable from below.
- **PIT**: Hole in floor. Dropping boulders (or falling) leads to 1F.
- **LADDER**: Vertical transport between floors.
- **BOULDER**: Pushable object (requires Strength). Acts as a wall until moved.
- **WARP**: Transitions to another map or location.

# Blackthorn Gym Strategy
- **Status:** East Side Puzzle Complete (Boulders 4 & 5 dropped).
- **Current Task:** Navigate to West Side via 1F.

## Puzzle State
- **East Side:**
  - Boulder 3 (8, 14): SACRIFICED (Stuck).
  - Boulder 4 (6, 16): SOLVED (Dropped in Pit 8,7).
  - Boulder 5 (8, 2): SOLVED (Dropped in Pit 8,3).
  - Boulder 6 (9, 1): Moved out of way.
- **West Side (To Do):**
  - Boulder 1 (2, 3): Needs to go to Pit (2, 5).
  - Boulder 2 (3, 3): Needs to go to Pit (8, 3)? Wait, Pit (8, 3) is for East side.
  - Re-evaluating West Side Targets:
    - Pit at (2, 5) is the primary target for West.
    - Pit at (8, 3) was used by Boulder 5.
    - Is there another pit? Or do multiple boulders go to the same pit?
    - Hypothesis: Boulder 2 might need to go to Pit (2, 5) as well, or there's another pit I haven't seen/used.
    - Actually, Boulder 2 is at (3, 3). Pit is at (2, 5).
    - Plan: Push B1 (2, 3) South to Pit (2, 5). Then check if B2 is needed or if B1 clears the path on 1F.

# Navigation Correction
- **Issue:** 2F West is divided by a wall at Row 5. Ladder (1, 7) leads to the blocked Bottom section.
- **Solution:** Access Top West 2F via Top West 1F.
- **Path:** 
  1. On 1F, go South to Row 15.
  2. Go East to Column 9.
  3. Go North through gap at (9, 5) to reach Top 1F.
  4. Find Ladder to Top West 2F (likely near Clair).

## Puzzle State
- **East Side:** Complete (Boulders 4 & 5 in Pits).
- **West Side:** Boulders 1 & 2 untouched.

# Key Locations
- **Gym Leader Clair:** 1F (North), currently inaccessible due to lava/channel. Needs boulders to bridge?
- **Ice Path Entrance:** (36, 9)
- **Move Deleter:** Blackthorn City.

# Lessons Learned
- **Verify Paths:** Always check the full path of a boulder push before executing. Boulders getting stuck requires a full room reset.
- **Sacrifice:** Some boulders are decoys or meant to be sacrificed to open paths for others.
- Strength Status: Active.
- Action: Closing text and pushing Boulder 2 (3, 3) North twice to (3, 1).
- Next: Move to (2, 2) -> Push Boulder 1 (2, 3) South to Pit (2, 5).