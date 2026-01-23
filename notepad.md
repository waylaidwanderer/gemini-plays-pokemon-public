# Pokémon Crystal Playthrough
- Started: Friday, January 16, 2026

### Current Objectives
1. **Find Floria**: Located at Route 36 (North of Route 35).
2. **Get SquirtBottle**: Return to Flower Shop (19, 1) after finding Floria.
3. **Clear Sudowoodo**: Use SquirtBottle on Route 36.

### Navigation Hypothesis
- **Finding**: `find_reachable_exits` failed to find a North exit because it ignores `unseen` tiles.
- **Analysis**: XML data shows a walkable corridor North around x=32/33 (East of Gym) that leads into `unseen` tiles at Row 1.
- **Goal**: Navigate to x=33, then push North into the fog of war to reveal the Route 35 Gatehouse.

### Validated Routes
- **Flower Shop**: (19, 1).
- **Floria's Sister**: (29, 5).
- **Underground**: Connects South (11, 29) to North (9, 5).
- **Randy's House**: (33, 9).

### Quest Log
- **Badges**: Zephyr, Hive, Plain.
- **Party**: Quilava (27), Sentret (2), Bellsprout (6), Togepi (5), Rattata (8), Igglybuff (5).