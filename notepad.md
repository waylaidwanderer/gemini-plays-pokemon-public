# Ice Path Strategy (Reset & Explore)

# Ice Path Strategy (B1F)

## Current Status
- **Position:** Player at (8, 8).
- **Goal:** Solve B2.
- **Puzzle State:**
  - **B1:** Missing.
  - **B2:** Verified at (7, 8).
  - **B3:** Not found in Top Left.

# Ice Path Strategy (B2F Recovery)

## Current Status
- **Position:** Player at (19, 6) (B2F).
- **Goal:** Locate B2 and Retrieve Item.
- **Puzzle State:**
  - **B2:** Pushed into Pit (4, 7). Likely at (4, 7) on B2F.
  - **Plan:** Check Column 4 from below.

## Immediate Plan
1.  **Navigate to Column 4:**
    - Slide Down to (19, 12).
    - Slide Left to (0, 12) (or until blocked).
    - Go to (4, 17) (Bottom of Col 4).
2.  **Check B2:**
    - Slide Up Column 4.
    - **Hypothesis:** Hit B2 at (4, 7), stop at (4, 8).
3.  **Retrieve Item:**
    - From (4, 8), Slide Right to (8, 8) (Floor).
    - Get Item at (8, 9).
    - Exit via Ladder (9, 11).
4.  **Contingency:**
    - If B2 not found, Escape via (19, 1) -> Ladder (17, 1).
    - Reset Puzzle on B1F.
    - Try Pit (5, 12) -> (3, 12) strategy.
## Lessons Learned
- **Map Resets:** Leaving a map (e.g. falling to B2F) resets all puzzle elements (Boulders) and deactivates Strength.
- **Pushing:** Requires deliberate input. 'Navigate' might fail if it treats the boulder as a static wall. Use 'slow_press' for pushing.

## Strategy: Retrieve Item (B2F)
1. **Preserve Boulder 2:** Do NOT push the boulder at (3, 12). It is needed as a backstop.
2. **Exit B2F:** Navigate to Ladder (17, 1) via (16, 16) -> (16, 1).
3. **Re-enter B2F:** On B1F, fall through the hole at (12, 13).
4. **Collect Item:**
   - Land at B2F (12, 12).
   - Slide Left -> Hit Boulder 2 at (3, 12) -> Stop at (4, 12).
   - Slide Up -> Hit Boulder 1 at (4, 7) -> Stop at (4, 8).
   - Slide Right -> Stop at (8, 8) (Item Island).
5. **Escape:** Use Ladder (9, 11).

## Current Action
- Sliding Right on Row 16 to exit area.