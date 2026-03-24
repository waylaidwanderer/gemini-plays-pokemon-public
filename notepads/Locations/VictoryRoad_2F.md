# Victory Road 2F
- Map ID: 0_194
- Elevation Facts (CRITICAL):
  - LOWER LEVEL is TYPE_3fe2. Contains Boulder at (5, 5), Item Ball at (9, 11), Item Ball at (18, 9), Moltres at (11, 5).
  - RAISED PLATFORM is TYPE_2770. Contains Blackbelt at (12, 9), Juggler at (21, 13), Target Hole at (23, 14), Stairs to 3F at (25, 14).
- Entrance from 1F is at (0, 8) on LOWER level.
- Puzzle 1 (Lower Level): Switch at (1, 16). The boulder at (5, 5) is meant for this switch! We must reach the North side of (5, 5) to push it South -> West -> South.
- Puzzle 1 Solution (Switch at 1,16):
  - HALLUCINATION CORRECTION: The boulder at (5,5) is NOT a decoy! Tiles (4,5) and (5,4) are floor tiles, NOT walls. It is fully movable. My Turn 51904 note was completely wrong.
  - Path:
    1. Walk to (5, 4) via (4, 7) -> (4, 5).
    2. Push Boulder DOWN to (5, 6).
    3. Walk to (6, 6) via (4, 5) -> (4, 7) -> (6, 7).
    4. Push Boulder LEFT to (4, 6).
    5. Walk to (4, 5) via (5, 5).
    6. Push Boulder DOWN towards Y=16.
- Topography Facts:
  - Stairs at (5, 10) connect Raised (5, 9) to Lower (5, 11).
  - NO STAIRS at (7, 8). It is a cliff edge.
  - West Lower Level (X < 8) is separated from East Lower Level by a solid rock wall at X=8.
  - East Raised Platform: Continues East past the Blackbelt at (12, 9) to reach the Juggler at (21, 13) and the Target Hole at (23, 14). My previous note about it being a dead end at X=15 was a massive hallucination!
  - West Raised Platform (West of X=8): DEAD END. Bounded by rocks at West X=4, North Y=7, South Y=10. 
  - CONCLUSION: The stairs at 1F (1,1) -> 2F (0,8) only lead to isolated dead-end platforms on 2F. To reach 3F via the stairs at 2F (23,7), we MUST use the alternate stairs at 1F (7,7) to access the East side of 2F!
  - South East Lower Level is accessed via stairs at (15, 15). Path West from stairs leads to TM05 at (9, 12). Path East is a dead-end pocket along Y=16/Y=17 containing the trap boulder drop at (23, 16). It DOES NOT connect to the 3F stairs at (23, 7). Another stairs at (27, 7) is blocked by walls, accessed by dropping from 3F.
- [Turn 51838] Discovered that Y=4 on the West Lower Level is a solid rock wall from X=0 to X=8. There is NO Northern Corridor on 2F. My previous assumption was a hallucination confusing 3F's layout with 2F.