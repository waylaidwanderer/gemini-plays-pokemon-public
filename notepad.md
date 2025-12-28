# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S movement. Verified at (3, 4) and (6, 2) on B2F and (9, 2), (10, 2), (12, 4) on B3F.
- LEDGE_HOP_RIGHT: One-way jump West to East. (11, 8), (11, 9) on B3F.
- LEDGE_HOP_LEFT: One-way jump East to West. (4, 8) on B2F and (34, 16) on 1F.
- LEDGE_HOP_DOWN: One-way jump North to South. (5, 9) on B2F and (35, 17), (36, 17), (37, 17) on 1F.

# Ice Path Exploration
- Goal: Reach Blackthorn City.

## Strategy (1F Item & Exit)
- Current Position: (32, 18).
1. Slide Down to (32, 22) (FLOOR).
2. Collect item at (32, 23).
3. Slide Up to (32, 18).
4. Slide Right to (34, 18).
5. Slide Down to (34, 22).
6. Walk to exit at (36, 25).

## Lessons Learned
- Warp Pathing: The `navigate` tool does not automatically avoid warp tiles. Use intermediate coordinates to steer around ladders/doors.
- B3F Rock: The rock at (6, 6) on B3F requires Rock Smash.
- Item at (8, 16) on B2F was TM44 Rest.

## History (Archive)
- B1F/B2F Puzzles: Solved.
- Reached 1F Blackthorn Side at Turn 29107.
- Turn 29113: Performing mandatory self-assessment. Notepad reorganized. Path to (32, 23) in progress.