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
- Start Turn (1F Blackthorn Side): 29107
- Goal: Reach Blackthorn City.

## Strategy (1F Blackthorn Section)
1. Slide Left from (37, 21) to (34, 21).
2. Walk to (36, 25) to exit to Blackthorn City.
3. (Optional) Explore for item at (32, 23).

## Hypotheses
- The exit at (36, 25) leads directly to Blackthorn City.
- Item at (32, 23) is accessible from the south or via a slide from the north.

## History (Archive)
- B1F Puzzle: Solved Turn 28985.
- B2F Puzzle (Mahogany Side): Solved Turn 29028.
- B3F Rock: Verified Rock Smash requirement at Turn 29041. Bypassed.
- TM44 Rest collected at (8, 16) on B2F (Turn 29075).