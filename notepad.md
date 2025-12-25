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
- Location: National Park (18, 12).
- NPC: Lady on a bench in the northeast area.
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

# Menu Navigation & Fly Map Defaults
- Olivine City: FLY cursor defaults to New Bark Town.
- Reset Strategy: Press Start, then Up 7 times to reach the top of the menu (POKEDEX), then Down 1 to reach POKEMON.
- Verification: Always check Game State Map ID and City before using navigate_fly_map.
- Clear Screen: Always press B multiple times to ensure no dialogue or menu is active before starting a sequence.

# Error Analysis & Lessons
- Hallucination Warning: Do not trust memory for coordinates. Use item_locator_agent.
- Stagnation: 30 turns lost to menu fumbling in Olivine City. Use the "Up" reset strategy to break loops.
- Roaming Tracking: Suicune moves every time the player crosses a map boundary. Pokedex checks are snapshots.
- Menu Wrapping: The main menu wraps around. Using "Up" from POKEDEX goes to EXIT. Using "Up" from POKEMON goes to POKEDEX.
- Fly Map Logic: navigate_fly_map requires cursor position and target. In Olivine, it starts on New Bark Town.

# Task Progress
- Turn 19523: Reflection performed. Notepad cleaned.
- Quick Claw Search: In progress.
- Suicune Tracking: Roaming.

# Reflection Turn 19523
- Immediate Execution: I previously deferred cleaning up the notepad and verifying the Fly cursor logic. Done now.
- Notepad Hygiene: Reorganized and added menu wrapping/Fly cursor lessons. Added task progress log.
- Map Hygiene: Markers are current for Olivine City.
- Automation Strategy: find_path_v2 and navigate_menu_v2 are active and working well when used with correct logic.
- Goal Clarity: Goals are outcome-based. HOW is in the notepad.
- Error Analysis: Identified menu wrapping as the cause of recent fumbling. Root hypothesis (Up 7 always lands on Pokedex) was wrong due to wrapping. Corrected.