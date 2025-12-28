# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S movement.
- LEDGE_HOP_RIGHT: One-way jump West to East.
- LEDGE_HOP_LEFT: One-way jump East to West.
- LEDGE_HOP_DOWN: One-way jump North to South.
- Warp Pathing: Navigate tool does not automatically avoid warp tiles. Use intermediate coordinates to steer around.

# Ice Path Exploration
- Goal: Reach Blackthorn City.

## Strategy (1F Exit)
1. Move Up to (32, 22).
2. Move Up to (32, 21) -> Slide to (32, 18).
3. Move Right to (33, 18) -> Slide to (37, 18).
4. Move Down to (37, 19) -> Slide to (37, 21).
5. Move Left to (36, 21) -> Slide to (34, 21).
6. Move Down to (34, 22).
7. Walk to exit at (36, 25) via (36, 22).

## History (Archive)
- B1F/B2F Puzzles: Solved.
- TM44 Rest collected at (8, 16) on B2F (Turn 29075).
- PP UP collected at (32, 23) on 1F (Turn 29116).