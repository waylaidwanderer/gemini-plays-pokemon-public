# Ice Path Strategy
- **Current Action:** Executing Ice Slide Path to West Section.
- **Path Plan:**
  1. From (20, 23), Slide Left -> Stop at (18, 23). [DONE]
  2. From (18, 23), Slide Up -> Stop at (18, 20). [DONE]
  3. From (18, 20), Slide Left -> Stop at (14, 20). [DONE]
  4. From (14, 20), Slide Up -> Stop at (14, 16). [NEXT]
  5. Walk Left -> Arrive at (13, 16) [Floor Area].
- **Items:** Item Balls at (32, 23), (35, 9), (31, 7) [East Side - Currently Unreachable].

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles at (7,18), (8,18), (9,18), (10,18), (14,22), (20,24) are **IMPASSABLE WALLS**.
- **Map Structure:** Map split into West (Goal?), Center (Start/Hub), and East (Dead ends/Item Balls).

# Map Notes
- **East Corridor:** Loop/Dead ends.
- **Central Maze:** Solved via path above.
- **West Section:** Exploring next.