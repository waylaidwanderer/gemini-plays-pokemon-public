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
- Status: Navigating to the south exit.
- Ladder to B3F: (3, 3).
- Exit Ladder: (3, 15).

## Strategy
1. Walk West from (9, 8) to (5, 8) (all FLOOR).
2. Jump West over LEDGE_HOP_LEFT at (4, 8) to land on (3, 8) (ICE).
3. Slide Down from (3, 8) through ICE to stop on FLOOR at (3, 14).
4. Walk to exit ladder at (3, 15).

## History (Archive)
- B1F Puzzle: Solved Turn 28985.
- B2F Puzzle (Mahogany Side): Solved Turn 29028.
- B3F Rock: Verified Rock Smash requirement at Turn 29041. Bypassed.
- B2F (Blackthorn Side): Reached (9, 8) at Turn 29060. Path to exit is clear.