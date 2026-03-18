[Active Reflections]
[Mansion Master Puzzle Solution]
Goal: Reach B1F isolated area to find the Secret Key.
Requirement: 3F Southern doors (15, 10) OPEN, AND B1F Central doors (20, 17) OPEN. This is STATE B.

[Door Logic]
- 2F West doors (7, 12) are CLOSED in State A.
- 2F East doors (24, 13) are OPEN in State A.
- Currently: West doors (7, 12) are OPEN. I am in STATE B.

[The True Route]
- To access the South-East stairs to 3F at (21, 23), I must reach the Central Doors at (20, 17).
- MAP CONSTRAINTS: 
  1. The South-West area (via West doors) is an isolated loop bounded by X=11 and Y=13. It is a DEAD END.
  2. The path East along Y=11 is BLOCKED by a solid wall at X=13.
- CONCLUSION: The Central area of 2F CANNOT be accessed from the West Wing or the Stairs area via Y=11. 
- The ONLY remaining unblocked path to the Central Doors at (20, 17) must be from the EAST WING.
- But wait! In State B, the East doors at (24, 13) are CLOSED.
- If the East doors are closed in State B, how can I reach the 3F stairs in State B?
- Hypothesis: I MUST be in State A to pass through the East doors (24, 13), reach the 3F stairs at (21, 23), and go up to 3F.
- BUT! If I go up to 3F in State A, the Southern doors at (15, 10) on 3F will be CLOSED, blocking the pit to B1F!
- There MUST be another switch on 3F that I can press to toggle to State B AFTER I pass the East doors!

[Revised Master Route]
1. 1F: Set switch to State A.
2. 2F: Walk through East doors at (24, 13) which are now OPEN.
3. 2F: Continue South to the stairs at (21, 23) and go up to 3F.
4. 3F: Arrive in State A. The Southern doors (15, 10) are CLOSED.
5. 3F: Find and press a switch to change to State B! This will OPEN the Southern doors (15, 10).
6. 3F: Jump down the pit at (16, 14).
7. 1F: Land in enclosed area. Take stairs down to B1F.
8. B1F: Central doors (20, 17) are OPEN (State B)! Walk West to find the Secret Key.