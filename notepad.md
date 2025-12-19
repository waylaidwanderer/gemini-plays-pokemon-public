# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Goal: Catch the bird to obtain HM01 (Cut).

## Puzzle Mechanics
- **Apprentice Hint**: "You have to get behind it to catch it."
- **Startle Logic**: Interacting from the front or side makes the bird fly ~6 tiles along the path.
- **Twig Logic**: Tiles with dark specs are noisy. Stepping on them makes the bird turn to face the player.
- **Noisy Rows**: 28, 31, 32, 33, 34, 35 (Verified by specs on ground).
- **Clean Rows**: 22, 23, 24, 25, 26, 27, 29, 30.
- **Success Condition**: Interact from the tile directly behind the bird's facing direction WITHOUT alerting it (use clean ground).

## Strategy: Current Status
- Bird at (28, 31), Facing LEFT.
- Player at (28, 30), Facing DOWN. (Side interaction).
- Plan: Interact to drive bird to (22, 31). Then catch on clean ground if possible.

## Tile Mechanics
- **FLOOR**: Passable. Clean ground.
- **TWIGS**: Noisy floor (specs on ground). Alert Farfetch'd. (Rows 28, 31-35).
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal.

## Locations & Progress
- **Charcoal Kiln**: Azalea (21, 13). Reward for this quest is Cut.
- **Badges**: Zephyr, Hive.

## Party
- Calcifer (QUILAVA) Lv22, ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.
- Note: Use 'battle_strategist_v3' for wild encounters.

---
## Chase History (Archived)
- Attempt 1 (T2867): North (28, 30) -> Bird (28, 31) South.
- Attempt 2 (T2878): West (23, 35) -> Bird (24, 35) Right.
- Attempt 3 (T2888): East (29, 31) -> Bird (28, 31) Left.
- Attempt 4 (T2892): East (23, 31) -> Bird (22, 31) Right.
- Attempt 5 (T2897): East (25, 35) -> Bird (24, 35) Left.
- Attempt 6 (T2901): East (23, 31) -> Bird (22, 31) Left.
- Attempt 7 (T2905): East (25, 35) -> Bird (24, 35) UP.
- Attempt 8 (T2936): West (28, 22) -> Bird (29, 22) LEFT. ( hallu check: verified bird at 28,31 in T2943)