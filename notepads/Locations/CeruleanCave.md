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

## Topological Connectivity and Progression Path to Mewtwo:
- **B1F Access**: The stairs down to B1F are located in the isolated northwestern quadrant of 1F.
- **Northwest Quadrant of 1F**: This isolated quadrant can ONLY be accessed by descending from 2F via a specific ladder located in the northwestern portion of 2F.
- **Western Portion of 2F**: Whether the western section of 2F is completely isolated from the eastern section of 2F on foot is currently under active audit.
- **Accessing Western 2F**: If 2F is indeed connected on foot, we can simply walk west on 2F. If 2F is isolated, we must climb up a specific ladder from the western/southern portion of 1F.
- **Western/Southern Portion of 1F**: We are auditing if there is a separate western landmass accessible on foot or if the 2F-transit is the only pathway.
- **Water Canal**: The water canal runs horizontally across the north on Rows 4-5 and goes south on Columns 8-9 down to Row 15. We must determine if there is an alternative branch of this canal or an overworld land path we missed.

## Cerulean Cave 2F Connectivity Audit (Turn 112311):
- **Hypothesis**: The "empirical proof" of Turn 112168 stating that 2F East and West are completely isolated on foot was an artifact of an incomplete pathfinder grid (treating off-screen/unexplored tiles as solid walls). In standard Pokémon Red/Blue, Cerulean Cave 2F (Map 226) is a single, fully connected floor.
- **Verification Methodology**: We will climb up Ladder 4 at (23, 7) on foot, which is easily accessible from our current position (21, 13) via Row 8. Once on 2F at (22, 6), we will walk west and attempt to navigate to the western portion of 2F to find the northwest ladder at (3, 3).
- **Proof of Work Logs**:
  - Turn 112311: Standing at (21, 13) on foot. We will move Up 5 steps to reach Row 8 at (21, 8), then Right 2 steps to (23, 8), then Up 1 step to (23, 7) to take Ladder 4.