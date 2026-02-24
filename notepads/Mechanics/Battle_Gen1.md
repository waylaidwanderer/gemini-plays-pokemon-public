- "But, it failed!" refers to the move just executed by the current Pokemon (e.g., an enemy's stat-dropping move failing because the stat can't go lower, or Gen 1 AI quirks). It does NOT mean the player's previous attack missed.
[Mechanics/Combat]
- Gen 1 battle menus WRAP AROUND (pressing Down at move 4 goes to move 1).
- Cursor position is remembered per Pokemon. Must accurately track current_move_index.
- The battle cursor RESETS to index 1 in two cases:
  1. At the start of a NEW BATTLE.
  2. After a Pokemon LEVELS UP.
- It is REMEMBERED between enemy Pokemon within the SAME battle (if no level up occurred).
[Cursor Memory]
- In Gen 1, menu cursor positions are remembered! The Item menu remembers the last used item position globally. The Fight menu remembers the last used move per-Pokemon. The Party menu remembers the last selected Pokemon. ALWAYS check the visual cursor position before using navigation tools, as assuming it resets to index 1 will cause wrong selections.
- Wrap/Bind Mechanic: In Gen 1, trapping moves like Wrap completely immobilize the target. The move selection phase is skipped entirely and you cannot attack until the effect ends. Do not try to use battle menus during Wrap.