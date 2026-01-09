# Lessons Learned
- **Tool Insight:** `navigate_menu` requires `hold_ms` >= 300 for Fly Map.
- **Efficiency:** Super Repels (2.5 ¥/step) are cheaper than Max Repels (2.8 ¥/step).

# Current Status
- **Location:** Mahogany Town.
- **Activity:** Flying to Ecruteak City.
- **Time Started:** Turn 29710.
- **Inventory:** 10 Super Repels.
- **Objective:** Fly to Ecruteak City (Route 37) to hunt Raikou/Entei.
- **Status:** Super Repel active. Exiting menu to begin hunt.
- **Next Steps:**
  1. Exit Menu (B x4).
  2. Call `execute_hunt_routine` to toggle between Route 37 and Ecruteak.
- **Hunt Logic:**
  - Route 37 Grass encounters are ~Lv 16.
  - Gyarados is Lv 36.
  - Super Repel blocks wild Pokemon < Lv 36.
  - Raikou/Entei are Lv 40.
  - Result: Only Raikou/Entei (and maybe very high level wilds if any exist, but likely not) will appear.
- **Exploration Queue:**
  - **Mahogany Town:** West edge (x=0-2) and East edge (x=15, y=3) unseen tiles. Investigate later.
  - **Ecruteak City:** Northern edges and Barrier Station area (27, 11). Investigate later.

# Legendary Beast Hunt Strategy
- **Target:** Raikou (#238) & Entei (#239).
- **Method:** Blind Hunt Loop (Route 37 <-> Ecruteak).
- **Tactics:** Enter Rt 37 -> Grass (Down x2, Wiggle) -> If none, Return to Ecruteak -> Repeat.

# Tile Mechanics
- GRASS: Traversable, encounters.
- FLOOR/DOOR/STAIRS: Traversable.
- WALL/OBSTACLES: Impassable.
- WARP_CARPET: Transition.
- WATER: Surfable.
- **Phone Call (Turn 29598):** Wade (Route 31) found Berries.
- **Phone Call (Turn 29712):** Gaven (Route 26) wants a rematch.