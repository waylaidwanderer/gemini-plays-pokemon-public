# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S and S->N movement. Verified at (9, 2), (10, 2), (12, 4) on B3F.
- LEDGE_HOP_RIGHT: One-way jump from West to East. (11, 8), (11, 9) on B3F.

# Ice Path Exploration
- Start Turn (B3F): 29033
- Start Turn (B2F Blackthorn Side): 29044
- Goal: Reach Blackthorn City.

## Ice Path B3F (Completed)
- Item: (5, 7). Blocked by ROCK at (6, 6).
- ROCK (ID 2) at (6, 6): Confirmed Rock Smash target (Turn 29041).
- Ladder to B2F/B4F: (15, 5).

## Ice Path B2F (Blackthorn Side)
- Status: Exploring western floor area.
- Ladder back to B3F: (3, 3).
- Potential Ledge: (3, 4) (FLOOR_UP_WALL).

## Strategy
1. Map the western floor section and test the ledge at (3, 4).
2. Enter the ice at (0, 6) to reach the southern unseen area.
3. Locate the exit to Blackthorn City.

## History (Archive)
- B1F Puzzle: Solved Turn 28985.
- B2F Puzzle (Mahogany Side): Solved Turn 29028.
- B3F Rock: Verified Rock Smash requirement at Turn 29041. Bypassed.
- Note: Accidentally took the ladder at (3, 3) on B2F back to B3F. Navigating back to B2F. Be careful to avoid warp tiles in path plans.