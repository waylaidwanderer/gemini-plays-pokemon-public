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
- Result: Pushed UP at (3, 13) on Turn 28739, 28740, 28741. Received "GNEISS can move boulders" text on Turn 28739. Boulder did not move. Hypothesis: A button interaction or another push is required.
- Attempting A button interaction at (3, 13) facing UP.

# Failed Hypotheses
- "B1F floor tiles do NOT slide" - Too broad; Row 1-2 ice tiles DO slide.
- "B3 is unreachable from entry (4, 17)" - Incorrect, reached via (3, 17) FLOOR.