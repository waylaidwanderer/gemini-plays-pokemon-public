# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Success Condition
Interact from the tile directly behind the bird's facing direction.

## Current Status (Turn 3083)
- **Bird Position**: (15, 29).
- **Bird Facing**: UP.
- **Player Position**: (9, 34) [In Battle].
- **Plan**: Reach (15, 30) (Behind) silently.
- **Silent Path**: Approach from the south via Row 34/35. (15, 31) and (14, 31) are clean.
- **Noisy Barriers**: Avoid Row 28 (14-18), Row 29 (17-18), Row 30 (14), Row 31 (23-29).

## Puzzle Mechanics
- **Success Condition**: Interact from the tile directly behind the bird's facing direction.
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles away.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the player.

## Tile Mechanics (Global)
- **FLOOR**: Passable. Clean ground.
- **TWIGS (FLOOR with specs)**: Passable. Noisy; bird turns to face the player.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE**: Passable (One-way: Down, Left, or Right).

## Strategy: General
- Avoid twigs when approaching from behind.
- Use twigs strategically to change the bird's facing.
- If stuck, move the bird to a new area by startling it.