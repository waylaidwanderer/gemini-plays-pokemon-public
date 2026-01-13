# Verified Game Systems
- Start Menu: 1.POKEDEX, 2.POKEMON, 3.PACK, 4.POKEGEAR, 5.GEM, 6.SAVE, 7.OPTION, 8.EXIT.
- Fly Map: Cursor starts at New Bark Town (5, 4).
- Johto Fly Grid:
  - (3,3) Ecruteak, (4,3) Violet, (5,3) Mahogany
  - (3,4) Goldenrod, (4,4) Cherrygrove, (5,4) New Bark
  - (3,5) Azalea
  - (5,2) Indigo Plateau
  - (2,4) Olivine, (1,4) Cianwood
- Map Transitions: Map-edge transitions (Warp Carpets) require walking 'off' the grid (e.g., moving Down from the bottom row). Tools like `find_path` won't trigger these if the destination is on the edge.

# Strategy: Ecruteak Shuffle
- Goal: Force first encounter with Entei/Raikou (Lv 40).
- Location: Ecruteak City <-> Route 37 (Left side).
- Repel Trick: Lead Lv 19 (ICARUS) + Super Repel.
- Method:
  1. Transition from Ecruteak to Route 37.
  2. Pace 4 steps in grass at (7, 2).
  3. Transition back to Ecruteak.
  4. Repeat.
- Timestamp: Started Ecruteak-specific shuffle at Turn 45539.

# Tracking: Session 4
- Start: Turn 45281.
- Total Shuffle Cycles (Ecruteak): 4 completed.
- Current Cycle: 5 (Turn 45560).
- Repel Status: Applied Turn 45439. Steps: 47/200.

# Quest Log
- Dana's Gift: Route 38 (Waiting).
- Yanma Swarm: Route 35 (Active).

# Lessons Learned
- Fly Map: Always count from New Bark Town.
- Menu Fumbles: Verify Start menu is open before using navigation tools.
- Overwatch Tips: Use current coordinates, not stale ones, for tool inputs.