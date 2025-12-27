# Kanto Campaign Status
- **Location:** Cerulean Pokemon Center.
- **Current Objective:** Reach the Power Plant via Route 9.
- **Immediate Task:** Recovery and Cut: Exit Pokedex (B x5), Move Up x4 (to fix potential position slide), Face Right, Open Menu, Select Pokemon (Down, A), Select Belladonna (Down x4), Cut (A, A).
- **Observation:** Game State places player at (32, 28) despite being in Pokedex. This implies a sync issue or movement occurred during menuing. Moving Up x4 corrects this (safe if already at 32, 24 due to ledge).
- **Cursor Logic:** Main Menu cursor likely on Pokedex (last used). Party cursor likely on Garnet (Slot 2, last used).

# Strategic Goals
1. **Restore Power:**
   - Investigate Power Plant (East of Cerulean, end of Route 9).
   - Fix the Generator (likely requires a part).
2. **Wake Snorlax:**
   - Requires Poke Flute functionality (Radio expansion card?).
   - Requires Power restored.
3. **Collect Kanto Badges:**
   - [x] Vermilion (Thunder)
   - [x] Saffron (Marsh)
   - [ ] Cerulean (Cascade) - Misty?
   - [ ] Celadon (Rainbow)
   - [ ] Fuchsia (Soul)
   - [ ] Pewter (Boulder)
   - [ ] Viridian (Earth)
   - [ ] Cinnabar (Volcano)

# Discovery Log
- **Cerulean City:**
  - **Fisherman:** Confirmed Power Plant is near end of Route 9.
  - **Cooltrainer M:** Mentions trainers at Cerulean Cape (Route 25).
  - **Gym:** Located at (30, 23).
  - **Bike Shop:** Found sign.
- **Saffron City:**
  - Magnet Train station exists but no power.
  - Copycat girl (lost doll?).

# Tile Mechanics
- **FLOOR:** Standard walkable tile.
- **WALL:** Impassable tile.
- **LEDGE_HOP_DOWN:** One-way jumpable ledge (South).
- **TALL_GRASS:** Wild Pokemon encounters.
- **WARP_CARPET_DOWN:** Transition to map below.
- **DOOR:** Warp to interior.
- **WATER:** Requires Surf.
- **Observation:** Tried to move past tree at (33, 24) but failed. Tree is still there. Retrying Cut action.