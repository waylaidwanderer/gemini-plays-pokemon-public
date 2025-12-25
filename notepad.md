# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.
- Hunt started Turn 20250.

# Side Quests & Resources
- Quick Claw: National Park (17, 10). Talk to lady on the rightmost bench in NE section. (Available Morning/Day/Night).
- Clear Bell: In Key Items. Required for Tin Tower.
- Sick Miltank (Moomoo Farm): Needs many Berries to recover.
- Thunderstone: Obtained from Dana (Route 38) at Turn 20360.

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL / FENCE: Impassable.
- LEDGE_HOP_DOWN (Y=13, 15): One-way South.
- LEDGE_HOP_LEFT (X=10): One-way West.
- LEDGE_HOP_RIGHT (X=7, 21): One-way East.
- TALL_GRASS / LONG_GRASS: Traversable, wild encounters.
- HEADBUTT_TREE: Impassable, interact for encounter.
- WARP_CARPET_RIGHT / LEFT: Traversable, triggers map transition.

# Route 38/39 Mechanics & Exploration
- Lane Analysis:
  - Top Lane (Rows 0-6): Fragmented by walls. 
    - Western Pocket (X=0-2): Isolated from south/east.
    - Middle Pocket A (X=4-5): Reachable via gap at (4, 7).
    - Middle Pocket B (X=8-9): Reachable via gap at (8, 7).
    - Eastern Strip (X=16-35): Reachable via Ecruteak or gaps at X=30-35.
  - One-Way Restriction: Route 38 is effectively a one-way path West due to ledges at X=7 and X=10. Walking from Olivine to Ecruteak is impossible.
- Search Log:
  - Top Lane Eastern Strip (X=16-35): Searched. No Suicune.
  - Top Lane Middle Pocket A (X=4-5): Searched. No Suicune.
  - Top Lane Middle Pocket B (X=8-9): Unexplored.
  - Top Lane Western Pocket (X=0-2): Unexplored. Isolated.
  - Route 39 Barn: Searched. No Suicune.
- Current Plan: 
  1. Search Middle Pocket B (X=8-9) on Route 38.
  2. Investigate Row 0-1 for a path to the Western Pocket (X=0-2).
  3. Approach Suicune (Sighting #4) near the Miltank farm.
  4. Head to National Park (via Route 36) to obtain the Quick Claw from the lady at (17, 10).

# Lessons Learned
- Menu Mechanics: Use single button presses or "B-reset" (press B 4 times) for deep menus to avoid cursor persistence errors.
- Suicune Tracking: Overworld sightings don't register in Pokedex. Tracking is impossible until roaming starts after Tin Tower.
- False Constraints: Don't assume you can walk back to missed spots on routes with ledges. Pivot to Fly immediately.
- Bug Catching Contest: Active today (Thursday). May affect National Park access.