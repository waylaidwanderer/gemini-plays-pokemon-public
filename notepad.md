# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the sound.
- **Noisy Tiles (Specs)**: 
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28) to (18, 28)
  - Row 31: (23, 31) to (29, 31)
- **Verified Clean Tiles**: Rows 22, 23, 24, 25, 27, 29, 30.

## Strategy: Current Plan
1. **Status**: Bird is at (15, 29). Facing: LEFT.
2. **Target**: (16, 29) (Behind).
3. **Approach**: Path via Row 23 (Clean) -> X=22 (Clean) -> Row 29 (Clean) to reach (16, 29).
4. **Action**: Interact LEFT from (16, 29) to catch.

## Tile Mechanics
- **FLOOR**: Clean ground. Passable.
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