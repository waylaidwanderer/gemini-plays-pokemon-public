# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Success Condition
Interact from the tile directly behind the bird's facing direction.

## Current Status (Turn 3086)
- **Bird Position**: (15, 29).
- **Bird Facing**: LEFT.
- **Player Position**: (14, 33).
- **Plan**: Make bird face UP, then catch from (15, 30).
- **Steps**:
  1. Step on (15, 28) [Noisy] to make it face UP.
  2. Retreat to (14, 34) via Row 27 and western corridor.
  3. Reach (15, 30) via (14, 31) -> (15, 31).
  4. Interact from (15, 30) facing UP.
- **Reason**: (15, 31) and (15, 30) are clean. Approach from (14, 30) is noisy.

## Verified Tile Data
- Noisy (Bird faces player):
  - Row 24: (20, 24)-(25, 24)
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28)-(18, 28)
  - Row 29: (17, 29), (18, 29)
  - Row 30: (14, 30)
  - Row 31: (23, 31)-(29, 31)
- Clean (Silent): Row 22, 23, 25, 27, 29 (except 17, 18), 30 (except 14), 31 (except 23-29), 34, 35.

## Tile Mechanics (Global)
- **FLOOR**: Passable. Clean ground.
- **TWIGS (FLOOR with specs)**: Passable. Noisy; bird turns to face the player.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE**: Passable (One-way: Down, Left, or Right).