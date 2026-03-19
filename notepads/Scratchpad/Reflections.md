[Active Reflections]
[Paradox Resolved]
- Central Doors (20, 17) are blocked from the North in State B by solid wall at Y=13.
- The stairs at (21, 23) on 1F lead DOWN to B1F. The map marker I placed at (21, 23) on 2F for "Stairs to 3F" was a hallucination! They don't exist there.
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

[Stairs Navigation]
- 1F to 2F: Stairs at (5, 10) on 1F lead to 2F.
- 2F to 3F (UP): LOCATION UNKNOWN. Must find them!
- 3F to 2F (DOWN-ONLY): Found drop-down stairs at (6, 1) and (6, 21) on 2F. These cannot be ascended.
- 1F to B1F: Stairs at (21, 23) in the isolated enclosed area of 1F lead down to B1F. (Accessed by jumping down 3F pit at 16, 14).
[2F Stairs Search]
- VERIFIED: The North-East corridor accessed via the Northern doors at (16, 7) is a trap! It is a dead end containing switch statues at (16, 10) and (18, 10). Pressing them will close the doors and trap you. There are NO stairs here.
- The stairs to 3F MUST be in the East Wing, accessible via the East doors at (24, 13) ONLY when they are OPEN (State A).
[3F South Re-exploration Completed - Turns 41857-41861] Area is a verified dead end.
[Search for 3F Stairs]
- Stairs to 3F main area ARE in the 2F South-East area (accessed via doors at 24, 13 in State A). My previous note about a Bar Graph was a hallucination!
- 3F South room (accessed via 1F warp stairs at 7, 10) is a DEAD END containing only a Max Potion.
- NEW PLAN: Explore 2F West area (South of Y=18, the red carpet room) or look for hidden gaps on 1F / 2F Central.
[50-Turn Reflection - Turn 42005]
- Caught in a menu loop due to overusing long `move_sequence` macros without verifying cursor memory. Going forward, I will strictly use 1-to-2 button presses for manual menu navigation or use dedicated state-aware tools.
- Tool Maintenance: Need to fix `execute_battle_turn` to not wrap to ITEM when `start_on_main` is true and the cursor is already on FIGHT.
[Turn 42033 - 2F West Exploration]
- Standing at 2F (5, 15).
- There is a Burglar trainer at (1, 17). He paces between X=1 and X=3.
- The path South is clear at X=5. I will walk down to Y=22 to enter the red carpet room and see what's there.
[Turn 42039 - Route to 3F Main]
- I am currently back on 1F at (5, 10).
- I need to get to 2F East Wing, then take the stairs at (24, 13) up to 3F.
- To reach 2F East Wing from 2F Central, I MUST pass through the Northern doors at (16, 7).
- The Northern doors are ONLY open in STATE B.
- However, to access the stairs at (24, 13) in the 2F East Wing, the East doors at (24, 13) must be OPEN.
- The East doors are ONLY open in STATE A.
- This means I need to toggle the state WHILE I am in the East Wing!
- But wait, the only switches I know of in the East Wing are the trap switches at (16, 10) and (18, 10) that lock you in.
- Let me re-read my notes carefully.
- "Found a glowing-eye switch statue at (21, 13)/(21, 14) in the enclosed South-East area (accessed via East doors)."
- Ah! That's it!
- The route is:
  1. Set Mansion to STATE A (using 1F switch).
  2. The 2F Northern doors (16, 7) are CLOSED in State A. I CANNOT reach the East Wing via the 2F Northern hallway!
  3. Wait. If the Mansion is in State A, how do I get to the East Wing?
  4. On 1F, the East Wing is accessible via the gaps at X=9 (Y=4/Y=5 and Y=10/Y=11).
  5. Are there stairs to 2F in the 1F East Wing?
  6. Let me check my notes: "South-East corridor (X=18 to X=21, Y=12 to Y=15) is a dead end. Stairs are visible behind the East wall at (25, 14)/(25, 15) but inaccessible from here."
  7. Okay, so I can't reach those stairs from 1F.
  8. So I MUST be on 2F to reach the East Wing.
  9. To get from 2F Central to 2F East Wing, I MUST use the 2F Northern hallway, which requires the Northern doors at (16, 7) to be OPEN (State B).
  10. So the Mansion MUST be in State B to enter the 2F East Wing.
  11. If the Mansion is in State B, the East doors at (24, 13) are CLOSED.
  12. This means I can enter the East Wing, but I'll be blocked from the stairs by the closed doors at (24, 13).
  13. Is there a switch in the accessible part of the 2F East Wing (North of the doors) that I can use to toggle back to State A?
  14. My notes say: "Corridor South of (16, 7) leads to two switch statues at (16, 10) and (18, 10)."
  15. Are these really trap switches? Or are they the key to progressing?
  16. Let's test this theory! I need to get the Mansion into State B, go to 2F, walk through the Northern doors to the East Wing, and press one of those switches!
- The 1F switch is a statue at (2, 10)/(2, 11). I am currently at (4, 11).
- I need to stand at (3, 11) or (2, 12) to interact with it.
- Let's walk Left 1 step, then face Left and press A.