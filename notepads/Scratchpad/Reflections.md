[Active Reflections]
- Strategy: Now that I have the Card Key, I need to systematically unlock the electronic doors on each floor to find the path forward. I'll start by unlocking the doors here on 9F.
- Turn 36599 Reflection:
  - Tools: Identified a critical flaw in `execute_battle_turn` regarding `start_on_main` when the cursor is already on FIGHT (it wraps to ITEM). Avoiding its use when already on FIGHT.