# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S movement (S->N unverified). Verified at (3, 4) and (6, 2) on B2F.
- LEDGE_HOP_RIGHT: One-way jump West to East. (11, 8), (11, 9) on B3F.
- LEDGE_HOP_LEFT: One-way jump East to West. (4, 8) on B2F.
- LEDGE_HOP_DOWN: One-way jump North to South. (5, 9) on B2F.

# Ice Path Exploration
- Start Turn (B2F Blackthorn Side): 29044
- Goal: Reach Blackthorn City.

## Strategy
1. Walk to (6, 5) via northern corridor: (2,2)->(3,2)->(3,1)->(6,1)->(6,5).
2. Move Down from (6, 5) onto ICE (6, 6). Slide Down to stop on FLOOR at (6, 8).
3. Walk to (5, 8).
4. Jump West over ledge (4, 8) to (3, 8) (ICE). Player slides to (0, 8).
5. Move Right from (0, 8) to slide to (3, 8).
6. Move Down from (3, 8) to slide to (3, 14) (FLOOR).
7. Walk to exit ladder (3, 15).

## Hypotheses
- Item at (8, 16) was TM44 Rest. (Note: Labeled as 'Potential HM07' prior to collection).

## Reflection & Lessons Learned
- Warp Pathing: Navigate tool does not avoid warp tiles. Use intermediate coordinates.
- Ledge Verification: (3, 4) on B2F is a FLOOR_UP_WALL and is impassable from the North.
- B3F Rock: The rock at (6, 6) on B3F requires Rock Smash.
- Time Tracking: Exploration of B2F (Blackthorn Side) began at Turn 29044. Progress is efficient.