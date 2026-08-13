# Fuchsia City - Overworld Layout & Points of Interest

## Map Transitions & Connections
- **East Connection (Route 15):** Transition at Fuchsia City `(39, 17)` connects directly to Route 15 `(0, 9)` on the western corridor (Player entered Fuchsia City on Turn 20389).
- **East Gatehouse (Route 15 Gate):** Located at rows 8-9, columns 8-12 on Route 15, with west exit at `(7, 9)`. Inside, the mat is at `(7, 5)` (east) and `(0, 5)` (west).
- **South Exit (Route 19 Connection):** Transition at Fuchsia City `(23, 35)` connects directly to Route 19 at `(13, 0)` (verified on Turn 20873).

## Physical Layout & Exploration
- **Regrowing Cut-able Bush (26, 13):** Crucial mechanic! This bush regrows immediately upon reloading the map or entering/exiting the Safari Zone. Always ensure TRUFFLE (Paras) is in the party to CUT it when navigating Column 26 down to row 14.
- **Continuous House Roof Obstruction (Rows 22-23, Columns 12-23):** This massive horizontal roof completely blocks north-south traversal in the center-west of Fuchsia City. To go from north-middle to south-middle, you must walk left all the way to Column 1 (which is completely open going down) or walk right to Column 24.
- **Overworld Cut-able Bush (26, 13):** This bush blocks the path going north along the left side of the Zoo pens. It was successfully CUT on Turn 21624 using TRUFFLE (Paras), making the vertical path on Column 26 fully walkable.
- The eastern part of Fuchsia City has a Zoo/Safari Zone area with walled pens (bordered by grey Rhydon statues).
- Columns 18-22 on Rows 22-23 form the roof of a house.
- Column 23 has a walkable paved corridor running from Row 17 to Row 31 connecting the east and west sides.
- Row 33 has a horizontal row of grey Rhydon statues (columns 24-35).
- Row 34 has trees blocking southern movement at columns 30-35.
- Column 2 has a solid vertical wall/fence running from Row 24 to Row 31, dividing the western Gym area from the eastern center. Bypassed by walking south to Row 32.

## Landmarks & Points of Interest
- **Pokémon Center:** Located in the southeast quadrant. Verified entrance door is at `(19, 27)`. Inside, entrance mat is at `(3, 7)` and Nurse Joy is at `(3, 2)`.
- **Fuchsia City Gym:** Located in the southwest quadrant at columns 4-6, rows 26-27. Verified entrance door is at `(5, 27)` facing south. Gym signpost is at `(5, 29)`.
- **Poké Mart:** Entrance door is at `(11, 27)` (verified on Turn 20864). Inside, the entrance mat is at `(2, 7)`, and the clerk is behind the counter at `(2, 3)`.
- **Warden's House:** Located in the southeast at `(27, 27)` (verified on Turn 20885). Inside, Warden resides and speaks in gibberish until his Gold Teeth are returned.
- **Regular House (Slowpoke Fan):** Entrance at `(22, 13)` (verified on Turn 20903). The resident inside says: "We nicknamed the WARDEN SLOWPOKE. He and SLOWPOKE both look vacant!"
- **Safari Zone Gatehouse:** Located at columns 18-21, rows 0-3 on Fuchsia City map. The verified entrance door is at `(18, 3)` facing south.
- **Verified Northern Route to Safari Gatehouse:** Walk Up along Column 24 to Row 21, walk Left to Column 22 on Row 21/20, walk Up along Column 22 to Row 14, walk Right along Row 14 to Column 26, walk Up along Column 26 (through cut bush at 26,13) to Row 9, walk Left to Column 19 on Row 9, walk Up along Column 19 to Row 8, walk Right along Row 8/9 to Column 37, walk Up along Column 37 to Row 2, walk Left along Row 2 to Column 22, walk Down to Row 4, and Up to enter the Gatehouse at (22, 3) or (18, 3).

## Spatial Layout Clarifications & Routing
- **Row 31 Walkability:** Row 31 is NOT a solid horizontal ledge on Columns 1-9. It is fully walkable going UP (and Down). It is merely a decorative border tile of the path, not an impassable cliff ledge.
- **Path Around the Pokémon Center (Corrected):**
  - The Pokémon Center is located at columns 18-21, rows 22-27 with the entrance door at `(19, 27)`.
  - The hypothesized route via Column 1 and Row 32 is BLOCKED because the Slowpoke pen on Row 32 (Columns 10-14) is impassable.
  - **Actual Verified Path to Pokémon Center from North:**
    - From the northern zoo/path area, walk to Column 24 (or Column 22/23 corridor) and walk DOWN to Row 21.
    - From `(24, 21)`, walk DOWN Column 24 to `(24, 28)`. Column 24 is completely open and free of fence blockages down to Row 28.
    - From `(24, 28)`, walk LEFT horizontally along Row 28 to `(19, 28)`.
    - Walk UP from `(19, 28)` to `(19, 27)` to enter the Pokémon Center.

## Verified Physical Collisions
- Verified properties:
  - Column 8 ledge gap at Row 31/32 allows the player to jump down from Row 31 to Row 32 to reach the western area.
  - Column 22 vertical corridor allows walking north/south between Row 21 and Row 14, bypassing the horizontal fence at Row 22.
- **Verified spatial boundaries (Turn 33355):**
  - Up movement from (24, 27) to (24, 26) is blocked by a solid building wall (the Warden's House).
  - Column 25 has solid fence posts at Rows 28 and 29.
## 🧪 Verified Northern Fuchsia City Collisions (Turns 34554 - 34559)
- **Column 17 and Column 14 (Rows 6-12):** Continuous solid overworld tree walls that block horizontal ground traversal on the north side of Fuchsia City.
- **Row 7 Barrier:** A continuous solid pine tree wall running horizontally from Column 13 to Column 35, completely blocking direct vertical traversal from the south to the northern corridor (Row 2).
- **Column 37 Passage:** The ONLY walkable vertical gap in the Row 7 tree barrier, allowing players to walk UP from Row 8/9 to Row 2 to reach the northernmost corridor.
- **Safari Gatehouse Roof/Wall Block (Rows 3-7, Columns 16-21):** Completely solid structure, preventing direct northern passage on Column 18 from Row 8. Players must detour east to Column 37, walk up to Row 2, walk left to Column 22, and then walk down to enter.
## Newly Verified Physical Barriers & walkable corridors (Turns 36315-36329)
- **Column 18 Row 7 Tree Wall:** Solid overworld tree at `(18, 7)`, blocking downward traversal on Column 18 from Row 6 (Turn 36315).
- **Row 16 Tree Barrier (Columns 27-35):** Solid horizontal line of trees running across Columns 27-35 on Row 16, blocking direct vertical ground crossing (Turn 36325).
- **Column 22/23 Corridor:** Completely open and walkable vertical corridor on Columns 22 and 23 from Row 14 down to Row 21, connecting the north-middle area to the south-middle area (Turn 36328).
- **Row 22 South-Facing Ledge (Column 23):** South-facing one-way ledge at Column 23 Row 22. Walking DOWN jumps over the ledge to Row 23, but walking UP is blocked (Turn 36329).

## Newly Verified Collisions & Barriers (Turn 36482)
- **Row 29 Horizontal Fence (Columns 25-29):** A solid horizontal fence running across Columns 25-29 on Row 29, blocking vertical ground crossing.
- **Column 27 Row 29 Solid Signpost:** A solid 2-tile high signpost located at `(27, 29)`, which blocks passage.
- **Column 30 Row 14 Wandering NPC:** A wandering NPC who can block traversal on Column 30 Row 14.
- **Column 16 Row 31/32 Walkable Ledge Gap:** Column 16 Row 31/32 contains a fully walkable gap in the south-facing ledge going UP (and Down). This allows players below the ledge in the southern area to walk UP to Row 31, Row 30, and Row 28, and return to the main/northern areas of Fuchsia City safely without being stuck.