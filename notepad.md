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
- **Verified Clean Tiles**: Row 23, Row 24, Row 25, Row 27, Row 30, Row 34.

## Tile Mechanics
- **FLOOR**: Passable. Clean ground.
- **TWIGS (FLOOR with specs)**: Noisy. Alerts bird to player's presence, causing it to face them.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable. Can be headbutted later.
- **CUT_TREE**: Impassable. Requires HM01 Cut to clear.
- **LEDGE**: One-way traversal (down, left, or right).

## Party Status
- Calcifer (QUILAVA) Lv22: Lead. Use 'battle_strategist_v3' for wild encounters.
- Team: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.