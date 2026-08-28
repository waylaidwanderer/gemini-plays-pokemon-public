# Viridian Gym Navigation & Mapping Log

## Gym Status
- Unlocked! Entered Gym on Turn 64190.
- Goal: Defeat Giovanni for the Earth Badge (8th Badge).

## Current Position
- Player is at `(5, 12)` inside the Viridian Gym.
- Gym Guide is currently wandering near `(6, 11)`.

## Gym Layout Notes
- The Gym contains one-way spinner (arrow) tiles.
- (6, 12) is a LEFT spinner tile.
- Row 13, Columns 6 and 7 are occupied by gold wall blocks.
- Columns 2 and 3 are occupied by walls/obstacles.

## Exploration Plan
- Use Python scripts to probe walkability of adjacent tiles.
- Trace safe paths to avoid getting spun out of bounds or into unwanted trainer fights before we are ready.
- Locate Giovanni (usually at the top center/right).