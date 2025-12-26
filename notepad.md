# Tile Mechanics (Global)
- FLOOR: Traversable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Traversable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- DOOR/STAIRS/CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]
- FLOOR_UP_WALL: Impassable from below, likely a ledge or wall variant. [Verified]

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

# Suicune Hunt Strategy (Crystal)
- Status: Suicune is a visible overworld sprite.
- Trigger: The "Tower Shook" event in Ecruteak City is required to progress the hunt.
- Sightings Sequence:
  1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. [Pokedex shows Route 42]
  4. Route 36 (Sudowoodo junction): Near the fat guy.
  5. Wise Trio Battle: In Tin Tower Gatehouse (Map 4_1). [Locked by sighting 3]
  6. Tin Tower 1F (Final Battle): Requires Clear Bell.

# Money & Economy
- Current Balance: ¥373. Very low. Need to prioritize trainer battles for cash.

# Metadata
- Current Turn: 23871
- Suicune Hunt Duration: 171 turns (since turn 23700)

# Suicune Hunt Progress Log
- Sighting 3 (Route 42): Systematic sweep of island floor tiles (55+ tiles checked). No trigger.
- Current Status: Pokedex confirms Suicune on Route 42. Wise Trio locked.
- Conclusion: Simple map reset (Mt. Mortar) failed. Sprite is not spawned.
- Plan: 'Hard Reset' - Fly to Mahogany, enter Route 42 from East, Surf West to island, approach from East side.
- Start Turn: 23700.