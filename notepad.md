# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Objectives
1. **Find Floria**: Located at Route 36 (North of Route 35).
2. **Get SquirtBottle**: Return to Flower Shop (19, 1) after finding Floria.
3. **Clear Sudowoodo**: Use SquirtBottle on Route 36.

### Exploration Status
- **East Side (x>17)**: DEAD END. Blocked by walls/houses.
- **Center (x=6-17)**: Blocked by Underground Entrance (9, 5).
- **West Side (x<6)**:
  - **Radio Tower Area**: North path (x=3) is a dead end.
  - **Tracks (x=0-1)**: Potential path North? Need to find access point (likely South near Route 34 junction).

### Validated Locations
- **Flower Shop**: (19, 1).
- **Underground Entrance**: (9, 5).
- **Radio Tower**: (5, 15).
- **Gym**: (24, 7).

### Quest Log
- **Badges**: Zephyr, Hive, Plain.
- **Party**: Quilava (27), Bellsprout (6), Togepi (5), Rattata (8), Igglybuff (5).
- **West Narrow Path**: Explored (x=3, y=15). Dead end to the North.
- **Correction**: The area around the Gym (24, 7) is a dead end for the North path. The wall at y=5 seems to block the entire center. Need to find a gap, possibly on the far West (x=0-1) or verify if the Underground has a different exit.
- **Hypothesis**: Use 'find_reachable_exits' to check if the North edge (y=0) is reachable from current position. If not, must find a new route (e.g. West tracks).
- **Tracks**: Possible path North along the tracks (x=0-1)? Need to find access point (likely South).