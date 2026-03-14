# Safari Zone Run (Turn 31231)
- Goal: Reach Secret House at Area 4 West (3,3)
- Status: Entering Gate.
- Plan:
  1. Go to Area 2 East via (29, 22).
  2. Go to Area 3 North via (0, 4).
  3. Go to Area 4 West via (8, 35).
  4. Navigate to (3,3).
[Reflection Turn 31247]
- Error Analysis: The Cut bush "glitch" was a spatial hallucination (I was at X=18, not X=22). I've learned to heavily verify coordinates before assuming glitches.
[Turn 31253] Entering Area 2 East via (29, 22). Next target: Area 3 North via Northwest Exit at (0, 4) in Area 2 East.
[Turn 31272] Position (16, 24). Moving to climb the East Plateau stairs at (20, 21) to head North towards Area 3.
[Turn 31278] Path North at X=18..20 blocked by ledges/trees. The correct path North is at X=21/X=22. Moving East to X=21 then North.
[Turn 31286] Currently at (21, 12) in Area 2 East. Navigating North to Y=8, then will head West towards the exit at (0, 4).
[Turn 31289] Potential Hallucination: At (21, 12), the transition to (21, 11) looks like a ledge, but (21, 11) is TYPE_3fe2 (regular walkable grass). Dirt-to-grass transitions are often NOT solid. I will test walking North from (21, 12) to confirm if it's actually blocked before giving up on this path.
[Turn 31323] Area 2 East Routing: Discovered a solid wall of bushes at Y=6 from X=0 to X=8. It is IMPOSSIBLE to walk straight North from the Dirt Trench along the West edge to reach the (0, 4) exit. The path must be further East, possibly via the stairs at (12, 7).
[Turn 31326] Taking stairs up at (12, 7) to reach the northern part of the plateau.
[Turn 31337] Area 2 East Routing: The stairs at (12, 7) lead up to a dirt plateau. West is blocked at X=10, but the plateau continues EAST. We can bypass the tree at (14, 8) by walking East on the plateau and taking stairs down at (17, 7).
[Turn 31348 CRITICAL REVELATION]
- Area 2 East is a ONE-WAY LOOP from Area 3 North. The ledges at Y=6 mean you CANNOT walk from the rest of Area 2 East to the (0, 4) exit to Area 3 North.
- The Safari Zone is NOT linear (1->2->3->4).
- The TRUE path from Area 1 Center to Area 3 North is the NORTH EXIT of Area 1 Center at (15, 0)!
- I have been wasting runs going to Area 2 East. The correct route is: Area 1 Center (North) -> Area 3 North (West) -> Area 4 West.