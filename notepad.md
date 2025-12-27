# Post-Game: Kanto Adventure
- **Status:** Exploring Saffron Gym.
- **Goal:** Earn Marsh Badge.
- **Task Start:** Turn 20979 (Warp Puzzle).

# Warp Puzzle Log
- **Room 1 (Entrance):**
    - Warp A (11, 15) <-> Room 2 (19, 17) [Warp B]
- **Room 2 (Bottom Right):**
    - Warp B (19, 17) <-> Room 1 (11, 15) [Warp A]
    - Warp C (19, 15) -> Room 3 (19, 9) [Warp F]
    - Warp D (15, 17) -> Room 5 (5, 15) [Warp N]
    - Warp E (15, 15) -> Room 2 (15, 15) [Self-Loop]
- **Room 3 (Middle Right):**
    - Warp F (19, 9) [From C]
    - Warp G (15, 9) -> Room 4 (15, 3) [Warp J]
    - Warp H (19, 11) [From W]
    - Warp I (15, 11) -> Room 6 (9, 3) [Warp U]
- **Room 4 (Top Right) [Current]:**
    - Warp J (15, 3) [From G]
    - Warp K (19, 3) -> Room 2 (15, 15) [Warp E]
    - Warp L (15, 5) [From BB]
    - Warp M (19, 5) -> ?
- **Room 5 (Bottom Left):**
    - Warp N (5, 15) [From D]
    - Warp O (1, 15) -> ?
    - Warp P (1, 17) -> Room 6 (11, 5) [Warp R]
    - Warp Q (5, 17) -> ?
- **Room 6 (Top Center):**
    - Warp R (11, 5) [From P]
    - Warp S (9, 5) -> Room 7 (5, 9) [Warp V]
    - Warp T (11, 3) -> Room 8 (5, 3) [Warp AA]
    - Warp U (9, 3) [From I]
- **Room 7 (Middle Left):**
    - Warp V (5, 9) [From S]
    - Warp W (1, 9) -> Room 3 (19, 11) [Warp H]
    - Warp X (1, 11) -> ?
    - Warp Y (5, 11) -> ?
- **Room 8 (Top Left):**
    - Warp AA (5, 3) [From T]
    - Warp BB (1, 3) -> Room 4 (15, 5) [Warp L]
    - Warp CC (1, 5) -> ?
    - Warp DD (5, 5) -> ?

# Current Plan
- **Immediate:** Handle Youngster interaction (Battle likely).
- **Next Steps:**
    1. Defeat Youngster.
    2. Test Warp M (19, 5).
    3. Determine if M leads to Sabrina or a new room.

# Tile Mechanics
- **WARP_PANEL:** Stepping on these instantly teleports the player to another location. If you arrive on one, you must step off and step back on to use it again.
- **FLOOR:** Standard walkable tile.
- **WALL:** Impassable tile.