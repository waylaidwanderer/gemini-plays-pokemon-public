# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S movement (S->N unverified). Verified at (3, 4) on B2F and (9, 2), (10, 2), (12, 4) on B3F.
- LEDGE_HOP_RIGHT: One-way jump from West to East. (11, 8), (11, 9) on B3F.
- LEDGE_HOP_LEFT: One-way jump from East to West. (4, 8) on B2F.
- LEDGE_HOP_DOWN: One-way jump from North to South. (5, 9) on B2F.

# Ice Path Exploration
- Start Turn (B2F Blackthorn Side): 29044
- Goal: Reach Blackthorn City.

## Ice Path B2F (Blackthorn Side)
- Ladder to B3F: (3, 3).
- Exit Ladder: (3, 15).

## Hypotheses
- Item at (8, 16) is HM07 Waterfall.

## Strategy
1. Pick up item at (8, 16).
2. Slide Left to (0, 16).
3. Slide Up to (0, 5) (FLOOR).
4. Walk to (9, 3) via northern corridor: (0,5)->(0,4)->(1,4)->(1,3)->(2,3)->(2,2)->(3,2)->(3,1)->(9,1)->(9,3).
5. Slide Down from (9, 4) to (9, 8) (FLOOR).
6. Walk to (5, 8).
7. Jump West over ledge (4, 8) to (3, 8) (ICE).
8. Slide Down to (3, 14) (FLOOR).
9. Walk to exit ladder (3, 15).

## Reflection & Lessons Learned
- Warp Pathing: The navigate tool does not automatically avoid warp tiles. Use intermediate coordinates.
- Ledge Verification: (3, 4) on B2F is a FLOOR_UP_WALL and is impassable from the North.
- B3F Rock: The rock at (6, 6) on B3F requires Rock Smash. Item at (5, 7) is temporarily inaccessible.
- Ice Path Exit: The ladder at (3, 15) on B2F is the primary target for exiting to Blackthorn City.
- Time Tracking: Exploration of B2F (Blackthorn Side) began at Turn 29044. Progress is efficient.