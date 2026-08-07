# Game Corner Plaza Lateral Movement Empirical Test Log

## Hypothesis
Tile (10, 0) in Game Corner Plaza is the warp tile back to Celadon City (20, 35).
Stepping Down 1 step from (10, 0) to (10, 1) lands the player safely at (10, 1) without warping.
From (10, 1), lateral East/West movements along Row 1 (e.g. testing Right to (11, 1)) will test if (11, 1) is a passable tile or statue gap leading to (12, 1), (13, 1), and (14, 1) [the Game Corner main entrance red door mats].

## Step-by-Step Test Execution Plan
1. Return West to (20, 30) along Row 31 / Row 30 street in Celadon City.
2. Walk Down along Column 20 to (20, 35).
3. Step Down 1 step to (20, 36) to warp into Game Corner Plaza at (10, 0).
4. Step Down 1 step to (10, 1) [verified safe from warp].
5. Press Right at (10, 1) to empirically test collision / movement onto (11, 1).
6. Document result and continue East along Row 1 towards (14, 1) red door mat.