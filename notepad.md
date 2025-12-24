# Ice Path Strategy
- **Primary Goal:** Reach Blackthorn City.
- **Status:** Backtracking to Puzzle Start (13, 16).
- **Location:** Escaping from (20, 23).
- **New Hypothesis (Center-North Path):**
  - **Action:** Restart Puzzle -> (13, 17) Right to (15, 17) -> **Slide UP**.
  - **Rationale:** This vector (Row 15/16 Northbound) is the only untested path from the start. All South/East paths led to dead ends or loops.
  - **Hope:** Access the North-West area (Rows 0-14, x<13) or B1F.
- **Plan:**
  1. Escape: (20, 23) -> Left to (18, 23) -> Up to (18, 20) -> Left to (14, 20) -> Up to (14, 16) -> Left to (13, 16).
  2. Heal Gyarados if not full.
  3. Execute Slide Up from (15, 17).

# Mechanics & Lessons
- **Ice Physics:** Sliding continues until collision.
- **Ledges:** `FLOOR_UP_WALL` tiles at (7,18), (8,18), (9,18), (10,18), (14,22), (20,24) are **IMPASSABLE WALLS**. Do not attempt to jump them.
- **Map Structure:** Map appears split into West (Goal?), Center (Start/Hub), and East (Dead ends/Item Balls).

# Reflection (Turn 16417)
- **Execution:** Delayed healing slightly due to movement errors, now correcting.
- **Hygiene:** Notepad consolidated. Markers updated for walls.
- **Goals:** Clear.
- **Errors:** Hallucinated ledge jumps. Root cause: Visual similarity to ledges in other tilesets. Verification: Bump test confirmed they are walls. Lesson: Verify collision before assuming traversal.