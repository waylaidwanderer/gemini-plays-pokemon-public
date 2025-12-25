# Strategy: Suicune Hunt (Crystal)
- Start Turn: 20637 (Thursday)
- Sequence: 1. Burned Tower (Done) -> 2. Cianwood (Done) -> 3. Route 42 (Done) -> 4. Route 38 (Ledge trigger) -> 5. Route 14 -> 6. Tin Tower (Stationary battle).
- Route 38 Trigger: Proximity to the northern ledge (Rows 8-12, X=0-15).
- Goal: Confirm sighting via Pokédex AREA map.

# Strategy: Roaming Beasts (Raikou/Entei)
- Raikou encountered on Route 38 (Turn 20702). Raikou used Roar (Turn 20705). Raikou is roaming.

# Side Quests & Resources
- Arthur (Hard Stone): Route 36. Thursday only. Arthur is in the NE corner of Route 36, near the National Park entrance. (Arthur dialogue looped Turn 20594, Hard Stone not in inventory).
- Clear Bell: In Key Items (Verified Turn 20623).

# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- TALL_GRASS: Traversable; triggers wild encounters.
- LEDGE_HOP_DOWN: One-way jump South.
- LEDGE_HOP_LEFT: One-way jump West.
- LEDGE_HOP_RIGHT: One-way jump East.
- HEADBUTT_TREE: Impassable.
- WATER: Traversable with Surf.
- BERRY_TREE: Impassable.

# Lessons Learned
- Menu Automation: Avoid complex custom tools for one-off menu tasks (e.g., using a single item). Manual `press_buttons` is more reliable.
- Root Hypothesis: Always verify if a 'blocked' path is actually a scripted event or a misunderstanding of tile collision (e.g., Ledge Hop tiles).
- Ledge Navigation: You cannot move 'Left' into a 'LEDGE_HOP_RIGHT' tile. Check tile types before pathing.