[Active Reflections]
- Strategy: Now that I have the Card Key, I will systematically clear Silph Co. from bottom to top (2F to 11F). This ensures I don't miss any items, trainers, or the ultimate path forward.
- Turn 36599 Reflection:
  - Tools: Identified a critical flaw in `execute_battle_turn` regarding `start_on_main` when the cursor is already on FIGHT (it wraps to ITEM). Avoiding its use when already on FIGHT.