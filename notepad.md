# Strategy: Suicune Hunt (Johto)
- Status: Suicune confirmed on Route 42 via Pokedex (Turn 21433).
- Strategy: Systematic floor sweep of the central island (X=24-30, Y=14-17) and northern strip to trigger Sighting 3 flee event.
- Progress:
    - Island sweep started: Turn 21455 (Thursday, Dec 25, 2025).
    - Failed attempts to trigger: 2 (Central sweep, Northern strip sweep).
- Lessons Learned:
    - Pokedex: Default order is Johto Order (#245). Check sorting if entries seem missing.
    - Scripted: Sighting sequence is fixed. Pokedex AREA map tracks current scripted location.
    - Animation: Sprite flees with a visible jump. If no jump seen, event is not complete.
    - Hallucination Warning: Pokedex AREA map is a simple grid; it does not show "nests," "blue squares," or "red dots."
    - Map Reset: If a scripted event fails to trigger after a sweep, try resetting the map by Flying or entering a cave.

# Tile Mechanics
- FLOOR: Traversable. Standard ground. [Verified]
- WALL: Impassable. [Verified]
- WATER: Traversable via Surf. [Verified]
- HEADBUTT_TREE: Impassable. Interaction triggers Headbutt. [Verified]
- CUT_TREE: Impassable. Interaction triggers Cut. [Verified]
- FRUIT_TREE: Impassable. Interaction gives Apricorn/Berry. [Verified]
- TALL_GRASS: Traversable. Wild encounters. [Verified]
- CAVE: Warp. [Verified]
- WARP_CARPET_LEFT/DOWN: Warp. [Verified]
- LADDER: Warp. [Verified]
- FLOOR_UP_WALL: Impassable. Ledge that can be jumped over from above. [Verified]

# Milestone Audit (Turn 21517)
- Current Milestone: Sighting 3 (Route 42).
- Previous Milestones: Sighting 1 (Burned Tower), Sighting 2 (Cianwood).
- Eusine: Defeated in Cianwood.
- Problem: Complete floor sweep of Route 42 island (X=24-30, Y=14-17) failed to trigger flee.
- Hypothesis 1: Trigger is on a specific tile missed. (Step on (27, 15) again).
- Hypothesis 2: Trigger is on the water surrounding the island.
- Hypothesis 3: Milestone confusion - Suicune has already moved to Sighting 4.

# Failed Hypothesis: Island Floor Sweep
- Sweep of (24-30, 13-17) floor tiles failed to trigger Suicune flee.
- New Strategy: Verify exact blinking location in Pokedex AREA. If on island, check water tiles (Y=14-17) and northern strip (Y=11-12).
- Contingency: If sweep fails, reset map by flying or entering cave.