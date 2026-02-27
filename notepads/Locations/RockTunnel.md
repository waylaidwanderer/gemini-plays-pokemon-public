# Rock Tunnel
- Navigating using tile collision data ('TYPE_xxxx') since it's dark and I don't have Flash.
- Entrance is at Route 10 (8, 16).
[Turn 7501 Reflection]
- Path so far: Entered at (15, 3). Walked Right to X=21, then Down. Defeated Pokemaniac near (21, 8).
- Map marker placed for Pokemaniac at (21, 10).
- Lesson Learned: NEVER use blind `execute_macro` for battle menus. I threw a Poke Ball by accident. Use `execute_battle_turn` instead.
- Lesson Learned: Always check Game State position after moving. Encounters interrupt macros.
[Current Status]
- True Location: Confirmed at (15, 7).
- Traced X=13 on the grid: it is a SOLID WALL from Y=3 to Y=11.
- The ladder at (17, 11) is completely walled off from the north and right (X=18/19 are walls).
- Lower right (X=20-28, Y=10-13) is a dead end.
- Upper right (X=30, Y=4-7) is a dead end.