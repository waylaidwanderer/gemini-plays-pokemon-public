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

## Plan
1. Approach Farfetch'd at (22, 31) from South at (22, 32) (Behind).
2. Observe if it turns or if it can be caught.
3. If it flies, track next position.

## Key Locations
- **Apprentice**: (7, 28).
- **Charcoal Kiln**: Azalea Town (21, 13).

## Party Status
- **Calcifer (QUILAVA) Lv22**: Lead.
- **Team**: ONIX, GEODUDE, PIDGEY, TOGEPI, EKANS.