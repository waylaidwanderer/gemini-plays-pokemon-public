# Suicune Tracking
- Observation (Turn #12014): Suicune is missing from its pedestal at (9, 9) in Tin Tower 1F.
- Hypothesis: Suicune fled because of the previous white-out and is now roaming or triggered to return elsewhere.
- Johto Pokédex: Suicune is #238. (National Dex: #245).
- Start of Pokédex Search: Turn #12027.

# Strategy for Suicune Rematch (If Roaming)
1. Lead with KIMCHI (Gloom) or a fast Pokémon.
2. Use Sleep Powder immediately.
3. If it flees, track it using the Pokédex map.
4. Use `capture_analyst` agent to optimize capture once engaged.

# Tile Mechanics (Global)
- FLOOR: Traversable. (Verified: Tin Tower 1F, Goldenrod City, Dept Store 2F)
- WALL: Impassable. (Verified: Tin Tower 1F, Goldenrod City)
- COUNTER: Impassable. Interact with NPCs behind by facing the counter and pressing A. (Verified: Dept Store 2F)
- MART_SHELF: Impassable. (Verified: Dept Store 2F)
- STAIRCASE/WARP: Triggers map transition. (Verified: Dept Store floors)
- WARP_CARPET_LEFT: Warp tile. Moving Left on this tile triggers a map transition. (Verified: Ecruteak City 20,2)
- WARP_CARPET_DOWN: Warp tile. Moving Down on this tile triggers a map transition. (Verified: Tin Tower 1F 9,15)
- WATER: HM03 Surf required.
- GRASS: Encounters possible.
- CUT_TREE: HM01 Cut required.
- DOOR: Warp tile. (Verified: Goldenrod City)
- DECORATIVE_STAIRS: Non-functional decorative tile at (10, 2) in Tin Tower 1F. Does not trigger warp.

# PC Storage
- Box 1: ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Roaming Mechanics (General)
- Roaming Pokémon move between routes when the player crosses a boundary (map transition).
- They can be tracked via the Pokédex "AREA" map if they have been seen.
- They flee immediately in battle. Mean Look or Sleep can help, but they are very fast.
- If Suicune is roaming, I need to check its location every time I change routes.
- Movement Pattern: When you move to a new route/city, the roaming Pokémon moves to an adjacent route. If you use Fly, they move to a random location.