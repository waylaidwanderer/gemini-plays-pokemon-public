# Post-Game Mewtwo Quest Log & Active Routing
- Current Status: Standing on foot at (3, 8) on Map 0_227 (B1F) on Turn 148215.

## Active Backtracking Log (Turns 147920 - 148215)
- Turn 147920: Captured legendary Pokémon Mewtwo (PSYGEM, Level 70) at (27, 13) using Master Ball and transferred it to Box 2.
- Turn 147936: Boarded Surf to navigate water canals, subsequently exploring overworld bypasses and on-foot corridors.
- Turn 148047: Fled successfully from wild Marowak battle at (19, 8) in the overworld facing Up.
- Turn 148048: Walked Down 3 steps to reach (19, 11) on foot on Turn 148061.
- Turn 148071: Boarded Surf on GEMMY at (19, 12), swam Down to (19, 16), Left to (14, 16), and Up through water canal to dismount at (13, 13) on foot on Turn 148077.
- Turn 148105: Boarded Surf at (13, 14), swam east/south to (15, 16) and (19, 16), and swam Up to dismount at (19, 11) on foot on Turn 148115.
- Turn 148115: Walked Up 3 steps to (19, 8), visually verifying that Row 5 at Column 19 is blocked by solid rock wall of TYPE_2889.
- Turn 148120: Walked Down 3 steps to return to (19, 11).
- Turn 148125: Boarded Surf at (19, 12), swam along southern canal, and dismounted at (13, 13) on foot on Turn 148134.
- Turn 148135: Walked Up 5 steps along Column 13 to (13, 8), fled wild Marowak, and stood at (13, 8) facing Up on Turn 148137.
- Turn 148139: Walked Left 4 steps along Row 8 to stand at (9, 8) on foot on Turn 148141.
- Turn 148171: Walked Down stairs at (9, 13) to (9, 14), Left along Row 14, Down Column 7, and Left along Row 17 to reach (4, 17) on foot.
- Turn 148185: Walked Left to (2, 16), intercepted by wild Marowak, fled successfully, returning to overworld at (2, 16).
- Turn 148189: Walked Up Column 2 to (2, 12) on foot.
- Turn 148190: Attempted to walk Up to (2, 11) and bumped against solid rock wall of TYPE_2889, verifying Row 11 blockage.
- Turn 148192: Pressed Left to test (1, 12), intercepted by wild Raichu, fled successfully.
- Turn 148194: Walked Left 2 steps along Row 12 to (0, 12) on foot.
- Turn 148194: Walked Up 2 steps along Column 0 to (0, 10). Intercepted by wild Electrode, fled successfully.
- Turn 148199: Walked Right 3 steps to (3, 9) and Up 1 step to (3, 8) on foot. Standing at (3, 8).

## Lower Level On-Foot Bypass Path & Verification Rigor
- **Verified Segments (physically traversed on foot on this play session)**:
  - Column 13 from Y=13 up to Y=8 (completely unblocked ground floor).
  - Row 8 from Column 13 left to Column 9 (completely unblocked ground floor).
  - Column 2 from Y=16 up to Y=12 (completely unblocked ground floor).
  - Row 12 from Column 2 left to Column 0 (completely unblocked ground floor).
  - Column 0 from Y=12 up to Y=10 (completely unblocked ground floor).
  - Row 10 from Column 0 right to Column 1 (completely unblocked ground floor).
  - Row 9 from Column 1 right to Column 3 (completely unblocked ground floor).
  - Row 8 from Column 3 right to Column 6 (completely unblocked ground floor).
- **Theoretical Segments (visually scanned / computed but currently untraversed)**:
  - Column 9 from Row 8 down to Row 14 via the (9, 13) stairs (visually open and expected unblocked).
  - Row 14 from Column 9 left to Column 7 (visually open and expected unblocked).
  - Column 7 from Row 14 down to Row 15 (visually open and expected unblocked).
  - Row 15 from Column 7 left to Column 6 (visually open and expected unblocked).
  - Column 6 from Row 15 down to Row 17 (visually open and expected unblocked).
  - Row 17 from Column 6 left to Column 3 (visually open and expected unblocked).
  - Column 3 from Row 17 up to the stairs at (3, 6) (visually open and expected unblocked).
  - Row 7 from Column 6 to Column 7 (visually open and expected unblocked).
  - Column 7 from Row 7 up to Row 5 (visually open and expected unblocked).
  - Row 5 from Column 7 to Column 3 (visually open and expected unblocked).

## B1F (Map 0_227) Verified Constraints
- (3, 13) Blockage (Verified Turn 148169): Solid rock wall of TYPE_2889 on foot.
- (2, 11) Blockage (Verified Turn 148190): Solid rock wall of TYPE_2889 on foot.
- (5, 9) Blockage (Verified Turn 148198): Solid rock wall of TYPE_2889 on foot.
- Row 7 on-foot barrier: Row 7 consists of solid rock walls (TYPE_2889) from Column 0 to Column 5, completely isolating Row 6 from the south on foot on the west side.
- Row 5 on-foot barrier: Row 5 consists of solid rock walls (TYPE_2889) at (4, 5) and (5, 5), completely blocking vertical or horizontal crossover along Row 5 between the east and west halves.
- Conclusion: To backtrack from the lower ground level (Rows 8-17) to the stairs at (3, 6), we must walk through Koga's lower level bypass back to Column 9, climb to the upper level (Row 2) via the (13, 3) or (19, 3) stairs, walk Left along Row 2 to (3, 2), and walk Down to (3, 6).

## Active Backtracking Strategy (The Upper Bypass)
- **Goal**: Reach (13, 4) on foot via the lower-level on-foot bypass.
- **Route to (13, 4)**:
  1. From (3, 8), walk Right along Row 8 to (6, 8) and Up to (6, 7).
  2. Walk Right to (7, 7), Up to (7, 6), and Up to (7, 5).
  3. Walk Right to (10, 5) and continue Right along Row 5 to (13, 5).
  4. Walk Up Column 13 through (13, 4) and take the (13, 3) stairs Up to Row 2.
  5. Walk Left along Row 2 to (3, 2).
  6. Walk Down Column 3 through (3, 5) to reach the (3, 6) stairs.
- Let's execute this step-by-step to safely exit Cerulean Cave!