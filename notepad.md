# Tile Mechanics
- TALL_GRASS: Traversable. Triggers wild encounters. Verified: Yes.
- FLOOR: Traversable. Verified: Yes.
- WALL: Impassable. Verified: Yes.
- HEADBUTT_TREE: Impassable. Verified: Yes.
- LEDGE_HOP_DOWN: One-way traversable (down only). Verified: Yes.

# Legendary Roamer Hunt Strategy
- **Overview**: Manual Ecruteak Shuffle (R37 <-> Ecruteak). Roamers move on map transitions. Transition, pace 10 steps in grass, repeat.
- **Session 2 Start**: Turn 44880 (2026-01-12 21:30).
- **Lead**: ICARUS (Lv 19 Pidgeotto). Correct for R37 (Wild Lv 13-16) to filter for Roamers (Lv 40) using Repel Trick.
- **Repel Status**: Active (Turn 44936). ~190 steps remaining. (Inventory: 71 Super Repels).
- **Roamer Status**: Raikou/Entei roaming. NOT YET ENCOUNTERED.
- **Catching Strategy**: Master Ball immediately upon first encounter.

# Progress Log
- **Session 1 (Turns 44738-44876)**: 10+ transitions, 0 encounters.
- **Session 2 (Turn 44880-Present)**:
    - Transitions 1-17: 0 encounters.
    - Transition 18: Ready to start (Moving to Ecruteak).

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Lessons Learned
- **Roamers**: Do NOT appear on Pokegear map until first encounter.
- **Repel Logic**: ICARUS (Lv 19) is perfect for Route 37 to filter for Roamers.
- **Tool Hygiene**: Move to the target tile in one turn and initiate the tool in the next to avoid input conflicts. Do not chain press_buttons with grass_pacer.
- **Menu Persistence**: The cursor position in the main menu and pack is persistent. Always verify the starting selection before executing a long `menu_navigator_v2` sequence.
- **Phone Calls**: Scripted phone calls interrupt menu sequences and tools. Close text before retrying.