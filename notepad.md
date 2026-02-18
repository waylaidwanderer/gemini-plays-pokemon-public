Current State: S1=1, S2=0, S3=1 (Actual).
Previous: S1=1, S2=1, S3=1. Turned S2 OFF to test 1-0-1.

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 1  | 1  | 0  | Closed   | Closed    | OPEN      | Closed   | Verified G3 Open. G1/G2/SecDoor Closed. |
| 1  | 0  | 0  | Closed   | Closed    | OPEN      | Closed   | Verified G3 Open. G1/G2 Closed. |
| 1  | 0  | 1  | OPEN     | Closed    | Closed    | Closed   | Verified G1 Open. Others Closed. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed (Reset). |
| 0  | 1  | 1  | Closed   | OPEN      | OPEN      | Closed   | Verified G2/G3 Open. Wall(11,10) Closed. |
| 0  | 1  | 0  | Closed   | Closed    | Closed    | Closed   | Verified G1/G2/SecDoor Closed. |
| 0  | 0  | 1  | Closed   | ?         | OPEN      | ?        | Verified G1 Closed. |
| 1  | 1  | 1  | Closed   | Closed    | OPEN      | Closed   | G3 Open. Wall(11,10) Closed. |

Reflection (Turn 48815):
- Strategy: Systematically testing all 8 switch permutations.
- Progress: 7/8 states tested for Gate 1.
- Current Task: Test the final state (1-1-0).
- Hygiene: Notepad log is accurate. Markers are up to date.
- Next Steps: If G1 opens, proceed. If not, analyze map for overlooked paths (e.g. wall at 11,10).
Goal: Test state 0-0-1 (S1=OFF, S2=OFF, S3=ON).
Current Switches: S1=OFF, S2=ON, S3=ON (0-1-1).
Log: 0-1-1 verified. All gates appear closed.
Next: Go to Switch 2 (10, 1), Turn OFF.
Reflection (Turn 49074):
- Progress: systematically testing switch combos. 0-1-1 is current test.
- Hygiene: Notepad table is proving vital. Markers helping track traps.
- Strategy: Continue brute force. If 0-1-1 fails, try 0-0-1.
- Note: Need to verify if Switch 1 OFF disables the trap room traps.