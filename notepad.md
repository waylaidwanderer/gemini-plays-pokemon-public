# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803*

## Success Condition
Interact from the tile directly behind the bird's facing direction.

## Verified Tile Data
- Noisy (Bird faces player):
  - Row 24: (20, 24)-(25, 24)
  - Row 26: (14, 26), (15, 26)
  - Row 28: (14, 28)-(18, 28)
  - Row 29: (17, 29), (18, 29)
  - Row 30: (14, 30)
  - Row 31: (23, 31)-(29, 31)
- Clean (Silent): Row 22, 23, 25, 27, 29 (except 17, 18), 30 (except 14), 31 (except 23-29), 34, 35.

## Current Status (Turn 3079)
- Bird Position: (15, 29). Facing: LEFT.
- Player Position: (19, 29).
- Plan: Make bird face UP, then catch from (15, 30) silently.
- Steps:
  1. Move to Row 22 via Column 29.
  2. Reach (15, 28) [Noisy] to make bird face UP.
  3. Retreat and go to (15, 31) -> (15, 30) silently via Row 35.
  4. Interact facing UP.