# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the player.

## Tile Mechanics (Verified)
- **FLOOR**: Passable. Clean ground.
- **TWIGS (FLOOR with specs)**: Passable. Noisy floor; alerts bird.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE**: Passable (One-way: Down, Left, or Right).

## Verified Noisy Tiles (Specs)
- Row 24: (20, 24) to (25, 24)
- Row 26: (14, 26), (15, 26)
- Row 28: (14, 28) to (18, 28)
- Row 29: (17, 29), (18, 29)
- Row 31: (23, 31) to (29, 31)

## Quest Log
- **Turn 3063**: Interacted from (29, 31) [Behind]. Bird turned to face player (RIGHT). Catch failed.
- **Turn 3076**: Bird is at (22, 31), Facing DOWN. Player at (22, 32).
- **Plan**: Startle from front to move it.