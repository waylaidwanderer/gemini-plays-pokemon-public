Location: Warehouse (3_54).
Objective: Test State 1-0-0 (Sw1 ON, Sw2 OFF, Sw3 OFF).
Switch States & Effects Matrix:
[Sw1][Sw2][Sw3] -> [G1(2,6)][G2(10,6)][G3(16,6)][G4(2,10)][Trap(12,8)]
[ 1 ][ 1 ][ 1 ] -> [Open ][Closed][Open ][Closed][Active]
[ 1 ][ 1 ][ 0 ] -> [Open ][  ?   ][ ?  ][Closed][  ?   ]
[ 1 ][ 0 ][ 1 ] -> [Closed][Closed][ ?  ][ ?   ][Active]
Key: 1=ON, 0=OFF.
Hypothesis:
- Maybe Sw2 & Sw3 OFF is the key (State 1-0-0)?
Plan:
1. Turn Sw3 OFF.
2. Use tool 'check_gate_states' to check all gates.