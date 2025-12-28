# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S and S->N movement. Verified at (3, 4) on B2F and (9, 2), (10, 2), (12, 4) on B3F.
- LEDGE_HOP_RIGHT: One-way jump from West to East. (11, 8), (11, 9) on B3F.
- LEDGE_HOP_LEFT: One-way jump from East to West. (4, 8) on B2F.
- LEDGE_HOP_DOWN: One-way jump from North to South. (5, 9) on B2F.

# Ice Path Exploration
- Start Turn (B3F): 29033
- Start Turn (B2F Blackthorn Side): 29044
- Goal: Reach Blackthorn City.

## Ice Path B2F (Blackthorn Side)
- Status: Navigating to the item at (8, 16).
- Ladder to B3F: (3, 3).
- Exit Ladder: (3, 15).

## Strategy
1. Move Down from (6, 5) onto ICE (6, 6). Slide Down to stop on FLOOR at (6, 8).
2. Walk to (5, 8).
3. Jump Down over the ledge at (5, 9) to land on (5, 10) (ICE).
4. Slide Down from (5, 10) to stop on ICE at (5, 16) (hits wall at (5, 17)).
5. Move Right from (5, 16) to slide to (8, 16) (FLOOR).
6. Collect the item (Potential HM07 Waterfall).
7. Slide Left from (8, 16) to stop on WALL at (0, 16).
8. Slide Up to (0, 14).
9. Slide Right to stop on FLOOR at (2, 14).
10. Walk to exit ladder at (3, 15).

## History (Archive)
- B1F Puzzle: Solved Turn 28985.
- B2F Puzzle (Mahogany Side): Solved Turn 29028.
- B3F Rock: Verified Rock Smash requirement at Turn 29041. Bypassed.
- B2F (Blackthorn Side): Reached (6, 5) at Turn 29068.