# 2F Staircase / Warp Audit Protocol

## Objective
Systematically test candidate tiles in Pokémon Mansion 2F Central Hall to locate the descent to 1F or verify traversability.

## Candidate Matrix
- Tile (5, 10): Occupied on Turns 14437-14465. Flat pink floor; NO warp triggered.
- Tile (6, 10): Open pink floor connecting east.
- Tile (7, 10): Dark background tile with ascending bars graphic. Testing physical collision and warp trigger.
- Tile (5, 11): Flat pink floor, previously traversed.
- Tile (7, 11): Flat pink floor below (7, 10).

## Log
- Turn 14465: Player at (5, 10). Initiating test sequence towards (7, 10). First stepping Right to (6, 10).