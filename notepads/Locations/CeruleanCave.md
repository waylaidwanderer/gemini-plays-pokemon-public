# Cerulean Cave - Verified Records
- Map ID: 0_228 (1F), 0_226 (2F)

## 1F (0_228) Verified Layout:
- **Ladder (24, 17)**: Leads out of Cerulean Cave to Cerulean City.
- **Ladder (21, 11)**: Labeled TYPE_4b8d. One-way dropdown ladder; cannot be used to ascend from 1F.
- **Ladder (23, 7)**: Labeled TYPE_3fe2. Interacting with or stepping onto this tile immediately warps the player to 2F at (22, 6).
- **Ladder (22, 6) [2F]**: Connects back down to 1F at (23, 7).
- **Ramps to Water**:
  - Located at (23, 3), (15, 3), (11, 13), and (25, 9) (TYPE_4b8d).
  - Standing on any of these ramps facing the water and selecting SURF from the party menu successfully mounts the water.
- **Water Canal**:
  - Rows 4 and 5 on 1F are water (TYPE_4e8c) and can be surfed upon.
- **Northern Landmass Layout (Row 0-2 ground-level shortcut)**:
  - Rows 0, 1, and 2 form an unblocked, completely walkable ground-level connection on foot from Column 23 (Water Ramp 1) all the way east to Column 28 (Ladder 2 landing at 27,1). There is NO solid rock barrier on Column 26 on 1F, allowing the player to bypass the 2F serpentine path entirely when navigating from the western water canal to the northeast section of 1F. Verified on Turns 112008-112012.
- **Visual Artifact Note**: Red flower tiles (TYPE_3fe2) (such as at 19, 3) visually resemble red-and-white Poké Balls in the Crystal palette swap but are passable ground tiles with no physical items.

## 2F (0_226) Verified Layout:
- **Serpentine Bypass**:
  - Located at Column 25, Row 9. Bypasses the solid Column 26 rock barrier to allow access to the northeast section of 2F.
- **Ladder 2**:
  - Located at (29, 1) (labeled [=], TYPE_3fe2).
  - To reach it from (29, 3): walk Left to (28, 3), Up 2 steps to (28, 1), and Right to (29, 1). Descending this ladder lands on 1F at (27, 1).
- **Row 11 Passage**:
  - Row 11 forms a completely open, unblocked horizontal passage from Column 18 to Column 24.
- **Row 16 Blockage**:
  - Row 16 contains a solid horizontal rock wall from Column 14 to Column 20, blocking direct downward access from Row 15 to Row 17.
- **Row 9 Blockage**:
  - Row 9 is blocked by rock walls at (22, 9) and (24, 9), so it is not a continuous horizontal corridor.
- **Topological Goal**:
  - To access the basement (B1F) where Mewtwo is, the player must locate the northwest ladder on 2F. This ladder descends into the isolated northwestern quadrant of 1F, which contains the stairs leading to B1F.
- **(15, 13) Rock Wall Blockage**:
  - Visually appearing as a rock wall but labeled TYPE_3fe2 in some overlays, (15, 13) is an impassable rock wall blocking any direct horizontal transition between Column 14 and Column 15 on Row 13.
- **(16, 13) Rock Wall Blockage (Verified Turns 112374, 112378)**:
  - While labeled as TYPE_3fe2 (open ground) in the visual overlay, (16, 13) is physically a solid, impassable rock wall.
  - Verification: On Turn 112374 and Turn 112378, standing at (17, 13), attempting to walk Left to (16, 13) resulted in zero coordinate change, proving that (16, 13) is impassable.
  - This definitively proves that the eastern section of 2F is blocked from navigating westwards at Row 13, and since Row 11 is blocked at (13, 11) and Row 16 is a solid horizontal wall, 2F East is physically disconnected from 2F West on foot. Our connectivity hypothesis is falsified. We must use the 1F water canal and find a western/southern ladder to access 2F West.

## Topological Connectivity and Progression Path to Mewtwo:
- **B1F Access**: The stairs down to B1F are located in the isolated northwestern quadrant of 1F.
- **Northwest Quadrant of 1F**: This isolated quadrant can ONLY be accessed by descending from 2F via a specific ladder located in the northwestern portion of 2F.
- **Western/Southern Portion of 1F**: Impassable via the western water canal. Our empirical testing on Turns 112211-112224 and 112487-112495 proved that the western vertical canal (Columns 8-9) is a dead end on Row 16 with no connected dismount points. We empirically verified on Turn 112601 that Column 19 on Row 15 is physically impassable on foot, which definitively proves that the eastern entrance platform of 1F is completely physically isolated on foot from the western/southern portion of 1F. Thus, the only way to reach the western/southern portions of 1F is by climbing up to 2F, crossing over, and descending elsewhere, or via the horizontal water canals.
- **Accessing Western 2F**: The eastern section of 2F is completely isolated from the western section of 2F on foot. This has been empirically proven by the rock wall blockages at (16, 13) and (13, 11). Thus, we must climb up a different ladder from 1F.
- **Water Canal**: Rows 4 and 5 on 1F contain water, but passability at Column 13 is currently unverified. We need to test if we can surf horizontally across the northern canal past Column 13.

- **Ladder 6**:
  - Located on 1F at (1, 3) (labeled TYPE_3fe2). Ascending this ladder warps the player to 2F at (1, 3).
  - Located on 2F at (1, 3) (labeled [=], TYPE_3fe2). Descending this ladder warps the player to 1F at (1, 3). This is the critical gateway to the northwest isolated quadrant of 1F and the B1F stairs.