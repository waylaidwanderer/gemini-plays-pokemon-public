# Pokémon Mansion 2F - Map & Navigation Log

## Physical Layout & Walkable Areas
- **Stairs to 1F West:** Located at `(7, 10)`. Landing from 1F West places the player at `(7, 11)`.
- **Stairs to 3F West:** Located at `(6, 1)`.
- **Stairs to 3F East:** Located at `(25, 14)` in the Southeastern Chamber.
- **Southeastern Chamber:** Bounded by Column 22 rubble and Row 16 railing. Landing from `(25, 14)` enters this room.

## Mewtwo Statue Switches & Shutter Gates
- **2F West Mewtwo Switch:** Located at `(2, 11)`. Interacting from `(2, 12)` facing UP toggles between State A and State B (confirmed Turn 73065, Turn 74302).
- **2F West Shutter Gates (Columns 9-10, Rows 4-5):**
  - Shutter gate at `(9, 4)` and `(9, 5)` is **OPEN** in State A, **CLOSED** in State B.
- **2F East Shutter Gate (Columns 18-19, Row 8):**
  - Shutter gate at `(18, 8)` / `(19, 8)` is **CLOSED** in State A, **OPEN** in State B (verified Turn 73513).
- **Balcony Railing:** Row 16 at `(21, 16)` is a solid impassable railing (verified Turn 74249).

## Empirical Landings & Pitfall Warps
- **Landing from 3F East Pitfall `(19, 14)` (Verified Turn 74244):** Player lands at `(18, 14)` on 2F East Southwest Corridor. From here, open pink floor extends north along Column 19/20 up to Row 10 corridor, and west towards 1F stairs.
- **Landing from 3F East Pitfall `(17, 14)` (Verified Turn 74402):** Player lands at `(16, 14)` in the 2F Balcony Chamber.

## 2F Balcony Chamber (Verified Ground Truth)
- **Scientist Trainer at `(17, 17)`:** Defeated on Turn 74424 (Electrode Lv 29, Weezing Lv 29; awarded ¥1450).
- **Balcony Barriers (Rows 18-19 and 22-23):** Green hedges at `(14-19, 18)` & `(14-19, 22)`, gold balustrades/urns at `(14-19, 19)` & `(14-19, 23)`.
- **Corridors:** Open pink checkered corridors on Columns 12-13 and Columns 20-23 bypass the barriers to the south.
- **Item Ball at `(18, 21)`:** Located in the corridor between the hedge rows.

- **2F-3F Balcony Chamber Staircase Pair (Verified Turn 74442 & 74451):** Tile `(21, 23)` on 2F is an ascending staircase warping to `(23, 22)` on 3F East. Tile `(23, 22)` on 3F East descends directly back to `(21, 23)` on 2F (player lands at `(21, 24)`).