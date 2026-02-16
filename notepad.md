Location: Warehouse (3_54).
Objective: Test State 1-0-1 (Sw1 ON, Sw3 ON, Sw2 OFF).
Switch States & Effects Matrix:
[Sw1][Sw2][Sw3] -> [G1(2,6)][G2(10,6)][G3(16,6)][G4(2,10)][Trap(12,8)]
[ 1 ][ 1 ][ 1 ] -> [Open ][Closed][Open ][Closed][Active]
[ 1 ][ 1 ][ 0 ] -> [Open ][  ?   ][ ?  ][Closed][  ?   ]
Key: 1=ON, 0=OFF.
Hypothesis:
- Sw2 might need to be OFF for the middle path?
Plan:
1. Turn Sw3 ON (State 1-1-1).
2. Go to Sw2 (10, 1) and turn OFF.
3. Check Gate 2 (10, 6).