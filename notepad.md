# Ice Path B1F Puzzle Status
- Start Turn: 28759 | Start Time: Sunday, Dec 28, 5:32 AM
- Boulder 1: (10, 1) | Target Pit 1: (11, 2)
- Boulder 2: (5, 6) | Target Pit 2: (4, 7)

# Map Sections (B1F)
- Section 1 (Left): (0, 1) to (7, 16). Contains Ladder to 1F (3, 15) and Pit 2 (4, 7).
- Section 2 (Middle): (9, 1) to (13, 15). Contains Pit 1 (11, 2) and Boulder 1 (10, 1).
- Section 3 (Right): (14, 1) to (19, 16). Contains Ladder to B2F (17, 3) and Pit 4 (12, 13).
- Connectivity: 
    - Row 1 (ICE): Connects Sections 1, 2, and 3. Boulder 1 at (10, 1) acts as a stopper for sliding from Section 3.
    - Row 9: (7, 9) to (9, 9) is a walkable 1-tile gap in the wall connecting Sections 1 and 2.
    - Row 16: Connects Section 3 (Bottom) to Section 2 (Bottom).
- Pathfinding: To reach Section 1 from Section 2, walk down to Row 9 and cross at (8, 9). To reach the left side of Boulder 1, slide right from Section 1 Row 1.

# Strategies
## Fill Pit 1 (11, 2) with Boulder 1 (10, 1)
1. Position: Player at (11, 1) facing Boulder 1 at (10, 1).
2. Action: Activate Strength.
3. Navigate to Section 1 (Left) via Row 9 gap at (8, 9).
4. Move to (7, 1) in Section 1.
5. Move RIGHT from (7, 1). Slide on ice until hitting Boulder 1 at (10, 1). Stop at (9, 1).
6. Push Boulder 1 RIGHT to (11, 1). (Player at 10, 1).
7. Navigate around the pit to (11, 0). (e.g., via Row 0).
8. Push Boulder 1 DOWN into Pit 1 (11, 2).

## Fill Pit 2 (4, 7) with Boulder 2 (5, 6)
1. Complete "Fill Pit 1" strategy.
2. Navigate to (5, 5) in Section 1.
3. Push B2 LEFT to (4, 6). (Player at 5, 6).
4. Navigate to (4, 5).
5. Push B2 DOWN into Pit 2 (4, 7).

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