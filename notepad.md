# Kanto Campaign Status
- **Location:** Cerulean Pokemon Center.
- **Current Objective:** Reach the Power Plant via Route 9.
- **Location:** Cerulean Gym (Exit).
- **Immediate Task:** Enter and explore the house at (7, 15).
- **Observation:** Found a house with a Youngster in the backyard. Access to the backyard is likely through this house.
- **Strategy:** Check if the house has a back door to reach the Youngster and the area behind.
- **Hypothesis:** This path leads to Route 24/25.

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
- **Observation:** Found a gap in the ledges at x=6 (Row 19).
- **Strategy:** Heading North through (6, 19) to reach Route 24.