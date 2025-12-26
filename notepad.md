# Tile Mechanics (Global)
- FLOOR: Walkable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Walkable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- DOOR/STAIRS/CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]
- FLOOR_UP_WALL: Impassable from below. [Verified]

# Battle and Pokemon Information
## Type Effectiveness (Verified)
- Fire -> Grass: Super Effective
- Water -> Fire: Super Effective
- Electric -> Water: Super Effective
- Ground -> Poison: Super Effective
- Ghost -> Psychic: Super Effective

## Party Movesets
- Calcifer (TYPHLOSION): Lv45. Flame Wheel, Headbutt, Smokescreen, Thunderpunch.
- ICARUS (PIDGEY): Lv16. Quick Attack, Sand-Attack, Gust, Fly.
- GNEISS (GRAVELER): Lv44. Earthquake, Defense Curl, Strength, Rollout.
- Ravioli (KRABBY): Lv10. Bubble, Leer, Surf.
- XENON (GASTLY): Lv21. Hypnosis, Lick, Night Shade, Mean Look.
- KIMCHI (GLOOM): Lv21. Absorb, Sweet Scent, Cut, Sleep Powder.

# Event Mechanics: Suicune Hunt (Crystal)
- Status: Suicune is a visible overworld sprite.
- Trigger: The "Tower Shook" event in Ecruteak City is required.
- Sightings Sequence:
  1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. [Pokedex shows Route 42]
     - Hard Reset Start Turn: 23902
     - Strategy: Approach from East (Mahogany Town) and interact with trees or stand on (26, 14).
     - Contingency: If no trigger after Pokedex verification, check Route 36 or Ecruteak flags.
  4. Route 36 (Sudowoodo junction): Near fat guy NPC.
  5. Wise Trio Battle: In Tin Tower Gatehouse (Map 4_1). [Locked by sighting 3]
  6. Tin Tower 1F (Final Battle): Requires Clear Bell.

# Money & Economy
- Current Balance: ¥373. Need to prioritize trainer battles.

# Lessons Learned
- FLY Map Navigation: Grid-based. Relative positions match region map.
- Suicune Sighting 3: Simple map resets (Mt. Mortar) failed. Approaching from East (Mahogany) is required to trigger the island event.
- Trigger Logic: Event likely requires walking on (26, 14) or interacting with trees. Approach from Right/East side is recommended.
- Stagnation: Spending 200+ turns on one trigger is excessive. Verify location and pivot if needed.