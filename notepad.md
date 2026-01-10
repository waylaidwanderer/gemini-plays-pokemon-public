# Long Term Notes
## Lessons Learned
- **Tool Insight:** `navigate_menu` requires `hold_ms >= 300` for Fly Map movement.
- **Menu Safety:** Start Menu cursor remembers previous position (e.g., PACK). Always verify cursor before pressing A.
- **Efficiency:** Super Repels (2.5 ¥/step) > Max Repels (2.8 ¥/step).
- **Fly Map:** Vertical movement is safer.
- **Interruptions:** Phone calls can interrupt movement patterns; always check screen text and confirm position after clearing.
- **Map Transitions:** Input queue often clears on map change. Avoid tools that cross map boundaries; handle warps manually.
- **Tool Safety:** Always verify exact start coordinates before calling blind movement tools (e.g., `rt37_hunt_return` requires Rt 37 (8,0)).

## Legendary Beast Hunt Strategy
- **Target:** Raikou (#238) & Entei (#239).
- **Method:** Blind Hunt Loop (Route 37 <-> Ecruteak).
- **Tactics:** Rt 37 Grass -> Wiggle -> Return -> Repeat.
- **Mechanic:** Repel blocks wild Pokemon (Lv15) but allows Roamers (Lv40).

## Tile Mechanics
- GRASS: Traversable, encounters.
- FLOOR/DOOR/STAIRS: Traversable.
- WALL/OBSTACLES: Impassable.
- WATER: Surfable.

# Current Strategy
## Objectives
- **Primary:** Complete Pokedex.
- **Secondary:** Hunt Roaming Beasts (Raikou/Entei).
- **Navigation:** Route 35 Gatehouse -> Goldenrod.

## Roamer Hunt Strategy
- **Session Start:** Turn 30996 (Current: 31643)
- **Status:** Selecting SELL Option.
- **Goal:** Enter SELL Menu.
- **Action:** Pressing Down (Step 1 of 2).
- **Reason:** System blocks mixed input types in `press_buttons`. Splitting "Down" and "A" into separate turns to ensure precision and avoid re-entering BUY menu.
- **Current Selection:** BUY.
- **Next:** Verify cursor on SELL -> Press A.