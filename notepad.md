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

## Current Status (Turn 3101)
- Bird Position: (15, 29). Facing: RIGHT.
- Player Position: (16, 29).
- Plan: Move to (15, 28) [Noisy] to make bird face UP.
- Next Steps: Retreat silently via western corridor and flank to (15, 30).

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