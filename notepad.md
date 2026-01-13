# Roamer Hunt Strategy
- **Current Operation:**
  1.  **Shuffle:** Use `cycle_roamer_hunt_route35` (defined Turn 36631) to enter/exit gatehouse and check map.
  2.  **Check:** If Roamer is on Route 35, Hunt.
  3.  **Repeat:** If not, repeat shuffle.
- **Status:** Clearing Phone Call (Wade).
- **Roamers:** Spotted on Route 42, 31, 46 (Turn 36631).
- **Hunt Session:** Started ~Turn 36369. Current: 36633.
- **Resources:** 16 Repels.

# Reflection & Strategy Notes (Turn 36288)
- **Menu Navigation:** The Pokegear cursor remembers its last position. To reliably open the Map, use `Left, Left` (forces cursor to BACK) then `Right` (selects MAP).
- **Roamer Behavior:** Observed persistent clustering on Route 38 and 44 for ~30 turns. If this persists for another 20 turns, consider relocating to Ecruteak/Route 37 to disrupt the pattern.
- **Shuffle Timing:** Warp transitions require ~5000-6000ms sleep in tools to be safe.
- **Session Stats:** Start: Turn 34090. Current: 36315.

# Tile Mechanics
- **Ledge Hop:** One-way jump over ledges.
- **Headbutt Tree:** Can be shaken for Pokemon.
- **WARP_CARPET_LEFT:** Map transition tile.

# Hall of Fame Entry
- **Achievement:** **CHAMPION OF THE JOHTO LEAGUE!**
- **Date:** Turn 33314
- **MVP:** Muscle (Machoke) Lv88.

# Completed Objectives
- **Pewter to Saffron Transit:** Completed via Mt. Moon & Magnet Train.
- **Observation:** Walked ~20 steps on Route 38 with Repel (Lv36 Lead) and found nothing. Assuming Roamers are not present. Shuffling.
- **Observation:** Roamers confirmed on Route 42 and 44 (East). Shuffling again.
- **Event:** Received phone call from Cooltrainer Gaven (Turn 36326).

- **Bug Report:** Fly Map cursor stuck on Silver Cave (Turn 36476). Cannot Fly to Goldenrod. Walking instead.
- **Tool Note:** `pathfind` has a 50-step safety limit. For long-distance travel (e.g. National Park traversal), break the path into intermediate waypoints (approx 15-20 steps away).
- **Resupply Plan:** In Goldenrod Dept Store 2F. Top Clerk checked (No Super Repels). Buying bulk Standard Repels from Bottom Clerk instead.
- **Shop Data:** 
  - 2F Bottom Clerk (13,6): Poke Ball, Great Ball, Escape Rope, Repel, Revive, Full Heal, Poke Doll, Flower Mail.
  - 2F Top Clerk (13,5): Potion, Super Potion, Antidote, Parlyz Heal, Awakening, Burn Heal, Ice Heal.
  - Conclusion: No Super Repels available. Using Standard Repels.
- **Resupply Plan:** Mission Accomplished. Bought 17 Repels. Current Inventory: 17 Repels.
- **Next Step:** Exit Goldenrod, Check Pokegear, Hunt Roamers.
- **Status:** In Pack Menu (Items Pocket).
- **Action:** Highlighting Repel.
- **Hypothesis:** Repel is the last item acquired, so `Up` x2 from top should wrap to Cancel then Repel.
- **Strategy:** "Blind Shuffle"
  1. Apply Repel.
  2. Run in grass (Route 35) for ~20 steps.
  3. If no encounter, enter/exit Gatehouse (Shuffle).
  4. Repeat.
- **Menu Mechanics:** Pack Menu (Items) does NOT wrap from Top to Bottom using `Up`.
- **Action:** To reach new items (Repel), scroll DOWN to bottom.
- **Sequence:** `B` (Exit sub-menu) -> `Down` x 15 (Hit bottom) -> `Up` (Select last item/Repel) -> `A`.
- **Status:** Repel Applied (Turn 36576).
- **Next:** Exiting menu. Running in Route 35 grass (south of gatehouse) to check for Roamers.
- **Contingency:** If no encounter after ~20 steps, shuffle via Gatehouse.
- Status: Cycling Roamers (Cycle 37).
- Observation: Shuffle worked! Roamers moved to Route 42, 31, 46. None on 35.
- Action: Executing `cycle_roamer_hunt_route35`.