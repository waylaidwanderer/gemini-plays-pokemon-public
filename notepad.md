# Suicune Capture Strategy (Historical)
- Attempt 1: Failed (Turn #11814). Whited out.
- Rematch Attempt 2 Start: Turn #11972.
- Lesson: Always verify Map ID before assuming floor transitions in multi-floor buildings to avoid time loops.
- Lesson: Pokédex "SEARCH" by type only returns CAUGHT Pokémon. Seen-only Pokémon must be found in the main list.

# Suicune Tracking
- Observation (Turn #12014): Suicune is missing from its pedestal at (9, 9) in Tin Tower 1F.
- Hypothesis: Suicune fled because of the previous white-out and is now roaming or triggered to return elsewhere.
- Goal: Check Suicune's Pokédex entry for "AREA" to confirm roaming status.

# Strategy for Suicune Rematch (If Roaming)
1. Lead with KIMCHI (Gloom) or a fast Pokémon.
2. Use Sleep Powder immediately.
3. If it flees, track it using the Pokédex map.
4. Goal: Catch Suicune without whiting out.

# Investigation: Tin Tower Access
- Observation: Suicune (9, 9) was inside a walled box (X=6-13, Y=4-10).
- Test 1 (Turn #11981-11990): Talking to Sages (5, 6, 7) - backstories provided, no path opened.
- Test 2 (Turn #11992-11997): (10, 2) is a floor tile labeled "warp tile" in status (`is-warp="true"`). Result: No transition on step or A.
- Test 3 (Turn #12005): Face (9, 4) and press A. Result: No effect.
- Test 4 (Turn #12011): Face (9, 10) and press A. Result: No effect.

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

# PC Storage
- Box 1: ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).
- (10, 2) identified as an 'Unmarked Warp' by system (Turn #11997). Currently non-functional or one-way.