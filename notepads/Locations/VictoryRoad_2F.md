# Victory Road 2F
- Map ID: 0_194
- Elevation Facts (CRITICAL):
  - LOWER LEVEL is TYPE_3fe2. Contains Boulder at (5, 5), Item Ball at (9, 11), Item Ball at (18, 9), Moltres at (11, 5).
  - RAISED PLATFORM is TYPE_2770. Contains Blackbelt at (12, 9), Juggler at (21, 13), Target Hole at (23, 14), Stairs to 3F at (25, 14).
- Entrance from 1F is at (0, 8) on LOWER level.
- Puzzle 1 (Lower Level): Switch at (1, 16).
- Puzzle 1 Solution (Switch at 1,16):
  - FACT: The boulder at (5,5) is a DECOY. It is bounded East by a wall at (6,5) and North by a 1-tile deep alcove at (5,4) bounded by walls at (4,4) and (6,4). It CANNOT be pushed Left or Down. My Turn 52082 note was a hallucination.
  - TRUE SOLUTION: We must drop a boulder from 3F down to 2F. The boulder at 3F (6, 14) is the most likely candidate. We need to go to 3F to solve this.
- To reach 3F, we must use the stairs at (25, 14) on the East Raised Platform.
- How to reach the Raised Platform East:
  1. From 2F entrance at (0, 8), walk East to (3, 8).
  2. Walk South through the gap at (3, 8) to reach the South side of the West Lower Level.
  3. Walk East to (5, 11).
  4. Take the stairs UP at (5, 10) to reach the Raised Platform!
  5. Walk East to (14, 12), then continue East to (25, 12), then South to the stairs at (25, 14).
- Topography Facts:
  - Stairs at (5, 10) connect Raised (5, 9) to Lower (5, 11).
  - NO STAIRS at (7, 8). It is a cliff edge.
  - West Lower Level (X < 8) is separated from East Lower Level by a solid rock wall at X=8.
  - East Raised Platform: The Juggler is at (21, 13). DEAD END. Y=12 and Y=13 are blocked by walls at X=22. Y=14 is blocked by a wall at (20, 14). It is impossible to walk East past X=21. The stairs at (25, 14) CANNOT be reached from here. We must find another way to 3F.
  - West Raised Platform (West of X=8): DEAD END. Bounded by rocks at West X=4, North Y=7, South Y=10. 
  - CONCLUSION: The stairs at 1F (1,1) -> 2F (0,8) only lead to isolated dead-end platforms on 2F. To reach 3F via the stairs at 2F (23,7), we MUST use the alternate stairs at 1F (7,7) to access the East side of 2F!
  - South East Lower Level is accessed via stairs at (15, 15). Path West from stairs leads to TM05 at (9, 12). Path East is a dead-end pocket along Y=16/Y=17 containing the trap boulder drop at (23, 16). It DOES NOT connect to the 3F stairs at (23, 7). Another stairs at (27, 7) is blocked by walls, accessed by dropping from 3F.
- [Turn 51838] Discovered that Y=4 on the West Lower Level is a solid rock wall from X=0 to X=8. There is NO Northern Corridor on 2F. My previous assumption was a hallucination confusing 3F's layout with 2F.