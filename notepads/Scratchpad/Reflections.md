[Active Reflections]
[Mansion Master Puzzle Solution]
Goal: Reach B1F isolated area to find the Secret Key.
Requirement: 3F Southern doors (15, 10) OPEN, AND B1F Central doors (20, 17) OPEN. This is STATE B.

[Door Logic]
- TYPE_a83b (glowing orange lines) = ACTIVE LASER BARRIER (CLOSED).
- TYPE_3fe2 (plain pink floor) = OPEN DOOR / REGULAR FLOOR.
- 2F West doors (7, 12) are CLOSED in State A.
- 2F East doors (24, 13) are OPEN in State A.
- 2F Central doors (20, 17) are CLOSED in State A.
- 3F Southern doors (15, 10) are CLOSED in State A.
- Currently: East doors (24, 13) are TYPE_a83b (CLOSED). I am in STATE B.

[Constraints]
- The South-West area of 2F is isolated by a solid vertical wall at X=11 extending from at least Y=17 to Y=25. You CANNOT reach the Central doors at (20, 17) via the West doors at (7, 12).
- The East doors (24, 13) are the ONLY entry to the South-East area. Since they CLOSE in State B, the SE area is inaccessible in State B.
- Therefore, the 2F switch statue in the SE area MUST be the key to reaching the 3F stairs.

[NEW HYPOTHESIS: The 2F Statue is NOT fake]
- The statue at (20, 13)/(21, 13) and (20, 14)/(21, 14) is 2 tiles wide.
- I only tested interacting from (21, 15) facing Up (the right half).
- I MUST test interacting from (20, 15) facing Up (the left half).
- If it works, it will swap the door states locally on 2F, allowing me to pass the Central doors (20, 17) while they are OPEN in State B!

[THE TRUE MASTER ROUTE TO THE SECRET KEY (Draft 3)]
1. 1F: Set switch at (2, 10) to State A (Default).
2. 2F: Navigate East Wing to access the South-East area.
3. 2F: Walk to the switch statue at (20, 14)/(21, 14).
4. 2F: Stand at (20, 15), face Up, and interact to change to State B.
5. 2F: Walk West to the Central doors at (20, 17). They should now be OPEN!
6. 2F: Walk South through OPEN Central doors (20, 17) to reach the stairs at (21, 23).
7. 3F: Arrive on 3F in State B. The 3F Southern doors (15, 10) will be OPEN.
8. 3F: Walk South and jump down the pit at (16, 14) or (17, 14).
9. 1F: Land in the enclosed area. Take the stairs down to B1F.
10. B1F: Central doors (20, 17) are OPEN (State B)! Walk West to find the Secret Key.
[Turn 40185 50-Turn Reflection]
- Immediate Execution: Currently executing Master Route (Draft 3) to the Secret Key. On 2F, heading to the East doors at (24, 13) which should be OPEN in State A.
- Error Analysis: Previously stuck in a switch-toggling loop due to mashing 'A' through dialogue. Corrected by using single 'A' presses and 'B' mashing.
- Hypothesis: The 2F switch statue in the SE area MUST be interactable from the left side (20, 15). If so, it will swap states locally and allow access to the Central doors.