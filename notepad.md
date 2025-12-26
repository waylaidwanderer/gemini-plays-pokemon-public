# Tile Mechanics
- FLOOR: Traversable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Traversable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. Regrows upon map reload. [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- DOOR: Warp point. [Verified]
- STAIRS: Warp point. [Verified]
- CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]

# Suicune Hunt Strategy (Crystal)
- Status: Fixed sightings sequence. Suicune is a visible overworld sprite, not a hidden tile trigger.
- Prerequisites/Sightings:
  1. Burned Tower (Ecruteak City): Legendary beasts flee. [Cleared]
  2. Cianwood City (North): Suicune observed at (10, 14). [Cleared]
  3. Route 42 (Central Island): Middle Apricorn grove. Trigger tile (26, 14). Requires map reload (enter/exit cave) if it doesn't appear.
  4. Route 36 (Sudowoodo junction): Near the fat guy.
  5. Tin Tower 1F (Final Battle): Requires Clear Bell (In Inventory).
- Current Objective: Trigger Sighting 3 on Route 42 island.

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

# Ecruteak Contingency Plan
- If island sighting fails:
  1. Go to Ecruteak City.
  2. Talk to the Sage in the Dance Hall.
  3. Talk to the Wise Trio in the Tin Tower Gatehouse/Wise Trio Room.
  4. Verify if Sighting 3 flag is set by checking if Suicune moves in Pokedex.
- Turn 23568: Reset Route 42 by entering/exiting Mt. Mortar.
- Turn 23565: Confirmed Suicune location is "Route 42" in Pokedex.
- Observation: Suicune sprite is not yet visible on screen. Cutting tree at (24, 13) to access island.