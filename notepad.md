# Suicune Hunt Strategy (Started Turn #13189)
- Lead: KIMCHI (Lv 21 Gloom).
- Method: Repel Trick. Wild Pokemon on Route 38 are Lv 13-16. Leading with Lv 21 KIMCHI + Super Repel filters out all wild encounters except Suicune (Lv 40).
- Repel Tracking: Repel #4 expired. Attempting to use Super Repel #5 (Turn #13496 attempt failed due to Tully phone call). Encountered Raticate on Turn #13477. Current Super Repel count: 8.
- Tool Reliability: check_suicune_location_v8 and use_super_repel_v4 now assume cursor starts on EXIT (based on last action in Turn #13491).
- Tracking: Use Pokedex AREA map via check_suicune_location_v8.
- Battle Plan:
  - Suicune (Base Speed 85) outspeeds Gloom (Base Speed 40).
  - Expect Suicune to flee on Turn 1 before Sleep Powder.
  - Strategy: Multiple encounters to chip HP, or find a faster Sleep user/Mean Look trapper if progress stalls. Use `suicune_capture_analyst_v2`.
- Capture Notes: Status and HP damage are permanent. Sleep prevents fleeing on Turn 1 *if* the user is faster. Suicune is Lv 40.
- Roamer Logic: Roamers only move when map boundaries are crossed, Fly is used, or after a battle with the roamer. Pacing or regular wild battles do not move them.
- Contingency: If progress stalls after 5 failed encounters, I will pivot to catching a faster Pokémon (e.g., Haunter for Mean Look/Hypnosis).

# Roaming Pokémon Reference
- Movement: Suicune shifts routes ONLY when the player crosses a map boundary (warp, carpet, or edge), uses Fly, or after a battle with the roamer.
- Logic: Pacing in grass, phone calls, or battling OTHER wild Pokemon on the same route do NOT move it.
- Tracking: Suicune's location is verified visually via Pokedex AREA map. It is currently on Route 38 (west of Ecruteak City).

# Tile Mechanics
- TALL_GRASS: Traversable. Triggers wild encounters. Repel Trick filters encounters based on lead level.
- FLOOR: Traversable. Standard collision-free ground.
- WALL / HEADBUTT_TREE: Impassable.
- LEDGE_HOP_DOWN / LEFT / RIGHT: Hypothesized one-way traversable. Verification required.
- WARP_CARPET: Traversable. Triggers map transition (warp).

# Route 38/39 Boundary Reference
- Route 38 (0, 8) <-> Route 39 (19, 8)
- Route 38 (0, 10) <-> Route 39 (19, 10)
- Crossing this line shifts roamer locations.

# PC Storage (Box 1)
- ROCKY (Onix Lv 6), EGG (Cleffa Lv 5), XFDW (Meowth Lv 16), FRITTATA (Togepi Lv 5), SHUCKIE (Shuckle Lv 15).

# Lessons Learned & Error Analysis
- Tool Reliability: Use v7 for Suicune location checks. Ensure Up/Down counts are accurate.
- Navigation: Paths are often wider than one tile.
- State Sync: Always verify inventory and money against Game State Information.
- Repel Hygiene: Use sleep commands between menu actions to ensure they register.
- Battle Mechanics: Roamers flee on Turn 1. Speed is critical for status moves. Damage/Status is persistent.

# Inventory Order (Verified Turn #13495)
1. PSNCUREBERRY
2. X ATTACK
3. BITTER BERRY
4. ICE BERRY
5. MAX ETHER
6. FULL HEAL
7. ICE HEAL
8. X SPECIAL
9. GUARD SPEC.
10. LEMONADE
11. FRESH WATER
12. SUPER POTION
13. AMULET COIN
14. REVIVE
15. SUPER REPEL (Target for Repel Trick)

# Menu Cursor Tracking
- Start Menu: Cursor on SAVE (index 5) as of Turn #13495.
- PACK: Cursor was on AMULET COIN (index 1) in previous attempts, but tools now reset to Item 1.
- Note: Menu does NOT wrap in the ITEMS pocket. Item 1 is PSNCUREBERRY.