# Scratchpad: Saffron Southeastern Exploration

## Active Hypothesis (Turn 37345)
- **Goal**: Find a path leading south or east past Saffron's eastern/southeastern boundary buildings (columns 31-39, rows 32-35) to see if we can find a functional entrance/bypass to Route 8 proper.
- **Current Observation**:
  - Saffron East Gatehouse yellow/trellis building spans columns 36-39, rows 32-35.
  - House 2 spans columns 32-35, rows 33-35.
  - House 1 spans columns 27-31, rows 33-35.
  - This forms a continuous wall of buildings from column 27 to 39 on rows 33-35 (and row 32 for the gatehouse).
  - Row 31 and 32 are completely open and passable from column 27 to 35.
- **Next Exploration Steps**:
  1. Walk Left to (27, 31) (Turn 37345).
  2. Inspect column 26 and further west to see where this wall of buildings ends or if there is a street heading south.
  3. If we find a street heading south, walk south to row 36-39 and then walk east along the bottom edge to inspect the south side of the gatehouse building!

- **Turn 37359 Saffron South Lawn Observation**:
  - Confirmed! Saffron South Lawn (rows 35-37) has the following layout:
    - Row 35: Grass is open on column 20 and 21 (TYPE_3fe2).
    - Row 36: Bounded by grey helmet pillars at column 19, column 21, and columns 24-26.
    - Row 36 & 37 are open grass at column 20, column 22, and column 23.
    - Row 38: Bounded by grey pillars on column 17 and columns 24-26. Yellow gatehouse building trellis roof/fence spans columns 18 to 23.
  - Let's walk to (20, 37) to stand right in front of the gatehouse building at columns 18-23 and see if there is an entrance!

- **Turn 37366 Saffron South Gatehouse Test Results & Final Proof of Work**:
  - **Methodology**: Walked south from Saffron City (Map 0_10) at (20, 36) on Turn 37360.
  - **Results**: Warped directly onto Route 6 (Map 0_17) at (10, 0) on Turn 37361. Found ourselves in a trapped 1x2 alcove:
    - Bounded on the south by the yellow gatehouse building roof at (10, 2) (spans columns 8-13, row 2).
    - Bounded on the sides by grey helmet statues at (9, 0), (9, 1) and (11, 0), (11, 1).
    - Walked Up from Route 6 (10, 0) on Turn 37364 to warp back to Saffron City at (20, 35) on Turn 37365.
  - **Comprehensive Collision & Alignment Mapping**:
    - Direct connection alignment: `Route 6 Column = Saffron Column - 10`, `Route 6 Row = Saffron Row - 36`.
    - Every Saffron south-boundary column (18-23) through the yellow trellis wall is blocked or trapped on Route 6:
      - Saffron Col 18 -> Route 6 Col 8 (Blocked by building)
      - Saffron Col 19 -> Route 6 Col 9 (Blocked by grey pillars)
      - Saffron Col 20 -> Route 6 Col 10 (Warped to trapped 1x2 alcove)
      - Saffron Col 21 -> Route 6 Col 11 (Blocked by grey pillars)
      - Saffron Col 22 -> Route 6 Col 12 (Warped to trapped 1x2 alcove)
      - Saffron Col 23 -> Route 6 Col 13 (Warped to trapped 1x2 alcove)
    - All other Saffron columns are blocked by grey pillars at Saffron Row 38 (columns 16, 17 and columns 24, 25, 26).
  - **Conclusion**: BOTH Saffron East Gatehouse (Route 8) and Saffron South Gatehouse (Route 6) are completely impassable. Direct map connections bypass the gatehouse indoor maps but dump the player into trapped, physical dead-end alcoves because the actual gatehouse buildings block the exit on the target maps.
  - **Pivot Strategy**: We must use the Saffron West Gatehouse (Route 7 Gatehouse) -> Route 7 -> Route 7/8 Underground Path -> Route 8 proper -> Lavender Town. This is the only functional and completely open pathway to reach Route 8 proper.