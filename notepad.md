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
- Goal: Reach Blackthorn City.

## Strategy
- Current Position: (12, 28).
1. Walk to (17, 27) via (12,26) to avoid ladder.
2. Slide Down from (17, 27) to (17, 29).
3. Slide Right to (19, 29).
4. Slide Down to (19, 33).
5. Slide Left to (17, 33).
6. Slide Up to (17, 31).
7. Slide Left to (12, 31).
8. Slide Up to (12, 30).
9. Slide Left to (11, 30) (FLOOR).
10. Explore Row 30 West to find the exit.

## Hypotheses
- Item at (8, 16) was TM44 Rest (Verified).
- The exit to 1F is in the southern floor area (Row 30+).

## Reflection & Lessons Learned
- Warp Pathing: Navigate tool does not avoid warp tiles. Use intermediate coordinates.
- Ledge Verification: FLOOR_UP_WALL is an impassable wall from the north.
- Time Tracking: Progression is efficient. Item collected at Turn 29075.