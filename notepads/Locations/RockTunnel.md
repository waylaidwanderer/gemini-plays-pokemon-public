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

# Rock Tunnel 1F
[Tile Dictionary]
- TYPE_3fe2: Walkable Floor
- TYPE_2889: Impassable Rock Wall
- TYPE_2770: Impassable Rock Wall

[Layout Notes]
- (15, 3): Entrance from Route 10
- (17, 11): Ladder (Unreachable from start area)
- (21, 10): Pokemaniac
- (24, 12): Dead End
- (30, 4): Dead End

# B1F Routing
- [Turn 7575] Arrived B1F at (33,25).
- Path: From (26,30) Pokemaniac, follow bottom wall left then up to (15,28) Jr Trainer.
- Path: From (20,21) Pokemaniac, head north and east to (30,10) Hiker.
- Path: From (30,10) Hiker, head north to (33,5) Hiker.
- Found Ladder to 1F at (27, 3).