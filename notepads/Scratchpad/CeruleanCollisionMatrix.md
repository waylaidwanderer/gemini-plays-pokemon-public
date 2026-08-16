# Cerulean City - Spatial Collision Matrix & Verified Boundaries

## Legend
- P: Passable / Walkable
- W: Impassable Wall / House / Obstacle
- L: One-way Ledge (Hopping South)
- D: Door / Map Warp
- C: Canal Water
- T: Tree / Bush Barrier
- ?: Unexplored / Northern Target Area

## Sector Breakdown
### Rows 0–13 (Northern Cerulean & Route 24 Access)
- (0..7, 0..13): Canal Water [C]
- (12..15, 4..7): Badge Master House [?]
- (20..23, 0..13): Route 24 North Highway [?]
- (26..29, 8..11): Burglarized House [?]

### Rows 14–19 (Central Boundary Partition)
- (0..7, 14..17): Canal Stone Barrier [W] & Water [C]
- (8..9, 15): One-way Ledge Hopping South [L] (Tested Turn 1389)
- (10..11, 15): Fence [W] (Tested Turn 1408)
- (12..17, 14..15): Trade House [W], Door at (13, 15) [D] (Tested Turn 1203/1444)
- (18..21, 14..17): Pokémon Center [W], Door at (19, 17) [D] (Tested Turn 1210/1435)
- (22..23, 17): Fence Post [W] (Tested Turn 1391 at 22,17; Turn 1464 at 23,17)
- (24..31, 16..19): Cerulean Gym [W], Door at (30, 19) [D] (Tested Turn 1233)
- (32..37, 19): One-way Ledge Hopping South [L] (Tested Turn 1451/1454)

### Rows 20–27 (Southern Plaza & Thoroughfare)
- (0..22, 18..19): Wide Open Thoroughfare [P] (Route 4 entry at 0,19)
- (22..34, 20..21): Gym Courtyard & Pavement [P]
- (12..15, 22..25): Bike Shop [W], Door at (13, 25) [D] (Tested Turn 1420)
- (24..27, 22..25): Pokémart [W], Door at (25, 25) [D] (Tested Turn 1223)
- (28..33, 24..25): Slowbro House [W], Backyard at (28..32, 26..27) [P] (Tested Turn 1429)
- (6..34, 26..27): Continuous South Street [P]

### Rows 28–31 (South Boundary & Route 5 Approach)
- (16..17, 28): Open Pavement [P]
- (16, 29): Barrels [W], (17, 29): Signpost [W]
- (11..25, 30..31): South Dashed Pavement Avenue [P]