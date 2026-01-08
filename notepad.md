# Blackthorn Gym (Puzzle Progress)
- Start Turn: 34501
- Pits (2F): P1 (8, 3), P2 (2, 5), P3 (8, 7).
- Boulders (2F): B6 (3, 3), B7 (6, 1), B8 (8, 14) [Default Positions].
- Floor Reset: Using a ladder or falling into a pit resets all boulder positions on 2F. (Verified Turn 34678).
- Push Mechanic: Player stays in the same tile after pushing a boulder. (Verified Turn 34644).

# Verified Connections & Obstacles
- (4, 13): FLOOR (Turn 34723).
- (4, 12): WALL (Turn 34724).
- (8, 15): FLOOR.
- (8, 9): WALL (Turn 34721).
- Fran (4, 11): Impassable NPC (Turn 34709).
- Cody (4, 1): Likely Impassable NPC.

# Strategy: Blackthorn Gym 2F
- Goal: Determine the intended path for Boulder 8 (8, 14).
- Hypothesis: One of the 'walls' in column 7 or 9 is actually a passable floor, allowing B8 to reach Pit 3 (8, 7) via a detour.
- Test Plan:
    1. Activate Strength.
    2. Push B8 UP to (8, 13).
    3. Test passability of (9, 13) and (9, 14).
    4. If passable, push B8 into column 9 and navigate north.

# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable collision (pillars, statues, rocks).
- PIT: Impassable on 2F; fills gap on 1F.
- LADDER: Warp between floors.
- BOULDER: Pushable object (requires Strength).

# Resource Locations
- Route 45: Good training spot for Haunter (Night Shade).