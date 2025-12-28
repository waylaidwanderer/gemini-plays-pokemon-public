# Ice Path B1F Puzzle Status
- B1: (11, 7)
- B2: (7, 8)
- Pit 1 (11, 2): UNFILLED
- Pit 2 (4, 7): UNFILLED
- Pit 3 (5, 12): FILLED
- Pit 4 (12, 13): FILLED

# Strategies
## Fill Pit 2 (4, 7) with Boulder 2 (7, 8)
1. Navigate to (8, 8).
2. Push B2 LEFT to (6, 8). (Player at 7, 8).
3. Push B2 LEFT to (5, 8). (Player at 6, 8).
4. Navigate to (5, 9).
5. Push B2 UP to (5, 7). (Player at 5, 8).
6. Push B2 UP to (5, 6). (Player at 5, 7).
7. Navigate to (6, 6).
8. Push B2 LEFT to (4, 6). (Player at 5, 6).
9. Navigate to (4, 5).
10. Push B2 DOWN into Pit 2 (4, 7).

## Fill Pit 1 (11, 2) with Boulder 1 (11, 7)
1. Navigate to (11, 8).
2. Push B1 UP to (11, 5).
3. Navigate to (12, 5).
4. Push B1 LEFT to (10, 5).
5. Navigate to (10, 6).
6. Push B1 UP to (10, 1).
7. Navigate to (9, 1).
8. Push B1 RIGHT to (11, 1).
9. Navigate to (11, 0).
10. Push B1 DOWN into Pit 1 (11, 2).

# Game Mechanics
- FLOOR (Brown): Walkable. Verified.
- ICE: Sliding mechanic. Verified.
- PIT: Warp to B2F. Filling a pit creates a permanent stopper on B2F. Verified.
- BOULDER: Resets on ladder use. Permanent if in pit. Verified.
- STRENGTH: Deactivates after every battle or floor change. Verified.

# Hypothesis Testing
- Topic: Boulder Sliding on Ice
- Hypothesis: Boulders pushed onto ICE slide until hitting an obstacle.
- Test: Push Boulder 3 (3, 12) UP from (3, 13) onto (3, 11) ICE on B2F.
- Result: Interacted with A. Screen Text: "It's immovably imbedded in ice." (Turn 28742).
- Conclusion: Boulders in pits cannot be moved. They serve as permanent stoppers for the B2F ice puzzle.

# Failed Hypotheses
- "B1F floor tiles do NOT slide" - Too broad; Row 1-2 tiles (labeled FLOOR) observed to slide.
- "B3 is unreachable from entry (4, 17)" - Incorrect, reached via (3, 17) FLOOR.