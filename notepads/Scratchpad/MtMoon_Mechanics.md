Tile Semantics Hypothesis (Turn 2251):
- Purple blocks = Lower floor.
- Brown speckled = Raised platforms.
- Turn 2307 Conclusion: There are NO clean direct boundaries between lower floors and raised platforms. They are always separated by Obstacle/Cave_Wall_Blue (cliff face) or Obstacle/Chasm_Blue. Elevation changes strictly require stairs/ladders.
- Turn 2599 Conclusion: Even when brown raised floor tiles and purple lower floor tiles are adjacent (e.g., at X=24 and X=23), they cannot be crossed directly. The purple tiles at the boundary have a black edge indicating a cliff drop-off. Elevation changes strictly require stairs/ladders or jumping down specific ledges.
- Turn 2735: Explicit boundary test at (24, 22). Attempted to walk West to (23, 22). Movement was BLOCKED. The transition from the brown platform to the purple lower floor is impassable here. Proceeding to test Southward along the X=24 boundary.
- Turn 2738: Explicit boundary test at (24, 23). Attempted to walk West to (23, 23). Movement was BLOCKED. The transition from the brown platform to the purple lower floor is impassable here. Proceeding to test Southward.
- Turn 3118: Encountered apparent dead-end strip at Y=19 (X=10 to X=17). System rule states soft-locks are impossible. Running exhaustive sweep of South (Y=20) and North (Y=18) boundaries to find the gap.