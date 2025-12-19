# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803. Reflection Turn 2960.*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Apprentice Hint**: "You have to get behind it to catch it."
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles along the forest path away from the player.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them near the bird makes it turn to face the player.
- **Verified Noisy Tiles (Specs)**: 
  - (14,28), (15,28), (17,28), (18,28)
  - (23,31), (24,31), (25,31), (26,31), (27,31), (28,31), (29,31)
- **Verified Clean Tiles**: Row 23, Row 24, Row 29, Row 30.
- **Success Condition**: Interact with the bird from the tile directly behind its facing direction without stepping on twigs during the approach.

## Strategy: Current Plan
1. **Status**: Bird is at (15, 25) facing DOWN.
2. **Target**: (15, 24) (Behind).
3. **Approach**: Circle via Row 23 (Clean) to reach (15, 24).
4. **Action**: Interact from (15, 24) to catch.

## Tile Mechanics
- **FLOOR**: Passable.
- **TWIGS**: Noisy floor (specs). Alerts bird.
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