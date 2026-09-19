# Post-Game: Cerulean Cave & Mewtwo Investigation

## Verified Dungeon Architecture & Empirical Facts
1. 2F Physical Collision Proofs:
   - Row 8: Physically bump-tested every column from 2 to 12. Solid rock boulders confirmed at (3, 8) [Turn 26973], (4, 8) [Turn 27414], (5, 8) [Turn 27506], (6, 8) [Turn 27585], (7, 8) [Turn 27587], (8, 8) [Turn 27589], (9, 8) [Turn 27415], (10, 8) [Turn 27591], (11, 8) [Turn 27508], and (12, 8) [Turn 27595].
   - Sector A: Physical bump tests confirmed (2, 1..3) are solid rock walls and (3..8, 4) are solid boulders [Turn 27545: (3, 4) solid].
   - Boulder (8, 5): Solid rock boulder separating Row 5 West from Row 5 East [Turn 27083].
   - Conclusion: 2F Northwest Enclave (Cols 0..7, Rows 2..7) containing Ladder (1, 3) cannot be entered via Sector A, Row 5 East, or Row 8.
2. 1F Physical Collision Proofs:
   - Western Terrace: Bump test confirmed (4, 7) is solid rock boulder [Turn 27580]. (3, 7), (5..7, 7) are solid boulders. Row 7 (Cols 0..2) contains a south-facing jump ledge dropping to Row 8.
   - Northwest Corridor: Visually confirmed Ladder at (0, 6) [Turn 27580]. Corridor is exit-only on 1F, terminating at the Row 7 jump ledge.
   - Waterway Boundary: Bump test confirmed (7, 6) is solid rock wall from (8, 6) [Turn 27568].
   - Eastern Shoreline: Bump test confirmed (27, 12) is elevated cliff from water (27, 11) [Turn 27615]. Row 12 is continuous cliff across Cols 23..30.
   - Eastern Corridor (Cols 27..28, Rows 12..16): Decorative basin enclosed by cliffs, Pillar 26, and cave walls. Contains zero ladders.
3. Cerulean Cave Multi-Floor Ladder Topology:
   - 1F (23, 7) <-> 2F (22, 6) [CONFIRMED 2-WAY: Entrance Terrace to Central Network]
   - 1F (18, 9) <-> 2F (19, 7) [CONFIRMED 2-WAY: Central-Western Terrace to Secluded Pocket]
   - 1F (27, 1) <-> 2F (29, 1) [CONFIRMED 2-WAY: Northern Elevated Terrace to Sector B]
   - 1F (7, 1) <-> 2F (9, 1) [CONFIRMED 2-WAY: Northern Terrace to Sector A]
   - 1F (3, 11) <-> 2F (3, 11) [CONFIRMED 2-WAY: Western Terrace to Western Network]
   - 1F (0, 6) <-> 2F (1, 3) [HYPOTHESIZED 2-WAY: 1F exit corridor to 2F NW Enclave]

## Active Route & Next Steps
- Current Location: Cerulean Cave 1F at (27, 11) in lake water.
- Immediate Task: Disembark from lake via Staircase (25, 9) onto Entrance Terrace.
- Working Hypothesis: The Lower Southwest Network on 2F (accessed via Ladder 3, 11) connects to the open floor chain at (1..2, 13), (1, 12), (0, 9..11), and (1, 8..9) leading to Ladder (1, 3).
- Active Plan:
  1. Surf west from (27, 11) to (25, 10), ascend Staircase (25, 9) to (25, 8).
  2. Take Ladder (23, 7) up to 2F Central Network to verify if any unknown connector exists.
