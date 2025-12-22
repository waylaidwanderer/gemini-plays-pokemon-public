# Suicune Tracking
- Observation: Suicune is missing from its pedestal at (9, 9) in Tin Tower 1F.
- Hypothesis: Suicune is now a roaming Pokémon after the previous encounter/white-out.
- Pokédex Info: Suicune is #239 (Johto/New Dex) and #245 (National/Old Dex).
- Time Tracking: Pokédex search started Turn #12027.

# Strategy for Suicune Rematch (If Roaming)
1. Lead with KIMCHI (Gloom) or a fast Pokémon.
2. Use Sleep Powder immediately.
3. Track location using Pokédex "AREA" map after every map transition.
4. Use `capture_analyst` agent upon engagement.

# Tile Mechanics (Global)
- FLOOR: Traversable.
- WALL: Impassable.
- COUNTER: Impassable. Interact with NPCs behind by facing the counter and pressing A.
- MART_SHELF: Impassable.
- STAIRCASE/WARP: Triggers map transition.
- WARP_CARPET_LEFT/DOWN: Triggers map transition.
- WATER: HM03 Surf required.
- GRASS: Wild encounters.
- CUT_TREE: HM01 Cut required.
- DOOR: Warp tile.
- DECORATIVE_STAIRS: Non-functional decorative tile (e.g., Tin Tower 1F (10, 2)). Does not trigger warp.

# PC Storage
- Box 1: ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Roaming Mechanics
- Move between routes when player crosses a boundary.
- Fly causes them to move to a random location.
- Flee immediately in battle. Use Mean Look or status conditions (Sleep).
- Trackable via Pokédex "AREA" map if seen.

# General Lessons Learned
- Pokédex "SEARCH" Mechanics: The "SEARCH" function by type/color only displays Pokémon that have been CAUGHT. Pokémon that have only been SEEN must be located manually in the alphabetical or numerical lists.
- Tool Efficiency vs. Manual Input: Do not spend more than a few turns defining or debugging a custom tool for a one-off task (like menu navigation). If a tool fails twice, switch to manual button presses or a simple `run_code` script to maintain momentum.
- Menu Time Blindness: Spending over 100 turns in a single menu system is a critical failure. Monitor turn counts for non-gameplay tasks and pivot if they exceed 20-30 turns.
- Mental Map XML Errors: The Mental Map XML may occasionally misidentify decorative tiles as warps (e.g., Tin Tower 1F (10, 2)). Always verify with Game State Information and manual investigation.
- Observation (Turn #12156): Pokédex AREA map for Suicune shows multiple red dots at (13, 9), (15, 10), (16, 11), (10, 11), and (8, 13). The map header is "SUICUNE'S NEST".
- Plan: Navigate to Route 37, use the route-hopping trick (moving between Ecruteak City and Route 37) while checking the Pokédex AREA map to find Suicune. Once Suicune is on Route 37, lead with KIMCHI (Gloom), use a Repel to filter out weak wild Pokémon, and encounter Suicune in the grass. Use Sleep Powder immediately upon encounter.

# Tile Mechanics (Verified)
- FLOOR: Reachable. Standard movement.
- WALL: Impassable.
- DOOR: Reachable. Triggers map warp.
- HEADBUTT_TREE: Impassable. Requires Headbutt to interact, Cut to remove (if small tree).
- WATER: Impassable. Requires Surf.
- LEDGE_HOP_DOWN/RIGHT: One-way movement. Can jump over from the ledge side.
- WARP_CARPET: Reachable. Triggers map warp at map edges.

# Suicune Hunt Log
- Hunt started: Turn #12156.
- Method: Route-hopping between Ecruteak City and Route 37.
- Status: Tracking via Pokédex.
- Suicune Hunt started Turn #12156.
- Method: Route-hopping between Ecruteak City and Route 37.
- Status (Turn #12189): Suicune is roaming. Checking Pokédex to track its location.
- Suicune Hunt officially tracked starting Turn #12156.
- Lead: KIMCHI (Gloom Lv 21) for Sleep Powder and Repel filtering (Repel filters < Lv 21, Suicune is Lv 40).

# Map Discoveries (Turn #12191)
- Ecruteak City (4_9) Isolated Sections: The Tin Tower Grounds (east of x=31) are physically separated from the main city. The only way out is via Fly or through the Tin Tower 1F -> Wise Trios Room path.
- Strategy: Use Fly to exit the grounds and reach the main city quickly.

# Reflection Turn #12204
- Immediate Execution: Deferred tracking Suicune location due to menu navigation errors. Fixed now by opening Pokédex.
- Notepad Hygiene: Merged "Suicune Hunt Log" sections. Added "Tile Mechanics" global section.
- Map Hygiene: Added markers for Ecruteak gatehouses and Suicune pedestals.
- Automation: Refined `navigate_to_route_37_exit` (in thought, will apply if needed). Created `suicune_capture_analyst`.
- Goal Clarity: Goals are focused on outcomes.
- Error Analysis: Navigation loop at Tin Tower was caused by direction confusion. Lesson: Always move 3+ tiles away from a warp before attempting complex pathfinding.

# General Lessons Learned
- Navigation Buffer: After using a warp, move at least 3 tiles in a consistent direction before starting a new `path_plan` to prevent accidental re-entry loops.
- Roaming Logic: Flying resets roaming Pokémon to random routes. Map transitions move them to adjacent routes.