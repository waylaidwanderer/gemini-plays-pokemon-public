# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the player.
- **Verified Noisy Tiles (Specs)**: 
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28) to (18, 28)
  - Row 29: (17, 29), (18, 29)
- Row 30: (14, 30) is noisy. (15, 30) is clean.
- Row 31: (23, 31) to (29, 31) are noisy. (14, 31) and (15, 31) are clean.
- **Verified Clean Tiles**: Row 23, Row 24, Row 25, Row 27, Row 30 (except 14,30).

## Current Status
- Bird is at (15, 29). Facing: UP.
- Target: (15, 30) (Behind).
- Approach: Silent flank via Row 35.
  1. Move to (14, 35) via (28, 33) -> (28, 34) -> (28, 35).
  2. Move to (14, 31) (Clean).
  3. Move to (15, 31) (Clean) then (15, 30) (Clean).
- Reason: Avoids all noisy tiles. (14, 30) is noisy, so I must enter (15, 30) from the south (15, 31). Row 35 is clean.

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