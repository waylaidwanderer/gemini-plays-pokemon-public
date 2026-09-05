# Victory Road 3F - Layout & Topology

## Ladders & Exits
- NW Ladder (from 2F NW (1, 1)): Located at (2, 0) in isolated NW room
- Ladder A (from 2F (23, 7)): Arrival tile at (23, 7) on upper plateau from 2F (23, 7). (Note: Descent from 3F (23, 7) is not bidirectional; use Ladder NE at (27, 7) or Ladder B at (25, 14) to descend).
- Ladder NE (to 2F): Located at (27, 7) (accessed from Upper Dark Plateau via row 6). Note: Row 10 is a solid wall blocking northward traversal along column 29 from (29, 11).
- Ladder B (to 2F SE): Located at (25, 14) in SE Lower Purple Room
- The Pit / Hole: Located at (23, 14).

## Physical Features & Topography
- Upper Dark Plateau (rows 0-11, cols 19-28): Contains Ladder A (23, 7), Ladder NE (27, 7), Boulder 1 at (22, 3). Separated from lower floor by impassable south-facing cliff wall between row 11 and 12.
- Northern Highway (Rows 0-1): Continuous open floor spanning across columns 6 through 25.
- Central Bridge (Column 6): Spans rows 0-6. Empirically verified on Turn 28794 that Central Bridge (cols 6-7, rows 0-6) dead-ends at row 6 against south-facing cliff walls (row 7) and impassable solid rock wall along column 8 (rows 2-9). Pushing Boulder 1 (22, 3) down Central Bridge traps it; the bridge does NOT connect to the lower purple floor.
- Central Corridor (Columns 9-10): Vertical corridor spanning rows 2-10 (terminates at (10, 10)). Row 10 connects west to (8, 10) (adjacent to Switch Plate at (3, 5)).
- Purple Chamber (rows 2-4, cols 14-18): Connected west to central corridor via row 2 (cols 9-18). Separated from Northern Highway by solid north wall at row 2, and blocked to the south by rock walls and Shutter at (17, 5).
- SE Lower Purple Floor (rows 12-14, cols 10-26): Accessible via 2F Ladder B at (25, 14). Contains Boulder 3 at (13, 12), the Pit at (23, 14), and Ladder B at (25, 14).

## Discovered Points of Interest & Topology (Verified Turn 28862)
- [ ] Item Ball at (11, 0) in northern corridor of western sector.
- Cooltrainer NPC at (19, 8): "You earned the right to be on VICTORY ROAD!".
- Shutter at (17, 5): Horizontal purple bars blocking passage south from row 4 purple room to row 6.
- Column 10 Connectivity: Row 1 above column 10 is separated from lower rows by a south-facing cliff wall; cannot walk south between row 1 and row 2 at column 10.
- Boulder 1 at (22, 3): Positioned on upper dark plateau.

## Northern Highway Branch Corridors & Scout Checklist
- Column 17: Open 1-tile gap at row 4 connecting rows 1-3 to rows 6-11 (Upper Dark Plateau & Ladder A arrival).
- Columns 9-10: North wall at row 2 separates row 1 Northern Highway from Purple Chamber.
- Columns 6-7 (Central Bridge): Spans rows 0-6; dead-ends at row 6 against south cliff wall and column 8 rock wall.
- Columns 0-5 (Far West Corridor): Under active scouting.

## Verified Master 3F Boulder 1 Solution to Switch (3, 5)
- Initial Position: Boulder 1 @ (22, 3).
- Master Push Protocol:
  1. Stand at (23, 3) facing West -> Push Left 2 times: Boulder to (20, 3) [Player at (21, 3)].
  2. Reposition around via (21, 4) -> (20, 4) facing North.
  3. Stand at (20, 4) facing North -> Push Up 2 times: Boulder to (20, 1) [Player at (20, 2)]. (CRITICAL: Stop at Row 1; do NOT push into Row 0!).
  4. Reposition around to (21, 1) via (20, 2) -> (21, 2) -> (21, 1) facing West.
  5. Stand at (21, 1) facing West -> Push Left 15 times along Row 1 to (6, 1) [Boulder at (6, 1), Player at (7, 1)].
  6. Reposition around to (6, 0) via (7, 1) -> (7, 0) -> (6, 0) facing South.
  7. Stand at (6, 0) facing South -> Push Down 1 time: Boulder to (6, 2) [Player at (6, 1)].
  8. Reposition around to (7, 2) via (6, 1) -> (7, 1) -> (7, 2) facing West.
  9. Stand at (7, 2) facing West -> Push Left 4 times across Row 2 to (2, 2) [Boulder at (2, 2), Player at (3, 2)].
  10. Reposition around to (2, 1) via (3, 2) -> (3, 1) -> (2, 1) facing South.
  11. Stand at (2, 1) facing South -> Push Down 3 times down Column 2 to (2, 5) [Boulder at (2, 5), Player at (2, 4)].
  12. Reposition around to (1, 5) via (2, 4) -> (1, 4) -> (1, 5) facing East.
  13. Stand at (1, 5) facing East -> Push Right 1 time: Boulder moves onto Switch (3, 5) [Player at (2, 5)]!
- Verified Outcome: Switch at (3, 5) activated! Shutter at (17, 5) permanently opened.
