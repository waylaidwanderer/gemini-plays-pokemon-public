# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Status
- **Location**: Route 38 (Map 1_12).
- **Goal**: Reach Olivine City.
- **Party**: Basil (Lead, Level 10), Garnet (Level 35), etc.
- **Health**: All Healthy.

### Tasks
- **Immediate**: Traverse Route 38. Switch-train Basil.
- **Short-term**: Reach Olivine City.
- **Long-term**: Get badges, beat Elite Four.

### Notes
- **Mechanics**:
  - Battle menu is a vertical list. Cursor memory is inconsistent. Use `Up` x3 to reset to top before selecting moves.
  - Fog Badge allows Surf out of battle.
- **Mistakes**:
  - Used Dig on Flying type (Hoppip).
  - Struggled with menu navigation for switching.
- **Route 38**:
  - Beware of poison.
- **Status**: Battle vs Bird Keeper Toby (Doduo).
- **Party**: Basil (FNT), Garnet (Lv 35), Topaz (Lv 15).
- **Task**: Win battle (Use Flame Wheel, NOT Ground moves) -> Return to Ecruteak.
- **Note**: Mud-Slap/Dig (Ground) have NO EFFECT on Flying types. Used Mud-Slap by mistake.
- **Strategy**: Manual move selection (A -> Down -> A) to ensure Flame Wheel (Slot 4) from Mud-Slap (Slot 2).
- **Battle Error**: `battle_select_move` failed to select Flame Wheel (Slot 4) multiple times, selecting Dig (Slot 1) instead.
- **Correction**: Will use manual button presses for move selection to guarantee Flame Wheel.
- **Situation**: Garnet is using Dig (Ground) on Flying type. It will fail. Next turn, MUST select Flame Wheel manually.
- **Mechanics Update**: The battle move menu is a **vertical list (1x4)**, not a 2x2 grid. 
- **Tool Failure**: `battle_select_move` assumes a grid (Down -> Right for Slot 4), which fails on a list (results in Slot 2).
- **Fix**: Must use manual `Down` presses to navigate moves. Slot 4 requires 3 `Down` presses from the top.