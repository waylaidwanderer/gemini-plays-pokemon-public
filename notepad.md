# Tile Mechanics (Global)
- FLOOR: Walkable.
- WALL: Impassable.
- ICE: Sliding mechanic. Moving onto ICE causes player to slide until hitting a WALL, non-ICE tile, or BOULDER.
- BOULDER: Stopper for sliding.
- ROCK: Destructible with ROCK SMASH. (6, 6) on B3F is a ROCK.
- FLOOR_UP_WALL: Impassable ledge face. Blocks N->S movement (S->N unverified). Verified at (3, 4) and (6, 2) on B2F and (9, 2), (10, 2), (12, 4) on B3F.
- LEDGE_HOP_RIGHT: One-way jump West to East. (11, 8), (11, 9) on B3F.
- LEDGE_HOP_LEFT: One-way jump East to West. (4, 8) on B2F.
- LEDGE_HOP_DOWN: One-way jump North to South. (5, 9) on B2F.

# Ice Path Exploration
- Start Turn (B2F Blackthorn Side): 29044
- Goal: Reach Blackthorn City.

## Strategy (B1F Southern Section)
1. Walk West along Row 30 to explore unseen area: (11, 30) -> (7, 30) -> (6, 30).
2. Locate the exit ladder to 1F.

## Hypotheses
- The exit to 1F is in the southern floor area (Row 30+).
- TM44 Rest was at (8, 16) on B2F. Verified.