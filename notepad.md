# Ice Path Strategy
- **Current State:** At Ice Path B1F (5, 3).
- **Goal:** Map the B1F Boulder Room and solve the puzzle.
- **Observations:**
  - Room contains Pits and Boulders.
  - Known Pits: (4, 7), (5, 12).
  - Known Boulders: (7, 8).
  - Need to find 3 more boulders (usually 4 total).
- **Plan:**
  1. Explore South to Row 8-12 to locate remaining boulders/pits.
  2. Use `puzzle_solver` agent (to be defined) to plan the pushes.
  3. Push boulders into pits.
  4. Drop down/Ladder up? (Usually drop down to fill holes, then fall).

# Map Structure
- **B1F Room:** Large Puzzle Room.
- **West Corridor (x=0-1):** Wraps around North.
- **East Room (x=2+):** Contains the puzzle.
- **Observation:** Found a Boulder at (7, 8).
- **Hypothesis:** This is a Strength puzzle. Pushing boulders into the pits (4, 7) and (5, 12) might be the goal, or they serve as bridges.
- **Action:** Continue exploring the room to locate all boulders and pits.