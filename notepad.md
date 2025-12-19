# Ilex Forest Strategy: Catching Farfetch'd

## Goal: Catch the runaway Farfetch'd to obtain HM01 (Cut).

## Farfetch'd Mechanics
- **Success Condition**: "You have to get behind it to catch it." (Apprentice hint).
- **Hypothesis**: Interacting from the tile directly opposite the bird's facing direction (behind it) is the key.
- **Flight Logic**: Interacting from the front or side causes the bird to fly ~6 tiles in the direction it is facing.
- **Attempt History**:
  - Attempt 1 (T2867): North (28, 30) -> Bird (28, 31) faced South. (Startled).
  - Attempt 2 (T2878): West (23, 35) -> Bird (24, 35) faced Right. (Startled).
  - Attempt 3 (T2888): East (29, 31) -> Bird (28, 31) faced Left. (Startled).
  - Attempt 4 (T2892): East (23, 31) -> Bird (22, 31) faced Right. (Startled).

## Tile Mechanics
- **FLOOR**: Passable. Standard movement.
- **WALL**: Impassable. Dense trees or map boundaries.
- **HEADBUTT_TREE**: Impassable (Verified at 28, 24).
- **CUT_TREE**: Impassable. Requires HM01 Cut to clear.
- **LEDGE_HOP**: One-way traversal in the direction of the ledge.

## Current Status
- **Bird Position**: (24, 35).
- **Bird Facing**: LEFT (Verified T2896).
- **Target Position**: (25, 35) (Behind).

## Key Locations
- **Apprentice**: (7, 28). Return here after catch.
- **Charcoal Kiln**: Azalea Town (21, 13). Boss gives Cut.

## Party Status
- **Calcifer (QUILAVA) Lv22**: Lead.
- **Team**: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.
- Attempt 5 (T2897): Player at (25, 35), Bird at (24, 35) facing Left. Bird turned Right to face player before interaction. Result: "Kwaa!" (Startled).
- Observation: Bird seems to turn to face the player if approached from behind.
- Strategy: Must find a way to prevent it from turning or drive it to a specific location.