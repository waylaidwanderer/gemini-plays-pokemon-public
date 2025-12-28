# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S and S->N movement. Verified at (9, 2), (10, 2), (12, 4) on B3F.
- LEDGE_HOP_RIGHT: One-way jump from West to East. (11, 8), (11, 9) on B3F.
- LEDGE_HOP_LEFT: One-way jump from East to West. (4, 8) on B2F.
- LEDGE_HOP_DOWN: One-way jump from North to South. (5, 9) on B2F.

# Ice Path Exploration
- Start Turn (B3F): 29033
- Start Turn (B2F Blackthorn Side): 29044
- Goal: Reach Blackthorn City.

## Ice Path B2F (Blackthorn Side)
- Status: Exploring western floor area.
- Ladder to B3F: (3, 3).
- Potential Ledge: (3, 4) (FLOOR_UP_WALL).
- Observed ICE: Starts at row 6.

## Strategy
1. Navigate to (6, 1) via the northern corridor, avoiding the ladder at (3, 3).
2. Test if (6, 2) (FLOOR_UP_WALL) is traversable from the North.
3. If traversable, reach (6, 5) and slide Down to (6, 8).
4. If blocked, explore (9, 0)-(9, 7) to find a path to the eastern floor.
5. From (5, 8), jump Left over the ledge at (4, 8) to land on (3, 8).
6. Slide Down from (3, 8) to land on the floor at (3, 14).
7. Walk to the exit ladder at (3, 15).

## History (Archive)
- B1F Puzzle: Solved Turn 28985.
- B2F Puzzle (Mahogany Side): Solved Turn 29028.
- B3F Rock: Verified Rock Smash requirement at Turn 29041. Bypassed.
- B2F (Blackthorn Side): Slid to (0, 17) and returned to (0, 5) at Turn 29054. planning path to exit.