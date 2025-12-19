# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Current Status (Turn 3073)
- **Bird Position**: (28, 31).
- **Bird Facing**: UP (Overwatch 3060).
- **Player Position**: (21, 33).
- **Plan**: Use EMBER to end battle. Then move to (28, 32) via Row 35 (Silent).
- **Silent Path**: (21, 33) -> (21, 35) -> (28, 35) -> (28, 32).

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the player.
- **Verified Noisy Tiles (Specs)**: 
  - Row 24: (20, 24)-(25, 24)
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28)-(18, 28)
  - Row 29: (17, 29), (18, 29)
  - Row 31: (23, 31)-(29, 31)
- **Verified Clean Tiles**: Row 22, 23, 25, 27, 30, 34.

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