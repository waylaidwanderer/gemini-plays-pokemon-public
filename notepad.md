# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- B1: (11, 5) | B2: (5, 6)

# Strategies
## Fill Pit 2 (4, 7) with Boulder 2 (5, 6)
1. Complete "Fill Pit 1" strategy.
2. Navigate to (6, 6) from the top section.
3. Push B2 LEFT to (4, 6). (Player at 5, 6).
4. Navigate to (4, 5).
5. Push B2 DOWN into Pit 2 (4, 7).

## Fill Pit 1 (11, 2) with Boulder 1 (11, 5)
1. Navigate to (12, 5).
2. Push B1 LEFT to (10, 5).
3. Navigate to (10, 3) or (10, 6).
4. Push B1 UP to (10, 1) (will stop at wall at 10, 0).
5. Navigate to (7, 2).
6. Move UP to (7, 1) (slide to wall at 7, 0).
7. Move RIGHT from (7, 1) to (9, 1) (slide into boulder at 10, 1).
8. Push B1 RIGHT to (11, 1). (Player at 10, 1).
9. Move UP to (10, 0).
10. Move RIGHT to (11, 0).
11. Push B1 DOWN into Pit 1 (11, 2).

# Lessons Learned & Tile Mechanics
- **Immovable Boulders:** Boulders pushed into pits on B1F become permanent, immovable "stoppers" on B2F. They cannot be pushed once imbedded.
- **Sliding Floor:** Tiles labeled "FLOOR" in Rows 1-2 on B1F function as ICE and cause sliding. In all other observed rows, "FLOOR" tiles are standard and non-sliding.
- **Puzzle Logic:** B2F requires these stoppers to create a path to the ladder at (9, 11). Without them, the player slides past critical junctions.

# Game Mechanics
- FLOOR (Brown): Walkable. Standard floor behavior in most areas.
- SLIDING FLOOR: Specific tiles in B1F Rows 1-2 labeled "FLOOR" function as ICE and cause sliding. Verified.
- ICE: Sliding mechanic. Verified.
- PIT: Warp to B2F. Filling a pit creates a permanent stopper on B2F. Verified.
- BOULDER: Resets on ladder use. Permanent if in pit. Verified.
- STRENGTH: Deactivates after every battle or floor change. Verified.

# Failed Hypotheses
- "B1F floor tiles do NOT slide" (Failed Turn 28160) - Row 1-2 tiles observed to slide.
- "Boulder 3 on B2F is moveable" (Failed Turn 28742) - "Immovably imbedded in ice."
- "B3 is unreachable from entry (4, 17)" (Failed Turn 28650) - Reached via (3, 17) FLOOR.
- **Navigation Safety:** Warps (Ladders/Stairs) trigger immediately upon stepping. Avoid including them in path plans unless the intention is to change floors.