# Route 14 - Overworld Mapping & Navigation

## Map Transitions & Connections
- **East Connection (Route 13):** Transition at Route 14 `(19, 4)` connects directly to Route 13 at `(0, 4)` on the eastern row 4 corridor (Player entered Route 14 on Turn 19499).

## Physical Layout & Navigation
- Row 4 is a completely open horizontal corridor from columns 4 to 19.
- Row 3 and Row 5 are blocked by impassable log fences from columns 4 to 19.
- Columns 4 and 5 on Row 5 have a walkable grass gap, allowing passage south from the Row 4 corridor.
- To the west of column 3, there appears to be a vertical boundary/ledge structure.
- Columns 1 and 2 contain vertical corridors of grass.

## Defeated Trainers
- **Bird Keeper:** Standing at `(4, 4)` (challenged after stepping to `(5, 4)` on Turn 19504). Defeated on Turn 19531. Roster: Pidgey Lv 28, Doduo Lv 28, Pidgeotto Lv 28. Prize money: 700.
- **Bird Keeper:** Standing at `(15, 6)` (challenged by talking from `(14, 6)` on Turn 19536). Defeated on Turn 19571. Roster: PIDGEY Lv 26, SPEAROW Lv 26, PIDGEY Lv 26, FEAROW Lv 26. Prize money: 650.
- **Bird Keeper:** Standing at `(12, 11)` (challenged on Turn 19578). Defeated on Turn 19614. Roster: Pidgeotto Lv 29, Fearow Lv 29. Prize money: 725.
- **Bird Keeper:** Standing at `(14, 15)` (challenged on Turn 19617). Defeated on Turn 19643. Roster: Spearow Lv 28, Doduo Lv 28, Fearow Lv 28. Prize money: 700.

## Points of Interest
- None yet discovered.

## Mechanics & Collision
- **Log Fences:** Log fences on Row 3 and Row 5 are solid and impassable, completely sealing Row 4 into a corridor except for the gap at columns 4-5 on Row 5.

## Detailed Layout Constraints & Obstacles
- **Vertical Barrier (Column 3):** Column 3 serves as the western boundary wall/cliff separating the eastern paved corridor from the western grass lanes of Route 14. However, at the bottom of the route (around Row 48), the wall ends, allowing horizontal traversal between the east and west sides of the route.
- **Row 11 Blockage:** Row 11 is completely blocked by solid log fences across columns 4 to 19, except for a single-tile gap at `(13, 11)`.
- **Row 12 Ledge:** Located at `(13, 12)`. Passing south through the `(13, 11)` gap requires jumping down this one-way ledge to `(13, 13)`.
- **Row 50 Stone Wall:** Row 50 is completely blocked by an unbroken solid stone wall/fence across columns 4 to 17, preventing direct southern passage from the paved side. To proceed south towards Route 15, players must bypass the Bikers/Bird Keepers (such as the one at `(6, 49)`) on the west side of column 12 to reach the southwest corner of Route 14 (columns 0-2, rows 48-49), which transitions directly west into Route 15.
- **Bird Keeper:** Standing at `(6, 49)` (challenged on Turn 20058). Defeated on Turn 20076. Roster: Spearow Lv 29, Fearow Lv 29. Prize money: ¥725.
- **Route 15 Connection Turn:** Transition to Route 15 occurred on Turn 20078.

## Verified Nested Slalom Maze Gaps (Verified Turn 42964)
Traversing Route 14 from south to north requires navigating a series of nested log fences that create a slalom maze. The walkable gaps in these horizontal barriers are:
1. **Row 11 Fence:** The ONLY gap is at `(13, 11)` (which was previously thought to be a one-way ledge, but is fully walkable UP and DOWN).
2. **Row 9 Fence:** The ONLY gap is at `(6, 9)` and `(7, 9)` (open grass).
3. **Row 5 Fence:** The ONLY gap is at `(4, 5)` and `(5, 5)` (open grass).
4. **Row 7 Fence:** The ONLY gap is at `(14, 7)` and `(15, 7)`.

### Step-by-Step Slalom Routing (Northbound from Row 16 to Row 4)
1. From `(14, 16)`, walk left to `(13, 16)`.
2. Walk UP through the Row 11 gap at `(13, 11)` to `(13, 10)`.
3. Walk LEFT to columns 6-7 (e.g., `(7, 10)`).
4. Walk UP through the Row 9 gap at `(7, 9)` to Row 8 (e.g., `(7, 8)`).
5. Walk RIGHT to Column 14 (e.g., `(14, 8)`).
6. Walk UP through the Row 7 gap at `(14, 7)` to Row 6 (e.g., `(14, 6)`).
7. Walk LEFT to columns 4-5 (e.g., `(5, 6)`).
8. Walk UP through the Row 5 gap at `(5, 5)` to Row 4 (`(5, 4)`).
9. Walk RIGHT along the Row 4 corridor to transition into Route 13 at `(19, 4)`!