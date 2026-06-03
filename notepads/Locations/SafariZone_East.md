# Safari Zone East Verified Records (Map 0_217)
- **Map Connections**:
  - Connected to Safari Zone Center (Map 0_220) at western boundary (Row 22, Col 0). Entering lands at (0, 22). (Verified on Turn 44318)
- **Physical Landmarks & Obstacles**:
  - Rest House building starts at Column 5, Row 23 (TYPE_2889!).
  - Wooden fences/trees run horizontally on Row 20 and Row 25.
  - The corridor between Row 21 and Row 24 is open grass (TYPE_3fe2).
  - **Row 6 Ground-Level Blockage**: Row 6 is completely blocked by solid trees and Rest House roof tiles (TYPE_2889) from Column 0 to Column 10, making ground-level vertical transitions from Row 7 to Row 5 physically impossible on the West. (Verified via systematic Western Passage Passability Test, Turns 44440-44458)
  - **High Plateau Cliff Edge Barrier**: The high plateau cliff edge on Row 12 (facing North to Row 11) is a solid, impassable vertical barrier. Northward steps or jumps from the high plateau at (21, 12) down to (21, 11) are physically blocked. We must use the established stairs to transition elevations. (Verified on Turn 44353)
- **Plateau & Stairs Discovery (Turns 44332-44335)**:
  - Discovered wooden stairs leading UP onto the cliff plateau at (20, 21) (TYPE_4b8d).
  - Bypassed the tall grass by climbing onto the plateau at (20, 20) (TYPE_2770) on Turn 44333.
  - A body of water (TYPE_4e8c) is located north of the plateau on Columns 16-19, Rows 16-17.
  - The plateau continues to the north-east along Columns 21-22 to bypass the water.
  - **Item Retrieval**: Retrieved CARBOS at (20, 13) on Turn 44338. Standing at (21, 13) facing Left, pressed 'A'.
  - **Item Retrieval**: Retrieved MAX POTION at (3, 7) on Turn 44437. Standing at (4, 7) facing Left, pressed 'A'. (Verified in inventory, Turn 44460)
- **Area 1 Master Routing Solution (Turn 44363)**:
  - **The Ground Level Connectivity**: Row 8 is verified as a flat, passable ground corridor that spans horizontally across Column 6 from Column 5 all the way to Column 13, connecting the western and eastern ground areas.
  - **The Intended Path**:
    1. Enter Map 0_217 at (0, 22). Walk East along Row 22 to Column 5, bypass the Rest House via Row 24, and walk East to Column 20.
    2. Walk UP the wooden stairs at (20, 21) (TYPE_4b8d) onto the high plateau.
    3. Walk across the plateau to the West side.
    4. Walk DOWN the western stairs at (11, 20) (TYPE_2770) to land on the ground level of the isolated central corridor.
    5. Walk East on Row 8 from (9, 8) to (12, 8), climb the northern stairs at (12, 7) onto the high plateau at (12, 6).
    6. Walk Up to Row 4 or 5 and attempt to jump West off the plateau's ledge (Column 10) onto the northwest ground corridor (Column 9).
- **Tall Grass (9, 9) Bypass Corridor**: The central vertical corridor from (9, 12) to (9, 8) is fully verified as 100% passable. The tall grass patch at (9, 9) can be completely bypassed with zero grass exposure and 0% wild encounters by walking: Up to (9, 10), Right to (10, 10), Up, Up to (10, 8), and Left to (9, 8). (Verified on Turn 44398)

### Northern Plateau Cliff-Jump Systematic Test Plan (Row 4-6)
- **Hypothesis**: The player can jump West (Left) off the high plateau (Column 11, Row 4 or Row 5) over the cliff edge (Column 10, TYPE_2889) to land on the northwest ground level (Column 9, Row 4 or Row 5).
- **Methodology**:
  1. Walk from current position (1, 7) to (12, 8) (ground).
  2. Walk Up to (12, 7) (stairs) and onto the plateau at (12, 6).
  3. Walk Up to (12, 4) (plateau) and Left to (11, 4) (plateau).
  4. Press Left to attempt the jump over (10, 4) onto (9, 4) (ground).
  5. If Row 4 fails, try Row 5: Walk to (11, 5) and press Left.