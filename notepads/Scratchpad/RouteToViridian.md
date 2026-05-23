# Scratchpad: Journey back to Viridian City
Started: Turn 521
Goal: Go from Pallet Town (13, 6) to Viridian City Poké Mart to buy Poké Balls.

## Live Route Planning:
1. Pallet Town (13, 6) to Route 1 Entrance (10, 0)
   - Route: Left 3 steps to (10, 6), then Up 6 steps to (10, 0).
   - Expected position after Left 3, Up 6: Route 1 at (10, 35) or similar.
2. Route 1 Navigation
   - We must go north through Route 1.
   - We need to watch out for wild battles and manage SQUIRTLE's health (12/24 HP).
   - We have 1 POTION in case SQUIRTLE gets low on HP.
   - Avoid jumping south over ledges since we want to go north.

## Turn Log:
- Pallet Town to Route 1 Phase (Turns 521-557): Successfully exited Pallet Town (13, 6) through northern grass exit (10, 0) and traveled up Route 1 to bypass the row 27 ledge by navigating Left to Column 8 at (8, 31) with Squirtle at 12/24 HP. Archiving completed turn logs in 'Archive/RouteToViridian_Turns521_557'.
- Turns 567-630: Successfully bypassed Row 27 and Row 19 obstacles on Route 1. Navigated north via Column 8 to (8, 27), crossed to Column 12 to pass Row 23, and moved to Column 14 at (14, 16) to prepare for bypassing the Row 13 barrier with Squirtle at 12/24 HP. Full history archived in 'Archive/RouteToViridian_Turns521_557'.
- Turn 633: Reached (14, 16) facing North. SQUIRTLE's health is 12/24 HP. Prepared to proceed north through the Column 14 grass passage (Y=15 to Y=12).
- Turn 634: Standing at (14, 16) facing North. SQUIRTLE's health is 12/24 HP. Checked surrounding tiles: Column 14 is open and clear of the Clerk NPC (who has moved to (17, 13)). Prepared to move Up 4 steps to (14, 12) and then Left 1 step to (13, 12).
- Turn 651: Resumed at (14, 16) facing North. SQUIRTLE is at 12/24 HP. The Clerk NPC is visually at (14, 13), but RAM tracker says they moved to (15, 13). I will test this by moving Up 1 step to (14, 15) and observing the NPC's position and checking if we get a wild encounter.
- Turn 660: Verified on `<CurrentScreen turn="660">` that the Clerk is at (17, 13). This leaves Column 14 completely clear. Our exact northbound path to bypass the Row 13 stone blocks:
  1. Move Up 1 step to (14, 15) [tall grass, chance of wild battle]
  2. Move Up 1 step to (14, 14) [tall grass, chance of wild battle]
  3. Move Up 1 step to (14, 13) [tall grass, chance of wild battle]
  4. Move Up 1 step to (14, 12) [tall grass, chance of wild battle]
  5. Move Left 4 steps to (10, 12) [clear path]
  I will proceed with the first step (Up) now. If we enter a battle, I will resolve it before continuing.
- Turn 663: Successfully arrived at (14, 15) facing North. SQUIRTLE is at 12/24 HP. No wild battle occurred. The Clerk NPC has moved and is visually at (14, 13). This currently blocks Column 14 at Row 13. I will move Up 1 step to (14, 14) to get closer and see if the NPC moves away on the next turn, or if we need to adjust our path.
- Turn 666: The Clerk NPC moved back to (14, 13) during the last turn transition, blocking Column 14.
  I will adapt my route to use Column 15 to bypass the Clerk:
  1. Move Right 1 step to (15, 15) [tall grass, chance of wild battle]
  2. Move Up 1 step to (15, 14) [tall grass, chance of wild battle]
  3. Move Up 1 step to (15, 13) [tall grass, chance of wild battle]
  4. Move Up 1 step to (15, 12) [tall grass, chance of wild battle]
  5. Move Left 5 steps to (10, 12) [clear path]
  I will start by moving Right 1 step to (15, 15).
- Turn 668: On `<CurrentScreen turn="668">`, the Clerk NPC is at (15, 13) (the green hat is at (15, 12) and torso is at (15, 13)). This leaves Column 14 completely clear! I will resume the original route of moving Up through Column 14:
  1. Move Up to (14, 14) [tall grass, chance of wild battle]
  2. Move Up to (14, 13) [tall grass, chance of wild battle]
  3. Move Up to (14, 12) [tall grass, chance of wild battle]
  4. Move Left to (10, 12) [clear path]
  Starting by moving Up 1 step to (14, 14).
- Turn 669: On `<CurrentScreen turn="669">`, the Clerk NPC appears visually at (15, 13) but RAM says they moved to (14, 13). I will move Up 1 step to (14, 14) [tall grass, chance of wild battle] to test the path and see the next state.