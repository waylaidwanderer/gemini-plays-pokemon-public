# Rock Tunnel B1F - Overworld Mapping & Navigation

## Map Dimensions
- Dimensions: Width = 40, Height = To Be Determined (visually confirmed y >= 24).

## Mapped Coordinates & Layout
- **Ladder to 1F (Central Section):** Located at `(23, 11)`. Connects to Rock Tunnel 1F at `(17, 11)`.

### Verified Walkable Coordinates (Physically stepped on in this session):

- Row 3: (10, 3), (28, 3), (29, 3), (30, 3), (31, 3), (32, 3), (33, 3), (34, 3), (35, 3), (36, 3), (37, 3)

- Row 4: (10, 4), (37, 4)

- Row 5: (10, 5), (37, 5)

- Row 6: (10, 6), (37, 6)

- Row 7: (10, 7), (37, 7)

- Row 8: (10, 8), (37, 8)

- Row 9: (10, 9), (37, 9)

- Row 10: (10, 10), (37, 10)

- Row 11: (2, 11), (3, 11), (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11), (17, 11), (18, 11), (19, 11), (20, 11), (21, 11), (22, 11), (23, 11), (37, 11)

- Row 12: (2, 12), (5, 12), (10, 12), (17, 12), (22, 12), (37, 12)

- Row 13: (2, 13), (5, 13), (10, 13), (17, 13), (18, 13), (19, 13), (20, 13), (21, 13), (22, 13), (23, 13), (37, 13)

- Row 14: (2, 14), (5, 14), (10, 14), (17, 14), (37, 14)

- Row 15: (2, 15), (5, 15), (10, 15), (17, 15), (37, 15)

- Row 16: (2, 16), (5, 16), (10, 16), (17, 16), (20, 16), (21, 16), (22, 16), (23, 16), (24, 16), (25, 16), (26, 16), (27, 16), (28, 16), (29, 16), (30, 16), (31, 16), (32, 16), (33, 16), (34, 16), (35, 16), (36, 16), (37, 16)

- Row 17: (2, 17), (5, 17), (10, 17), (11, 17), (12, 17), (13, 17), (14, 17), (17, 17), (20, 17), (21, 17), (22, 17), (23, 17), (24, 17), (25, 17), (26, 17), (27, 17), (37, 17)

- Row 18: (2, 18), (5, 18), (10, 18), (14, 18), (17, 18), (20, 18), (37, 18)

- Row 19: (2, 19), (5, 19), (10, 19), (13, 19), (14, 19), (15, 19), (16, 19), (17, 19), (20, 19), (23, 19), (24, 19), (25, 19), (26, 19), (27, 19), (28, 19), (29, 19), (30, 19), (31, 19), (32, 19), (33, 19), (34, 19), (35, 19), (36, 19), (37, 19)

- Row 20: (2, 20), (3, 20), (4, 20), (5, 20), (10, 20), (11, 20), (14, 20), (15, 20), (17, 20), (23, 20)

- Row 21: (2, 21), (10, 21), (14, 21), (15, 21), (16, 21), (17, 21), (23, 21)

- Row 22: (10, 22), (22, 22), (23, 22), (24, 22), (25, 22)

- Row 23: (10, 23), (22, 23), (25, 23)

- Row 24: (2, 24), (3, 24), (4, 24), (5, 24), (6, 24), (7, 24), (8, 24), (9, 24), (10, 24), (11, 24), (14, 24), (15, 24), (16, 24), (17, 24), (18, 24), (19, 24), (20, 24), (21, 24), (22, 24)

- Row 25: (2, 25), (14, 25), (15, 25)

- Row 26: (2, 26), (14, 26), (15, 26)

- Row 27: (2, 27), (3, 27), (4, 27), (5, 27), (6, 27), (7, 27), (11, 27), (14, 27), (15, 27)

### Defeated Trainers:
- **Hiker at (6, 11):** Engaged and defeated on Turn 11113-11141.
  - Roster: Geodude Lv 21, Geodude Lv 21, Graveler Lv 21.

## Verified Collisions
- (13, 19): Rock Wall (Turn 11056)

## Dark Cave Navigation & Visual Illusions
- **The Illusion of Walkability:** In pitch-black caves like Rock Tunnel, unrendered rock walls and walkable corridors are both drawn as identical pure black pixels.
- **Coordinate Grid Pitfalls:** The overlay coordinate grid renders on top of pitch-black unrendered space. This can easily lead to the hallucination that a coordinate is "empty walkable black space" when it actually contains a solid rock wall.
- **Strict Empirical Standard:** Walkability CANNOT be determined visually in dark zones. Every single tile must be physically stepped on (or bumped into to verify collision) before being logged as verified.
