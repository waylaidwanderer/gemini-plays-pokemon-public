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
- Turn 14471: Player stepped Down to (7, 11). Confirmed (7, 11) is flat floor.
- Visual Audit: Tile (7, 10) clearly displays a staircase graphic with steps ascending North and banisters on left/right.
- Hypothesis: Staircase at (7, 10) requires entry from the South (stepping Up from 7, 11). Side entry from (6, 10) did not trigger the warp.
- Next Test: Step Up from (7, 11) into (7, 10).
- Turn 14477: Stepped Up from (7, 11) toward (7, 10) - collided/bumped. Tile (7, 10) is solid from the south and is not an entry warp.
- Turn 14481: Facing North at (7, 11). Testing 'A' interaction on (7, 10).