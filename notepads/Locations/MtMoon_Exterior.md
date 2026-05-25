# Mt. Moon Exterior (Map 0_14) Location Records

## Overview & Connections:
- Located on the eastern end of Route 3, this area contains the Mt. Moon Pokémon Center and the main entrance to Mt. Moon 1F.
- West exit connects directly to Route 3 (Map 0_2) at (0, 10).
- East entrance leads to Mt. Moon 1F.
- Contains the Route 3 Pokémon Center.

## Structural Layout & Key Pathing:
- **Northern and Southern Corridors**: The map is split horizontally by a ledge on Row 7.
- **Row 4 & Row 5 Passageway**:
  - Column 17 has solid trees (TYPE_2889) blocking Rows 6-10.
  - Rows 4 and 5 at Column 17 are completely clear of trees (TYPE_3fe2), providing the primary passageway to go east from the western section.
  - Note: Bug Catcher Greg stands at (19, 5), so walking east requires using Row 4 to bypass him.
- **Row 7 Horizontal Ledge**:
  - Separates the northern area (Rows 4-6) from the southern area (Rows 8-10).
  - Ledge Gap at (11, 7): Flat ground (TYPE_3fe2), completely passable in both directions. Allows bypassing the horizontal ledge on Row 7 by walking north from (11, 9) to (11, 6) (verified on Turn 7319).
  - Ledge Gap at (27, 7): Flat ground (TYPE_3fe2), completely passable in both directions. Allows bypassing the horizontal ledge on Row 7 by walking south from (27, 6) to (27, 8) (verified on Turn 7365).
  - Ledge Gap at (37, 7): Flat ground (TYPE_3fe2). Hypothesized to be another bidirectional ledge gap.
- **Eastern Blockage (Columns 28-31)**:
  - Rows 4-7 are occupied by a massive mountain wall of TYPE_2889 starting at Column 28, blocking direct eastern progression on those rows.
  - **Empirical Collision Verification**: Physically tested on Turn 7355. Walking Right from (27, 5) against the wall at (28, 5) resulted in zero movement, confirming the wall is solid and impassable.
  - To continue east towards Mt. Moon, players must walk south through the (27, 7) ledge gap onto Row 8 or Row 9, which are completely clear of mountain walls to the east.

## Defeated Trainers:
- Bug Catcher Colton at (10, 6)
- Youngster Albert at (14, 5)
- Lass Janice at (15, 9)
- Bug Catcher Greg at (19, 5)
- Lass at (23, 4)
- Bug Catcher at (24, 6)
- Youngster Ben at (22, 9)
- Lass at (33, 9)
- **Cave Entrance Verification (Columns 47-48)**: On Turn 7406, standing at (47, 4), we physically tested (47, 3) by pressing UP and bumped (visited 0 tiles), confirming (47, 3) is a solid, impassable wall. On Turn 7422, standing at (48, 4), we are testing (48, 3) by pressing UP.