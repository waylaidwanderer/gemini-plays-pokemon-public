# Tile Mechanics (Global)
- FLOOR: Walkable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Walkable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]
- FLOOR_UP_WALL: Impassable from below. [Verified]
- VOID: Impassable. Map boundary. [Verified]

# Battle and Pokemon Information
## Type Immunities (Target-based)
- Ghost: Immune to Normal, Fighting.
- Ground: Immune to Electric.
- Steel: Immune to Poison.
- Flying: Immune to Ground.
- Dark: Immune to Psychic.

## Party Movesets
- Calcifer (TYPHLOSION): Lv45. Flame Wheel, Headbutt, Smokescreen, Thunderpunch.
- ICARUS (PIDGEY): Lv16. Quick Attack, Sand-Attack, Gust, Fly.
- GNEISS (GRAVELER): Lv44. Earthquake, Defense Curl, Strength, Rollout.
- Ravioli (KRABBY): Lv10. Bubble, Leer, Surf.
- XENON (GASTLY): Lv21. Hypnosis, Lick, Night Shade, Mean Look.
- KIMCHI (GLOOM): Lv21. Absorb, Sweet Scent, Cut, Sleep Powder.

# Event Mechanics: Suicune Hunt (Crystal)
- Status: Suicune is a visible overworld sprite for sightings. Roaming phase begins after Tin Tower?
- Trigger: The "Tower Shook" event in Ecruteak City is required.
- Sightings Sequence:
  1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. [Current Objective - Sprite Missing]
  4. Route 36 (Sudowoodo junction): [Pending]
  5. Wise Trio Battle: In Tin Tower Gatehouse (Map 4_1).
  6. Tin Tower 1F (Final Battle): Requires Clear Bell.

# Strategy for Suicune on Route 42
- Trigger Tile: (26, 13) or (26, 14) on the central island.
- Failure Log:
  - Attempt 1: Re-zoned via Mt. Mortar (middle), stepped on (26, 14). Result: Fail.
  - Attempt 2: Approach from East (Fly to Mahogany), Surf to island. Result: Fail.
  - Attempt 3: Full island sweep. Result: Fail. Sprite is NOT in the map object list.
- Roaming vs Sighting Test Plan:
  1. Check Pokedex location on Route 42. [Done: Pokedex shows blue squares on Route 42]
  2. Change maps (e.g., enter Mt. Mortar at 28, 9).
  3. Check Pokedex again. If location moves, Suicune is in roaming phase.
- Discrepancy: Pokedex shows Suicune on Route 42, but sprite is missing from island. Roaming encounter in tall grass is a high possibility.

# NPC & Interaction Rules
- Apricorn Trees: Face and press A to receive an Apricorn. One per day. (27, 16), (28, 16), (29, 16) on Route 42.

# Money & Economy
- Current Balance: ¥373. Need to prioritize trainer battles.