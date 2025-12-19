# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Apprentice Hint**: "You have to get behind it to catch it."
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles along the forest path away from the player.
- **Twig Logic**: Tiles with dark specs (Verified Row 31, X=23-29) are noisy. Stepping on them while near the bird makes it turn to face the player, preventing a 'behind' interaction.
- **Success Condition**: Interact with the bird from the tile directly behind its current facing direction WITHOUT stepping on noisy twigs during the approach.

## Strategy: Driving & Catching
- **Problem**: Noisy twigs on Row 31 prevent sneaking behind the bird when it hides in that row.
- **Solution**: Drive the bird to a location on clean ground (Rows 22-30, 32-35) where a stealthy approach is possible.
- **Current Status**: Bird is at (24, 35) facing DOWN. Row 35 is clean ground.
- **Plan**: Interact from (25, 35) (East) to drive it West towards the apprentice's area.

## Tile Mechanics
- **FLOOR**: Passable. Clean ground.
- **TWIGS**: Noisy floor (specs on ground). Alert Farfetch'd. (Verified Row 31, X=23-29).
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal in the direction of the ledge.

## Locations & Progress
- **Charcoal Kiln**: Azalea (21, 13). Reward for this quest is HM01 Cut.
- **Badges**: Zephyr, Hive.

## Party Status
- Calcifer (QUILAVA) Lv22: Lead. Use 'battle_strategist_v3' for battle reasoning.
- Team: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.