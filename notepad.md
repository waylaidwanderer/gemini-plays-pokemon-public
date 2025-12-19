# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*
*Status: Turn 3094 (300+ turns elapsed)*

## Goal: Catch the bird to obtain HM01 (Cut).

## Success Condition
Interact from the tile directly behind the bird's facing direction.

## Verified Noisy Zones (Specs)
- Zone A: Row 24 (20-25)
- Zone B: Row 26 (14-15)
- Zone C: Rows 28-30 (14)
- Zone D: Rows 28-29 (16-18)
- Zone E: Row 31 (23-28)
- Note: (15, 27), (15, 28), (15, 30), (15, 31) are CLEAN.

## Success Strategy: 'Face UP' Maneuver
1. Step on (15, 26) [Noisy] -> Bird at (15, 29) faces UP.
2. Retreat to (15, 27) [Clean].
3. Reach (15, 30) [Clean] via Row 22, Column 29, and Row 35 (Silent Path).
4. Interact from (15, 30) facing UP.

## Tile Mechanics (Global)
- FLOOR: Passable. Clean ground.
- TWIGS (Specs): Passable. Noisy; bird turns to face the player.
- WALL / DENSE_TREES: Impassable.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable. Requires Cut.
- LEDGE: Passable (One-way).