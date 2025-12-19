# Tile Mechanics
- `FLOOR`: Traversable. Standard ground.
- `WALL`: Impassable. Collision type for trees, rocks, and boundaries.
- `WATER`: Impassable. Requires the HM for Surf to traverse.
- `HEADBUTT_TREE`: Impassable. These trees block movement and can be interacted with if the player has Headbutt.
- `LEDGE_HOP_LEFT/RIGHT/DOWN`: One-way traversal. The player can jump over these in the specified direction but cannot return.
- `WARP_CARPET_RIGHT`: Triggers a map transition when walking off the edge of the current map.
- `CUT_TREE`: Impassable until the move Cut is used on it. (Verified at (8, 25)).

# Area Knowledge: Ilex Forest
- Signpost at (3, 17).
- Shrine at (8, 22): Honors the forest's protector.
- Rocker NPC at (15, 14).
- Item: X Attack at (9, 17) (Picked up Turn 3262).

# Strategy: Ilex Forest Exploration
- **Goal**: Reach Goldenrod City via the northern exit of Ilex Forest.
- **Progress**: TM02 Headbutt obtained (Turn 3298). Calcifer learned HEADBUTT, replacing LEER (Turn 3311).
- **Plan**: Navigate to the northern exit. Note that HEADBUTT_TREE tiles remain impassable even after interaction.
- Navigation to Northern Exit started at Turn 3266. Resuming from (13, 1).

## Lessons Learned
- **Menu Loops**: Turn 3169-3217. Always verify screen text before executing button sequences.
- **Type Matchups**: Onix (Rocky) is 4x weak to Grass (Absorb).
- **Running**: Use Calcifer (Quilava) as lead for high escape probability from wild battles.
- **Tool Hygiene**: Refined find_path_v4 and explore_unseen_v1 to treat 'unseen' tiles as impassable. Added HEADBUTT_TREE and WATER to collision checks.
- Encountered and defeated a wild Psyduck at (29, 5) (Turn 3288). gained 80 EXP.
- Item: Antidote at (17, 7) (Picked up Turn 3280).
- Item: Ether at (27, 1) (Picked up Turn 3284).