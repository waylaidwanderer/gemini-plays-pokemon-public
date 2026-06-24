# Post-Game Mewtwo Quest Plan & Logs
- Quest Started: Turn 111394
- Active Goal: Reach Cerulean Cave B1F on foot to locate and capture Mewtwo.

## Topological Realities & Floor Layout Analysis
- **2F West Layout Partitioning**:
  - **Component 1 (Northern Section)**: Contains Ladder 5 (9, 1) and the northern corridors.
  - **Component 3 (Southern/Western Section)**: Contains Southwest Ladder 6 (3, 11), Row 9 horizontal corridor, and several small dead-end pockets.
  - **The Barrier**: Row 8 contains solid rock walls across all columns from 3 to 12. Row 10 contains solid rock walls across columns 13 to 20, isolating Row 9. Row 7 contains solid walls from (13, 7) to (17, 7). Thus, Component 1 and Component 3 are completely disconnected on foot on 2F West. Also, on 2F West, (1, 3) is completely isolated in a 1x2 pocket of (1, 2) and (1, 3) bounded by solid rock walls of TYPE_2889 at (2, 1)-(2, 3), (1, 1), and (1, 4), meaning the Northwest Ladder (1, 3) cannot be accessed from Component 1 or Component 3 on 2F West.
- **The True Path to Mewtwo**:
  1. The "58-step southern loop detour" on 2F West has been mathematically and physically disproved (Turn 118420). Column 14, 15, and 16 on Rows 6, 7, and 8 contain solid, impassable wall blockages of TYPE_2889, creating a complete barrier between the north (Row 5) and south (Row 9) sections of 2F West.
  2. Therefore, Component 1 and Component 3 on 2F West are indeed completely physically isolated on foot.
  3. The Northwest Ladder (1, 3) is in Component 3, so it CANNOT be reached on foot from Ladder 5 at (9, 1).
  4. The only way to access the Northwest Ladder (1, 3) on 2F West is via Southwest Ladder 6 at (3, 11) from 1F Southwest!
  5. The true master path to reach B1F is:
     - Ascend Southwest Ladder 6 at (3, 11) to 2F West Component 3.
     - Navigate on 2F West Component 3 from (3, 11) to the Northwest Ladder (1, 3).
     - Descend Northwest Ladder (1, 3) to 1F Northwest.
     - Take the stairs on 1F Northwest to B1F.

## Verified On-Foot Crossover Path:
From (15, 5) to (15, 1):
- Right 1 step to (16, 5)
- Up 2 steps to (16, 3)
- Left 1 step to (15, 3)
- Up 2 steps to (15, 1)
- Left 6 steps to (9, 1) [Ladder 5].

## Obsolete Historical Attempts (Archived Summary):
- **Turns 111394 to 119725**: Mapped out various routes on 1F and 2F West. Discovered that the southwestern ground pocket on 1F Southwest is reached via dismounting at Water Ramp 2 (11, 13), walking over the central platform stairs, and backtracking along Row 17 on ground level. Walked up Southwest Ladder 6 at (3, 11) to 2F West Component 3, and backtracked to 1F via the same ladder.
- **Turns 119726 to 119814**: Attempted to bypass the 2F West Row 8/10 wall blockages on foot, confirming that Row 7 contains solid walls that block the horizontal on-foot path between the (9, 1) ladder and the (1, 3) Northwest Ladder on 2F West. This physically disproves the 2F West on-foot detour, forcing us to explore the 1F Northwest Surf/dismount path. Backtracked to (9, 1) and descended Ladder 5 to return to 1F Northwest at (7, 1).

## Live Navigation Logs:
- **Turn 123137**: Backtracked from 2F East, descended Ladder 3 to 1F, walked to Water Ramp 2 on foot, used SURF at (11, 13), and currently surfing at (11, 14) on Map 0_228, preparing to navigate the western canals to Southwest ground level.
- **Turn 123140**: Surfing at (11, 14) on Map 0_228. Confirmed that Row 15 completely blocks vertical ground-level traversal to the southwest on foot, meaning we must dismount back onto Water Ramp 2 at (11, 13) on foot and walk the central platform detour to reach Southwest Ladder 6.

## Consolidated Passability Analyses:
- Visually, Y=4 has solid rock walls (TYPE_2889) on Columns 1-8. Column 2 has solid rock walls (TYPE_2889) on Rows 1-3. 
- However, Column 1 has open tiles at (1, 2) and (1, 3), and Row 5 is open from Column 1 to Column 7. If there is any unverified opening on Row 4 or Column 2, or if we can cross Column 2 on foot, we can reach (1, 3).
- Our active priority is to walk to (3, 1) and attempt to step Left onto (2, 1) to physically verify its collision. If blocked, we will test (3, 2) -> (2, 2) and (3, 3) -> (2, 3) to conclusively verify the Column 2 barrier. We will also test Row 4 Column 1 (1, 4) from (1, 5) if we can navigate there. This strictly satisfies the Burden of Proof.
- **Unverified Visual Hypothesis**: Column 2 on 2F West on Rows 13 and 14 is currently an unverified visual hypothesis. We must perform a physical on-foot bump test here once we reach 2F West Component 3 (by climbing up Southwest Ladder 6 at (3, 11)) to verify if it is passable or blocked by solid rock walls.

## True Path to Northwest Ladder (1, 3) on 2F West:
- Wait! On Turn 122424, we ran our custom tool `cave_bfs_solver` and it returned an empty list `[]`, indicating that there is no valid on-foot path from our current position to (1, 3) on Map 0_226 with all verified obstacles registered.
- This is because Row 4 (Columns 1-7), Row 6 (Columns 0-5 and 7), and Row 8 (Columns 2-7) are completely blocked by solid rock walls of TYPE_2889. Column 6 Row 6 (6, 6) is open, but Row 7 is completely blocked horizontally across Columns 4-7, meaning we cannot reach (6, 6) from the south on foot.
- Therefore, the northern portion of 2F West (containing (1, 3)) is completely geographically split and isolated on foot from the southern portion (containing (3, 11)) on Map 0_226.
- To reach Northwest Ladder (1, 3), we must ascend from 1F Northwest. Let's look at 1F Northwest access.
- 1F Northwest can only be reached via Surf. Specifically, we must surf along the water canals of 1F (Map 0_228) from the main water body to the northwest quadrant!
- Wait, let's trace: does the water canal on 1F actually connect to the northwest quadrant on 1F?
- Let's check 1F (Map 0_228)'s water layout. We must re-examine our unverified assumptions about 1F Northwest isolation!
- Let's backtrack to 1F Southwest via Southwest Ladder 6 at (3, 11). Standing at (2, 7) on 2F, we will walk back to (3, 11) on 2F West and descend the ladder to 1F.
- **Turn 122432**: Redefined the custom tool `cave_bfs_solver` with the new rock walls to prevent any incorrect path suggestions. Tested BFS from (2, 7) to (1, 3) and confirmed no path exists on 2F. We must now backtrack to 1F.

- **Disproven bypass theory archived**: The long disproven "2F West direct on-foot bypass route" and backtracking logs have been permanently moved to `Archive/CeruleanCave_DisprovenTheories` on Turn 121235.
- **Turn 120809**: Empirically verified via visual overlay on `<CurrentScreen turn="120809">` that (8, 5) is a solid rock wall (`TYPE_2889`), and (7, 5), (7, 6) are solid rock walls (`TYPE_2889`). This completely disproves the "Column 7 Water Shortcut" hypothesis, confirming that the canal does not continue west or north at Column 8, Row 5. We must proceed east to Column 14 and navigate to Water Ramp 4 at (15, 3) to land on the northeast platform.
- **Turn 120915 systematic test**: Stood at (8, 6) facing Left and pressed Left to test (7, 6) passability. Result: BUMP collision, player remained at (8, 6). This physically and empirically proves that (7, 6) is a solid impassable rock wall of TYPE_2889.
- **Active Testing Protocol**:
  - We systematically tested the water canal on Row 5 across Columns 8 to 13 by standing on Row 6 facing Up and pressing Up at each column (completed on Turn 120968). All are impassable rock walls of TYPE_2889.
  - Final Conclusion migrated to Locations/CeruleanCave.
- Turn 120969: Step 6 Result: Stood at (13, 6) facing Up and pressed Up. Result was a BUMP collision (Turn 120968), proving (13, 5) is indeed an impassable rock wall of TYPE_2889. This systematic test of Row 5 on water is now 100% complete and fully verified!
- Turn 121560: Walked on foot to (1, 15), physically verified Column 0 passability on 1F Southwest at (0, 15), and successfully backtracked to the central platform stairs at (17, 15) on foot.

## Column 0 Passability Empirical Test Plan on 2F West:
- **Hypothesis**: Column 0 on 2F West is an open vertical corridor allowing vertical movement, or it is a solid rock boundary wall of TYPE_2889.
- **Testing Methodology**: Once we reach 2F West Component 3 (by climbing Southwest Ladder 6 at (3, 11)), we will navigate to (1, 15), and attempt to step Left onto Column 0 at (0, 15) by pressing Left.
- **Expected Outcome if Column 0 is open**: Player's position becomes (0, 15) with no collision.
- **Expected Outcome if Column 0 is a solid wall**: Player bumps and remains at (1, 15), proving Column 0 is a solid boundary wall. We will execute this test and log the exact turn and result.

## Row 12 Passability Empirical Test on 2F West:
- **Hypothesis**: Tile (3, 12) on 2F West is passable, allowing horizontal/vertical navigation, or it is a solid rock wall.
- **Testing Methodology (Turn 121534)**: Standing at (3, 11) on 2F West facing Down, pressed Down.
- **Result**: Direct bump collision with zero coordinate change (player remained at 3, 11).
- **Definitive Conclusion**: Tile (3, 12) on 2F West is 100% physically a solid, impassable rock wall of TYPE_2889. This physically and mathematically proves that the southwest pocket of 2F West is indeed a completely isolated dead-end pocket, and we must proceed with our master backtracking route via 1F to reach Northwest Ladder (1, 3).

## Column 0 Passability Empirical Test on 1F Southwest:
- **Hypothesis**: Tile (0, 15) on 1F Southwest is passable on foot, or it is a solid rock wall.
- **Testing Methodology (Turn 121539)**: Standing at (1, 15) on 1F Southwest facing Left, pressed Left.
- **Result**: Successfully stepped onto (0, 15) on foot with no collision, updating position to (0, 15).
- **Definitive Conclusion**: Column 0 on 1F Southwest is indeed 100% passable on foot! This is a massive empirical discovery that disproves any assumption of a solid rock boundary wall on Column 0 here, confirming that Column 0 is open. We will use this verified fact to plan future routes.

## Disproved Assumption: Direct path on 2F West from (9, 1) to (1, 3) is IMPASSABLE (Turn 121862)
- On Turn 121854, we hypothesized that we could walk on foot directly from (3, 3) to (1, 3) via Row 3, Column 11, and Column 6.
- **Empirical Test**: On Turn 121855, we attempted to walk Right from (9, 3) to (10, 3).
- **Result**: We collided with a solid rock wall at (10, 3) and remained at (9, 3).
- **Conclusive Proof**: (10, 3) is a solid, impassable rock wall of TYPE_2889. Thus, the northern corridor (Component 1) is completely isolated from the western section (Component 3) on Row 3.
- This confirms that we cannot walk directly from (9, 1) to (1, 3) on 2F West without transitioning. We must backtrack to 1F and execute our master backtracking route via 1F Southwest to reach the Southwest Ladder 6 at (3, 11), which is the only way to reach (1, 3) on 2F West.
## Physical Verification of Map 0_228 (1F Northwest) Column 4 Passability:
- **Turn 122260 Test**: Standing at (7, 1) on Map 0_228, we attempted to walk Left 3 steps to (4, 1).
- **Result**: Successfully stepped onto (6, 1) and (5, 1), then experienced a solid bump collision against (4, 1) on Turn 122261, remaining at (5, 1) facing Left.
- **Definitive Conclusion**: Tile (4, 1) is 100% physically a solid rock wall of TYPE_2889.
- This physically, empirically, and undeniably proves that Column 4 on Rows 0, 1, and 2 is a solid rock wall barrier, completely blocking any horizontal on-foot crossover from (7, 1) to the western area containing Northwest Ladder (1, 3) on Map 0_228.
- Thus, the northwest quadrant of 1F (containing Northwest Ladder (1, 3)) is indeed completely isolated on foot from the landmass around Ladder 5 (7, 1) on Map 0_228.
## Column 0/1/2 Passability on 1F Northwest - DISPROVEN (Turn 122327):
- **Hypothesis**: Column 0 on Map 0_228 (from Row 3 to Row 12) is completely passable on foot, allowing a direct vertical connection between the southwest ground area and the Northwest Ladder (1, 3).
- **Physical Test (Turn 122327)**: Standing at (1, 8) on foot on Map 0_228, we walked Right to (2, 8), and then attempted to walk Up to (2, 7) by pressing Up.
- **Result**: Direct bump collision, remaining at (2, 8) facing Up.
- **Definitive Conclusion**: Tile (2, 7) (and (1, 7)) are 100% physically solid, impassable barriers (rock walls). This physically, empirically, and mathematically disproves the Column 0/1/2 passability hypothesis. Row 7 forms a continuous, unbroken solid rock wall barrier across all columns on the west side of Map 0_228. Thus, the northwest quadrant on 1F is indeed completely physically isolated on foot from the southwest area on Map 0_228.
- Turn 122760: Started post-battle on 2F West at (10, 9). BFS solver incorrectly found a path assuming (1, 10) was open.
- **Turn 122773 Physical Collision Test of (1, 10)**: Standing at (2, 10) facing Left, pressed Left. Result was a solid bump collision, remaining at (2, 10) on foot.
- **Definitive Conclusion**: Tile (1, 10) on Map 0_226 is 100% physically a solid, impassable rock wall of TYPE_2889. This physically, empirically, and mathematically disproves the BFS path that assumed (1, 10) was open. The southwest pocket on 2F West (consisting of Columns 1-3, Rows 9-11) is indeed a completely isolated dead-end pocket. There is absolutely no walkable path on foot to the Northwest Ladder (1, 3) from Southwest Ladder 6 (3, 11) on 2F West. We must backtrack to 1F.

- Turn 123040: Started active post-game exploration on 2F West at (15, 1). Discovered that (19, 1) is indeed a solid, impassable rock wall of TYPE_2889. However, our programmatic BFS analysis of the screen grid shows we can successfully bypass this obstacle by walking:
  - Right 3 steps to (18, 1)
  - Down 2 steps to (18, 3)
  - Right 2 steps to (20, 3)
  - Up 2 steps to (20, 1)
  - Right to continue along Row 1 toward Ladder 2 at (29, 1).
  We will now execute this bypass path step-by-step. Expected start coordinates: (15, 1). Target coordinate: (18, 1).