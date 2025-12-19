# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Apprentice Hint**: "You have to get behind it to catch it."
- **Startle Logic**: Interacting from any side makes the bird fly ~6 tiles along the forest path away from the player.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them near the bird makes it turn to face the player.
- **Success Condition**: Interact with the bird from the tile directly behind its facing direction without stepping on twigs during the approach.

## Strategy: Current Status
- **Bird**: (15, 29), Facing: UP.
- **Player**: (16, 29), Facing: LEFT. (Side interaction).
- **Environment**: Row 28 and Row 31 are noisy (twigs). Rows 29 and 30 are clean.
- **Plan**: Interact from (16, 29) to drive bird West. Track landing spot.

## Tile Mechanics
- **FLOOR**: Passable. Clean ground (Rows 29, 30).
- **TWIGS**: Noisy ground (specs). Alert Farfetch'd. (Rows 28, 31).
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal.

## Locations & Progress
- **Charcoal Kiln**: Azalea (21, 13). Reward: Cut.
- **Badges**: Zephyr, Hive.

## Party Status
- Calcifer (QUILAVA) Lv22: Lead. Use 'battle_strategist_v3' for wild encounters.
- Team: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.