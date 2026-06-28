# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Turn: 131823
- Current Position: surfing on water at (8, 6) on Map 0_228 (1F)

## Active Progress & Discoveries:
- **Empirical Proof of Water Separation (Verified Turn 131004)**:
  - Stood at (10, 6) surfing and visually verified that Rows 4 and 5 are completely blocked by solid rock walls (TYPE_2889) across Columns 6 to 13.
  - This conclusively disproves any direct horizontal water connection between the eastern and western water canals on 1F on those rows.
## Definitive Master Path to Mewtwo
- **Topologically Verified Path**: 1F Northwest -> Surf -> Water Ramp 4 at (15, 3) -> Northern landmass -> Ladder 5 at (7, 1) -> 2F West (9, 1) -> B1F.
- **Why this path is required**:
  1. **1F Northwest** (where we entered) has a solid wall at Row 3 (Columns 3-14) which prevents on-foot walking down to the water canal. Thus, from the starting platform on foot we cannot enter the water directly.
  2. To enter the water, we had to go up Ladder 5 to 2F West, walk east on foot, and descend back to the eastern landmass.
  3. On the eastern landmass, we can surf at Water Ramp 4 at (15, 3).
  4. From Water Ramp 4, we surf down, navigate through the open central water, and dismount at Water Ramp 2 at (11, 13).
  5. From Water Ramp 2, we walk on foot to the central stairs at (17, 15) to descend to the ground, and walk west to (1, 13) where we climb to the elevated southwest plateau.
  6. From the southwest plateau, we walk to Southwest Ladder 6 at (3, 11) and climb to 2F West.

## Active Hypotheses (Scratchpad Category)
- **1F Row 5 Water Canal Crossover Detour (Column 8/9/10/11/12)**:
  - *Hypothesis*: While Row 5 Column 9 and Column 8 are blocked by solid rock, is it possible that Column 10, 11, or 12 on Row 5 is open on 1F, allowing us to Surf from the eastern canal to the western canal directly?
  - *Methodology*: Surf to (10, 6), (11, 6), and (12, 6) and systematically attempt to Surf Up to test columns 10, 11, and 12.
  - *Status*: Columns 8 and 9 are disproven. Columns 10, 11, and 12 are UNTESTED.

- **1F Row 3 Passability (Northern Landmass to Water)**:
  - *Hypothesis*: Row 3 on 1F contains an open vertical passage on some column (e.g. Column 12, 11, 10, 9, 8, 7, 6, 5) allowing us to step Down from the northern landmass directly into the water canal and Surf to (1, 3) on foot.
  - *Methodology*: Walk Left along Row 2 or Row 1, and systematically attempt to step Down (South) on each column to test passability. We will log the results.
  - *Status*: Columns 13 down to 6 have been physically tested (Turn 131644-131649) and are confirmed BLOCKED. Row 3 is solid rock across all these columns.

## Disproven Theories Archive
- **Row 4 Passability on 2F West (Direct Path)**:
  - *Hypothesis*: Row 4 (specifically (4, 4)) is open on 2F West to reach (1, 3) directly from (9, 1).
  - *Test*: Stood at (4, 3) on 2F West facing Left and pressed Down on Turn 131464.
  - *Result*: BUMP (visited 0 tiles). Disproven. Row 4 is completely impassable. Moving from Ladder 5 on 2F West to Northwest Ladder (1, 3) directly on foot is impossible.
- **Row 4 Detour on 2F West**:
  - *Hypothesis*: Columns 6, 7, or 8 on Row 4 on 2F West are open, allowing a detour from (9, 1) -> Row 3 -> Row 4 -> Row 5 -> (1, 3).
  - *Test*: Stood at (8, 3) and pressed Down on Turn 131775. Stood at (7, 3) and pressed Down on Turn 131780. Stood at (6, 3) and pressed Down on Turn 131784.
  - *Result*: Consistent BUMPs on all three columns. Disproven. Row 4 is completely impassable across all Columns 3 to 8 on 2F West.
- Turn 131589: Discovered (3, 7) on 1F is a solid rock wall blockage (TYPE_2889).
- Turn 131591: Confirmed via screen overlay that (3, 7) is indeed TYPE_2889.
- Turn 131591: We are standing at (3, 8) facing Up. We can bypass (3, 7) by moving Left to (2, 8) (TYPE_2770), Up to (2, 7) (TYPE_3fe2), Up to (2, 6) (TYPE_3fe2), Right to (3, 6) (TYPE_3fe2). From (3, 6), we can Surf Up to (3, 5). Let's test this route.
- Turn 131594-131602: Tested on-foot bypass on 1F Northwest.
  - *Fact*: (2, 7) and (1, 7) are ledges blocking northward movement. Row 7 across Columns 3-7 consists of solid rock walls (TYPE_2889).
  - *Conclusion*: 1F Southwest is completely disconnected on foot from the northern water and cannot reach (1, 3) or any water on foot. We must backtrack to the central platform to enter the water.
- Turn 131603: Ran BFS solver on 2F West from (9, 1) (Ladder 5 landing) to (1, 3) (Northwest Ladder / B1F access) on foot.
  - *Result*: Found unblocked path: ['Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Down', 'Down', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Left', 'Up', 'Left', 'Up'].
  - *Proof*: This path completely avoids the Row 4 blockage at (4, 4) by looping through Row 5 and Column 5! This is our definitive route to B1F.
- Turn 131751: Attempted to Surf Up from (9, 6) to (9, 5) on 1F water.
  - *Result*: BUMP. Disproven. Row 5 Column 9 is a solid rock wall on 1F.
- Turn 131710: Ran Python BFS analysis on 2F West using verified collision records.
  - *Result*: Proved that 2F West is bifurcated into two mutually isolated on-foot components. We must navigate through 1F's central water canals instead.
- Turn 131819: Attempted to Surf Up from (8, 6) to (8, 5) on 1F water.
  - *Result*: BUMP. Disproven. Row 5 Column 8 is a solid rock wall on 1F.