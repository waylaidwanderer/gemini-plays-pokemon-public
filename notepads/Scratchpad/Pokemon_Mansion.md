Mansion 1F Routing Solution (Final):
1. The Mansion has two global shutter states.
2. State B (Yellow-Open): Yellow Shutters (16,16), (9,6) are OPEN. Dark Grey Shutters (13,22) are CLOSED.
3. State A (Yellow-Closed): Yellow Shutters are CLOSED. Dark Grey Shutters (13,22) are OPEN.
4. The shutter at (9, 14) is ALWAYS a solid wall, it never opens.
5. Route to 2F/3F Stairs at 1F (5, 10):
   - The route must pass through the Yellow Shutter at (9, 6), which means we MUST end up in 'State B'.
   - If starting in State A (current state):
     - Walk from Center (12, 22) East through OPEN (13, 22) to the switch at (18, 25).
     - Toggle the switch to State B.
     - (13, 22) is now closed. Walk North and West through the now OPEN Yellow Shutter at (16, 16) to reach Center (x=12, y=15).
     - Walk North up x=12 to y=6.
     - Walk West through the OPEN Yellow Shutter at (9, 6) to reach the West Wing.
     - Walk North to the stairs at (5, 10).