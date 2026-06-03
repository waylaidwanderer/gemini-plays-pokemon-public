# Safari Zone West Exploration Scratchpad (Run 10 Planning)
- **Objective**: Retrieve Gold Teeth and HM03 Surf from the Secret House in Safari Zone West (Map 0_219).
- **Run 10 Start Turn**: Turn 48104 (Start Time: Tuesday, June 2, 2026).

## Current Status
- Standing at (17, 6) in Safari Zone East (Map 0_217) on Turn 48253. Exactly 383 remaining steps (500 minus 117 overworld steps taken). Run 10 is in progress!

## Chronological Exploration History & Discoveries (Archive):
- **Safari Zone East (Map 0_217) Exit Route Plan (ARCHIVED - COMPLETED)**: 
  - Successfully completed on Turn 47713. Bypassed central plateau using ground Row 5, transitioning with 0 wild encounters.
- **Safari Zone North (Map 0_218) Active Progress & Route (ARCHIVED - COMPLETED)**: 
  - Walked West along Row 31 (a grass-free, open horizontal corridor) from Column 39 to Column 28.
  - Walked Up onto the Western Plateau via the stairs at (22, 23) and crossed West to Column 16, then walked Down to ground level at (16, 28).
  - Walked West along Row 28/30 to Column 9, then walked South to transition into Safari Zone West at (9, 35) on Turn 47775.

## Structure for Map 0_219 (Safari Zone West):
### VERIFIED GROUND CONSTRAINTS (PROVEN EMPIRICALLY):
- Column 1 Row 15 & 14 are completely blocked by solid tree walls (TYPE_2889).
- Column 0 Row 16 is completely blocked by western map boundary wall.
- Columns 2 & 3 Row 13 are blocked by water (TYPE_4e8c).
- Column 24 Rows 1-12 are 100% blocked by solid tree walls (TYPE_2889).
- Row 6 Columns 12-16 on the plateau are completely blocked to the North by solid cliff walls.

### ACTIVE ON-FOOT NAVIGATION PATHS (UNVERIFIED):
- Northwest area containing Warden's Gold Teeth and Secret House is accessible ONLY via the southern elevated plateau route (stairs at 21, 17).

### 100% EMPIRICAL PROOF OF WORK (TURNS 48052-48069)
- On Turn 48052, we stood at (2, 15) on the southwest ground level.
- We pressed "Left" to test if Column 1 Row 15 (TYPE_2889, tree graphic) is passable from the East.
  - **Result (Turn 48053)**: We bumped directly into the tile, remaining at (2, 15). This proves (1, 15) has active solid collision from the East.
- On Turn 48068, we executed a 3-button test sequence: "Down", "Left", "Up" from (2, 15).
  - **Step 1 (Down)**: Moved to (2, 16).
  - **Step 2 (Left)**: Moved to (1, 16) (which is a passable grass tile labeled TYPE_3fe2).
  - **Step 3 (Up)**: Attempted to walk Up from (1, 16) onto (1, 15) (TYPE_2889).
  - **Result (Turn 48069)**: We experienced a direct collision, remaining at (1, 16).
- **CONCLUSION**: Column 1 Row 15 is 100% blocked and impassable from both the East and the South. Socratic Question 2's hypothesis is definitively disproven. The southwest and northwest quadrants are indeed completely physically separated on the ground level, and the plateau route is 100% the only way to reach the north side of the map.

## Run 10 Strategy & Socratic Responses (Turn 48097):
- **Socratic Question 1 (Wandering NPC vs. Solid Wall)**:
  - If the block at Column 1 Row 14/15 on Run 9 was caused by a wandering NPC, starting Run 10 resets all NPCs to their default positions.
  - Upon entering Safari Zone West (Map 0_219) from Safari Zone Center, we will immediately walk West along Row 11 to (13, 11), walk Down to (13, 15), and then walk Left to (1, 15). We will then face North and attempt to walk Up to (1, 14) and (1, 13).
  - If we can walk through, it proves the corridor is open on a fresh reset, and we will follow the direct ground route. If we still experience a collision, it proves Column 1 is permanently blocked by map geometry, and we must immediately pivot to the southern plateau route via the stairs at (21, 17).
- **Socratic Question 2 (Step Savings & Direct Route)**:
  - If Column 1 is open, the direct ground route from the entrance of Safari Zone West to the Secret House at (3, 3) takes exactly 46 steps:
    - (29, 11) -> (13, 11) [16 steps West]
    - (13, 11) -> (13, 15) [4 steps South]
    - (13, 15) -> (1, 15) [12 steps West]
    - (1, 15) -> (1, 3) [12 steps North]
    - (1, 3) -> (3, 3) [2 steps East to Secret House]
  - Compared to the elevated plateau route (which requires climbing stairs at (21, 17), crossing the plateau to (6, 16), walking North, and then descending, taking ~90 steps), the direct ground route would save **~44 steps**!
  - This step-saving is massive and would guarantee a highly optimized retrieval of both HM03 Surf and the Warden's Gold Teeth.

## Safari Zone Center (Map 0_220) Navigation Plan (Turn 48193):
- **Objective**: Transition to Safari Zone East at (29, 11) and navigate to Safari Zone West via Safari Zone East and North.
- **Verification & Discovery (Turn 48193)**:
  - Physically tested the eastern bypass of the central pond and Row 9 fence.
  - Discovered that Row 9 has a continuous fence on Columns 22-29 and water on Columns 18-21. Row 10 also has water on Columns 18-21.
  - Thus, there is NO on-foot passage to the North side within Safari Zone Center. The map's Southern and Northern halves are physically disconnected for a player on foot.
  - **New Plan**: Navigate to Safari Zone West via the standard completed route:
    Safari Zone Center -> Safari Zone East -> Safari Zone North -> Safari Zone West!
- **Current Action**: Walk Right 2 steps to transition from (27, 11) in Safari Zone Center to Safari Zone East at (0, 22).

## Safari Zone East (Map 0_217) Route & Step-by-Step Plan:
- **Objective**: From (16, 24) ground level, climb onto the plateau at (20, 21), cross to the West stairs, walk north through the central corridor, and transition to Safari Zone North at (0, 5).
- **Physical Path (Step-by-Step)**:
  - **Phase 1: Climb Plateau**
    - From (16, 24) walk Right 4 steps to (20, 24)
    - Walk Up 3 steps to (20, 21) (climb stairs)
    - Walk Up 1 step to (20, 20) (on plateau)
  - **Phase 2: Cross Plateau to West**
    - From (20, 20) walk Left 8 steps to (12, 20)
    - Walk Down 2 steps: (12, 20) -> (12, 21) -> (12, 22) (descend western stairs to ground level)
  - **Phase 3: Walk to Northern Stairs**
    - From (12, 22) walk Left 3 steps to (9, 22) (reaches the central vertical corridor)
    - Walk Up 14 steps along Column 9 to (9, 8)
    - Walk Right 3 steps to (12, 8)
    - Walk Up 1 step to (12, 7) (climb northern stairs)
    - Walk Up 1 step to (12, 6) (on the north plateau)
  - **Phase 4: Cross North Plateau & Exit**
    - From (12, 6) walk East 9 steps to (21, 6)
    - Walk Up 1 step to (21, 5) (Note: this is the eastern ground level bypass)
    - Walk Left 21 steps along Row 5 to (0, 5) to transition to Safari Zone North!
  - **Total Steps in East**: 4 + 3 + 1 + 8 + 2 + 3 + 14 + 3 + 1 + 1 + 9 + 1 + 21 = 71 steps.

## Safari Zone North (Map 0_218) Route & Step-by-Step Plan:
- **Objective**: From (39, 31) (isolated eastern basin), navigate across Safari Zone North to reach the southwest exit at (9, 35) leading back into Safari Zone West.
- **Physical Path (Step-by-Step)**:
  - **Phase 1: Navigate Southern Grass-Free Corridor**
    - Enter at (39, 31)
    - Walk Left 17 steps to (22, 31)
  - **Phase 2: Climb and Cross Plateau**
    - From (22, 31) walk Up 8 steps to (22, 23) (stairs UP onto the plateau)
    - Walk Up 1 step to (22, 22) (on plateau)
    - Walk Left 6 steps to (16, 22)
    - Walk Down 6 steps to (16, 28) (descend plateau to western ground level)
  - **Phase 3: Navigate to West Exit**
    - From (16, 28) walk Left 7 steps to (9, 28)
    - Walk Down 7 steps to (9, 35) (Note: Column 9 is open, Row 34 has the blockage)
    - Walk Down 1 step to transition into Safari Zone West at (27, 0) or (26, 0)!
  - **Total Steps in North**: 17 + 8 + 1 + 6 + 6 + 7 + 7 + 1 = 53 steps.
- **Combined Safari Zone East & North Steps**: 71 + 53 = 124 steps.
- **Remaining Step Budget after entering Safari Zone West**: 428 - 124 = 304 steps! This is extremely safe and leaves over 300 steps to grab the Gold Teeth and Surf HM!