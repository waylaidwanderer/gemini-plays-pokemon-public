# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Task
- **Mechanic**: Stepping on (7, 15) transitions between Map 3_14 (Upper) and Map 3_13 (Lower/Hole State).
- **Goal**: Find the B1F drop on Map 3_13.

### Notes
- **Map 3_13**: Burned Tower 1F (Outer). Warp at (10, 9) leads to 3_14.
- **Map 3_14**: Burned Tower 1F (Center/Rival Room). Exit at (7, 15) leads to 3_13 (Outer).
- **Goal**: Return to 3_14 via (10, 9). Find the *real* B1F hole in the center room (NOT the exit at 7, 15).
- **Map 3_13**: Tile (15, 4) is a BREAKABLE ROCK (impassable), despite being TYPE_3fe2. BFS will fail here. Go around via the Left side (Col 4).
- **Map 3_13**: Item at (14, 2) is blocked by Breakable Rock at (15, 4). Requires Rock Smash.
- **Exploration**: Checking bottom-right area (Cols 14-16) before leaving.