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
- Sighting 3 (Route 42): Proximity trigger on central island (X:22-30, Y:12-17).
- Sighting 4: Route 36 (Sudowoodo junction).
- Sighting 5: Tin Tower 1F (Final).
- Pivot Plan: If Route 42 sweep fails, verify prerequisites:
    - Ecruteak City: Check Wise Trio (Tin Tower Gatehouse).
    - Cianwood City: Re-verify Eusine dialogue post-Suicune sighting.

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

# Timestamps & Tracking
- Suicune Hunt Phase 3 (Route 42) started Turn 22256.
- Failed Trigger Attempts at: (26, 13), (27, 14), (26, 14), (25, 14), (24, 14), exhaustive sweep, and Hard Map Reset (Fly).
- Resets attempted: Ecruteak Gate, Mt. Mortar Entrance, Mahogany Gate, Ecruteak City (Fly).

# Route 42 Tile Mechanics
- WATER: Traversable with HM03 Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interacting with Headbutt may trigger encounters. [Verified]
- CUT_TREE: Impassable. Removed with HM01 Cut. [Verified]
- CAVE: Warp to Mount Mortar. [Verified]
- WARP_CARPET_LEFT: Warp to Ecruteak Gatehouse. [Verified]
- FLOOR_UP_WALL: Impassable. Visual boundary. [Verified]

# Suicune Hunt Strategy (Post-Reset) - Started Turn 23170
- Objective: Trigger Sighting 3 on Route 42 central island.
- Hypothesis: Hard Map Reset (Fly to Ecruteak and return) will re-initialize the script.
- Test 1 (Turn 23203): Approach (26, 14) from the north after clearing the tree.
- Result: FAILED. Suicune sprite not present; proximity trigger did not fire.
- New Hypothesis: Defeating the Wise Trio in Ecruteak is the prerequisite for the Route 42 sighting, as I have the Clear Bell and Glacier Badge.