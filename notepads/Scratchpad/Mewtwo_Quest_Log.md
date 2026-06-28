# Post-Game Mewtwo Quest Log & Active Routing
- Quest Started: Turn 111394
- Current Turn: 131762
- Current Position: standing on foot at (15, 3) on Map 0_228 (1F)

## Active Progress & Discoveries:
- **Empirical Proof of Water Separation (Verified Turn 131004)**:
  - Stood at (10, 6) surfing and visually verified that Rows 4 and 5 are completely blocked by solid rock walls (TYPE_2889) across Columns 6 to 13.
  - This conclusively disproves any direct horizontal water connection between the eastern and western water canals on 1F on those rows.
## Definitive Master Path to Mewtwo
- **Topologically Verified Path**: 1F Northwest -> Surf -> Water Ramp 4 at (15, 3) -> Northern landmass -> Ladder 5 at (7, 1) -> 2F West (9, 1) -> on foot to Northwest Ladder (1, 3) detour -> B1F.
- **Why this path is required**:
  1. **1F Northwest** (where we entered) has a solid wall at Row 3 (Columns 3-14) which prevents on-foot walking down to the water canal. Thus, from the starting platform on foot we cannot enter the water directly.
  2. To enter the water, we had to go up Ladder 5 to 2F West, walk east on foot, and descend back to the eastern landmass.
  3. On the eastern landmass, we can surf at Water Ramp 4 at (15, 3).
  4. From Water Ramp 4, we surf down, navigate through the open central water, and dismount at Water Ramp 2 at (11, 13).
  5. From Water Ramp 2, we walk on foot to the central stairs at (17, 15) to descend to the ground, and walk west to (1, 13) where we climb to the elevated southwest plateau.
  6. From the southwest plateau, we walk to Southwest Ladder 6 at (3, 11) and climb to 2F West.
  7. On 2F West, we must navigate to (1, 3).

## Active Hypotheses (Scratchpad Category)
- **2F West Row 4 Passability Detour**:
  - *Hypothesis*: While (4, 4) and (5, 4) are blocked on 2F West, Column 6, 7, or 8 on Row 4 is open and passable on foot, allowing us to walk from (9, 1) -> left to Row 3 -> down through the open Row 4 column -> Row 5 -> left to Column 2 Row 5 -> up to (1, 3) B1F stairs.
  - *Methodology*: Ascend Ladder 5 at (7, 1) to 2F West at (9, 1). Walk left to Column 6/7/8 on Row 3 and systematically test vertical downward passability onto Row 4.
  - *Status*: UNTESTED.

- **1F Row 3 Passability (Northern Landmass to Water)**:
  - *Hypothesis*: Row 3 on 1F contains an open vertical passage on some column (e.g. Column 12, 11, 10, 9, 8, 7, 6, 5) allowing us to step Down from the northern landmass directly into the water canal and Surf to (1, 3) on foot.
  - *Methodology*: Walk Left along Row 2 or Row 1, and systematically attempt to step Down (South) on each column to test passability. We will log the results.
  - *Status*: Columns 13 down to 6 have been physically tested (Turn 131644-131649) and are confirmed BLOCKED. Row 3 is solid rock across all these columns.

- **1F Row 5 Water Canal Crossover**:
  - *Hypothesis*: Row 5 Columns 8-12 on 1F is actually open water (not blocked by rock walls), meaning we can Surf from Water Ramp 2 at (11, 13) directly to (1, 3) without 2F.
  - *Methodology*: Surf from Water Ramp 4 to (8, 6) and attempt to Surf Up to (8, 5).
  - *Status*: Disproven. On Turn 131751, attempted to Surf Up from (9, 6) to (9, 5) and got a BUMP, physically proving Column 9 Row 5 is blocked by a solid rock wall of TYPE_2889.

## Disproven Theories Archive
- **Row 4 Passability on 2F West (Direct Path)**:
  - *Hypothesis*: Row 4 (specifically (4, 4)) is open on 2F West to reach (1, 3) directly from (9, 1).
  - *Test*: Stood at (4, 3) on 2F West facing Left and pressed Down on Turn 131464.
  - *Result*: BUMP (visited 0 tiles). Disproven. Row 4 is completely impassable. Moving from Ladder 5 on 2F West to Northwest Ladder (1, 3) directly on foot is impossible.
- Turn 131589: Discovered (3, 7) on 1F is a solid rock wall blockage (TYPE_2889).
- Turn 131591: Confirmed via screen overlay that (3, 7) is indeed TYPE_2889.
- Turn 131591: We are standing at (3, 8) facing Up. We can bypass (3, 7) by moving Left to (2, 8) (TYPE_2770), Up to (2, 7) (TYPE_3fe2), Up to (2, 6) (TYPE_3fe2), Right to (3, 6) (TYPE_3fe2). From (3, 6), we can Surf Up to (3, 5). Let's test this route.
- Turn 131594-131602: Tested on-foot bypass on 1F Northwest.
  - *Fact*: (2, 7) and (1, 7) are ledges blocking northward movement. Row 7 across Columns 3-7 consists of solid rock walls (TYPE_2889).
  - *Conclusion*: 1F Southwest is completely disconnected on foot from the northern water and cannot reach (1, 3) or any water on foot. We must backtrack to the central platform to enter the water.
- Turn 131603: Ran BFS solver on 2F West from (9, 1) (Ladder 5 landing) to (1, 3) (Northwest Ladder / B1F access) on foot.
  - *Result*: Found unblocked path: ['Left', 'Left', 'Left', 'Left', 'Left', 'Left', 'Down', 'Down', 'Right', 'Right', 'Down', 'Down', 'Left', 'Left', 'Left', 'Up', 'Left', 'Up'].
  - *Proof*: This path completely avoids the Row 4 blockage at (4, 4) by looping through Row 5 and Column 5! This is our definitive route to B1F.