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
## Walkability Discoveries inside Viridian Gym (Updated Turn 64255)
- **Start Position:** Entrance at `(5, 15)` or `(6, 15)`. We started at `(6, 15)`.
- **(6, 14) Defeated Trainer:** Defeated the level 35 Grimer trainer at `(6, 14)` (which was triggered/fought at `(7, 15)` on Turn 64231). This trainer remains as a solid block at `(6, 14)` facing DOWN.
- **Walkable Tiles (Column 5):**
  - Going LEFT from `(6, 15)` to `(5, 15)` is completely walkable.
  - From `(5, 15)`, we can walk vertically UP Column 5 all the way to `(5, 8)` without blockage or spin.
  - The tile `(5, 8)` is BLOCKED going UP.
- **Gym Guide:** SPRITE_cdfc (Gym Guide) is currently wandering around Row 11: `(6, 11) -> (4, 11) -> (5, 11) -> (6, 11) -> (7, 11) -> (8, 11) -> (9, 11)`.