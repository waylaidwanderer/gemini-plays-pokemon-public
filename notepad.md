Location: Warehouse (3_54).
Objective: Test State 0-1-0 (Sw1 OFF, Sw2 ON, Sw3 OFF).
Switch States & Effects Matrix:
[Sw1][Sw2][Sw3] -> [G1(2,6)][G2(10,6)][G3(16,6)][G4(2,10)][Trap(12,8)]
[ 1 ][ 1 ][ 1 ] -> [Open ][Closed][Open ][Closed][Active]
[ 1 ][ 1 ][ 0 ] -> [Open ][  ?   ][ ?  ][Closed][  ?   ]
[ 1 ][ 0 ][ 1 ] -> [Closed][Closed][ ?  ][ ?   ][Active]
[ 1 ][ 0 ][ 0 ] -> [Closed][Closed][Closed][Closed][  ?   ]
Key: 1=ON, 0=OFF.
Hypothesis:
- Sw2 ON is required for Gate 1.
- Sw1 OFF might be required for Gate 4 (Inner Left).
Plan:
1. Go to Sw2 (10,1). Turn ON.
2. Go to Sw1 (16,1). Turn OFF.
3. Check Gates.