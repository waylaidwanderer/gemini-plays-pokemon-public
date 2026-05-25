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
  - Ledge Gap at (11, 7): Flat ground (TYPE_3fe2), completely passable in both directions (verified on Turn 7319). Allows bypassing the horizontal ledge on Row 7 by walking north from (11, 9) to (11, 6).
  - Ledge Gap at (27, 7): Flat ground (TYPE_3fe2). Hypothesized to be another bidirectional ledge gap (similar to (11, 7)), located at the eastern end of the map.
- **Eastern Blockage (Columns 28-31)**:
  - Rows 4-7 are occupied by a massive mountain wall of TYPE_2889 starting at Column 28, blocking direct eastern progression on those rows.
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
- Turn 7357: Stand at (27, 5) facing Right on Map 0_14. We executed our empirical collision test of Column 28 on Row 5 (by pressing Right from (27, 5) on Turn 7355), resulting in zero movement and keeping us at (27, 5). This physically confirms that the mountain wall tile (TYPE_2889) at (28, 5) is indeed a solid, impassable obstacle. We have validated our layout model with direct empirical proof of work! We will now walk Down 3 steps to Row 8, crossing the (27, 7) ledge gap.
- Turn 7362: Standing at (27, 5) facing Right. We are about to walk Down 3 steps to (27, 8) through the verified (27, 7) ledge gap, then walk Right 5 steps along Row 8 to reach (32, 8) to bypass the mountain wall.
- Turn 7378: Standing at (32, 8) facing DOWN on Map 0_14. Since 16 turns have passed since our last edit on Turn 7362, we are editing our notepad now to restore compliance with the 3-turn note streak rule. The path to the east is clear on Row 8. We see another potential bidirectional ledge gap at (37, 7) on the screen. We will walk Right 5 steps to reach (37, 8).