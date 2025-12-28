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
1. Move Right from (0, 8) to slide to (3, 8).
2. Move Down from (3, 8) to slide to (3, 14) (FLOOR).
3. Walk to exit ladder (3, 15).

## Hypotheses
- Item at (8, 16) was TM44 Rest.

## Reflection & Lessons Learned
- Warp Pathing: Navigate tool does not avoid warp tiles. Use intermediate coordinates.
- Ledge Verification: (3, 4) on B2F is a FLOOR_UP_WALL and is impassable from the North.
- B3F Rock: The rock at (6, 6) on B3F requires Rock Smash.
- Time Tracking: Exploration of B2F (Blackthorn Side) began at Turn 29044. Progress is efficient.