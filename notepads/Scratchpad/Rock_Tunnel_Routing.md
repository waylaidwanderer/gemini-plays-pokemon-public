Rock Tunnel 1F Routing (Updated Turn 13412):
- Entrance at (15, 3). Stepping on it exits to Route 10.
- Re-evaluating West Section (X=14..17). I hallucinated that Y=8 is floor. Empirical test on turn 13406 showed that moving Down from (16, 7) into (16, 8) fails.
- Current Goal: Systematically test Y=8 by moving Down from (15, 7) and (14, 7) to confirm if the West section is a dead end.
- Hypothesis: In this tileset, the "top" of a rock wall uses the exact same visual tile as the walkable floor (`Walkable/Cave_Floor_Lower`). This means tiles that LOOK like floor might actually be solid walls if they are directly above a `Obstacle/Cave_Wall_Blue` face tile. I will test this by attempting to walk on the floor-looking tiles at Y=8.