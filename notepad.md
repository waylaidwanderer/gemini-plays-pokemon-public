Current State: S1=1, S2=1, S3=0 (Testing).
Previous: S1=1, S2=0, S3=0. Toggled S2 ON.

Switch Log (1=ON, 0=OFF):
| S1 | S2 | S3 | G1 (2,6) | G2 (10,6) | G3 (16,6) | Sec.Door | Notes |
|----|----|----|----------|-----------|-----------|----------|-------|
| 1  | 1  | 0  | Closed   | Closed    | OPEN      | Closed   | Verified G3 Open. G1/G2/SecDoor Closed. |
| 1  | 0  | 0  | Closed   | Closed    | OPEN      | Closed   | Verified G3 Open. G1/G2 Closed. |
| 1  | 0  | 1  | Closed   | Closed    | OPEN      | Closed   | Correction: G3 Open, G1 Closed. |
| 0  | 0  | 0  | Closed   | Closed    | Closed    | Closed   | All Closed (Reset). |
| 0  | 1  | 1  | Closed   | OPEN      | OPEN      | Closed   | Verified G2/G3 Open. Wall(11,10) Closed. |
| 0  | 1  | 0  | Closed   | Closed    | Closed    | Closed   | Verified G1/G2/SecDoor Closed. |
| 0  | 0  | 1  | Closed   | ?         | OPEN      | ?        | Verified G1 Closed. |
| 1  | 1  | 1  | Closed   | Closed    | OPEN      | Closed   | G3 Open. Wall(11,10) Closed. |

Reflection (Turn 49127):
- Progress: Systematically testing switches. Currently testing 1-1-0 (S1=ON, S2=ON, S3=OFF).
- Conflict: Summary says 0-1-1 opened Gate 1, but my Table says it didn't. Need to resolve this if 1-1-0 fails.
- Goal: Find the state that opens Gate 1 (to access Silver/Key) or opens the Wall at (11,10).
- Hygiene: Cleaning up old notes. Markers are helpful.
- Plan: Verify 1-1-0 fully (G1, G2, G3). Then considering 0-1-1 retry or S1 OFF strategies.

Action: Moving to Gate 1 (2,6).
Path: Left along Row 5 to (2,5), then Down to enter Gate 1.
Hypothesis: Summary suggests 1-1-0 opens Gate 1. Verifying.
Goal: Reach area behind Gate 1 (Silver/Key location).