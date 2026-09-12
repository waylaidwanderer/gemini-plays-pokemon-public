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
- Visual Audit: Tile (7, 10) displays dark graphic with vertical bars; physically tested from west (traversable) and south (solid bump).
- Next Test: Step Up from (7, 11) into (7, 10).
- Turn 14477: Stepped Up from (7, 11) toward (7, 10) - collided/bumped. Tile (7, 10) is solid from the south and is not an entry warp.
- Turn 14481: Facing North at (7, 11). Testing 'A' interaction on (7, 10).
- Turn 14483-14484: Pressed 'A' facing (7, 10). No dialogue or interaction triggered.
- Conclusion: Tile (7, 10) is a solid, non-interactive fixture (bookcase/furniture). Candidate audit of Central Hall (5-9, 8-15) complete: NO staircase to 1F exists in this room. Exiting to explore southern and western sections.
- Turn 14504-14505: Stepped Left from (6, 10) into (5, 10). Triggered map transition to Pokémon Mansion 1F! Player arrived at 1F (5, 10) on red carpet. 2F to 1F staircase at (5, 10) empirically verified! Audit successfully complete.