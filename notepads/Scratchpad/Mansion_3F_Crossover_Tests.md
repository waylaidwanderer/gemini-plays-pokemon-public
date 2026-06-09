# 3F West-East Southern Balcony Crossover Passability Tests
- **Objective**: Systematically test and document whether the southern balcony on Rows 16 and 17 provides a continuous, walkable horizontal crossover that connects 3F West to 3F East on foot.

## Test Log (Started Turn 77524)
- *TBD*
- **Turn 77569**: Systematic visual check of Rows 16 and 17 on 3F West confirms that Columns 6 to 10 are completely blocked by solid wall/rubble of TYPE_2889. Row 17 on Columns 1 to 10 is also blocked by solid wall/rubble or railing of TYPE_2889. This mathematically disproves the southern balcony crossover hypothesis. There is no walkable horizontal connection between 3F West and 3F East under State B.
- **Routing Decision**: We must backtrack down to 1F East under State B. We will check if the staircase at (25, 14) on 1F East (which we previously documented as a normal floor tile with no stairs) actually warps us up to the isolated 2F Southeast room, which contains the stairs up to 3F East.

## Socratic Question Response & Test Protocol (Turn 77665)
- **The Visual Check Danger**: Visually checking (25, 14) from across closed Gate 1 on Turn 76295 was a massive pitfall. In Gen 1, warp tiles can look identical to normal floor tiles, meaning visual observation is NOT proof of absence.
- **The Burden of Proof Principle**: Only physical foot-testing (standing on the exact tile and verifying if a map transition occurs) satisfies the Burden of Proof.
- **Physical Foot-Test Protocol for (25, 14)**:
  1. Walk to (26, 3) via Row 3.
  2. Walk South down Column 26 to Row 13: (26, 3) -> (26, 13).
  3. Walk Left to (25, 13) (Gate 1, open under State B).
  4. Walk Down 1 step onto (25, 14).
  5. Observe:
     - **Result A**: If we warp to 2F East South at (25, 14), then the staircase is bidirectionally active and verified. We will immediately update `Locations/CinnabarMansion` to reflect this.
     - **Result B**: If we stand on (25, 14) on 1F and nothing happens, we will attempt to interact facing in all directions. If still nothing, then (25, 14) is indeed a one-way warp from 2F or not a warp at all, proving the hypothesis false.