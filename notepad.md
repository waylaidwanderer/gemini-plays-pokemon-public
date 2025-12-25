# Suicune Hunt Strategy (Crystal)
- Status: ROAMING (Post-Tin Tower).
- Lead: XENON (Gastly Lv21) with Mean Look and Hypnosis.
- Strategy: Boundary cycling between Route 38 and Ecruteak City.
- Goal: Get Quick Claw to mitigate Speed issues.

# Suicune Battle Plan
- Turn 1: MEAN LOOK.
- Turn 2+: HYPNOSIS. (Priority: KEEP ASLEEP to prevent ROAR).
- Turn 3+: NIGHT SHADE (fixed damage).
- Failsafe: Roar ends the battle even with Mean Look. Keep it asleep!

# Quick Claw Quest
- Location: National Park (16, 12).
- NPC: Lady with Persian on a bench in the northeast area.
- Access: Enter National Park from Route 35 (3, 5).

# Tile Mechanics (Verified)
- FLOOR: Traversable.
- WALL: Impassable.
- WATER: Walkable with Surf.
- TALL_GRASS: Traversable, triggers encounters.
- HEADBUTT_TREE: Impassable, can be headbutted.
- LEDGE_HOP_DOWN: One-way movement (Down).
- CUT_TREE: Impassable; removable with Cut.
- DOOR/WARP_CARPET: Warps.
- BUOY: Impassable (Olivine City harbor).

# Resources & PC
- Balls: 1 Ultra, 23 Great, 2 Poke.
- Items: 3 Super Repels.
- PC Box 1: RICOTTA, CINNABAR, VORTEX, INTERCEPT, ROCKY, EGG, XFDW, FRITTATA, SHUCKIE, Blarney.

# Task Progress
- Quick Claw Quest started: Turn 19471.
- Suicune Log: Confirmed on Route 42, then Ecruteak City (Turn 19477).

# Error Analysis & Lessons
- Menu Navigation: Always clear screen text with B before starting a menu sequence.
- Fly Map: Verify current city in Game State before calling navigate_fly_map.
- Roaming Tracking: Suicune moves every time the player crosses a map boundary. Pokedex checks are snapshots.

# Menu Navigation Debugging
- Problem: Persistent cursor makes menu navigation unpredictable.
- Hypothesis: Resetting to the top of the menu using multiple "Up" presses will provide a consistent starting point.
- Test 1: Press Start, then Up 7 times, then Down 1 time to reach POKEMON.