Location: Warehouse (3_54).
Objective: Solve Switch Puzzle.
Switch States & Effects Matrix:
[Sw1][Sw2][Sw3] -> [G1(2,6)][G2(10,6)][G3(16,6)][G4(2,10)][Trap(12,8)]
[ 1 ][ 1 ][ 1 ] -> [Open ][Closed][Open ][Closed][Active]
[ 1 ][ 1 ][ 0 ] -> [Testing...                                     ]
Key: 1=ON, 0=OFF.
Hypothesis:
- Sw3 might control G4 (Inner Left) or G1.
- Sw2 might control G2 (Middle).
- Sw1 controls G3 (Right) & Trap?
Plan:
1. Test State 1-1-0 (Current). Check G1 & G4.
2. If fails, try State 1-0-0.
3. If fails, try State 0-1-0.