# Key Items & Progress
- Badges: Zephyr, Hive, Plain, Fog.
- HM01 Cut, HM03 Surf, HM05 Flash.
- TM30 Shadow Ball.

# Tile Mechanics
- FLOOR: Traversable.
- WALL: Impassable.
- DOOR / LADDER / PIT: Warp tiles.
- LADDER: Two-way warp between floors.
- PIT: One-way warp to the floor below.
- WATER: Requires Surf.
- TALL_GRASS: Wild encounters.
- LEDGE_HOP: One-way traversal.
- COUNTER: Interaction across tile.
- HEADBUTT_TREE: Requires Headbutt.
- STATUE / BOOKSHELF / PC / WINDOW: Impassable background objects.

# Trainer Progress (Route 38/39)
- Beat: Olivia, Valerie, Toby, Harry, Dana, Chad, Norman, Ruth, Derek, Eugene.

# Lessons Learned
- Nicknamed Meowth 'XFDW'.
- Ecruteak Gym Path: (3,9)->(3,7)->(6,7)->(6,5)->(7,5)->Martha; (6,5)->(5,5)->(5,1)->Morty.
- Moomoo Farm: Sick Miltank needs 7 standard BERRY items. (Started Turn 5458)
- NPC Verification: Do not assume an NPC is static or present based on a single turn's observation; use stun_npc or re-verify if they seem to disappear.
- Lighthouse Layout: The lighthouse has many split levels and floor warps; exploration is key to finding the correct path up.
- Battle Strategy: Use battle_strategist_v2 for all trainer battles to ensure consistent performance.
- Warp Verification: (16, 7) and (17, 7) on 4F are confirmed FLOOR tiles (not pits). They are labeled as warps in the game data and may be exits to a balcony. Step on them and walk "off" the map to trigger.
- Section Connectivity: 4F East and Middle sections are connected by a gap at (10, 2) and (10, 3).

# Berry Knowledge
- Standard BERRY: 0/7.
- Mint (R39), Bitter (R31), Mystery (R35), Ice (R36).
- Inventory: Mint x1, Bitter x1, Ice x1, PsnCure x1.
- Berry Collection Strategy: Fly to New Bark Town after finding Jasmine. Check trees on R29, R30, R31, R32, R35, R36, R37, R38, R39.

# Strategy
- Olivine Lighthouse: Currently on 3F Middle (landed from 4F pit).
- Goal: Reach Jasmine.
- Path: Defeat Sailor Terrell -> Grab item (8, 2) -> Take ladder (9, 5) back to 4F Middle -> Take ladder (9, 5) to 5F.

# Trainer Progress (Olivine Lighthouse)
- Gentleman Alfred (2F): Defeated.
- Sailor Huey (2F): Defeated.
- Bird Keeper Theo (3F): Defeated.
- Gentleman Preston (3F): Defeated.
- Sailor Kent (4F): Defeated.
- Lass Connie (4F): Defeated.
- Sailor Terrell (3F Middle): Poliwhirl Lv20. In progress.

# Map Notes (Olivine Lighthouse)
- 3F Sections: West (x=0-6), Middle (x=8-10), East (x=12-19). Separated by walls at x=7 and x=11.
- 3F Middle Section: Contains Sailor (9, 2), Item (8, 2), and Ladder to 4F (9, 5). Reachable by falling through pit (8, 3) or (9, 3) on 4F.
- 3F Warps: (13, 3) Ladder, (5, 3) Ladder, (9, 5) Ladder, (16, 11) PIT, (17, 11) PIT.
- 4F Warps: (13, 3) Ladder, (3, 5) Ladder, (9, 7) Ladder, (9, 5) Ladder, (8, 3) PIT, (9, 3) PIT, (16, 9) PIT, (17, 9) PIT.