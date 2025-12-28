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
1. Navigate to (9, 3) via the northern corridor, avoiding the ladder at (3, 3).
2. Slide Down from (9, 4) to stop on FLOOR at (9, 8).
3. Walk to (5, 8).
4. Jump Down over the ledge at (5, 9) to land on (5, 10) (ICE).
5. Slide Down from (5, 10) to stop on ICE at (5, 16) (hits wall at (5, 17)).
6. Slide Right from (5, 16) to stop on FLOOR at (8, 16).
7. Collect the item (Potential HM07 Waterfall).
8. Exit via the ladder at (3, 15).

## History (Archive)
- B1F Puzzle: Solved Turn 28985.
- B2F Puzzle (Mahogany Side): Solved Turn 29028.
- B3F Rock: Verified Rock Smash requirement at Turn 29041. Bypassed.
- B2F (Blackthorn Side): Reached southern floor at Turn 29064. Planning item collection.
## Reflection & Lessons Learned (Turn 29061)
- **Warp Pathing:** The `navigate` tool does not automatically avoid warp tiles (ladders, doors, exit mats) unless they are the destination. To avoid accidental floor changes, always use intermediate coordinates to steer the path plan around these tiles.
- **Ledge Verification:** (3, 4) on B2F is a FLOOR_UP_WALL (ledge face) and is impassable from the North.
- **B3F Rock:** The rock at (6, 6) on B3F requires Rock Smash. Since this move is currently unavailable, the item at (5, 7) is temporarily inaccessible.
- **Ice Path Exit:** The ladder at (3, 15) on B2F is the primary target for exiting to Blackthorn City.
- **Time Check:** Exploration of B3F/B2F (Blackthorn Side) began at Turn 29033. Total time in cave: ~30 turns. Progression is efficient.