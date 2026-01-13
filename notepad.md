# Tile Mechanics
- FLOOR: Traversable. Verified Turn 45281.
- WALL: Impassable. Verified Turn 45281.
- TALL_GRASS: Traversable, triggers wild encounters. Verified Turn 45281.
- HEADBUTT_TREE: Impassable. Verified Turn 45281.
- LEDGE_HOP_DOWN: One-way movement (Down). Verified Turn 45281.
- LEDGE_HOP_RIGHT: One-way movement (Right). Verified Turn 45281.
- WATER: Traversable with HM03 Surf. Verified Turn 45281.
- DOOR: Warp trigger. Verified Turn 45281.

# Strategy: Roamer Hunt (Ecruteak Shuffle)
- Start Turn: 45281 (Timestamp: Tuesday, Jan 13, 2026).
- Completed Cycles: 120.
- Resources: Super Repel x56 remaining.
- Method: Lead Lv 19 (ICARUS) + Super Repel. Shuffle between Ecruteak (17, 35) and Route 37 (7, 2).
- Repel Tracking: Last Applied Turn 45998.
- Strategy Note: Pokedex roamer check verified (Turn 46040): Not in Pokedex. Pausing shuffle to catch Suicune.

# Reflection Turn 46049
- Immediate Execution: No deferred tasks.
- Notepad Hygiene: Updated with liquidation plan.
- Map Hygiene: Markers verified for Violet City.
- Automation Strategy: Using find_path for navigation.
- Goal Clarity: Need money for Ultra Balls. Selling surplus healing items and repels.
- Error Analysis: Fly tool landed in Violet City instead of Indigo Plateau. Pathing to Mart was partially blocked or buttons were skipped. Retrying.

# Liquidation Plan
- Goal: ¥36,000 for 30 Ultra Balls.
- Sell List:
  - Super Repel x36 (Keep 20) -> ~¥9,000
  - Revive x15 -> ~¥11,250
  - Max Potion x6 -> ~¥7,500
  - Full Heal x12 -> ~¥3,600
  - Lemonade x9 -> ~¥1,575
  - Total Potential: ~¥33,000 + current ¥224. Close enough.

# Legendaries
- Suicune: Tin Tower (37, 7). Requires Clear Bell (Owned).
- Entei/Raikou: Roaming. Encounter required to track via Pokedex.
- Strategy: Buy Ultra Balls at Indigo Plateau, then head to Tin Tower.

# Legendaries
- Suicune: Tin Tower (37, 7). Requires Clear Bell (Owned).
- Entei/Raikou: Roaming. Encounter required to track via Pokedex.
- Strategy: Buy Ultra Balls at Indigo Plateau, then head to Tin Tower.

# Trapper Strategy
- Xenon (Haunter, Lv 44): Lacks Mean Look. Confirmed: Cannot relearn (Turn 45962).
- AAAAAAAAAA (Spinarak, Lv 13): Lacks Spider Web. Confirmed: Cannot relearn (Turn 45962).
- Recommendation: Catch new trapper (Gastly < 13 or Zubat/Golbat 42) or use Master Ball.
- Decision: Continue shuffle; prioritize Master Ball for first encounter.

# Quest Log
- Dana's Gift: Route 38 (Waiting).
- Yanma Swarm: Route 35 (Active).

# Lessons Learned
- Roamers relocate on every map boundary cross.
- Bookkeeping: Use turn history for cycle counts. Verified Turn 45874.
- Phone calls can cancel menu actions; verify item usage. Verified Turn 45917.
- Map transitions stop 'autopress_buttons' sequences. Call tools in Ecruteak for best results.
- Menu Navigation: Split navigation into smaller chunks (max 50 buttons). Cursor position in menu is persistent. Refine custom tools to be context-aware.