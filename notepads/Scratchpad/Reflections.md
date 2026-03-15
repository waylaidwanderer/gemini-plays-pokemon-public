[100-Turn Reflection]
- Error Analysis: The "input eating" mechanic of text boxes continues to be a major factor in macro failures. I must explicitly wait for text to clear (or manually clear it with safe_mash_b) before invoking any custom tools that navigate menus.
- Map Hygiene: Placed a marker for the Celadon City warp on Route 16.

[50-Turn Reflection (Turn 34884)]
- Error Analysis (TM/HM Input Eating): When using an HM/TM, the text "Teach [MOVE] to a POKeMON?" appears simultaneously with the party menu. Sending directional inputs immediately causes them to be eaten as text-advances. I must explicitly send an 'A' press or sleep to clear this hidden text state before attempting to navigate the party menu.