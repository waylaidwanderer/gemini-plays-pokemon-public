# Strategic Notes
## Objectives
- **Primary:** Reach Indigo Plateau (Money Farming Loop).
- **Secondary:** Defeat Elite Four.
- **Tertiary:** Hunt Roamers (Raikou/Entei) - *Paused*.

## Current Task: Traverse Victory Road 3F (Final Floor)
- **Location:** Victory Road 3F (ID: 3_91) at (17, 10).
- **Goal:** Reach Exit to Indigo Plateau at (13, 5).
- **Route:** `(17, 10) -> West to (12, 10) -> North to (12, 6) -> (13, 5)`.
- **Reasoning:**
  - Encountered wild Pokemon at (17, 10).
  - Need to flee and continue West to the exit corridor.

## Reflection (Turn 32967)
- **Execution:** No deferred tasks identified in the last 50 turns.
- **Hygiene:** Notepad sections are relevant. Map markers are active and accurate.
- **Tools:** Current navigation challenges are due to map topology (vertical stacking), not tool deficiency. Standard `navigate` is sufficient with manual warp handling.
- **Goals:** Primary goal (Indigo Plateau) remains valid. Strategy shifted from 2F West (blocked/bugged ledge) to 1F Southeast (exploration).
- **Lesson:** Victory Road (3_91) is a single map with stacked floors. Navigation tools see it as one continuous area but cannot pathfind through warps automatically. I must manually step off and onto ladders to transition between floors.