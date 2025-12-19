# Tile Mechanics
- `FLOOR`: Traversable. Standard ground.
- `WALL`: Impassable. Collision type for trees, rocks, and boundaries.
- `WATER`: Impassable. Requires the HM for Surf to traverse.
- `HEADBUTT_TREE`: Impassable. These trees block movement and can be interacted with if the player has Headbutt.
- `LEDGE_HOP_LEFT/RIGHT/DOWN`: One-way traversal. The player can jump over these in the specified direction but cannot return.
- `WARP_CARPET_RIGHT`: Triggers a map transition when walking off the edge of the current map.
- `CUT_TREE`: Impassable until the move Cut is used on it. (Verified at (8, 25)).
- `TALL_GRASS`: Traversable. Walking in this tile can trigger wild Pokémon encounters.
- `LONG_GRASS`: Traversable. Functions like tall grass but with different encounter rates or species. (Observed on Route 34).
- `DOOR`: Triggers a map transition when entered.

# Area Knowledge
## Ilex Forest
- Signpost at (3, 17).
- Shrine at (8, 22): Honors the forest's protector.
- Rocker NPC at (15, 14): Headbutt Tutor.

## Route 34
- Gatehouse to Ilex Forest at (13, 37) and (14, 37).
- Trainer Tips sign at (13, 33).
- Day-Care at (10, 14).

# Strategy: Reach Goldenrod City
- **Goal**: Reach Goldenrod City via Route 34.
- **Plan**: 
    1. Explore Route 34 northwards. (Started Turn 3347)
    2. Battle trainers to level up the team, especially FRITTATA.
    3. Locate Goldenrod City at the north end.

## Lessons Learned
- **Menu Loops**: Turn 3169-3217. Always verify screen text before executing button sequences.
- **Type Matchups**: Onix (Rocky) is 4x weak to Grass (Absorb). Paras is 4x weak to Fire (Ember).
- **Running**: Use Calcifer (Quilava) as lead for high escape probability from wild battles.
- **Tool Hygiene**: Refined find_path_v4 and explore_unseen_v1 to treat 'unseen' tiles as impassable. Added HEADBUTT_TREE and WATER to collision checks.
- **Item Usage**: `use_item_v4` is for the Items pocket only. TMs require manual navigation or a specialized tool (`use_tm_v1`).
- **Nicknaming**: FRITTATA (Togepi) hatched on Turn 3330.
- Defeated Youngster Samuel at (15, 32) on Route 34 (Turn 3374).
## Lessons Learned
- **NPC Collision**: Defeated trainers (and other NPCs) remain as solid objects on the map and must be navigated around. (Observed Turn 3374).
- **Turn Tracking**: Always verify the current turn number from Game State to avoid mismatches.