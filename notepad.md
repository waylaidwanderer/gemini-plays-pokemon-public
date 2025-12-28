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

## Strategy (B1F Exit)
1. Slide Left from (17, 31) to (13, 31) (Hits WALL at 12,31).
2. Slide Up to (13, 30) (Hits WALL at 13,29).
3. Slide Left to (11, 30) (FLOOR).

## Hypotheses
- Item at (8, 16) was TM44 Rest (Verified).
- The exit to 1F is in the southern floor area (Row 30+).