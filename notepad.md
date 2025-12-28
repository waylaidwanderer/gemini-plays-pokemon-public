# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. (9, 2), (10, 2), (12, 4) on B3F. Blocks N->S and S->N movement.
- LEDGE_HOP_RIGHT: One-way jump from West to East. (11, 8), (11, 9) on B3F.

# Ice Path Exploration
- Start Turn (B3F): 29033
- Goal: Reach Blackthorn City.

## Ice Path B3F
- Item: (5, 7). Blocked by ROCK at (6, 6).
- ROCK (ID 2) at (6, 6): Confirmed Rock Smash target (Turn 29041).
- Ladder to B2F: (3, 5).
- Ladder to B4F: (15, 5).

## Strategy
1. Proceed to ladder at (15, 5) to bypass Rock Smash requirement.

## History (Archive)
- B1F Puzzle: Solved Turn 28985.
- B2F Puzzle: Solved Turn 29028.
- B3F Rock: Verified Rock Smash requirement at Turn 29041. Proceeding to bypass.

# Ice Path B2F (Blackthorn Side)
- Start Turn: 29044
- Goal: Find the exit to Blackthorn City.

## Exploration
- Just arrived from B3F via ladder at (3, 3).
- Map appears to have a large ice section to the south and east.
- Initial surroundings: FLOOR at (3, 3), (2, 3), (3, 1), (4, 1). WALL at (3, 0), (4, 0), (4, 3), (1, 1), (2, 1).
- FLOOR_UP_WALL (ledge face) at (3, 4). Testing if it's a jumpable ledge or just a wall.

## Strategy
1. Explore the reachable floor areas near the ladder.
2. Navigate the ice puzzle to find the exit.
3. Record all new tile behaviors and obstacles.