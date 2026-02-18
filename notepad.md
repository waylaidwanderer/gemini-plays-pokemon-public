Current State: S1=1, S2=1, S3=0 (Actual).
Previous: S1=1, S2=1, S3=1. Note: S2 was never OFF.

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 1  | 1  | 0  | OPEN     | Closed    | Closed    | Closed   | Verified G1 Open, G2/Sec Door Closed. |
| 1  | 0  | 0  | Closed   | Closed    | OPEN      | Closed   | Verified G3 Open. G1/G2 Closed. |
| 1  | 0  | 1  | OPEN     | Closed    | Closed    | Closed   | Verified G1 Open. Others Closed. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed (Reset). |
| 0  | 1  | 1  | Closed   | Closed    | OPEN      | Closed   | Verified G1 Closed. |
| 0  | 1  | 0  | Closed   | OPEN      | OPEN      | OPEN     | Verified G1 Closed. |
| 0  | 0  | 1  | Closed   | ?         | OPEN      | ?        | Verified G1 Closed. |
| 1  | 1  | 1  | OPEN     | Closed    | Closed    | OPEN     | G1 Open. Sec Door Open. Wall(11,10) Closed. |

Reflection (Turn 48815):
- Strategy: Systematically testing all 8 switch permutations.
- Progress: 7/8 states tested for Gate 1.
- Current Task: Test the final state (1-1-0).
- Hygiene: Notepad log is accurate. Markers are up to date.
- Next Steps: If G1 opens, proceed. If not, analyze map for overlooked paths (e.g. wall at 11,10).