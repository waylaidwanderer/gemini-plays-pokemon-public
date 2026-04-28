Mansion 1F Navigation Plan:

Current Objective:
Establish the true state of the shutters on 1F empirically. Stop looping at the switch at (18, 25). I will walk to the shutters at (16, 16) and (13, 22) to determine which ones are open.
I need to find a clear path to the 2F stairs at (5, 10) in the West Wing.

Known Switch: 1F (18, 25).
We need to rigorously map the shutter states.

Convention:
STATE 1: (16, 16) CLOSED, (16, 7) CLOSED, (13, 22) OPEN.
STATE 2: (16, 16) OPEN, (16, 7) OPEN, (13, 22) CLOSED.

Current State: STATE 1. (Observed Turn 44012)
Goal: Reach 2F stairs at (5, 10).

Observation: In State 1, the Dark Grey shutters at x=9 are CLOSED.
This confirms we MUST use State 2 to reach the stairs.

Route:
1. Walk to switch at (18, 25) and toggle to STATE 2.
   - Down to (12, 22), Right to (14, 22), Down to (14, 26), Right to (18, 26), press A.
2. Walk to West Wing crossing at (16, 7).
   - Left to (16, 26), Up to (16, 14) through open yellow shutter at (16, 16).
   - Left to (10, 14).
3. Enter West Wing and take stairs.
   - Left to (5, 14) through (hopefully) open Dark Grey shutters at x=9.
   - Up to (5, 10)!
OBSERVATION Turn 43987:
Current State (after toggle on 43977):
- (13, 22)/(13, 23): Yellow Shutter is CLOSED.
- (13, 24): Dark Grey Shutter is OPEN (displays as Shutter_Base_Solid).
- (14, 16)/(15, 16): Looks like a CLOSED Dark Grey Shutter (Horizontal).
- (16, 16)/(17, 16): Floor is pink. Shutter is OPEN.
Wait, so the Yellow Shutter at (16, 16) is OPEN. The Yellow Shutter at (13, 22) is CLOSED.
This means YELLOW SHUTTERS CAN BE OUT OF SYNC WITH EACH OTHER!
I need to verify this immediately by toggling the switch again.
OBSERVATION Turn 44006:
In State A, the Dark Grey Shutters at x=9 (y=10 to 16) are ALL CLOSED.
I will now go toggle to State B and verify their state from the East.