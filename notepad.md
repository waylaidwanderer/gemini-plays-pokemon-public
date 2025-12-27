# Kanto Campaign Status
- **Location:** Cerulean Pokemon Center.
- **Current Objective:** Reach the Power Plant via Route 9.
- **Location:** Cerulean Gym (Exit).
- **Immediate Task:** Exit Gym and go North to Route 24 to find the path to Route 9.
- **Observation:** The Gym is empty. No Misty, no Rocket Grunt.
- **Lore:** The Rocket Grunt appears after the "Missing Machine Part" quest starts.
- **Strategy:**
    1. Go North to Route 24 (Golden Bridge).
    2. Look for a path East (usually involving water or a cuttable tree gap) to reach Route 9.
    3. Reach the Power Plant.

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
- **Observation:** The tree at (33, 24) is definitely uncuttable (message confirmed).
- **Strategy:** Navigating West to (15, 24) to find a path North, bypassing the Gym and ledges, aiming for the Route 24/9 connector.
- **Observation:** Direct West path on Row 24 is blocked by Cooltrainer F (21, 24) and Slowpoke (20, 24).
- **Strategy:** Circling around via Row 25 to continue West.
- **Hypothesis:** The path North to Route 24 is located at the far West edge of the map (x < 9).
- **LADDER:** Used for the bridge in Cerulean Gym. Functionally acts as a walkable FLOOR tile.
- **Observation:** Ledges at (9-11, 19) confirm the path North must be west of x=9.
- **Strategy:** Moving to x=6 to explore the unseen area and find the gap in the ledges.