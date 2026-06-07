# Koga's Plateau Elevation Split & True Northwest Victory Route Answers

## 1. Socratic Question 1: The Row 5 Column 15-21 Tree Wall
- **Why (20, 5) is physically blocked on ground level**: (20, 5) contains a solid tree trunk tile of `TYPE_2889`. This is part of a large tree structure (spanning (20, 4), (20, 5), (21, 4), (21, 5)).
- **Cite specific tile types and visual evidence on Row 5**:
  - (16, 5) is `TYPE_2889` (large tree trunk - impassable)
  - (17, 5) is `TYPE_2889` (large tree trunk - impassable)
  - (20, 5) is `TYPE_2889` (large tree trunk - impassable)
  - (21, 5) is `TYPE_2889` (large tree trunk - impassable)
- **How this affects your pathway to the East**: This tree wall physically blocks any direct horizontal ground-level pathway to the East on Row 5, forcing us to step Down 1 to Row 6 (which is completely open) to proceed East.

## 2. Socratic Question 2: Ground-Level Bypasses of Koga's Plateau in Safari Zone North
- **Ground-Level Path to West Transition**:
  - From current position (19, 5), walk Down 1 to (19, 6).
  - Walk East 6 steps to (25, 6).
  - Walk Up 3 steps to (25, 3).
  - Walk West 25 steps to (0, 3).
  - Walk Down 9 steps to the West transition at (0, 12).
  - Total step cost: 1 + 6 + 3 + 25 + 9 = 44 steps!
- **How it mathematically avoids both the water lake and Koga's Plateau**:
  - The central water lake in Safari Zone North is located around Rows 8-13 (on Columns 8-11) and Rows 14-19 (on Columns 4-7).
  - Koga's Plateau is located around Rows 20-22 (on Columns 18-24).
  - Because Row 3 is completely North of both the lake (maximum north row 8) and Koga's Plateau (maximum north row 20), walking along Row 3 completely avoids both obstacles.
- **Is this ground-level route superior to climbing Koga's Plateau at (22, 23)? Why or why not?**:
  - Yes! It is vastly superior because climbing onto Koga's Plateau requires a long detour down to Row 24 to reach the staircase at (22, 23). The ground-level route takes only 44 steps and avoids multiple staircase elevation transitions, which are highly complex and prone to navigation/pathfinding errors.

## 3. Socratic Question 3: Chronological Step-Budget Reconciliation
- **Step-by-step math of physical overworld steps consumed since Turn 68670**:
  - Turn 68670: Standing at (12, 5) with exactly **156 steps remaining**.
  - Turn 68679: Walked Down 2 steps to (12, 7) [consuming 2 steps, remaining: 154].
  - Turn 68680: Pressed Left 1 step to test (11, 7), bumping and stopping at (12, 7) [consuming 1 step, remaining: 153].
  - Turn 68687: Walked Up 1, Right 6, Up 1, Right 2 to (19, 5) [colliding with tree at (20, 5) and stopping at (19, 5)] [consuming 10 steps, remaining: 143].
  - **Reconciled Remaining Steps**: 156 - 2 - 1 - 10 = **143 steps remaining** on Turn 68700/68706. This perfectly matches the RAM's step counter, ensuring 100% accurate, drift-free step-keeping.
- **How to update chronological logs to ensure perfect tracking accuracy**:
  - We have successfully appended the missing overworld movement entries for Turn 68679, Turn 68680, and Turn 68687 to 'Scratchpad/SafariZone_West_Route' to ensure perfect tracking accuracy.