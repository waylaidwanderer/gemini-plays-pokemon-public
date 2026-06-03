# Socratic Question Answers (Run 14 Update — Turn 50137)

### Socratic Question 1:
- **Current Position**: Standing at (21, 8) on Map 0_217 with 397 steps remaining.
- **Planned Path**: 
  - Walk Left to Column 20, then Up along Column 20 to Row 2: `(21, 8) -> (20, 8) -> (20, 7) -> (20, 6) [grass] -> (20, 5) -> (20, 4) [grass] -> (20, 3) [grass] -> (20, 2)` (7 overworld steps total, only 3 tall grass tiles).
  - Walk West along Row 2 to transition: `(20, 2) -> (0, 2)` (20 steps Left) and 1 more Left to transition to Map 0_218 (Safari Zone North).
  - **Total Steps**: 28 overworld steps.

### Socratic Question 2:
- **Why it failed**: The custom `safari_pathfinder` tool's source code has no collision database defined for Map 0_217 (Safari Zone East). It only has definitions for Saffron City (0_10) and Rocket Hideout B4F (0_202). Thus, the BFS algorithm treated Map 0_217 as a completely empty 100x100 grid and calculated a straight line Up on Column 0, crashing directly into the solid tree wall at (0, 20).
- **Required definitions to make it robust**: 
  - Solid tree walls/fences on Row 20 (Columns 0-29) and Row 25 (Columns 0-29).
  - Rest House building blocking Row 22 and Row 23 (Columns 5-7).
  - High plateau boundaries and cliff edges (Row 12, Column 10, Column 19).
  - Body of water on Columns 16-19, Rows 16-17.

### Socratic Question 3:
- **Safari Zone North crossing path**:
  - Spawn in isolated eastern basin at (39, 31).
  - Walk to eastern plateau stairs at (34, 15) and climb onto plateau.
  - Traverse plateau to descent stairs at (28, 27) and descend to southern ground level.
  - Walk to Western Plateau stairs at (22, 23) and climb onto plateau.
  - Traverse Western Plateau to descent stairs at (16, 27) and descend to western ground level.
  - Walk to Row 33 Column 9, walk Down through gap at (9, 34) to (9, 35) and transition into Safari Zone West at (26, 0).

### Socratic Question 4:
- **Discipline improvement**: We established the habit of tracking steps taken and steps remaining Turn-by-Turn, meticulously updating both the scratchpad and objectives during every movement chunk. We also chunk our button presses into smaller segments (e.g. 5-8 steps) and handle wild encounters immediately before calculating the next step. This prevents step tracking drift during transitions and battle interruptions. We will maintain this rigorous tracking discipline as we transition between maps.