# Post-Game: Cerulean Cave & Mewtwo Master Strategy

## Definitive Dungeon Architecture & Verified Facts
1. 2F Layout & Boundary Audits:
   - Row 8: 100% physically bump-tested solid boulders from Col 2 to Col 12: (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8). Zero passage between Row 9 and Row 7.
   - Sector A: Row 4 (Cols 2..8) is 100% solid boulders [tested (3, 4) Turn 27545]. Column 2 is solid rock. Boulder (8, 5) separates Row 5 West from East.
   - Central Network: 100% explored. Loops between Ladder (22, 6), Sector B (Ladder 29, 1), and Sector A (Ladder 9, 1). Zero descent to B1F.
2. 1F Layout & Boundary Audits:
   - Western Terrace: Bump-test confirmed (4, 7) is solid boulder [Turn 27580]. Row 7 jump ledge (Cols 0..2) is south-facing exit only.
   - Eastern Corridor (Cols 27..28, Rows 12..16): Decorative basin enclosed by Row 12 cliff (tested from water Turn 27615), Pillar 26, and cave walls. Zero ladders.
   - Waterways: 100% surveyed. Boundary (7, 6) is solid rock wall [Turn 27568].
3. Ladder Pairings (6 Pairs):
   - 1F (23, 7) <-> 2F (22, 6) [2-way confirmed]
   - 1F (18, 9) <-> 2F (19, 7) [2-way confirmed]
   - 1F (27, 1) <-> 2F (29, 1) [2-way confirmed]
   - 1F (7, 1) <-> 2F (9, 1) [2-way confirmed]
   - 1F (3, 11) <-> 2F (3, 11) [2-way confirmed]
   - Unverified Candidate: 1F (0, 6) and 2F (1, 3) [Neither stepped on; correlation is a working hypothesis]

## Active Breakthrough Strategy & Routing Protocol
- Empirical Finding: 2F comprises isolated subgraphs:
  - Sector A (9, 1): 100% enclosed by Row 0 ceiling, Row 4 boulders, and (8, 5) boulder.
  - Southwest Sector (3, 11): 100% enclosed by solid boulders on west ((1, 10..11), (4, 13), (0..1, 14), (2, 15), (3..5, 16)).
  - Central/Eastern Sector (22, 6 / 29, 1): Loops between Column 29, (27, 6..7), and (25, 7..10).
- Working Hypothesis: The true descent to B1F lies in the segregated 1F Northwest Corridor (0, 6) which connects to 2F Ladder (1, 3).
- Active Protocol:
  1. On 2F at (27, 6): Move through (27, 7) -> (25, 7) to inspect whether (24..27, 4) or any passage connects westward into the northern perimeter.
  2. If 2F eastern transit is fully confirmed closed, immediately pivot to 1F ground-level waterways to test the western water boundaries along Row 7/8 for an unverified access point into the Northwest Corridor.
