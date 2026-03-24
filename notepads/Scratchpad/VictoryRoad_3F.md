# Victory Road 3F Empirical Map
- Map ID: 0_198
- Stairs down to 2F at (23, 7) (Lower Level).
- Lower Level path West from stairs dead-ends at X=12 (Y=6, Y=7).
- Stairs to Raised Platform at (17, 5).
- RAISED PLATFORM (TYPE_2770): Contains Cooltrainer at (16, 3). Path extends North to Y=2, East to X=18 (wall at X=19), and West to X=9 (wall at X=8). At X=9, path turns South to Y=10, then West to a hole at (7, 10).
- HOLE at (7, 10): Acts as a solid obstacle to the player. Cannot walk into it. Need to drop a boulder in it from somewhere? Wait, (7, 10) might be where a boulder drops *to*, or drops *from*.
- LOWER LEVEL EAST: Visible East of the X=19 wall. The wall at X=19 has a gap at Y=6 and Y=7 connecting to the West. Contains Boulder 1 at (22, 3), Item Ball at (26, 5), Boulder 2 at (24, 10), Boulder 3 at (22, 15), and HOLE at (23, 15). Path South from (20, 11) is blocked. Path East from (23, 5) is blocked by rock wall at X=24..25. NE Corner (Item Ball & Trainer at 28,5) must be accessed by routing North via Y=2.
- TOPOGRAPHY: X=21 is a solid wall from Y=9 to Y=12. Y=9 is a solid wall from X=21 to X=24. This completely blocks access to Boulder 2 (24, 10) and Boulder 3 (22, 15) from the North and West. We MUST find a way to access them from the South!
- LOWER LEVEL CENTRAL: Path from East side at (19, 9) goes South to (19, 10), then West along Y=10 and Y=11, connecting to the North side of the Western Boulder at (13, 12). This confirms there is no path South from here.
- LOWER LEVEL WEST: Path West at Y=11 connects North to Y=7 via X=12. Path South at X=13 is blocked by Boulder at (13, 12). Pushing it DOWN from the North traps it at (13, 13)! It MUST be approached from the South and pushed UP. Southern area likely accessed via Raised Platform stairs at (7, 10).
- Defeated Cooltrainer♂ at (28, 5).
- LOWER LEVEL EAST: Max Revive collected at (26, 5). Second stairs DOWN at (26, 8) (blocked from North by rock wall at Y=6).
- Raised Platform (7, 10): Tile TYPE_de37 is a solid obstacle when approached from the Right. Cannot walk onto it. Abandoning this route. Will re-explore Lower Level East around Boulder 2 (24, 10) to find a path South.
- HYPOTHESIS REJECTED: The Boulder at (13, 12) is in a 1-tile wide hallway. Tiles (12, 12) and (14, 12) are solid rock walls (TYPE_2889). It is physically impossible to push it Left or Right. It MUST be pushed UP from the South.
- NEW PLAN: The Southern area must be accessed via the Raised Platform. I am going back to the stairs at (17, 5) to explore the far West side of the Raised Platform (West of X=9 at Y=2..Y=4).
- LOWER LEVEL NORTH CORRIDOR: Discovered on Turn 51253. There is a 1-tile wide corridor along Y=1 that connects the East side (X>19) to the West. It runs North of the Raised Platform. Exploring it now.
- LOWER LEVEL WEST (NORTH OF RAISED PLATFORM): Reached via the Northern Corridor (Y=1). This area contains a Switch (`TYPE_eb90`) at (3, 5) and an Item Ball at (7, 7). The area is bounded by the Raised Platform to the South at Y=7. The Switch at (3, 5) likely needs a boulder. Boulder 1 at (22, 3) is the only candidate, meaning it must be pushed all the way across the Northern Corridor!
[Boulder 1 Puzzle Routing]
Current: Boulder at (22, 3). Switch at (3, 5).
Strategy: Push the boulder UP to Y=1, then push it all the way LEFT through the Northern Corridor to X=7. From there, navigate it DOWN and LEFT through the obstacles to reach the switch at (3, 5).
- RAISED PLATFORM WEST: Path from (7, 10) continues West and North to (5, 8). At (5, 8), the path goes West to X=1. There appears to be a staircase DOWN at (1, 9).
- LOWER LEVEL FAR WEST: Accessed via stairs at (1, 9) from the Raised Platform. This area goes South along X=1 to Y=15, and opens Eastward. There is a boulder at (6, 14).
- LOWER LEVEL SOUTH CORRIDOR: Discovered Turn 51442. There is a path along Y=15/Y=16 connecting the Far West (X=6) to the East! This allows access to the southern area containing Boulder 3 (22, 15) and the target hole (23, 15).
- [Turn 51444] Reached Boulder 3 at (22, 15) via the South Corridor! The target hole is directly East of it at (23, 15). Preparing to push it in.
- [Turn 51445] Pushed Boulder 3 at (22, 15) into the hole at (23, 15)! It disappeared. (Note: Strength was still active despite wild encounters, meaning my previous hypothesis that *all* wild encounters deactivate it might be wrong. Perhaps running from them preserves it? Regardless, the boulder is in!). Jumping in after it!
- [Turn 51446] REVELATION: The hole at 3F (23, 15) drops to 2F (23, 16), which is on the LOWER LEVEL. The target hole for 2F is at (23, 14) on the RAISED PLATFORM. Furthermore, the boulder is stuck at 2F (23, 16) surrounded by rocks, and I landed at (22, 16). Therefore, the hole at 3F (23, 15) is a TRAP/EXIT! It does not solve the 2F Raised Platform puzzle. Exploring the path West from 2F (22, 16) now.
- [Turn 52415] Accidentally pushed Boulder 1 up to Y=0 instead of Y=1. Testing if the corridor is open along Y=0 to the West.
- [Turn 52417 Trap Discovery] CRITICAL MECHANIC: If a boulder is pushed against the map boundary (like Y=0), it can NEVER be pushed away from that boundary. To push a boulder DOWN, the player must be ABOVE it (at Y=-1), which is off the map. Because the switch is at Y=5, the boulder must eventually be pushed DOWN. Therefore, pushing the boulder to Y=0 has permanently soft-locked the puzzle. I MUST take the stairs at (23, 7) to reset the floor and try again.