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
- **Secondary:** Hunt Roaming Beasts.
- **Navigation:** Goldenrod City via Fly.

## Session Information
- **Current Location:** New Bark Town (Fly Map).
- **Goal:** Fly to Ecruteak City.
- **Status:** Navigating Fly Map (Attempt 2).
- **Method:** Navigate Menu: Left x3 (Hold 250ms).
- **Notes:** `slow_press` failed to move the map cursor (taps too short). Reverting to `navigate_menu` with `hold_ms` to ensure movement. Not pressing 'A' yet to verify destination first.