[Active Reflections]
[Mansion Master Puzzle Solution]
Goal: Reach B1F isolated area to find the Secret Key.
Requirement: 3F Southern doors (15, 10) OPEN, AND B1F Central doors (20, 17) OPEN. This is STATE B.

[Door Logic]
- TYPE_a83b (glowing orange lines) = ACTIVE LASER BARRIER (CLOSED).
- TYPE_3fe2 (plain pink floor) = OPEN DOOR / REGULAR FLOOR.
- 2F East doors (24, 13) OPEN in State A, CLOSED in State B.
- 2F Northern doors (16, 7) CLOSED in State A, OPEN in State B.
- 2F Central doors (20, 17) CLOSED in State A, OPEN in State B.
- 3F Southern doors (15, 10) CLOSED in State A, OPEN in State B.
- B1F Central doors (20, 17) CLOSED in State A, OPEN in State B.

[NEW HYPOTHESIS: The 2F SE Statue is a RED HERRING]
- Tested both (22, 14) and (23, 14) facing Up. Neither triggered a switch.
- The statue at (22, 13) is completely inert.
- This means you CANNOT change door states locally in the SE area of 2F.

[DRAFT 5 DEBUNKED]
- I exhaustively mapped the South-West area. It is just two empty parallel corridors. There are NO UP stairs there.
- The SE area is a trap because you enter in State A (East doors open), but need State B to pass the Central doors. No switch exists there.
- Therefore, the Central doors MUST be reached from the North!

[THE TRUE MASTER ROUTE TO THE SECRET KEY (Draft 6)]
- The entire puzzle can be solved while remaining in STATE B! (Reverting to Draft 4's logic).
- My previous observation that the Northern doors led to a dead end at Y=13 was an unverified hallucination. I saw a wall on screen but never actually walked down to it to check for side paths.
1. 1F: Set switch at (2, 10) to State B.
2. 2F: Navigate to the Northern doors at (16, 7). They will be OPEN.
3. 2F: Walk South through the Northern doors and carefully explore the path to the Central doors at (20, 17).
4. 2F: Since we are in State B, the Central doors at (20, 17) will ALSO be OPEN!
5. 2F: Walk South through Central doors to reach 3F stairs at (21, 23).
6. 3F: Arrive on 3F in State B. The 3F Southern doors (15, 10) will be OPEN.
7. 3F: Walk South and jump down the pit at (16, 14).
8. 1F: Land in the enclosed area. Take stairs down to B1F.
9. B1F: Central doors (20, 17) are OPEN! Walk West to find the Secret Key.
[Turn 40596] Confirmed 1F switch set to State B. Proceeding to 2F Northern Doors.
[Turn 40605] Arrived at 2F Northern Doors (16, 7). They are CLOSED (State A). I must have double-toggled the 1F switch by accident on Turns 40589-40595. Returning to 1F to carefully toggle it ONCE.
[Turn 40609] REALIZATION: Pressing 'B' (via safe_mash_b or otherwise) while a YES/NO prompt is active will CANCEL the prompt (defaults to NO). This is exactly why my toggle failed on Turn 40596! I must press 'A' on the YES/NO prompt to actually activate the switch.