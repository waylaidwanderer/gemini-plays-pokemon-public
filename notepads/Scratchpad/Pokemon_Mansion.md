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
- EMPIRICAL PROOF (Turn 47333): Crossed x=9 by walking East at y=18 from (6, 18) to (11, 18). The wall at x=9 is OPEN at y=18.
- B1F Dark Grey Shutters at x=11 were empirically proven to be CLOSED in State A (Turn 46990, 47101) and State B (Turn 47180). Note: (13, 11)/(13, 12) is a solid Dark Grey Wall.
- EMPIRICAL PROOF (Turn 47454): The objects at 1F (18, 16)/(19, 16) and (14, 16)/(15, 16) are the top halves of the statues located at y=17. They are permanently solid. The ONLY shutters at the Central Hub choke point are the Yellow Shutters at (16, 16)/(17, 16).
- MANSION ESCAPE ROUTE:
  1. Toggle switch at 1F (18, 25) to STATE B (Yellow OPEN).
  2. Walk North through the open Yellow Shutters at (16, 16)/(17, 16) to reach y=15.
  3. Walk East at y=15 to x=23 (East Wing).
  4. Walk South to stairs at (23, 22) -> down to B1F.
  5. Navigate B1F North to the stairs leading to the North West Wing (Entrance).
- EMPIRICAL PROOF (Turn 47180): Bumped into Dark Grey Shutter at B1F (11, 19) while in State B. It is CLOSED. Since it was also CLOSED in State A, either it is permanently closed, or there is another switch/condition required to open it.
- EMPIRICAL PROOF (Turn 47201): Bumped into the southern boundary at 1F (23, 27). It is `Obstacle/Wall_Horizontal_YellowBrown` and completely solid. There is no exit in the East Wing. The only exit must be at the West Wing entrance (x=16/17).