Mansion 1F Routing Analysis:
1. The Mansion has global shutter states toggled by statues.
2. State B (Yellow-Open): Yellow Shutters (16,16), (9,6) are OPEN. Dark Grey Shutters (13,22), (9,14) are CLOSED.
3. State A (Yellow-Closed): Yellow Shutters are CLOSED. Dark Grey Shutters are OPEN.
4. Important: The shutter at (9, 14) is NEVER open. It is a solid wall.
5. The Center section (x=10 to 15) is fully passable East/West at y=15, connecting to East Wing.
6. To reach 2F Stairs at (5, 10):
   - We must enter the North West Wing via the Yellow Shutter at (9, 6)/(9, 7).
   - This requires State B (Yellow-Open).
   - Route: Set to State B at (18, 25). Walk North via East Wing corridor (x=21) to y=15. Cross West to Center (x=12). Walk North to y=6. Cross West through open Yellow Shutter at (9, 6). Walk to stairs at (5, 10).