# Gem's Johto Adventure

## Quest: Ilex Forest Farfetch'd
- **Apprentice Hint**: "Get behind it."
- **Observed Behavior**:
  - Startle: Interacting from front/side makes it fly ~6 tiles.
  - Turning: Bird turns to face the player if they step on noisy tiles (twigs).
  - Noisy Tiles: Row 31 (x=23 to 29) verified. Alert the bird when stepped on.
- **Current Status**:
  - Bird Position: (28, 31)
  - Bird Facing: RIGHT
  - Strategy: Drive bird to a clean row (28, 29, 30, 32, 33, 35) to avoid twig-turning.

## Strategy: Driving North to Row 28
1. Reach (28, 32) (South of bird) without stepping on Row 31.
2. Interact from (28, 32) -> Bird flies North to (28, 28).
3. Since Row 28 is clean (no twigs), sneak behind it at (27, 28) or (29, 28) and catch!

## Tile Mechanics
- **FLOOR**: Passable.
- **TWIGS**: Noisy floor tiles (specs on ground). Alert Farfetch'd. Row 31.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal.

## Important Locations
- **Azalea Town**:
  - Kurt's House (9, 5): Special balls.
  - Charcoal Kiln (21, 13): HM01 Cut reward.

## Party Status
- **Calcifer (QUILAVA)** Lv22: Lead.
- **Team**: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.

---
*Started Farfetch'd Chase: Turn 2803.*