# Gem's Johto Adventure

## Quest: Ilex Forest Farfetch'd
- **Apprentice Hint**: "Get behind it."
- **Observed Behavior**:
  - Startle: Interacting from front/side makes it fly ~6 tiles.
  - Turning: Bird turns to face the player if they step on noisy tiles (twigs).
  - Noisy Tiles: Verified Row 31 (specs on ground). Alert the bird when stepped on.

## Strategy: Catching at (28, 31)
1. Bird is at (28, 31). Assuming it faces LEFT.
2. Target: (29, 31) (Behind).
3. Path: Avoid Row 31 near the bird. Go around via Row 35 or Row 30.
4. Catch: Interact from (29, 31).

## Tile Mechanics
- **FLOOR**: Passable.
- **TWIGS**: Noisy floor tiles (specs on ground). Alert Farfetch'd. Verified Row 31.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal.

## Important Locations
- **Azalea Town**:
  - Kurt's House (9, 5): Kurt (3, 2) makes special balls.
  - Charcoal Kiln (21, 13): Apprentice's boss. Reward for Farfetch'd is HM01 Cut.

## Party Status
- **Calcifer (QUILAVA)** Lv22: Lead.
- **Team**: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.

---
*Started Farfetch'd Chase: Turn 2803.*