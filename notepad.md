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
- **Current Location:** Route 29 (Just outside New Bark Town).
- **Goal:** Fly to Ecruteak City.
- **Status:** Executing Fly Sequence.
- **Method:** `navigate_menu` (A -> Left -> Up -> Left -> A).
- **Notes:** Selects 'FLY', waits (interval), then moves cursor New Bark -> Cherrygrove -> Violet -> Ecruteak, then confirms.
- **Next Step:** Arrive in Ecruteak -> Search for Beasts on Route 37.

# Reflection (Turn 30528)
1. **Execution:** No deferred tasks.
2. **Hygiene:** Notepad updated. Map markers verified (New Bark Town is well-mapped).
3. **Automation:** `navigate_menu` requires a longer initial delay for map screens. The 750ms interval was likely insufficient for the Fly map to fully load and accept inputs, causing the cursor movement to be ignored and the default location (New Bark) to be selected.
4. **Goals:** Primary goal remains "Complete Pokedex". Navigation goal is "Fly to Ecruteak City".
5. **Error Analysis:** Fly attempt failed to reach target. Root cause: Input timing relative to map load.
**Corrective Action:** Increase delay after selecting 'FLY' to 2000ms before inputting directions.

## Session Information Update
- **Current Location:** New Bark Town (12, 6).
- **Goal:** Fly to Ecruteak City (Retry).
- **Status:** Opening Pokemon Menu.
- **Method:** Start -> Up x2 -> Down -> A.
- **Next Step:** Select Pidgey -> Fly -> Wait 2s -> Left, Up, Left -> A.