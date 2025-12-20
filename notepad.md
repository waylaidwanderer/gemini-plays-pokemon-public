# Tile Mechanics
- FLOOR: Traversable. Standard ground for walking.
- WALL / WINDOW: Impassable. Structural barriers.
- COUNTER: Impassable; interact with NPC behind it from adjacent tile (e.g., Nurse Joy, Mart Clerk).
- MART_SHELF: Impassable. Contains items for sale.
- LADDER: Two-way warp between floors.
- PIT: One-way warp to the floor below.
- WARP_CARPET_DOWN: Exit warp typically leading outside or to a different map section.
- WATER: Traversable only while using Surf. Requires a Pokémon with the move Surf and the Fog Badge (obtained from Morty).
- BUOY: Impassable water barrier. Verified at (13, 32) in Olivine City and (19, 14-17) on Route 40.
- WHIRLPOOL: Impassable water hazard. Requires HM06 (Whirlpool) to cross. Observed on Route 41.

# Lessons Learned
- Ecruteak Gym Path: (3,9)->(3,7)->(6,7)->(6,5)->(7,5)->Martha; (6,5)->(5,5)->(5,1)->Morty.
- Moomoo Farm: Sick Miltank needs 7 standard BERRY items to recover and produce milk.
- Section Connectivity: 4F sections connected by gaps at y=2/3 (East-Middle) and y=14 (Middle-West).
- Warp Verification: (16, 7) and (17, 7) on 4F are NOT map transitions; (18, 7) is a WALL.
- Descent Strategy: Use pits to quickly reach lower floors. 4F (16, 9)/(17, 9) are PITs to 3F.
- Visuals vs. Collision: Visual appearance of tiles (e.g., ground vs wall) can be misleading. Always verify collision types in the Mental Map (e.g., WALL type) before planning paths. (Turn 5863)
- Olivine Harbor: Enclosed by buoys at Y=32. This is a dead end for reaching Route 40. (Turn 5911)
- Battle Tools: find_path_v2 and other map-based tools fail during battle due to missing map data.

# Berry Knowledge
- Mint (R39), Bitter (R31), Mystery (R35), Ice (R36).
- Strategy: Check trees R29-R32 for Berries. Note: Fly requires the Storm Badge from Cianwood Gym.

# Trainer Progress
- Olivine Lighthouse Defeated: Alfred (2F), Huey (2F), Theo (3F), Preston (3F), Kent (4F), Connie (4F), Terrell (3F Middle), Ernest (5F).
- Route 41 Defeated: Swimmer George (46, 8).
- Current Battle: Swimmer Kara (44, 28). Staryu defeated. Calcifer (Lv 30) vs Starmie (Lv 20).

# PC Storage (Box 1)
- Blarney (SUDOWOODO): Lv20
- ROCKY (ONIX): Lv6
- ICARUS (PIDGEY): Lv11
- EGG (CLEFFA): Lv5

# Milestones
- Turn 5860: Caught Krabby (Ravioli) at (6, 25) in Olivine City.
- Turn 5718: Reached Jasmine at top of Olivine Lighthouse.
- Turn 5922: Reached Route 40.
- Turn 5965: Reached Route 41.

# Primary Goal Strategy: Deliver SecretPotion to Jasmine
- Current Objective: Surf south across Route 40 and Route 41 to reach Cianwood City. (Started Turn 5863)
- Next Step: Locate the Pharmacy in Cianwood and obtain the SecretPotion from the shopkeeper.
- Return Strategy: Use Surf to navigate back through Route 41 and 40. If the Storm Badge is obtained, Fly can be used to return to Olivine City instantly.
- Final Step: Climb the Olivine Lighthouse to the 6th floor and interact with Jasmine to deliver the medicine to the sick Pokémon Amphy.
- Recovery Plan: Monitor party HP and PP. Use Potions/Berries from the inventory or return to a Pokémon Center (Olivine or Cianwood) if resources are low.