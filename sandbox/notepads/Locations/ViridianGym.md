# Viridian Gym Navigation & Mapping Log

## Gym Status
- Unlocked! Entered Gym on Turn 64190.
- Goal: Defeat Giovanni for the Earth Badge (8th Badge).

## Gym Layout Notes
- The Gym contains one-way spinner (arrow) tiles.
- Columns 2 and 3 are occupied by walls/obstacles.

## Exploration Plan
- Use Python scripts to probe walkability of adjacent tiles.
- Trace safe paths to avoid getting spun out of bounds or into unwanted trainer fights before we are ready.
- Locate Giovanni (usually at the top center/right).
## Gym Inhabitants & Defeated Trainers
- **(6, 14) Defeated Trainer:** Defeated the level 35 Grimer trainer at `(6, 14)` (fought at `(7, 15)` on Turn 64231). This trainer remains as a solid block at `(6, 14)` facing DOWN.
- **Gym Guide:** SPRITE_cdfc (Gym Guide) wanders around Row 11: `(6, 11) -> (4, 11) -> (5, 11) -> (6, 11) -> (7, 11) -> (8, 11) -> (9, 11)`.

## One-Way Spinner Transitions (Discovered Ground Truth)
- **(11, 4) going Right:** Spins and pushes the player to `(12, 5)`.
- **(15, 6) going Right:** Spins and pushes the player to `(17, 6)`.
- **(16, 3) going Right:** Spins and pushes the player to `(17, 4)`.
- **(15, 5) going Right:** Spins and pushes the player to `(17, 6)`.
- **(19, 3) going Down:** Spins and pushes the player to `(20, 5)`.

## Discovered Walkable Paths summary (Turn 65163)
- **Identified Safe Paths on the Platform:**
  - **Column 1:** Walkable rows: [1, 6, 7, 8]
  - **Column 2:** Walkable rows: [1, 6, 7, 8]
  - **Column 3:** Walkable rows: [1, 4, 5, 6, 7, 8]
  - **Column 4:** Walkable rows: [1, 2, 3, 4, 5, 8]
  - **Column 5:** Walkable rows: [1, 2, 3, 4, 5, 6, 7, 8]
  - **Column 6:** Walkable rows: [1, 2, 3, 6, 7, 8]
  - **Column 7:** Walkable rows: [1, 2, 3, 6, 7, 8]
  - **Column 8:** Walkable rows: [1, 2, 3, 7]
  - **Column 9:** Walkable rows: [1, 2]
  - **Column 10:** Walkable rows: [1, 2, 3]
  - **Column 11:** Walkable rows: [1, 2, 3, 4]
  - **Column 12:** Walkable rows: [1, 2, 3, 4]
  - **Column 13:** Walkable rows: [3]

- **Dead Ends & Obstacles:**
  - Node (1, 1) is blocked going: ['Left', 'Down', 'Up']
  - Node (1, 6) is blocked going: ['Left', 'Up']
  - Node (1, 7) is blocked going: ['Left']
  - Node (1, 8) is blocked going: ['Left', 'Down']
  - Node (2, 1) is blocked going: ['Down', 'Up']
  - Node (2, 6) is blocked going: ['Up']
  - Node (2, 8) is blocked going: ['Down']
  - Node (3, 1) is blocked going: ['Up', 'Down']
  - Node (3, 4) is blocked going: ['Left', 'Up']
  - Node (3, 5) is blocked going: ['Left']
  - Node (3, 6) is blocked going: ['Right']
  - Node (3, 7) is blocked going: ['Right']
  - Node (3, 8) is blocked going: ['Down']
  - Node (4, 1) is blocked going: ['Up']
  - Node (4, 2) is blocked going: ['Left']
  - Node (4, 3) is blocked going: ['Left']
  - Node (4, 5) is blocked going: ['Down']
  - Node (4, 8) is blocked going: ['Down', 'Up']
  - Node (5, 1) is blocked going: ['Up']
  - Node (5, 4) is blocked going: ['Right']
  - Node (5, 5) is blocked going: ['Right']
  - Node (5, 6) is blocked going: ['Left']
  - Node (5, 7) is blocked going: ['Left']
  - Node (5, 8) is blocked going: ['Down']
  - Node (6, 1) is blocked going: ['Up']
  - Node (6, 3) is blocked going: ['Down']
  - Node (6, 6) is blocked going: ['Up']
  - Node (6, 8) is blocked going: ['Down']
  - Node (7, 1) is blocked going: ['Up']
  - Node (7, 3) is blocked going: ['Left', 'Down', 'Up', 'Right']
  - Node (7, 8) is blocked going: ['Down']
  - Node (8, 1) is blocked going: ['Up']
  - Node (9, 1) is blocked going: ['Up']
  - Node (9, 2) is blocked going: ['Down']
  - Node (10, 1) is blocked going: ['Up']
  - Node (11, 1) is blocked going: ['Up']
  - Node (12, 1) is blocked going: ['Up']
  - Node (12, 2) is blocked going: ['Right']

- **Mapping Progress:**
  - Total Walkable Tiles (Visited): 58
  - Remaining Unexplored Target Nodes: [[10, 3], [11, 4], [8, 3], [8, 7], [13, 3], [12, 3], [12, 4]]
