# Route 1 — Verified Coordinates & Navigation

## Map Connections
- **South Exit (to Pallet Town)**: `x = 10..11, y = 35` -> `Down` warps to Pallet Town `(10..11, 0)`.
- **North Exit (to Viridian City)**: `x = 10..11, y = 0` -> `Up` warps to Viridian City `(20..21, 35)`.

## Key NPCs
- **Poké Mart Sample Clerk (Free Potion)**: Wanders around `(5, 24..25)` in the west-central clearing.

## Verified Northbound Path (Pallet -> Viridian)
1. Enter at `(10, 35)` -> `Up` x 7 to `(10, 28)`.
2. `Left` x 2 to `(8, 28)` -> `Up` x 2 to `(8, 26)` -> `Right` x 5 to `(13, 26)` -> `Up` x 6 to `(13, 20)`.
3. `Left` x 8 to `(5, 20)` -> `Up` x 6 to `(5, 14)`.
4. `Right` x 10 to `(15, 14)` (avoids Boy NPC at `(14, 13)`) -> `Up` x 3 to `(15, 11)`.
5. `Left` x 4 to `(11, 11)` -> `Up` x 5 to `(11, 6)` -> `Right` x 3 to `(14, 6)` -> `Up` x 2 to `(14, 4)` -> `Left` x 3 to `(11, 4)` -> `Up` x 5 into Viridian City.

## Verified Southbound Ledge Chain (Viridian -> Pallet, Minimal Grass)
1. Enter at `(10, 0)` -> `Down` x 3 to `(10, 3)` -> `Left` x 2 to `(8, 3)`.
2. `Down` along column `x = 8` down to `(8, 18)` (hops 3 ledges at `y = 5, 9, 13` with ZERO tall grass tiles!).
3. `Right` x 5 to `(13, 18)` -> `Down` to `(13, 26)` (hops `y = 19` ledge; 4 grass tiles `y = 22..25`).
4. `Left` x 3 to `(10, 26)` -> `Down` to `(10, 35)` -> `Down` into Pallet Town `(10, 0)` (hops `y = 27` ledge; 4 grass tiles `y = 32..35`).

