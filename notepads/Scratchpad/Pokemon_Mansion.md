Mansion Routing:
- State A = Dark Grey OPEN, Yellow CLOSED.
- State B = Yellow OPEN, Dark Grey CLOSED.
Current State: B.

- Confirmed (Turn 46828): y=17 in the West Wing is a solid dead end.
- To reach the West Wing stairs at (5, 10) from the Central Hub, there MUST be a gap in the x=9 wall between y=9 and y=16.
- Goal: Systematically press 'Left' against the x=9 wall at every y-coordinate from y=15 up to y=9 to find the gap.
- Tested x=9 wall:
  - (9, 15) is solid (Turn 46838).
  - (9, 14) is solid (Turn 46839).
  - (9, 13) is solid (Turn 46840/46841).
  - (9, 12) is solid (Turn 46841/46843).
Correction: y=17 is NOT completely solid. Overwatch confirmed this is logically impossible since I reached the stairs before. There must be an open path North at x=4 or x=5. I will test this next. The x=9 wall is confirmed permanently solid.