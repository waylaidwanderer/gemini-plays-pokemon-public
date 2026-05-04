- Master Route to Secret Key was fundamentally flawed due to y=8 being completely solid in State B. 
- Route to Secret Key: Use B1F in State A (Yellow Closed, Dark Grey Open). From 1F stairs (23,22), enter B1F. Walk West to x=12, then North to pass through the open Dark Grey Shutters at x=11/13.
- Reflection Turn 51098: I have been experiencing 'navigation drift', where I walk partway to my destination (West side of B1F), get into a wild battle, and then unintentionally re-orient East afterwards. I must strictly maintain my directional heading (West to x=12, then South to y=26) despite battle interruptions.
- Reflection Turn 51565: I must visually confirm my immediate adjacent tiles before executing long movement sequences. Blindly mashing 'Up' caused me to bump into a statue at (14, 17) and completely derailed my pathing. I will always check the <CurrentScreen> crop before moving.

- OVERWATCH CORRECTION: B1F East is NOT a dead end! I hallucinated that the gap at x=13 was closed just because I bumped into a wall next to it at x=12. I must return to B1F and test walking North through the gap at (13, 12).
- EMPIRICAL TEST CONFIRMED (Turn 51671): Walked Up from (13, 14) and bumped into a solid wall at (13, 13). B1F East IS A DEAD END. Overwatch hallucinated an open gap here. The ONLY way to B1F West is to drop from 3F.
- Turn 51687: Confirmed visually that (16, 8) is a permanent solid wall. Center North and Center South are COMPLETELY separated. To reach the West Wing (Entrance / 2F stairs), we must find a connection either at y=15 or y=26/y=27.
- Turn 51692: I am in State B. (9, 15) Dark Grey Vertical Shutter is CLOSED in State B. I will toggle to State A at (18, 25) and then check if (9, 15) is OPEN. If it is, I can reach the West Wing and the 2F stairs!
- B1F MASTER ROUTE (UPDATED): B1F East is a DEAD END! The walls at x=11 and y=13 are permanent. To reach B1F West (Secret Key), we MUST drop from 3F! Route: 1F stairs (5,10) -> 2F stairs (6,1) -> 3F. On 3F, drop down the LEFT side of the wide pit to land in 1F West. Then take the stairs down to B1F West!
- Turn 51707: Confirmed that (9, 9) is a permanent dark grey wall. The ONLY connection between Center North and West Wing is via the Yellow Shutters at (9, 6) and (9, 7), which are currently CLOSED in State A. I must toggle to State B to open them, and navigate there via the East Wing!
- Turn 51723 Reflection: I figured out why my movement sequence aborted! The tile at (14, 22) is a Potted Plant obstacle. I bumped into it when trying to move Right from (13, 22), forcing me to walk down the x=13 column instead of x=14. I need to remember to avoid (14, 22).

- CORRECTION: The statues are actually at (14, 17) and (15, 17), NOT y=23. The tiles at (14, 16) and (15, 16) are the tops of these statues, not yellow shutters. The path at x=14 is clear.
- 1F to 2F Warp: Stairs at 1F (5, 10) connect to 2F (1, 18).
- SHUTTER RULE DISCOVERY:
STATE 1: Vertical Yellow OPEN. Horizontal Yellow CLOSED.
STATE 2: Vertical Yellow CLOSED. Horizontal Yellow OPEN.
* Dark Grey Shutters on 1F are PERMANENT WALLS.
- MANSION 1F SOUTH IS ISOLATED: Wall at y=8 is solid across the entire mansion. Wall at x=9 is also completely solid. No path to West Wing on 1F.
- B1F CONNECTION HYPOTHESIS: Since 1F South is isolated, B1F East MUST connect to B1F West. The Dark Grey Shutters at B1F x=11 must open in State 1.
- CURRENT GOAL: Toggle 1F switch to State 1 to check B1F x=11.