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

# Strategy: HM Cut
- **Goal**: Reach Goldenrod City.
- **How**: Use KIMCHI's CUT to clear the tree at (8, 25) in Ilex Forest. (Tree cleared Turn 3246).
- **Recruitment**: KIMCHI (Oddish) caught in Ilex Forest, now in party slot 6. Learned CUT (Turn 3233).

## Lessons Learned
- **Menu Loops**: Turn 3169-3217. Always verify screen text before executing button sequences.
- **Type Matchups**: Onix (Rocky) is 4x weak to Grass (Absorb).
- **Running**: Use Calcifer (Quilava) as lead for high escape probability from wild battles.
- **Tool Hygiene**: Ensure navigation tools account for all impassable tile types, including HEADBUTT_TREE.
- Navigation to Northern Exit started at Turn 3266.