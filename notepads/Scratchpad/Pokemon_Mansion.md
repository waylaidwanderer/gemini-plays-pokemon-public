- MANSION PUZZLE EMPIRICAL TESTING:
I need to figure out exactly what the switch at (18, 25) does.

STATE 1 (Turn 48458):
- 1F (16, 16) Yellow: CLOSED (Visually confirmed Turn 48464)
- 1F (13, 16) Dark Grey: CLOSED (Visually confirmed Turn 48464)

STATE 2 (Turn 48475):
- 1F (16, 16) Yellow: OPEN (Visually confirmed Turn 48482)
- EMPIRICAL PROOF (Turn 48498): Walked West to (3, 18) and verified that the `Obstacle/Wall_Horizontal_YellowBrown` at y=17 is completely solid from x=1 to x=9. There is NO path North from the West Wing South area. I must use a different route to reach the West Wing North stairs at (5, 10). I recall old notes mentioning a passage at (16, 7). I will head there now.
- EMPIRICAL PROOF (Turn 48500): The wall at 1F x=13 is completely solid from y=17 to y=20. The only way back to the Central Hub from the West Wing South is through the dark grey shutter at (13, 16).
- MANSION PUZZLE HYPOTHESIS: To progress North on B1F, I need State A (Dark Grey Shutters open). However, I can only reach the B1F stairs on 1F in State B (Yellow Shutters open). This means I either need to find a switch on B1F South, or I need to find a drop hole from 2F/3F that deposits me near the B1F stairs while the Mansion is already in State A.
- MECHANIC (Turn 48507): When arriving on B1F via the stairs at 1F (23, 22), you spawn at B1F (21, 24) (forced to step off the stairs at 21, 23). Walking Up back into (21, 23) will immediately warp you back to 1F.
- MANSION MASTER PLAN (Turn 48533): 
1. The goal is to reach 2F in State A (Dark Grey Shutters open). This will likely allow access to the correct drop hole to reach B1F in State A.
2. The Entrance Hallway to the 2F stairs is blocked at y=17. 
3. The only path North past y=17 is the x=12 corridor. 
4. The x=12 corridor is separated from the Entrance Hallway by Dark Grey Shutters at (9, 15)/(9, 16). These are OPEN in State A.
5. In State A, the Dark Grey Shutter at (13, 26) is hypothesized to be OPEN.
6. Therefore, the path to 2F in State A is: Switch (18, 25) -> (18, 26) -> Left through (13, 26) to (12, 26) -> North to (12, 16) -> West through (9, 16) to Entrance Hallway -> North to 2F stairs at (5, 10).
7. I must empirically test the states of (13, 26) and (9, 16) individually, as my previous notes confirmed shutters are individually mapped to the global switch.
- EMPIRICAL PROOF (Turn 48552): Visually verified that (13, 26) is `Obstacle/Wall_Dark_Grey_Solid` without any tracks. It is a permanent solid wall, not a shutter. Therefore, the x=12 corridor can NEVER be accessed from the South.