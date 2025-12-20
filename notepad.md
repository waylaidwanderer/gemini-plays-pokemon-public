# Strategy for Primary Goal (Defeat Gym Leader Chuck)
- Observation: Chuck uses Fighting-type Pokémon (Primeape Lv27, Poliwrath Lv30).
- Weaknesses: Flying, Psychic.
- Team Assets: KIMCHI (Poison resists Fighting), Blarney (Sudowoodo). 
- Note: Poliwrath is Water/Fighting. GNEISS is 4x weak to Water. Calcifer is weak to Water.
- Plan: Train KIMCHI to a higher level. Use KIMCHI's Grass moves against Poliwrath.

# Strategy for KIMCHI Training
- Training Route: Surf Route 40/41.
- Method: Use shared XP by leading with KIMCHI and switching to Calcifer or GNEISS.
- Goal: Reach Lv21+ for evolution into Gloom.

# Game Mechanics & Systems
## Tile Mechanics
- Verified Traversal:
  - FLOOR: Traversable in all directions.
  - WALL / BUOY / ROCK / BOOKSHELF / TV / RADIO / TOWN_MAP / STATUE / COUNTER: Impassable barriers.
  - WATER: Traversable while surfing (HM03 Surf + Fog Badge). Verified.
  - LADDER / DOOR / PIT / WARP_CARPET: Triggers map transition upon entry.
  - PIT: Drops player to the floor below (usually landing on a specific tile).
- Verified RELATIONAL Behavior:
  - Counter NPCs: Must interact with the COUNTER tile in front of them.
  - PCs/Switches: Must face UP from directly BELOW the tile.

## Lessons Learned
- Strength (HM04): Obtained from the Sailor in Olivine Cafe (1, 7).
- Boulder Dialogue: "A POKéMON may be able to move this" indicates Strength is needed.
- Gym Access: Cianwood Gym requires Strength to reach the Leader.
- Battle Mechanics: FIRE moves are Special in Gen 2. HEADBUTT is a Physical Normal-type move. Steelix has high Physical Defense but lower Special Defense.
- NPC Interaction: Always face the counter tile, not the NPC sprite, when talking to Clerks or Nurses.
- XP Sharing: Switching a Pokémon out allows it to gain 50% of the battle experience.
- Rival (Malice) Anomaly: Sprite confirmed standing on water at (14, 15) on Route 40 (Turn 6868). Currently absent.
- Lighthouse Descent: The structure is a series of concentric rings. Navigating between the inner pillar and outer ring requires dropping through specific pits on higher floors. Path: 6F (16, 5) -> 5F (16, 7) -> 4F (16, 9) -> 3F outer ring -> 2F ladder -> 1F exit.

# Battle and Pokemon Information
## Observed Movesets
- Swimmer Charlie: Shellder (Lv21), Tentacool (Lv19), Tentacruel (Lv19).
- Swimmer Kaylee: Goldeen (Lv18/20), Seaking (Lv20). Uses Peck.
- Swimmer Randall: Shellder (Lv18), Wartortle (Lv20).
- Swimmer Simon: Tentacool (Lv20) x2.
- Swimmer Susie: Psyduck (Lv20) uses Disable, Goldeen (Lv22).
- Blackbelt Lung (Cianwood Gym): Mankny (Lv23) x2, Primeape (Lv25).
- Leader Chuck (Cianwood Gym): Primeape (Lv27) uses Leer, Karate Chop. Poliwrath (Lv30) uses Surf, DynamicPunch.

## Type Effectiveness (Gen 2 Observed)
- Fire: Super Effective against Steel.
- Ground: Super Effective against Steel, Electric.
- Water: Resists Fire.

# PC Storage (Box 1)
- ROCKY (ONIX) Lv6, ICARUS (PIDGEY) Lv11, EGG (CLEFFA) Lv5, XFDW (MEOWTH) Lv16, FRITTATA (TOGEPI) Lv5.

# Progress & Logs
- Badges: 5/16 (Zephyr, Hive, Plain, Fog, Mineral).
- KIMCHI Training: Lv15. Target: Lv21+ for evolution.

# General Knowledge
- Abra Weakness: Bug, Ghost, Dark.
- Growlithe Weakness: Water, Ground, Rock.
- Snubbull Weakness: Fighting (Arnie asked Turn 6949).

# Area Notes
## Olivine City
- Olivine Port (19, 27) and (20, 27): Entry to S.S. Aqua.
- Olivine Lighthouse (29, 27): Entry.
- Sailor at (26, 27): Paces between (26, 26) and (26, 28).
- Lass at (13, 4) in 4F: Non-battling NPC. Mentions JASMINE and the GYM.

## Current Task: Return to Cianwood
- Start Turn: 7025
- Plan:
    1. Exit Olivine Gym.
    2. Heal at Olivine Pokemon Center (13, 21).
    3. Surf from Route 40 to Cianwood City.
    4. Defeat Gym Leader Chuck.