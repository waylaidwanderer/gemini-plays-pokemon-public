# Strategy: Suicune Hunt (Johto)
- Status: Suicune confirmed on Route 42 via Pokedex (Turn 21433).
- Strategy: Reset map (enter Mount Mortar) then methodical floor sweep of the central island (X=24-30, Y=14-17) to trigger Sighting 3 flee event.
- Lessons Learned:
    - Pokedex: Currently in Alphabetical order. SUICUNE is located above SUNKERN.
    - Scripted: Sighting sequence is fixed. Pokedex AREA map tracks current scripted location.
    - Animation: Sprite flees with a visible jump. If no jump seen, event is not complete.
    - Map Reset: If a scripted event fails to trigger after a sweep, reset the map by entering a cave or using Fly.
    - Trigger: Suicune on Route 42 is a tile trigger on the southern Apricorn island floor.

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

# Milestone Audit
- Current Milestone: Sighting 3 (Route 42).
- Previous Milestones: Sighting 1 (Burned Tower), Sighting 2 (Cianwood).
- Eusine: Defeated in Cianwood.
- Problem: Complete floor sweep of Route 42 island (X=24-30, Y=14-17) failed to trigger flee.
- Hypothesis: Sprite didn't load or trigger failed. Reset required.

# Island Sweep Contingency
- If methodical sweep after map reset fails, I will:
    1. Re-verify Pokedex AREA map for exact blinking box.
    2. Check if Suicune moved to Route 36 (Sighting 4).
    3. Visit Tin Tower to see if sequence skipped.