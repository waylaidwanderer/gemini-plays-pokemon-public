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
- Calcifer (TYPHLOSION): Flame Wheel, Headbutt, Smokescreen, Thunderpunch.
- ICARUS (PIDGEY): Quick Attack, Sand-Attack, Gust, Fly.
- GNEISS (GRAVELER): Earthquake, Defense Curl, Strength, Rollout.
- Ravioli (KRABBY): Bubble, Leer, Surf.
- XENON (GASTLY): Hypnosis, Lick, Night Shade, Mean Look.
- KIMCHI (GLOOM): Absorb, Sweet Scent, Cut, Sleep Powder.

## PC Storage Inventory
- Box 1: RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.

# Event Mechanics: Suicune Hunt (Crystal)
- Status: Suicune is a visible overworld sprite.
- Trigger: The "Tower Shook" event in Ecruteak City is required.
- Sightings Sequence:
  1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. [Pokedex shows Route 42]
     - Trigger Hypothesis: Approach from East (Mahogany Town) to force script load.
     - Targeted Trigger Tile: (26, 13) [Per Agent Advice]
  4. Route 36 (Sudowoodo junction): Near the fat guy.
  5. Wise Trio Battle: In Tin Tower Gatehouse (Map 4_1). [Locked by sighting 3]
  6. Tin Tower 1F (Final Battle): Requires Clear Bell.

# Money & Economy
- Current Balance: ¥373. Need to prioritize trainer battles.

# Lessons Learned
- FLY Map Navigation: Grid-based. Relative positions match region map.
- Suicune Sighting 3: Approaching from West/Mt. Mortar failed. Trying East approach (Hard Reset).