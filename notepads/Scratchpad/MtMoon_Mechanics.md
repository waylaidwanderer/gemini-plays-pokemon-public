Tile Semantics Hypothesis (Turn 2251):
- Purple blocks = Lower floor.
- Brown speckled = Raised platforms.
- Test Required: Empirically test crossing a brown/purple boundary (without stairs) to prove if this is an elevation barrier or just a standard cave wall. Previous collision at (26, 21) -> (26, 22) might have just been a standard wall.
- Turn 2262 Update: The test on Turn 2261 was flawed because (25, 23) is actually the right half of the stairs. Stepping Up from stairs to a platform works normally. I am now navigating to (26, 22) [purple tile] to test stepping Left onto (25, 22) [brown tile] to isolate a pure purple-to-brown boundary.
- Turn 2263 Correction: I failed to verify visual semantics. (26, 23) is not a purple floor tile, it's an Obstacle/Cave_Wall_Blue tile! (26, 22) is completely blocked off by rock walls from the south. I am re-routing to (20, 22) to test a clean purple-to-brown boundary at (20, 21).