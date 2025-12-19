# Ilex Forest Strategy: Catching Farfetch'd

## Goal: Catch the runaway Farfetch'd to obtain HM01 (Cut).

## Farfetch'd Flight Logic (Hypothesis)
- **Mechanic**: The bird flies away if approached from the front or side. To catch it, interact from directly behind its facing direction.
- **Flight Behavior**: It flies ~4-5 tiles in the direction it is facing when startled.
- **Catch Condition**: Interacting from the tile directly behind it (opposite its facing direction).
- **Testing Log**:
  - Attempt 1 (T2867): Interacted from North (28, 30) while bird at (28, 31) faced South. Result: Flew South. (Hypothesis: Maybe "behind" means something else, or I misidentified facing).
  - Attempt 2 (T2878): Interacted from West (23, 35) while bird at (24, 35) faced Right. Result: Flew East. (Confirmed: Side interaction causes flight).

## Current Status
- Bird at (28, 31), Facing: DOWN.
- Target Position: (28, 30) (Behind).

## Tile Mechanics
- FLOOR: Traversable. Standard movement.
- WALL: Impassable. Boundaries or dense trees.
- HEADBUTT_TREE: Impassable.
- CUT_TREE: Impassable. Requires HM01 Cut.
- LEDGE_HOP: One-way traversal (Down/Left/Right).

## Post-Catch Plan
1. Return to the apprentice (7, 28).
2. Go to Charcoal Kiln in Azalea Town (21, 13) to get HM01 Cut.
3. Teach Cut and clear the tree to Route 34.

## Key Locations
- Kurt's House: Azalea (9, 5). Kurt (3, 2) makes balls.
- Charcoal Kiln: Azalea (21, 13). Boss gives Cut.

## Party Status
- Calcifer (QUILAVA) Lv22: Lead.
- Team: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.