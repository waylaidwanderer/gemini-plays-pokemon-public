# Ilex Forest Strategy: Catching Farfetch'd

## Goal: Catch the runaway Farfetch'd to obtain HM01 (Cut).

## Farfetch'd Chase Mechanics
- **Success Condition**: "You have to get behind it to catch it." (Apprentice hint).
- **Flight Logic**: The bird flies ~6 tiles away from the player's interaction point along the forest path.
- **Hypothesis**: The bird turns to face the player before fleeing if approached from behind. Catching may require driving it to a specific spot or using noisy tiles (twigs) to distract it.
- **Interaction History**:
  - T2892: Player at (23, 31) (East), Bird at (22, 31) faced Right. Result: Flew to (24, 35).
  - T2905: Player at (25, 35) (East), Bird at (24, 35) faced UP. Result: Flew to (22, 31).

## Procedure to drive Bird North:
1. Bird is at (22, 31) facing LEFT.
2. Interact from (23, 31) (East) -> Bird flies to (24, 35).
3. Move to (22, 32) (South of bird's future landing spot).
4. Interact with bird at (24, 35) from East (25, 35) -> Bird flies back to (22, 31).
5. Now Player is at (22, 32) and Bird is at (22, 31).
6. Interact from (22, 32) (South) -> Bird flies North to (22, 28).

## Tile Mechanics
- FLOOR: Passable.
- WALL / DENSE_TREES: Impassable.
- HEADBUTT_TREE: Impassable (Verified at 28, 24 and 22, 34).
- CUT_TREE: Impassable. Requires HM01 Cut.
- LEDGE_HOP: One-way traversal in the direction of the arrow.

## Key Locations
- **Apprentice**: (7, 28).
- **Charcoal Kiln**: Azalea Town (21, 13).

## Party Status
- **Calcifer (QUILAVA) Lv22**: Lead.
- **Team**: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.