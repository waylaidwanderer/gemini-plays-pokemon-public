# Gem's Johto Adventure

## Quest: Ilex Forest Farfetch'd
- **Apprentice Hint**: "Get behind it."
- **Observed Behavior**:
  - Startle: Interacting (A button) makes it fly ~6 tiles away from the player.
  - Noisy Tiles (Twigs): Stepping on these (specs on ground) makes the bird turn to face the player.
  - Twig Locations: Row 31 (X=23 to 29) verified.

## Strategy: Driving to Clean Ground
- **Problem**: Cannot "get behind" the bird on Row 31 because it turns when I approach.
- **Solution**: Drive the bird to a row without twigs (Row 28 or 35).
- **Current Plan (Bird at 28, 31)**:
  1. Reach (28, 32) (South) without stepping on Row 31.
  2. Interact from (28, 32) -> Bird flies North to (28, 28) (Hypothesis).
  3. Row 28 is clean ground. Catch it there.

## Tile Mechanics
- **FLOOR**: Passable.
- **TWIGS**: Noisy floor (specs on ground). Alert Farfetch'd when stepped on. Verified Row 31 (X=23-29).
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