# Warehouse Puzzle
- Goal: Reach Director at (7, 11). Needs Card Key? Or just switches.
- Switch 1 (Silver Room): "Ice in your veins...". Currently ON (Toggled).
- Switch Connection: Switch 1 -> Grunt at (22, 24) ("I feel a chill").
- Grunt (22, 24): Investigate him now. He might have moved or is battling.
- Switch 2: Unfound. Likely behind Gentleman at (7, 23).
- Switch 3: Unfound.
- Trap: (21, 31)-(22, 31) warps to (18, 6). Verified.
- Connection: Stairs at (21, 25) in 3_54 lead to West Corridor (3, 2).
- Exit: Mat at (21, 29) in 3_54 leads to Goldenrod City (9, 5) (North Entrance).

# Hidden Corridor (Col 6/7)
- Entrances: (6, 19) & (6, 23). Currently SOLID/LOCKED.
- Theory: Switches open these walls.
- Blocker: Gentleman at (7, 23).
- Warp Connection: 3_54 (21, 25) -> 3_53 (3, 2). Confirmed.
- Map 11_2: Goldenrod City Surface.
- Map 3_54: North Entrance Hall & Silver Room.
- Map 3_53: Public Underground & Warehouse (Likely shared map).
- Problem: Navigation to (11, 29) failed.
- Cause: "NPC Blocker" at (16, 23) on the direct path. BFS doesn't see it.
- Solution: Manually route South to (19, 28) to use the gap at Row 28.
- Plan: Move to (19, 28) -> Move West to (11, 29) -> Enter Underground.
- Switch 1 (Silver Room): ON.
- Key: Have Basement Key.
- Access Denied: South Entrance (11, 29) is blocked by a stubborn Rocket Grunt at (16, 23).
- Conclusion: Must use North Entrance (9, 5).
- Revised Plan:
  1. Return to North Entrance (9, 5).
  2. Enter Warehouse Entrance Hall (3_54).
  3. Go to Silver Room -> Maze Stairs (23, 3).
  4. Check Grunt at (22, 24) in Maze (3_53). Switch 1 might have affected him.
  5. If no luck, go to West Corridor (3_53) and check Gentleman at (7, 23).
- Goal: Find Switch 2 & 3 to open walls at (6, 19/23).