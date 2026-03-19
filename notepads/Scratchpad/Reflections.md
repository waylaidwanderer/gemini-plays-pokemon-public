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
- 2F East Wing is an exhausted space and a DEAD END. (The "stairs" are a Bar Graph decoration).
- 3F South room (accessed via 1F warp stairs at 7, 10) is a DEAD END containing only a Max Potion.
- NEW PLAN: Explore 2F West area (South of Y=18, the red carpet room) or look for hidden gaps on 1F / 2F Central.
[50-Turn Reflection - Turn 42005]
- Caught in a menu loop due to overusing long `move_sequence` macros without verifying cursor memory. Going forward, I will strictly use 1-to-2 button presses for manual menu navigation or use dedicated state-aware tools.
- Tool Maintenance: Need to fix `execute_battle_turn` to not wrap to ITEM when `start_on_main` is true and the cursor is already on FIGHT.