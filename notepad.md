# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Current Status (Turn 3063)
- **Bird Position**: (28, 31).
- **Bird Facing**: LEFT.
- **Player Position**: (29, 31).
- **Plan**: Interact (A) from behind to catch the bird.
- **Hypothesis**: Interacting from (29, 31) while the bird faces LEFT satisfies the success condition.

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the player.
- **Verified Noisy Tiles (Specs)**: 
  - Row 24: (20, 24) to (25, 24)
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28) to (18, 28)
  - Row 29: (17, 29), (18, 29)
  - Row 31: (23, 31) to (29, 31)
- **Verified Clean Tiles**: Row 22, Row 23, Row 25, Row 27, Row 30, Row 34.

## Tile Mechanics
- **FLOOR**: Passable. Standard movement.
- **TWIGS (FLOOR with specs)**: Passable. Noisy; bird turns to face the player.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE**: Passable (One-way).

## Strategy: General
- Avoid twigs when approaching from behind.
- Use twigs strategically to change the bird's facing.
- If stuck, move the bird to a new area by startling it.