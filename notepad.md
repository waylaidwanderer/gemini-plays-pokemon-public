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
- Status: Suicune appears at fixed sighting locations. Final encounter at Tin Tower.
- Prerequisite: "Tower Shook" event in Ecruteak City + Possession of CLEAR BELL.
- Sightings Sequence:
  1. Burned Tower (Ecruteak City): Beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. [Sighting FAILED/SKIPPED]
  4. Route 36 (Sudowoodo junction): [Pending]
  5. Wise Trio Battle: In Tin Tower Gatehouse (Map 4_1). [Pending]
  6. Tin Tower 1F (Final Battle): Requires Clear Bell. [Current Target]

# Strategy for Tin Tower
- Current Items: Clear Bell in inventory.
- Event Status: Tin Tower has already shaken (Sage mentioned a Pokemon returned to the top).
- Hypothesis: Suicune has moved to Tin Tower because the Clear Bell is in inventory and the Tower has shaken.
- Action: Visit Tin Tower Gatehouse at (18, 11) and proceed to the Tower for the final encounter.

# NPC & Interaction Rules
- Apricorn Trees: Face and press A to receive an Apricorn. One per day. (27, 16), (28, 16), (29, 16) on Route 42.

# Money & Economy
- Current Balance: ¥373. Need to prioritize trainer battles.

# Tool & Mechanic Notes
- find_path_v3: Provides directional inputs but does NOT trigger context-sensitive actions like Surf or Cut. Manual interaction is required to transition between movement modes.
- Suicune Roaming: In Pokémon Crystal, Suicune does not roam until after the fixed encounter at Tin Tower. Pokedex "blue squares" represent fixed sighting locations.

# Strategy for Beating Suicune
- Status: Lv40 legendary.
- Lead: Gneiss (Lv44) for durability or XENON (Lv21) for Hypnosis/Mean Look if capture is attempted.
- Capture Strategy: Use XENON to sleep it, then switch to a high-level attacker to weaken. Great Balls ready.