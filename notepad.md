# Strategic Objectives
- **Primary:** Earn Rising Badge.
- **Secondary:** Pass Dragon User Challenge.
- **Immediate:** Reach the Dragon Shrine via the East Whirlpool.

# Current Status (Turn 18306)
- **Location:** Dragon's Den B1F (25, 22).
- **Facing:** Down (Towards Whirlpool at 25, 23).
- **Action:** Switch Lapis (Poliwag) to Slot 1.
- **Reasoning:** Direct interaction failed. Putting the Whirlpool user in the lead slot often fixes interaction issues or makes "Press A" work more reliably. Also allows confirming menu navigation works.
- **Sequence:**
  1. `Start` (Open Menu).
  2. `A` (Pokemon).
  3. `A` (Select Gyarados/Lead).
  4. `Down` -> `A` (Select 'Switch').
  5. `Down` -> `Down` -> `A` (Select Lapis/Slot 3).
  6. `B` -> `B` (Close Menus).

# Plan
1. Switch Lapis to Lead (This turn).
2. Interact with Whirlpool at (25, 23) using 'A'.
3. If successful, Navigate South to Dragon Shrine.
4. If fails, try Menu -> Pokemon -> Lapis -> Whirlpool again.

# Tile Mechanics
- **Whirlpool:** Requires HM06 Whirlpool + Glacier Badge.
- **Cage Layout:** Player seems confined in an area (x=24-26, y=20-23) bounded by walls and buoys/whirlpools. Escaping requires clearing a whirlpool.

# Tile Mechanics
- **Whirlpool:** Requires HM06 Whirlpool + Glacier Badge. 
- **Lava/Magma:** (None here).
- **Ice:** (None here).

# Lessons
- **Menu Navigation:** Always verify cursor position before committing to a sequence. Blind input leads to wrong menus (e.g., PACK instead of POKEMON).