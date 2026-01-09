# Current Status
- Location: Roaming (Route 37 <-> Ecruteak).
- Activity: Hunting Raikou & Entei.
- Party: Gyarados (Lv 36) Lead for Repel Trick. Lugia in party.
- **Hunt Session Start:** Turn 28662.

# Legendary Beast Hunt Strategy
- **Target:** Raikou (#238) & Entei (#239).
- **Method:** Blind Hunt Loop (Route 37 Grass <-> Ecruteak City).
- **Tactics:**
  1. Enter Route 37 from Ecruteak.
  2. Run into grass (Down x2, Left/Right wiggle).
  3. If no encounter, run back to Ecruteak (Up).
  4. Repeat.
- **Items:** Max Repel ACTIVE.

# Tile Mechanics
- GRASS: Traversable. Potential encounters.
- FLOOR: Traversable. Safe.
- WARP_CARPET: Map transition.
- WALL: Impassable.
- WATER: Surfable.
- HEADBUTT_TREE: Impassable. Interaction possible.
- LEDGE_HOP_DOWN: One-way traversable (down).
- DOOR: Traversable (warp).

# Hunting Status
- **Goal:** Blind Hunt Raikou & Entei (Lv 40) on Route 37.
- **Method:** Loop `execute_hunt_routine` (Route 37 <-> Ecruteak City).
- **Active Effect:** Max Repel (Active).
- **Lead:** Gyarados (Lv 36) - Repel Trick Active.
- **Notes:** Hunting loop active. Route 37 is SOUTH of Ecruteak. Cycling Down (to Route 37) and Up (to Ecruteak).
- **Reflection (Turn 29285):** Max Repel wore off. Currently in Pack menu. Applying Max Repel. Hunt loop suspended briefly for maintenance. Routine 'execute_hunt_routine' was updated and is ready.
- **Self-Assessment (Turn 29285):**
  1. **Execution:** Immediate. Addressing Repel expiration now.
  2. **Notepad:** Good. Keeping track of hunt status.
  3. **Map:** Markers are sufficient for this loop.
  4. **Automation:** `execute_hunt_routine` fixed (deeper grass).
  5. **Goals:** Clear.
  6. **Errors:** Fixed previous grass-check error. No new errors.