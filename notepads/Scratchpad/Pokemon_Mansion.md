Mansion Routing:
- Shutters are individually mapped to the global switch. They are NOT strictly grouped by color.
- State A: Dark Grey OPEN, Yellow CLOSED
  - (16, 16) Yellow: CLOSED
  - (17, 16) Yellow: CLOSED
  - (13, 22)/(13, 23) Dark Grey: OPEN
- State B: Yellow OPEN, Dark Grey CLOSED
  - (16, 16) Yellow: OPEN
  - (17, 16) Yellow: OPEN
  - (13, 22)/(13, 23) Dark Grey: CLOSED
  - (9, 6)/(9, 7) Yellow: OPEN

Currently in STATE A. Heading to B1F North via the stairs at (23, 22).
- EMPIRICAL PROOF: (9, 14), (9, 13), and (9, 12) are SOLID in State A (Dark Grey OPEN state). Tested on turn 46944-46945.
- EMPIRICAL PROOF (Turn 46949): The wall at x=9 is entirely composed of solid `Obstacle/Wall_Dark_Grey_Solid` tiles from y=8 down to at least y=17. There are NO Dark Grey shutters in this wall. The ONLY passage across x=9 is the Yellow Shutter at (9, 6)/(9, 7). This confirms that to reach the West Wing stairs at (5, 10), the Mansion MUST be in State B (Yellow OPEN).
- EMPIRICAL PROOF (Turn 47005): The Central Hub is ALSO completely blocked from heading North by the permanent solid wall at y=8. This means it is physically impossible to reach the West Wing stairs at (5, 10) from the Entrance Hallway or Central Hub on 1F. The ONLY way forward is via B1F.
- B1F Dark Grey Shutters at x=11 and (13, 11)/(13, 12) are CLOSED in State A. I must toggle the switch to State B to explore B1F.