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

- EMPIRICAL PROOF (Turn 46949): The wall at x=9 is solid. ONLY passage across x=9 is Yellow Shutter at (9, 6)/(9, 7).
- EMPIRICAL PROOF (Turn 47005): Central Hub is completely blocked from heading North by permanent wall at y=8.
- CONCLUSION: The 1F Route to West Wing is IMPOSSIBLE in both states. B1F is the ONLY way forward.
- B1F Dark Grey Shutters at x=11 are CLOSED in State B. I need to toggle back to State A to open them. Note: (13, 11)/(13, 12) is a solid Dark Grey Wall.