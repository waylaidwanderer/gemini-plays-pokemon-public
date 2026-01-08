# Tile Mechanics (Global)
- FLOOR: Standard walkable tile.
- WALL: Impassable collision (pillars, statues, rocks, NPCs).
- LADDER: Two-way warp between floors. (1, 7) and (7, 9).
- PIT: A hole that leads to 1F. Boulders fall through to fill gaps on 1F. Empty pits are impassable/warp for player on 2F.
- BOULDER: Pushable object. Requires STRENGTH. Pushing moves it one tile. Player STAYS in original tile. (Verified Turn 34566)

# Blackthorn Gym Puzzle Analysis
- Start Turn: 34501
- Goal: Fill three pits on 2F to bridge gaps on 1F.
- Boulders: B6 (3, 3), B7 (6, 1), B8 (8, 16) [Current Positions].
- Pits: P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Critical Mechanic: Changing floors (using ladders) RESETS all boulder positions on 2F. (Verified Turn 34592).
- Push Mechanic: Player stays in place after push (Verified Turn 34644).
- Passability: Cody (4, 1) is a wall. Fran (4, 11) likely also a wall. (Verified Turn 34647).

# Strategy & Progress
- Lead Pokémon: XENON (Haunter, Lv36).
- Plan: Use Row 13 gap (4, 13) and (5, 13) to move between Middle and Right corridors.
- Note: B6 (3, 3) cannot be pushed left from (4, 3) due to WALL. Investigate alternative paths or boulder-pit assignments.
- Note: Cody (4, 1) and Fran (4, 11) are likely walls. Verification needed.

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).

## Tested Mechanics
- Push Mechanic: Player stays in place after push (Verified Turn 34566).
- Floor Reset: Transitions between 1F and 2F reset boulders (Verified Turn 34592).

# Puzzle Obstacles & Hypotheses
- Hypothesis: Strip 2 (Section A, Row 1-7) is isolated from Row 9-17 by walls at Row 8 (2,8), (3,8), (4,8).
- Path to Section A: Must go via Row 13-17 crossing -> Strip 2 (bottom) -> Row 9 crossing -> Strip 1 -> Row 1 crossing -> Strip 2 (top).
- Problem: B8 (8, 14) appears trapped in Strip 4 (bottom) by walls at (8, 8), (8, 9) and (9, 12-17).
- Action: Verify passability of (8, 8), (8, 9) and x=9 tiles.