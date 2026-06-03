# Safari Zone North (Area 2) Systematic Exploration & Routing Plan (Turn 44615)
- **Objective**: Navigate systematically through Safari Zone North (Area 2) to locate the transition to Safari Zone West (Area 3, containing the Secret House and Warden's Gold Teeth).
- **Strategy & Methodology**:
  - We must explore on foot coordinate-by-coordinate to document passable routes and establish absolute proof of passability.
  - To prevent spatial backtracking and time blindless, we will record the starting turn and track all unvisited boundaries/ledges.
- **Initial Verification Plan**:
  1. **Identify Entry Coordinates**: Note the exact entry coordinates (X, Y) when transitioning from Safari Zone East (Map 0_217) into Safari Zone North (Area 2).
  2. **Explore Eastern Ground Level**: Check the ground level immediately surrounding the entry point for exits or paths leading West.
  3. **Plateau Elevation Assessment**: Locate any plateau staircases (wooden stairs, TYPE_4b8d) in Area 2. Test climbing them on foot and map out their connectivity.
  4. **Systematic Boundary Tracking**: Document all fence boundaries (TYPE_2889), ledge boundaries (one-way drops), and water obstacles (water pools) to define the passable corridors.
  5. **Bypass Tall Grass where possible**: Optimize routing to minimize exposure to wild encounter grass (TYPE_fed7) and preserve Safari Zone steps.
  6. **Locate West Transition**: Map out the western border to find the transition to Safari Zone West (Area 3). Ensure on-foot verification of the pathway's coordinates.
- **Turn 44631 Connection Verified**:
  - Exiting Safari Zone East (Map 0_217) to the West at (0, 5) transitions directly to Safari Zone North (Map 0_218) at (39, 31).
  - This is a bidirectional transition. Walking East from (39, 31) on Safari Zone North transitions back to Safari Zone East at (0, 5).
- **Turn 44649 Northern Plateau Boundary Test**:
  - standing at (28, 24) (TYPE_2770, sandy plateau).
  - Hypothesis: Moving Up to (28, 23) (TYPE_3fe2, green grass ground) will be blocked because of the plateau's northern cliff face.
  - Result: The attempt to walk Up from (28, 24) to (28, 23) was completely blocked. The system warning confirmed we visited 0 tiles.
  - Conclusion: The northern boundary of the plateau is a solid cliff face, blocking Northward movement from Row 24 to Row 23.
- **Turn 44686 Lower Ground Row 11 Barrier Verified**:
  - Found a continuous fence of TYPE_2889 on Row 11 extending from Column 16 on the west to Column 31 on the east.
  - Column 32 has a passable green ground tile on Row 11, but Column 32, Row 12 is blocked by the cliff face (TYPE_2889).
  - This completely blocks lower-ground vertical transit between Rows 12-20 and Rows 8-10.
  - Conclusion: To access the northern area of the map (Rows 8-10), we must use the plateau stairs at (34, 15) to climb onto the plateau, navigate north across the plateau, and find an exit to the northern ground level.
- **Turn 44694 Eastern Corridor Northern Plateau Boundary Test**:
  - standing at (37, 12) (TYPE_2770, sandy plateau).
  - Hypothesis: Moving Up to (37, 11) (TYPE_3fe2, green grass ground) will be blocked because of the plateau's northern cliff face.
  - Result: The attempt to walk Up from (37, 12) to (37, 11) was completely blocked (0 tiles moved).
  - Conclusion: The northern boundary of the plateau at Column 37 is a solid cliff face, blocking Northward movement from Row 12 to Row 11.

- **Turn 44701 Central Corridor Northern Plateau Boundary Test**:
  - standing at (34, 12) (TYPE_2770, sandy plateau).
  - Hypothesis: Moving Up to (34, 11) (TYPE_fed7, tall grass on lower ground) will be blocked because of the plateau's northern cliff face.
  - Result: The attempt to walk Up from (34, 12) to (34, 11) was completely blocked (0 tiles moved).
  - Conclusion: The northern boundary of the plateau at Column 34 is a solid cliff face, blocking Northward movement from Row 12 to Row 11.
- **Turn 44724 Southwest Plateau Boundary Test**:
  - standing at (18, 19) (TYPE_3fe2, lower green ground).
  - Hypothesis: Moving Down to (18, 20) (TYPE_2770, sandy plateau) will be blocked because of the plateau's northern cliff face.
  - Result: The attempt to walk Down from (18, 19) to (18, 20) was completely blocked (0 tiles moved).
  - Conclusion: The northern boundary of the southwest plateau at Column 18 is a solid cliff face, blocking Southward movement from Row 19 to Row 20.

- **Post-Warp Re-Entry & Routing Strategy**:
  1. Once steps run out, we will be warped back to the Safari Zone Gatehouse.
  2. Walk South to exit the Gatehouse and step into Fuchsia City.
  3. Re-enter the Gatehouse and pay ¥500 to start a fresh Safari Zone run with 500 steps.
  4. Follow the standard route through Safari Zone East and Safari Zone North to find the entrance to Safari Zone West.
- Turn 44920: Reached (22, 22) on the western plateau.
  - Verification of plateau exit: We are standing on the sandy plateau at (22, 22). Let's see our surroundings.
  - Row 22 shows:
    - (21, 22): TYPE_2770 (plateau ground)
    - (22, 22): TYPE_2770 (player standing here)
    - (23, 22): TYPE_2770 (plateau ground)
    - (24, 22): TYPE_2770 (plateau ground)
    - (25, 22): TYPE_2889 (cliff face/wall)
    - (26, 22): TYPE_3fe2 (lower green ground)
  - Row 21 shows:
    - (18, 21) to (24, 21): TYPE_2770 (passable sandy plateau ground)
    - (25, 21): TYPE_2889
  - Row 20 shows:
    - (18, 20) to (24, 20): TYPE_2770 (passable sandy plateau ground)
    - (25, 20): TYPE_2889
  - Row 19 shows:
    - (18, 19) to (27, 19): TYPE_3fe2 (passable green ground)
    - Wait! Row 19 is lower green ground!
    - This means the plateau ends at Row 20!
    - So Row 20 is the northern edge of this western plateau.
    - Let's check if there is a cliff face between Row 20 (plateau) and Row 19 (lower ground).
    - Yes, there is! But wait! Can we walk West on the plateau?
    - Row 20, Column 18: TYPE_2770
    - Row 21, Column 18: TYPE_2770
    - Row 22, Column 18: TYPE_2770
    - Row 23, Column 18: TYPE_2770 (plateau sandy ground)
    - Row 24, Column 18: TYPE_2770 (plateau sandy ground)
    - Row 25, Column 18: TYPE_2770 (plateau sandy ground)
    - Row 26, Column 18: TYPE_2770 (plateau sandy ground)
    - Wait, Columns 18 is plateau ground!
    - This means the plateau continues to the West!
    - Let's explore West on the plateau to find where it leads.
    - Let's walk Left from (22, 22) to (18, 22) (4 steps Left).
      - (22, 22) -> Left -> (21, 22) -> Left -> (20, 22) -> Left -> (19, 22) -> Left -> (18, 22)
    - Let's trace if they are all TYPE_2770 (sandy plateau):
      - Yes, (21, 22), (20, 22), (19, 22), (18, 22) are all TYPE_2770.
    - Let's walk!