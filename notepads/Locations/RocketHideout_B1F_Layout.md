# Rocket Hideout B1F Layout Records
- **Southeast Pocket (Column 28)**:
  - (28, 11) to (28, 15) is an open vertical corridor.
  - On rows 12 to 20, column 28 is separated from column 27 by a solid vertical partition wall.
  - Column 28 is blocked on row 16 by a solid counter at (28, 16) (TYPE_2889).
  - Therefore, (28, 15) is a dead end.
  - **Overworld Steps**: (24, 16) and (25, 16) are step tiles (TYPE_a83b).
    - **Collision Test (Turn 33386)**: Standing at (24, 15) facing Down, we tried to walk Down onto (24, 16) and collided.
    - **Collision Test (Turn 33389)**: Standing at (25, 15) facing Down, we tried to walk Down onto (25, 16) and collided.
    - **Conclusion**: These step tiles are completely impassable from north-to-south. They are either one-way steps (only passable south-to-north) or entirely decorative/solid boundaries. Therefore, the northern and southern sections of B1F are completely separated in this eastern region, and the southern section (row 17+) cannot be reached from the upper-right section.
  - **Rocket Grunt 3**: Standing at (28, 18) looking UP. Can only be reached by walking through the main southeast room (columns 24-27) and stepping onto row 17.

- **Western Section & Central Row 16 Blockage (Turn 33405)**:
  - **Empirical Test**: Backtracked to the western section of B1F (columns 10-15) and walked down to row 14.
  - **Visual Verification**: Visually and physically verified that row 16 is completely solid and blocked by TYPE_2889 walls across all columns from column 9 to column 15.
  - **Overall Conclusion**: Since row 16 is completely blocked from column 9 to column 23, and the stairs at (24, 16) and (25, 16) are impassable from the north, the northern section of B1F (upper floor) is isolated from the southern section of B1F (lower floor, row 17+) across all tested columns (columns 9 to 28). Columns 0 to 8 are completely blocked and separated on B1F by a solid vertical partition wall at column 8 (Verified on Turn 33590).
  - Therefore, Rocket Grunt 3 at (28, 18) and the B1F elevator door are completely unreachable from the upper area of B1F. We MUST obtain the LIFT KEY from B4F first, and then take the elevator to B1F to access the southern area.

## Multi-Floor Connections & Staircase Redirection (Turn 33613 Verification)
- **Staircase Warp at (23, 2)**: This staircase, located in the northeast section of B1F, does NOT connect to B2F (27, 8) as typically expected in vanilla. Instead, it connects directly to B4F (25, 6) (Verified Turn 33613).
- **Implications**: The direct staircase to B4F provides immediate access to the lowest floor, bypassing B2F and B3F entirely for quick traversal to Giovanni's chamber and the Lift Key.