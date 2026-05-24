# Scratchpad: Viridian Forest Grinding and Caterpie Capture

## Current Status:
- Turn 2106: Entered Viridian Forest.
- SQUIRTLE (GEMMY): Level 8, HP: 14/26.
- PIDGEY (BIRBIE): Level 4, HP: 18/18.
- RATTATA (REMY): Level 4, HP: 16/16.
- Poké Balls: 7. Antidotes: 1.

## Grinding & Encounters Log:
- Target: Caterpie (highly wanted for Butterfree evolution!).
- Location: Southernmost grass patch (rows 40-41, columns 12-15 and 18-21).
- Cumulative steps taken on grass: 9
- Encounters:
  - Encounter 1: Level 3 CATERPIE (Turn 2114/2115). Decision: Throw Poké Ball directly at full health.
- Turn 2110: Initiated grass patrol on the southernmost grass patch at (15, 41). Creating a custom tool 'patrol_forest_grass1' to automate the 4-step loop (15,41) -> (14,41) -> (14,40) -> (15,40) -> (15,41).
- Turn 2113: Patrolled 1 cycle of patrol_forest_grass1 (4 steps). Cumulative steps: 4. No encounters yet.
- Turn 2116: Encountered Level 3 CATERPIE. Cursor at FIGHT. Choosing ITEM -> POKé BALL.
- Turn 2126: CATERPIE successfully captured on Turn 2125! Currently viewing Pokédex entry screen. Plan to nickname it BUGGY once the nickname screen loads.
- Turn 2128: Naming prompt "give a nickname to CATERPIE?" is visible on screen with cursor at YES. Pressing A to proceed to the nickname screen.
- Turn 2132: Entered the naming screen.
- Turn 2151: Successfully finalized the nickname "BUGGY" for CATERPIE! Currently on the name screen selecting ED to complete the naming phase.
- Turn 2159: Naming phase successfully concluded. Starting the training phase for BUGGY. Plan to put BUGGY in slot 1 to initiate switch-training. Opening overworld menu.
- Turn 2164: Start menu is open. Cursor at POKéDEX. Pressing Down to move to POKéMON, then A to enter the party menu.
- Turn 2166: Party menu is open. Cursor at GEMMY (SQUIRTLE). Pressing A to open the Pokémon option menu.
- Turn 2168: Option menu is open on GEMMY. Cursor at STATS. Pressing Down to select SWITCH and A to confirm.
- Turn 2170: Swap mode activated ("Move POKéMON where?"). Cursor on GEMMY (slot 1). Pressing Down 3 times to move to BUGGY (slot 4), then A to complete the swap.
- Turn 2173: Successfully verified BUGGY is now in slot 1 leading the party. Plan to press B twice to close the menus and resume patrolling for switch-training.
- Turn 2178: Redefined 'patrol_forest_grass1' to properly read player coordinates. Player at (14, 41). Restarting patrol loop for wild encounters.