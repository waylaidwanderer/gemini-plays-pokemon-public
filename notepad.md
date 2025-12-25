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
- Top Lane: Rows 0-6. Divided into pockets by vertical walls. Eastern Pocket (X=16-39) contains Lass Dana and Sailor Harry; reachable via Row 7 gaps at X=30-32 and X=34-35. Middle Pocket (X=4-5) reachable via Row 7 gaps at X=4-5. Western Pocket (X=0-2) is isolated; connects to Route 39 strip.
- Middle Lane: Rows 8-10. Main path. Contains Beauty Olivia and Beauty Valerie. Heavily restricted by one-way ledges (X=7, X=10) and walls (X=6, X=14). Passage from Olivine to Ecruteak is blocked for walking.
- Bottom Lane: Rows 12-14. Contains "Ledge Pocket" and "Valley Trap". One-way entry from North via ledges at Y=13.
- Vertical Walls: Solid walls at X=3, X=6, X=10, X=15 on Route 38, and X=16 on Route 39, enforce lane separation.
- Fence Gaps (Row 7): X=4, 5, 30, 31, 32, 34, 35. Allows passage between Top and Middle lanes.

# Reflection (Turn 20300)
- Lane Trap: Route 38 is divided into Top, Middle, and Bottom lanes. Suicune is in the Top Lane. Middle lane is a dead end for the hunt.
- Menu Error: Accidental Pack menu entry caused delay. Use B-reset tool to ensure clean state.
- Strategy Pivot: Fly to Ecruteak to access Top Lane.
- Falsification: Proved Middle Lane is isolated by attempting all adjacent tiles and observing ASCII map. Found no gap to Top Lane.
- Start Turn for Hunt: 20250. Current Turn: 20300. (50 turns elapsed).
- Suicune scripted encounters (Burned Tower, Cianwood, Route 42) do NOT register in Pokedex. Tracking via Pokedex is impossible until roaming starts after the Tin Tower event.
- Western Pocket (Route 38 X=0-2 / Route 39 X=16-19) is isolated from the Middle Pocket (X=4-5) by a wall at X=3 on Route 38.
- Entrance to Western Pocket must be a gap in the Row 7 fence at X=0, 1, or 2 on Route 38. Checking this now.
- Search Log (Route 38):
  - Middle Pocket (X=4-5): Searched. No Suicune.
  - Western Pocket (X=0-2): Isolated from south. Must approach from East (Ecruteak).
- Strategy: Fly to Ecruteak City, enter Route 38 Gatehouse, and stay in the Top Lane (Rows 0-6) while walking West. This is the only way to reach the isolated western sections where Suicune is likely waiting.
- Search Log (Route 38):
  - Middle Pocket (X=4-5): Searched. No Suicune.
  - Western Pocket (X=0-2): Isolated from south. Must approach from East (Ecruteak).
- Strategy: Fly to Ecruteak City, enter Route 38 Gatehouse, and stay in the Top Lane (Rows 0-6) while walking West. This is the only way to reach the isolated western sections where Suicune is likely waiting.