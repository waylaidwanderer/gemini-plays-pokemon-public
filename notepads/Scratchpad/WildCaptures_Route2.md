# Scratchpad: Wild Captures and Leveling Goals

## High-Level Strategy:
- Goal: Capture additional wild Pokémon (Pidgey, Rattata, Nidoran, etc.) to build our team.
- Goal: Level up SQUIRTLE (GEMMY) and new team members to prepare for Pewter City Gym.
- Goal: Travel north through Route 2 towards Viridian Forest.

## Live Status:
- Turn 875: SQUIRTLE is at 21/24 HP (Level 7).
- Money: ¥1075.
- Inventory: 10 Poké Balls, 1 Antidote, 1 Town Map.
- Location: Viridian City (Map 0_1) at (19, 12) facing Up.

## Live Route Planning:
- From (19, 12), move Up 4 steps to (19, 8) to clear the Gym building.
- From (19, 8), go north to the exit gatehouse (usually around Row 0 to 4).

## Summary of Journey:
- Turns 809-848: Entered Viridian Mart and purchased 10 Poké Balls and 1 Antidote.
- Turns 849-852: Exited Poké Mart to (29, 20).
- Turns 853-860: Moved Left 9 steps to (20, 20).
- Turns 861-865: Bypassed Trainer School by moving Left to Column 19 and Up to (19, 16).
- Turns 866-871: Moved Up 4 steps along Column 19 to (19, 12).
- Turn 884: SQUIRTLE is at 21/24 HP. Player is at (19, 8) facing Up in Viridian City (Map 0_1).
  - Visual Verification: `<CurrentScreen turn="884">` shows that the old man NPC (SPRITE_578e) has moved to (19, 5), blocking our straight-north path on Column 19.
  - Bypass Plan: Move Left 1 step to (18, 8), then walk Up 4 steps to (18, 4) along the completely clear Column 18.
  - Testing Methodology: Execute `["Left", "Up", "Up", "Up", "Up"]` and verify that the player's coordinate becomes (18, 4) on the next turn.
- Turn 889: SQUIRTLE is at 21/24 HP. Player is at (19, 4) facing Up in Viridian City (Map 0_1).
  - Visual Verification: `<CurrentScreen turn="889">` shows (19, 1) is TYPE_2889 (blocked by gatehouse wall), but Column 18 is completely clear of obstacles (TYPE_3fe2) up to Row 0.
  - Navigation Plan: Move Left 1 step to (18, 4), then Up 4 steps to (18, 0) to exit the city.
  - Testing Methodology: Execute `["Left", "Up", "Up", "Up", "Up"]` and verify the coordinates and map transition on Turn 890.
- Turn 894: SQUIRTLE is at 21/24 HP. Player is standing at (18, 0) facing Up on Map 0_1 (Viridian City).
  - Visual Verification: `<CurrentScreen turn="894">` confirms we are at (18, 0) facing Up. The tiles above us (Rows -1, -2, etc. representing Route 2) are clear road.
  - Movement Plan: Move Up 1 step to trigger the transition into Route 2 (Map 0_13).
  - Testing Methodology: Execute `["Up"]` and verify that the map ID changes to Map 0_13 in the game state on Turn 895.