Pokemon Mansion Navigation & Discoveries:

MECHANICS (DEFINITIVE):
- Exiting to Cinnabar Island resets everything to State A.
- "A secret switch! Press it?" -> YES ("Who wouldn't?") = TOGGLES STATE. NO ("Not quite yet!") = DOES NOTHING.
- State A (Default):
  - Dark Grey Shutters (e.g. 9,9/9,10 and 13,18..21): OPEN (Walkable)
  - Yellow Shutters (e.g. 13,22..23, 9,6/9,7, 16,16): CLOSED (Solid)
- State B (Toggled by switch):
  - Dark Grey Shutters (e.g. 9,9/9,10 and 13,18..21): CLOSED (Solid)
  - Yellow Shutters (e.g. 13,22..23, 9,6/9,7, 16,16): OPEN (Walkable, but visually look solid!)

PERMANENT WALLS:
- All dark grey tiles WITHOUT white tracks on BOTH sides (e.g. x=13 y=16..21) are PERMANENT WALLS.
- y=8 solid wall (x=10 to x=15) blocking North/South in the Middle Section.
- y=17 solid wall (x=1 to x=8) blocking North/South in the West Wing.
- x=13 solid wall (y=17 to y=21). Empirically verified Turn 42050.
- x=13 solid wall (y=24 to y=26). Empirically verified Turn 42084.
- y=27 solid wall blocks connecting West/Middle/East wings along the bottom. Empirically verified Turn 42080.

CURRENT GOAL: EXPLORE EAST WING NORTH TO REACH WEST WING
I am currently in State B. The gap at (16, 16)/(17, 16) is an open hallway, not a shutter. I will walk North through it to find a way West towards the main stairs at (5, 10).

Current plan: Walk Left to x=17, then walk Up repeatedly to explore the Northern part of the East Wing. I am looking for a path West, potentially crossing the Yellow Shutter at (9, 7) into the West Wing North.
Turn 42102: I am in State B. I verified that (13, 18) is CLOSED in State B. I am now heading North in the East Wing to pass through the Yellow Shutter at (16, 16).
Turn 42103 Verification: I am in State A. I pressed Left from (14, 18) and bumped into (13, 18). So (13, 18) is a solid wall in State A. I previously verified it is a solid wall in State B. Therefore, despite having white tracks on the side, the dark grey tiles at x=13 (y=16..21) are PERMANENT WALLS. I must toggle to State B and proceed North via the yellow shutters at (16, 16).
Turn 42105 Reflection: It's been 50 turns. I have been stuck navigating the 1F shutters because my assumption that (13, 18) and (13, 26) were open shutters in State A was incorrect; they are permanent walls disguised as shutters. The only crossing is the yellow shutter at (13, 22), which is open in State B. Therefore, I must be in State B to be in the East Wing, or State B to leave it.
My plan: Toggle to State B. Walk North in the East Wing. The yellow shutters at (16, 16)/(17, 16) will be open. I will go through them and find a way back West. I need to be careful with my visual glossaries - a closed shutter looks like a shutter, an open shutter looks like a floor tile. The fact that (13, 18) looks like a shutter in State A (when dark grey shutters should be open) proves it's a permanent wall.
Turn 42116 Discovery: In State B, the yellow shutters at (16, 16) and (17, 16) are indeed OPEN (walkable pink/white floor tiles). I also see that the dark grey shutters in the East Wing are located at x=20 (from y=16 to y=26), and they are currently CLOSED in State B. I can proceed North through (17, 16).
Turn 42125 Discovery: In State B, the yellow shutters at (16, 16) and (17, 16) are open. This allows access to a horizontal corridor at y=15 that spans from x=13 to at least x=22. I am now walking West along y=15 to see if it connects to the West Wing.
Turn 42131: Reached (10, 15) in the Middle Section (between x=9 and x=13). The dark grey shutters at x=9 appear closed in State B. I am testing walking Left into (9, 15) to confirm, and then proceeding North in the Middle Section to find a path to the main stairs at (5, 10).