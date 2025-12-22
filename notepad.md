# Suicune Capture Strategy
- Attempt 1: Failed (Turn #11814). Whited out.
- Status: KIMCHI (Gloom) leading. 5 Revives in inventory.
- Lesson: Always verify Map ID before assuming floor transitions in multi-floor buildings to avoid time loops.
- Rematch Start: Turn #11972.
- Current Position: (10, 3) in Tin Tower 1F.
- WARP_CARPET_DOWN: Warp tile. Moving Down on this tile triggers a map transition. (Verified: Tin Tower 1F 9,15)

# Strategy for Suicune Rematch
1. Lead with KIMCHI (Gloom).
2. Use Sleep Powder until Suicune falls asleep.
3. While Suicune is asleep, call `capture_analyst` tool to determine catch probabilities and optimal ball usage based on current HP and status.
4. If Suicune wakes up, re-apply Sleep Powder.
5. Use Smokescreen (Typhlosion) to minimize damage if Suicune is awake.
6. Goal: Catch Suicune without whiting out.

# Tile Mechanics (Global)
- FLOOR: Traversable. (Verified: Tin Tower 1F, Goldenrod City, Dept Store 2F)
- WALL: Impassable. (Verified: Tin Tower 1F, Goldenrod City)
- COUNTER: Impassable. Interact with NPCs behind by facing the counter and pressing A. (Verified: Dept Store 2F)
- MART_SHELF: Impassable. (Verified: Dept Store 2F)
- STAIRCASE/WARP: Triggers map transition. (Verified: Dept Store floors)
- WARP_CARPET_LEFT: Warp tile. Moving Left on this tile triggers a map transition. (Verified: Ecruteak City 20,2)
- WATER: HM03 Surf required.
- GRASS: Encounters possible.
- CUT_TREE: HM01 Cut required.
- DOOR: Warp tile. (Verified: Goldenrod City)

# PC Storage
- Box 1: ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).
- Observation: Suicune is in a walled box (X=6-13, Y=4-10). Checking Sages for access.