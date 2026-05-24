# Scratchpad: Viridian Forest Grinding and Caterpie Capture

## Current Status:
- Turn 2216: Patrolling Viridian Forest. Gym Readiness: 80%.
- SQUIRTLE (GEMMY): Level 8, HP: 14/26. (Goal: Level 10+ for gym sweep)
- PIDGEY (BIRBIE): Level 4, HP: 18/18.
- RATTATA (REMY): Level 4, HP: 16/16.
- CATERPIE (BUGGY): Level 3, HP: 16/16. (Goal: Level 7 Metapod -> Level 10 Butterfree -> Level 12 Confusion)
- Poké Balls: 6. Antidotes: 1.

## Grinding & Encounters Log:
- Target: Caterpie (highly wanted for Butterfree evolution!).
- Location: Southernmost grass patch (rows 40-41, columns 12-15 and 18-21).
- Cumulative steps taken on grass: 13
- Encounters:
  - Encounter 1: Level 3 CATERPIE (Turn 2114/2115). Decision: Throw Poké Ball directly at full health. (Captured, Nicknamed BUGGY)
  - Encounter 2: Level 5 METAPOD (Turn 2189). Decision: Switch-trained successfully. BUGGY gained 25 EXP.
- Turn 2110: Initiated grass patrol on the southernmost grass patch at (15, 41). Creating a custom tool 'patrol_forest_grass1' to automate the 4-step loop (15,41) -> (14,41) -> (14,40) -> (15,40) -> (15,41).
- Turn 2113: Patrolled 1 cycle of patrol_forest_grass1 (4 steps). Cumulative steps: 4. No encounters yet.
- Turn 2116: Encountered Level 3 CATERPIE. Cursor at FIGHT. Choosing ITEM -> POKé BALL.
- Turn 2126: CATERPIE successfully captured on Turn 2125! Currently viewing Pokédex entry screen. Plan to nickname it BUGGY once the nickname screen loads.
- Turn 2128: Naming prompt "give a nickname to CATERPIE?" is visible on screen with cursor at YES. Pressing A to proceed to the nickname screen.
- Turn 2132: Entered the naming screen.
- Turn 2151: Successfully finalized the nickname "BUGGY" for CATERPIE! Currently on the name screen selecting ED to complete the naming phase.
- Turn 2178: Redefined 'patrol_forest_grass1' to properly read player coordinates. Player at (14, 41). Restarting patrol loop for wild encounters.

## Switch-Training Strategy:
- Lead: BUGGY (CATERPIE) in slot 1.
- Step 1: When a wild battle starts, select POKéMON.
- Step 2: Switch BUGGY out for GEMMY (SQUIRTLE).
- Step 3: Defeat the wild Pokémon with GEMMY's Tackle or Bubble.
- Step 4: BUGGY shares 50% EXP safely to reach Level 10 and evolve into Butterfree!
- Turn 2189: Encounter 2: Wild Level 5 METAPOD. Cursor at FIGHT. Choosing PKMN (Right, A) to switch BUGGY out for GEMMY.
- Turn 2195: Inside wild Metapod battle. Party select option submenu is open on GEMMY. Cursor at SWITCH. Pressing A to finalize the switch-out and bring GEMMY into battle.
- Turn 2198: GEMMY is active in battle. Metapod has raised its defense with Harden, so we are choosing BUBBLE (Down, Down, A) to deal special damage and bypass the physical defense buff.
- Turn 2203: Move selection is open, and cursor is pointing directly at BUBBLE. Pressing A to execute the attack.
- Turn 2205: Metapod is partially damaged. Cursor is at ▶FIGHT. Pressing A to open move list, then plan to select BUBBLE (Down, Down, A) to continue our assault.
- Turn 2207: Confirmed cursor is pointing directly at BUBBLE. Pressing A to execute the attack.
- Turn 2210: Metapod HP is in the red zone. Cursor is at ▶FIGHT. Pressing A to open move list to execute the final attack.