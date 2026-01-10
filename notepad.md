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
- **Current Location:** Ecruteak City (18, 35).
- **Goal:** Hunt Raikou/Entei.
- **Status:** Fixing Hunt Tool.
- **Method:** Redefining `hunt_cycle_ecruteak_rt37`.
- **Notes:** Previous tool failed JSON parsing and lacked commit message. Updating with manual string construction and `sleep` for transitions.
- **Time:** Start ~Turn 30680. Current 30858.
- **Next Step:** Activate `hunt_cycle_ecruteak_rt37`.