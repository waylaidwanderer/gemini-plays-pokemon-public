# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.
- Hunt started Turn 20250.

# Side Quests & Resources
- Quick Claw: National Park (17, 10). Talk to lady on the rightmost bench in NE section. (Available Morning/Day/Night).
- Clear Bell: In Key Items. Required for Tin Tower.
- Sick Miltank (Moomoo Farm): Needs many Berries to recover.

# Route 38/39 Mechanics & Exploration
- Tile Mechanics (Verified):
  - LEDGE_HOP_DOWN (Y=13, 15): One-way South.
  - LEDGE_HOP_LEFT (X=10): One-way West.
  - LEDGE_HOP_RIGHT (X=7, 21): One-way East.
  - WALL / FENCE: Impassable.
  - TALL_GRASS / LONG_GRASS: Traversable, wild encounters.
- Lane Analysis:
  - Top Lane (Rows 0-6): Fragmented by walls. Eastern Pocket (X=16-39) reachable via gaps at X=30-35. Middle Pocket (X=4-5) reachable via gaps at X=4-5. Western Pocket (X=0-2) is isolated from south.
  - One-Way Restriction: Route 38 is effectively a one-way path West due to ledges at X=7 and X=10. Walking from Olivine to Ecruteak is impossible.
- Search Log:
  - Middle Pocket (X=4-5): Searched. No Suicune.
  - Western Pocket (X=0-2): Unexplored.
  - Eastern Pocket (X=16-39): Unexplored.
- Current Plan: Approach Route 38 from Ecruteak (East) and stay in the Top Lane (Rows 0-6) while walking West. This is the only way to reach isolated sections where Suicune (Sighting #4) is waiting near the Miltank farm.

# Lessons Learned
- Menu Mechanics: Use single button presses or "B-reset" (press B 4 times) for deep menus to avoid cursor persistence errors (e.g., the Fly Loop failure Turn 20304-20341).
- Pokedex Navigation: Wrapping from #001 to #251 is faster.
- Suicune Tracking: Overworld sightings don't register in Pokedex. Tracking is impossible until roaming starts after Tin Tower.
- False Constraints: Don't assume you can walk back to missed spots on routes with ledges. Pivot to Fly immediately.
- Dana (Lass) called: Has a gift for me. She is waiting on Route 38.