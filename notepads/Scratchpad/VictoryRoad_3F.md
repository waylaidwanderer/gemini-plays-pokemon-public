# Victory Road 3F Empirical Map
- Map ID: 0_198
- Stairs down to 2F at (23, 7) (Lower Level).
- Lower Level path West from stairs dead-ends at X=12 (Y=6, Y=7).
- Stairs to Raised Platform at (17, 5).
- RAISED PLATFORM (TYPE_2770): Contains Cooltrainer at (16, 3). Path extends North to Y=2, East to X=18 (wall at X=19), and West to X=9 (wall at X=8). At X=9, path turns South to Y=10, then West to a hole at (7, 10).
- HOLE at (7, 10): Acts as a solid obstacle to the player. Cannot walk into it. Need to drop a boulder in it from somewhere? Wait, (7, 10) might be where a boulder drops *to*, or drops *from*.
- LOWER LEVEL EAST: Visible East of the X=19 wall. The wall at X=19 has a gap at Y=6 and Y=7 connecting to the West. Contains Boulder 1 at (22, 1), Item Ball at (26, 5), Boulder 2 at (24, 10), Boulder 3 at (22, 15), and HOLE at (23, 15). Path South from (20, 11) is blocked. Path East from (23, 5) is blocked by rock wall at X=24..25. NE Corner (Item Ball & Trainer at 28,5) must be accessed by routing North via Y=2.
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
Current: Boulder at (2, 5). Switch at (3, 5). Must reactivate Strength after every wild battle!
Strategy: Reactivate Strength. Walk to (1, 5) and push Right to (3, 5).
- RAISED PLATFORM WEST: Path from (7, 10) continues West and North to (5, 8). At (5, 8), the path goes West to X=1. There appears to be a staircase DOWN at (1, 9).
- LOWER LEVEL FAR WEST: Accessed via stairs at (1, 9) from the Raised Platform. This area goes South along X=1 to Y=15, and opens Eastward. There is a boulder at (6, 14).
- LOWER LEVEL SOUTH CORRIDOR: Discovered Turn 51442. There is a path along Y=15/Y=16 connecting the Far West (X=6) to the East! This allows access to the southern area containing Boulder 3 (22, 15) and the target hole (23, 15).
- [Turn 51444] Reached Boulder 3 at (22, 15) via the South Corridor! The target hole is directly East of it at (23, 15). Preparing to push it in.
- [Turn 51445] Pushed Boulder 3 at (22, 15) into the hole at (23, 15)! It disappeared. (Note: Strength was still active despite wild encounters, meaning my previous hypothesis that *all* wild encounters deactivate it might be wrong. Perhaps running from them preserves it? Regardless, the boulder is in!). Jumping in after it!
- [Turn 51446] REVELATION: The hole at 3F (23, 15) drops to 2F (23, 16), which is on the LOWER LEVEL. The target hole for 2F is at (23, 14) on the RAISED PLATFORM. Furthermore, the boulder is stuck at 2F (23, 16) surrounded by rocks, and I landed at (22, 16). Therefore, the hole at 3F (23, 15) is a TRAP/EXIT! It does not solve the 2F Raised Platform puzzle. Exploring the path West from 2F (22, 16) now.
- [Turn 52458] Boulder 1 successfully pushed onto the switch at (3,5) AGAIN! Puzzle solved. The path at (7, 10) is open.
- [Turn 52525] Topography Correction: The Northern Corridor has a 1-way ledge at Y=2 (facing South). This means you CANNOT walk North from (4,3) to (4,2). Furthermore, (3,3) is a rock wall. The area at (4,3) and (4,4) is a ledge trap! You must loop around via X=2: (4,3) -> (4,4) -> (2,4) -> (2,1) -> (3,1) -> (3,2) -> (4,2).
- [Turn 52527 WARNING: TRAP TILE] Tile (4, 3) is a 1x1 inescapable pit trap! It is bounded by a 1-way ledge to the North (4, 2) and solid walls on all other sides (Left, Right, and Down). Stepping Down from (4, 2) permanently traps the player here! MUST use Dig or Escape Rope to exit the dungeon!
- [Turn 53197] Topography Update: The East pocket (containing the 23,7 stairs) is completely separated from Boulder 2 (24,10) by a solid rock wall at Y=9 (X=21..24). Boulder 2 must be reached from the South! The stairs at 2F (25,14) likely emerge South of Boulder 2.
- NEW PUZZLE HYPOTHESIS: Boulder 3 at (22,15) is a decoy for the trap hole. The true puzzle solution for the 2F (9,16) switch is to use the boulder at 3F (6,14) in the Far West!
- [Turn 53216] EPIPHANY! The hole at 3F (9, 15) perfectly aligns with the switch at 2F (9, 16) due to the map's +1 Y drop offset! The boulder at 3F (6, 14) must be pushed into this hole.
- [Turn 53431] CRITICAL REMINDER: The wall at (7, 10) is CLOSED! Leaving the floor reset the rock wall, even though the boulder is still on the switch at (3, 5). I MUST travel to (3, 5), push the boulder OFF the switch, and push it back ON to re-open the wall.
- Strategy: From (8, 10), walk East to the stairs at (17, 5), drop to the Lower Level, walk North to the Y=1 corridor, and walk West to (3, 5).
- [Turn 53434] Raised Platform navigation: The Raised Platform from X=10 goes North to Y=2, then East to the stairs at (17, 5). I cannot go West from X=10 because of the rock wall at X=8.
- [Turn 53500] Routing Boulder 1: Boulder is at (7,1). The wall at X=5 is solid at Y=0 and Y=1 (`TYPE_2889`). The ONLY gap is at (5,2). Sequence planned: push LEFT to (6,1), walk to (6,0), push DOWN to (6,2), walk to (7,2), push LEFT through the gap to (5,2) and then (4,2).
- [Turn 53503] Pushing Boulder 1 from (2,2) to (2,5), then navigating to (1,5) and pushing it Right to the switch at (3,5).
- [Turn 53669] Navigating South Corridor East. The path at Y=15 is blocked by a rock at (12, 15). The corridor dips down to Y=16 via (11, 16) to continue East.
- [Turn 53761] Route from Boulder 3 Drop to 2F Switch:
  1. From (23, 13), I am blocked from walking North to the (23, 7) stairs by the solid rock wall at Y=9.
  2. I must take the long way around: Walk West through South Corridor -> Stairs at (1, 9) UP to Raised Platform -> Walk East to stairs at (17, 5) DOWN to Lower Level -> Walk North to Y=1 -> Walk East to X=23 -> Walk South to stairs at (23, 7) DOWN to 2F.
  3. Once on 2F, walk South to the dropped boulder and push it West to the switch at 2F (9, 16).