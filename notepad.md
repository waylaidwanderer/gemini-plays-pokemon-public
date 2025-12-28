# B1F Boulder Puzzle Status
- B1: (10, 1) in B1F
- B2: (5, 6) in B1F
- B3: (3, 12) in B2F
- B4: (12, 13) in B2F
- Pit 3 (5, 12) & Pit 4 (12, 13): FILLED (Confirmed by B3/B4 on B2F)
- Pit 1 (11, 2) & Pit 2 (4, 7): UNFILLED

# Game Mechanics
- FLOOR (Brown): Walkable, non-sliding. Verified.
- ICE: Sliding mechanic. Verified.
- PIT: Warp to B2F. Filling a pit creates a permanent stopper on B2F. Verified.
- BOULDER: Resets on ladder use. Permanent if in pit. Verified.
- STRENGTH: Deactivates after every battle or floor change. Verified.

# Hypothesis Testing
- Topic: Boulder Sliding on Ice
- Hypothesis: Boulders pushed onto ICE slide until hitting an obstacle.
- Test: Push Boulder 3 (3, 12) UP from (3, 13) onto (3, 11) ICE.
- Result: Interacted with A. Screen Text: "It's immovably imbedded in ice." (Turn 28742).
- Conclusion: Boulders in pits cannot be moved. They serve as permanent stoppers for the B2F ice puzzle. I must fill the remaining two pits on B1F.

# Failed Hypotheses
- "B1F floor tiles do NOT slide" - Too broad; Row 1-2 ice tiles DO slide.
- "B3 is unreachable from entry (4, 17)" - Incorrect, reached via (3, 17) FLOOR.
## Strategy for Boulder 1 (ID 1) -> Pit 1 (11, 2)
1. Navigate to (9, 1).
2. Push Boulder 1 RIGHT to (11, 1).
3. Navigate to (11, 0).
4. Push Boulder 1 DOWN into Pit 1 at (11, 2).

## Strategy for Boulder 2 (ID 2) -> Pit 2 (4, 7)
1. Navigate to (6, 6).
2. Push Boulder 2 LEFT to (4, 6).
3. Navigate to (4, 5).
4. Push Boulder 2 DOWN into Pit 2 at (4, 7).