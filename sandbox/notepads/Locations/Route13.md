# Route 13 - Overworld Mapping & Navigation

## Map Transitions & Connections
- **North Connection (Route 12):** Transition at Route 12 `(11, 107)` / `(11, 108)` which connects directly to Route 13 at `(51, 0)` on the northeast wooden dock (Player entered Route 13 on Turn 19120).
- **West Connection (Route 14):** Transition at Route 13 `(0, 4)` connects directly to Route 14 at `(19, 4)` on the eastern row 4 corridor (Player entered Route 14 on Turn 19499).

## Physical Layout & Navigation
- The route begins with a wooden dock at the northeast starting at `(51, 0)`.
- The dock runs south to row 11, then turns west horizontally.
- Row 12 and below on columns 47-51 are water.
- Row 10 has trainers standing on the dock.
- **Picket Fence Maze Boundaries:**
  - Row 10 has a permanent block at `(7, 10)` by a defeated Bird Keeper who remains standing there forever, requiring a detour through Row 11 (columns 7 to 9) to bypass him.
  - Row 12 is blocked at column 16 by impassable brown logs `(16, 12)`.
  - Columns 1-5 on Row 12 form a dead-end pocket with no western or northern exit, as Row 11 is completely blocked on columns 1-5 by log fences, and Column 0 is blocked on Row 12 by logs.
  - Row 11 is blocked at column 34 by logs.
  - The white picket fence at `(6, 11)` is solid and impassable, leaving `(22, 11)` as the only verified walkable fence connection in the central area. Only column 22 on Row 11 connects Row 12 and Row 10 in that segment.
## Defeated Trainers
- **Beauty:** Standing at `(33, 6)` (challenged from `(32, 6)` on Turn 19409). Defeated on Turn 19434. Roster: Rattata Lv 27, Pikachu Lv 27, Rattata Lv 27. Prize money: ¥1890.
- **Bird Keeper:** Standing at `(50, 10)` after challenging from `(49, 10)` on Turn 19124. Defeated on Turn 19139. Roster: Pidgey Lv 29, Pidgeotto Lv 29. Prize money: ¥725.
- **Jr. Trainer♀ (Piknicker):** Standing at `(48, 10)` after challenging from `(48, 11)` on Turn 19143. Defeated on Turn 19176. Roster: Pidgey Lv 24, Meowth Lv 24, Rattata Lv 24, Pikachu Lv 24, Meowth Lv 24. Prize money: ¥480.
- **Beauty:** Standing at `(32, 6)` (moved to `(32, 7)` to challenge from `(32, 8)`). Defeated on Turn 19234. Roster: Clefairy Lv 29, Meowth Lv 29. Prize money: ¥2030.
- **Jr. Trainer♀:** Standing at `(27, 9)` after challenging from `(27, 10)` on Turn 19237. Defeated on Turn 19253. Roster: Poliwag Lv 30, Poliwag Lv 30. Prize money: ¥600.
- **Jr. Trainer♀:** Standing at `(23, 10)` after challenging from `(23, 10)` (facing left) on Turn 19263. Defeated on Turn 19297. Roster: Pidgey Lv 27, Meowth Lv 27, Pidgey Lv 27, Pidgeotto Lv 27. Prize money: ¥540.
- **Bird Keeper:** Standing at `(7, 11)` (challenged from `(7, 10)` on Turn 19302). Defeated on Turn 19337. Roster: Pidgey Lv 26, Pidgeotto Lv 26, Spearow Lv 26, Fearow Lv 26. Prize money: ¥624.

## Points of Interest
- None yet discovered.

## Mechanics & Collision
- **Walkable Picket Fences:** The white picket fence tiles of Route 13 are walkable and passable, allowing the player to navigate directly through them to traverse the maze. However, the brown log fences are solid and impassable.
## Detailed Maze Layout & Collision Coordinates
- **Row 4:** Row 4 is a horizontal corridor extending across the map, but it is blocked at Column 26 `(26, 4)` by a log fence, and has a Cut-able tree at `(34, 4)` that regenerates when scrolled off-screen. Bypassing the Column 26 log fence requires walking Down to Row 6, West to column 17, Down to Row 8, and East along Row 8 past Column 26.
- **Row 5:** Blocked by log fences from column 16 to column 22.
- **Row 6:** Open from column 17 to column 27, but blocked at `(16, 6)` by a log fence.
- **Row 7:** Blocked by log fences from column 12 to 16, and column 18 to 22. Column 17 is empty and passable.
- **Row 8:** Open from column 13 to column 26, but blocked at `(12, 8)` by a log fence.
- **Row 9:** Blocked by log fences across column 6 to 12, and column 14 to 27. Column 13 is a dead-end pocket.
- **Row 11:** Blocked by log fences from column 0 to column 6 on the west, and column 10 to 16 on the east. But `(22, 11)` has a walkable white picket fence connecting row 12 and row 10.

## Mechanics
- **Off-Screen Tree Respawning:** CUT-able trees (such as the one at `(34, 4)`) regenerate automatically when they are scrolled off-screen. Plan routing with tree respawns in mind.
- **Biker:** Standing at `(10, 7)` (challenged from `(10, 6)` on Turn 19988). Defeated on Turn 20011.

## Verified Maze Path & Gaps (Verified Turn 42969)
Traversing Route 13 from west to east requires navigating around several solid log fence blocks and NPCs:
1. **West Entrance:** Enter at `(0, 4)` from Route 14 `(19, 4)` on the Row 4 corridor.
2. **First Slalom Bypass (Columns 11-13):**
   - Row 4 is blocked at Column 12 by the defeated Beauty NPC at `(12, 4)`.
   - Row 5 has log fences from Column 5 to Column 11.
   - To bypass: Walk LEFT to `(10, 4)`. Walk DOWN to `(10, 5)` (open grass!). Walk RIGHT 3 steps to `(13, 5)` (open grass!). Walk UP to `(13, 4)` (paved path). This completely bypasses the Beauty NPC at `(12, 4)`.
3. **Second Slalom Bypass (Columns 17-26):**
   - Row 4 is blocked at Column 26 `(26, 4)` by a log fence.
   - Bypassing requires: Walk DOWN from `(25, 4)` to `(25, 6)`. Walk LEFT 8 steps along Row 6 (which is completely open) to Column 17 `(17, 6)`. Walk DOWN 2 steps through the Row 7 Column 17 gap `(17, 7)` to Row 8 Column 17 `(17, 8)`. Walk RIGHT 10 steps along Row 8 (completely open) to Column 27 `(27, 8)`. This completely bypasses the Column 26 fence!
4. **Third Slalom Bypass (Columns 27-36):**
   - From `(27, 8)`, walk LEFT to `(26, 8)`. Walk DOWN 2 steps to Row 10 `(26, 10)` (Row 10 is completely open horizontally).
   - Walk RIGHT along Row 10 all the way to `(36, 10)` onto the wooden dock.
5. **Northeast Wooden Highway (Columns 36-51):**
   - Row 10 is blocked at Column 48 by the defeated Piknicker and Bird Keeper.
   - To bypass: Walk DOWN 1 step to Row 11 `(47, 11)` (Row 11 is completely open wooden dock). Walk RIGHT 4 steps to Column 51 `(51, 11)`. Walk UP 11 steps along Column 51 to `(51, 0)` on the northeast corner of Route 13, which transitions directly UP into Route 12 at `(11, 107)`.