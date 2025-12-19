# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the player.
- **Noisy Tiles (Specs)**: 
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28) to (18, 28)
  - Row 31: (23, 31) to (29, 31)
  - Row 29: (17, 29), (18, 29)
- **Verified Clean Tiles**: Rows 22, 23, 24, 25, 27, 30.

## Current Status
- Bird is at (20, 24). Facing: LEFT.
- Target: (21, 24) (Behind).
- Approach: Reach (21, 24) via Row 25 (Clean).

## Tile Mechanics
- **FLOOR**: Passable. Clean ground.
- **TWIGS**: Noisy floor (specs). Alerts bird.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.

## Locations & Progress
- **Charcoal Kiln**: Azalea (21, 13). Reward: Cut.
- **Badges**: Zephyr, Hive.

## Party Status
- Calcifer (QUILAVA) Lv22: Lead. Use 'battle_strategist_v3' for wild encounters.
- Team: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.