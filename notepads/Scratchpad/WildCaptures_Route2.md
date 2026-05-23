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