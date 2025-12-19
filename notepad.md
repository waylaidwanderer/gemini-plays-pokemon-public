# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*
*Status: Turn 3097*

## Goal: Catch the bird to obtain HM01 (Cut).

## Success Condition
Interact from the tile directly behind the bird's facing direction.

## Verified Noisy Zones (Specs)
- Zone A: Row 24 (20-25)
- Zone B: Row 26 (14-15)
- Zone C: Rows 28-30 (14)
- Zone D: Rows 28-29 (16-18)
- Zone E: Row 31 (23-28)

## Silent Path to (15, 30) [Bird faces UP]
1. Step on (15, 26) [Noisy] -> Bird faces UP. (Done)
2. Path: (15, 26) -> (15, 23) -> (20, 23) -> (20, 24) -> (29, 24) -> (29, 33) -> (28, 33) -> (28, 35) -> (14, 35) -> (14, 30) -> (15, 30).
3. Interact from (15, 30) facing UP.

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