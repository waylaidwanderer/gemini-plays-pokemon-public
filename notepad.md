Action: Moving to Gate 1 (2,6) via Row 5.
Path: Down to (16,5), Left to (2,5), Down to check Gate 1.
Hypothesis: Switch 1 (ON) in state 1-1-0 opens Gate 1.
Observation: Map update at (12,8) confirms S1 does something. Checking if it affected Gate 1.
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

Observation: Gate 1 is Closed.
Correction: Map Marker (16,1) says 'Switch 1 (OFF)'. Notepad said 'S1=1'. This was a mismatch.
Conclusion: Current State is 0-1-0 (S1=0, S2=1, S3=0).
Plan: Go to Switch 1 (16,1) and turn it ON to achieve State 1-1-0.
Hypothesis: 1-1-0 might open Gate 1 or the Wall at (11,10).
Observation: Turning Switch 1 ON changed (12,9) from Wall to Floor.
Action: Toggling Switch 1 (16,1).
Hypothesis: Current state is 0-1-0 (G3 Closed). Toggling S1 will create 1-1-0.
Prediction: 1-1-0 will OPEN Gate 3.
Goal: If Gate 3 opens, return to Director's Room (3_53) to interrogate the Rocket Grunts (I left before doing this).
Markers: Cleaning up conflicting S1 markers.