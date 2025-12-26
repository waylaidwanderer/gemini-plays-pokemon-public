# Global Tile Mechanics
- FLOOR: Traversable. Standard collision. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable only when using HM03 Surf. [Verified]
- TALL_GRASS: Traversable. Triggers wild encounters. [Verified]
- HEADBUTT_TREE: Impassable. Can be interacted with using Headbutt. (e.g., 28,14) [Verified]
- CUT_TREE: Impassable. Can be removed using HM01 Cut. (e.g., 24,13) [Verified]
- WARP_CARPET: Traversable. Triggers map transition. [Verified]
- CAVE: Warp point. [Verified]
- LEDGE: One-way traversal. Blocks movement from the direction it hops into. [Verified]
- PC/COUNTER/SIGN: Impassable. Interact from adjacent tile. [Verified]

# Suicune Hunt Strategy (Crystal)
- Trigger Logic: Proximity-based sighting sequence. Suicune does NOT roam. Pokedex "Area" will be "Unknown" until Tin Tower.
- Sighting 3 (Route 42): Proximity trigger on central island (X:22-30, Y:12-17). landing at (26, 15) from south.
- Sighting 4: Route 36 (Sudowoodo junction).
- Sighting 5: Tin Tower 1F (Final).
- Current Reset Strategy: Mt. Mortar Middle Entrance Reset.
    1. Fly to Mahogany Town.
    2. Surf to Mt. Mortar middle entrance (28, 9).
    3. Enter and exit immediately to re-initialize Route 42 script.
    4. Surf to central island and land at (26, 15).

# Battle Strategy: Suicune
- Status: Leading with XENON (Gastly).
- Overworld: Scripted fleeing events. Mean Look not required.
- Scripted Battle (Tin Tower): Focus on Hypnosis/Sleep Powder and chip damage.

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

# Route 42 Tile Mechanics
- WATER: Traversable with HM03 Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interacting with Headbutt may trigger encounters. [Verified]
- CUT_TREE: Impassable. Removed with HM01 Cut. [Verified]
- CAVE: Warp to Mount Mortar. [Verified]
- WARP_CARPET_LEFT: Warp to Ecruteak Gatehouse. [Verified]
- FLOOR_UP_WALL: Impassable. Visual boundary. [Verified]