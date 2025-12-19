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
  - Row 31: (23, 31) to (29, 31)
- **Verified Clean Tiles**: Row 23, Row 24, Row 25, Row 27, Row 30.

## Current Status
- Bird is at (15, 29). Facing: UP.
- Target: (15, 30) (Behind).
- Approach: Sneak around via the far left. 
  1. Move to (15, 25) to leave.
  2. Go to Entrance (3, 42) via the corridor at col 29.
  3. Go up far left (col 1) to Row 29.
  4. Go right to col 8, then down to Row 34.
  5. Go right to (14, 34), then up to (15, 30).
- Reason: Avoids all noisy tiles near the bird while it's facing UP. Row 34 passage at (14, 34) is the key.

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