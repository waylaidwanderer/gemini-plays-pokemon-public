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
- **Status**: Battle vs Bird Keeper Toby (Part 2).
- **Party**: Basil (FNT), Garnet (Lv 35), Topaz (Lv 15).
- **Task**: Win battle -> Return to Ecruteak to heal Basil.
- **Battle Mechanics**:
  - Menu remembers last selection.
  - Menu WRAPS (Down from Slot 4 -> Slot 1).
  - Current cursor: Slot 3 (Smokescreen).
- **Strategy**: Use `battle_select_move_smart` with `current_slot=3` next turn.
- **Current Action**: Advance text (Enemy turn pending).