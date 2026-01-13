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

# Legendary Roamer Hunt
- **Strategy**: Ecruteak Shuffle (R37 <-> Ecruteak). Roamers move on map transitions. Shuffle, then take 1-2 steps in grass. Repeat until first encounter.
- **Lead**: ICARUS (Lv 19 Pidgeotto). Perfect for Repel trick on Route 37 (wild Lv 13-16, roamers Lv 40).
- **Repel Status**: Super Repel active. Applied Turn 44824. (183 steps remaining).
- **Current Task**: Executing Ecruteak Shuffle. Moving to Ecruteak City warp. (Turn 44835).
- **Roamer Status**: Raikou/Entei roaming. NOT YET ENCOUNTERED. They will not appear on the Pokegear map until the first battle.
- **Catching Strategy**: Master Ball immediately upon first encounter.
- **Agent Advice**: Raikou is the target. Use Repel Trick with lead Lv 20-39 on Route 37/38. Use Master Ball. (Current lead ICARUS Lv 19 works for R37 wild Lv 13-16). Ecruteak Loop (Shuffle) is best. Master Ball on first encounter.

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Lessons Learned
- Roamers: Do NOT appear on Pokegear map until first encounter. Red dots on map are NOT roamers.
- Menu Navigation: Cursor memory is persistent. Every button press must be an individual string in the array for menu_navigator_v2.
- Fly: Outdoors only.
- Repel Step Counting: Reset count when Repel wears off.
- Tool Interruptions: Repel messages and phone calls interrupt tools like grass_pacer. Clear text before resuming.