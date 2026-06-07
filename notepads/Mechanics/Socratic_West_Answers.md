# Socratic Answers - Safari Zone West & East Traversals (Turn 68942)

## 1. Socratic Question 1: The Eastern Ground Corridor Route
- **Why this ground-level route is physically possible**: Column 21 is a completely open vertical passage on the East side of Safari Zone East.
- **Specific Barriers Bypassed**: 
  - The Row 20 and Row 25 fences are only present on Columns 0 to 5, so they do not block Column 21.
  - The central water lake is on Columns 16-19, Rows 16-17. Column 21 lies entirely to the East of the lake.
  - The high plateau is on Columns 11-19, which is completely West of Column 21.
- **Why it is superior in terms of step-budget and execution**: It requires exactly 30 steps from (15, 25) to (29, 11) in Center, and then a clean ground-level path in East with absolutely no stairs elevation transitions (z=0 -> z=1). This eliminates any risk of staircase transition bugs, making it extremely easy to execute with high accuracy.

## 2. Socratic Question 2: Plateau-Staircase Boundary Correctness
- **How we resolved the boundary discrepancy**: 
  - We discarded the ground-level staircase base tiles (12, 8) and (17, 8) as well as the staircase tiles (12, 7) and (17, 7) from the `plateau` set. This correctly classified them as non-plateau ground-level/transition tiles in the BFS.
  - We updated the stair transition dictionaries (`stairs_climb` and `stairs_descend`) to map transitions directly between the ground-level base (12, 8) and the elevated staircase top (12, 7) or (12, 6).
- **Why it is vital**: Properly separating staircase transition points from the flat plateau body is vital because treating them as flat plateau tiles prevents ground-level entries to the stair base, completely blocking the pathfinder from finding short routes that utilize these staircases, forcing it to find highly convoluted routes that go all the way around the map.

## 3. Socratic Question 3: Chronological Step-Budget Reconciliation
- **Step-by-step math of physical overworld steps consumed since Turn 68911**:
  - Turn 68911 starting steps: **424 steps remaining** at (12, 21).
  - Walk to (9, 10): Down 1, Left 3, Up 12 = 1 + 3 + 12 = 16 steps [remaining: 408].
  - Tall grass bypass to (9, 8): Right 1, Up 2, Left 1 = 1 + 2 + 1 = 4 steps [remaining: 404].
  - Walk to (12, 8): Right 3 = 3 steps [remaining: 401].
  - Plateau crossing to (17, 8): Up 2, Right 5, Down 2 = 2 + 5 + 2 = 9 steps [remaining: 392].
- **Reconciled Remaining Steps**: 424 - 16 - 4 - 3 - 9 = **392 steps remaining** on Turn 68940. This perfectly matches the RAM's step counter, ensuring 100% accurate, drift-free step-keeping.
- **Chronological Log Update**: The completed overworld logs from Turn 68900 to Turn 68913 have been successfully appended to the log at the bottom of 'Scratchpad/SafariZone_West_Route' to ensure perfect tracking accuracy.

# Socratic Answers - Safari Zone North Traversal (Turn 68973)

## 1. Socratic Question 1 (The Western Plateau of Safari Zone North)
- **Why we must climb the Western Plateau**: Ground-level passage to the West is completely blocked by a solid vertical tree wall (TYPE_2889) at Column 17 on Rows 29-34, and a solid building roof structure (TYPE_2889) at Column 19 Row 33. This isolates the Eastern ground basin from the Western side. Climbing the Western Plateau stairs at (22, 23) is strictly mandatory to cross over this barrier.

## 2. Socratic Question 2 (Sequential Overworld Traversal Tracking)
- **Step consumption math since Turn 68962**:
  - Starting steps at (33, 31): 356 remaining.
  - Walk Left 5 steps to (28, 31) -> 351 remaining.
  - Walk Up 4 steps along Column 28 to climb Eastern stairs at (28, 27) -> 347 remaining.
  - Walk Down 2 steps to descend Eastern stairs to (28, 29) -> 345 remaining.
  - Total physical overworld steps consumed: 11 steps.
  - Corrected remaining steps on Turn 68970: 345 remaining in RAM.
- **Movement history updated**: Missing chronological logs from Turn 68913 to Turn 68969 have been appended to 'Scratchpad/SafariZone_West_Route' to ensure perfect tracking accuracy.

## 3. Socratic Question 3 (Plateau Crossing vs. Ledge Boundaries)
- **Plateau traversal route**: Walk Left 6 steps and Down 5 steps from (22, 22) [z=1] to (16, 27) [z=1].
- **Coordinates of the Western Plateau**: Rows 20-22, Columns 15-23.
- **No risk of falling off**: In Gen 1, plateau boundaries (cliff edges) are treated as solid, impassable walls on the plateau level (elevation z=1). The player cannot walk off the edge, so there is zero risk of falling off.