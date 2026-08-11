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
- **Path Around the Pokémon Center:**
  - The Pokémon Center is located at columns 18-21, rows 22-27.
  - To go from behind the Pokémon Center (row 21) to its entrance (19, 27):
    - Walk Right to Column 24 (or walk Left to Column 1).
    - Walk Down along Column 1 to Row 32, then walk Right to Column 19 and Up to enter the Pokémon Center.

    - Note: Columns 22-23 on rows 22-25 are blocked by the roof of the adjacent house. Column 24 is blocked by a dead-end fence pocket at Row 28/29 on the south, so to go south to the Pokémon Center entrance, you MUST use Column 1 on the west and cross Row 32.

## Verified Physical Collisions
- Attempted Down from (22, 6) to (22, 7) (solid hedges, Fuchsia City, Turn 33071).
- Attempted Left from (26, 15) to (25, 15) (solid building wall, Fuchsia City, Turn 33086).
- Attempted Down from (26, 15) to (26, 16) (solid tree, Fuchsia City, Turn 33086).

- Attempted Right from (9, 32) to (10, 32) (solid diagonal ledge, Fuchsia City, Turn 33117).
- Attempted Up from (9, 32) to (9, 31) (solid horizontal ledge, Fuchsia City, Turn 33118).
- Attempted Left from (24, 27) to (23, 27) (solid fence/hedge, Fuchsia City, Turn 33166).
- Attempted Left from (24, 29) to (23, 29) (solid fence/hedge, Fuchsia City, Turn 33169).
- Attempted Left from (24, 30) to (23, 30) (solid fence/hedge, Fuchsia City, Turn 33171).
- Attempted Up from (36, 24) to (36, 23) (solid tree, Fuchsia City, Turn 33175).
- Attempted Up from (24, 16) to (24, 15) (solid fence post, Fuchsia City, Turn 33208).
- Verified properties:
  - Column 8 ledge gap at Row 31/32 allows the player to jump down from Row 31 to Row 32 to reach the western area.
  - Column 22 vertical corridor allows walking north/south between Row 21 and Row 14, bypassing the horizontal fence at Row 22.
- **Verified spatial boundaries (Turn 33355):**
  - Up movement from (24, 27) to (24, 26) is blocked by a solid building wall (the Warden's House).
  - Column 25 has solid fence posts at Rows 28 and 29.