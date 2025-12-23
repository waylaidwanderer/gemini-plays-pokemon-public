# Suicune Capture Strategy
## The Repel Trick (Active)
- **Lead:** KIMCHI (Lv 21 Gloom).
- **Method:** Use Super Repel to filter out wild Pokémon (Lv 13-16). Suicune (Lv 40) is the only possible encounter.
- **Status:** Super Repel #6 active (Used Turn #13551).
- **Inventory:** Super Repel x6 (Slot 13 in ITEMS pocket).
- **Pacing Progress:** 0/200 steps (Repel #6).

## Battle Plan (vs Suicune Lv 40)
- **Stats:** Suicune (Base Speed 85) vs Gloom (Base Speed 40).
- **Strategy:**
  1. Use Sleep Powder immediately.
  2. Chip damage and status are persistent.
  3. Catching probability: ~0.39% (Base HP, No Status, Great Ball).

## Route 38 Environment
- **Pacing Area:** Tall grass at (26, 7).
- **Roamer Logic:** Suicune moves routes ONLY when crossing map boundaries (Route 38/39 edge), using Fly, or after battle. Pacing does NOT move it.
- **Tile Mechanics:**
  - FLOOR: Traversable.
  - WALL/HEADBUTT_TREE: Impassable.
  - TALL_GRASS: Encounter zone.
  - LEDGE_HOP: One-way.

## Party & Resources
- **Balls:** Great Ball x40.
- **Healing:** Super Potion x10, Revive x5, Fresh Water x5.
- **PC Box 1:** ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Lessons Learned & Error Analysis
- **Inventory Listing:** The Game State Information 'Items' list is ALPHABETICAL. The actual PACK order is different. Always verify indices via screen text.
- **Super Repel Slot:** Super Repel is confirmed to be Item 15 (14 Down presses from Item 1) in the current PACK configuration.
- **Repel Logic:** Using an item like AMULET COIN does not use up a Repel. Current count is 7.

# Pacing Log
- Repel #5: Completed ~200 steps (Turn #13515 - #13543).
- Repel #6: Attempting to use now (Item 15).
- Suicune confirmed on Route 38 at Turn #13537.