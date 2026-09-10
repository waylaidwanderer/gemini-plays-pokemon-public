# Cerulean Cave Frontier & Junction Tracking

## Verified Collisions & Impassable Boundaries (2F)
- (2, 1), (5..10, 2), (9, 2), (17, 2), (10, 1..3), (12, 3), (14, 2..4)
- (8, 4..5), (11, 4), (20, 4), (8, 5), (15, 6), (5..14, 6), (17, 6), (21, 6)
- (22, 5), (23, 6), (14, 10), (11, 11), (13, 12), (13, 11..13), (15, 12), (16, 12)
- (18..20, 12), (16, 13..14), (14, 14..16), (15, 14), (22, 8..10), (24, 8..10)
- (25, 10..11), (17, 10), (17, 14), (18, 14), (19, 14), (20, 12..20 solid wall)
- (21, 14), (22, 16), (27, 12..13), (27, 15), (28, 8), (28, 13), (29, 7..8), (29, 10..11)

## Verified Map Topology (2F)
- **North Branch (cols 1..22, rows 1..5)**:
  - Ladder E at (9, 1) <-> Row 1 West (3, 1) <-> (3, 3) <-> Row 3 East (9, 3) <-> Column 9 South (9, 5) <-> Row 5 East (13..16, 5) <-> Central S-Bypass (18, 1..3) <-> (22, 2..4) <-> (21, 5) <-> (22, 5).
  - **South Branch (cols 11..27, rows 7..17)**:
  - Accessible via (22, 7) <-> Column 23 (23, 7..15) <-> Row 11 (14..23, 11) <-> Row 13 (17..27, 13) <-> Row 15 (15..26, 15) <-> Row 17 (21..27, 17 SE dead-end).
  - Column 20 is a solid rock barrier separating East (cols 21-29) and West (cols 1-19) in rows 12-20.

- Additional verified collisions: (13, 10..11), (13, 13..15), (14, 10), (14, 15), (15, 10), (15, 12), (16, 12..14).