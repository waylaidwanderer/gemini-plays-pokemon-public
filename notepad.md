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
- Status: Fixed sightings sequence. Suicune is a visible overworld sprite, not a hidden tile trigger.
- Prerequisites/Sightings:
  1. Burned Tower (Ecruteak City): Legendary beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. Trigger tile is likely (26, 14). Requires map reload (enter/exit cave).
  4. Route 36 (Sudowoodo junction): Near the fat guy.
  5. Battle the Wise Trio: In Tin Tower Gatehouse (Map 4_1 / 4_3). [REQUIRED after Tower Shook]
  6. Tin Tower 1F (Final Battle): Requires Clear Bell (In Inventory).

## Route 42 Troubleshooting
- Start Turn: 23700
- Observation: Stood on (26, 14) and (28, 15) after Tin Tower shook event. No trigger.
- Pokedex Status: Suicune confirmed on Route 42.
- Expert Advice: Approach from the east side of the Apricorn trees. Possible map script reset needed (enter/exit Mt. Mortar).
- Attempt Log:
  - Attempt 1: (26, 14). No trigger.
  - Attempt 2: (28, 15). No trigger.
  - Attempt 3: Approached from East (y=15). No trigger.
  - Attempt 4: Reset map script (Mt. Mortar) and returned. No trigger.
- Next: approach from the east side of the entire map (Surf west from Mahogany side).

# Money & Economy
- Current Balance: ¥373. Very low. Need to prioritize trainer battles for cash.

# Metadata
- Current Turn: 23731