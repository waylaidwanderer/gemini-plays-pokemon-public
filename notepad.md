# B1F Boulder Puzzle
- Status: B1 at (10, 1), B2 at (5, 6).
- Pit 3 (5, 12) and Pit 4 (12, 13) FILLED.
- Pits 1 (11, 2) and 2 (4, 7) UNFILLED.

## Strategy: Boulder 1 (ID 1) -> Pit 1 (11, 2)
1. Get to (9, 1) on B1F.
2. Push RIGHT to (11, 1).
3. Move to (11, 0), push DOWN into Pit 1.

## Strategy: Boulder 2 (ID 2) -> Pit 2 (4, 7)
1. Get to (6, 6) on B1F.
2. Push LEFT to (4, 6).
3. Move to (4, 5), push DOWN into Pit 2.

# Game Mechanics
## Tile Mechanics
- FLOOR (Brown): Walkable, non-sliding. Verified.
- ICE: Sliding mechanic. Verified.
- PIT: Warp to B2F. Filling a pit creates a stopper on B2F. Verified.
- BOULDER: Boulders on floor reset on ladder use. Boulders in pits are permanent. Verified.
- STRENGTH: Deactivates after EVERY battle or floor change. Verified.

## B2F Sliding Observations
- Land at (12, 12) from Pit 4 -> Slide LEFT to (4, 12).
- At (4, 12) move DOWN -> Slide to (4, 17).
- (4, 12) is NOT a warp. (Verified: No warp triggered).

## Experiment: Boulder Sliding
- Hypothesis: Boulders pushed onto ICE slide until hitting an obstacle.
- Test: Push Boulder 3 (3, 12) UP from (3, 13) onto (3, 11) ICE.
- Observation: [PUSHING NOW]

# Failed Hypotheses
- "B1F floor tiles do NOT slide" was too broad; Row 1-2 ice tiles DO slide.
- "Boulder 1 is at (11, 5)" - Incorrect, it was pushed to (10, 5).
- "B3 at (3, 12) is unreachable from B2F entry point (4, 17)" - Incorrect, can be reached via (3, 17) FLOOR.