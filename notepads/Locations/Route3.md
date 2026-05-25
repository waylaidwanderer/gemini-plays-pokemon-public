# Route 3 (Map 0_14) Location Records

## Connections:
- West exit connects directly to Pewter City (Map 0_2) at (0, 10) via map boundary transition.
- East exit connects to Route 4 West / Mt. Moon Exterior (Map 0_15) at (59, 0) and (61, 0) via northern boundary map connections.

## Structural Layout & Key Pathing:
- **Northern and Southern Corridors**: The map is split horizontally by a ledge on Row 7.
- **Row 4 & Row 5 Passageway**:
  - Column 17 has solid trees (TYPE_2889) blocking Rows 6-10.
  - Rows 4 and 5 at Column 17 are completely clear of trees (TYPE_3fe2), providing the primary passageway to go east from the western section.
  - Note: Bug Catcher Greg stands at (19, 5), so walking east requires using Row 4 to bypass him.
- **Row 7 Horizontal Ledge**:
  - Separates the northern area (Rows 4-6) from the southern area (Rows 8-10).
  - Ledge Gap at (11, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7319). Allows bypassing the horizontal ledge on Row 7 by walking north from (11, 9) to (11, 6).
  - Ledge Gap at (15, 11): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 4360). Allows bypassing the tree line by moving between (15, 11) and (15, 12).
  - Ledge Gap at (27, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7365). Allows bypassing the rock wall at column 28 by moving south to Row 8, then east.
  - Ledge Gap at (31, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7256). Allows access to the northern section from (31, 8).
  - Ledge Gap at (49, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7662). Allows crossing between northern and southern corridors at Column 49. (↔️ marked)
- **Eastern Blockage (Columns 28-31)**:
  - Rows 4-7 are occupied by a massive mountain wall of TYPE_2889 starting at Column 28, blocking direct eastern progression on those rows.
  - **Empirical Collision Verification**: Physically tested on Turn 7355. Walking Right from (27, 5) against the wall at (28, 5) resulted in zero movement, confirming the wall is solid and impassable.
  - To continue east towards Mt. Moon, players must walk south through the (27, 7) ledge gap onto Row 8 or Row 9, which are completely clear of mountain walls to the east.

## Inactive Tall Grass Patch:
- The westernmost tall grass patch at (2, 10) (Rows 8-11, Columns 2-5) has disabled or extremely rare wild spawns. Verified on Turn 4982: we took 150 overworld steps (15 loops) with exactly zero wild encounters.

## Defeated Trainers:
- Bug Catcher Colton at (10, 6)
- Youngster Albert at (14, 5)
- Lass Janice at (15, 9)
- Bug Catcher Greg at (19, 5)
- Lass at (23, 4)
- Bug Catcher at (24, 6)
- Youngster Ben at (22, 9)
- Lass at (33, 9)