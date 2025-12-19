# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Apprentice Hint**: "You have to get behind it to catch it."
- **Startle Logic**: Interacting from any side makes the bird fly ~6 tiles along the forest path away from the player.
- **Twig Logic**: Tiles with dark specs are noisy (Row 31 verified). Stepping on them near the bird makes it turn to face the player.
- **Success Condition**: Interact with the bird from the tile directly behind its facing direction without stepping on twigs during the approach.

## Strategy: Current Plan
1. **Status**: Bird is at (22, 31) facing UP.
2. **Action**: Catch bird by interacting from the South (22, 32).
3. **Approach**: Already at (22, 32) behind it.

## Tile Mechanics
- **FLOOR**: Passable. Clean ground.
- **TWIGS**: Noisy floor (specs on ground). Alert Farfetch'd. (Verified Row 31, X=23-29). (22, 31) is clean.
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