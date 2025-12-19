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

## Current Status (Turn 3102)
- Bird Position: (15, 29). Facing: UP.
- Player Position: (15, 28).
- Plan: Reach (15, 30) (Behind) via the silent western corridor.
- Steps:
  1. Move to (15, 27) [Clean].
  2. Move to (8, 27) [Clean].
  3. Move to (8, 34) [Clean].
  4. Move to (14, 34) [Clean].
  5. Move to (14, 31) [Clean] -> (15, 31) [Clean] -> (15, 30) [Clean].
  6. Interact from (15, 30) facing UP.

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