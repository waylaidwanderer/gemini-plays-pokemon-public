# Rock Tunnel
- Navigating using tile collision data ('TYPE_xxxx') since it's dark and I don't have Flash.
- Entrance is at Route 10 (8, 16).
[Turn 7501 Reflection]
- Path so far: Entered at (15, 3). Walked Right to X=21, then Down. Defeated Pokemaniac near (21, 8).
- I need to place a map marker for the defeated trainer once I return to the overworld.
- Lesson Learned: NEVER use blind `execute_macro` for battle menus. I threw a Poke Ball by accident. Use `execute_battle_turn` instead.
- Lesson Learned (from Route 10): ALWAYS trust the system's identification of tiles (e.g., `TYPE_5519` = bush, not Cut tree). Do not let confirmation bias override factual data.
- Current Location: (24, 12)
- Path history: (15,3) -> Right to (21,3) -> Down to (21,12) -> Right to (24,12).
- Bottom right area (X=20..28, Y=10..13) is a dead-end room. Backtracking to (21, 8) to explore left.
- Navigating from (21, 8) up and left around the rock wall. Now at (16, 7). Path continues left.