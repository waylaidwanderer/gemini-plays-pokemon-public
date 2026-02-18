Current State: S1=1, S2=1, S3=0 (Testing).
Previous: S1=1, S2=0, S3=0 (Fixing Interaction).

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 1  | 1  | 0  | OPEN     | Closed    | ?         | ?        | SUCCESS! Gate 1 is Open! |
| 1  | 0  | 0  | Closed   | Closed    | OPEN      | Closed   | Verified G1 Closed. |
| 1  | 0  | 1  | Closed   | ?         | ?         | ?        | Verified G1 Closed. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed (Reset). |
| 0  | 1  | 1  | Closed   | Closed    | OPEN      | Closed   | Verified G1 Closed. |
| 0  | 1  | 0  | Closed   | OPEN      | OPEN      | OPEN     | Verified G1 Closed. |
| 0  | 0  | 1  | Closed   | ?         | OPEN      | ?        | Verified G1 Closed. |
| 1  | 1  | 1  | Closed   | OPEN      | Closed    | OPEN     | G2, Sec. Door Open. (11,10) Closed. |

Reflection (Turn 48815):
- Strategy: Systematically testing all 8 switch permutations.
- Progress: 7/8 states tested for Gate 1.
- Current Task: Test the final state (1-1-0).
- Hygiene: Notepad log is accurate. Markers are up to date.
- Next Steps: If G1 opens, proceed. If not, analyze map for overlooked paths (e.g. wall at 11,10).