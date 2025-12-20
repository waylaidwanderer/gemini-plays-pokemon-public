# Strategy for Primary Goal (Defeat Gym Leader Jasmine)
- Observation: Jasmine uses Steel-type Pokémon (2x Magnemite Lv30, Steelix Lv35).
- Weaknesses: Fire, Fighting, Ground.
- Team Assets: Calcifer (Fire), GNEISS (Ground), Blarney (Fighting move: Low Kick).
- Plan: Lead with Calcifer (Flame Wheel) or GNEISS (Magnitude). Use Blarney's Low Kick as backup.

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
- Battle Mechanics: FIRE moves are Special in Gen 2. HEADBUTT is a Physical Normal-type move.
- NPC Interaction: Always face the counter tile, not the NPC sprite, when talking to Clerks or Nurses.
- XP Sharing: Switching a Pokémon out allows it to gain 50% of the battle experience.
- Rival (Malice) Anomaly: Sprite confirmed standing on water at (14, 15) on Route 40 (Turn 6868). Currently absent.
- Lead Selection: Quilava (Calcifer) is the optimal lead for Jasmine due to Special Fire STAB.

# Battle and Pokemon Information
## Observed Movesets
- Swimmer Charlie: Shellder (Lv21), Tentacool (Lv19), Tentacruel (Lv19).
- Swimmer Kaylee: Goldeen (Lv18/20), Seaking (Lv20). Uses Peck.
- Swimmer Randall: Shellder (Lv18), Wartortle (Lv20).
- Swimmer Simon: Tentacool (Lv20) x2.
- Swimmer Susie: Psyduck (Lv20) uses Disable, Goldeen (Lv22).
- Blackbelt Lung (Cianwood Gym): Mankey (Lv23) x2, Primeape (Lv25).
- Leader Chuck (Cianwood Gym): Primeape (Lv27) uses Leer, Karate Chop. Poliwrath (Lv30) uses Surf, DynamicPunch.

## Type Effectiveness (Gen 2 Observed)
- Fire: Resisted by Water.
- Normal: Neutral against Water.
- Poison: Resists Fighting.
- Grass: Super Effective against Water.
- Fighting: Resisted by Poison.

# PC Storage (Box 1)
- ROCKY (ONIX) Lv6, ICARUS (PIDGEY) Lv11, EGG (CLEFFA) Lv5, XFDW (MEOWTH) Lv16, FRITTATA (TOGEPI) Lv5.

# Progress & Logs
- Status: Amphy cured. Jasmine at Olivine Gym.
- Gym Progress: 4/8 Badges. Cianwood Gym trainers cleared.
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
## Navigation Lessons
- Ladders and Pits: These are triggered by walking onto the tile. Pressing A is unnecessary and often does nothing.
- Lighthouse Descent: Successfully navigated by alternating floors to reach the outer ring. The path from 6F to 1F requires dropping through specific pits: 6F (16, 5) -> 5F (16, 7) -> 4F (16, 9) -> 3F outer ring -> 2F ladder at (5, 3) -> 1F ladder at (3, 11).
- Connectivity: Always verify if a target coordinate is reachable from the current position using a pathfinding script or by checking the Mental Map for walls.

## Current Task: Defeat Jasmine
- Start Turn: 6994
- Current Position: Olivine Gym (5, 5)
- Plan:
    1. Swap Calcifer (QUILAVA) to the lead position. (In progress: swapping Calcifer and KIMCHI)
    2. Move to (5, 4) and face UP to talk to Jasmine at (5, 3).
    3. Defeat Jasmine using Calcifer's FLAME WHEEL.