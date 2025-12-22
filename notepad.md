# Suicune Capture Strategy
- Attempt 1: Failed (Turn #11814). Whited out.
- Rematch Attempt 2 Start: Turn #11972.
- Current Status: KIMCHI (Gloom) leading. 5 Revives in inventory.
- Lesson: Always verify Map ID before assuming floor transitions in multi-floor buildings to avoid time loops.

# Strategy for Suicune Rematch
1. Lead with KIMCHI (Gloom).
2. Use Sleep Powder until Suicune falls asleep.
3. While Suicune is asleep, call `capture_analyst` tool to determine catch probabilities and optimal ball usage based on current HP and status.
4. If Suicune wakes up, re-apply Sleep Powder.
5. Use Smokescreen (Typhlosion) to minimize damage if Suicune is awake.
6. Goal: Catch Suicune without whiting out.

# Investigation: Suicune Access
- Observation: Suicune (9, 9) is inside a walled box (X=6-13, Y=4-10).
- Test 1 (Turn #11981-11990): Talking to Sages (5, 6, 7) - backstories provided, no path opened.
- Test 2 (Turn #11992-11997): (10, 2) is a floor tile labeled "warp tile" in status. Result: No transition on step or A.
- Test 3 (Turn #12005): Face (9, 4) and press A. Result: No effect.
- Test 4 (Turn #12011): Face (9, 10) and press A. Result: No effect.
- Observation (Turn #12014): Suicune is missing from its pedestal at (9, 9).
- Hypothesis 5: Suicune fled because of the previous white-out and must be triggered to return.
- Hypothesis 6: Suicune has moved to a different location in the tower.

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
- Investigation (Turn #12022): Checking Pokédex for Suicune's current location.

# Pokédex Search Plan for Suicune
- Current Menu: Pokédex Search
- Target: Suicune (#245, WATER type)
- Current TYPE1: BUG
- Steps:
  1. Press Right x8 to set TYPE1 to WATER.
  2. Press Down x3 to select "BEGIN SEARCH!!".
  3. Press A to start search.
  4. Find Suicune in the results and check AREA.