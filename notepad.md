# B1F Boulder Puzzle
- Attempt Start: Turn 28546 (Sunday, Dec 28, 4:26 AM).
- Pit Locations: P1 (11, 2), P2 (4, 7), P3 (5, 12), P4 (12, 13)
- B1F Layout: Brown floor tiles are NOT slippery. Rows 1-2 have ICE tiles.
- Status: B1 at (10, 3). B2 at (5, 6). B3 and B4 unverified.

## Strategy: Boulder 1 (ID 1) -> Pit 1 (11, 2)
1. Move to (10, 6).
2. Push UP to (10, 1).
3. Navigate to (6, 1), slide RIGHT to (9, 1).
4. Push RIGHT to (11, 1).
5. Slide UP from (10, 1) to (10, 0), then walk to (11, 0).
6. Push DOWN into Pit 1 (11, 2).

## Strategy: Boulder 2 (ID 2) -> Pit 2 (4, 7)
1. Navigate to (6, 6) via loop.
2. Push LEFT to (4, 6).
3. Move to (4, 5), push DOWN into Pit 2 (4, 7).

# Game Mechanics & Discoveries
## Tile Mechanics
- FLOOR (Brown): Walkable, non-sliding.
- ICE (Rows 1-2): Sliding mechanic. Boulders do NOT slide on ice.
- PIT: Warp to B2F. Filling a pit creates a stopper on B2F.
- BOULDER: Boulders on floor reset on ladder use. Boulders in pits are permanent.
- STRENGTH: Deactivates after battle or floor change. Verified.

## Encounters
- Golbat (Lv25) at (5, 9).
- Delibird at (7, 9).
- Zubat at (12, 11).
- Swinub (Lv24) at (15, 13).

# Tracking & Verification
- B2F Stoppers: P3 and P4 (Likely filled, but unverified).
- Pits: P1 and P2 unfilled.

# Failed Hypotheses
- "B1F floor tiles do NOT slide" was too broad; Row 1-2 ice tiles DO slide.
- "Boulder 1 is at (11, 5)" - Incorrect, it was pushed to (10, 5).
- "Mixed inputs in menus" - Always use single actions or autopress.
- "navigation_and_puzzle_solver" tool - Hallucinated. Use built-in tools.