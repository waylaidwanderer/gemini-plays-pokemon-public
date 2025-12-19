# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the source.
- **Noisy Tiles (Specs)**: 
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28) to (18, 28)
  - Row 31: (23, 31) to (29, 31)
- **Verified Clean Tiles**: Row 23, Row 24, Row 25, Row 27, Row 29, Row 30.

## Current Status
- Bird at (15, 25). Facing: DOWN (Alerted by noise at 15, 26).
- Player at (15, 26). Facing: UP.
- Strategy: Drive North to Row 23 (Clean ground).
  1. Interact from (15, 26) -> Bird flies to (15, 23).
  2. Bird should face UP at (15, 23).
  3. Move to (15, 24) (Behind) on clean ground.
  4. Catch.

## Tile Mechanics
- **FLOOR**: Passable. Clean ground.
- **TWIGS**: Noisy ground (specs). Alerts bird.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.

## Locations & Progress
- **Charcoal Kiln**: Azalea (21, 13). Reward: Cut.
- **Badges**: Zephyr, Hive.

## Party Status
- Calcifer (QUILAVA) Lv22: Lead. Use 'battle_strategist_v3' for wild encounters.
- Team: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.