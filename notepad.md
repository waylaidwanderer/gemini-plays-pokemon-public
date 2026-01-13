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
- **Strategy**: Ecruteak Shuffle. Transition between Route 37 and Ecruteak City to force roamer movement, then pace in grass.
- **Start Turn**: 44738.
- **Lead**: ICARUS (Lv 19 Pidgeotto). Perfect for Repel trick on Route 37 (wild Lv 13-16, roamers Lv 40).
- **Repel Status**: None active. (Last wore off Turn 44784).
- **Shuffle Progress**: Pacing interrupted by Repel expiration at Turn 44784. Re-applying now.
- **Agent Advice (legendary_tracker)**: Use Repel Trick with Lv 17-39 lead on Route 37/38. Master Ball is best due to Roar.

# Pokemon Info
- Party: ICARUS (19), Calcifer (64), KIMCHI (52), GNEISS (55), GORP (50), XENON (44).
- PC Box 1: 10/20.

# Lessons Learned
- Menu Navigation: Cursor memory is persistent. Split deep navigation into chunks < 50 buttons.
- Fly: Outdoors only.
- Roamers: Move only on map transitions. Shorter pacing sessions (10 steps) are more efficient.
- Repel Step Counting: Log summary only to avoid bloat and errors. Reset count when Repel wears off.