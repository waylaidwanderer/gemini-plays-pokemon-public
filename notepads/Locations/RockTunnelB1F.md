# Rock Tunnel B1F - Overworld Mapping & Navigation

## Map Dimensions
- Dimensions: Width = 40, Height = To Be Determined (visually confirmed y >= 24).

## Mapped Coordinates & Layout
- **Ladder to 1F (Central Section):** Located at `(23, 11)`. Connects to Rock Tunnel 1F at `(17, 11)`.

### Verified Walkable Coordinates (Physically stepped on in this session):
- (23, 11), (22, 11), (21, 11), (20, 11), (19, 11), (18, 11)
- (17, 11), (17, 12), (17, 13), (17, 14), (17, 15), (17, 16), (17, 17), (17, 18), (17, 19)
- (16, 19), (15, 19), (14, 19)
- (14, 18), (14, 17), (13, 17), (12, 17), (11, 17), (10, 17)
- (10, 18), (10, 19), (10, 20), (10, 21), (10, 22), (10, 23), (10, 24), (9, 24), (8, 24), (7, 24), (6, 24), (5, 24), (4, 24), (3, 24), (2, 24), (2, 25), (2, 26), (2, 27), (10, 16), (10, 15), (10, 14), (10, 13), (10, 12), (10, 11), (9, 11), (8, 11), (7, 11), (6, 11), (10, 6), (10, 5), (10, 4), (10, 3), (10, 10), (10, 9), (10, 8), (10, 7), (22, 12), (22, 13), (23, 13), (21, 13), (20, 13), (19, 13), (18, 13), (5, 11), (4, 11), (3, 11), (2, 11), (2, 12), (2, 13), (2, 14), (2, 15), (2, 16), (2, 17), (2, 18), (2, 19), (2, 20), (2, 21), (3, 20), (4, 20), (5, 20), (5, 19), (5, 18), (5, 17), (5, 16), (5, 15), (5, 14), (5, 13), (5, 12)


### Defeated Trainers:
- **Hiker at (6, 11):** Engaged and defeated on Turn 11113-11141.
  - Roster: Geodude Lv 21, Geodude Lv 21, Graveler Lv 21.

## Verified Collisions
- (13, 19): Rock Wall (Turn 11056)

## Dark Cave Navigation & Visual Illusions
- **The Illusion of Walkability:** In pitch-black caves like Rock Tunnel, unrendered rock walls and walkable corridors are both drawn as identical pure black pixels.
- **Coordinate Grid Pitfalls:** The overlay coordinate grid renders on top of pitch-black unrendered space. This can easily lead to the hallucination that a coordinate is "empty walkable black space" when it actually contains a solid rock wall.
- **Strict Empirical Standard:** Walkability CANNOT be determined visually in dark zones. Every single tile must be physically stepped on (or bumped into to verify collision) before being logged as verified.
