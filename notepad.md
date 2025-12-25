# Suicune Hunt Strategy (Crystal)
- Status: ROAMING. Suicune roams Johto after the Tin Tower event if not caught.
- Lead: XENON (Gastly Lv21). Moves: Mean Look, Hypnosis.
- Strategy: Boundary cycling between Route 38 and Ecruteak City. Check Pokedex 'Area' snapshot.
- Goal: Obtain Quick Claw to ensure XENON can move first.

# Suicune Battle Plan
- Turn 1: MEAN LOOK.
- Turn 2+: HYPNOSIS. (Keep asleep to prevent Roar).
- Turn 3+: NIGHT SHADE. (Fixed damage).

# Quick Claw Quest
- NPC: Teacher sitting on a bench in the northeast section of National Park.
- Coordinates: Pending verification from agent.
- Path: Enter National Park from Route 35 (3, 5). Head north through grass, then east along fence.

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Traversable with Surf.
- TALL_GRASS / LONG_GRASS: Traversable, triggers encounters.
- HEADBUTT_TREE: Impassable, can be headbutted.
- LEDGE_HOP_DOWN: One-way movement (Down).
- CUT_TREE: Impassable; removable with Cut.
- DOOR / WARP_CARPET: Warps.
- BUOY: Impassable (Olivine City harbor).

# Resources & PC Inventory
- Poke Balls: 1 Ultra, 23 Great, 2 Poke.
- Items: 3 Super Repels, 1 Max Ether, 1 Max Revive, 2 Lemonades.
- PC Box 1 (10/20): RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.

# Start Menu & Navigation Rules
- Rule: Execute menu navigation one step at a time. Do not use long sequences.
- Rule: Always B-mash to clear the screen before starting a menu sequence.
- Rule: Move away from doors/water before menuing.
- Cursor Persistence: Start menu and Pokemon menu remember their last position.
- Fly Map: In Olivine, the cursor defaults to New Bark Town.

# Error Analysis & Lessons
- Menu Hell: 100+ turns lost to long 'navigate_menu_v2' sequences failing. Breaking into chunks now.
- Accidental Actions: Triggered Surf and Strength by not verifying cursor position.
- Wrapping: Start menu wraps (POKEDEX <-> EXIT).

# Swarms & Tracking
- Yanma Swarm: Route 35 (Turn 19540). Verify via Radio.
- Suicune Tracking: Moves on map transition. Snapshot via Pokedex 'Area'.