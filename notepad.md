# Gem's Johto Adventure

## Quest: Ilex Forest Farfetch'd
- **Apprentice Hint**: "Get behind it."
- **Observed Behavior**:
  - Startle: Interacting (A button) makes it fly ~6 tiles away from the player along the forest path.
  - Noisy Tiles (Twigs): Stepping on these (specs on ground) makes the bird turn to face the player.
  - Twig Locations: Row 31 (X=23 to 29) verified.

## Strategy: Catching the Bird
- **Problem**: Approaching from twigs causes the bird to turn, preventing a "behind" interaction.
- **Solution**: Drive the bird to clean floor (Rows 22-30, 32-35) or approach from behind on clean floor.
- **Driving Direction**: Bird flies away from the player's interaction point (e.g., interact from South -> flies North).

## Tile Mechanics
- **FLOOR**: Passable. Clean ground.
- **TWIGS**: Noisy floor (specs on ground). Alert Farfetch'd when stepped on. Verified Row 31.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable.
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal.

## Important Locations
- **Azalea Town**:
  - Kurt's House (9, 5): special balls from Apricorns.
  - Charcoal Kiln (21, 13): Reward for quest is HM01 Cut.

## Party Status
- **Calcifer (QUILAVA)** Lv22: Lead.
- **Team**: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.

---
*Started Farfetch'd Chase: Turn 2803.*