# Pokémon Mansion 2F - Map & Navigation Log

## Physical Layout & Permanent Barriers
- **Stairs to 1F West:** Located at `(7, 10)`. Descending places the player at `(7, 11)` on 1F West.
- **Stairs to 3F West:** Located at `(6, 1)` on 2F West (ascending). Stepping on it warps player up to 3F West, landing at `(6, 2)`.
- **Stairs to 3F East (Southeastern Chamber):** Located at `(25, 14)` on 2F East. Warps directly between 2F Southeastern Chamber and 3F East `(25, 14)`.
- **Active Switch at `(2, 11)`:** Located on the Mewtwo statue on 2F West. Interacted facing UP from `(2, 12)` to toggle Mansion state.
- **Row 10 Corridor:** Open pink checkered floor corridor connecting 2F West to 2F East along Row 10.
- **Column 22 Rubble Barrier:** Continuous solid rubble barrier blocking horizontal passage along Column 22 on Rows 11-15.
- **Balcony Railing:** Row 16 at `(21, 16)` is a solid impassable balcony railing.

## State-Dependent Shutter Gates
- **Column 9 Gate at `(9, 4)` and `(9, 5)`:**
  - **State A:** OPEN (allowing passage along northern 2F West corridor).
  - **State B:** CLOSED (blocks passage).
- **Column 18 Gate at `(18, 8)` and `(19, 8)`:**
  - **State A:** CLOSED (blocks passage into 2F East corridor).
  - **State B:** OPEN (allows passage into 2F East corridor).

## Chamber Connectivity
- **2F West:** Contains stairs to 1F `(7, 10)`, stairs to 3F `(6, 1)`, and switch at `(2, 11)`.
- **2F East Northeast Pocket (Columns 24-28, Rows 1-7):** Dead end enclosed to the south by solid wall panels on Row 8 `(24-28, 8)` and rubble on Rows 6-7.
- **2F East Southwest Corridor (Columns 18-21, Rows 8-15):** Dead end blocked to the east by Column 22 rubble and south by Row 16 railing.
- **2F East Southeastern Chamber (Columns 23-28, Rows 9-16):** Contains stairs at `(25, 14)`. Inaccessible via walking on 2F in either state; only accessible via stairs from 3F East `(25, 14)`.
