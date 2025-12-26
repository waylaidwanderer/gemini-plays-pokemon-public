# Global Tile Mechanics
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

# Suicune Hunt Strategy (Crystal)
- Status: Fixed sightings sequence. Suicune is a visible overworld sprite, not a hidden tile trigger.
- Prerequisites/Sightings:
  1. Burned Tower (Ecruteak City): Legendary beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. Trigger tile is likely (26, 14) or (26, 13) (Adjacency to trees). Note: (26, 13) is a Headbutt tree, not a floor tile. Requires map reload (enter/exit cave).
  4. Route 36 (Sudowoodo junction): Near the fat guy.
  5. Battle the Wise Trio: In Tin Tower Gatehouse (Map 4_1 / 4_3). [REQUIRED after Tower Shook]
  6. Tin Tower 1F (Final Battle): Requires Clear Bell (In Inventory).

# Type Effectiveness (Verified)
- Fire -> Grass: Super Effective
- Water -> Fire: Super Effective
- Electric -> Water: Super Effective
- Ground -> Poison: Super Effective
- Ghost -> Psychic: Super Effective

# Observed Movesets
- GASTLY (Xenon): Hypnosis, Lick, Night Shade, Mean Look.
- KRABBY (Ravioli): Bubble, Leer, Surf.
- PIDGEY (Icarus): Quick Attack, Sand-Attack, Gust, Fly.
- GRAVELER (Gneiss): Earthquake, Defense CURL, Strength, Rollout.
- TYPHLOSION (Calcifer): Flame Wheel, HEADBUTT, SMOKESCREEN, THUNDERPUNCH.
- GLOOM (KimCHI): Absorb, Sweet Scent, Cut, Sleep Powder.

# PC Storage Inventory
- Box 1: RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.

# Money & Economy
- Current Balance: ¥373. Very low. Need to prioritize trainer battles for cash.

# Metadata
- Last sighting check: Turn 23645 (Suicune on Route 42).
- Current Turn: 23680
## Suicune Route 42 Troubleshooting
- Observation: Stood on (26, 14) and (28, 15) after Tin Tower shook event. No trigger.
- Pokedex Status: Suicune confirmed on Route 42.
- Expert Advice: approach from the east side of the Apricorn trees. Possible map script reset needed (enter/exit Mt. Mortar).
- Plan: Exit menu -> Move to (30, 16) -> Approach trees from the east. If fails, enter/exit Mt. Mortar (28, 9) and repeat.
- Failed Attempt 3: Approached (26, 14) from the east (y=15 line). No trigger.
- Next: Resetting map script via Mt. Mortar (28, 9).