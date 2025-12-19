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
  - Row 29: (17, 29), (18, 29)
  - Row 31: (23, 31) to (29, 31)
- **Verified Clean Tiles**: Row 23, Row 24, Row 25, Row 27, Row 30. (14-16, 29) are clean.

## Current Status
- Bird at (15, 29). Facing: RIGHT.
- Player at (16, 29). Facing: LEFT.
- Action: Clearing text "Kwaa!". Bird will fly.

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

---
## Lessons Learned
- Approaching a bird on clean ground from a noisy tile alerts it even if the final tile is clean.
- Bird turns to face the source of the noise.
- Driving the bird to an open area with clean ground is essential.