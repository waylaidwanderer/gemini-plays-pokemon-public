Mansion 1F Navigation Plan:

Current Objective:
I must test if the Dark Grey Shutters at x=9 are open in STATE 2. I previously hallucinated testing them.

Convention:
STATE 1: (16, 16) CLOSED, (13, 22) OPEN. Dark Grey Shutters CLOSED.
STATE 2: (16, 16) OPEN, (13, 22) CLOSED. Dark Grey Shutters OPEN (Hypothesis).

Current State: STATE 1. (Observed Turn 44034, 16,16 is CLOSED. Confirmed by 13,25 being CLOSED.)
Goal: Reach 2F stairs at (5, 10).

Route:
1. Walk to switch at (18, 25) and toggle to STATE 2.
   - From (12, 25): Up to (12, 22), Right to (16, 22), Down to (16, 26), Right to (18, 26), press A.
2. Navigate to West Wing crossing at y=14:
   - Walk Left to (16, 26), Up to (16, 14) [passes through open Yellow Shutter at 16,16].
3. Cross West to West Wing.
   - Walk Left to (10, 14).
   - Walk Left to (5, 14) through Dark Grey Shutters at x=9 (Testing if OPEN IN STATE 2).
   - Walk Up to 2F stairs at (5, 10)!
- Reflected at Turn 44082. GameState coordinates are often incorrect during battles (e.g. showing 12,26 instead of 18,26). Always wait for the overworld to stabilize before trusting them.
Turn 44083: Huge revelation! 'Obstacle/Shutter_Vertical_Yellow' is actually the OPEN yellow shutter, and is horizontally walkable! Currently Yellow is OPEN, Dark Grey is CLOSED. Heading to switch to toggle it so I can test x=9 Dark Grey shutters.
Turn 44096: I incorrectly assumed (13, 22) was solid because my macros were aborting when I bumped into the statue at the end of the route. (13, 22) and (13, 23) are both valid paths when the Yellow Shutter is open.