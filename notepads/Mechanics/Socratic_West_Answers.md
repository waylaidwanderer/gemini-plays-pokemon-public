# Koga's Plateau Elevation Split & True Northwest Victory Route Answers

## 1. Socratic Question 1: The Western Plateau Elevation Split (z=1)
- **Why the Western Plateau is physically split**: 
  Koga's Western Plateau in Safari Zone West (Map 0_219) is physically divided on the elevated plateau level (z=1) into separate Eastern and Western halves, making a direct crossing on the plateau impossible.
- **Specific Coordinate Blockages**:
  - **Column 10 (Rows 6-8)**: Symmetrical vertical brown cliff faces (`TYPE_2889`) occupy Column 10 on Rows 6-8 on the plateau. Walking West from Column 11 to Column 9 is physically blocked.
  - **Column 14 (Rows 9-14)**: Symmetrical vertical cliff drop-off walls (`TYPE_2889`) occupy Column 14 on Rows 9-14 on the plateau. Walking East/West on these rows is physically blocked.
- **Conclusion**:
  These continuous cliff wall barriers isolate Koga's plateau on the z=1 level. It is physically impossible to walk continuously on z=1 from the East side (staircase at 21, 17) to the West side to descend onto the Northwest plains.

## 2. Socratic Question 2: The True Northwest Ground Route
- **Why we must backtrack through Safari Zone North**:
  - The Southwest ground pocket of Safari Zone West is 100% closed (blocked by Rest House 3 at (11, 12) and Row 13 water lake on Columns 2-9).
  - Koga's Western Plateau is physically split on the z=1 level.
  - The Eastern ground corridor (Columns 25-28) is completely isolated from the central area at ground level by tree/cliff walls.
  - Because of these three physical constraints, there is **zero** ground-level or plateau-level pathway connecting the East side of Map 0_219 directly to the Northwest plains.
  - The **only** physically possible path to reach the Northwest plains (where the Secret House at (3, 3) is located) is to backtrack all the way to Safari Zone North (Map 0_218) via the (27, 0) warp, walk across the North corridor of Map 0_218, and transition back to Safari Zone West ground level on the North-West side (which has open ground level connections).
- **Backtrack Traversal Step Count**:
  1. Walk Up from (25, 12) to (25, 0) [12 steps], Right 2 to (27, 0) [2 steps], and Up 1 to transition [1 step] -> **15 steps** to enter North.
  2. Walk across Safari Zone North from (9, 35) to the Northwest transition to West -> **41 steps**.
  3. Total backtrack steps: 15 + 41 = **56 steps** total to reach the Northwest plains of West.

## 3. Socratic Question 3: Chronological Step-Budget Reconciliation
- **Step-by-step math of physical overworld steps consumed since Turn 68495**:
  - Stand at (6, 20) with **247 steps remaining**.
  - Walk Up 2 to (6, 18) [z=1] -> 2 steps.
  - Walk Up 2 to (6, 16) [z=1] -> 2 steps.
  - Walk Right 5 to (11, 16) [z=1] -> 5 steps.
  - Walk Right 5 to (16, 16) [z=1] -> 5 steps.
  - Walk Right 5 to (21, 16) [z=1] -> 5 steps.
  - Walk Down 2 to descend stairs to (21, 18) [z=0] -> 2 steps.
  - Walk Right 4 to (25, 18) [z=0] -> 4 steps.
  - Walk Up 6 to (25, 12) [z=0] -> 6 steps.
  - **Total Steps Consumed**: 2 + 2 + 5 + 5 + 5 + 2 + 4 + 6 = **31 steps**.
  - **Reconciled Remaining Steps**: 247 - 31 = **216 steps remaining** on Turn 68527 (standing at 25, 12).
  - This perfectly matches the RAM's step counter, ensuring 100% accurate, drift-free step-keeping!