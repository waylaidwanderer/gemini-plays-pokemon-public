# Post-Game Mewtwo Quest Log & Active Routing
- Current Status: Standing on foot at (3, 11) on Map 0_228 (1F Southwest) on Turn 137623 facing Down.

## 1F Water Canal Column 7 and Column 13 Passability Test Log
- **Objective**: Empirically verify water passability at Column 13 Rows 4/5 and Column 7 Rows 6/7 on Map 0_228 (1F) on water.
- **Experimental Results**:
  - **Tile (13, 5)**: Impassable (Bumped on Turn 137432; verified solid rock of TYPE_2889).
  - **Tile (13, 4)**: Impassable (Bumped on Turn 137436; verified solid rock of TYPE_2889).
  - **Tile (7, 7)**: Impassable (Bumped on Turn 137525; verified solid rock of TYPE_2889).
  - **Tile (7, 6)**: Impassable (Bumped on Turn 137530; verified solid rock of TYPE_2889).
- **Status**: Completed and fully disproven on Turn 137530. The water canals are 100% split at Column 13 and Column 7. There is no horizontal water shortcut on 1F. We must use the verified multi-map backtracking route to reach B1F.

## Verified Master Route to Mewtwo (B1F)
- **Concept**: Since the 2F West landing pocket at (9, 1)/(7, 1) is 100% isolated because (7, 1) is a warp and Row 0 is blocked at (6, 0), we must use Southwest Ladder 6 at (3, 11) to reach 2F West, and then take the alternate path through Column 14/15 to reach Northwest Ladder (1, 3) to descend to B1F.
- **Path Steps**:
  1. Walk East from (8, 1) to Water Ramp 4 at (15, 3).
  2. Use SURF to board the water canal and surf south to Water Ramp 2 at (11, 13).
  3. Dismount onto the central platform and descend the central staircase at (17, 15) to (17, 16) on the ground floor.
  4. Walk west along Row 17 to (1, 13) and climb the wooden stairs onto the southwest plateau.
  5. Walk to Southwest Ladder 6 at (3, 11) and climb up to 2F West at (3, 11).
  6. On 2F West, navigate the alternate path around the blockages:
     - (3, 11) -> (3, 9) -> (13, 9) -> (13, 8) -> (14, 8) -> (14, 7) -> (14, 6) -> (14, 5) -> (14, 4) -> (13, 4) -> (12, 4) -> (11, 4) -> (10, 4) -> (9, 4) -> (8, 4) -> (7, 4) -> (7, 5) -> (6, 5) -> (5, 5) -> (4, 5) -> (3, 5) -> (2, 5) -> (2, 4) -> (1, 4) -> (1, 3).
  7. Take Northwest Ladder at (1, 3) DOWN to 1F Northwest.
  8. Take the adjacent stairs down to B1F to capture Mewtwo!

## Disproven Theories Archive
- **Direct 1F Horizontal Surfing Route (Disproven Turns 135121-135471)**:
  - Direct water surfing from Water Ramp 2 at (11, 13) to (1, 4) is blocked. Column 7 on Rows 6-7 is blocked by solid rock walls, and Column 6 is blocked across Rows 4-7.
- **Direct Western Canal Surf Boarding (Disproven Turns 135380 and 135400)**:
  - Attempting to Surf facing Left from (1, 14) towards (0, 14) or facing Up from (0, 14) towards (0, 13) failed, proving that Column 0 is blocked on Row 13 and there is no direct Surf-Left boarding option at ground level.

- **Direct Connection Finding (Turn 137593 Socratic Challenge)**:
  - We have been operating under the assumption that 2F West is horizontally split. However, vanilla Cerulean Cave 2F is a perfect grid of 1x1 pillars at even-even coordinates (X and Y both even). Every odd-numbered row and odd-numbered column is fully open.
  - This implies a direct on-foot connection between Southwest Ladder 6 at (3, 11) and Northwest Ladder (1, 3) must exist on 2F West! Specifically, walking up Column 11 or other odd columns should connect the south to the north.
  - We will systematically test the passability of these lanes to find the unblocked route! We start by walking north to Row 9 and then east.
  - Let's establish a dedicated testing scratchpad 'Scratchpad/2F_West_Pillar_Grid_Test' to log our physical testing and findings.
- **2F East (29, 1) Pocket Passability (Disproven Turn 136026)**:
  - **Objective**: Verify if Row 0 at (27, 0) on Map 0_226 is passable on foot.
  - **Experimental Results**: On Turn 136025, starting from (29, 1), we walked Left to (28, 1), Up to (28, 0), and pressed Left against (27, 0). Result: BUMP (visited 0 tiles). This conclusively disproves the passability of (27, 0), proving 2F East (29, 1) is a 100% closed, dead-end pocket on foot.