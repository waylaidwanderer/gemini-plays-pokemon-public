- EMPIRICAL FACTS (Victory Road 2F):
  - CRITICAL NAV RULE: GameState provides FEET coordinates (X, Y). The hat visually overlaps (X, Y-1).
  - TILE LEVELS: Dark Red Blocky = Level 1 (Low). DP Speckled = Level 2 (High).
  - 2F West and East appear disconnected. Paths East are blocked by Level 1 Blue Rubble or Level 2 dropoffs.
  - 2F BOULDER PUZZLE SOLUTION (In Progress):
    1. Stand at Feet(4,13). Push boulder Down to (4,15), stepping to (4,14).
    2. Walk to (5,15). Push boulder Left to (3,15).
    3. Walk to (3,14). Push boulder Down to (3,16).
    4. Walk to (4,16). Push boulder Left to (1,16) onto the switch.
- STRATEGY UPDATE (SOLVED PUZZLE LOGIC):
  - The only connection between 2F East and West is the Level 2 overpass, crossing the X=8 boundary at Y=9. We verified this path exists!
  - To cross from 2F East to 2F West: The Level 2 bridge runs West at Y=8/Y=9. We must be on Level 2 (Dark Purple). Use the stairs at (21,15) to ascend to Level 2. Walk Left to X=14 (X=15 is blocked at Y=11). Walk North along X=14 to (14,8), then Left to cross over the Juggler's hat at (12,8).
  - From (5,11) Level 1 West: Walk to (3,8), which was opened by the 2F boulder puzzle. Walk Left to the (0,8) ladder down to 1F (1,1). From 1F (1,1), find the 3F ladder.
- EMPIRICAL BOUNDARIES & LAYOUT (VERIFIED):
  - The Level 2 bridge at Y=9 successfully allows crossing the X=8 boundary. 
  - The Juggler at (12,9) blocks the path on Level 1, but we can walk OVER his hat on Level 2 at (12,8) to bypass him. 
  - The Level 2 overpass continues East and South, functioning as a wide open area at Y=12/13. It leads to stairs DOWN to Level 1 at (15,15) and (21,15).