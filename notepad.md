# Long Term Notes
## Lessons Learned
- **Tool Insight:** `navigate_menu` requires `hold_ms >= 300` for Fly Map movement.
- **Menu Safety:** Start Menu cursor remembers previous position (e.g., PACK). Always verify cursor before pressing A.
- **Efficiency:** Super Repels (2.5 ¥/step) > Max Repels (2.8 ¥/step).
- **Fly Map:** Vertical movement is safer.
- **Interruptions:** Phone calls can interrupt movement patterns; always check screen text and confirm position after clearing.
- **Map Transitions:** Input queue often clears on map change. Avoid tools that cross map boundaries; handle warps manually.

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
- **Navigation:** Route 37 (Grass Area).

## Roamer Hunt Strategy
- **Session Start:** Turn 30996
- **Route:** Ecruteak (18,35) <-> Route 37 (7,0)/(8,0)
- **Method:** 2-Turn Split Loop (Manual + Tool).
  - **Turn 1:** Ecruteak -> Route 37 (Manual).
  - **Turn 2:** `rt37_hunt_return` Tool (Hunt & Return).
- **Status:** Burning steps to expire Repel (Cycle 51 - Positioning).
- **Repel:** Active (Critical 1-2 steps). Expect expiry.