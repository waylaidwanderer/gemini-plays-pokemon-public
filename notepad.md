# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- B1: (11, 7) | B2: (5, 7)
- Pit 1 (11, 2): UNFILLED
- Pit 2 (4, 7): UNFILLED
- Pit 3 (5, 12): FILLED (Stopper at B2F 5, 12)
- Pit 4 (12, 13): FILLED (Stopper at B2F 12, 13)

# Strategies
## Fill Pit 2 (4, 7) with Boulder 2 (5, 8)
1. Navigate to (5, 9).
2. Push B2 UP to (5, 7). (Player at 5, 8).
3. Push B2 UP to (5, 6). (Player at 5, 7).
4. Navigate to (6, 6).
5. Push B2 LEFT to (4, 6). (Player at 5, 6).
6. Navigate to (4, 5).
7. Push B2 DOWN into Pit 2 (4, 7).

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

# Lessons Learned & Tile Mechanics
- **Immovable Boulders:** Boulders pushed into pits on B1F become permanent, immovable "stoppers" on B2F. They cannot be pushed once imbedded.
- **Sliding Floor:** Tiles labeled "FLOOR" in Rows 1-2 on B1F function as ICE and cause sliding.
- **Puzzle Logic:** B2F requires these stoppers to create a path to the ladder at (9, 11). Without them, the player slides past critical junctions.

# Failed Hypotheses
- "B1F floor tiles do NOT slide" (Failed Turn 28160) - Row 1-2 tiles observed to slide.
- "Boulder 3 on B2F is moveable" (Failed Turn 28742) - "Immovably imbedded in ice."
- "B3 is unreachable from entry (4, 17)" (Failed Turn 28650) - Reached via (3, 17) FLOOR.