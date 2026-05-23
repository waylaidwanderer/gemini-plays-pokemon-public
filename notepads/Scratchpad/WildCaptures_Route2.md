# Scratchpad: Wild Captures and Leveling Goals

## High-Level Strategy:
- Goal: Capture additional wild Pokémon (Pidgey, Rattata, Nidoran, etc.) to build our team.
- Goal: Level up SQUIRTLE (GEMMY) and new team members to prepare for Pewter City Gym.
- Goal: Travel north through Route 2 towards Viridian Forest.

## Live Status:
- Turn 904: SQUIRTLE is at 21/24 HP (Level 7).
- Money: ¥1075.
- Inventory: 10 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Route 2 (Map 0_13) at (8, 71) facing Up.

## Live Route Planning:
- From (8, 71), walk Up 4 steps to (8, 67) to proceed north.
- From (8, 67), look for wild grass patches to capture Pokémon.

## Summary of Journey:
- Turns 809-848: Entered Viridian Mart; purchased 10 Poké Balls and 1 Antidote.
- Turns 849-871: Bypassed Trainer School and moved Up Column 19 to (19, 12).
- Turns 872-895: Navigated past the old man at (19, 5) and moved Up Column 18 to transition to Route 2 (Map 0_13) at (8, 71).
- Turn 907: SQUIRTLE is at 21/24 HP. Player is at (8, 71) facing Up on Route 2 (Map 0_13).
  - Visual Verification: `<CurrentScreen turn="907">` shows Column 8 from Row 71 to Row 67 is completely clear path (TYPE_3fe2).
  - Movement Plan: Move Up 4 steps along Column 8 to (8, 67).
  - Testing Methodology: Execute `["Up", "Up", "Up", "Up"]` and verify that the player's coordinate becomes (8, 67) on Turn 908.
Turn 910: Successfully reached (8, 67) on Route 2 (Map 0_13). SQUIRTLE is at 21/24 HP.
Current visual analysis:
- Column 8 is clear going up.
- Row 67 has red flowers/tall grass to the left: (7, 67), (6, 67), (5, 67).
- Let's test if moving Left into (7, 67) triggers wild encounters.
- Let's move Left 1 step to (7, 67).
- Expected outcome: Player is at (7, 67), potentially triggering a wild encounter if (7, 67) is indeed tall grass.
Turn 919: Standing on (8, 67) facing Right.
Proof of Work:
- Verified that Column 8 and Column 9 contain gray vertical tufts, which correspond visually to tall grass.
- Verified that Columns 10 and 11 contain green grass (no tufts), which is a clear path.
- Verified that Columns 4, 5, 6, and 7 on Rows 66 and 67 contain red flowers, which represent non-tall-grass decoration.
- Plan: Step Right to (9, 67) to continue searching for wild encounters.
Turn 922: Standing on (9, 67) facing Right.
Visual verification of Route 2 Tall Grass Patch boundaries:
- Row 67: (8, 67) and (9, 67) (Tall Grass).
- Row 66: (8, 66) and (9, 66) (Tall Grass).
- Row 65: (6, 65) to (9, 65) (Tall Grass). (5, 65) is an impassable Cut tree (TYPE_2889).
- Row 64: (5, 64) to (9, 64) (Tall Grass).
- Row 63: (8, 63) and (9, 63) (Tall Grass).
Total tall grass area is extensive, offering ample opportunities for encounters.
Plan: Move Up to (9, 66) to continue wild encounter search.
Turn 927: Standing on (9, 66) facing Up. SQUIRTLE is at 21/24 HP.
Current plan: Move Up to (9, 65) to continue searching for wild encounters in the tall grass.
Testing Methodology:
- Step Up to (9, 65).
- Verify player's position is (9, 65) on Turn 928, and check if a wild battle is triggered.