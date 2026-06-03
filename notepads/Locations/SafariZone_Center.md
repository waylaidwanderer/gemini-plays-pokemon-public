# Safari Zone Center Verified Records (Map 0_220)
- **Map Connections**:
  - Connected to Safari Zone Gatehouse (Map 0_156) at southern exit (Row 26, Col 15/14). Lands at (15, 25). (Verified)
  - Connected to Safari Zone East (Area 1) at eastern boundary (Row 10-13, Col 29). (Verified on Turn 44312)
  - *Unverified Hypothesis*: Connected to Safari Zone West (Area 3) at western boundary (Row 10-13, Col 0).
  - *Unverified Hypothesis*: Connected to Safari Zone North (Area 2) at northern boundary (Row 0, Col 10-15).
- **Physical Landmarks & Obstacles**:
  - Entrance has a wooden fence layout on Row 25.
  - Solid building at Columns 13-14, Row 22 (Rest House 1).
  - Gate at Column 15, Row 24 is solid (TYPE_2889).
  - Passable gate opening is at Column 14, Row 24 (TYPE_3fe2).

# Safari Zone Route Optimization & Tracking (Turn 44298)
- **Start Turn**: 44298
- **Goal**: Reach Safari Zone East (Area 1) with minimal step usage and zero unnecessary battles.
- **Visual Grid Map Analysis (Turn 44298)**:
  - Columns 20 & 21 are open, passable grass (TYPE_3fe2) up to Row 14.
  - Column 22 contains tall grass (TYPE_fed7) from Row 14, but Row 15 is open (TYPE_3fe2).
  - Row 14 is open (TYPE_3fe2) across Columns 20-21, but features tall grass (TYPE_fed7) on Columns 22-25.
  - Columns 16 and 19 have solid building structures (TYPE_2889) at Rows 14 and 15 (looks like columns, possibly a gate or rest house entrance).
    - Specifically, (16, 14), (16, 15) are TYPE_2889.
    - (19, 14), (19, 15) are TYPE_2889.
    - So Columns 16 and 19 are blocked at Rows 14-15.
    - Column 20 is completely open: (20, 18) -> (20, 17) -> (20, 16) -> (20, 15) -> (20, 14).
    - Column 21 is also completely open: (21, 18) -> (21, 17) -> (21, 16) -> (21, 15) -> (21, 14).
  - Above Row 14, a pond (water, TYPE_4e8c) stretches across Columns 18-21 on Rows 10-13.
  - To bypass the pond on foot, walk East on Row 14 to Column 22 (tall grass), then go North to Row 10 (open grass). Row 10 is completely open grass leading directly to the eastern exit at Row 10/11, Column 29.