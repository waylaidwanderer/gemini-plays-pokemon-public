# Victory Road 3F - Layout & Topology

## Ladders & Exits
- NW Ladder (from 2F NW (1, 1)): Located at (2, 0) in isolated NW room
- Ladder A (from 2F (23, 7)): Arrival tile at (23, 7) on upper plateau from 2F (23, 7). (Note: Descent from 3F (23, 7) is not bidirectional; use Ladder NE at (27, 7) or Ladder B at (25, 14) to descend).
- Ladder NE (to 2F): Located at (27, 7) (accessed from Upper Dark Plateau via row 6). Note: Row 10 is a solid wall blocking northward traversal along column 29 from (29, 11).
- Ladder B (to 2F SE): Located at (25, 14) in SE Lower Purple Room
- The Pit / Hole: Located at (23, 14) in SE Lower Purple Room.

## Physical Features & Topography
- Column 14 Barrier (Empirically Verified Turn 29710): Column 14 (x=14, y=0..1) contains a solid continuous rock wall blocking east-west traversal across the northern sector.
- NW Room Access Protocol: The NW Room (Switch (3, 5) and NW Boulder (5, 5)) must be accessed exclusively via 2F NW Ladder at (1, 1) <-> 3F NW Ladder at (2, 0).
- Upper Dark Plateau (rows 0-11, cols 15-28): Contains Ladder A (23, 7), Ladder NE (27, 7), and connects via southern corridor (row 11) to column 28/29.
- Central Bridge (Column 6): Spans rows 0-6. Empirically verified on Turn 28794 that Central Bridge (cols 6-7, rows 0-6) dead-ends at row 6 against south-facing cliff walls (row 7) and impassable solid rock wall along column 8 (rows 2-9). Pushing Boulder 1 (22, 3) down Central Bridge traps it; the bridge does NOT connect to the lower purple floor.
- Central Corridor (Columns 9-10): Vertical corridor spanning rows 2-10 (terminates at (10, 10)). Row 10 connects west to (8, 10) (adjacent to Switch Plate at (3, 5)).
- Purple Chamber (rows 2-4, cols 14-18): Connected west to central corridor via row 2 (cols 9-18). Separated from Northern Highway by solid north wall at row 2, and blocked to the south by rock walls and Shutter at (17, 5).
- SE Lower Purple Floor (rows 12-14, cols 10-26): Accessible via 2F Ladder B at (25, 14). Contains Boulder 3 at (13, 12), the Pit at (23, 14), and Ladder B at (25, 14).

## Discovered Points of Interest & Topology
- [ ] Item Ball at (11, 0) in northern corridor of western sector.
- Cooltrainer NPC at (19, 8): "You earned the right to be on VICTORY ROAD!".
- Shutter at (17, 5): Horizontal purple bars blocking passage south from row 4 purple room to row 6.

## Northern Highway Branch Corridors & Scout Checklist
- Column 17: Open 1-tile gap at row 4 connecting rows 1-3 to rows 6-11 (Upper Dark Plateau & Ladder A arrival).
- Columns 9-10: North wall at row 2 separates row 1 Northern Highway from Purple Chamber.
- Columns 6-7 (Central Bridge): Spans rows 0-6; dead-ends at row 6 against south cliff wall and column 8 rock wall.
- Columns 0-5 (Far West Room): Contains NW Boulder at (5, 5) and Switch Plate at (3, 5).

## Verified Master 3F NW Boulder Solution to Switch (3, 5) (VERIFIED Turn 29241)
- Initial Position: NW Boulder @ (5, 5). Switch @ (3, 5).
- Master Push Protocol:
  1. Stand at (5, 4) facing South -> Push Down 1 time: Boulder to (5, 6).
  2. Reposition around via (5, 4) -> (6, 6) facing West.
  3. Stand at (6, 6) facing West -> Push Left 2 times: Boulder to (3, 6).
  4. Reposition around via (4, 6) -> (4, 7) -> (3, 7) facing North.
  5. Stand at (3, 7) facing North -> Push Up 1 time: Boulder moves onto Switch (3, 5) [Player at (3, 6)]!
- Verified Outcome: Switch at (3, 5) activated! Shutter at (17, 5) opened.

## 3F Pit Area & Boulder Observations
- Boulder observed at (24, 10).
- Column 13 / Row 11: Pushing boulder at (13, 12) down to (13, 13) dead-ends against rock obstacle at (13, 14).
## 3F Default Boulder & Switch Layout
- Note: Warping out via Dig / Escape Rope resets all dungeon entities to default spawn positions.
- Boulder 1 default position: (22, 3) on Upper Dark Plateau.
- NW Boulder default position: (5, 5) near NW Switch at (3, 5).
