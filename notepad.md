# Global Tile Mechanics
- FLOOR: Traversable.
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
- **HOW**: Ecruteak Shuffle. Transition between Route 37 and Ecruteak City at (7,0)/(17,36). Roamers move ONLY on map transitions.
- **Lead**: ICARUS (Lv 19 Pidgeotto). Perfect for Repel trick on Route 37 (wild Lv 13-16, roamers Lv 40).
- **Repel Status**: Super Repel active. Applied Turn 44824. (~150 steps remaining).
- **Roamer Status**: Raikou/Entei roaming. NOT YET ENCOUNTERED. (Red dots on Pokegear are cities).
- **Catching Strategy**: Master Ball immediately upon first encounter.
- **Agent Advice (legendary_tracker)**: Use Repel Trick with Lv 20-39 lead on Route 37/38. Master Ball is best due to Roar. Ecruteak Loop (Shuffle) is the most efficient method.

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Lessons Learned
- **Roamers**: Do NOT appear on Pokegear map until first encounter.
- **Shuffle**: Map transitions move roamers. Shuffling is better than long pacing.
- **Menu Navigation**: Every button press must be an individual string in `menu_navigator_v2`.
- **Repel Logic**: ICARUS (Lv 19) is perfect for Route 37 (Wild Lv 13-16) to filter for Roamers (Lv 40).
- **Tool Interruptions**: Repel expiration and phone calls stop tool execution. Clear text before resuming.
- **Tool Hygiene**: Ensure `menu_navigator_v2` sequences are individual strings, not comma-separated blocks.