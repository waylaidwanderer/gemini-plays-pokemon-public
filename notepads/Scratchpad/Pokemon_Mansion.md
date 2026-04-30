Mansion Routing:
- Shutters are individually mapped to the global switch. They are NOT strictly grouped by color.
- State A: Dark Grey OPEN, Yellow CLOSED
  - (16, 16) Yellow: CLOSED
  - (17, 16) Yellow: CLOSED
  - (13, 22)/(13, 23) Dark Grey: OPEN
  - (18, 16) Dark Grey: OPEN
  - y=13 (Central Hub) Dark Grey: OPEN
- State B: Yellow OPEN, Dark Grey CLOSED
  - (16, 16) Yellow: OPEN
  - (17, 16) Yellow: OPEN
  - (13, 22)/(13, 23) Dark Grey: CLOSED
  - (9, 6)/(9, 7) Yellow: OPEN
  - (18, 16) Dark Grey: CLOSED
  - y=13 (Central Hub) Dark Grey: CLOSED

- EMPIRICAL PROOF: (9, 14), (9, 13), and (9, 12) are SOLID in State A (Dark Grey OPEN state).
- EMPIRICAL PROOF (Turn 46949): The wall at x=9 is entirely composed of solid tiles from y=8 down to at least y=17. There are NO Dark Grey shutters in this wall. The ONLY passage across x=9 is the Yellow Shutter at (9, 6)/(9, 7).
- EMPIRICAL PROOF (Turn 47005): The Central Hub is completely blocked from heading North by the permanent solid wall at y=8.
- B1F Dark Grey Shutters at x=11 are CLOSED in State B. Note: (13, 11)/(13, 12) is a permanently solid Dark Grey Wall, not a shutter.