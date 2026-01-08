# Game Mechanics & Systems
## Tile Mechanics (Confirmed)
- FLOOR / TALL_GRASS / GRASS: Walkable.
- WALL / COUNTER / PC / FLOOR_UP_WALL (from North): Impassable. (Verified FLOOR_UP_WALL at 13, 12; 11-14, 58; 11, 88).
- WATER: Requires Surf to traverse.
- WARP_CARPET_DOWN / DOOR / LADDER: Triggers map transition.
- HEADBUTT_TREE: Interact to use Headbutt.
- LEDGE_HOP_DOWN (⤵️): One-way movement from North to South. Landing on the tile below. (Verified at 17, 13; 12, 25; 12, 29; 10, 45; 10, 47; 10, 53; 16, 59; 17, 59; 11, 85; 21, 32).

## Type Effectiveness Chart (Verified)
- Acid (Poison) -> Gligar (Ground/Flying): Not very effective.
- Flame Wheel (Fire) -> Donphan (Ground): Neutral.

## Money & Economy
- AMULET COIN: Doubles prize money from trainer battles. (Held by ICARUS).

# Pokemon & Party Information
## Party Strategy
- **Training Session (Route 45):** Started Turn 33466. (Last Updated: Turn 33943).
  - Goal: Xenon and Kimchi to Lv40.
  - Method: KIMCHI holds EXP.SHARE. Lead XENON (Ghost immunity to Selfdestruct).
  - Progress: Xenon Lv36, Kimchi Lv33.

# Area Mechanics & Strategy
## Strategy for Rising Badge (Gym Leader Clair)
- Status: Gym trainers defeated. Boulders pushed into pits.
- Opponent: Clair uses Dragon-type Pokemon (Dragonair, Kingdra).
- Strategy:
  - GNEISS (Lv48): Physical damage.
  - XENON (Lv36): Night Shade and Hypnosis (固定 damage and control).
  - CALCIFER (Lv49): Thunderpunch for coverage vs Kingdra.
- Blocked Unseen: (14, 61-62). (Hypothesis: Reachable from the strip starting at x=14-15 at the top of Route 45).

# Exploration Log
- Items: Max Potion at (7, 33), Mysteryberry from (16, 82).
- Trainers: All trainers in middle/right strips defeated (Kenji, Michael, Timothy, Erik, etc.).
- Basin Hypothesis: All southern strips end in basins or exits. Strip 1 (x=0-2) ends at y=81 (Warp to R46). Strip 2-4 (x=4-11) ends at y=87. Strip 5 (x=12-17) ends at y=83.
- Strategy: RESET COMPLETE. Landed in Blackthorn. Now heading to PokeCenter (21, 29) to heal, then to eastern entrance (x=15-18) via ledge at (21, 32).
- Target Unseen: (17-19, 86-89) in the rightmost strip of Route 45.

# Lessons Learned
- **Ghost Lead:** Haunter lead is ideal for wild Graveler encounters (Selfdestruct immunity).
- **Strips & Ledges:** Route 45 is a one-way system of vertical strips. Exit to Route 46 is in the leftmost strip (x=0-2).
- **Basin Navigation:** Some strips are connected at specific latitudes (e.g., y=83 connects middle and right strips).
- **Blackthorn Wall:** A wall at y=34 blocks most eastern exits. Use the ledge at (21, 32) to reach the southern edge.
- **Menu Verification:** Always check the current screen before executing long button sequences to avoid logic loops.