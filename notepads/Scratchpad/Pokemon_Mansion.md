Mansion 1F Routing Solution:
1. The Mansion has two global shutter states.
2. In 'State Yellow-Open', Yellow shutters like (16, 16) are OPEN, and Dark Grey shutters are CLOSED.
3. In 'State DarkGrey-Open', Dark Grey shutters like (9, 14) are OPEN, and Yellow shutters are CLOSED.
4. Route to 2F/3F Stairs at 1F (5, 10):
   - The route must pass through the Dark Grey shutter at (9, 14), which means we MUST be in 'State DarkGrey-Open'.
   - From the Entrance (6, 27), walk North to y=22, then East to (13, 22). This allows accessing the center section.
   - Walk North up x=12 to (12, 14).
   - Walk West through the OPEN Dark Grey shutter at (9, 14) to reach the West Wing.
   - Walk North to the stairs at (5, 10).
5. If in 'State Yellow-Open' (we can tell if we can't pass (9, 14)), we need to go to the East Wing via the OPEN Yellow Shutter at (16, 16), press the switch at (18, 25) to change to 'State DarkGrey-Open', then walk South and West through (13, 22) to x=12, and follow the route above.