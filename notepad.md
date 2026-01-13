# Global Tile Mechanics
- FLOOR: Traversable. (7, 0) R37 and (17, 36) Ecruteak are walk-off warps.
- WALL: Impassable.
- HEADBUTT_TREE: Impassable. Interacts with Headbutt.
- TALL_GRASS: Traversable. Triggers encounters.
- LEDGE_HOP_DOWN: One-way jump down.
- FLOOR_UP_WALL: Traversable.
- WATER: Requires Surf.
- DOOR/WARP: Transition to another map.
- WARP_CARPET: Transition to another map.
- LEDGE_HOP_RIGHT: One-way jump right.

# Legendary Roamer Hunt (Started Turn 44738)
- **Strategy**: Manual Ecruteak Shuffle (R37 <-> Ecruteak). Roamers move on map transitions. Transition, pace 4-10 steps in grass, repeat. Manual buttons are used to bypass tool fragility with warps.
- **Lead**: ICARUS (Lv 19 Pidgeotto). Correct for R37 (Wild Lv 13-16) to filter for Roamers (Lv 40).
- **Repel Status**: Active (Turn 44880). ~150 steps remaining. Inventory: 72.
- **Strategy**: Ecruteak Shuffle.
- **Current Action**: Moving to grass at (8, 2) to pace. Transition 8. Session started Turn 44880.
- **Roamer Search History**:
    - Session 1 (Turns 44738-44876): 10+ transitions, 0 encounters. Interrupted by Repel expiration.
    - Session 2 (Turn 44880-Present): 7 transitions complete. Super Repel active. Strategy: 10 steps in grass per transition. Currently on transition 8.

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Lessons Learned
- **Roamers**: Do NOT appear on Pokegear map until first encounter.
- **Shuffle**: Map transitions move roamers. Manual press_buttons is more robust than tools for multi-map loops.
- **Repel Logic**: ICARUS (Lv 19) is perfect for Route 37 to filter for Roamers.
- **Tool Interruptions**: Repel expiration and phone calls stop tool execution. Clear text before resuming.
- **Tool Hygiene**: Ensure menu_navigator_v2 sequences are individual strings. Avoid multi-warp tool sequences.