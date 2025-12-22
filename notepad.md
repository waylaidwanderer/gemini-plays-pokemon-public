# Suicune Tracking
- Observation: Suicune is missing from its pedestal at (9, 9) in Tin Tower 1F.
- Hypothesis: Suicune is now a roaming Pokémon after the previous encounter/white-out.
- Pokédex Info: Suicune is #239 (Johto/New Dex) and #245 (National/Old Dex).
- Time Tracking: Pokédex search started Turn #12027.

# Strategy for Suicune Rematch (If Roaming)
1. Lead with KIMCHI (Gloom) or a fast Pokémon.
2. Use Sleep Powder immediately.
3. Track location using Pokédex "AREA" map after every map transition.
4. Use `suicune_capture_analyst` agent upon engagement.

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
- HEADBUTT_TREE: Impassable. Requires Headbutt to interact. (Verification needed: are these removable by Cut?)

# PC Storage
- Box 1: ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Roaming Mechanics
- Move between routes when player crosses a boundary.
- Fly causes them to move to a random location.
- Flee immediately in battle. Use Mean Look or status conditions (Sleep).
- Trackable via Pokédex "AREA" map if seen.

# Observation (Turn #12156)
- Pokédex AREA map for Suicune shows multiple red dots at (13, 9), (15, 10), (16, 11), (10, 11), and (8, 13). The map header is "SUICUNE'S NEST".
- Plan: Navigate to Route 37, use the route-hopping trick (moving between Ecruteak City and Route 37) while checking the Pokédex AREA map to find Suicune. Once Suicune is on Route 37, lead with KIMCHI (Gloom), use a Repel to filter out weak wild Pokémon, and encounter Suicune in the grass. Use Sleep Powder immediately upon encounter.

# Suicune Hunt - Hopping Phase
- Hopping started: Turn #12207.
- Border: Ecruteak City (18, 35) <-> Route 37 (18, 0).
- Strategy: Cross border, check Pokedex AREA map. If Suicune is on Route 37, use Repel and encounter in grass. If not, cross back and repeat.
- Lead: KIMCHI (Gloom Lv 21) for Sleep Powder and Repel filtering (Repel filters < Lv 21, Suicune is Lv 40).