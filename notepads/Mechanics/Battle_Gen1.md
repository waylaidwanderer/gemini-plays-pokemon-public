- "But, it failed!" refers to the move just executed by the current Pokemon (e.g., an enemy's stat-dropping move failing because the stat can't go lower, or Gen 1 AI quirks). It does NOT mean the player's previous attack missed.
[Mechanics/Combat]
- Gen 1 battle menus WRAP AROUND (pressing Down at move 4 goes to move 1).
- Cursor position is remembered per Pokemon. Must accurately track current_move_index.
- The battle cursor RESETS to index 1 in two cases:
  1. At the start of a NEW BATTLE.
  2. After a Pokemon LEVELS UP.
- It is REMEMBERED between enemy Pokemon within the SAME battle (if no level up occurred).