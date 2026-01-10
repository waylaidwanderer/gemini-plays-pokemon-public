# Long Term Notes
## Lessons Learned
- **Tool Insight:** `navigate_menu` is unreliable for small adjustments (overshoots). Use `press_buttons` for precision.
- **Menu Safety:** Always verify cursor position before confirming.
- **Efficiency:** Super Repels > Max Repels.
- **Interruptions:** Check screen text after phone calls.
- **Tool Safety:** Verify start coordinates before blind movement.

## Self-Reflection (Turn 31670)
1. **Execution:** Deferring tool fixes caused menu loops. Switching to manual `press_buttons` NOW.
2. **Notepad:** Good. Keeping "Transaction State" for immediate tracking.
3. **Map:** Markers are accurate.
4. **Automation:** `navigate_menu` is failing. Abandoning it for this menu.
5. **Goals:** Clear.
6. **Errors:** Overshooting due to tool lag/repetition. Fix: Single-step or raw button presses.

# Current Strategy
## Objectives
- **Primary:** Complete Pokedex.
- **Secondary:** Hunt Roaming Beasts (Raikou/Entei).
- **Navigation:** Goldenrod Dept. Store -> Sell Revives -> Buy Super Repels.

## Transaction State
- **Current Goal:** Buy Super Repels (Target: 10).
- **Location:** Goldenrod Dept. Store 4F.
- **Status:** Positioning to talk to 4F Clerk.
- **Action:** Pathfinding to (13, 3).
- **Reason:** Clerk is at (13, 5) behind counter. Optimal interaction spot is (13, 3) facing Down.
- **Plan:**
  1. Move to (13, 3).
  2. Interact -> Check for Super Repels.
  3. If not found, check 5F.