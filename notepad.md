Current State: S1=0, S2=1, S3=1 (Actual).
Previous: S1=0, S2=1, S3=0. Turned S3 ON to test 0-1-1.

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 1  | 1  | 0  | OPEN     | Closed    | Closed    | Closed   | Verified G1 Open, G2/Sec Door Closed. |
| 1  | 0  | 0  | Closed   | Closed    | OPEN      | Closed   | Verified G3 Open. G1/G2 Closed. |
| 1  | 0  | 1  | OPEN     | Closed    | Closed    | Closed   | Verified G1 Open. Others Closed. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed (Reset). |
| 0  | 1  | 1  | Closed   | OPEN      | OPEN      | Closed   | Verified G2/G3 Open. Wall(11,10) Closed. |
| 0  | 1  | 0  | Closed   | OPEN      | OPEN      | OPEN     | Verified G2/G3/SecDoor Open. Wall(11,10) Closed. |
| 0  | 0  | 1  | Closed   | ?         | OPEN      | ?        | Verified G1 Closed. |
| 1  | 1  | 1  | OPEN     | Closed    | Closed    | OPEN     | G1 Open. Sec Door Open. Wall(11,10) Closed. |

Reflection (Turn 48815):
- Strategy: Systematically testing all 8 switch permutations.
- Progress: 7/8 states tested for Gate 1.
- Current Task: Test the final state (1-1-0).
- Hygiene: Notepad log is accurate. Markers are up to date.
- Next Steps: If G1 opens, proceed. If not, analyze map for overlooked paths (e.g. wall at 11,10).
Arrived in Map 3_54 (Warehouse).
Current location: (16, 2).
Goal: Test state 1-1-0 (S1=ON, S2=ON, S3=OFF).
Current Switches: S1=ON, S2=ON, S3=ON.
Step 1: Complete. Switch 1 is ON.
Step 2: Toggle Switch 3 (2, 1) to OFF.
Log: Verified 0-1-0 opens Secret Door. Testing 1-1-0 next.