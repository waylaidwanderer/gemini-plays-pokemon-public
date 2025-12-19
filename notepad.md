# Ilex Forest Strategy: Catching Farfetch'd

## Goal: Catch the runaway Farfetch'd to obtain HM01 (Cut).

## Farfetch'd Mechanics
- **Success Condition**: "You have to get behind it to catch it." (Apprentice hint).
- **Approach Mechanic**: 
  - Interacting from the front/side causes flight.
  - It flies in the direction it is facing, then turns 180 degrees.
  - Flight distance appears to be ~6 tiles.
- **Hypothesis**: Catching occurs when interacting from the tile directly behind the bird (opposite its facing) while the bird is trapped or in a specific area.
- **Attempt History**:
  - T2888: Bird at (28, 31) facing LEFT. Interacted from (29, 31) (Behind). Result: Bird flew to (22, 31), now faces RIGHT.
  - T2890: Bird at (22, 31) facing RIGHT. Player at (27, 31).

## Tile Mechanics
- **FLOOR**: Passable. Standard movement.
- **WALL**: Impassable.
- **HEADBUTT_TREE**: Impassable (Verified at 28, 24).
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal in the direction of the ledge.

## Plan
1. Startle bird from (23, 31) to move it east.
2. Drive it to an area where I can reliably get behind it.
3. Return to apprentice (7, 28) after catch.

## Key Locations
- **Apprentice**: (7, 28).
- **Charcoal Kiln**: Azalea Town (21, 13).

## Party Status
- **Calcifer (QUILAVA) Lv22**: Lead.
- Team: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.