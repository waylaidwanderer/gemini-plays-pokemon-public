# Ilex Forest Strategy: Catching Farfetch'd

## Goal: Catch the runaway Farfetch'd to obtain HM01 (Cut).

## Farfetch'd Chase Mechanics
- **Success Condition**: "You have to get behind it to catch it." (Apprentice hint).
- **Flight Logic (Hypothesis)**: The bird flies away along the path if startled from the front or side. If approached from behind, it may turn to face the player unless trapped.
- **Flight Behavior**: Moves along the defined forest paths to the next "hiding spot" when startled.
- **Interaction History**:
  - Attempt 1 (T2867): Interacted from North (28, 30) while bird at (28, 31) faced South. Bird flew South.
  - Attempt 2 (T2878): Interacted from West (23, 35) while bird at (24, 35) faced Right. Bird flew East.
  - Attempt 3 (T2888): Interacted from East (29, 31) while bird at (28, 31) faced Left. Bird flew West to (22, 31).
  - Attempt 4 (T2892): Interacted from East (23, 31) while bird at (22, 31) faced Right. Bird flew to (24, 35).
  - Attempt 5 (T2897): Interacted from East (25, 35) while bird at (24, 35) faced Left. Bird turned Right to face player before flight.

## Tile Mechanics
- **FLOOR**: Passable. Standard terrain.
- **WALL / DENSE_TREES**: Impassable.
- **HEADBUTT_TREE**: Impassable. Interacting with it might trigger encounters (not tested).
- **CUT_TREE**: Impassable. Requires HM01 Cut.
- **LEDGE_HOP**: One-way traversal in the direction of the ledge.

## Battle Strategy
- **Wild Battles**: Run from low-level encounters (Metapod, Weedle) to conserve HP/PP.
- **Trainer Battles**: Lead with Calcifer (Quilava). Switch to Gneiss (Geodude) for Rock-type coverage if needed.

## Current Status
- Bird Position: (24, 35).
- Bird Facing: DOWN (Verified T2903).
- Target Position: (25, 35) (to drive West).

## Farfetch'd Chase Log
- Attempt 6 (T2901): Player at (23, 31), Bird at (22, 31) faced Left. Result: Bird turned Right, then flew to (24, 35).
- Observation: Bird turns to face player before fleeing if approached from behind? Or maybe I was in its line of sight during the approach?
- Strategy: Drive bird toward north-west area by interacting from the east/south.