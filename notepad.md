# Ilex Forest Quest: Runaway Farfetch'd
*Started Turn 2803. Current: Turn 3115 (312 turns elapsed).*

## Goal: Catch the bird to obtain HM01 (Cut).

## Success Condition
Interact from the tile directly behind the bird's facing direction.
**CRITICAL**: You must reach the 'Behind' tile WITHOUT stepping on any noisy tiles.

## Verified Noisy Tiles (Specs)
- Row 26: (14, 26), (15, 26)
- Row 28: (14, 28), (16, 28), (17, 28), (18, 28)
- Row 29: (17, 29), (18, 29)
- Row 30: (14, 30)
- Row 31: (23, 31) to (29, 31)
- **Clean Spots**: (15, 27), (15, 28), (15, 30), (15, 31), Row 34-35.

## Current Status (Turn 3115)
- Bird Position: (15, 29). Facing: LEFT.
- Player Position: (15, 28).
- Plan: Make bird face UP, then catch from (15, 30) silently.
- Steps:
  1. Move to (15, 26) [Noisy] -> Bird faces UP.
  2. Retreat to (15, 27) [Clean].
  3. Loop around via Row 34/35 to reach (15, 31) silently.
  4. Move to (15, 30) [Clean] and interact facing UP.

## Tile Mechanics (Global)
- FLOOR: Passable. Clean ground.
- TWIGS (Specs): Passable. Noisy; bird turns to face the player.
- WALL / DENSE_TREES: Impassable.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable. Requires Cut.
- LEDGE: Passable (One-way).

## Party Status
- Calcifer (QUILAVA) Lv22: Lead. Use 'battle_strategist_v3'.
- Team: ROCKY (ONIX), GNEISS (GEODUDE), ICARUS (PIDGEY), EGG (TOGEPI), APOPHIS (EKANS).