# Long Term Notes
## Lessons Learned
- **Tool Insight:** `navigate_menu` requires `hold_ms >= 300` for Fly Map movement.
- **Menu Safety:** Start Menu cursor remembers previous position (e.g., PACK). Always verify cursor before pressing A.
- **Efficiency:** Super Repels (2.5 ¥/step) > Max Repels (2.8 ¥/step).
- **Fly Map:** Vertical movement is safer.

## Legendary Beast Hunt Strategy
- **Target:** Raikou (#238) & Entei (#239).
- **Method:** Blind Hunt Loop (Route 37 <-> Ecruteak).
- **Tactics:** Rt 37 Grass -> Wiggle -> Return -> Repeat.

## Tile Mechanics
- GRASS: Traversable, encounters.
- FLOOR/DOOR/STAIRS: Traversable.
- WALL/OBSTACLES: Impassable.
- WATER: Surfable.

# Current Strategy
## Objectives
- **Primary:** Complete Pokedex.
- **Secondary:** Hunt Roaming Beasts (Raikou/Entei).
- **Navigation:** Route 37 (Grass Area).

## Session Information
- **Current Location:** Ecruteak City (17, 35).
- **Goal:** Hunt Raikou/Entei.
- **Status:** Re-entering Route 37.
- **Method:** `press_buttons` (Down).
- **Notes:** Hunt loop check complete. No encounter. Repel active. Returning to Route 37.
- **Next Step:** Enter Route 37 -> Run `hunt_check_route37`.