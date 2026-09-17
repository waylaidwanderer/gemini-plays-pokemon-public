# Victory Road Master Routing & Active Testing

## Current Verified State [Turn 23733]:
- Player is at 3F (26, 5) facing South. Switch (3, 5) is depressed.
- Empirical Test: (27, 6) [Turn 23729] and (26, 6) [Turn 23734] both confirmed 0 movement delta against solid rock with Switch (3, 5) depressed. Disproved Northeast Alcove Row 6 barrier hypothesis. Row 6 is permanent cave wall.
- Post-Switch Activation Test Protocol (Hypothesis Testing):
  1. Once Switch (3, 5) is depressed, do NOT take any ladders or change floors (ladders reset all switches and boulders).
  2. Backtrack north up Column 2 to (2, 2), east along Row 2 to (6, 2), north up Column 6 to (6, 0).
  3. Traverse east along Row 0/1 Northern Highway directly to Northeast Alcove (cols 26-28).
  4. At (26, 5) and (27, 5), perform physical collision bump tests facing South into (26, 6) and (27, 6) to empirically verify if Row 6 barrier lowered.
  5. If lowered, proceed down Column 25 to Boulder 2 at (24, 10) and Pit Hole at (23, 15). If impassable, document negative collision telemetry before testing other sectors.
- Northeast Alcove on 3F (cols 26-28, rows 3-5) is completely enclosed: Row 6 is solid rock wall (tile 27, 6 tested 0 delta Turn 23625), Column 29 is solid rock wall across all rows 0-7. Ground access to Ladder (26, 8) from Northeast Alcove is confirmed impossible.
- Tile (24, 7) on 3F tested solid rock wall (0 delta Turn 23615).
- Boulder 3 Visual & Spatial Audit [Turn 23661]: Player at (13, 11) directly facing Boulder 3 at (13, 12). Visual confirmation proves: (12, 12) is rock wall, (14..18, 12) is rock wall, (12, 13) is rock wall, (12..13, 14..15) is solid rock wall. Pushing Boulder 3 south to (13, 13) traps it against (13, 14) wall; without diagonal movement, player cannot step into (14, 13). Boulder 3 is definitively a dead-end trap from the north. Southern runway (rows 13-15) must be accessed from the eastern sector.