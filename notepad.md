# Strategy: Suicune Hunt (Crystal)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 -> 5. Route 14 -> 6. Tin Tower.
- Battle Plan (Tin Tower): 1. Hypnosis, 2. Night Shade (Fixed 21 dmg), 3. Catch.
- Hunt started Turn 20250.

# Tile Mechanics (Verified)
- WALL: Impassable.
- FLOOR: Standard traversable tile.
- COUNTER: Impassable; interact from front.
- WARP_CARPET: Warp tile; triggers map transition.
- LADDER: Warp tile; triggers warp when stepping on.
- PC: Impassable; interact from below.
- TALL_GRASS / LONG_GRASS: Wild encounters.
- LEDGE_HOP_DOWN: One-way North -> South.
- LEDGE_HOP_LEFT: One-way East -> West.
- LEDGE_HOP_RIGHT: One-way West -> East.
- HEADBUTT_TREE: Interact for encounter/event.
- CUT_TREE: Requires CUT to remove.
- WATER: Requires SURF to traverse.
- TOWN_MAP / WINDOW / BOOKSHELF / TV / RADIO: Background objects.
- Fences: Act as WALL tiles. Gaps at (3, 8) and (3, 11) allow passage between Route 38 strips.

# Route 38/39 Mechanics
- Valley Trap: (8, 12) area is blocked north by ledges. Exit south or Fly.
- Ledge Pocket: (12, 14) area requires Fly to exit.
- Moomoo Farm: (3, 7) on Route 39 leads to farmhouse.

# Lessons Learned
- Pokedex Navigation: Wrapping from #001 to #251 is faster.
- Menu Mechanics: Use a "B-reset" (press B 4 times) before navigating deep menus to clear cursor persistence.
- Hallucination Warning: Beauty Olivia (5, 8) is NOT Suicune.

# Side Quests
- Quick Claw: National Park (16, 12). Talk to Teacher on bench in NE section.
- Yanma Swarm: Caught.
- Sick Miltank (Moomoo Farm): Needs many Berries to recover.
- Suicune Hunt: Started Turn 20250. Currently on Sighting #4 (Route 38).

# Resources
- Clear Bell: In Key Items. Required for Tin Tower.

# Route 38 Lane Analysis
- Top Lane: Row 0-6. Contains Suicune sighting #4 at the western end. Reachable only from Ecruteak City by staying North.
- Middle Lane: Row 8-10. Contains Beauty Olivia. Connects to Route 39 main road.
- Bottom Lane: Row 12-14. Contains "Ledge Pocket" and "Valley Trap". Entrance via ledge hop at Row 11/13. Requires Fly to exit.
- Vertical Walls: Solid walls at X=11 and X=16 on Route 38, and X=16 on Route 39, enforce lane separation.