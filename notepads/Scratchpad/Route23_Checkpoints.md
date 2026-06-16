# Route 23 Checkpoints
## Chronological Investigation Log

### The Eastern Dead-End Discovery
- **Hypothesis**: Walking east along Row 44 from (12, 44) will bypass the central rock barrier and reveal a pathway north.
- **Methodology & Test (Turns 97003-97019)**:
  - Walked east 5 steps from (12, 44) to (17, 44).
  - Observed the tiles in Columns 13 to 19.
  - **Results**: Row 43 is a solid rock wall of TYPE_2889 extending across all Columns (13 to 19). The eastern edge (Column 20+) is blocked by dense forest trees. There is no pathway north on the east side of Row 44.
  - **Conclusion**: The eastern side is a complete dead end. We must backtrack to the western side of the map.
  - **Backtracking**: Returned to (12, 48) on Turn 97022 by moving Left 5, Down 4.

### The Western Pathway Investigation
- **Hypothesis**: The western side of the map (Columns 0 to 9) near Row 48 contains the shoreline to a body of water that can be surfed north to bypass the Row 43 rock wall.
- **Methodology (Active)**:
  - Walk West along Row 48 from (12, 48) to check the left side of the map and find the shoreline.
  - **Turn 97026**: Initiating movement. Row 48 is verified passable (TYPE_3fe2) from Column 12 down to Column 8.

- **Bypassing the Row 43 Barrier (Turns 97031-97049)**:
  - Backtracked West along Row 48 to (2, 48).
  - Discovered that Columns 6 and 7 form a completely unblocked, 2-tile wide grassy vertical corridor (TYPE_3fe2) running from Row 48 to Row 44.
  - Moved to (6, 44) facing Up on Turn 97049.
  - **Results**: The vertical Column 6/7 corridor is open green grass on land, continuing North through Row 43, 42, 41, and 40 (all TYPE_3fe2), bypassing the solid rock walls of TYPE_2889 present on either side. There is no water yet at this height on Columns 6 and 7.

- **The Final Earth Badge Checkpoint (Turn 97089)**:
  - Positioned at (4, 36) directly below the guard at (4, 35) on land.
  - Spoke to the guard by pressing A.
  - **Dialogue**: "You can pass here only if you have the EARTHBADGE! Oh! That is the EARTHBADGE! OK then! Please, go right ahead!"
  - **Results**: Checkpoint successfully verified and cleared! The guard remains at (4, 35), but the vertical path north on Columns 3 and 5 are completely open land (all TYPE_3fe2 passable grass) leading north to Row 32, meaning we do not need to Surf.

### Victory Road Preparation and PC Box Action Plan
- **Current Box Status**: Box 1 is currently at 18/20. To prevent a soft-lock where we cannot catch any new wild Pokémon in Victory Road or beyond, we must swap boxes before proceeding with any captures.
- **Current Bag Optimization**: Teaching TM14 (Blizzard) to GEMMY (Blastoise) to replace BITE. This is in progress on Turn 97117.
- **Action Plan**:
  1. Complete teaching TM14 Blizzard to Blastoise.
  2. Navigate north to Row 31 and take the warp at (4, 31) to enter Victory Road 1F.
  3. Once Victory Road 1F is successfully entered (marking the checkpoint), use DIG to immediately warp back to the Viridian City Pokémon Center.
  4. At the Viridian Pokémon Center:
     - Heal the party at Nurse Joy's counter (restoring fainted BIRBIE and GEMMY's HP/PP).
     - Access Bill's PC to change the active box from Box 1 (18/20) to Box 2 (0/20).
     - Withdraw TM26 (Earthquake) and TM29 (Psychic) from PC Storage.
     - Teach TM26 (Earthquake) to GEMMY (Blastoise) in place of DIG for ultimate endgame ground STAB/coverage.
     - Teach TM29 (Psychic) to BUGGY (Butterfree) to maximize special attack coverage.
  5. Ride the bicycle back up Route 23 (since all badge guards are permanently cleared and no longer intercept us, this run is incredibly fast and takes less than 70 turns).
  6. Re-enter Victory Road 1F fully healed, optimized, and with a fresh empty PC box!