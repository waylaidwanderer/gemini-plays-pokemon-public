Mansion 1F Navigation Plan:

Current Objective:
Establish the true state of the shutters on 1F empirically. Stop looping at the switch at (18, 25). I will walk to the shutters at (16, 16) and (13, 22) to determine which ones are open.
I need to find a clear path to the 2F stairs at (5, 10) in the West Wing.

Known Switch: 1F (18, 25).
We need to rigorously map the shutter states.

Convention:
STATE 1: (16, 16) CLOSED, (16, 7) CLOSED, (13, 22) OPEN.
STATE 2: (16, 16) OPEN, (16, 7) OPEN, (13, 22) CLOSED.

Current State: STATE 2. (Toggled Turn 44050)

Observation Turn 44061: In State 2, the Dark Grey shutters at x=9 are CLOSED.
Conclusion: The shutters at x=9 are CLOSED in both states. 1F South is a dead end for reaching the West Wing stairs.

New Goal: Explore B1F. Check if the Dark Grey shutter at B1F x=11 is OPEN in State 2.
Route to B1F:
1. Walk South to (12, 22).
2. Walk East to (16, 22) through the open Yellow Shutter at (13, 22)? Wait, State 2 means (13, 22) is CLOSED.
3. Path to B1F in State 2:
   - Walk South to (12, 26).
   - Walk East through OPEN Dark Grey Shutter at (13, 26) to (18, 26).
   - Walk East through OPEN Dark Grey Shutter at x=20 to reach the stairs at (23, 22).
   - Take stairs DOWN to B1F.
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