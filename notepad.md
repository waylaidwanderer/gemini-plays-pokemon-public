# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S movement. (S->N unverified). Verified at (3, 4) and (6, 2) on B2F and (9, 2), (10, 2), (12, 4) on B3F.
- LEDGE_HOP_RIGHT: One-way jump West to East. (11, 8), (11, 9) on B3F.
- LEDGE_HOP_LEFT: One-way jump East to West. (4, 8) on B2F.
- LEDGE_HOP_DOWN: One-way jump North to South. (5, 9) on B2F.

# Ice Path Exploration
- Start Turn (B2F Blackthorn Side): 29044
- Start Turn (B1F Exit Area): 29086
- Goal: Reach Blackthorn City.

## Strategy
1. Navigate to (12, 28) (FLOOR).
2. Move Down onto ICE at (12, 30) and slide Left to stop on FLOOR at (11, 30).
3. Explore the southern area from (11, 30) to find the exit ladder.

## Hypotheses
- The exit to 1F is located in the southern part of this B1F section.
- Item at (8, 16) was TM44 Rest.

## Reflection & Lessons Learned
- Warp Pathing: Navigate tool does not avoid warp tiles. Use intermediate coordinates.
- Ledge Verification: (3, 4) and (6, 2) on B2F are FLOOR_UP_WALL and are impassable from the North.
- B3F Rock: The rock at (6, 6) on B3F requires Rock Smash.
- Time Tracking: Progression is efficient. Item TM44 Rest collected at Turn 29075.