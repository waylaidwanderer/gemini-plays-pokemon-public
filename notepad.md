# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*
*Status: Turn 3098 (295 turns elapsed)*

## Goal: Catch the bird to obtain HM01 (Cut).

## Success Condition
Interact from the tile directly behind the bird's facing direction.

## Verified Noisy Zones (Specs)
- Zone A: Row 24 (20-25)
- Zone B: Row 26 (14-15)
- Zone C: Rows 28-30 (14)
- Zone D: Rows 28-29 (16-18)
- Zone E: Row 31 (23-28)
- Note: (15, 27), (15, 30), (15, 31) are CLEAN. (15, 28) is NOISY.

## Success Strategy: 'Face UP' Maneuver
1. Step on (16, 28) [Noisy] -> Bird at (15, 29) faces UP.
2. Retreat silently: (16, 28) -> Row 23 -> Column 29.
3. Flank via Row 35: (29, 35) -> (14, 35) -> (14, 31) -> (15, 31) -> (15, 30).
4. Interact from (15, 30) facing UP.
- Note: (15, 30) is clean and behind an UP-facing bird.

## Tile Mechanics (Global)
- FLOOR: Passable. Clean ground.
- TWIGS (Specs): Passable. Noisy; bird turns to face the player.
- WALL / DENSE_TREES: Impassable.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable. Requires Cut.
- LEDGE: Passable (One-way).

## Strategy: General
- Use 'battle_strategist_v3' for all wild encounters.
- Avoid noisy zones when approaching from behind.