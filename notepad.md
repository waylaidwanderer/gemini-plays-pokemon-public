# Gem's Johto Adventure

## Quest: Ilex Forest Farfetch'd
- **Apprentice Hint**: "Get behind it."
- **Observed Behavior**:
  - Startle: Interacting from front/side makes it fly ~6 tiles.
  - Turning: Bird turns to face the player if they step on noisy tiles (twigs).
  - Noisy Tiles: (23,31) to (28,31) confirmed. alert the bird when stepped on.
- **Current Status**:
  - Bird Position: (22, 31)
  - Bird Facing: RIGHT
  - Target Tile: (21, 31) (Behind - Blocked by Wall)

## Tile Mechanics
- **FLOOR**: Passable.
- **TWIGS**: Noisy floor tiles (specs on ground). Alert Farfetch'd.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal.

## Strategy: Driving the Bird North
1. Drive bird to (24, 35) by interacting from North or East.
2. Position yourself at (22, 32) (South of bird's landing spot) via the clean floor route around the east (X=29).
3. Drive bird back to (22, 31) from (25, 35) (East).
4. Since you are already at (22, 32), interact from the South to drive it North to (22, 28).
5. From (22, 28), drive it West towards the apprentice.

## Important Locations
- **Azalea Town**:
  - Kurt's House (9, 5): Kurt (3, 2) makes special balls.
  - Charcoal Kiln (21, 13): Apprentice's boss. Reward for Farfetch'd is HM01 Cut.

## Party Status
- **Calcifer (QUILAVA)** Lv22: Lead.
- **Team**: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.

---
*Started Farfetch'd Chase: Turn 2803.*